# Author : NavinKumarMNK
"""Training script"""

import torch
import pyaml as yaml
import pandas as pd
import tqdm

from sklearn.model_selection import train_test_split
from .model import Transformer
from .tokenizer import BPETokenizer
from .dataset import TransformerDataset
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

SEED = 42
torch.manual_seed(seed=SEED)
torch.cuda.manual_seed_all(seed=SEED)
torch.backends.cudnn.deterministic = True

CONFIG = {
    'tokenizer_path': 'tokenizer/tokenizer-{}.json',
    'vocab_path': 'tokenizer/vocab-{}.json',
}

if __name__ == '__main__':
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    
    dataset = pd.read_csv(config['dataset_path'])


    tokenizer_src = BPETokenizer(config['tokenizer']['src'])
    tokenizer_tgt = BPETokenizer(config['tokenizer']['tgt'])

    tokenizer_src.train(dataset)
    tokenizer_tgt.train(dataset)
    
    # Inspecting Tokenizers
    print(f"Vocab size of source language: {tokenizer_src.vocab_size}")
    print(f"Vocab size of target language: {tokenizer_tgt.vocab_size}")
    config['model']['parameters']['src_vocab_size'] = tokenizer_src.vocab_size
    config['model']['parameters']['tgt_vocab_size'] = tokenizer_tgt.vocab_size

    # modify the config.yaml file with the vocab size
    with open("config.yaml", "w") as f:
        yaml.dump(config, f)

    # customize manually for better and robust training
    train_dataset, val_dataset = train_test_split(
        dataset, test_size=0.2, random_state=SEED
    )

    train_dataset = TransformerDataset(
        df=dataset, 
        tokenizer_src=tokenizer_src,
        tokenizer_tgt=tokenizer_tgt, 
        src_lang=config['tokenizer']['src']['lang'],
        tgt_lang=config['tokenizer']['tgt']['lang'],
        seq_len=config['model']['parmaters']['seq_len'])
    
    val_dataset = TransformerDataset(
        df=dataset, 
        tokenizer_src=tokenizer_src,
        tokenizer_tgt=tokenizer_tgt, 
        src_lang=config['tokenizer']['src']['lang'],
        tgt_lang=config['tokenizer']['tgt']['lang'],
        seq_len=config['model']['parmaters']['seq_len'])
    
    train_loader = DataLoader(train_dataset, batch_size=config['train']['batch_size'], shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=config['train']['batch_size'], shuffle=False)

    model = Transformer(**config["model"]["parameters"])
    optimzer = torch.optim.Adam(
        params=model.parameters(), lr=config['train']['lr'])
    print(model)

    # tensorboard logging
    writer = SummaryWriter(log_dir=config['train']['log']['dir'])

    device = config['train']['device'] 
    if device == 'cuda':
        if not torch.cuda.is_available():
            print("Device set to cuda but cuda is not available. Using CPU")
            device = 'cpu'
    
    model.to(device)
    print(f"Training on: {device}")

    if config['train']['fine_tune']:
        model.load_state_dict(torch.load(config['model']['path']))
        
    
    # training loop
    for epoch in range(config['train']['epochs']):


        
