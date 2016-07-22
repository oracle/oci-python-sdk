import unittest

from oraclebmi import ConfigFileLoader

class TestConfigFileLoader(unittest.TestCase):

    def test_load_default_profile(self):
        config = ConfigFileLoader.load_config(config_file_location='tests/resources/config')

        # check some default properties
        self.assertEqual('https://identity.us-az-phoenix-1.OracleIaaS.com/v1', config.endpoint_identity_api)
        self.assertEqual('https://core.us-az-phoenix-1.OracleIaaS.com/v1', config.endpoint_compute_api)

        # check properties set in file
        self.assertEqual('ocidv1:user:oc1:phx:1460406592659:aaaaaaaawcbqrkycbolrirg2n3xjl5fyxe', config.user)
        self.assertEqual('20:3b:97:13:55:1c:5b:0d:d3:37:d8:50:4e:c5:3a:34', config.fingerprint)
        self.assertEqual('ocidv1:tenancy:oc1:phx:1460406592660:aaaaaaaab4faofrfkxecohhjuivjq262pu', config.tenancy)
        self.assertEqual(False, config.debugging)

    def test_child_profile(self):
        config = ConfigFileLoader.load_config(config_file_location='tests/resources/config', profile_name='DEBUG')

        # check some default properties
        self.assertEqual('https://identity.us-az-phoenix-1.OracleIaaS.com/v1', config.endpoint_identity_api)

        # check properties inherited from the default profile
        self.assertEqual('ocidv1:user:oc1:phx:1460406592659:aaaaaaaawcbqrkycbolrirg2n3xjl5fyxe', config.user)
        self.assertEqual('20:3b:97:13:55:1c:5b:0d:d3:37:d8:50:4e:c5:3a:34', config.fingerprint)
        self.assertEqual('ocidv1:tenancy:oc1:phx:1460406592660:aaaaaaaab4faofrfkxecohhjuivjq262pu', config.tenancy)

        # check properties overridden by the specified profile
        self.assertEqual(True, config.debugging)
        self.assertEqual('foo', config.endpoint_compute_api)

    def test_invalid_parameter(self):
        # The invalid parameter should be ignored.
        config = ConfigFileLoader.load_config(config_file_location='tests/resources/config', profile_name='INVALID_PARAMETER')

        # check some default properties
        self.assertEqual('https://identity.us-az-phoenix-1.OracleIaaS.com/v1', config.endpoint_identity_api)
        self.assertEqual('https://core.us-az-phoenix-1.OracleIaaS.com/v1', config.endpoint_compute_api)

        # check properties set in file
        self.assertEqual('ocidv1:user:oc1:phx:1460406592659:aaaaaaaawcbqrkycbolrirg2n3xjl5fyxe', config.user)
        self.assertEqual('20:3b:97:13:55:1c:5b:0d:d3:37:d8:50:4e:c5:3a:34', config.fingerprint)
        assert('/.ssh/id_rsa.pem' in config.key_file and '~' not in config.key_file)
        self.assertEqual('ocidv1:tenancy:oc1:phx:1460406592660:aaaaaaaab4faofrfkxecohhjuivjq262pu', config.tenancy)
        self.assertEqual(False, config.debugging)

        # Make sure that hte invalid attribute was not added.
        assert(not hasattr(config, 'foo'))

    def test_file_not_found(self):
        with self.assertRaises(Exception):
            ConfigFileLoader.load_config(config_file_location='blah')


if __name__ == '__main__':
    unittest.main()