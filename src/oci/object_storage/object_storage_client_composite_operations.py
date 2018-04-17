# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import oci   # noqa: F401


class ObjectStorageClientCompositeOperations(object):

    def __init__(self, client, **kwargs):
        self.client = client
