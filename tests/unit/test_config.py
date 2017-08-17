import oci

import pytest

from tests.util import get_resource_path

DEFAULT_REGION = "us-phoenix-1"
HARDCODED_TENANCY = "ocidv1:tenancy:oc1:phx:1460406592660:aaaaaaaab4faofrfkxecohhjuivjq262pu"
HARDCODED_USER = "ocid1.user.oc1..aaaaaaaakjkdrsqwljdpszrynrcosihxf2uspf7pzt7d4fmqomui2ngzysna"
HARDCODED_FINGERPRINT = "e1:8d:6a:cb:74:ed:25:51:a2:9f:38:a4:71:42:01:c8"
HARDCODED_KEYFILE = "keys/sdk_test_admin_user_key.pem"
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


def test_manual_config_doesnt_require_optional_fields():
    config = {
        'tenancy': HARDCODED_TENANCY,
        'user': HARDCODED_USER,
        'fingerprint': HARDCODED_FINGERPRINT,
        'key_file': HARDCODED_KEYFILE_NO_PASSPHRASE,
        'region': HARDCODED_REGION
    }

    # validate that creating client doesn't throw when optional fields are not present in config
    oci.identity.IdentityClient(config)


def test_config_get_value_or_default():
    assert oci.config.get_config_value_or_default({}, "additional_user_agent") == oci.config.DEFAULT_CONFIG["additional_user_agent"]
