import oci
import tests.util


def test_user_crud(identity, config):
    compartment = config["tenancy"]
    user_name = tests.util.unique_name("python_temp_user")
    user_description = "Created by python SDK TestUserCrud test."

    initial_user_count = count_all_users(identity, config)

    # Create User
    request = oci.identity.models.CreateUserDetails()
    request.compartment_id = compartment
    request.name = user_name
    request.description = user_description

    response = identity.create_user(request)

    assert type(response.data) is oci.identity.models.User
    assert user_name == response.data.name
    assert user_description == response.data.description
    assert compartment == response.data.compartment_id
    user_id = response.data.id

    assert initial_user_count + 1 == count_all_users(identity, config)

    # Get User
    response = identity.get_user(user_id)
    assert type(response.data) is oci.identity.models.User
    assert user_name == response.data.name
    assert user_description == response.data.description
    assert compartment == response.data.compartment_id

    # Update User
    new_description = "updated user description"
    request = oci.identity.models.UpdateUserDetails()
    request.description = new_description
    response = identity.update_user(user_id, request)

    assert type(response.data) is oci.identity.models.User
    assert user_name == response.data.name
    assert new_description == response.data.description
    assert compartment == response.data.compartment_id

    # Delete User
    identity.delete_user(user_id)
    assert initial_user_count == count_all_users(identity, config)


def count_all_users(identity, config):
    compartment = config["tenancy"]

    response = identity.list_users(compartment, limit=500)
    user_count = len(response.data)
    page = response.next_page

    while page is not None:
        response = identity.list_users(compartment, limit=500, page=page)
        page = response.next_page
        user_count = user_count + len(response.data)

    return user_count
