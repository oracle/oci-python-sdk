import oraclebmc

import pytest

HARDCODED_IDENTITY_ENDPOINT = 'https://identity.us-phoenix-1.oraclecloud.com/20160918'
HARDCODED_COMPUTE_ENDPOINT = 'https://iaas.us-phoenix-1.oraclecloud.com/20160918'
HARDCODED_USER = 'ocid1.user.oc1..aaaaaaaaizi4xazrfv747ul6qwazrutt4dhg7ciazibypbjtkxdaszoicemq'
HARDCODED_FINGERPRINT = '35:69:71:f1:54:19:b8:12:71:76:0f:27:f4:26:04:fd'
HARDCODED_TENANCY = 'ocidv1:tenancy:oc1:phx:1460406592660:aaaaaaaab4faofrfkxecohhjuivjq262pu'


def test_load_default_profile():
    config = oraclebmc.config_file_loader.load_config(file_location='tests/resources/config')

    # check some default properties
    assert config.endpoint_identity_api == HARDCODED_IDENTITY_ENDPOINT
    assert config.endpoint_compute_api == HARDCODED_COMPUTE_ENDPOINT

    # check properties set in file
    assert config.user == HARDCODED_USER
    assert config.fingerprint == HARDCODED_FINGERPRINT
    assert config.tenancy == HARDCODED_TENANCY
    assert config.log_requests is False


def test_child_profile():
    config = oraclebmc.config_file_loader.load_config(
        file_location='tests/resources/config', profile_name='DEBUG')

    # check some default properties
    assert config.endpoint_identity_api == HARDCODED_IDENTITY_ENDPOINT
    assert config.endpoint_compute_api == HARDCODED_COMPUTE_ENDPOINT

    # check properties inherited from the default profile
    assert config.user == HARDCODED_USER
    assert config.fingerprint == HARDCODED_FINGERPRINT
    assert config.tenancy == HARDCODED_TENANCY

    # check properties overridden by the specified profile
    assert config.log_requests is True
    assert len(config.additional_user_agent) > 0


def test_invalid_parameter():
    # The invalid parameter should be ignored.
    config = oraclebmc.config_file_loader.load_config(
        file_location='tests/resources/config', profile_name='INVALID_PARAMETER')

    # check some default properties
    assert config.endpoint_identity_api == HARDCODED_IDENTITY_ENDPOINT
    assert config.endpoint_compute_api == HARDCODED_COMPUTE_ENDPOINT

    # check properties set in file
    assert config.user == HARDCODED_USER
    assert config.fingerprint == HARDCODED_FINGERPRINT
    assert '/.ssh/bmc_key' in config.key_file and '~' not in config.key_file
    assert config.tenancy == HARDCODED_TENANCY
    assert config.log_requests is False

    # Make sure that the invalid attribute was not added.
    assert not hasattr(config, 'foo')


def test_file_not_found():
    with pytest.raises(oraclebmc.exceptions.ConfigFileNotFound) as excinfo:
        oraclebmc.config_file_loader.load_config(file_location='does_not_exist')

    assert 'does_not_exist' in str(excinfo.value)


def test_profile_not_found():
    with pytest.raises(oraclebmc.exceptions.ProfileNotFound) as excinfo:
        oraclebmc.config_file_loader.load_config(profile_name='does_not_exist')

    assert 'does_not_exist' in str(excinfo.value)
