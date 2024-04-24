# Author : NavinKumarMNK
"""Transformer Model"""
from dataclasses import dataclass
from typing import Tuple, Optional
import math
import torch
import torch.nn as nn
import yaml

SEED = 42
torch.manual_seed(seed=SEED)
torch.cuda.manual_seed_all(seed=SEED)
torch.backends.cudnn.deterministic = True

class InputEmbeddings(nn.Module):
    # stores embedding of the tokens
    def __init__(self, dim_model: int, vocab_size: int):
        super().__init__()
        self.dim_model = dim_model
        self.vocab_size = vocab_size
        self.embedding = nn.Embedding(
            num_embeddings=self.vocab_size, embedding_dim=self.dim_model
        )

    def forward(self, x: torch.Tensor):
        return self.embedding(x) * math.sqrt(self.dim_model)


class PositionalEncoding(nn.Module):
    # calculate the positional embedding
    def __init__(self, dim_model: int, seq_len: int, dropout: float):
        super().__init__()
        self.dropout = nn.Dropout(dropout)

        # PE => (seq_len, d_model) ; position, div_term => (self.seq_len, 1)
        position_encoding = torch.zeros(size=(seq_len, dim_model))
        position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, dim_model, 2).float() * (-math.log(10000.0) / dim_model)
        )  # e^(2*i * (ln 10000) / dim_model)

        # sin() to even pos & cos() to odd position
        position_encoding[:, 0::2] = torch.sin(position * div_term)
        position_encoding[:, 1::2] = torch.cos(position * div_term)
        position_encoding = position_encoding.unsqueeze(0)  # (1, seq_len, dim_model)

        # register buffer => Keep with module but not as learnable paramter
        self.register_buffer("position_encoding", position_encoding)

    def forward(self, x: torch.Tensor):
        # positional encodings are added only till the valid tokens in x : (batch_size, seq_len, dim)
        return self.dropout(
            x + (self.position_encoding[:, : x.shape[1], :]).requires_grad_(False)
        )

class ConvBlock(nn.Module):
    def __init__(self, input_size, ):
        super().__init__()
        self.block = nn.Sequential(
            nn.Conv1d(in_channels=input_size,
                      out_channels=input_size // 2 , 
                      kernel_size=3),
            nn.ReLU(),
            nn.Conv1d(in_channels=input_size//2, 
                       out_channels=input_size//4, 
                       kernel_size=3),
            nn.ReLU(),
        )
    
    def forward(self, x):
        return self.block(x)

class LayerNorm(nn.Module):
    # Normazalize across Layers => Xj = (xj - uj)/(sigma^2 + e)^(0.5)
    def __init__(self, eps: float = 10**-6) -> None:
        super().__init__()
        self.eps = eps

        # parameters: alpha (multiplicative) bias (additive)
        self.alpha = nn.Parameter(torch.ones(1))
        self.bias = nn.Parameter(torch.zeros(1))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return (
            self.alpha
            * (x - x.mean(-1, keepdim=True))
            / (self.eps + x.std(dim=-1, keepdim=True))
        ) + self.bias


class FeedForwardBlock(nn.Module):
    # sequence of linear layer : [dim -> ddf(general-4*dim) -> dim]
    def __init__(self, dim_model: int, d_ff: int, dropout: float) -> None:
        super().__init__()
        # Linear -> Norm -> Activation -> Dropout -> Linear
        self.ffn = nn.Sequential(
            nn.Linear(dim_model, d_ff),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(d_ff, dim_model),
            nn.Dropout(dropout),
        )

    def forward(self, x: torch.Tensor):
        return self.ffn(x)


class MultiHeadAttentionBlock(nn.Module):
    def __init__(self, dim_model: int, num_heads: int, dropout: float) -> None:
        super().__init__()
        self.dim_model = dim_model
        self.num_heads = num_heads
        assert (
            self.dim_model % self.num_heads == 0
        ), "dim_model is not divisible by num_heads"

        self.d_k = self.dim_model // self.num_heads

        # key, query, value
        self.w_q = nn.Linear(self.dim_model, self.dim_model)
        self.w_k = nn.Linear(self.dim_model, self.dim_model)
        self.w_v = nn.Linear(self.dim_model, self.dim_model)

        # concat([heads]) * w_o
        self.w_o = nn.Linear(self.dim_model, self.dim_model)
        self.dropout = nn.Dropout(dropout)

    @staticmethod
    def attention(
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        mask: Optional[torch.Tensor] = None,
        dropout: Optional[nn.Dropout] = None,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        d_k = query.shape[-1]

        # attention = q.k / sqrt(dim) : (batch_szie, h, seq_len, d_k) -> (_, _, _, seq_len)
        attention_scores = (query @ key.transpose(-2, -1)) / math.sqrt(d_k)

        if mask is not None:
            attention_scores.masked_fill_(mask == 0, -1e4)
        attention_scores = attention_scores.softmax(dim=-1)

        if dropout is not None:
            attention_scores = dropout(attention_scores)

        return attention_scores @ value

    # mask => control attention by blocking interactions between two words
    def forward(self, query, key, value, mask: Optional[torch.Tensor]):
        # (batch_size, seq_len, dim_model) -> (batch_size, seq_len, dim_model) ->
        # (batch_size, seq_len, heads, d_k) -> (batch_size, heads, seq_len, d_k) : process across heads
        query = (
            self.w_q(query)
            .view(query.shape[0], query.shape[1], self.num_heads, self.d_k)
            .transpose(1, 2)
        )
        key = (
            self.w_k(key)
            .view(key.shape[0], key.shape[1], self.num_heads, self.d_k)
            .transpose(1, 2)
        )
        value = (
            self.w_v(value)
            .view(value.shape[0], value.shape[1], self.num_heads, self.d_k)
            .transpose(1, 2)
        )

        # final multihead attentions
        x = MultiHeadAttentionBlock.attention(query, key, value, mask, self.dropout)

        # (batch_size, heads, seq_len, d_k) -> (_, seq_len, heads, _) -> (batch_size, seq_len, dim_model)
        x = x.transpose(1, 2).contiguous().view(x.shape[0], -1, self.dim_model)
        x = self.w_o(x)
        return x


class EncoderBlock(nn.Module):
    # pre_norm -> mha() -> residual(before norm) -> pre_norm -> ffn() -> residual(before norm)
    def __init__(
        self, dim_model: int, num_heads: int, dropout: float, d_ff: int
    ) -> None:
        super().__init__()
        self.multi_head_attention = MultiHeadAttentionBlock(
            dim_model=dim_model, num_heads=num_heads, dropout=dropout
        )
        self.ffn = FeedForwardBlock(dim_model=dim_model, d_ff=d_ff, dropout=dropout)

        self.norm_ffn = LayerNorm()
        self.norm_mha = LayerNorm()

    def forward(self, x: torch.Tensor, mask: Optional[torch.Tensor]):
        x_norm = self.norm_mha(x)
        x_atten = x + self.multi_head_attention(x_norm, x_norm, x_norm, mask)
        x_ffn = x_atten + self.ffn(self.norm_ffn(x_atten))
        return x_ffn

class Encoder(nn.Module):
    # stacked n EncoderBlocks
    def __init__(
        self,
        dim_model: int,
        num_layers: int,
        dropout: float,
        num_heads: int,
        d_ff: int,
    ) -> None:
        super().__init__()
        self.layer_norm = LayerNorm()
        self.encoder_layers = nn.ModuleList(
            modules=[
                EncoderBlock(
                    dim_model=dim_model, num_heads=num_heads, dropout=dropout, d_ff=d_ff
                )
                for _ in range(num_layers)
            ]
        )

    def forward(self, x: torch.Tensor, mask: Optional[torch.Tensor]) -> torch.Tensor:
        for layer in self.encoder_layers:
            x = layer(x, mask)
        return self.layer_norm(x)


class DecoderBlock(nn.Module):
    # pre_norm -> masked mha (self-attention) -> residual -> pre_norm(q) + encoder(k, v) ->
    # mha (cross-attention) -> residual -> pre_norm -> ffn -> residual
    def __init__(
        self, dim_model: int, num_heads: int, dropout: float, d_ff: int
    ) -> None:
        super().__init__()

        self.self_attention = MultiHeadAttentionBlock(
            dim_model=dim_model, num_heads=num_heads, dropout=dropout
        )
        self.cross_attention = MultiHeadAttentionBlock(
            dim_model=dim_model, num_heads=num_heads, dropout=dropout
        )
        self.ffn = FeedForwardBlock(dim_model=dim_model, d_ff=d_ff, dropout=dropout)

        self.norm_self = LayerNorm()
        self.norm_cross = LayerNorm()
        self.norm_ffn = LayerNorm()

    def forward(
        self,
        x: torch.Tensor,
        encoder_x: torch.Tensor,
        src_mask: Optional[torch.Tensor],
        tgt_mask: Optional[torch.Tensor],
    ) -> torch.Tensor:
        x_norm = self.norm_self(x)
        x = x + self.self_attention(x_norm, x_norm, x_norm, tgt_mask)

        x_norm = self.norm_cross(x)
        x = x + self.cross_attention(x, encoder_x, encoder_x, src_mask)

        x_norm = self.norm_ffn(x)
        x = x + self.ffn(x_norm)

        return x


class Decoder(nn.Module):
    # stacked n DecoderBlocks
    def __init__(
        self,
        dim_model: int,
        num_layers: int,
        dropout: float,
        num_heads: int,
        d_ff: int,
    ) -> None:
        super().__init__()

        # module list of n Decoder Blocks
        self.layer_norm = LayerNorm()
        self.decoder_layers = nn.ModuleList(
            modules=[
                DecoderBlock(
                    dim_model=dim_model, num_heads=num_heads, dropout=dropout, d_ff=d_ff
                )
                for _ in range(num_layers)
            ]
        )

    def forward(
        self,
        x: torch.Tensor,
        encoder_output: torch.Tensor,
        src_mask: torch.Tensor,
        tgt_mask: torch.Tensor,
    ) -> torch.Tensor:
        for layer in self.decoder_layers:
            x = layer(x, encoder_output, src_mask, tgt_mask)

        return self.layer_norm(x)


class ProjectionHead(nn.Module):
    # feature vector to vocab
    def __init__(self, dim_model: int, vocab_size: int) -> None:
        super().__init__()
        self.proj = nn.Linear(dim_model, vocab_size)

    def forward(self, x) -> torch.Tensor:
        # (batch_size, seq_len, d_model) -> (_, _, vocab_size)
        return torch.log_softmax(self.proj(x), dim=-1)


class Transformer(nn.Module):
    def __init__(
        self,
        dim_model: int,
        num_layers: int,
        dropout: float,
        num_heads: int,
        d_ff: int,
        src_max_seq_len: int,
        tgt_max_seq_len: int,
        src_vocab_size: int,
        tgt_vocab_size: int,
    ) -> None:
        super().__init__()
        self.dim_model = dim_model
        self.num_layers = num_layers
        self.dropout = dropout
        self.num_heads = num_heads
        self.d_ff = d_ff
        self.src_max_seq_len = src_max_seq_len
        self.tgt_max_seq_len = tgt_max_seq_len
        self.src_vocab_size = src_vocab_size
        self.tgt_vocab_size = tgt_vocab_size

        # Embeddings (vocab -> vector)
        self.src_emb = InputEmbeddings(
            dim_model=self.dim_model, vocab_size=self.src_vocab_size
        )
        self.tgt_emb = InputEmbeddings(
            dim_model=self.dim_model, vocab_size=self.tgt_vocab_size
        )

        self.src_pos = PositionalEncoding(
            dim_model=self.dim_model, seq_len=self.src_max_seq_len, dropout=self.dropout
        )
        self.tgt_pos = PositionalEncoding(
            dim_model=self.dim_model, seq_len=self.tgt_max_seq_len, dropout=self.dropout
        )
        
        # Core Layers
        self.encoder = Encoder(
            dim_model=self.dim_model,
            num_layers=self.num_layers,
            dropout=self.dropout,
            num_heads=self.num_heads,
            d_ff=self.d_ff,
        )
        self.decoder = Decoder(
            dim_model=self.dim_model,
            num_layers=self.num_layers,
            dropout=self.dropout,
            num_heads=self.num_heads,
            d_ff=self.d_ff,
        )

        # Conversion head (vector -> word)
        self.projection = ProjectionHead(
            dim_model=self.dim_model, vocab_size=self.tgt_vocab_size
        )

        for params in self.parameters():
            if params.dim() > 1:
                nn.init.xavier_uniform_(params)

    def encode(self, src, src_mask):
        src = self.src_emb(src)
        src = self.src_pos(src)
        return self.encoder(src, src_mask)

    def decode(self, tgt, src_output, src_mask, tgt_mask):
        tgt = self.tgt_emb(tgt)
        tgt = self.tgt_pos(tgt)
        return self.decoder(tgt, src_output, src_mask, tgt_mask)

    def project(self, x: torch.Tensor) -> torch.Tensor:
        return self.projection(x)
    
    def forward(self, src, tgt, src_mask, tgt_mask):
        src_output = self.encode(src, src_mask)
        tgt_output = self.decode(tgt, src_output, src_mask, tgt_mask)
        return self.project(tgt_output)


if __name__ == "__main__":
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    model = Transformer(**config["model"]["parameters"])    
    print(model)
    
    # calculate no of parameters in encoder, decoder, and embedding layers separately
    # encoder
    encoder_params = sum(p.numel() for p in model.encoder.parameters() if p.requires_grad)
    print(f"Encoder Parameters: {encoder_params:,}")
    
    # decoder
    decoder_params = sum(p.numel() for p in model.decoder.parameters() if p.requires_grad)
    print(f"Decoder Parameters: {decoder_params:,}")
    
    # embedding
    embedding_params = sum(p.numel() for p in model.src_emb.parameters() if p.requires_grad)
    print(f"Embedding Parameters: {embedding_params:,}")
    
    # embedding target 
    embedding_params = sum(p.numel() for p in model.tgt_emb.parameters() if p.requires_grad)
    print(f"Embedding Parameters: {embedding_params:,}")
    
    pos_parms = sum(p.numel() for p in model.src_pos.parameters() if p.requires_grad)
    print(f"Positional Encoding Parameters: {pos_parms:,}")
    
    pos_parms = sum(p.numel() for p in model.tgt_pos.parameters() if p.requires_grad)
    print(f"Positional Encoding Parameters: {pos_parms:,}")
    
    
    # projection
    projection_params = sum(p.numel() for p in model.projection.parameters() if p.requires_grad)
    print(f"Projection Parameters: {projection_params:,}")
    
    
    