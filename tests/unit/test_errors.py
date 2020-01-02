# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

import oci
import pytest
from oci._vendor import requests
import tests.util


def test_invalid_compartment(identity):
    with pytest.raises(oci.exceptions.ServiceError) as excinfo:
        identity.list_users('invalid_compartment')
    tests.util.validate_service_error(excinfo.value, 404, "NotAuthorizedOrNotFound", "Authorization failed or requested resource not found")


def test_invalid_policy(identity, config):
    request = oci.identity.models.CreatePolicyDetails()
    request.compartment_id = config["tenancy"]
    request.name = 'invalid_policy'
    request.description = 'create should fail'
    request.statements = ['ALLOW group NotARealGroup inspect all-resources ON TENANCY']

    with pytest.raises(oci.exceptions.ServiceError) as excinfo:
        identity.create_policy(request)

    tests.util.validate_service_error(excinfo.value, 400, "InvalidParameter", "")


def test_invalid_endpoint_host(identity):
    identity.base_client.endpoint = "https://identity.us-phoenix-999999.oraclecloud.com/v1"

    with pytest.raises(Exception):
        identity.list_users('invalid_compartment')


def test_empty_path_param(identity):
    with pytest.raises(ValueError) as exc_info:
        identity.get_user('')

    assert 'Parameter userId cannot be None' in str(exc_info)


def test_none_path_param(identity):
    with pytest.raises(ValueError) as exc_info:
        identity.get_user(None)

    assert 'Parameter userId cannot be None' in str(exc_info)


def test_request_id_comes_from_request_when_nothing_in_response_header():
    dummy_response = requests.Response()
    dummy_response.headers = requests.structures.CaseInsensitiveDict()
    req = oci.request.Request('GET', 'http://httpbin.org/get', header_params={'opc-request-id': 'my-fake-id'})

    service_error = oci.exceptions.ServiceError(404, 'UnitTestCode', dummy_response.headers, 'Unit Test', original_request=req)
    assert service_error.request_id == 'my-fake-id'


def test_request_id_comes_from_response_when_in_response_header():
    dummy_response = requests.Response()
    dummy_response.headers = requests.structures.CaseInsensitiveDict()
    dummy_response.headers['opc-request-id'] = 'response-header-request-id'
    req = oci.request.Request('GET', 'http://httpbin.org/get', header_params={'opc-request-id': 'my-fake-id'})

    service_error = oci.exceptions.ServiceError(412, 'UnitTestCode', dummy_response.headers, 'Unit Test', original_request=req)
    assert service_error.request_id == 'response-header-request-id'
