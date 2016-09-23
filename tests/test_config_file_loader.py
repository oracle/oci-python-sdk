import unittest
import oraclebmc

HARDCODED_IDENTITY_ENDPOINT = 'https://identity.us-phoenix-1.oraclecloud.com/20160918'
HARDCODED_COMPUTE_ENDPOINT = 'https://iaas.us-phoenix-1.oraclecloud.com/20160918'
HARDCODED_USER_OCID = 'ocidv1:user:oc1:phx:1460406592659:aaaaaaaawcbqrkycbolrirg2n3xjl5fyxe'
HARDCODED_FINGERPRINT = '20:3b:97:13:55:1c:5b:0d:d3:37:d8:50:4e:c5:3a:34'
HARDCODED_TENANCY = 'ocidv1:tenancy:oc1:phx:1460406592660:aaaaaaaab4faofrfkxecohhjuivjq262pu'


class TestConfigFileLoader(unittest.TestCase):
    def test_load_default_profile(self):
        config = oraclebmc.config_file_loader.load_config(file_location='tests/resources/config')

        # check some default properties
        assert config.endpoint_identity_api == HARDCODED_IDENTITY_ENDPOINT
        assert config.endpoint_compute_api == HARDCODED_COMPUTE_ENDPOINT

        # check properties set in file
        assert config.user == HARDCODED_USER_OCID
        assert config.fingerprint == HARDCODED_FINGERPRINT
        assert config.tenancy == HARDCODED_TENANCY
        assert config.log_requests is False

    def test_child_profile(self):
        config = oraclebmc.config_file_loader.load_config(
            file_location='tests/resources/config', profile_name='DEBUG')

        # check some default properties
        assert config.endpoint_identity_api == HARDCODED_IDENTITY_ENDPOINT
        assert config.endpoint_compute_api == HARDCODED_COMPUTE_ENDPOINT

        # check properties inherited from the default profile
        assert config.user == HARDCODED_USER_OCID
        assert config.fingerprint == HARDCODED_FINGERPRINT
        assert config.tenancy == HARDCODED_TENANCY

        # check properties overridden by the specified profile
        assert config.log_requests is True
        assert len(config.additional_user_agent) > 0

    def test_invalid_parameter(self):
        # The invalid parameter should be ignored.
        config = oraclebmc.config_file_loader.load_config(
            file_location='tests/resources/config', profile_name='INVALID_PARAMETER')

        # check some default properties
        assert config.endpoint_identity_api == HARDCODED_IDENTITY_ENDPOINT
        assert config.endpoint_compute_api == HARDCODED_COMPUTE_ENDPOINT

        # check properties set in file
        assert config.user == HARDCODED_USER_OCID
        assert config.fingerprint == HARDCODED_FINGERPRINT
        assert '/.ssh/id_rsa.pem' in config.key_file and '~' not in config.key_file
        assert config.tenancy == HARDCODED_TENANCY
        assert config.log_requests is False

        # Make sure that the invalid attribute was not added.
        assert not hasattr(config, 'foo')

    def test_file_not_found(self):
        with self.assertRaises(oraclebmc.exceptions.ConfigFileNotFound) as errorContext:
            oraclebmc.config_file_loader.load_config(file_location='does_not_exist')

        assert 'does_not_exist' in str(errorContext.exception)

    def test_profile_not_found(self):
        with self.assertRaises(oraclebmc.exceptions.ProfileNotFound) as errorContext:
            oraclebmc.config_file_loader.load_config(profile_name='does_not_exist')

        assert 'does_not_exist' in str(errorContext.exception)
