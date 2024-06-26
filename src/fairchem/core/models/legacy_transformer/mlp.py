import torch
import torch.nn as nn
import torch.nn.functional as F

from typing import Optional

class ResMLP(nn.Module):
    def __init__(
        self,
        input_dim: int = 512,
        hidden_dim: int = 512,
        output_dim: int = 512,
        num_layers: int = 2,
        dropout: float = 0., 
    ):
        super().__init__()
        assert num_layers >= 2

        self.dropout = nn.Dropout(dropout)
        self.activation = nn.SiLU()

        self.linears = nn.ModuleList([
            nn.Linear(hidden_dim, hidden_dim) 
            for _ in range(num_layers - 2)
        ])

        self.input = nn.Linear(input_dim, hidden_dim)
        self.output = nn.Linear(hidden_dim, output_dim)

    def forward(self, x: torch.Tensor, gate: Optional[torch.Tensor] = None):

        x = self.input(x)
        x = self.dropout(x)
        x = self.activation(x)

        for linear in self.linears:
            z = linear(x)
            z = self.dropout(z)
            z = self.activation(z)
            x = x + z

        if gate is not None:
            x = x * gate

        x = self.output(x)

        return x