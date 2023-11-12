"""
author: @NavinKumarMNK
Train a Byte-Pair Encoding tokenizer for the given src, tgt langugaes
"""

import pandas as pd
import yaml
from pathlib import Path
from typing import Generator
from tokenizers import Tokenizer, models, normalizers, pre_tokenizers, decoders, trainers, processors

class BPETokenizer:
    def __init__(self, config):
        self.config = config
        self.tokenizer = Tokenizer(models.BPE(unk_token=config['special_tokens']['unk_token']))

    def _get_special_tokens(self):
        return {
            self.config['special_tokens']['bos_token']: 0,
            self.config['special_tokens']['pad_token']: 1,
            self.config['special_tokens']['eos_token']: 2,
            self.config['special_tokens']['unk_token']: 3,
            self.config['special_tokens']['mask_token']: 50264,
        }

    def _get_language_specific_components(self):
        if config['lang'] == 'ta':
            normalizer = normalizers.NFKC()
            pre_tokenizer = pre_tokenizers.Metaspace()
            decoder = decoders.Metaspace()
        elif config['lang'] == 'en':
            normalizer = normalizers.Sequence([
                normalizers.NFKC(),
                normalizers.Lowercase()
            ])
            pre_tokenizer = pre_tokenizers.ByteLevel()
            decoder = decoders.ByteLevel()
        else:
            raise ValueError(f"Unsupported language: {config['lang']}")
        
        return normalizer, pre_tokenizer, decoder

    def _get_post_processor(self, special_tokens):
        return processors.TemplateProcessing(
            single=f"{self.config['special_tokens']['bos_token']} $A {self.config['special_tokens']['eos_token']}",
            special_tokens=list(special_tokens.items()),
        )

    def _get_trainer(self, special_tokens):
        return trainers.BpeTrainer(
            special_tokens=list(special_tokens.keys()),
            vocab_size=self.config['vocab_size'],
            min_frequency=self.config['min_frequency'],
            show_progress=True,
        )

    def _configure_tokenizer(self, normalizer, pre_tokenizer, decoder, post_processor, trainer):
        self.tokenizer.normalizer = normalizer
        self.tokenizer.pre_tokenizer = pre_tokenizer
        self.tokenizer.decoder = decoder
        self.tokenizer.post_processor = post_processor
        self.trainer = trainer

    def _train_tokenizer(self):
        get_sentences = lambda series: (text for text in series)

        self.tokenizer.train_from_iterator(
            get_sentences(series=self.series),
            trainer=self.trainer,
            length=len(self.series),
        )

        self.tokenizer.save(str(self.tokenizer_path))
        print(self.tokenizer)
        print(self.tokenizer.get_vocab_size())

    def _setup_tokenizer(self):
        special_tokens = self._get_special_tokens()
        normalizer, pre_tokenizer, decoder = self._get_language_specific_components()
        post_processor = self._get_post_processor(special_tokens)
        trainer = self._get_trainer(special_tokens)

        self.tokenizer_path = Path(self.config['tokenizer_path'])
        self._configure_tokenizer(normalizer, pre_tokenizer, decoder, post_processor, trainer)
        self._train_tokenizer()

    def train(self, series):
        self.series = series
        self._setup_tokenizer()

    def load_tokenizer(self, path):
        self.tokenizer = Tokenizer.from_file(path)

    def save_tokenizer(self, path):
        self.tokenizer.save(path)


if __name__ == '__main__':
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    config = config['tokenizer']
    df = pd.read_parquet(config['data_path'])

    for items in (config['src'], config['tgt']):
        _df = df[items['lang']]

        bpe_tokenizer = BPETokenizer(items)
        bpe_tokenizer.train(_df)

        # Save the tokenizer
        bpe_tokenizer.save_tokenizer("saved_tokenizer.json")

        # Load the saved tokenizer
        bpe_tokenizer.load_tokenizer("saved_tokenizer.json")

        encoded_tokens = bpe_tokenizer.tokenizer.encode(_df[0])
        print(encoded_tokens.ids)
        print(encoded_tokens.type_ids)
        print(encoded_tokens.tokens)
        print(encoded_tokens.overflowing)

        encoded_ids = encoded_tokens.ids

        decoded_string = bpe_tokenizer.tokenizer.decode(encoded_ids)
        print(f"{decoded_string = }")

        print("Size of vocabulary:", bpe_tokenizer.tokenizer.get_vocab_size())
        print("Successfully trained and saved/loaded tokenizer", bpe_tokenizer.tokenizer)
