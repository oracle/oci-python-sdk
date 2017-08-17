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

    with pytest.raises(oci.exceptions.ServiceError) as excinfo:
        response = virtual_network.get_vcn(vcn.id)
        assert 'TERMINATING' == response.data.lifecycle_state
        oci.wait_until(
            virtual_network,
            response,
            'lifecycle_state',
            'TERMINATED',
            max_wait_seconds=180
        )

    assert excinfo.value.status == 404

    total_time = time.time() - start_time

    # This should always be between 1 second and 5 minutes.
    assert total_time < 60 * 5
    assert total_time > 1


def test_invalid_operation(identity, config):
    # Create User
    request = oci.identity.models.CreateUserDetails()
    request.compartment_id = config["tenancy"]
    request.name = tests.util.unique_name('python_wait_test_user')
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
    request.name = tests.util.unique_name('python_wait_test_user')
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
    request.name = tests.util.unique_name('python_wait_test_user')
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
