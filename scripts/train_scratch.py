# Author : NavinKumarMNK
"""Training script"""

import torch
import torch.nn as nn
import yaml
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

from model import Transformer
from tokenizer import BPETokenizer
from dataset import Seq2SeqDataLoader
from preprocessing import load_corpus
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

SEED = 42
torch.manual_seed(seed=SEED)
torch.cuda.manual_seed_all(seed=SEED)
torch.backends.cudnn.deterministic = True


if __name__ == '__main__':
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    
    train_config = config['train']
    model_config = config['model']
    token_config = config['tokenizer']
    data_config = config['data']
    
    # Preprocessing Dataset
    corpus = load_corpus(data_config)
    corpus.to_parquet(data_config['dataset_path'])
    print("Corpus Preprocessed and saved to ", data_config['dataset_path'])
    
    # Tokenizer setup
    # df = pd.read_parquet(token_config['dataset_path'])
    src_bool = True
    for items in (token_config['src'], token_config['tgt']):
        _df = corpus[items['lang']]

        bpe_tokenizer = BPETokenizer(items)
        bpe_tokenizer.train(_df)
        print("Size of vocabulary:", bpe_tokenizer.tokenizer.get_vocab_size())
        if src_bool:
            tokenizer_src = bpe_tokenizer.tokenizer
            src_bool = False
        else:
            tokenizer_tgt = bpe_tokenizer.tokenizer

    print("Successfully trained Tokenizers")

    '''
    from tokenizers import Tokenizer
    tokenizer_src: BPETokenizer = Tokenizer.from_file(token_config['src']['tokenizer_path'])
    tokenizer_tgt: BPETokenizer = Tokenizer.from_file(token_config['tgt']['tokenizer_path'])
    '''

    # Dataset setup
    dataset = Seq2SeqDataLoader(
        df=pd.read_parquet(train_config['dataset_path']),
        tokenizer_src=train_config['tokenizer']['src']['path'],
        tokenizer_tgt=train_config['tokenizer']['tgt']['path'],
        src_lang=train_config['tokenizer']['src']['lang'],
        tgt_lang=train_config['tokenizer']['tgt']['lang'],
        src_seq_len=train_config['tokenizer']['src']['seq_len'],
        tgt_seq_len=train_config['tokenizer']['tgt']['seq_len'],
        batch_size=train_config['batch_size'],
        num_workers=train_config['num_workers'],
        split_size=train_config['split_size']
    )
    dataset.setup()
    print("Dataset setup complete")
    
    train_loader = dataset.train_dataloader()
    val_loader = dataset.val_dataloader()

    # device settings for training
    device = train_config['device'] 
    if device == 'cuda':
        if not torch.cuda.is_available():
            print("Device set to cuda but cuda is not available. Using CPU")
            device = 'cpu'
    
    # model setup
    model = Transformer(**model_config["parameters"])
    optimizer = torch.optim.Adam(
        params=model.parameters(), **train_config['optimizer'])
    
    # label smooting = True;
    loss_fn = nn.CrossEntropyLoss(
        ignore_index=1, # ignore padding token
        label_smoothing=train_config['label_smoothing'],
    ).to(device)
    
    print(model)

    # tensorboard logging
    writer = SummaryWriter(log_dir=train_config['logging']['dir'])
    
    model.to(device)
    model.half()
    print(f"Training on: {device}")

    if train_config['fine_tune']:
        model = torch.load(model_config['path'])
    
    # Custom training Loop
    try:    
        for epoch in range(train_config['epochs']):
            # training loop
            model.train()
            total_train_loss = 0
            train_bar = tqdm(train_loader, desc=f"Training epoch {epoch:02d}")
            for i, batch in enumerate(train_bar):
                encoder_input = batch['encoder_input'].to(device) # (batch_size, seq_len)
                decoder_input = batch['decoder_input'].to(device) # (batch_size, seq_len)
                encoder_mask = batch['encoder_mask'].to(device) # (batch_size, 1, 1, seq_len)
                decoder_mask = batch['decoder_mask'].to(device) # (batch_size, 1, seq_len, seq_len)
                label = batch['label'].to(device) # (batch_size, seq_len)

                # forward pass
                output = model(src=encoder_input, tgt=decoder_input,
                            src_mask=encoder_mask, tgt_mask=decoder_mask)
                
                # loss calculation
                loss = loss_fn(output.view(-1, tokenizer_tgt.get_vocab_size()), label.view(-1))
                print(loss)
                total_train_loss += loss.item()
                
                # backward pass
                loss.backward()
                optimizer.step()
                optimizer.zero_grad()

                # update tqdm bar
                train_bar.set_postfix({'train_loss': total_train_loss/(i+1)})

            # validation loop
            model.eval()
            total_val_loss = 0
            val_bar = tqdm(val_loader, desc=f"Validation epoch {epoch:02d}")
            with torch.no_grad():
                for i, batch in enumerate(val_bar):
                    if batch.shape[0] != train_config['batch_size']:
                        continue

                    encoder_input = batch['encoder_input'].to(device) # (batch_size, seq_len)
                    decoder_input = batch['decoder_input'].to(device) # (batch_size, seq_len)
                    encoder_mask = batch['encoder_mask'].to(device) # (batch_size, 1, 1, seq_len)
                    decoder_mask = batch['decoder_mask'].to(device) # (batch_size, 1, seq_len, seq_len)
                    label = batch['label'].to(device) # (batch_size, seq_len)

                    # forward pass
                    output = model(src=encoder_input, tgt=decoder_input,
                                src_mask=encoder_mask, tgt_mask=decoder_mask)
                    
                    # loss calculation
                    loss = loss_fn(output.view(-1, tokenizer_tgt.get_vocab_size()), label.view(-1))
                    total_val_loss += loss.item()

                    # update tqdm bar
                    val_bar.set_postfix({'valid_loss': total_val_loss/(i+1)})
    except KeyboardInterrupt:        
        # Save model
        torch.save(model, config['model']['path']+f"epoch_{epoch}.pt")
    