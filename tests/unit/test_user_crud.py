# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import oci
import tests.util


def test_user_crud(identity, config):
    compartment = config["tenancy"]
    user_name = tests.util.unique_name("python_temp_user")
    user_description = "Created by python SDK TestUserCrud test."

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

    all_users = list_all_users(identity, config)
    assert search_non_deleted_user_in_list(user_id=user_id, user_list=all_users, should_find=True)

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
    all_users = list_all_users(identity, config)
    assert search_non_deleted_user_in_list(user_id=user_id, user_list=all_users, should_find=False)


def search_non_deleted_user_in_list(user_id, user_list, should_find=True):
    for user in user_list:
        if user.id == user_id and user.lifecycle_state in ['CREATING', 'ACTIVE', 'INACTIVE']:  # Non-deleted state
            return should_find

    return not should_find


def list_all_users(identity, config):
    compartment = config["tenancy"]

    response = identity.list_users(compartment, limit=500)
    user_list = response.data
    page = response.next_page

    while page is not None:
        response = identity.list_users(compartment, limit=500, page=page)
        page = response.next_page
        user_list.extend(response.data)

    return user_list


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
