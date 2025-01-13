# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import tests.util
import oci
import time
import pytest
from oci.request import Request
from oci.response import Response
from oci.exceptions import ServiceError


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

    # This should always be under 5 minutes.
    assert total_time < 60 * 5


def test_invalid_operation(object_storage, config):
    # Create Bucket
    namespace_name = object_storage.get_namespace().data
    request = oci.object_storage.models.CreateBucketDetails()
    request.compartment_id = config["tenancy"]
    bucket_name = tests.util.unique_name('python_wait_test_bucket', ignore_vcr=True)
    request.name = bucket_name
    response = object_storage.create_bucket(namespace_name, request)

    with pytest.raises(oci.exceptions.WaitUntilNotSupported):
        oci.wait_until(object_storage, response, 'name', 'test')

    with pytest.raises(ValueError):
        response = object_storage.get_bucket(namespace_name, bucket_name)
        oci.wait_until(object_storage, response, 'fake_property', 'test')

    # Delete Bucket
    response = object_storage.delete_bucket(namespace_name, bucket_name)

    with pytest.raises(oci.exceptions.WaitUntilNotSupported):
        oci.wait_until(object_storage, response, 'not a real property', 'test')


def test_already_in_state(object_storage, config):
    # Create Bucket
    namespace_name = object_storage.get_namespace().data
    request = oci.object_storage.models.CreateBucketDetails()
    request.compartment_id = config["tenancy"]
    bucket_name = tests.util.unique_name('python_wait_test_bucket', ignore_vcr=True)
    request.name = bucket_name
    response = object_storage.create_bucket(namespace_name, request)
    bucket_id = response.data.id

    response = object_storage.get_bucket(namespace_name, bucket_name)
    assert bucket_id == response.data.id

    start_time = time.time()
    oci.wait_until(object_storage, response, 'id', bucket_id)
    assert start_time - time.time() < 1

    # clean up
    object_storage.delete_bucket(namespace_name, bucket_name)


def test_wait_time_exceeded(object_storage, config):
    # Create Bucket
    namespace_name = object_storage.get_namespace().data
    request = oci.object_storage.models.CreateBucketDetails()
    request.compartment_id = config["tenancy"]
    bucket_name = tests.util.unique_name('python_wait_test_bucket', ignore_vcr=True)
    request.name = bucket_name
    response = object_storage.create_bucket(namespace_name, request)
    bucket_id = response.data.id

    response = object_storage.get_bucket(namespace_name, bucket_name)
    assert bucket_id == response.data.id

    with pytest.raises(oci.exceptions.MaximumWaitTimeExceeded):
        # Wait on a property that will not change until we time out.
        oci.wait_until(object_storage, response, 'name', 'test', max_wait_seconds=2)

    # clean up
    object_storage.delete_bucket(namespace_name, bucket_name)


def test_property_and_eval_function_provided(virtual_network):
    with pytest.raises(ValueError) as ve:
        oci.wait_until(virtual_network, oci.Response(200, {}, None, oci.Request('GET', 'https://blah.example.org')), 'unit-test-prop', 'val', evaluate_response=lambda x: isinstance(x, object))

    assert str(ve.value) == 'Invalid wait_until configuration - can not provide both evaluate_response function and property argument, only one should be specified'


def test_eval_function_lambda(object_storage, config):
    bucket_id = None
    namespace_name = ""
    bucket_name = ""
    try:
        namespace_name = object_storage.get_namespace().data
        request = oci.object_storage.models.CreateBucketDetails()
        request.compartment_id = config["tenancy"]
        bucket_name = tests.util.unique_name('python_wait_test_bucket', ignore_vcr=True)
        request.name = bucket_name
        response = object_storage.create_bucket(namespace_name, request)
        bucket_id = response.data.id

        response = object_storage.get_bucket(namespace_name, bucket_name)
        assert bucket_id == response.data.id

        response = oci.wait_until(object_storage, response, evaluate_response=lambda x: x.data.id == bucket_id and x.data.name == request.name and x.data.namespace == namespace_name)
        assert response.data.id == bucket_id
        assert response.data.compartment_id == config["tenancy"]
        assert response.data.name == request.name
        assert response.data.namespace == namespace_name
    finally:
        if bucket_id:
            object_storage.delete_bucket(namespace_name, bucket_name)


def test_eval_function_func_ref(object_storage, config):
    bucket_id = None
    namespace_name = ""
    bucket_name = ""
    try:
        namespace_name = object_storage.get_namespace().data
        request = oci.object_storage.models.CreateBucketDetails()
        request.compartment_id = config["tenancy"]
        bucket_name = tests.util.unique_name('python_wait_test_bucket', ignore_vcr=True)
        request.name = bucket_name
        response = object_storage.create_bucket(namespace_name, request)
        bucket_id = response.data.id

        response = object_storage.get_bucket(namespace_name, bucket_name)
        assert bucket_id == response.data.id

        def test_bucket_response(bucket_response):
            print('Invoked function reference in test_bucket_response')
            bucket = bucket_response.data
            return bucket.id == bucket_id and bucket.name == request.name and bucket.compartment_id == config["tenancy"]

        response = oci.wait_until(object_storage, response, evaluate_response=test_bucket_response)
        assert response.data.id == bucket_id
        assert response.data.namespace == namespace_name
        assert response.data.name == request.name
        assert response.data.compartment_id == config["tenancy"]

        times_called = {'counter': 0}

        def test_bucket_response_for_timeout(bucket_response):
            print('Invoked function reference in test_bucket_response_for_timeout')
            bucket = bucket_response.data
            times_called['counter'] += 1
            return bucket.id == bucket_id and bucket.name == request.name and bucket.compartment_id == 'superman'

        with pytest.raises(oci.exceptions.MaximumWaitTimeExceeded):
            response = oci.wait_until(object_storage, response, evaluate_response=test_bucket_response_for_timeout, max_wait_seconds=45, max_interval_seconds=10)

        assert times_called['counter'] >= 2
    finally:
        if bucket_id:
            object_storage.delete_bucket(namespace_name, bucket_name)


def test_callback_func(virtual_network, config):
    name = "pythonsdk_waiter_" + tests.util.random_number_string()

    counters = {'create': 0, 'delete': 0, 'wait': 0}

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

    def fetch_func(response=None, num=2):
        counters['wait'] = counters['wait'] + 1
        if counters['wait'] < num:
            resp = virtual_network.get_vcn(vcn.id)
            resp.data.lifecycle_state = 'DUMMY'
            return resp
        else:
            return virtual_network.get_vcn(vcn.id)

    response = oci.wait_until(virtual_network, get_vcn_response, 'lifecycle_state', 'AVAILABLE', wait_callback=create_vcn_callback, fetch_func=fetch_func)
    assert 'AVAILABLE' == response.data.lifecycle_state
    assert counters['create'] > 0  # make sure call-back function is called here

    print('Deleting vcn')
    response = virtual_network.delete_vcn(vcn.id)
    result = oci.wait_until(virtual_network, get_vcn_response, 'lifecycle_state', 'TERMINATED', max_wait_seconds=180, succeed_on_not_found=True, wait_callback=delete_vcn_callback)
    assert result == oci.waiter.WAIT_RESOURCE_NOT_FOUND
    assert counters['delete'] >= 0


def test_callback_cornercase(virtual_network, config):
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
    assert counters['create'] == 0  # This will make sure invoke wait_callbacK after checking resource property

    print('Deleting vcn')
    response = virtual_network.delete_vcn(vcn.id)
    result = oci.wait_until(virtual_network, get_vcn_response, 'lifecycle_state', 'TERMINATED', max_wait_seconds=180, succeed_on_not_found=True, wait_callback=delete_vcn_callback)
    assert result == oci.waiter.WAIT_RESOURCE_NOT_FOUND
    assert counters['delete'] >= 0


def test_fetch_func(virtual_network, config):
    name = "pythonsdk_waiter_" + tests.util.random_number_string()

    counters = {'wait': 0}

    request = oci.core.models.CreateVcnDetails()
    request.cidr_block = '10.0.0.0/16'
    request.display_name = name
    request.compartment_id = config["tenancy"]

    response = virtual_network.create_vcn(request)
    vcn = response.data
    get_vcn_response = virtual_network.get_vcn(vcn.id)
    get_vcn_response.data.lifecycle_state = 'DUMMY'  # This will force at least one service call

    def fetch_func(response=None):
        counters['wait'] = counters['wait'] + 1
        return virtual_network.get_vcn(vcn.id)

    response = oci.wait_until(virtual_network, get_vcn_response, 'lifecycle_state', 'AVAILABLE', fetch_func=fetch_func)
    assert 'AVAILABLE' == response.data.lifecycle_state
    assert counters['wait'] > 0

    print('Deleting vcn')
    response = virtual_network.delete_vcn(vcn.id)
    result = oci.wait_until(virtual_network, get_vcn_response, 'lifecycle_state', 'TERMINATED', max_wait_seconds=180, succeed_on_not_found=True)
    assert result == oci.waiter.WAIT_RESOURCE_NOT_FOUND


def test_401_retry_on_waiters():
    mock_request = Request("GET", "https://blahblah.com")
    mock_response_data = MockResponseData("BLAH")
    mock_response = Response("402", {}, mock_response_data, mock_request)
    mock_401_service_error = ServiceError(401, "blah", {}, "blah")
    mock_404_service_error = ServiceError(404, "blah", {}, "blah")

    # Test Scenario 1: The signer is an instance or resource principal signer, and we get back
    # a 401 service error upon a request
    with pytest.raises(ServiceError):
        mock_client_1 = MockClient(True, mock_401_service_error)
        oci.wait_until(mock_client_1, mock_response, "val", "blah")
    # In this scenario, we retry twice in addition to the initial request call.
    # Hence, total number of request calls should be 3 (initial call + 2 retry calls).
    assert mock_client_1.base_client.total_calls == 3
    assert mock_client_1.base_client.signer.refresh_count == 2

    # Test Scenario 2: The signer is not an instance or resource principal signer, and we get back
    # a 401 service error upon a request
    with pytest.raises(ServiceError):
        mock_client_2 = MockClient(False, mock_401_service_error)
        oci.wait_until(mock_client_2, mock_response, "val", "blah")
    # In this scenario, we do not retry in addition to the initial request call.
    # Hence, total number of request calls should be 1 (initial call only).
    assert mock_client_2.base_client.total_calls == 1
    assert mock_client_2.base_client.signer.refresh_count == 0

    # Test Scenario 3: The signer is an instance or resource principal signer, and we get back
    # a non-401 (404 in this case) service error upon a request
    with pytest.raises(ServiceError):
        mock_client_3 = MockClient(True, mock_404_service_error)
        oci.wait_until(mock_client_3, mock_response, "val", "blah")
    # In this scenario, we do not retry in addition to the initial request call.
    # Hence, total number of request calls should be 1 (initial call only).
    assert mock_client_3.base_client.total_calls == 1
    assert mock_client_3.base_client.signer.refresh_count == 0

    # Test Scenario 4: The signer is not an instance or resource principal signer, and we get back
    # a non-401 (404 in this case) service error upon a request
    with pytest.raises(ServiceError):
        mock_client_4 = MockClient(False, mock_404_service_error)
        oci.wait_until(mock_client_4, mock_response, "val", "blah")
    # In this scenario, we do not retry in addition to the initial request call.
    # Hence, total number of request calls should be 1 (initial call only).
    assert mock_client_4.base_client.total_calls == 1
    assert mock_client_4.base_client.signer.refresh_count == 0


class MockSigner:

    def __init__(self, is_instance_principal_or_resource_principal_signer):
        self.is_instance_principal_or_resource_principal_signer = is_instance_principal_or_resource_principal_signer
        self.refresh_count = 0

    def refresh_security_token(self):
        self.refresh_count += 1


class MockBaseClient:

    def __init__(self, service_error):
        self.total_calls = 0
        self.service_error = service_error
        self.signer = None

    def is_instance_principal_or_resource_principal_signer(self):
        return self.signer.is_instance_principal_or_resource_principal_signer

    def request(self, request):
        self.total_calls += 1
        raise self.service_error


class MockClient:

    def __init__(self, is_instance_principal_or_resource_principal_signer, service_error):
        self.base_client = MockBaseClient(service_error)
        self.base_client.signer = MockSigner(is_instance_principal_or_resource_principal_signer)


class MockResponseData:

    def __init__(self, val):
        self.val = val
