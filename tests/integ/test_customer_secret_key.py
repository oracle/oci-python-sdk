# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import oci
import pytest

from . import util
from .. import test_config_container


ACTIVE_LIFECYCLE_STATES = set(['CREATING', 'ACTIVE'])
DELETE_LIFECYCLE_STATES = set(['DELETING', 'DELETED'])


@pytest.fixture
def customer_secret_key_user(identity, config):
    with test_config_container.create_vcr().use_cassette('test_customer_secret_key_secret_key_user_fixture.yml'):
        create_user_details = oci.identity.models.CreateUserDetails()
        create_user_details.name = util.random_name('python_sdk_secret_key_test_user')
        create_user_details.description = 'Python SDK customer secret key test user'
        create_user_details.compartment_id = config['tenancy']

        create_user_response = identity.create_user(create_user_details)
        yield create_user_response.data

        identity.delete_user(create_user_response.data.id)


def test_customer_secret_key_crud(identity, customer_secret_key_user):
    with test_config_container.create_vcr().use_cassette('test_customer_secret_key_crud.yml'):
        create_secret_key_one_details = oci.identity.models.CreateCustomerSecretKeyDetails()
        create_secret_key_one_details.display_name = 'Secret Key One'

        create_secret_key_one_response = create_customer_secret_key_with_assertions(identity, customer_secret_key_user, create_secret_key_one_details)

        customer_secret_keys = identity.list_customer_secret_keys(customer_secret_key_user.id).data
        assert len(customer_secret_keys) == 1
        assert_secret_key_from_list_secret_keys(customer_secret_keys[0], create_secret_key_one_response.data, ACTIVE_LIFECYCLE_STATES)

        update_secret_key_one_details = oci.identity.models.UpdateCustomerSecretKeyDetails()
        update_secret_key_one_details.display_name = 'Updated Secret Key One'

        update_secret_key_one_response = identity.update_customer_secret_key(customer_secret_key_user.id, create_secret_key_one_response.data.id, update_secret_key_one_details)
        assert update_secret_key_one_response.data.id == create_secret_key_one_response.data.id
        assert update_secret_key_one_response.data.user_id == customer_secret_key_user.id
        assert update_secret_key_one_response.data.display_name == update_secret_key_one_details.display_name
        assert update_secret_key_one_response.data.time_created == create_secret_key_one_response.data.time_created
        assert update_secret_key_one_response.data.time_expires is None
        assert update_secret_key_one_response.data.lifecycle_state in ACTIVE_LIFECYCLE_STATES

        create_secret_key_two_details = oci.identity.models.CreateCustomerSecretKeyDetails()
        create_secret_key_two_details.display_name = 'Secret Key Two'

        create_secret_key_two_response = create_customer_secret_key_with_assertions(identity, customer_secret_key_user, create_secret_key_two_details)

        customer_secret_keys = identity.list_customer_secret_keys(customer_secret_key_user.id).data
        assert len(customer_secret_keys) == 2
        if customer_secret_keys[0].id == create_secret_key_one_response.data.id:
            assert_secret_key_from_list_secret_keys(customer_secret_keys[0], update_secret_key_one_response.data, ACTIVE_LIFECYCLE_STATES)
            assert_secret_key_from_list_secret_keys(customer_secret_keys[1], create_secret_key_two_response.data, ACTIVE_LIFECYCLE_STATES)
        else:
            assert_secret_key_from_list_secret_keys(customer_secret_keys[0], create_secret_key_two_response.data, ACTIVE_LIFECYCLE_STATES)
            assert_secret_key_from_list_secret_keys(customer_secret_keys[1], update_secret_key_one_response.data, ACTIVE_LIFECYCLE_STATES)

        # A user can only have two active secret keys
        create_secret_key_three_details = oci.identity.models.CreateCustomerSecretKeyDetails()
        create_secret_key_three_details.display_name = 'Secret Key Two'
        with pytest.raises(oci.exceptions.ServiceError):
            identity.create_customer_secret_key(create_secret_key_three_details, customer_secret_key_user.id)

        identity.delete_customer_secret_key(customer_secret_key_user.id, create_secret_key_one_response.data.id)
        identity.delete_customer_secret_key(customer_secret_key_user.id, create_secret_key_two_response.data.id)

        customer_secret_keys = identity.list_customer_secret_keys(customer_secret_key_user.id).data
        if len(customer_secret_keys) != 0:
            for csk in customer_secret_keys:
                assert csk.lifecycle_state in DELETE_LIFECYCLE_STATES


def create_customer_secret_key_with_assertions(identity, customer_secret_key_user, create_secret_key_details):
    create_secret_key_response = identity.create_customer_secret_key(create_secret_key_details, customer_secret_key_user.id)
    assert create_secret_key_response.data.key
    assert create_secret_key_response.data.id
    assert customer_secret_key_user.id == create_secret_key_response.data.user_id
    assert create_secret_key_details.display_name == create_secret_key_response.data.display_name
    assert create_secret_key_response.data.time_created
    assert create_secret_key_response.data.time_expires is None
    assert create_secret_key_response.data.lifecycle_state in ACTIVE_LIFECYCLE_STATES

    return create_secret_key_response


def assert_secret_key_from_list_secret_keys(list_secret_key_entry, customer_secret_key, valid_lifecycle_states):
    assert list_secret_key_entry.id == customer_secret_key.id
    assert list_secret_key_entry.user_id == customer_secret_key.user_id
    assert list_secret_key_entry.display_name == customer_secret_key.display_name
    assert list_secret_key_entry.time_created == customer_secret_key.time_created
    assert list_secret_key_entry.time_expires is None
    assert list_secret_key_entry.lifecycle_state in valid_lifecycle_states
