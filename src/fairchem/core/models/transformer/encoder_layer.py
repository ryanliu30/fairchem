import torch
import torch.nn as nn

from .mlp import ResMLP
from .sparse_att import SparseSelfAttention

class EncoderLayer(nn.Module):
    """
    An encoder layer implementation based on https://nn.labml.ai/transformers/models.html
    """
    def __init__(
        self, 
        embed_dim: int = 512, 
        hidden_dim: int = 1024,
        num_heads: int = 8, 
        dropout: float = 0.,
        att_dropout: float = 0.,
        activation: nn.Module = nn.SiLU(),
    ):
        """
        Initialize an `SelfAttentionLayer` instance
        arguments:
            embed_dim: the size of input 
            hidden_dim: hidden size of the feed forward network
            num_heads: number of heads used in MHA
            dropout: dropout strength
            activation: activation function
        """
        super().__init__()

        self.self_att = SparseSelfAttention(
            embed_dim=embed_dim,
            num_heads=num_heads,
            dropout=att_dropout
        )

        self.feed_forward = ResMLP(
            input_dim=embed_dim,
            hidden_dim=hidden_dim,
            output_dim=embed_dim,
            dropout=dropout,
        )

        self.norm_att = nn.LayerNorm(embed_dim)
        self.norm_ff = nn.LayerNorm(embed_dim)
        self.activation = activation

    def forward(
        self,
        x: torch.Tensor,
        edge_index: torch.Tensor, 
        att_bias: torch.Tensor,
    ) -> torch.tensor:
        """
        transform the input using the attention block
        arguments:
            x: input sequence of shape (L, C)
            pos: input positions of shape (L, 3)
            edge_index: coo formated sparse matrix of shape (2, E)
            att_bias: a tensor of shape (E, H)
        """

        z = self.norm_att(x)
        
        self_att = self.self_att(
            z, edge_index[0], edge_index[1], att_bias, False
        )

        x = x + self_att
        z = self.norm_ff(x)
        ff = self.feed_forward(z)
        x = x + ff
        
        return x