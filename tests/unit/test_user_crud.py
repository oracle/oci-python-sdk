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

        assert type(response.data) is oraclebmc.models.User
        assert user_name == response.data.name
        assert user_description == response.data.description
        assert compartment == response.data.compartment_id
        user_id = response.data.id

        assert initial_user_count + 1 == len(api.list_users(compartment).data)

        # Get User
        response = api.get_user(user_id)
        assert type(response.data) is oraclebmc.models.User
        assert user_name == response.data.name
        assert user_description == response.data.description
        assert compartment == response.data.compartment_id

        # Update User
        new_description = "updated user description"
        request = oraclebmc.models.UpdateUserDetails()
        request.description = new_description
        response = api.update_user(user_id, request)

        assert type(response.data) is oraclebmc.models.User
        assert user_name == response.data.name
        assert new_description == response.data.description
        assert compartment == response.data.compartment_id

        # Delete User
        api.delete_user(user_id)
        assert initial_user_count == len(api.list_users(self.config.tenancy).data)
