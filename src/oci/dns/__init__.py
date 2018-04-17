# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import


from .dns_client import DnsClient
from .dns_client_composite_operations import DnsClientCompositeOperations
from . import models

__all__ = ["DnsClient", "DnsClientCompositeOperations", "models"]
