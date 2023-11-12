# Author : NavinKumarMNK
"""Training script"""

import torch
import torch.nn as nn
import yaml
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

from scripts.model import Transformer
from scripts.tokenizer import BPETokenizer
from scripts.dataset import Seq2SeqDataLoader
from scripts.preprocessing import load_corpus
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

SEED = 42
torch.manual_seed(seed=SEED)
torch.cuda.manual_seed_all(seed=SEED)
torch.backends.cudnn.deterministic = True

import lightning as L
import lightning.pytorch.loggers as logger
import lightning.pytorch.callbacks as callback

class Seq2SeqModel(L.LightningModule):
    def __init__(self, model_config, train_config):
        super().__init__()
        self.model_config = model_config
        self.train_config = train_config
        
        self.model = Transformer(**self.model_config["parameters"])
        self.loss_fn = nn.CrossEntropyLoss(
            ignore_index=1, # ignore padding token
            # label_smoothing=self.train_config['label_smoothing'],
        )
       
        self.save_hyperparameters()

    def forward(self, src, tgt, src_mask, tgt_mask):
        return self.model(src=src, tgt=tgt, src_mask=src_mask, tgt_mask=tgt_mask)

    def training_step(self, batch, batch_idx):
        encoder_input = batch['encoder_input'] # (batch_size, seq_len)
        decoder_input = batch['decoder_input'] # (batch_size, seq_len)
        encoder_mask = batch['encoder_mask'] # (batch_size, 1, 1, seq_len)
        decoder_mask = batch['decoder_mask'] # (batch_size, 1, seq_len, seq_len)
        label = batch['label'] # (batch_size, seq_len)

        output = self(src=encoder_input, tgt=decoder_input,
                      src_mask=encoder_mask, tgt_mask=decoder_mask)
        
        loss = self.loss_fn(output.view(-1, output.size(-1)), label.view(-1))
        self.log('train_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return loss

    def validation_step(self, batch, batch_idx):
        encoder_input = batch['encoder_input'] # (batch_size, seq_len)
        decoder_input = batch['decoder_input'] # (batch_size, seq_len)
        encoder_mask = batch['encoder_mask'] # (batch_size, 1, 1, seq_len)
        decoder_mask = batch['decoder_mask'] # (batch_size, 1, seq_len, seq_len)
        label = batch['label'] # (batch_size, seq_len)

        output = self(src=encoder_input, tgt=decoder_input,
                      src_mask=encoder_mask, tgt_mask=decoder_mask)
        
        loss = self.loss_fn(output.view(-1, output.size(-1)), label.view(-1))
        self.log('val_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(
            params=self.parameters(), 
            **self.train_config['optimizer'])
        return optimizer

if __name__ == '__main__':
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    
    train_config = config['train']
    model_config = config['model']
    token_config = config['tokenizer']
    data_config = config['data']
    
    '''
    # Preprocessing Dataset
    corpus = load_corpus(data_config)
    corpus.to_parquet(data_config['dataset_path'])
    print("Corpus Preprocessed and saved to ", data_config['dataset_path'])
    
    # Tokenizer setup
    # df = pd.read_parquet(token_config['dataset_path'])
    src_bool = True
    for items in (token_config['src'], token_config['tgt']):
        _df = corpus[items['lang']]

        bpe_tokenizer = BPETokenizer(items)
        bpe_tokenizer.train(_df)
        print("Size of vocabulary:", bpe_tokenizer.tokenizer.get_vocab_size())
        if src_bool:
            tokenizer_src = bpe_tokenizer.tokenizer
            src_bool = False
        else:
            tokenizer_tgt = bpe_tokenizer.tokenizer

    print("Successfully trained Tokenizers")

    '''
    from tokenizers import Tokenizer
    tokenizer_src: BPETokenizer = Tokenizer.from_file(token_config['src']['tokenizer_path'])
    tokenizer_tgt: BPETokenizer = Tokenizer.from_file(token_config['tgt']['tokenizer_path'])
    

    # Dataset setup
    dataset = Seq2SeqDataLoader(
        df=pd.read_parquet(train_config['dataset_path']),
        tokenizer_src=train_config['tokenizer']['src']['path'],
        tokenizer_tgt=train_config['tokenizer']['tgt']['path'],
        src_lang=train_config['tokenizer']['src']['lang'],
        tgt_lang=train_config['tokenizer']['tgt']['lang'],
        src_seq_len=train_config['tokenizer']['src']['seq_len'],
        tgt_seq_len=train_config['tokenizer']['tgt']['seq_len'],
        batch_size=train_config['batch_size'],
        num_workers=train_config['num_workers'],
        split_size=train_config['split_size']
    )
    dataset.setup()
    print("Dataset setup complete")
    
    train_loader = dataset.train_dataloader()
    val_loader = dataset.val_dataloader()

    # device settings for training
    if train_config['device'] == 'cuda':
        if not torch.cuda.is_available():
            print("Device set to cuda but cuda is not available. Using CPU")
            train_config['device'] = 'cpu'
    
    # model setup
    model = Seq2SeqModel(model_config, train_config)

    if train_config['fine_tune']:
        model.model = torch.load(train_config['model_path'])
        print("Loaded model from ", train_config['model_path'])

    # tensorboard logging
    callbacks = [
        callback.EarlyStopping(**train_config['callbacks']['early_stopping']),
        callback.ModelCheckpoint(**train_config['callbacks']['model_checkpoint']),
        callback.LearningRateMonitor(logging_interval='step'),
        callback.DeviceStatsMonitor(),  
        callback.ModelSummary(max_depth=5),
    ]
    
    tensorboard_logger = logger.TensorBoardLogger(
        save_dir=train_config['logger']['save_dir'],
        name=train_config['logger']['name'],    
    )
    
    trainer = L.Trainer(
        **train_config['trainer'],
        logger=tensorboard_logger,
        callbacks=callbacks,
    )
    
    try:
        trainer.fit(model, dataset)
    except KeyboardInterrupt:
        print("Keyboard Interrupted... Continuing Further")
    
    # Saving the model
    torch.save(model.model, train_config['model_path'])   
    