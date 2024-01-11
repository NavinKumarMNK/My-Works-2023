import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
    config = config['general']

def download_entire_repo(repo_id, local_dir, local_dir_use_symlinks=False):
    from huggingface_hub import snapshot_download
    snapshot_download(repo_id, local_dir=local_dir, local_dir_use_symlinks=local_dir_use_symlinks)

def download_file(repo_id, filename, local_dir):
    from huggingface_hub import hf_hub_download
    hf_hub_download(repo_id=repo_id, filename=filename, local_dir=local_dir)

'''
download_entire_repo(
    repo_id = "TheBloke/zephyr-7B-alpha-GPTQ",
    local_dir="/app/models/",
    local_dir_use_symlinks=False,
)
'''

download_file(
    repo_id = config['repo_id'],
    filename = config['model'], 
    local_dir = config['model_dir'],
)

from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
embedder = FastEmbedEmbeddings()

