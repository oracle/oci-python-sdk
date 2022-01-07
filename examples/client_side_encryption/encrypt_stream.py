# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Instructions:
# As a pre-requisite for this example you must have a vault created in KMS with at least one master key.
# OCI KMS has APIs that allow creating master keys or importing a previously generated key, either will work.
# You can refer to the example at examples/kms_example.py for an example of how to create a master key.
# Update the values for VAULT_ID and MASTER_KEY_ID below with the values for your vault and key and then run
# the example.

import shutil
import filecmp

import oci

# TODO: populate variables below
VAULT_ID = ""
MASTER_KEY_ID = ""

# load default configuration from ~/.oci/config
config = oci.config.from_file()

# if you want to target a region other than the one specified
# in your config, you must override 'region' in the config
# before initializing the MasterKey and MasterKeyProvider
config['region'] = 'us-phoenix-1'

kms_master_key = oci.encryption.KMSMasterKey(
    config=config, master_key_id=MASTER_KEY_ID, vault_id=VAULT_ID
)

kms_master_key_provider = oci.encryption.KMSMasterKeyProvider(
    config=config,
    kms_master_keys=[kms_master_key]
)

###############################################
# stream encryption / decryption
###############################################
input_payload_file = 'encryption_payload_sample.txt'
encrypted_file = 'encrypted_payload.enc'
decrypted_file = 'decrypted_payload.txt'

# encrypt stream and write to file
encryption_context = {"some_additional_authenticated": "data"}
with open(input_payload_file, 'rb') as input_file, open(encrypted_file, 'wb') as output_file:
    with oci.encryption.create_encryption_stream(
        master_key_provider=kms_master_key_provider,
        stream_to_encrypt=input_file,
        encryption_context=encryption_context,
    ) as encryption_stream:
        # copy bytes from encryption stream to output file incrementally
        shutil.copyfileobj(encryption_stream, output_file)

        # copy bytes from encryption stream to output file all at once
        # output_file.write(encryption_stream.read())

# decrypt stream and write to file
with open(encrypted_file, 'rb') as input_file, open(decrypted_file, 'wb') as decrypted_output_file:
    with oci.encryption.create_decryption_stream(
        master_key_provider=kms_master_key_provider,
        stream_to_decrypt=input_file
    ) as decryption_stream:
        # copy bytes from decryption stream to output file incrementally
        shutil.copyfileobj(decryption_stream, decrypted_output_file)

        # copy bytes from decryption stream to output file all at once
        # decrypted_output_file.write(decryption_stream.read())

        # validate encryption context contains all keys passed in initial encryption context
        # do not check exact equality as the SDK may add additional keys to the returned context
        encryption_context_keys = list(encryption_context)
        for key in encryption_context_keys:
            assert encryption_context[key] == decryption_stream.get_encryption_context()[key]

# validate that decrypted data matches initial payload
assert filecmp.cmp(input_payload_file, decrypted_file)

# decrypt file reading into memory
with open(encrypted_file, 'rb') as input_file:
    with oci.encryption.create_decryption_stream(
        master_key_provider=kms_master_key_provider,
        stream_to_decrypt=input_file
    ) as decryption_stream:
        # copy bytes from decryption stream into memory all at once
        decrypted_content = decryption_stream.read()

with open(input_payload_file, 'rb') as input_file:
    assert input_file.read() == decrypted_content
