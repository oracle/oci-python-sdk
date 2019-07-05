# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import


from .quotas_client import QuotasClient
from .quotas_client_composite_operations import QuotasClientCompositeOperations
from . import models

__all__ = ["QuotasClient", "QuotasClientCompositeOperations", "models"]
