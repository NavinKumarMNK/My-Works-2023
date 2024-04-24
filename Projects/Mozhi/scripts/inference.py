# Author : NavinKumarMNK
"""Inference script"""

import torch
import torch.nn as nn
import yaml
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

from tokenizers import Tokenizer
torch.backends.cudnn.benchmark = True

try:
    from model import Transformer
except:
    from scripts.model import Transformer
    
class Infer():
    def __init__(self, config, model_config):
        self.model = Transformer(**model_config)
        self.model.load_state_dict(state_dict=torch.load(config['model_path']))
        self.tokenizer_src: Tokenizer = Tokenizer.from_file(config['tokenizer_src'])
        self.tokenizer_tgt: Tokenizer = Tokenizer.from_file(config['tokenizer_tgt'])

        self.seq_len = config['seq_len']
        self.device = config['device'] if torch.cuda.is_available() else 'cpu'
        self.model.to(self.device)
    
    def translate(self, text):
        # Encoding the text
        src_input_ids = torch.Tensor(self.tokenizer_src.encode(text).ids).long()
        src_pad_len = self.seq_len - len(src_input_ids) - 2
        if src_pad_len < 0:
            src_input_ids = src_input_ids[:self.seq_len-2]
            src_pad_len = 0
        src_input_ids = torch.cat(
            [torch.Tensor([0]), src_input_ids, torch.Tensor([2]), torch.Tensor([1]*src_pad_len)]
        ).long().to(self.device)
        attenion_mask = (src_input_ids != 1).unsqueeze(0).unsqueeze(0).to(self.device)

        # Set the model to evaluation mode
        self.model.eval()

        # Encode the input
        with torch.no_grad():
            encoder_output = self.model.encode(src_input_ids, attenion_mask)
            
            # Decode the output
            output = torch.empty(1, 1).fill_(0).type_as(src_input_ids).long().to(self.device)
            for i in range(self.seq_len):
                decoder_mask = torch.triu(
                    torch.ones((i+1, i+1)).type_as(attenion_mask), diagonal=1
                ).unsqueeze(0).to(self.device)
                decoder_output = self.model.decode(
                    tgt = output,
                    src_output = encoder_output,
                    src_mask = attenion_mask,
                    tgt_mask = decoder_mask
                )
                decoder_output = decoder_output[:, -1, :].argmax(dim=-1).unsqueeze(1)
                output = torch.cat([output, decoder_output], dim=1)
                if decoder_output.item() == 2:  # End of Sentence token
                    break
            return self.tokenizer_tgt.decode(output.squeeze(0).tolist())


if __name__ == '__main__':
    with open('config.yaml', 'r') as f:
        x = yaml.safe_load(f)
        config = x['infer']
        model_config = x['model']['parameters']

    infer = Infer(config, model_config=model_config)
    text = "Hello! How are you?"
    print(infer.translate(text))
