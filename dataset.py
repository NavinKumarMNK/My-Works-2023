import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import yaml
import pandas as pd

with open("config.yaml") as f:
    config = yaml.safe_load(f)


class TransformerDataset(Dataset):
    def __init__(self, df: pd.DataFrame, tokenizer_src: str, tokenizer_tgt: str, src_lang: str, tgt_lang: str, seq_len: int) -> None:
        super().__init__()
        
        self.df = df
        self.tokenizer_src = tokenizer_src
        self.tokenizer_tgt = tokenizer_tgt
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang
        self.seq_len = seq_len  # same seq_len for both source and target language

        # special tokens from the custom tokenizer
        self.sos_token = torch.Tensor([tokenizer_src.token_to_id("[SOS]")], dtype=torch.int64)
        self.eos_token = torch.Tensor([tokenizer_src.token_to_id("[EOS]")], dtype=torch.int64)
        self.pad_token = torch.Tensor([tokenizer_src.token_to_id("[PAD]")], dtype=torch.int64)

    def __len__(self) -> int:
        return len(self.df)
    
    def __getitem__(self, idx: int) -> dict:
        # support for only DataFrame pair
        src_text, tgt_text = self.df.iloc[idx][self.src_lang], self.df.iloc[idx][self.tgt_lang]
        src_input_ids, tgt_input_ids = self.tokenizer_src.encode(src_text).ids, self.tokenizer_tgt.encode(tgt_text).ids
        src_pad_len, tgt_pad_len = self.seq_len - len(src_input_ids) - 2, \
            self.seq_len - len(tgt_input_ids) - 1 # -2 for sos and eos token & -1 for sos token

        if src_pad_len < 0 or tgt_pad_len < 0:
            src_input_ids, tgt_input_ids = src_input_ids[:self.seq_len-2], \
                tgt_input_ids[:self.seq_len-1]
            src_pad_len, tgt_pad_len = 0, 0
        
        src_input_ids, tgt_input_ids = torch.Tensor(src_input_ids, dtype=torch.int64), \
            torch.Tensor(tgt_input_ids, dtype=torch.int64)
         
        # concatenating sos, eos and pad tokens
        src_input_ids = torch.cat(
            [self.sos_token, src_input_ids, self.eos_token, self.pad_token.repeat(src_pad_len)])
        label = torch.cat(
            [tgt_input_ids, self.eos_token, self.pad_token.repeat(tgt_pad_len)])
        tgt_input_ids = torch.cat(
            [self.sos_token, tgt_input_ids, self.pad_token.repeat(tgt_pad_len)])
        
        # attention mask in encoder is 1 for all non-pad tokens and 0 for pad tokens
        attenion_mask = (src_input_ids != self.pad_token).int()
        # casual attention mask in decoder is 1 for previous tokens and 0 for future tokens
        casual_attention_mask = torch.triu(
            torch.ones((self.seq_len, self.seq_len), dtype=torch.int64), diagonal=1
        )
        
        return {
            "encoder_input": src_input_ids, # (seq_len,)
            "decoder_input": tgt_input_ids, # (seq_len,)
            "encoder_mask": attenion_mask.unsqueeze(0).unsqueeze(0), # (seq_len,)
            "decoder_mask": casual_attention_mask.unsqueeze(0), # (seq_len, seq_len)
            "label" : label # (seq_len,)
        }