import unittest
import oraclebmi

class ServiceTestBase(unittest.TestCase):
    def setUp(self):
        self.context = self.create_context()

    def create_context(self, profile_name=oraclebmi.config_file_loader.DEFAULT_PROFILE):
        # This is a workaround for the fact that these tests are often run from
        # two different working directories, depending on where the test is run.
        try:
            return oraclebmi.Context(config_file_location='tests/resources/config', profile_name=profile_name)
        except oraclebmi.exceptions.ConfigFileNotFoundError:
            return oraclebmi.Context(config_file_location='resources/config', profile_name=profile_name)

