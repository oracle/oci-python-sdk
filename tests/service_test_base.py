import unittest
import oraclebmc
import tests.util

class ServiceTestBase(unittest.TestCase):
    def setUp(self):
        self.context = self.create_context()

    def create_context(self, profile_name=oraclebmc.config_file_loader.DEFAULT_PROFILE):
        return oraclebmc.Context(config_file_location=tests.util.get_resource_path('config'), profile_name=profile_name)

