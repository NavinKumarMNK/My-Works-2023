import gym
import numpy as np
import matplotlib.pyplot as plt
import torch

from ppo import Agent
from tqdm import tqdm

def plot_learning_curve(x, scores, figure_file):
    running_avg = np.zeros(len(scores))
    for i in range(len(running_avg)):
        running_avg[i] = np.mean(scores[max(0, i-100):(i+1)])
    plt.plot(x, running_avg)
    plt.title('Running average of previous 100 scores')
    plt.savefig(figure_file)

if __name__ == '__main__':
    torch.set_default_device('cuda' if torch.cuda.is_available() else 'cpu')
    torch.random.manual_seed(42)
    np.random.seed(42)
    env = gym.make("CartPole-v1")
    N = 20
    batch_size = 5
    n_epochs = 4
    alpha = 3e-4
    n_games = 300
    
    agent = Agent(
        input_dims=env.observation_space.shape,
        n_actions=env.action_space.n,
        gamma=0.99,
        alpha=alpha,
        policy_clip=0.2,
        batch_size=batch_size,
        N=N,
        n_epochs=n_epochs,
        gae_lambda=0.95,
        entropy_beta=0.01
    )
    
    fig_file = f'plots/ppo_{n_games}_games.png'
    best_score = env.reward_range[0]
    score_history = []
    learn_iters = 0
    avg_score = 0
    n_steps = 0
    
    pbar = tqdm(total=n_games, desc='Episode', position=0, leave=True)
    for i in range(n_games):
        observation, _ = env.reset()
        done = False
        score = 0
        
        while not done:
            action, prob, val = agent.choose_action(observation)
            a = env.step(action)
            _observation, reward, done, info, _ = env.step(action)
            n_steps += 1
            score += reward
            agent.remember(observation, action, prob, val, reward, done)
            if n_steps % N == 0:
                agent.learn()
                learn_iters += 1
            observation = _observation
        score_history.append(score)
        
        if avg_score > best_score:
            best_score = avg_score
            agent.save_models()
        
        avg_score = np.mean(score_history[-100:])
        
        pbar.set_postfix({'Episode': i+1, 'Score': score, 'Avg Score': avg_score, 'Time Steps': n_steps, 'Learning Steps': learn_iters}, refresh=True)
        pbar.update()

    x = [i+1 for i in range(n_games)]
    plot_learning_curve(x, score_history, fig_file)


    