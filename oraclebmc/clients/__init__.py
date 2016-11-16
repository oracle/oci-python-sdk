# coding: utf-8
# Copyright (c) 2016 Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

from .blockstorage_client import BlockstorageClient
from .compute_client import ComputeClient
from .virtual_network_client import VirtualNetworkClient
from .identity_client import IdentityClient
from .object_storage_client import ObjectStorageClient

__all__ = ["BlockstorageClient", "ComputeClient", "IdentityClient", "ObjectStorageClient", "VirtualNetworkClient"]
