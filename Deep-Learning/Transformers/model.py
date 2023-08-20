# Author : NavinKumarMNK
"""Transformer Model"""
from dataclasses import dataclass
from typing import Tuple, Optional
import math
import torch
import torch.nn as nn


SEED = 42
torch.manual_seed(seed=SEED)
torch.cuda.manual_seed_all(seed=SEED)
torch.backends.cudnn.deterministic = True


@dataclass
class Paramters:
    DIM_MODEL = 512
    SEQ_LENGTH = 512
    VOCAB_SIZE = 25
    EPS = 1e-6


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
        return self.embedding * math.sqrt(self.dim_model)


class PositionalEncoding(nn.Module):
    # calculate the positional embedding
    def __init__(self, dim_model: int, seq_len: int, dropout: float):
        super().__init__()
        self.dim_model = dim_model
        self.seq_len = seq_len
        self.dropout = nn.Dropout(dropout)

        # PE => (seq_len, d_model) ; position, div_term => (self.seq_len, 1)
        position_encoding = torch.zeros(size=(self.seq_len, self.dim_model))
        position = torch.arange(0, self.seq_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, self.dim_model, 2).float()
            * (-math.log(10000.0) / self.dim_model)
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
        self.dim_model = dim_model
        self.d_ff = d_ff
        self.dropout = dropout

        # Linear -> Norm -> Activation -> Dropout -> Linear
        self.ffn = nn.Sequential(
            nn.Linear(self.dim_model, d_ff),
            nn.ReLU(),
            nn.Dropout(self.dropout),
            nn.Linear(self.d_ff, self.dim_model),
            nn.Dropout(self.dropout),
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
            attention_scores.masked_fill_(mask == 0, -1e9)
        attention_scores = attention_scores.softmax(dim=-1)

        if dropout is not None:
            attention_scores = dropout(attention_scores)

        return attention_scores @ value

    # mask => control attention by blocking interactions between two words
    def forward(self, q, k, v, mask: Optional[torch.Tensor]):
        # (batch_size, seq_len, dim_model) -> (batch_size, seq_len, dim_model) ->
        # (batch_size, seq_len, heads, d_k) -> (batch_size, heads, seq_len, d_k) : process across heads
        query = (
            self.w_q(q)
            .view(query.shape[0], query.shape[1], self.num_heads, self.d_k)
            .transpose(1, 2)
        )
        key = (
            self.w_k(k)
            .view(key.shape[0], key.shape[1], self.num_heads, self.d_k)
            .transpose(1, 2)
        )
        value = (
            self.w_v(v)
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
    def __init__(self, dim_model: int, num_heads: int, dropout: float) -> None:
        super().__init__()
        self.dim_model = dim_model
        self.num_heads = num_heads
        self.dropout = dropout

        self.multi_head_attention = MultiHeadAttentionBlock(
            dim_model=self.dim_model, num_heads=self.num_heads, dropout=self.dropout
        )
        self.ffn = FeedForwardBlock(
            dim_model=self.dim_model, d_ff=4 * self.dim_model, dropout=self.dropout
        )

        self.norm_ffn = LayerNorm()
        self.norm_mha = LayerNorm()

    def forward(self, x: torch.Tensor, mask: Optional[torch.Tensor]):
        x_norm = self.norm_mha(x)
        x_atten = x + self.multi_head_attention(x_norm, x_norm, x_norm, mask)
        x_ffn = x_atten + self.ffn(self.norm_ffn((x_atten)))
        return x_ffn


class Encoder(nn.Module):
    # stacked n EncoderBlocks
    def __init__(
        self,
        dim_model: int,
        seq_len: int,
        n_blocks: int,
        dropout: float,
        num_heads: int,
    ) -> None:
        self.dim_model = dim_model
        self.seq_len = seq_len
        self.n_blocks = n_blocks
        self.dropout = dropout
        self.num_heads = num_heads

        # module list of n Encoder Blocks
        self.layer_norm = LayerNorm()
        self.encoder_layers = nn.ModuleList(
            [
                EncoderBlock(
                    dim_model=self.dim_model,
                    num_heads=self.num_heads,
                    dropout=self.dropout,
                )
                for _ in range(n_blocks)
            ]
        )

    def forward(self, x: torch.Tensor, mask: Optional[torch.Tensor]) -> torch.Tensor:
        for layer in self.encoder_layers:
            x = layer(x, mask)
        return self.layer_norm(self.x)





if __name__ == "__main__":
    params = Paramters()
    # print(params)
    # inp =  InputEmbeddings(2, 3)
    # pe = PositionalEncoding(params.DIM_MODEL, seq_len=params.SEQ_LENGTH, dropout=0.2)
    # ln = LayerNorm()
    # y = torch.rand(1, 512, 512)
    # x: torch.Tensor = ln(y)
    # print(y, x)
