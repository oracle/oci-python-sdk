# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


class md5:
    """
    Wrapper for MD5 implementation in cryptography for when the hashlib MD5
    implementation has be turned off due to FIPS
    """

    def __init__(self):
        self._digest = hashes.Hash(hashes.MD5(), backend=default_backend())

    def update(self, message):
        data = message
        if isinstance(message, memoryview):
            data = message.tobytes()

        self._digest.update(data)

    def digest(self):
        return self._digest.finalize()
