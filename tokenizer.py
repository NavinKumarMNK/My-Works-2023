"author: @NavinKumarMNK"

import pandas as pd
import yaml

from pathlib import Path
from typing import Generator
from tokenizers import (
    Tokenizer, 
    models, 
    normalizers, 
    pre_tokenizers, 
    decoders, 
    trainers, 
    processors
)

def train_bpe_tokenizer(tokenizer: Tokenizer, series, config):
    tokenizer_path = Path(config['tokenizer_path'])
    special_tokens = {
        config['special_tokens']['bos_token']: 0,
        config['special_tokens']['pad_token']: 1,
        config['special_tokens']['eos_token']: 2,
        config['special_tokens']['unk_token']: 3,
        config['special_tokens']['mask_token']: 50264,
    }
    
    if config['lang'] == 'en':
        normalizer = normalizers.Sequence([
            normalizers.NFKC(),
            normalizers.Lowercase()
        ])
        pre_tokenizer = pre_tokenizers.Metaspace()
        decoder = decoders.Metaspace()
    elif config['lang'] == 'ta':
        normalizer = normalizers.NFKC()
        pre_tokenizer = pre_tokenizers.ByteLevel()
        decoder = decoders.ByteLevel()
    else:
        raise ValueError(f"Unsupported language: {config['lang']}")
    
    post_processor = processors.TemplateProcessing(
        single=f"{config['special_tokens']['bos_token']} $A {config['special_tokens']['eos_token']}",
        special_tokens=list(special_tokens.items()),
    )
    
    trainer = trainers.BpeTrainer(
        special_tokens=list(special_tokens.keys()),
        vocab_size=config['vocab_size'],
        min_frequency=config['min_frequency'],
        show_progress=True,
    )

    tokenizer.normalizer = normalizer
    tokenizer.pre_tokenizer = pre_tokenizer
    tokenizer.decoder = decoder
    tokenizer.post_processor = post_processor
    
    def get_sentences(series: pd.Series) -> Generator[str, None, None]:
        for text in series:
            yield text

    tokenizer.train_from_iterator(
        get_sentences(series=series),
        trainer=trainer,
        length=len(series),
    )

    tokenizer.save(str(tokenizer_path))
    print(tokenizer)
    print(tokenizer.get_vocab_size())


if __name__ == '__main__':
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    config = config['tokenizer']
    df = pd.read_parquet(config['data_path'])

    for items in (config['src'], config['tgt']):
        _df = df[items['lang']]

        tokenizer = Tokenizer(models.BPE(unk_token=items['special_tokens']['unk_token']))
        train_bpe_tokenizer(tokenizer, _df, items)

        encoded_tokens = tokenizer.encode(_df[0])
        print(encoded_tokens.ids)
        print(encoded_tokens.type_ids)
        print(encoded_tokens.tokens)
        print(encoded_tokens.overflowing)

        encoded_ids = encoded_tokens.ids

        decoded_string = tokenizer.decode(encoded_ids)
        print(f"{decoded_string = }")

        print("Size of vocabulary:", tokenizer.get_vocab_size())
        print("Successfully trained tokenizer", tokenizer)

        