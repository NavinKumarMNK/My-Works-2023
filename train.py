# Author : NavinKumarMNK
"""Training script"""

import torch
import torch.nn as nn
import yaml
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from .model import Transformer
from .tokenizer import BPETokenizer
from .dataset import TransformerDataset
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm


SEED = 42
torch.manual_seed(seed=SEED)
torch.cuda.manual_seed_all(seed=SEED)
torch.backends.cudnn.deterministic = True

if __name__ == '__main__':
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    
    dataset = pd.read_csv(config['dataset_path'])


    tokenizer_src = BPETokenizer()
    tokenizer_tgt = BPETokenizer()

    tokenizer_src.train(dataset, config['tokenizer']['src'])
    tokenizer_tgt.train(dataset, config['tokenizer']['tgt'])
    
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

    # device settings for training
    device = config['train']['device'] 
    if device == 'cuda':
        if not torch.cuda.is_available():
            print("Device set to cuda but cuda is not available. Using CPU")
            device = 'cpu'
    

    model = Transformer(**config["model"]["parameters"])
    optimzer = torch.optim.Adam(
        params=model.parameters(), **config['train']['optimizer'])
    # label smooting = True;
    loss_fn = nn.CrossEntropyLoss(
        ignore_index=tokenizer_tgt.token_to_id("[PAD]"),
        label_smoothing=config['train']['label_smoothing'],
    ).to(device)
    
    print(model)

    # tensorboard logging
    writer = SummaryWriter(log_dir=config['train']['log']['dir'])
    
    model.to(device)
    print(f"Training on: {device}")

    if config['train']['fine_tune']:
        model.load_state_dict(torch.load(config['model']['path']))
            
    for epoch in tqdm(range(config['train']['epochs']), desc="Epochs"):
        # training loop
        model.train()
        for batch in tqdm(train_loader, desc=f"Training epoch {epoch:02d}"):
            encoder_input = batch['encoder_input'].to(device) # (batch_size, seq_len)
            decoder_input = batch['decoder_input'].to(device) # (batch_size, seq_len)
            encoder_mask = batch['encoder_mask'].to(device) # (batch_size, 1, 1, seq_len)
            decoder_mask = batch['decoder_mask'].to(device) # (batch_size, 1, seq_len, seq_len)

            # forward pass
            encoder_output = model.encoder(
                src=encoder_input, scr_mask=encoder_mask) # (batch_size, seq_len, d_model)
            decoder_output = model.decoder(
                tgt=decoder_input, tgt_mask=decoder_mask, 
                src_output=encoder_output, src_mask=encoder_mask) # (batch_size, seq_len, d_model)

            label = decoder_input[:, 1:].contiguous() # (batch_size, seq_len)
            output = model.project(decoder_output) # (batch_size, seq_len, tgt_vocab_size)

            # loss calculation
            loss = loss_fn(output.view(-1, tokenizer_tgt.vocab_size), label.view(-1))
            writer.add_scalar("Loss/train", loss.item(), epoch)
            writer.flush()

            # set postfix for tqdm
            postfix = {
                "train_loss": loss.item(),
            }
            tqdm.set_postfix(postfix, refresh=True)
            
            # backward pass
            loss.backward()
            optimzer.step()
            optimzer.zero_grad()
        
        # validation loop
        model.eval()
        with torch.no_grad():
            for batch in tqdm(val_loader, desc=f"Validation epoch {epoch:02d}"):
                if batch.shape[0] != config['train']['batch_size']:
                    continue

                encoder_input = batch['encoder_input'].to(device) # (batch_size, seq_len)
                decoder_input = batch['decoder_input'].to(device) # (batch_size, seq_len)
                encoder_mask = batch['encoder_mask'].to(device) # (batch_size, 1, 1, seq_len)
                decoder_mask = batch['decoder_mask'].to(device) # (batch_size, 1, seq_len, seq_len)
                label = batch['label'].to(device) # (batch_size, seq_len)

                # forward pass
                encoder_output = model.encoder(
                    src=encoder_input, scr_mask=encoder_mask) # (batch_size, seq_len, d_model)
                decoder_output = model.decoder(
                    tgt=decoder_input, tgt_mask=decoder_mask, 
                    src_output=encoder_output, src_mask=encoder_mask) # (batch_size, seq_len, d_model)

                output = model.project(decoder_output) # (batch_size, seq_len, tgt_vocab_size)

                # loss calculation
                loss = loss_fn(output.view(-1, tokenizer_tgt.vocab_size), label.view(-1))
                writer.add_scalar("Loss/val", loss.item(), epoch)
                writer.flush()

                # set postfix for tqdm
                postfix = {
                    "valid_loss": loss.item(),
                }
                tqdm.set_postfix(postfix, refresh=True)
   
        # Save model
        torch.save(model.state_dict(), config['model']['path']+f"epoch_{epoch}.pt")