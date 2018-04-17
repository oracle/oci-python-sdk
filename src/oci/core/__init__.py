# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import


from .blockstorage_client import BlockstorageClient
from .blockstorage_client_composite_operations import BlockstorageClientCompositeOperations
from .compute_client import ComputeClient
from .compute_client_composite_operations import ComputeClientCompositeOperations
from .virtual_network_client import VirtualNetworkClient
from .virtual_network_client_composite_operations import VirtualNetworkClientCompositeOperations
from . import models

__all__ = ["BlockstorageClient", "BlockstorageClientCompositeOperations", "ComputeClient", "ComputeClientCompositeOperations", "VirtualNetworkClient", "VirtualNetworkClientCompositeOperations", "models"]
