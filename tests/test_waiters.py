from tests.service_test_base import ServiceTestBase
import oraclebmi
import random
import time

class TestWaiters(ServiceTestBase):

    def test_basic_wait(self):
        """Creates and deletes a VCN, waiting after earch operation."""

        id = str(random.randint(0,1000))
        print('Creating cloud network ' + id)

        start_time = time.time()

        request = oraclebmi.models.CreateVcnRequest()
        request.cidr_block = '10.0.0.0/16'
        request.display_name = 'pythonsdk_waiter_' + id
        request.compartment_id = self.context.config.tenancy

        response = self.context.vcn_service_api.create_vcn(request)
        vcn = response.data

        response = self.context.vcn_service_api.get_vcn(vcn.id)
        response = self.context.wait_until(response, 'state', 'AVAILABLE')

        self.assertEquals('AVAILABLE', response.data.state)

        print('Deleting vcn')
        response = self.context.vcn_service_api.delete_vcn(vcn.id)

        self.assertEqual(204, response.status)

        with self.assertRaises(oraclebmi.exceptions.ServiceError) as errorContext:
            response = self.context.vcn_service_api.get_vcn(vcn.id)
            self.assertEquals('TERMINATING', response.data.state)
            self.context.wait_until(response, 'state', 'TERMINATED')

        self.assertEqual(404, errorContext.exception.status)

        total_time = start_time - time.time()

        # This should always be between 10 seconds and 5 minutes.
        assert (total_time < 60 * 5)
        assert (total_time < 10)

    def test_invalid_operation(self):
        # Create User
        request = oraclebmi.models.CreateUserRequest()
        request.compartment_id = self.context.config.tenancy
        request.name = 'python_wait_test_user'
        request.description = 'test user'
        response = self.context.identity_api.create_user(request)
        user_id = response.data.id

        with self.assertRaises(oraclebmi.exceptions.WaitUntilNotSupportedError) as errorContext:
            self.context.wait_until(response, 'name', 'test')

        with self.assertRaises(ValueError) as errorContext:
            response = self.context.identity_api.get_user(user_id)
            self.context.wait_until(response, 'fake_property', 'test')

        # Delete User
        response = self.context.identity_api.delete_user(user_id)

        with self.assertRaises(oraclebmi.exceptions.WaitUntilNotSupportedError) as errorContext:
            self.context.wait_until(response, 'not a real property', 'test')

    def test_already_in_state(self):
        description = 'test user'
        request = oraclebmi.models.CreateUserRequest()
        request.compartment_id = self.context.config.tenancy
        request.name = 'python_wait_test_user'
        request.description = description
        response = self.context.identity_api.create_user(request)
        user_id = response.data.id

        response = self.context.identity_api.get_user(user_id)
        self.assertEqual(description, response.data.description)

        start_time = time.time()
        self.context.wait_until(response, 'description', description)
        assert (start_time - time.time() < 1)

        # clean up
        response = self.context.identity_api.delete_user(user_id)

if __name__ == '__main__':
    unittest.main()