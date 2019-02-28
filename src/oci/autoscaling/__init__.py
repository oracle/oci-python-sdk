# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import


from .auto_scaling_client import AutoScalingClient
from .auto_scaling_client_composite_operations import AutoScalingClientCompositeOperations
from . import models

__all__ = ["AutoScalingClient", "AutoScalingClientCompositeOperations", "models"]
