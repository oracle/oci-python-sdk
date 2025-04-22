# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import
import ctypes.util
import ctypes
import logging
import os
import re
import ssl
import sys


class DevNull:
    """
    Simple class to supress errors which may occur when importing hashlib
    in FIPS mode.
    """
    def write(self, msg):
        pass


def get_openssl_version():
    version_str = ssl.OPENSSL_VERSION
    match = re.search(r'OpenSSL (\d+\.\d+\.\d+)', version_str)
    if match:
        return match.group(1)
    else:
        return version_str


def override_libcrypto(fips_libcrypto_path):
    """
    Override libcrypto and add FIPS_mode function to ssl if it is not there
    """
    logger = logging.getLogger("{}.{}".format(__name__, id(override_libcrypto)))
    logger.addHandler(logging.NullHandler())
    openssl_version = get_openssl_version()
    if openssl_version.startswith("1") and fips_libcrypto_path is not None:
        # Handle Openssl 1
        _bs_crypto = ctypes.CDLL(fips_libcrypto_path)
        _bs_crypto.FIPS_mode_set(ctypes.c_int(1))
        import ssl  # noqa: E402
        if not hasattr(ssl, 'FIPS_mode'):
            ssl.FIPS_mode = _bs_crypto.FIPS_mode


def md5(initial_message=''):
    """
    Placeholder md5 function for hashlib so it won't segfault when called after
    enabling FIPS mode.
    """
    raise ValueError("md5 disabled for fips")
    return None


def patch_hashlib_md5():
    """
    hashlib.md5 is imported by urllib3, which is required by requests,
    which is used by oci (python sdk).  This will cause errors so we need to
    patch hashlib.
    """

    stderr = sys.stderr
    try:
        sys.stderr = DevNull()
        import hashlib  # noqa: E402
    except (RuntimeError, ValueError):
        pass
    sys.stderr = stderr
    hashlib.md5 = md5


def is_fips_mode():
    """
    Verify that ssl.FIPS_mode() returns 1 and that using md5 raises an
    exception
    """
    logger = logging.getLogger("{}.{}".format(__name__, id(is_fips_mode)))
    logger.addHandler(logging.NullHandler())
    openssl_version = get_openssl_version()
    if openssl_version.startswith("1"):
        import ssl
        if not hasattr(ssl, 'FIPS_mode'):
            return False
        elif ssl.FIPS_mode() != 1:
            return False

    # check if hashlib has been disabled
    import hashlib
    try:
        digest = hashlib.md5(b"Hello World\n").hexdigest()  # noqa: F841
        return False
    except ValueError:
        # Expect to get this exception so do nothing
        pass
    return True


def enable_fips_mode(fips_libcrypto_path=None):
    """
    Enable FIPS mode by overriding libcrypto and patching hashlib
    """
    openssl_version = get_openssl_version()
    logger = logging.getLogger("{}.{}".format(__name__, id(enable_fips_mode)))
    logger.addHandler(logging.NullHandler())

    if not fips_libcrypto_path:
        if 'FIPS_LIBCRYPTO_PATH' in os.environ:
            fips_libcrypto_path = os.environ['FIPS_LIBCRYPTO_PATH']
        elif 'OCI_PYTHON_SDK_FIPS_LIBCRYPTO_PATH' in os.environ:
            fips_libcrypto_path = os.environ['OCI_PYTHON_SDK_FIPS_LIBCRYPTO_PATH']

    if fips_libcrypto_path:
        if openssl_version.startswith("1"):
            override_libcrypto(fips_libcrypto_path)

            import hashlib
            try:
                digest = hashlib.md5(b"Hello World\n").hexdigest()  # noqa: F841

                # If the previous line did not raise an exception md5 needs to be
                # patched
                patch_hashlib_md5()

            except ValueError:
                # Expect to get this exception so do nothing
                pass

            logger.info("Using '{}' for libcypto".format(fips_libcrypto_path))
            if is_fips_mode():
                logger.info("FIPS mode is active")
            else:
                logger.error("Failed to enter FIPS mode")
        else:
            # Warn users who set the FIPS crypto path via environment variable that FIPS mode needs to be set in OS
            logger.warning("FIPS mode for openssl version {} needs to be set in your operating system!".format(openssl_version))
