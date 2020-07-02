# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import time
import oci
import pytest
import json
import io
import os
import struct
import shutil
import tempfile
import filecmp
import math

from oci._vendor import six
from oci.encryption.algorithms import Algorithm

from oci.encryption.internal.utils import (
    convert_to_bytes
)

from oci.encryption.internal.defaults import DEFAULT_MAX_ENCRYPTION_SIZE_SENTINEL

MASTER_KEY_AND_VAULT_FOR_TENANCY_AND_REGION = {
    # dex-us-phoenix-1
    "ocid1.tenancy.oc1..aaaaaaaa5nfwo53cezleyy6t73v6rn6knhu3molvptnl3kcq34l5zb7ptiaq": {
        'us-phoenix-1': (
            "ocid1.vault.oc1.phx.a5pgvhpkaadfa.abyhqljreadhmvhhlkablvnifggtbhm5w4xjaizuzrbdow5y5wgll7ploz2a",
            "ocid1.key.oc1.phx.a5pgvhpkaadfa.abyhqljrabndwgftbhqwd2zfwyhcyvucosoiw5j6oc47ecbnkhiyasiyvrga"
        ),
        'us-ashburn-1': (
            "ocid1.vault.oc1.iad.bbpgx4gdaacuu.abuwcljr2ar44wnsolwdizlzrkzusqog6tujpkw352woz6sb2vnmhps44txa",
            "ocid1.key.oc1.iad.bbpgx4gdaacuu.abuwcljrpbs5hfjzrbbz7ot5letlsmk7n4sncvekathvxn3jodn5xnzmbdfq"
        )
    },
    # bmcs-dex-us-ashburn-1
    "ocid1.tenancy.oc1..aaaaaaaayqotwvxvy4t433xh3b5ccj4z3w6ke4t4m2sjlib32lyio244pucq": {
        'us-ashburn-1': (
            "ocid1.vault.oc1.iad.bbpdrfg5aaeuk.abuwcljtbbdktfykyoc6uwyoilfcd5eatmtcxqjcgvdfswro6mwqtlke25ya",
            "ocid1.key.oc1.iad.bbpdrfg5aaeuk.abuwcljro6nnx3rvkpdxloiwbdyqfqlmgjcyoqlgyd4e7pzn7oeyfyfaib3q"
        ),
        'us-phoenix-1': (
            "ocid1.vault.oc1.phx.a5pgx4bnaafqw.abyhqljtvq67gr3eip4mu5xnweejy73cxdzjhisys7an7bmov5mssmqe3mla",
            "ocid1.key.oc1.phx.a5pgx4bnaafqw.abyhqljs3nu2gla3jg2woiraz5scqdyhkkcqnk7yghztyfpef5j7vkwpcxha"
        )
    }
}

MASTER_KEY_LENGTH = 16
MASTER_KEY_ALGORITHM = oci.key_management.models.KeyShape.ALGORITHM_AES

BYTES_IN_MEBIBYTE = int(math.pow(2, 20))
LARGE_FILE_TEST_SIZE_MB = 1100
SMALL_FILE_TEST_SIZE_MB = 1


@pytest.fixture(scope="function", autouse=True)
def label():
    current_test_name = os.environ.get('PYTEST_CURRENT_TEST')
    print("Running test: {}".format(current_test_name))
    yield


@pytest.fixture(scope="module")
def vault_id(config):
    tenancy_id = config['tenancy']
    region = config['region']

    key_and_vault_for_tenancy = MASTER_KEY_AND_VAULT_FOR_TENANCY_AND_REGION.get(tenancy_id)
    if not key_and_vault_for_tenancy:
        raise ValueError("No master key and vault are configured for this tenancy: {}".format(tenancy_id))

    key_and_vault_for_region = key_and_vault_for_tenancy.get(region)
    if not key_and_vault_for_region:
        raise ValueError("No master key and vault are configured the region: {} within tenancy: {}".format(region, tenancy_id))

    return key_and_vault_for_region[0]


@pytest.fixture(scope="module")
def master_key_id(config):
    tenancy_id = config['tenancy']
    region = config['region']

    key_and_vault_for_tenancy = MASTER_KEY_AND_VAULT_FOR_TENANCY_AND_REGION.get(tenancy_id)
    if not key_and_vault_for_tenancy:
        raise ValueError("No master key and vault are configured for this tenancy: {}".format(tenancy_id))

    key_and_vault_for_region = key_and_vault_for_tenancy.get(region)
    if not key_and_vault_for_region:
        raise ValueError("No master key and vault are configured the region: {} within tenancy: {}".format(region, tenancy_id))

    return key_and_vault_for_region[1]


@pytest.fixture(scope="module")
def large_random_file_path():
    large_random_file = create_named_file_with_random_content(LARGE_FILE_TEST_SIZE_MB)

    yield large_random_file.name

    if large_random_file:
        large_random_file.close()

        if os.path.exists(large_random_file.name):
            os.remove(large_random_file.name)


@pytest.fixture(scope="module")
def small_random_file_path():
    small_random_file = create_named_file_with_random_content(SMALL_FILE_TEST_SIZE_MB)

    yield small_random_file.name

    if small_random_file:
        small_random_file.close()

        if os.path.exists(small_random_file.name):
            os.remove(small_random_file.name)


def create_named_file_with_content(content):
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(content)
    f.seek(0)
    return f


def create_named_file_with_random_content(size_in_mbs):
    print("Creating {} MiB file...".format(size_in_mbs))
    t1 = time.time()
    size_in_bytes = int(size_in_mbs * BYTES_IN_MEBIBYTE)
    chunk_size_in_bytes = int(250 * BYTES_IN_MEBIBYTE)
    total_size_in_bytes = 0
    f = tempfile.NamedTemporaryFile(delete=False)
    while total_size_in_bytes <= size_in_bytes and (chunk_size_in_bytes != 0):
        if (total_size_in_bytes + chunk_size_in_bytes) > size_in_bytes:
            chunk_size_in_bytes = size_in_bytes - total_size_in_bytes
            data = os.urandom(chunk_size_in_bytes)
        else:
            data = os.urandom(1024) * int(chunk_size_in_bytes / 1024)

        f.write(data)
        total_size_in_bytes += len(data)

    f.seek(0)
    t2 = time.time()
    print("Took {} seconds to generate file".format(t2 - t1))
    return f


########################
# max encryption size
########################
def test_client_side_encryption_stream_exceed_max_encryption_size_gcm(config, vault_id, master_key_id, small_random_file_path):
    with open(small_random_file_path, 'rb') as small_random_file:
        with pytest.raises(ValueError) as exc_info:
            encrypt_decrypt_stream(config, vault_id, master_key_id, small_random_file, read_data_all_at_once=False, max_encryption_size=100)

    assert "_max_encryption_size" in str(exc_info)


def test_client_side_encryption_stream_full_read_exceed_max_encryption_size(config, vault_id, master_key_id, small_random_file_path):
    with open(small_random_file_path, 'rb') as small_random_file:
        with pytest.raises(ValueError) as exc_info:
            encrypt_decrypt_stream(config, vault_id, master_key_id, small_random_file, read_data_all_at_once=True, max_encryption_size=100)

    assert "_max_encryption_size" in str(exc_info)


################################################
# Data
################################################
def test_client_side_encryption_empty_bytes_gcm(config, vault_id, master_key_id):
    encrypt_decrypt_data(config, vault_id, master_key_id, b"")


def test_client_side_encryption_string_gcm(config, vault_id, master_key_id):
    encrypt_decrypt_data(config, vault_id, master_key_id, "This is a secret payload encrypted using AES-GCM")


def test_client_side_encryption_bytes_gcm(config, vault_id, master_key_id):
    encrypt_decrypt_data(config, vault_id, master_key_id, b"This is a secret payload encrypted using AES-GCM")


def test_client_side_encryption_bytes_with_context_gcm(config, vault_id, master_key_id):
    encrypt_decrypt_data(config, vault_id, master_key_id, b"This is a secret payload encrypted using AES-GCM", encryption_context={"foo": "bar"})


def test_client_side_encryption_bytes_with_context_with_utf8_char_gcm(config, vault_id, master_key_id):
    if str == bytes:
        with pytest.raises(ValueError) as exc_info:
            encrypt_decrypt_data(config, vault_id, master_key_id, b"This is a secret payload encrypted using AES-GCM", encryption_context={"\xe1": "bar"})

        assert "encryption_context" in str(exc_info)
    else:
        encrypt_decrypt_data(config, vault_id, master_key_id, b"This is a secret payload encrypted using AES-GCM", encryption_context={"\xe1": "bar"})


def test_client_side_encryption_bytes_with_empty_dict_context_gcm(config, vault_id, master_key_id):
    encrypt_decrypt_data(config, vault_id, master_key_id, b"This is a secret payload encrypted using AES-GCM", encryption_context={})


def test_client_side_encryption_bytes_with_explicit_none_context_gcm(config, vault_id, master_key_id):
    encrypt_decrypt_data(config, vault_id, master_key_id, b"This is a secret payload encrypted using AES-GCM", encryption_context=None)


def test_client_side_encryption_bytes_context_with_invalid_type_gcm(config, vault_id, master_key_id):
    with pytest.raises(TypeError) as exc_info:
        encrypt_decrypt_data(config, vault_id, master_key_id, b"This is a secret payload encrypted using AES-GCM", encryption_context="some invalid encryption context")

    assert "encryption_context" in str(exc_info)


def test_client_side_encryption_bytes_context_with_invalid_key_gcm(config, vault_id, master_key_id):
    with pytest.raises(ValueError) as exc_info:
        encrypt_decrypt_data(config, vault_id, master_key_id, b"This is a secret payload encrypted using AES-GCM", encryption_context={"oci-foo": "bar"})

    assert "encryption_context" in str(exc_info)
    assert "oci-foo" in str(exc_info)


def test_client_side_encryption_large_string_gcm(config, vault_id, master_key_id, large_random_file_path):
    with open(large_random_file_path, 'rb') as large_random_file:
        content = large_random_file.read()
        encrypt_decrypt_data(config, vault_id, master_key_id, content)


################################################
# Encryption context validation
################################################
def test_client_side_encryption_bytes_context_with_int_value(config, vault_id, master_key_id):
    with pytest.raises(TypeError) as exc_info:
        oci.encryption.internal.streaming._validate_encryption_context({"foo": 2, "bar": "baz"})

    assert "encryption_context" in str(exc_info)


def test_client_side_encryption_bytes_context_with_bytes_keys(config, vault_id, master_key_id):
    if bytes == str:
        # in python 2 this should execute without error because there is no true 'bytes' type
        # they just become strings
        oci.encryption.internal.streaming._validate_encryption_context({b"foo": b"bar"})
    else:
        # in python 3 we explicitly disallow keys and values of type 'bytes'
        with pytest.raises(TypeError) as exc_info:
            oci.encryption.internal.streaming._validate_encryption_context({b"foo": b"bar"})

        assert "encryption_context" in str(exc_info)


################################################
# Streaming
################################################
def test_client_side_encryption_empty_stream_full_read_gcm(config, vault_id, master_key_id):
    input_stream = create_named_file_with_content(b"")
    encrypt_decrypt_stream(config, vault_id, master_key_id, input_stream)


def test_client_side_encryption_non_seekable_stream(config, vault_id, master_key_id):
    content_to_encrypt = b"This is a secret payload encrypted using streams and AES-GCM"

    class NonSeekableStream(object):
        def __init__(self, internal_stream_content):
            self.internal_stream_content = internal_stream_content

        def read(self, size=-1):
            return self.internal_stream_content.read(size)

        def seekable(self):
            return False

        def seek(self, offset, whence=os.SEEK_SET):
            raise NotImplementedError()

    input_stream = NonSeekableStream(io.BytesIO(content_to_encrypt))

    kms_master_key = oci.encryption.KMSMasterKey(
        config=config, master_key_id=master_key_id, vault_id=vault_id
    )

    kms_master_key_provider = oci.encryption.KMSMasterKeyProvider(
        config=config,
        kms_master_keys=[kms_master_key]
    )

    with tempfile.NamedTemporaryFile(delete=False) as encrypted_output_file:
        with oci.encryption.create_encryption_stream(
            master_key_provider=kms_master_key_provider,
            stream_to_encrypt=input_stream
        ) as encryption_stream:
            encrypted_output_file.write(encryption_stream.read())

        encrypted_output_file.seek(0)
        output_content = encrypted_output_file.read()

    crypto_result = oci.encryption.decrypt(data=output_content, master_key_provider=kms_master_key_provider)
    assert crypto_result.get_data() == content_to_encrypt


def test_client_side_encryption_stream_full_read_gcm(config, vault_id, master_key_id):
    content_to_encrypt = b"This is a secret payload encrypted using streams and AES-GCM"
    input_stream = create_named_file_with_content(content_to_encrypt)
    encrypt_decrypt_stream(config, vault_id, master_key_id, input_stream)


def test_client_side_encryption_string_stream_full_read_gcm(config, vault_id, master_key_id):
    input_stream = io.StringIO(u"This is a secret payload encrypted using streams and AES-GCM")
    encrypt_decrypt_stream(config, vault_id, master_key_id, input_stream)


def test_client_side_encryption_stream_incremental_gcm(config, vault_id, master_key_id):
    content_to_encrypt = b"This is a secret payload encrypted using streams and AES-GCM"
    input_stream = create_named_file_with_content(content_to_encrypt)

    # explcitly read in small chunks (less than header size to verify proper buffering of header data)
    encrypt_decrypt_stream(config, vault_id, master_key_id, input_stream, read_data_all_at_once=False, read_data_chunk_size=10)


def test_client_side_encryption_stream_incremental_with_context_gcm(config, vault_id, master_key_id):
    content_to_encrypt = b"This is a secret payload encrypted using streams and AES-GCM"
    input_stream = create_named_file_with_content(content_to_encrypt)

    # explcitly read in small chunks (less than header size to verify proper buffering of header data)
    encrypt_decrypt_stream(config, vault_id, master_key_id, input_stream, read_data_all_at_once=False, read_data_chunk_size=10, encryption_context={"foo": "bar"})


def test_client_side_encryption_stream_large_file_full_read_gcm(config, vault_id, master_key_id, large_random_file_path):
    with open(large_random_file_path, 'rb') as large_random_file:
        encrypt_decrypt_stream(config, vault_id, master_key_id, large_random_file, max_encryption_size=None)


def test_client_side_encryption_stream_large_file_incremental_gcm(config, vault_id, master_key_id, large_random_file_path):
    with open(large_random_file_path, 'rb') as large_random_file:
        encrypt_decrypt_stream(config, vault_id, master_key_id, large_random_file, read_data_all_at_once=False, max_encryption_size=None)


def test_client_side_encryption_fetch_context_before_any_read(config, vault_id, master_key_id):
    kms_master_key = oci.encryption.KMSMasterKey(
        config=config, master_key_id=master_key_id, vault_id=vault_id
    )

    kms_master_key_provider = oci.encryption.KMSMasterKeyProvider(
        config=config,
        kms_master_keys=[kms_master_key]
    )

    encryption_context = {"foo": "bar", "baz": "foo"}
    content = b"this is some content to encrypt"
    crypto_result = oci.encryption.encrypt(master_key_provider=kms_master_key_provider, data=content, encryption_context=encryption_context)
    ciphertext = crypto_result.get_data()

    stream_to_decrypt = io.BytesIO(ciphertext)
    decryption_stream = oci.encryption.create_decryption_stream(stream_to_decrypt=stream_to_decrypt, master_key_provider=kms_master_key_provider)
    result_encryption_context = decryption_stream.get_encryption_context()

    for key, value in six.iteritems(encryption_context):
        assert result_encryption_context[key] == value

    # test read 0 bytes
    assert len(decryption_stream.read(0)) == 0


def test_client_side_encryption_failed_encryption_gcm(config, vault_id, master_key_id):
    # Encrypt string example
    kms_master_key = oci.encryption.KMSMasterKey(
        config=config, master_key_id=master_key_id, vault_id=vault_id
    )

    kms_master_key_provider = oci.encryption.KMSMasterKeyProvider(
        config=config,
        kms_master_keys=[kms_master_key]
    )

    # Decrypt string example
    with pytest.raises(ValueError) as exc_info:
        oci.encryption.decrypt(data=b"invalidencrypteddata", master_key_provider=kms_master_key_provider)

    assert "Could not deserialize header" in str(exc_info)


################################################
# Cross-region
################################################
def test_client_side_encryption_key_provider_can_decrypt_payloads_from_multiple_regions_in_same_tenancy(config):
    tenancy_id = config['tenancy']
    vault_and_key_for_tenancy = MASTER_KEY_AND_VAULT_FOR_TENANCY_AND_REGION.get(tenancy_id)
    if not vault_and_key_for_tenancy:
        raise ValueError("No vault and keys configured for tenancy: {}".format(tenancy_id))

    if len(vault_and_key_for_tenancy) < 2:
        raise ValueError("Test required configuring vault + keys across at least 2 regions for tenancy: {}".format(tenancy_id))

    # create configs explicitly for 2 different regions
    region_1 = list(vault_and_key_for_tenancy)[0]
    region_2 = list(vault_and_key_for_tenancy)[1]

    region_1_vault_and_key = vault_and_key_for_tenancy[region_1]

    region_1_explicit_config = config.copy()
    region_1_explicit_config['region'] = region_1

    region_2_explicit_config = config.copy()
    region_2_explicit_config['region'] = region_2

    # encrypt data with vault + key in region 1
    data_to_encrypt = b"This is a secret message encrypted in region 1"
    kms_master_key_region_1 = oci.encryption.KMSMasterKey(
        config=region_1_explicit_config, master_key_id=region_1_vault_and_key[1], vault_id=region_1_vault_and_key[0]
    )

    kms_master_key_provider_region_1 = oci.encryption.KMSMasterKeyProvider(
        config=region_1_explicit_config,
        kms_master_keys=[kms_master_key_region_1]
    )

    encrypt_crypto_result = oci.encryption.encrypt(master_key_provider=kms_master_key_provider_region_1, data=data_to_encrypt)

    # decrypt with KMSMasterKeyProvider configured for region 2 in same tenancy
    kms_master_key_provider_region_2 = oci.encryption.KMSMasterKeyProvider(
        config=region_2_explicit_config
    )

    decrypt_crypto_result = oci.encryption.decrypt(master_key_provider=kms_master_key_provider_region_2, data=encrypt_crypto_result.get_data())

    assert decrypt_crypto_result.get_data() == data_to_encrypt


################################################
# Serialization / Deserialization
################################################
def test_client_side_encryption_deserialize_header_invalid_serialization_format_version(config):
    header = io.BytesIO(struct.pack(">H", 0x0000))
    with pytest.raises(ValueError) as exc_info:
        oci.encryption.internal.serialization.deserialize_header_from_stream(header)

    assert "unrecognized serialization format version" in str(exc_info)


def test_client_side_encryption_deserialize_header_invalid_header(config):
    content = io.BytesIO(b"somepayloadthatisnotavalidencryptedpayload")
    with pytest.raises(ValueError) as exc_info:
        oci.encryption.internal.serialization.deserialize_header_from_stream(content)

    assert "unrecognized serialization format version" in str(exc_info)


def test_client_side_encryption_deserialize_header_invalid_json(config):
    header = io.BytesIO(struct.pack(">HI2s", 0x0001, 2, b"{]"))
    with pytest.raises(ValueError) as exc_info:
        oci.encryption.internal.serialization.deserialize_header_from_stream(header)

    assert "Could not parse metadata" in str(exc_info)


def test_client_side_encryption_deserialize_header_missing_top_level_fields(config):
    header = io.BytesIO(struct.pack(">HI2s", 0x0001, 2, b"{}"))
    with pytest.raises(ValueError) as exc_info:
        oci.encryption.internal.serialization.deserialize_header_from_stream(header)

    assert "keys must be present" in str(exc_info)


def test_client_side_encryption_deserialize_header_missing_dek_fields():
    header_dict = {
        "iv": "123",
        "algorithmId": 0,
        "additionalAuthenticatedData": "",
        "encryptedDataKeys": [{}]
    }

    metadata_content = json.dumps(header_dict)

    header = io.BytesIO(struct.pack(">HI{}s".format(len(metadata_content)), 0x0001, len(metadata_content), convert_to_bytes(metadata_content)))
    with pytest.raises(ValueError) as exc_info:
        oci.encryption.internal.serialization.deserialize_header_from_stream(header)

    assert "keys must be present" in str(exc_info)


################################################
# Closing streams
################################################
def test_client_side_encryption_encryption_stream_close(config, vault_id, master_key_id):
    content_to_encrypt = b"This is a secret payload encrypted using streams and AES-GCM"
    input_stream = io.BytesIO(content_to_encrypt)

    kms_master_key = oci.encryption.KMSMasterKey(
        config=config, master_key_id=master_key_id, vault_id=vault_id
    )

    kms_master_key_provider = oci.encryption.KMSMasterKeyProvider(
        config=config,
        kms_master_keys=[kms_master_key]
    )

    with oci.encryption.create_encryption_stream(
        master_key_provider=kms_master_key_provider,
        stream_to_encrypt=input_stream
    ) as encryption_stream:
        encryption_stream.read()

        # duplicate read is fine as long as stream it not yet closed
        assert len(encryption_stream.read()) == 0

        assert not encryption_stream._closed

    # check we do not close the stream that was passed in
    assert not input_stream.closed

    # check that we do close encryption stream
    # this is not a public property, but in the test we can validate it
    assert encryption_stream._closed

    # validate reading from closed stream produces ValueError
    with pytest.raises(ValueError):
        encryption_stream.read()


def test_client_side_encryption_decryption_stream_close(config, vault_id, master_key_id):
    content_to_encrypt = b"This is a secret payload encrypted using streams and AES-GCM"

    kms_master_key = oci.encryption.KMSMasterKey(
        config=config, master_key_id=master_key_id, vault_id=vault_id
    )

    kms_master_key_provider = oci.encryption.KMSMasterKeyProvider(
        config=config,
        kms_master_keys=[kms_master_key]
    )

    crypto_result = oci.encryption.encrypt(data=content_to_encrypt, master_key_provider=kms_master_key_provider)

    ciphertext_stream = io.BytesIO(crypto_result.get_data())
    with oci.encryption.create_decryption_stream(
        master_key_provider=kms_master_key_provider,
        stream_to_decrypt=ciphertext_stream
    ) as decryption_stream:
        decryption_stream.read()

        # duplicate read is fine as long as stream it not yet closed
        assert len(decryption_stream.read()) == 0

        assert not decryption_stream._closed

    # check we do not close the stream that was passed in
    assert not ciphertext_stream.closed

    # check that we do close encryption stream
    # this is not a public property, but in the test we can validate it
    assert decryption_stream._closed

    # validate reading from closed stream produces ValueError
    with pytest.raises(ValueError):
        decryption_stream.read()


def test_client_side_encryption_get_encryption_context_from_closed_decryption_stream_before_header_is_read(config, vault_id, master_key_id):
    content_to_encrypt = b"This is a secret payload encrypted using streams and AES-GCM"
    encryption_context = {"foo": "bar"}

    kms_master_key = oci.encryption.KMSMasterKey(
        config=config, master_key_id=master_key_id, vault_id=vault_id
    )

    kms_master_key_provider = oci.encryption.KMSMasterKeyProvider(
        config=config,
        kms_master_keys=[kms_master_key]
    )

    crypto_result = oci.encryption.encrypt(data=content_to_encrypt, master_key_provider=kms_master_key_provider, encryption_context=encryption_context)

    ciphertext_stream = io.BytesIO(crypto_result.get_data())
    with oci.encryption.create_decryption_stream(
        master_key_provider=kms_master_key_provider,
        stream_to_decrypt=ciphertext_stream
    ) as decryption_stream:
        # don't read anything and let the stream close
        pass

    # check that we do close encryption stream
    # this is not a public property, but in the test we can validate it
    assert decryption_stream._closed

    # nothing has been read from the stream yet (including the header)
    # so validate that trying to get the encryption context, attempts to read
    # the header from the stream and throws an error since the stream is closed
    with pytest.raises(ValueError):
        decryption_stream.get_encryption_context()


def test_client_side_encryption_get_encryption_context_from_closed_decryption_stream_after_header_is_read(config, vault_id, master_key_id):
    content_to_encrypt = b"This is a secret payload encrypted using streams and AES-GCM"
    encryption_context = {"foo": "bar"}

    kms_master_key = oci.encryption.KMSMasterKey(
        config=config, master_key_id=master_key_id, vault_id=vault_id
    )

    kms_master_key_provider = oci.encryption.KMSMasterKeyProvider(
        config=config,
        kms_master_keys=[kms_master_key]
    )

    crypto_result = oci.encryption.encrypt(data=content_to_encrypt, master_key_provider=kms_master_key_provider, encryption_context=encryption_context)

    ciphertext_stream = io.BytesIO(crypto_result.get_data())
    with oci.encryption.create_decryption_stream(
        master_key_provider=kms_master_key_provider,
        stream_to_decrypt=ciphertext_stream
    ) as decryption_stream:
        # read entire stream
        decryption_stream.read()

    # check that we do close encryption stream
    # this is not a public property, but in the test we can validate it
    assert decryption_stream._closed

    # stream is closed but it already has read the header so validate
    # that caller can fetch the encryption contet without error
    assert decryption_stream.get_encryption_context()


def test_client_side_encryption_get_encryption_context_from_open_decryption_stream(config, vault_id, master_key_id):
    content_to_encrypt = b"This is a secret payload encrypted using streams and AES-GCM"
    encryption_context = {"foo": "bar"}

    kms_master_key = oci.encryption.KMSMasterKey(
        config=config, master_key_id=master_key_id, vault_id=vault_id
    )

    kms_master_key_provider = oci.encryption.KMSMasterKeyProvider(
        config=config,
        kms_master_keys=[kms_master_key]
    )

    crypto_result = oci.encryption.encrypt(data=content_to_encrypt, master_key_provider=kms_master_key_provider, encryption_context=encryption_context)

    ciphertext_stream = io.BytesIO(crypto_result.get_data())
    with oci.encryption.create_decryption_stream(
        master_key_provider=kms_master_key_provider,
        stream_to_decrypt=ciphertext_stream
    ) as decryption_stream:
        # get_encryption_context to force reading of header
        assert decryption_stream.get_encryption_context()

    # check that we do close encryption stream
    # this is not a public property, but in the test we can validate it
    assert decryption_stream._closed


################################################
# Exceptions
################################################
def test_client_side_encryption_non_existent_vault_id(config, master_key_id, vault_id):
    with pytest.raises(RuntimeError) as exc_info:
        oci.encryption.KMSMasterKey(
            config=config, master_key_id=master_key_id, vault_id="ocid1.vault.oc1.phx.a5pgvhpkaadfa.doesnt_exist"
        )

    if six.PY2:
        assert "caused by" in str(exc_info).lower()
    else:
        assert isinstance(exc_info.value.__cause__, oci.exceptions.ServiceError)


def test_client_side_encryption_non_existent_master_key_id_decrypt(config, master_key_id, vault_id):
    with pytest.raises(RuntimeError) as exc_info:
        kms_master_key = oci.encryption.KMSMasterKey(
            config=config, master_key_id="ocid1.key.oc1.phx.a5pgvhpkaadfa.doesnt_exist", vault_id=vault_id
        )

        kms_master_key.decrypt(b"some bytes to decrypt")

    if six.PY2:
        assert "caused by" in str(exc_info).lower()
    else:
        assert isinstance(exc_info.value.__cause__, oci.exceptions.ServiceError)


def test_client_side_encryption_non_existent_master_key_id_generate_data_encryption_key(config, master_key_id, vault_id):
    with pytest.raises(RuntimeError) as exc_info:
        kms_master_key = oci.encryption.KMSMasterKey(
            config=config, master_key_id="ocid1.key.oc1.phx.a5pgvhpkaadfa.doesnt_exist", vault_id=vault_id
        )

        kms_master_key.generate_data_encryption_key(Algorithm.AES_256_GCM_IV12_TAG16)

    if six.PY2:
        assert "caused by" in str(exc_info).lower()
    else:
        assert isinstance(exc_info.value.__cause__, oci.exceptions.ServiceError)


def encrypt_decrypt_data(config, vault_id, master_key_id, data, encryption_context=None):

    kms_master_key = oci.encryption.KMSMasterKey(
        config=config, master_key_id=master_key_id, vault_id=vault_id
    )

    encryption_master_key_provider = oci.encryption.KMSMasterKeyProvider(
        config=config,
        kms_master_keys=[kms_master_key]
    )

    t1 = time.time()
    crypto_result = oci.encryption.encrypt(master_key_provider=encryption_master_key_provider, data=data, encryption_context=encryption_context)
    ciphertext = crypto_result.get_data()
    t2 = time.time()
    print("Time to encrypt {}: {}".format(sizeof_fmt(len(data)), t2 - t1))

    # Decrypt string example using a newly initialized KMSMasterKeyProvider
    # with no master keys to test initializing a master key on the fly
    decryption_master_key_provider = oci.encryption.KMSMasterKeyProvider(
        config=config,
    )

    t1 = time.time()
    crypto_result = oci.encryption.decrypt(data=ciphertext, master_key_provider=decryption_master_key_provider)
    t2 = time.time()
    print("Time to decrypt {} without supplying master key: {}".format(sizeof_fmt(len(data)), t2 - t1))

    assert crypto_result.get_data() == convert_to_bytes(data)
    assert crypto_result.get_encryption_context() is not None

    if encryption_context:
        for key, value in six.iteritems(encryption_context):
            assert crypto_result.get_encryption_context()[key] == value

    # Decrypt string example using the same KMSMasterKeyProvider as for
    # encryption
    t1 = time.time()
    crypto_result = oci.encryption.decrypt(data=ciphertext, master_key_provider=encryption_master_key_provider)
    t2 = time.time()
    print("Time to decrypt {}: {}".format(sizeof_fmt(len(data)), t2 - t1))

    assert crypto_result.get_data() == convert_to_bytes(data)
    assert crypto_result.get_encryption_context() is not None

    if encryption_context:
        for key, value in six.iteritems(encryption_context):
            assert crypto_result.get_encryption_context()[key] == value


def encrypt_decrypt_stream(
    config,
    vault_id,
    master_key_id,
    input_stream,
    read_data_all_at_once=True,
    read_data_chunk_size=None,
    max_encryption_size=DEFAULT_MAX_ENCRYPTION_SIZE_SENTINEL,
    encryption_context=None
):
    kms_master_key = oci.encryption.KMSMasterKey(
        config=config, master_key_id=master_key_id, vault_id=vault_id
    )

    kms_master_key_provider = oci.encryption.KMSMasterKeyProvider(
        config=config,
        kms_master_keys=[kms_master_key]
    )

    try:
        encrypted_output_file = None
        decrypted_output_file = None

        encrypted_output_file = tempfile.NamedTemporaryFile(delete=False)

        input_stream.seek(0)

        # write encrypted content to encrypted_output_file
        t1 = time.time()
        with oci.encryption.create_encryption_stream(
            master_key_provider=kms_master_key_provider,
            stream_to_encrypt=input_stream,
            max_encryption_size=max_encryption_size,
            encryption_context=encryption_context,
        ) as encryption_stream:
            if read_data_all_at_once:
                content = encryption_stream.read()
                encrypted_output_file.write(content)
            else:
                kwargs = {}
                if read_data_chunk_size:
                    kwargs["length"] = read_data_chunk_size

                shutil.copyfileobj(encryption_stream, encrypted_output_file, **kwargs)

            t2 = time.time()
            print("Time to encrypt {}: {}".format(sizeof_fmt(encryption_stream._bytes_written_total), t2 - t1))

        # reset encrypted_output_file before we read from it again
        encrypted_output_file.seek(0)

        # write decrypted content to decrypted_output_file
        decrypted_output_file = tempfile.NamedTemporaryFile(delete=False)

        t1 = time.time()
        with oci.encryption.create_decryption_stream(
            stream_to_decrypt=encrypted_output_file,
            master_key_provider=kms_master_key_provider
        ) as decryption_stream:
            if read_data_all_at_once:
                decrypted_output_file.write(decryption_stream.read())
            else:
                kwargs = {}
                if read_data_chunk_size:
                    kwargs["length"] = read_data_chunk_size

                shutil.copyfileobj(decryption_stream, decrypted_output_file, **kwargs)

            t2 = time.time()
            print("Time to decrypt: {}".format(t2 - t1))

            result_encryption_context = decryption_stream.get_encryption_context()

        decrypted_output_file.seek(0)
        input_stream.seek(0)

        # assert that input stream and decrypted output stream match
        if hasattr(input_stream, "name"):
            assert filecmp.cmp(input_stream.name, decrypted_output_file.name)
        else:
            input_content = convert_to_bytes(input_stream.read())
            output_content = decrypted_output_file.read()
            assert input_content == output_content

        # even if input encryption context is None, we always return a dict
        assert result_encryption_context is not None

        if encryption_context:
            for key, value in six.iteritems(encryption_context):
                assert result_encryption_context[key] == value

    finally:
        delete_and_close_files_if_exist(encrypted_output_file, decrypted_output_file)


def delete_and_close_files_if_exist(*files):
    for f in files:
        if f:
            f.close()
            os.remove(f.name)


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)
