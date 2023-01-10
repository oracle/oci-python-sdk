# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# Instructions:
# As a pre-requisite for this example you must have a vault created in KMS with at least one master key.
# OCI KMS has APIs that allow creating master keys or importing a previously generated key, either will work.
# You can refer to the example at examples/kms_example.py for an example of how to create a master key.
# Update the values for VAULT_ID and MASTER_KEY_ID below with the values for your vault and key and then run
# the example.
# Also update BUCKET_NAME to a bucket in your tenancy that can be used for the upload / download encrypted object
# portion of the sample.

import oci

# TODO: populate variables below
VAULT_ID = ""
MASTER_KEY_ID = ""
BUCKET_NAME = ""

# load default configuration from ~/.oci/config
config = oci.config.from_file()

kms_master_key = oci.encryption.KMSMasterKey(
    config=config, master_key_id=MASTER_KEY_ID, vault_id=VAULT_ID
)

kms_master_key_provider = oci.encryption.KMSMasterKeyProvider(
    config=config,
    kms_master_keys=[kms_master_key]
)

###############################################
# Object Storage examples
###############################################
input_payload_file = 'encryption_payload_sample.txt'
object_name = input_payload_file + '.enc'

object_storage_client = oci.object_storage.ObjectStorageClient(config)
upload_manager = oci.object_storage.UploadManager(object_storage_client)
namespace_name = object_storage_client.get_namespace().data

# encrypt and upload file to object storage
with open(input_payload_file, 'rb') as input_file:
    with oci.encryption.create_encryption_stream(
        master_key_provider=kms_master_key_provider,
        stream_to_encrypt=input_file,
    ) as encryption_stream:
        upload_manager.upload_stream(
            namespace_name=namespace_name,
            bucket_name=BUCKET_NAME,
            object_name=object_name,
            stream_ref=encryption_stream,
        )

print('encrypted object uploaded. namespace: {}, bucket: {}, object: {}'.format(namespace_name, BUCKET_NAME, object_name))

get_obj_response = object_storage_client.get_object(namespace_name=namespace_name, bucket_name=BUCKET_NAME, object_name=object_name)

# download content from object storage and decrypt
with oci.encryption.create_decryption_stream(
    master_key_provider=kms_master_key_provider,
    stream_to_decrypt=get_obj_response.data.raw
) as decryption_stream:
    decrypted_content = decryption_stream.read()

print('decrypted object downloaded. namespace: {}, bucket: {}, object: {}'.format(namespace_name, BUCKET_NAME, object_name))

with open(input_payload_file, 'rb') as input_file:
    assert input_file.read() == decrypted_content
