"""
Copyright (c) Meta Platforms, Inc. and affiliates.

This source code is licensed under the MIT license found in the
LICENSE file in the root directory of this source tree.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("fairchem.demo.ocpapi")
except PackageNotFoundError:
    # package is not installed
    __version__ = ""


from .client import *  # noqa
from .workflows import *  # noqa
