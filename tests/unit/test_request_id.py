from tests.service_test_base import ServiceTestBase
import oraclebmc


class TestRequestId(ServiceTestBase):

    def test_core_automatic_request_id(self):
        api = oraclebmc.apis.VirtualNetworkApi(self.config)
        response = api.list_vcns(self.config.tenancy)
        self.assertEqual(200, response.status)
        assert response.request_id is not None
        assert len(response.request_id.split('/')) == 3
        assert len(response.request_id) == 98

'''
Commenting this out until Casper updates support for request ID.

    def test_object_storage_request_id(self):
        request_id = 'example_request_id_1234'
        response = self.context.object_storage_api.get_namespace(opc_client_request_id=request_id)

        self.assertEqual(200, response.status)
        assert (response.request_id != None)
        self.assertEquals (3, len(response.request_id.split('/')))
        assert (request_id in response.request_id)

    def test_object_storage_automatic_request_id(self):
        response = self.context.object_storage_api.get_namespace()

        self.assertEqual(200, response.status)
        assert (response.request_id != None)
        self.assertEquals(3, len(response.request_id.split('/')))
'''
