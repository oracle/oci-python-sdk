# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import tests.util
import oci
import time
import pytest


def test_basic_wait(virtual_network, config):
    """Creates and deletes a VCN, waiting after each operation."""

    name = "pythonsdk_waiter_" + tests.util.random_number_string()
    print('Creating cloud network ' + name)

    start_time = time.time()

    request = oci.core.models.CreateVcnDetails()
    request.cidr_block = '10.0.0.0/16'
    request.display_name = name
    request.compartment_id = config["tenancy"]

    response = virtual_network.create_vcn(request)
    vcn = response.data

    response = virtual_network.get_vcn(vcn.id)
    response = oci.wait_until(virtual_network, response, 'lifecycle_state', 'AVAILABLE')

    assert 'AVAILABLE' == response.data.lifecycle_state

    print('Deleting vcn')
    response = virtual_network.delete_vcn(vcn.id)

    assert response.status == 204

    get_response = None
    with pytest.raises(oci.exceptions.ServiceError) as excinfo:
        get_response = virtual_network.get_vcn(vcn.id)
        assert 'TERMINATING' == get_response.data.lifecycle_state
        oci.wait_until(
            virtual_network,
            get_response,
            'lifecycle_state',
            'TERMINATED',
            max_wait_seconds=180
        )

    assert excinfo.value.status == 404

    if get_response is not None:
        result = oci.wait_until(virtual_network, get_response, 'lifecycle_state', 'TERMINATED', max_wait_seconds=180, succeed_on_not_found=True)
        assert result == oci.waiter.WAIT_RESOURCE_NOT_FOUND

    total_time = time.time() - start_time

    # This should always be under 5 minutes.
    assert total_time < 60 * 5


def test_wait_multiple_states(virtual_network, config):
    """Creates and deletes a VCN, waiting with multiple states after each operation."""

    name = "pythonsdk_waiter_" + tests.util.random_number_string()
    print('Creating cloud network ' + name)

    start_time = time.time()

    request = oci.core.models.CreateVcnDetails()
    request.cidr_block = '10.0.0.0/16'
    request.display_name = name
    request.compartment_id = config["tenancy"]

    response = virtual_network.create_vcn(request)
    vcn = response.data

    response = virtual_network.get_vcn(vcn.id)
    response = oci.wait_until(virtual_network, response, 'lifecycle_state', ('AVAILABLE', 'TERMINATED', 'TERMINATING'))

    assert 'AVAILABLE' == response.data.lifecycle_state

    print('Deleting vcn')
    response = virtual_network.delete_vcn(vcn.id)

    assert response.status == 204

    get_response = None
    with pytest.raises(oci.exceptions.ServiceError) as excinfo:
        get_response = virtual_network.get_vcn(vcn.id)
        assert 'TERMINATING' == get_response.data.lifecycle_state
        oci.wait_until(
            virtual_network,
            get_response,
            'lifecycle_state',
            ('AVAILABLE', 'TERMINATED'),
            max_wait_seconds=180
        )

    assert excinfo.value.status == 404

    if get_response is not None:
        result = oci.wait_until(virtual_network, get_response, 'lifecycle_state', 'TERMINATED', max_wait_seconds=180,
                                succeed_on_not_found=True)
        assert result == oci.waiter.WAIT_RESOURCE_NOT_FOUND

    total_time = time.time() - start_time

    # This should always be between 1 second and 5 minutes.
    assert total_time < 60 * 5


def test_invalid_operation(identity, config):
    # Create User
    request = oci.identity.models.CreateUserDetails()
    request.compartment_id = config["tenancy"]
    request.name = tests.util.unique_name('python_wait_test_user', ignore_vcr=True)
    request.description = 'test user'
    response = identity.create_user(request)
    user_id = response.data.id

    with pytest.raises(oci.exceptions.WaitUntilNotSupported):
        oci.wait_until(identity, response, 'name', 'test')

    with pytest.raises(ValueError):
        response = identity.get_user(user_id)
        oci.wait_until(identity, response, 'fake_property', 'test')

    # Delete User
    response = identity.delete_user(user_id)

    with pytest.raises(oci.exceptions.WaitUntilNotSupported):
        oci.wait_until(identity, response, 'not a real property', 'test')


def test_already_in_state(identity, config):
    description = 'test user'
    request = oci.identity.models.CreateUserDetails()
    request.compartment_id = config["tenancy"]
    request.name = tests.util.unique_name('python_wait_test_user', ignore_vcr=True)
    request.description = description
    response = identity.create_user(request)
    user_id = response.data.id

    response = identity.get_user(user_id)
    assert description == response.data.description

    start_time = time.time()
    oci.wait_until(identity, response, 'description', description)
    assert start_time - time.time() < 1

    # clean up
    identity.delete_user(user_id)


def test_wait_time_exceeded(identity, config):
    description = 'test user'
    request = oci.identity.models.CreateUserDetails()
    request.compartment_id = config["tenancy"]
    request.name = tests.util.unique_name('python_wait_test_user', ignore_vcr=True)
    request.description = description
    response = identity.create_user(request)
    user_id = response.data.id

    response = identity.get_user(user_id)
    assert description == response.data.description

    start_time = time.time()
    with pytest.raises(oci.exceptions.MaximumWaitTimeExceeded):
        # Wait on a property that will not change until we time out.
        oci.wait_until(identity, response, 'name', 'test', max_wait_seconds=2)

    total_time = time.time() - start_time
    assert 1 < total_time < 4

    # clean up
    identity.delete_user(user_id)


def test_property_and_eval_function_provided(virtual_network):
    with pytest.raises(ValueError) as ve:
        oci.wait_until(virtual_network, oci.Response(200, {}, None, oci.Request('GET', 'https://blah.example.org')), 'unit-test-prop', 'val', evaluate_response=lambda x: isinstance(x, object))

    assert str(ve.value) == 'If an evaluate_response function is provided, then the property argument cannot also be provided'


def test_eval_function_lambda(identity, config):
    user_id = None
    try:
        description = 'test user'
        request = oci.identity.models.CreateUserDetails()
        request.compartment_id = config["tenancy"]
        request.name = tests.util.unique_name('python_wait_test_user', ignore_vcr=True)
        request.description = description
        response = identity.create_user(request)
        user_id = response.data.id

        response = identity.get_user(user_id)
        assert description == response.data.description

        response = oci.wait_until(identity, response, evaluate_response=lambda x: x.data.description == description and x.data.name == request.name and x.data.lifecycle_state == 'ACTIVE')
        assert response.data.id == user_id
        assert response.data.description == description
        assert response.data.name == request.name
        assert response.data.lifecycle_state == 'ACTIVE'
    finally:
        if user_id:
            identity.delete_user(user_id)


def test_eval_function_func_ref(identity, config):
    user_id = None
    try:
        description = 'test user'
        request = oci.identity.models.CreateUserDetails()
        request.compartment_id = config["tenancy"]
        request.name = tests.util.unique_name('python_wait_test_user', ignore_vcr=True)
        request.description = description
        response = identity.create_user(request)
        user_id = response.data.id

        response = identity.get_user(user_id)
        assert description == response.data.description

        def test_user_response(user_response):
            print('Invoked function reference in test_user_response')
            user = user_response.data
            return user.description == description and user.name == request.name and user.lifecycle_state == 'ACTIVE'

        response = oci.wait_until(identity, response, evaluate_response=test_user_response)
        assert response.data.id == user_id
        assert response.data.description == description
        assert response.data.name == request.name
        assert response.data.lifecycle_state == 'ACTIVE'

        times_called = {'counter': 0}

        def test_user_response_for_timeout(user_response):
            print('Invoked function reference in test_user_response_for_timeout')
            user = user_response.data
            times_called['counter'] += 1
            return user.description == description and user.name == request.name and user.lifecycle_state == 'superman'

        with pytest.raises(oci.exceptions.MaximumWaitTimeExceeded):
            response = oci.wait_until(identity, response, evaluate_response=test_user_response_for_timeout, max_wait_seconds=45, max_interval_seconds=10)

        assert times_called['counter'] >= 2
    finally:
        if user_id:
            identity.delete_user(user_id)


def test_callback_func(virtual_network, config):
    name = "pythonsdk_waiter_" + tests.util.random_number_string()

    counters = {'create': 0, 'delete': 0}

    def create_vcn_callback(times_called, response):
        counters['create'] = times_called

    def delete_vcn_callback(times_called, response):
        counters['delete'] = times_called

    request = oci.core.models.CreateVcnDetails()
    request.cidr_block = '10.0.0.0/16'
    request.display_name = name
    request.compartment_id = config["tenancy"]

    response = virtual_network.create_vcn(request)
    vcn = response.data
    get_vcn_response = virtual_network.get_vcn(vcn.id)
    get_vcn_response.data.lifecycle_state = 'DUMMY'  # This will force at least one service call
    response = oci.wait_until(virtual_network, get_vcn_response, 'lifecycle_state', 'AVAILABLE', wait_callback=create_vcn_callback)
    assert 'AVAILABLE' == response.data.lifecycle_state
    assert counters['create'] > 0

    print('Deleting vcn')
    response = virtual_network.delete_vcn(vcn.id)
    result = oci.wait_until(virtual_network, get_vcn_response, 'lifecycle_state', 'TERMINATED', max_wait_seconds=180, succeed_on_not_found=True, wait_callback=delete_vcn_callback)
    assert result == oci.waiter.WAIT_RESOURCE_NOT_FOUND
    assert counters['delete'] >= 0
