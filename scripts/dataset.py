import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import yaml
import pandas as pd
import lightning.pytorch as pl
from tokenizers import Tokenizer
from sklearn.model_selection import train_test_split

class Seq2SeqDataset(Dataset):
    def __init__(self, df: pd.DataFrame, tokenizer_src: str, tokenizer_tgt: str, src_lang: str, 
                 tgt_lang: str, src_seq_len: int, tgt_seq_len: int ) -> None:
        super().__init__()
        
        self.df = df
        self.tokenizer_src = tokenizer_src
        self.tokenizer_tgt = tokenizer_tgt
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang
        self.src_seq_len = src_seq_len
        self.tgt_seq_len = tgt_seq_len

        self.tokenizer_src: Tokenizer = Tokenizer.from_file(self.tokenizer_src)
        self.tokenizer_tgt: Tokenizer = Tokenizer.from_file(self.tokenizer_tgt)

        self.sos_token_src = self.sos_token_tgt = torch.tensor([0], dtype=torch.int64)
        self.pad_token_src = self.pad_token_tgt = torch.tensor([1], dtype=torch.int64)
        self.eos_token_src = self.eos_token_tgt = torch.tensor([2], dtype=torch.int64)
        self.mask_token_src = torch.tensor([self.tokenizer_src.get_vocab_size() - 1], dtype=torch.int64)  
        self.mask_token_tgt = torch.tensor([self.tokenizer_tgt.get_vocab_size() - 1], dtype=torch.int64) 

    def __len__(self) -> int:
        return len(self.df)
    
    def __getitem__(self, idx: int) -> dict:
        # support for only DataFrame pair
        src_text, tgt_text = self.df.iloc[idx][self.src_lang], self.df.iloc[idx][self.tgt_lang]
        src_input_ids, tgt_input_ids = self.tokenizer_src.encode(src_text).ids, self.tokenizer_tgt.encode(tgt_text).ids
        src_pad_len, tgt_pad_len = self.src_seq_len - len(src_input_ids) - 2, \
            self.tgt_seq_len - len(tgt_input_ids) - 1 # -2 for sos and eos token & -1 for sos token

        if src_pad_len < 0 or tgt_pad_len < 0:
            src_input_ids, tgt_input_ids = src_input_ids[:self.src_seq_len-2], \
                tgt_input_ids[:self.tgt_seq_len-1]
            src_pad_len, tgt_pad_len = 0, 0
        
        src_input_ids, tgt_input_ids = torch.tensor(src_input_ids, dtype=torch.int64), \
            torch.tensor(tgt_input_ids, dtype=torch.int64)
         
        # concatenating sos, eos and pad tokens
        src_input_ids = torch.cat(
            [self.sos_token_src, src_input_ids, self.eos_token_src, self.pad_token_src.repeat(src_pad_len)])
        label = torch.cat(
            [tgt_input_ids, self.eos_token_tgt, self.pad_token_tgt.repeat(tgt_pad_len)])
        tgt_input_ids = torch.cat(
            [self.sos_token_tgt, tgt_input_ids, self.pad_token_tgt.repeat(tgt_pad_len)])
        
        # attention mask in encoder is 1 for all non-pad tokens and 0 for pad tokens
        attention_mask_src = (src_input_ids != self.pad_token_src).int()
        # casual attention mask in decoder is 1 for previous tokens and 0 for future tokens
        casual_attention_mask_tgt = torch.triu(
            torch.ones((self.tgt_seq_len, self.tgt_seq_len), dtype=torch.int64), diagonal=1
        )
        
        return {
            "encoder_input": src_input_ids, # (seq_len,)
            "decoder_input": tgt_input_ids, # (seq_len,)
            "encoder_mask": attention_mask_src.unsqueeze(0).unsqueeze(0), # (seq_len,)
            "decoder_mask": casual_attention_mask_tgt.unsqueeze(0), # (seq_len, seq_len)
            "label" : label # (seq_len,)
        }

        
class Seq2SeqDataLoader(pl.LightningDataModule):
    def __init__(self, df: pd.DataFrame, tokenizer_src: str, tokenizer_tgt: str, 
                 src_lang: str, tgt_lang: str, src_seq_len: int, tgt_seq_len: int, 
                 batch_size: int, num_workers: int, split_size:int) -> None:
        super().__init__()
        
        self.df = df
        self.tokenizer_src = tokenizer_src
        self.tokenizer_tgt = tokenizer_tgt
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang
        self.src_seq_len = src_seq_len
        self.tgt_seq_len = tgt_seq_len
        self.batch_size = batch_size
        self.num_workers = num_workers
        self.split_size = split_size

    def setup(self, stage: str = None):
        self.train_df, self.val_df = train_test_split(
            self.df, test_size=self.split_size, random_state=42
        )
        self.train_dataset = Seq2SeqDataset(
            df=self.train_df, 
            tokenizer_src=self.tokenizer_src,
            tokenizer_tgt=self.tokenizer_tgt, 
            src_lang=self.src_lang,
            tgt_lang=self.tgt_lang,
            src_seq_len=self.src_seq_len,
            tgt_seq_len=self.tgt_seq_len)
        
        self.val_dataset = Seq2SeqDataset(
            df=self.val_df, 
            tokenizer_src=self.tokenizer_src,
            tokenizer_tgt=self.tokenizer_tgt, 
            src_lang=self.src_lang,
            tgt_lang=self.tgt_lang,
            src_seq_len=self.src_seq_len,
            tgt_seq_len=self.tgt_seq_len)

        print(len(self.train_dataset), len(self.val_dataset))
        
    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=True, num_workers=self.num_workers)
    
    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.batch_size, shuffle=False, num_workers=self.num_workers)
        
if __name__ == '__main__':
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    config = config['train']
    dataset = Seq2SeqDataLoader(
        df=pd.read_parquet(config['dataset_path']),
        tokenizer_src=config['tokenizer']['src']['path'],
        tokenizer_tgt=config['tokenizer']['tgt']['path'],
        src_lang=config['tokenizer']['src']['lang'],
        tgt_lang=config['tokenizer']['tgt']['lang'],
        src_seq_len=config['tokenizer']['src']['seq_len'],
        tgt_seq_len=config['tokenizer']['tgt']['seq_len'],
        batch_size=config['batch_size'],
        num_workers=config['num_workers'],
        split_size=config['split_size']
    )
    dataset.setup()
    print("Dataset setup complete")
    
    for batch in dataset.train_dataloader():
        print(batch)
        break
