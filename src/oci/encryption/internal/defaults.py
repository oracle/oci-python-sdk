# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from oci.encryption.algorithms import Algorithm

import math

DEFAULT_ENCODING = "utf-8"

DEFAULT_ALGORITHM = Algorithm.AES_256_GCM_IV12_TAG16

DEFAULT_MAX_GCM_ENCRYPTION_SIZE = int(math.pow(2, 31) - 1)

DEFAULT_MAX_ENCRYPTION_SIZE_SENTINEL = object()
