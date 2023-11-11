"author: @NavinKumarMNK"

import pandas as pd

from pathlib import Path
from tokenizers import Tokenizer, trainers, pre_tokenizers
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.decoders import ByteLevel as ByteLevelDecoder

from tokenizers.normalizers import NFKC, Lowercase
from tqdm import tqdm
from typing import Generator

SPECIAL_TOKENS = ["[PAD]", "[CLS]", "[SEP]", "[MASK]", "[UNK]"]

class BPETokenizer(Tokenizer):
    def __init__(self):
        self = Tokenizer(BPE(unk_token=SPECIAL_TOKENS[0]))
        self.pre_tokenizer = Whitespace()

    def train(self, series: pd.Series, config):
        self.config = config
        self.tokenizer_path = Path(self.config['tokenizer_path'])
        
        self.normalizer = NFKC()  
        self.normalizer = Lowercase()  

        trainer = BpeTrainer(
            special_tokens=SPECIAL_TOKENS,
            vocab_size=self.config['vocab_size'],
            show_progress=True,
            )
        with tqdm(total=len(series), desc="Training tokenizer") as pbar:
            def progress_callback(trainer):
                pbar.update()
            
            # Apply pre-processing and train the tokenizer
            self.train_from_iterator(
                self._get_sentences(series=series, lang=self.config['lang']),
                
                trainer=trainer,
                progress_callback=progress_callback
            )
        self.save(str(self.tokenizer_path))

    def load(self, path):
        if not Path.exists(path):
            raise FileNotFoundError(f'No tokenizer found at {path}')
        self = Tokenizer.from_file(str(path))

    def _get_sentences(self, series: pd.Series, lang: str) -> Generator[str, None, None]:
        for text in series.apply(lambda x: x[lang]):
            yield text

    @property
    def vocab_size(self) -> int:
        return self.get_vocab_size()

if __name__ == '__main__':
    import yaml
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        
        
    config = config['tokenizer']
    df = pd.read_parquet(config['data_path'])
    
    for items in (config['src'], config['tgt']):
        df = df[items['lang']]
        
        tokenizer = BPETokenizer()

        tokenizer.train(df, items)
        tokenizer.save(items['tokenizer_path'])
        
        encoded_tokens = tokenizer.encode(df[0])
        print(encoded_tokens)
        decoded_string = tokenizer.decode(encoded_tokens)
        print(decoded_string)
        
        print("Size of vocabulary:", tokenizer.vocab_size)
        print("Successfully trained tokenizer", tokenizer)
        