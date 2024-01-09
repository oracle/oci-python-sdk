# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import oci
import sys

"""
Example showing how to initialize and use the Yubikey signer.

This example shows the Yubikey signer being used with the
DBaaS service.  The instance must be set up for Yubikey for
this example to work.

The compartment ID must be provided when running the example.

python yubikey_example <compartment_id>
"""


if len(sys.argv) != 2:
    raise RuntimeError('A compartment ID must be provided')

compartment_id = sys.argv[1]

# Create a YubiKey signer
print("Intializing new signer")
config = oci.config.from_file()
ykpin = oci.auth.signers.YubikeyRequestSigner.get_yubikey_pin()
ybsSigner = oci.auth.signers.YubikeyRequestSigner.get_yubikey_signer(config, ykpin)
print("=" * 80)
print("Get Objectstorage namespace")
object_storage_client = oci.object_storage.ObjectStorageClient(config, signer=ybsSigner)
print(object_storage_client.get_namespace().data)
