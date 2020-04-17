# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

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
    if test_config_container.test_mode == 'mock':
        yield
    else:
        # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
        # instead of 'query' matcher (which ignores sessionId in the url)
        # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
        custom_vcr = test_config_container.create_vcr()
        custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

        cassette_location = os.path.join('generated', 'key_management_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_cancel_key_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'CancelKeyDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'CancelKeyDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='CancelKeyDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "CancelKeyDeletion")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.cancel_key_deletion(
                key_id=request.pop(util.camelize('keyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'CancelKeyDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'key',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_cancel_key_version_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'CancelKeyVersionDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'CancelKeyVersionDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='CancelKeyVersionDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "CancelKeyVersionDeletion")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.cancel_key_version_deletion(
                key_id=request.pop(util.camelize('keyId')),
                key_version_id=request.pop(util.camelize('keyVersionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'CancelKeyVersionDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'keyVersion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_change_key_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'ChangeKeyCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'ChangeKeyCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='ChangeKeyCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "ChangeKeyCompartment")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_key_compartment(
                key_id=request.pop(util.camelize('keyId')),
                change_key_compartment_details=request.pop(util.camelize('ChangeKeyCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'ChangeKeyCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_key_compartment',
            False,
            False
        )


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
                create_key_details=request.pop(util.camelize('CreateKeyDetails')),
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
                key_id=request.pop(util.camelize('keyId')),
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
                key_id=request.pop(util.camelize('keyId')),
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
                key_id=request.pop(util.camelize('keyId')),
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
                key_id=request.pop(util.camelize('keyId')),
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
                key_id=request.pop(util.camelize('keyId')),
                key_version_id=request.pop(util.camelize('keyVersionId')),
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
def test_get_wrapping_key(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'GetWrappingKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'GetWrappingKey')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='GetWrappingKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "GetWrappingKey")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_wrapping_key(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'GetWrappingKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'wrappingKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_import_key(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'ImportKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'ImportKey')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='ImportKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "ImportKey")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.import_key(
                import_key_details=request.pop(util.camelize('ImportKeyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'ImportKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'key',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_import_key_version(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'ImportKeyVersion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'ImportKeyVersion')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='ImportKeyVersion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "ImportKeyVersion")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.import_key_version(
                key_id=request.pop(util.camelize('keyId')),
                import_key_version_details=request.pop(util.camelize('ImportKeyVersionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'ImportKeyVersion',
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='ListKeyVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "ListKeyVersions")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_key_versions(
                key_id=request.pop(util.camelize('keyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_key_versions(
                    key_id=request.pop(util.camelize('keyId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_key_versions(
                        key_id=request.pop(util.camelize('keyId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='ListKeys')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "ListKeys")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_keys(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_keys(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_keys(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
def test_schedule_key_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'ScheduleKeyDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'ScheduleKeyDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='ScheduleKeyDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "ScheduleKeyDeletion")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.schedule_key_deletion(
                key_id=request.pop(util.camelize('keyId')),
                schedule_key_deletion_details=request.pop(util.camelize('ScheduleKeyDeletionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'ScheduleKeyDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'key',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_schedule_key_version_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'ScheduleKeyVersionDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_management'), 'ScheduleKeyVersionDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='ScheduleKeyVersionDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("key_management", "KmsManagementClient", "ScheduleKeyVersionDeletion")
            client = oci.key_management.KmsManagementClient(config, service_endpoint=service_endpoint)
            response = client.schedule_key_version_deletion(
                key_id=request.pop(util.camelize('keyId')),
                key_version_id=request.pop(util.camelize('keyVersionId')),
                schedule_key_version_deletion_details=request.pop(util.camelize('ScheduleKeyVersionDeletionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'ScheduleKeyVersionDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'keyVersion',
            False,
            False
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
                key_id=request.pop(util.camelize('keyId')),
                update_key_details=request.pop(util.camelize('UpdateKeyDetails')),
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
