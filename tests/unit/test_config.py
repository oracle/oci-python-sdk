# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os
import oci

import pytest

from tests.util import get_resource_path

DEFAULT_REGION = "us-phoenix-1"
HARDCODED_TENANCY = "ocid1.tenancy.oc1..aaaaaaaa5nfwo53cezleyy6t73v6rn6knhu3molvptnl3kcq34l5zb7ptiaq"
HARDCODED_USER = "ocid1.user.oc1..aaaaaaaaiez5uibmpj7ybgiexgudk2h2z4i7nz4rqyp5mpqko4ucqfcbjhqq"
HARDCODED_FINGERPRINT = "5b:c5:18:ba:4e:37:51:b6:29:cb:71:d1:fa:a3:5d:42"
HARDCODED_KEYFILE = "shared_keys/oci_sdk_admin_key.pem"
HARDCODED_KEYFILE_NO_PASSPHRASE = 'keys/no_permissions_unencrypted_key.pem'
HARDCODED_REGION = "us-phoenix-1"


def test_load_default_profile():
    config = oci.config.from_file(file_location=get_resource_path('config'))

    # check some default properties
    assert config["log_requests"] is False

    # check properties set in file
    assert config["tenancy"] == HARDCODED_TENANCY
    assert config["user"] == HARDCODED_USER
    assert config["fingerprint"] == HARDCODED_FINGERPRINT
    assert config["region"] == HARDCODED_REGION
    # key file is expanded by the signer, not config
    assert config["key_file"] == HARDCODED_KEYFILE


def test_child_profile():
    config = oci.config.from_file(
        file_location=get_resource_path('config'), profile_name='DEBUG')

    # check properties inherited from the default profile
    assert config["tenancy"] == HARDCODED_TENANCY
    assert config["user"] == HARDCODED_USER
    assert config["fingerprint"] == HARDCODED_FINGERPRINT
    assert config["region"] == HARDCODED_REGION

    # check properties overridden by the specified profile
    assert config["log_requests"]
    assert config["additional_user_agent"]


def test_extra_config_values():
    # Extra config is passed along; this may be customer-specific
    # config for some subclass of the clients.
    config = oci.config.from_file(
        file_location=get_resource_path('config'), profile_name='INVALID_PARAMETER')
    assert config["foo"] == "bar"


def test_file_not_found():
    with pytest.raises(oci.exceptions.ConfigFileNotFound) as excinfo:
        oci.config.from_file(file_location='does_not_exist')
    assert 'does_not_exist' in str(excinfo.value)


def test_profile_not_found():
    with pytest.raises(oci.exceptions.ProfileNotFound) as excinfo:
        oci.config.from_file(file_location=get_resource_path('config'), profile_name='does_not_exist')
    assert 'does_not_exist' in str(excinfo.value)


def test_new_region():
    config = oci.config.from_file(
        get_resource_path('config'),
        profile_name='NEW_REGION')

    # Creating the client (which builds an endpoint)
    client = oci.identity.IdentityClient(config)
    assert config["region"] in client.base_client.endpoint


def test_missing_required():
    config = {
        "user": "malformed-user",
        "tenancy": "malformed-tenancy",
        # missing "region"
        # valid fingerprint
        "fingerprint": "00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00",
        "key_file": "~/.oci/config"
    }
    with pytest.raises(oci.exceptions.InvalidConfig) as excinfo:
        oci.config.validate_config(config)

    assert excinfo.value.errors == {
        "user": "malformed",
        "tenancy": "malformed",
        "region": "missing"
    }


def test_key_file_not_required_if_key_content_present():
    config = {
        "user": HARDCODED_USER,
        "tenancy": HARDCODED_TENANCY,
        "region": HARDCODED_REGION,
        "fingerprint": HARDCODED_FINGERPRINT,
        "key_content": "KEYCONTENT"
    }

    oci.config.validate_config(config)


def test_config_from_file_does_not_allow_key_content():
    with pytest.raises(ValueError) as excinfo:
        oci.config.from_file(file_location=get_resource_path('config'), profile_name='KEY_CONTENT')

    assert "'key_content' cannot be specified in a config file" in str(excinfo)


def test_invalid_key_file_path():
    with pytest.raises(oci.exceptions.InvalidKeyFilePath) as excinfo:
        oci.config.from_file(file_location=get_resource_path('config'), profile_name='INVALID_KEY_FILE_PATH')

    assert "invalid_key_file_path" in str(excinfo.value)
    assert "line 65" in str(excinfo.value)


def test_manual_config_doesnt_require_optional_fields():
    config = {
        'tenancy': HARDCODED_TENANCY,
        'user': HARDCODED_USER,
        'fingerprint': HARDCODED_FINGERPRINT,
        'key_file': HARDCODED_KEYFILE_NO_PASSPHRASE,
        'region': HARDCODED_REGION
    }

    # validate that creating client doesn't throw error when optional fields are not present in config
    oci.identity.IdentityClient(config)


def test_config_get_value_or_default():
    assert oci.config.get_config_value_or_default({}, "additional_user_agent") == oci.config.DEFAULT_CONFIG["additional_user_agent"]


def test_region_from_env_var():
    # Config without region
    config = {
        'tenancy': HARDCODED_TENANCY,
        'user': HARDCODED_USER,
        'fingerprint': HARDCODED_FINGERPRINT,
        'key_file': HARDCODED_KEYFILE_NO_PASSPHRASE
    }

    # Without the env var, the SDK should raise an error
    with pytest.raises(oci.exceptions.InvalidConfig) as excinfo:
        # Client init calls oci.config.validate_config internally
        oci.identity.IdentityClient(config)

    assert excinfo.value.errors == {
        "region": "missing"
    }

    # Set env var
    os.environ[oci.config.REGION_ENV_VAR_NAME] = 'us-phoenix-1'
    # Client init should not fail now
    oci.identity.IdentityClient(config)

    # Cleanup
    del os.environ[oci.config.REGION_ENV_VAR_NAME]


def test_delegation_token_config():
    config = oci.config.from_file(file_location=get_resource_path('config'), profile_name="DELEGATION_TOKEN")
    # validate_config should not throw
    oci.config.validate_config(config)

    # Test invalid value for authentication_type
    config = oci.config.from_file(file_location=get_resource_path('config'), profile_name="INVALID_AUTHENTICATION_TYPE")
    with pytest.raises(oci.exceptions.InvalidConfig) as excinfo:
        oci.config.validate_config(config)
    assert excinfo.value.errors == "The authentication type invalid_authentication_type is not supported"

    # Test error for non-existing file
    config = oci.config.from_file(file_location=get_resource_path('config'), profile_name="INVALID_DELEGATION_TOKEN_FILE")
    with pytest.raises(oci.exceptions.InvalidConfig):
        oci.config.validate_config(config)
