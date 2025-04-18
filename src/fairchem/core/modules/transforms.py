from __future__ import annotations

from typing import TYPE_CHECKING

import torch

from fairchem.core.common.utils import cg_change_mat, irreps_sum

if TYPE_CHECKING:
    from torch_geometric.data import Data
from contextlib import suppress

with suppress(ImportError):
    # TODO remove this in favor of a better solution
    # We should never be importing * from a module
    from fairchem.experimental.foundation_models.multi_task_dataloader.transforms.data_object import *  # noqa


class DataTransforms:
    def __init__(self, config) -> None:
        self.config = config

    def __call__(self, data_object):
        if not self.config:
            return data_object

        for transform_fn in self.config:
            # TODO: Normalization information used in the trainers. Ignore here for now
            # TODO: if we dont use them here, these should not be defined as "transforms" in the config
            # TODO: add them as another entry under dataset, maybe "standardize"?
            if transform_fn in ("normalizer", "element_references"):
                continue

            data_object = eval(transform_fn)(data_object, self.config[transform_fn])

        return data_object
    

def reshape_stress(data_object, config) -> Data:
    if config:
        data_object.stress = data_object.stress.view(1, 3, 3)
    return data_object

def append_fixed(data_object, config) -> Data:
    if config:
        data_object.fixed = torch.zeros_like(data_object.atomic_numbers)
    return data_object

def decompose_tensor(data_object, config) -> Data:
    tensor_key = config["tensor"]
    rank = config["rank"]

    if tensor_key not in data_object:
        return data_object

    if rank != 2:
        raise NotImplementedError

    tensor_decomposition = torch.einsum(
        "ab, cb->ca",
        cg_change_mat(rank),
        data_object[tensor_key].reshape(1, irreps_sum(rank)),
    )

    for decomposition_key in config["decomposition"]:
        irrep_dim = config["decomposition"][decomposition_key]["irrep_dim"]
        data_object[decomposition_key] = tensor_decomposition[
            :,
            max(0, irreps_sum(irrep_dim - 1)) : irreps_sum(irrep_dim),
        ]

    return data_object
