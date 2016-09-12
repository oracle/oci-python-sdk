from tests.service_test_base import ServiceTestBase
import tests.util
import oraclebmc
import time

class TestWaiters(ServiceTestBase):

    def test_basic_wait(self):
        """Creates and deletes a VCN, waiting after each operation."""

        api = oraclebmc.apis.VirtualNetworkApi(self.config)

        id = tests.util.random_number_string()
        print('Creating cloud network ' + id)

        start_time = time.time()

        request = oraclebmc.models.CreateVcnDetails()
        request.cidr_block = '10.0.0.0/16'
        request.display_name = 'pythonsdk_waiter_' + id
        request.compartment_id = self.config.tenancy

        response = api.create_vcn(request)
        vcn = response.data

        response = api.get_vcn(vcn.id)
        response = oraclebmc.wait_until(api, response, 'lifecycle_state', 'AVAILABLE')

        self.assertEqual('AVAILABLE', response.data.lifecycle_state)

        print('Deleting vcn')
        response = api.delete_vcn(vcn.id)

        self.assertEqual(204, response.status)

        with self.assertRaises(oraclebmc.exceptions.ServiceError) as errorContext:
            response = api.get_vcn(vcn.id)
            self.assertEqual('TERMINATING', response.data.lifecycle_state)
            oraclebmc.wait_until(api, response, 'lifecycle_state', 'TERMINATED', max_wait_seconds=180)

        self.assertEqual(404, errorContext.exception.status)

        total_time =  time.time() - start_time

        # This should always be between 2 seconds and 5 minutes.
        assert (total_time < 60 * 5)
        assert (total_time > 2)

    def test_invalid_operation(self):
        # Create User
        api = oraclebmc.apis.IdentityApi(self.config)

        request = oraclebmc.models.CreateUserDetails()
        request.compartment_id = self.config.tenancy
        request.name = tests.util.unique_name('python_wait_test_user')
        request.description = 'test user'
        response = api.create_user(request)
        user_id = response.data.id

        with self.assertRaises(oraclebmc.exceptions.WaitUntilNotSupported) as errorContext:
            oraclebmc.wait_until(api, response, 'name', 'test')

        with self.assertRaises(ValueError) as errorContext:
            response = api.get_user(user_id)
            oraclebmc.wait_until(api, response, 'fake_property', 'test')

        # Delete User
        response = api.delete_user(user_id)

        with self.assertRaises(oraclebmc.exceptions.WaitUntilNotSupported) as errorContext:
            oraclebmc.wait_until(api, response, 'not a real property', 'test')

    def test_already_in_state(self):
        api = oraclebmc.apis.IdentityApi(self.config)

        description = 'test user'
        request = oraclebmc.models.CreateUserDetails()
        request.compartment_id = self.config.tenancy
        request.name = tests.util.unique_name('python_wait_test_user')
        request.description = description
        response = api.create_user(request)
        user_id = response.data.id

        response = api.get_user(user_id)
        self.assertEqual(description, response.data.description)

        start_time = time.time()
        oraclebmc.wait_until(api, response, 'description', description)
        assert (start_time - time.time() < 1)

        # clean up
        response = api.delete_user(user_id)

    def test_wait_time_exceeded(self):
        api = oraclebmc.apis.IdentityApi(self.config)

        description = 'test user'
        request = oraclebmc.models.CreateUserDetails()
        request.compartment_id = self.config.tenancy
        request.name = tests.util.unique_name('python_wait_test_user')
        request.description = description
        response = api.create_user(request)
        user_id = response.data.id

        response = api.get_user(user_id)
        self.assertEqual(description, response.data.description)

        start_time = time.time()
        with self.assertRaises(oraclebmc.exceptions.MaximumWaitTimeExceeded) as errorContext:
            # Wait on a property that will not change until we time out.
            oraclebmc.wait_until(api, response, 'name', 'test', max_wait_seconds=2)

        total_time = time.time() - start_time
        assert (total_time > 1)
        assert (total_time < 4)

        # clean up
        response = api.delete_user(user_id)

if __name__ == '__main__':
    unittest.main()