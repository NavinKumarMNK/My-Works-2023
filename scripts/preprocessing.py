import os
import yaml
import pandas as pd
from typing import Dict

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def load_corpus(data_config: Dict) -> pd.DataFrame:
    docs = data_config['src_to_tgt']

    dfs = []
    for key, val in docs.items():
        txt1, txt2 = (read_text_file(os.path.join(data_config['data_dir'], key)), 
                      read_text_file(os.path.join(data_config['data_dir'], val)))
        corpus = pd.DataFrame({'src': txt1, 'tgt': txt2})    
        dfs.append(corpus)

    corpus = pd.concat(dfs, ignore_index=True)
    corpus.rename(columns={'src': data_config['src'], 'tgt': data_config['tgt']}, inplace=True)

    return corpus

if __name__ == '__main__':
    with open('../config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    
    data_config = config['data']
    corpus = load_corpus(data_config)
    print(len(corpus), corpus.columns)
