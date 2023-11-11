import torch
import pandas as pd

import os
import yaml

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

if '__main__' == __name__:
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        
    data_config = config['data']
    docs = data_config['src_to_tgt']

    dfs = []
    for key, val in docs.items():
        txt1, txt2 = (read_text_file(os.path.join(data_config['data_dir'], key)), 
                    read_text_file(os.path.join(data_config['data_dir'], val)))
        corpus = pd.DataFrame({'src': txt1, 'tgt': txt2})    
        dfs.append(corpus)

    corpus = pd.concat(dfs, ignore_index=True)
    corpus.rename(columns={'src': data_config['src'], 'tgt': data_config['src']}, inplace=True)

    print(len(corpus), corpus.columns)


