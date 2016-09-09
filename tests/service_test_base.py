import unittest
import oraclebmc
import tests.util

class ServiceTestBase(unittest.TestCase):
    def setUp(self):
        self.config = self.create_config()

    def create_config(self, profile_name=oraclebmc.config_file_loader.DEFAULT_PROFILE):
        return oraclebmc.config_file_loader.load_config(file_location=tests.util.get_resource_path('config'), profile_name=profile_name)

