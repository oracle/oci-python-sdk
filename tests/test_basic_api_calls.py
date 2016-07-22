from service_test_base import ServiceTestBase
import oraclebmi

class TestBasicAPICalls(ServiceTestBase):

    def test_identity_list_users(self):
        response = self.context.identity_api.list_users(self.context.config.tenancy)

        assert(response != None)
        assert(len(response.data) > 0)
        assert(type(response.data[0]) is oraclebmi.models.User)
        self.assertEquals(200, response.status)
        assert(response.request_id != None)

    def test_vcn_list_vcns(self):
        response = self.context.vcn_service_api.list_vcns(self.context.config.tenancy)

        assert (response != None)
        assert (len(response.data) > 0)
        assert (type(response.data[0]) is oraclebmi.models.Vcn)
        self.assertEquals(200, response.status)
        assert (response.request_id != None)

    def test_vcn_list_instances(self):
        response = self.context.compute_api.list_instances(self.context.config.tenancy)

        assert (response != None)
        self.assertEquals(200, response.status)
        assert (response.request_id != None)

    def test_limit(self):
        response = self.context.identity_api.list_users(self.context.config.tenancy, limit=1)

        assert (response != None)
        assert (len(response.data) == 1)
        assert (type(response.data[0]) is oraclebmi.models.User)
        self.assertEquals(200, response.status)
        assert (response.request_id != None)

if __name__ == '__main__':
    unittest.main()