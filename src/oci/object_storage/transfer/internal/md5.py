# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InternalError
from cryptography.exceptions import UnsupportedAlgorithm
import hashlib


def create_checksum_md5():
    """
    Return an MD5 hasher for Object Storage integrity checks.

    Object Storage uses base64-encoded MD5 values for Content-MD5 and
    multipart upload checksum validation. In this context MD5 is a transport
    integrity checksum, not a security primitive.

    This helper intentionally probes MD5 constructor availability instead of
    branching on oci.fips.is_fips_mode(). Some FIPS-enabled hosts can report
    false negatives through runtime FIPS detection, while the actual MD5
    constructor behavior is the only thing the upload path needs to know.

    The fallback order is:
      * hashlib.md5(usedforsecurity=False), for Python versions that support
        explicitly non-security MD5 use.
      * hashlib.new('md5', usedforsecurity=False), for environments where the
        generic constructor is available but the named constructor is not.
      * hashlib.md5(), for older or non-FIPS environments.
      * This module's cryptography-backed md5 wrapper.

    :return: A hash object with update(bytes) and digest() methods.
    :raises ValueError: If no usable MD5 implementation is available.
    """
    try:
        return hashlib.md5(usedforsecurity=False)
    except TypeError:
        # Python versions before 3.9 do not support usedforsecurity.
        pass
    except ValueError:
        pass

    try:
        return hashlib.new('md5', usedforsecurity=False)
    except TypeError:
        pass
    except ValueError:
        pass

    try:
        return hashlib.md5()
    except ValueError:
        pass

    try:
        return md5()
    except (InternalError, UnsupportedAlgorithm, ValueError) as ex:
        raise ValueError("Unable to create MD5 checksum for Object Storage upload") from ex


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
