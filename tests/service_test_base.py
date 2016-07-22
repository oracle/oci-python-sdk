import unittest
import oraclebmi

class ServiceTestBase(unittest.TestCase):
    def setUp(self):
        self.context = self.create_context()

    def create_context(self, profile_name=oraclebmi.ConfigFileLoader.DEFAULT_PROFILE):
        try:
            return oraclebmi.Context(config_file_location='resources/config', profile_name=profile_name)
        except:
            return oraclebmi.Context(config_file_location='tests/resources/config', profile_name=profile_name)

