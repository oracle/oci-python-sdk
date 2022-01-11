# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Instructions:
# As a pre-requisite for this example you must have a vault created in KMS with at least one master key.
# OCI KMS has APIs that allow creating master keys or importing a previously generated key, either will work.
# You can refer to the example at examples/kms_example.py for an example of how to create a master key.
# Update the values for VAULT_ID and MASTER_KEY_ID below with the values for your vault and key and then run
# the example.

import oci

# TODO: populate variables below
VAULT_ID = ""
MASTER_KEY_ID = ""

# load default configuration from ~/.oci/config
config = oci.config.from_file()

kms_master_key = oci.encryption.KMSMasterKey(
    config=config, master_key_id=MASTER_KEY_ID, vault_id=VAULT_ID
)

kms_master_key_provider = oci.encryption.KMSMasterKeyProvider(
    config=config,
    kms_master_keys=[kms_master_key]
)

# basic encrypt bytes or string data
data_to_encrypt = b"Sample data to encrypt"
encryption_context = {"some_additional_authenticated": "data"}
crypto_result_encrypt = oci.encryption.encrypt(master_key_provider=kms_master_key_provider, data=data_to_encrypt, encryption_context=encryption_context)
ciphertext = crypto_result_encrypt.get_data()

# basic decrypt bytes or str data
crypto_result_decrypt = oci.encryption.decrypt(master_key_provider=kms_master_key_provider, data=ciphertext)
decrypted_data = crypto_result_decrypt.get_data()

# crypto result includes the encryption context used to decrypt the data
result_encryption_context = crypto_result_decrypt.get_encryption_context()

# validate that decrypted data matches initial payload
assert data_to_encrypt == decrypted_data

# validate encryption context contains all keys passed in initial encryption context
# do not check exact equality as the SDK may add additional keys to the returned context
encryption_context_keys = list(encryption_context)
for key in encryption_context_keys:
    assert encryption_context[key] == crypto_result_decrypt.get_encryption_context()[key]


# You can also decrypt without specifying a specific KMSMasterKey ahead of time
decryption_only_master_key_provider = oci.encryption.KMSMasterKeyProvider(
    config=config
)

crypto_result_decrypt_2 = oci.encryption.decrypt(master_key_provider=decryption_only_master_key_provider, data=ciphertext)
assert data_to_encrypt == crypto_result_decrypt_2.get_data()
