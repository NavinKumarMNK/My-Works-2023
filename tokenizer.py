import torch
# Author : NavinKumarMNK
"""Tokenizer"""
import torch.nn as nn
import tqdm
import pandas as pd

from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.processors import TemplateProcessing
from tokenizers.decoders import ByteLevel as ByteLevelDecoder
from tokenizers.normalizers import NFKC, Sequence, Lowercase, StripAccents

from typing import Generator
from pathlib import Path


SPECIAL_TOKENS = ["[UNK]", "[CLS]", "[SEP]", "[PAD]"]

class BPETokenizer:
    def __init__(self, config):
        self.config = config
        self.tokenizer = Tokenizer(BPE(unk_token=SPECIAL_TOKENS[0]))        
        self.tokenizer.pre_tokenizer = Whitespace()
        self.tokenizer_path = Path(self.config['tokenizer_path'].format(lang))

    def train(self, df):
        trainer = BpeTrainer(special_tokens=SPECIAL_TOKENS)
        with tqdm(total=len(df), desc="Training tokenizer") as pbar:
            def progress_callback(trainer):
                pbar.update()
            self.tokenizer.train_from_iterator(self._get_sentences(
                df=df, lang=self.config['lang'], 
                progress_callback=progress_callback
            ), trainer=trainer)
        self.tokenizer.save(self.tokenizer_path)

    def load(self, ds, lang):
        if not Path.exists(self.tokenizer_path):
            raise FileNotFoundError(f'No tokenizer found at {self.tokenizer_path}')
        self.tokenizer = Tokenizer.from_file(self.tokenizer_path)

    def _get_sentences(self, df: pd.DataFrame, lang: str) -> Generator[str]: 
        for item in df:
            yield item[lang]

    def encode(self, text: str) -> dict:
        return self.tokenizer.encode(text)
    
    def decode(self, ids: list) -> str:
        return self.tokenizer.decode(ids)
    
    def token_to_id(self, token: str) -> int:
        return self.tokenizer.token_to_id(token)
    
    def id_to_token(self, id: int) -> str:
        return self.tokenizer.id_to_token(id)
    
    @property
    def vocab_size(self) -> int:
        return self.tokenizer.get_vocab_size()
    