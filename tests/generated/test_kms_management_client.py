# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import pytest
from .. import test_config_container  # noqa: F401
from .. import util
import oci
import oci.exceptions as oci_exception
import os


def session_agnostic_query_matcher(r1, r2):
    r1_query = [x for x in r1.query if x[0] != 'sessionId']
    r2_query = [x for x in r2.query if x[0] != 'sessionId']
    return r1_query == r2_query


@pytest.fixture(autouse=True, scope='function')
def vcr_fixture(request):
    # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
    # instead of 'query' matcher (which ignores sessionId in the url)
    # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
    custom_vcr = test_config_container.create_vcr()
    custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

    cassette_location = os.path.join('generated', 'key_management_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_create_key(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'CreateKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'CreateKey')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='CreateKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "CreateKey")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_key(
                create_key_details=request.pop(util.camelize('create_key_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'CreateKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'key',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_create_key_version(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'CreateKeyVersion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'CreateKeyVersion')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='CreateKeyVersion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "CreateKeyVersion")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_key_version(
                key_id=request.pop(util.camelize('key_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'CreateKeyVersion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'keyVersion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_disable_key(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'DisableKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'DisableKey')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='DisableKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "DisableKey")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.disable_key(
                key_id=request.pop(util.camelize('key_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'DisableKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'key',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_enable_key(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'EnableKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'EnableKey')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='EnableKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "EnableKey")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.enable_key(
                key_id=request.pop(util.camelize('key_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'EnableKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'key',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_get_key(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'GetKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'GetKey')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='GetKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "GetKey")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_key(
                key_id=request.pop(util.camelize('key_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'GetKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'key',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_get_key_version(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'GetKeyVersion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'GetKeyVersion')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='GetKeyVersion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "GetKeyVersion")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_key_version(
                key_id=request.pop(util.camelize('key_id')),
                key_version_id=request.pop(util.camelize('key_version_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'GetKeyVersion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'keyVersion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_list_key_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'ListKeyVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'ListKeyVersions')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='ListKeyVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "ListKeyVersions")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_key_versions(
                key_id=request.pop(util.camelize('key_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_key_versions(
                    key_id=request.pop(util.camelize('key_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_key_versions(
                        key_id=request.pop(util.camelize('key_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'ListKeyVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'keyVersionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_list_keys(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'ListKeys'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'ListKeys')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='ListKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "ListKeys")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_keys(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_keys(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_keys(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'ListKeys',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'keySummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_update_key(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'UpdateKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'UpdateKey')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='UpdateKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "UpdateKey")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_key(
                key_id=request.pop(util.camelize('key_id')),
                update_key_details=request.pop(util.camelize('update_key_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'UpdateKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'key',
            False,
            False
        )
