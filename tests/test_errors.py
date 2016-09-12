from tests.service_test_base import ServiceTestBase
import oraclebmc

class TestErrors(ServiceTestBase):

    def test_invalid_compartment(self):
        api = oraclebmc.apis.IdentityApi(self.config)

        with self.assertRaises(oraclebmc.exceptions.ServiceError) as errorContext:
            api.list_users('invalid_compartment')

        self.assertEqual(403, errorContext.exception.status)
        assert (errorContext.exception.headers != None)
        assert (type(errorContext.exception.data) is oraclebmc.models.Error)

    def test_invalid_endpoint_host(self):
        api = oraclebmc.apis.VirtualNetworkApi(self.create_config(profile_name='INVALID_ENDPOINT_HOST'))

        with self.assertRaises(Exception) as errorContext:
            api.list_users('invalid_compartment')

if __name__ == '__main__':
    unittest.main()