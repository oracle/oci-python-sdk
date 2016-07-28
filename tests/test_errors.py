from tests.service_test_base import ServiceTestBase
import oraclebmi

class TestErrors(ServiceTestBase):

    def test_invalid_compartment(self):
        with self.assertRaises(oraclebmi.exceptions.ServiceError) as errorContext:
            self.context.identity_api.list_users('invalid_compartment')

        self.assertEqual(403, errorContext.exception.status)
        assert (errorContext.exception.headers != None)
        assert (type(errorContext.exception.data) is oraclebmi.models.Error)

    def test_invalid_endpoint_host(self):
        context = self.create_context(profile_name='INVALID_ENDPOINT_HOST')

        with self.assertRaises(Exception) as errorContext:
            context.identity_api.list_users('invalid_compartment')

if __name__ == '__main__':
    unittest.main()