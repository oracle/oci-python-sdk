# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

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
def test_cancel_vault_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'CancelVaultDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_vault'), 'CancelVaultDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='CancelVaultDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.key_management.KmsVaultClient(config, service_endpoint=service_endpoint)
            response = client.cancel_vault_deletion(
                vault_id=request.pop(util.camelize('vaultId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'CancelVaultDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vault',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_change_vault_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'ChangeVaultCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_vault'), 'ChangeVaultCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='ChangeVaultCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.key_management.KmsVaultClient(config, service_endpoint=service_endpoint)
            response = client.change_vault_compartment(
                vault_id=request.pop(util.camelize('vaultId')),
                change_vault_compartment_details=request.pop(util.camelize('ChangeVaultCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'ChangeVaultCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_vault_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_create_vault(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'CreateVault'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_vault'), 'CreateVault')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='CreateVault')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.key_management.KmsVaultClient(config, service_endpoint=service_endpoint)
            response = client.create_vault(
                create_vault_details=request.pop(util.camelize('CreateVaultDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'CreateVault',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vault',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_get_vault(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'GetVault'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_vault'), 'GetVault')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='GetVault')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.key_management.KmsVaultClient(config, service_endpoint=service_endpoint)
            response = client.get_vault(
                vault_id=request.pop(util.camelize('vaultId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'GetVault',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vault',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_list_vaults(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'ListVaults'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_vault'), 'ListVaults')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='ListVaults')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.key_management.KmsVaultClient(config, service_endpoint=service_endpoint)
            response = client.list_vaults(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_vaults(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_vaults(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'ListVaults',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vaultSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_schedule_vault_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'ScheduleVaultDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_vault'), 'ScheduleVaultDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='ScheduleVaultDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.key_management.KmsVaultClient(config, service_endpoint=service_endpoint)
            response = client.schedule_vault_deletion(
                vault_id=request.pop(util.camelize('vaultId')),
                schedule_vault_deletion_details=request.pop(util.camelize('ScheduleVaultDeletionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'ScheduleVaultDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vault',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sparta_kms_us_grp@oracle.com" jiraProject="KMS" opsJiraProject="KMS"
def test_update_vault(testing_service_client):
    if not testing_service_client.is_api_enabled('key_management', 'UpdateVault'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('key_management', util.camelize('kms_vault'), 'UpdateVault')
    )

    request_containers = testing_service_client.get_requests(service_name='key_management', api_name='UpdateVault')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.key_management.KmsVaultClient(config, service_endpoint=service_endpoint)
            response = client.update_vault(
                vault_id=request.pop(util.camelize('vaultId')),
                update_vault_details=request.pop(util.camelize('UpdateVaultDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'key_management',
            'UpdateVault',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'vault',
            False,
            False
        )
