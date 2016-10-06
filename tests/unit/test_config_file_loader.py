import oraclebmc

import pytest

from tests.util import get_resource_path

HARDCODED_IDENTITY_ENDPOINT = 'https://identity.us-phoenix-1.oraclecloud.com/20160918'
HARDCODED_COMPUTE_ENDPOINT = 'https://iaas.us-phoenix-1.oraclecloud.com/20160918'
HARDCODED_USER = 'USER_OCID'
HARDCODED_FINGERPRINT = 'FINGERPRINT'
HARDCODED_TENANCY = 'TENANCY_OCID'


def test_load_default_profile():
    config = oraclebmc.config_file_loader.load_config(
        file_location=get_resource_path('config'))

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
        file_location=get_resource_path('config'), profile_name='DEBUG')

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
        file_location=get_resource_path('config'), profile_name='INVALID_PARAMETER')

    # check some default properties
    assert config.endpoint_identity_api == HARDCODED_IDENTITY_ENDPOINT
    assert config.endpoint_compute_api == HARDCODED_COMPUTE_ENDPOINT

    # check properties set in file
    assert config.user == HARDCODED_USER
    assert config.fingerprint == HARDCODED_FINGERPRINT
    assert '/.ssh/id_rsa.pem' in config.key_file and '~' not in config.key_file
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
