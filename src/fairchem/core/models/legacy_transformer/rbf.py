import math
import torch
import torch.nn as nn

class GaussianSmearing(nn.Module):
    def __init__(
        self,
        rbf_radius: float = 1,
        num_gaussians: int = 50,
        trainable: bool = False,
        std: float = 0.02,
    ):
        super().__init__()

        offset = torch.linspace(0, rbf_radius, num_gaussians)
        neg_log_var = torch.tensor(- 2 * math.log(std)).repeat(num_gaussians)
        self.origin_log_var = 2 * math.log(std)

        self.offset = nn.Parameter(offset, requires_grad=trainable)
        self.neg_log_var = nn.Parameter(neg_log_var, requires_grad=trainable)

        self.trainable = trainable

    def forward(self, x: torch.Tensor):
        # compute rbfs and embeddings
        shape = x.shape
        x = x.view(-1, 1) - self.offset.view(1, -1)
        x = - 0.5 * x.square() * self.neg_log_var.view(1, -1).exp()
        x = torch.exp(x)
        x = x.view(*shape, -1)
        return x

class RadialBasisFunction(nn.Module):
    def __init__(
        self,
        rbf_radius: float = 1,
        num_gaussians: int = 50,
        embed_dim: int = 128,
        trainable: bool = False
    ):
        super().__init__()

        self.smearing = GaussianSmearing(
            rbf_radius=rbf_radius,
            num_gaussians=num_gaussians,
            trainable=trainable,
            std=rbf_radius/num_gaussians,
        )
        
        self.linear = nn.Linear(num_gaussians, embed_dim, bias=False)

    def forward(self, x: torch.Tensor):
        x = self.smearing(x)
        return self.linear(x)