# coding: utf-8
# Copyright (c) 2016, 2026, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import gc
import logging

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

import oci
from oci.fips import is_fips_mode


def _key_pem():
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.TraditionalOpenSSL,
        serialization.NoEncryption()).decode()


def test_is_fips_mode_does_not_accumulate_handlers():
    logger = logging.getLogger("oci.fips.{}".format(id(is_fips_mode)))
    for _ in range(50):
        is_fips_mode()
    assert len(logger.handlers) == 1


def test_client_loggers_do_not_accumulate_handlers():
    config = {
        "user": "ocid1.user.oc1..aaaa",
        "fingerprint": ":".join(["aa"] * 16),
        "tenancy": "ocid1.tenancy.oc1..aaaa",
        "region": "us-ashburn-1",
        "key_content": _key_pem(),
    }
    # Short-lived clients: CPython reuses the freed ids, so new clients
    # get loggers that earlier clients already created.
    for _ in range(200):
        oci.object_storage.ObjectStorageClient(config)
    gc.collect()
    loggers = [lg for name, lg in logging.Logger.manager.loggerDict.items()
               if name.startswith("oci.base_client.") and isinstance(lg, logging.Logger)]
    assert loggers
    assert max(len(lg.handlers) for lg in loggers) == 1
