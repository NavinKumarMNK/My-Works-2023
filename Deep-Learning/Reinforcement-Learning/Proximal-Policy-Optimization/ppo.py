import os 
import numpy as np
import torch
from typing import Dict, Tuple
from abc import ABC, abstractmethod
from tqdm import tqdm

__DEVICE__ = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

class PPOMemory:
    def __init__(self, batch_size: int):
        self.states = []  # stores states
        self.probs = []  # stores probabilities of actions taken
        self.actions = []  # actions taken
        self.vals = []  # values that critic calculates
        self.rewards = []  # rewards given by environment
        self.dones = []  # Terminal Flags
        
        self.batch_size = batch_size
        
    def generate_batches(self) -> Dict:
        n_states = len(self.states)
        batch_start = np.arange(0, n_states, self.batch_size)
        indices = np.arange(n_states, dtype=np.int64)  # indices of states (for sampling)
        np.random.shuffle(indices)
        batches = [indices[i:i+self.batch_size] for i in batch_start]  # batches of indices
        
        return {
            "states": np.array(self.states),
            "actions": np.array(self.actions),
            "probs": np.array(self.probs),
            "vals": np.array(self.vals),
            "rewards": np.array(self.rewards),
            "dones": np.array(self.dones),
            "batches": batches
        }
    
    def store_memory(self, state, action, probs, vals, reward, done):
        self.states.append(state)
        self.actions.append(action)
        self.probs.append(probs)
        self.vals.append(vals)
        self.rewards.append(reward)
        self.dones.append(done)
    
    def clear_memory(self):
        self.states = []
        self.probs = []
        self.actions = []
        self.vals = []
        self.rewards = []
        self.dones = []

class BaseNetwork(ABC, torch.nn.Module):
    def __init__(self, input_dim, output_dim:int, alpha:float, ckpt_file:str):
        super(BaseNetwork, self).__init__()
        
        self.ckpt_file = ckpt_file
        self.network = torch.nn.Sequential(
            torch.nn.Linear(*input_dim, 256),
            torch.nn.ReLU(),
            torch.nn.Linear(256, 256),
            torch.nn.ReLU(),
            torch.nn.Linear(256, output_dim)
        )
        
        self.optimizer = torch.optim.Adam(
            self.parameters(), lr=alpha, eps=1e-5
        )
        
        self.to(__DEVICE__)  # for gpu computation

    @abstractmethod
    def forward(self, state: torch.Tensor):
        pass

    def save_checkpoint(self):
        torch.save(self.state_dict(), self.ckpt_file)
        
    def load_checkpoint(self):
        self.load_state_dict(torch.load(self.ckpt_file))


class ActorNetwork(BaseNetwork):
    def __init__(self, n_actions, input_dim:int, alpha:float, ckpt_dir:str='tmp/ppo'):
        super(ActorNetwork, self).__init__(
            *input_dim, n_actions, alpha, os.path.join(ckpt_dir, 'actor_torch_ppo')
        )
        self.network.add_module('Softmax', torch.nn.Softmax(dim=-1))

    def forward(self, state: torch.Tensor) -> torch.distributions.Categorical:
        dist_probs = self.network(state)
        dist = torch.distributions.Categorical(dist_probs)
        return dist


class CriticNetwork(BaseNetwork):
    def __init__(self, input_dim, alpha:float, ckpt_dir:str='tmp/ppo'):
        super(CriticNetwork, self).__init__(
            *input_dim, 1, alpha, os.path.join(ckpt_dir, 'critic_torch_ppo')
        )

    def forward(self, state: torch.Tensor) -> torch.Tensor:
        value = self.network(state)
        return value

class Agent:
    def __init__(self, n_actions, gamma=0.99, alpha=3e-4, 
                 policy_clip=0.2, batch_size=64, N=2048,
                 n_epochs=10, gae_lambda=0.95, entropy_beta=0.01):
        
        locals_ = locals()
        self.__dict__.update({
            k: locals_[k] for k in locals_ if k != 'self'
        })
        
        self.actor = ActorNetwork(n_actions, 33, alpha)
        self.critic = CriticNetwork(33, alpha)
        self.memory = PPOMemory(batch_size)
        
    def remember(self, state, action, probs, vals, reward, done):
        self.memory.store_memory(state, action, probs, vals, reward, done)
   
    def save_models(self):
        print('... saving models ...')
        self.actor.save_checkpoint()
        self.critic.save_checkpoint()
    
    def load_models(self):
        print('... loading models ...')
        self.actor.load_checkpoint()
        self.critic.load_checkpoint()
        
    def choose_action(self, observation) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        state = torch.Tensor([observation], dtype=torch.float).to(__DEVICE__)
        
        dist = self.actor(state)
        value = self.critic(state)
        action = dist.sample()
        
        probs = torch.squeeze(dist.log_prob(action)).item()
        action = torch.squeeze(action).item()
        value = torch.squeeze(value).item()
        
        return (action, probs, value)
    
    def learn(self):
        for _ in tqdm(range(self.n_epochs)):
            (states, actions, old_probs, 
             values, rewards, dones, batches) = self.memory.generate_batches().values()
            
            
            """
            A(t) = R(t) + gamma*lmabda*V(t+1) + ... + (gamma*lambda)**(T-t+1)*R(T-1)
            where R(t) = r(t) + gamma*V(s(st+1)) - V(st)
            """
            advantage = np.zeros(len(rewards), dtype=np.float32) 
            for t in range(len(rewards)-1): # calculate advantage
                discount = 1
                a_t = 0 
                for k in range(t, len(rewards)-1):
                    # value of terminal state is 0 because it has no future reward
                    a_t += discount*(rewards[k] + self.gamma*values[k+1]
                                     * (1-int(dones[k])) - values[k])
                    discount *= self.gamma*self.gae_lambda
                advantage[t] = a_t
            advantage = torch.Tensor(advantage).to(__DEVICE__)
            
            values = torch.Tensor(values).to(__DEVICE__)
            for batch in batches:
                states = torch.Tensor(states[batch], device=torch.float).to(__DEVICE__)
                old_probs = torch.Tensor(old_probs[batch], device=torch.float).to(__DEVICE__)
                actions = torch.Tensor(actions[batch], device=torch.float).to(__DEVICE__)
                
                dist: torch.distributions.Categorical = self.actor(states)
                critic_value = self.critic(states)
                
                critic_value = torch.squeeze(critic_value) 
                new_probs = dist.log_prob(actions)
                prob_ratio = (new_probs-old_probs).exp()
                weighted_probs = advantage[batch] * prob_ratio
                weighted_clipped_probs = torch.clamp(
                    prob_ratio, 1-self.policy_clip, 1+self.policy_clip
                )*advantage[batch]
                
                # loss
                actor_loss = -torch.min(weighted_probs, weighted_clipped_probs).mean()  # gradient ascent
                returns = advantage[batch] + values[batch]
                critic_loss = (returns-critic_value)**2
                critic_loss = critic_loss.mean()
                total_loss = actor_loss + 0.5*critic_loss - self.entropy_beta*dist.entropy().mean()

                # backprop
                self.actor.optimizer.zero_grad()
                self.critic.optimizer.zero_grad()
                total_loss.backward()
                self.actor.optimizer.step()
                self.critic.optimizer.step()
            
            self.memory.clear_memory()   
                

