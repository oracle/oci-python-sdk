import oraclebmc


def test_user_crud(identity, config):
    compartment = config["tenancy"]
    user_name = "python_temp_user_1"
    user_description = "Created by python SDK TestUserCrud test."

    initial_user_count = len(identity.list_users(compartment).data)

    # Create User
    request = oraclebmc.identity.models.CreateUserDetails()
    request.compartment_id = compartment
    request.name = user_name
    request.description = user_description

    response = identity.create_user(request)

    assert type(response.data) is oraclebmc.identity.models.User
    assert user_name == response.data.name
    assert user_description == response.data.description
    assert compartment == response.data.compartment_id
    user_id = response.data.id

    assert initial_user_count + 1 == len(identity.list_users(compartment).data)

    # Get User
    response = identity.get_user(user_id)
    assert type(response.data) is oraclebmc.identity.models.User
    assert user_name == response.data.name
    assert user_description == response.data.description
    assert compartment == response.data.compartment_id

    # Update User
    new_description = "updated user description"
    request = oraclebmc.identity.models.UpdateUserDetails()
    request.description = new_description
    response = identity.update_user(user_id, request)

    assert type(response.data) is oraclebmc.identity.models.User
    assert user_name == response.data.name
    assert new_description == response.data.description
    assert compartment == response.data.compartment_id

    # Delete User
    identity.delete_user(user_id)
    assert initial_user_count == len(identity.list_users(compartment).data)
