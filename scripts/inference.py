# Author : NavinKumarMNK
"""Inference script"""

import torch
import torch.nn as nn
import yaml
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from scripts.model import Transformer
from tokenizer import BPETokenizer
from scripts.dataset import TransformerDataset
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

torch.backends.cudnn.benchmark = True

class Infer():
    def __init__(self) -> None:
        with open("config.yaml") as f:
            self.config = yaml.safe_load(f)

        self.seq_len = self.config['model']['parameters']['seq_len']

        self.tokenizer_src = BPETokenizer()
        self.tokenizer_tgt = BPETokenizer()

        self.eos_token = torch.Tensor([self.tokenizer_src.token_to_id("[EOS]")]).to(self.device)
        self.sos_token = torch.Tensor([self.tokenizer_src.token_to_id("[SOS]")]).to(self.device)
        self.pad_token = torch.Tensor([self.tokenizer_src.token_to_id("[PAD]")]).to(self.device)

        self.tokenizer_src.load(self.config['tokenizer']['src']['tokenizer_path'])
        self.tokenizer_tgt.load(self.config['tokenizer']['tgt']['tokenizer_path'])

        self.src_lang = self.config['src']['lang']
        self.tgt_lang = self.config['tgt']['lang']

        self.model: Transformer = torch.load(self.config['model']['model_path'])
        
        # device settings for inference
        self.device = self.config['inference']['device']
        if self.device == 'cuda':
            if not torch.cuda.is_available():
                print("Device set to cuda but cuda is not available. Using CPU")
                self.device = 'cpu'
                
        self.model.to(self.device)

    def translate(self, text):
        # Encoding the text
        src_input_ids = torch.Tensor(self.tokenizer_src.encode(text).ids, dtype=torch.int64)
        src_pad_len = self.seq_len - len(src_input_ids) - 2
        if src_pad_len < 0:
            src_input_ids = src_input_ids[:self.seq_len-2]
            src_pad_len = 0
        src_input_ids = torch.cat(
            [self.sos_token, src_input_ids, self.eos_token, self.pad_token.repeat(src_pad_len)])
        attenion_mask = (src_input_ids != self.pad_token).unsqueeze(0).unsqueeze(0)

        src_input_ids = src_input_ids.to(self.device)
        attenion_mask = attenion_mask.to(self.device)

        # infer
        self.model.eval()
        with torch.no_grad():
            encoder_output = self.model.encode(src_input_ids, attenion_mask)
            # decode text generate
            output = (torch.empty(1, 1).fill_(self.sos_token)
                            .type_as(src_input_ids).to(self.device))
            for i in range(self.seq_len): 
                decoder_mask = torch.triu(
                    torch.ones((i+1, i+1)).type_as(attenion_mask), diagonal=1
                ).unsqueeze(0).to(self.device)
                decoder_output = self.model.decode(
                    tgt = output,
                    encoder_output = encoder_output,
                    encoder_mask = attenion_mask,
                    decoder_mask = decoder_mask
                )

                # greedy decoding, only max prob temp=0
                prob = self.model.project(decoder_output[: -1])
                _, next_token = torch.max(prob, dim=-1)
                
                # append next token to output
                output = torch.cat([output, next_token[-1].unsqueeze(0).unsqueeze(0)], dim=1).to(self.device)

                # yield current token after decoding
                yield self.tokenizer_tgt.decode(next_token[-1].item())

                # break if eos token is generated
                if next_token[-1] == self.eos_token:
                    break
                
if __name__ == '__main__':
    text = "World is cruel but beautiful"
    translated_text = Infer().translate(text) 
    for token in translated_text:
        print(token)

    import transformer_engine
    
