# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import


from .blockstorage_client import BlockstorageClient
from .blockstorage_client_composite_operations import BlockstorageClientCompositeOperations
from .compute_client import ComputeClient
from .compute_client_composite_operations import ComputeClientCompositeOperations
from .compute_management_client import ComputeManagementClient
from .compute_management_client_composite_operations import ComputeManagementClientCompositeOperations
from .virtual_network_client import VirtualNetworkClient
from .virtual_network_client_composite_operations import VirtualNetworkClientCompositeOperations
from . import models

__all__ = ["BlockstorageClient", "BlockstorageClientCompositeOperations", "ComputeClient", "ComputeClientCompositeOperations", "ComputeManagementClient", "ComputeManagementClientCompositeOperations", "VirtualNetworkClient", "VirtualNetworkClientCompositeOperations", "models"]
