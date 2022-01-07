# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import


from .auto_scaling_client import AutoScalingClient
from .auto_scaling_client_composite_operations import AutoScalingClientCompositeOperations
from . import models

__all__ = ["AutoScalingClient", "AutoScalingClientCompositeOperations", "models"]
