from tests.service_test_base import ServiceTestBase
import oraclebmc

class TestBasicAPICalls(ServiceTestBase):

    def test_identity_list_users(self):
        api = oraclebmc.apis.IdentityApi(self.config)
        response = api.list_users(self.config.tenancy)

        assert(response != None)
        assert(len(response.data) > 0)
        assert(type(response.data[0]) is oraclebmc.models.User)
        self.assertEqual(200, response.status)
        assert(response.request_id != None)

    def test_vcn_list_vcns(self):
        api = oraclebmc.apis.VirtualNetworkApi(self.config)
        response = api.list_vcns(self.config.tenancy)

        assert (response != None)
        self.assertEqual(200, response.status)
        assert (response.request_id != None)

    def test_vcn_list_instances(self):
        api = oraclebmc.apis.ComputeApi(self.config)
        response = api.list_instances(self.config.tenancy)

        assert (response != None)
        self.assertEqual(200, response.status)
        assert (response.request_id != None)

    def test_limit(self):
        api = oraclebmc.apis.IdentityApi(self.config)
        response = api.list_users(self.config.tenancy, limit=1)

        assert (response != None)
        assert (len(response.data) == 1)
        assert (type(response.data[0]) is oraclebmc.models.User)
        self.assertEqual(200, response.status)
        assert (response.request_id != None)

if __name__ == '__main__':
    unittest.main()