from tests.service_test_base import ServiceTestBase
import oraclebmc

class TestUserCrud(ServiceTestBase):

    def test_user_CRUD(self):
        api = oraclebmc.apis.IdentityApi(self.config)
        
        compartment = self.config.tenancy
        user_name = "python_temp_user_1"
        user_description = "Created by python SDK TestUserCrud test."

        initial_user_count = len(api.list_users(compartment).data)

        # Create User
        request = oraclebmc.models.CreateUserDetails()
        request.compartment_id = compartment
        request.name = user_name
        request.description = user_description

        response = api.create_user(request)

        assert (type(response.data) is oraclebmc.models.User)
        self.assertEqual(user_name, response.data.name)
        self.assertEqual(user_description, response.data.description)
        self.assertEqual(compartment, response.data.compartment_id)
        user_id = response.data.id

        self.assertEqual(initial_user_count + 1, len(api.list_users(compartment).data))

        # Get User
        response = api.get_user(user_id)
        assert (type(response.data) is oraclebmc.models.User)
        self.assertEqual(user_name, response.data.name)
        self.assertEqual(user_description, response.data.description)
        self.assertEqual(compartment, response.data.compartment_id)

        # Update User
        user_description = "Updated description"
        newDescription = "updated user description"
        request = oraclebmc.models.UpdateUserDetails()
        request.description = newDescription
        response = api.update_user(user_id, request)

        assert (type(response.data) is oraclebmc.models.User)
        self.assertEqual(user_name, response.data.name)
        self.assertEqual(newDescription, response.data.description)
        self.assertEqual(compartment, response.data.compartment_id)

        # Delete User
        api.delete_user(user_id)
        self.assertEqual(initial_user_count, len(api.list_users(self.config.tenancy).data))

if __name__ == '__main__':
    unittest.main()