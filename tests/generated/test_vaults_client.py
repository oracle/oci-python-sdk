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

        cassette_location = os.path.join('generated', 'vault_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="team_oci_vault_us_grp@oracle.com" jiraProject="SECSVC" opsJiraProject="SI"
def test_cancel_secret_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('vault', 'CancelSecretDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('vault', util.camelize('vaults'), 'CancelSecretDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='vault', api_name='CancelSecretDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.vault.VaultsClient(config, service_endpoint=service_endpoint)
            response = client.cancel_secret_deletion(
                secret_id=request.pop(util.camelize('secretId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'vault',
            'CancelSecretDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_secret_deletion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_vault_us_grp@oracle.com" jiraProject="SECSVC" opsJiraProject="SI"
def test_cancel_secret_version_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('vault', 'CancelSecretVersionDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('vault', util.camelize('vaults'), 'CancelSecretVersionDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='vault', api_name='CancelSecretVersionDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.vault.VaultsClient(config, service_endpoint=service_endpoint)
            response = client.cancel_secret_version_deletion(
                secret_id=request.pop(util.camelize('secretId')),
                secret_version_number=request.pop(util.camelize('secretVersionNumber')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'vault',
            'CancelSecretVersionDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_secret_version_deletion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_vault_us_grp@oracle.com" jiraProject="SECSVC" opsJiraProject="SI"
def test_change_secret_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('vault', 'ChangeSecretCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('vault', util.camelize('vaults'), 'ChangeSecretCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='vault', api_name='ChangeSecretCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.vault.VaultsClient(config, service_endpoint=service_endpoint)
            response = client.change_secret_compartment(
                secret_id=request.pop(util.camelize('secretId')),
                change_secret_compartment_details=request.pop(util.camelize('ChangeSecretCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'vault',
            'ChangeSecretCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_secret_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_vault_us_grp@oracle.com" jiraProject="SECSVC" opsJiraProject="SI"
def test_create_secret(testing_service_client):
    if not testing_service_client.is_api_enabled('vault', 'CreateSecret'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('vault', util.camelize('vaults'), 'CreateSecret')
    )

    request_containers = testing_service_client.get_requests(service_name='vault', api_name='CreateSecret')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.vault.VaultsClient(config, service_endpoint=service_endpoint)
            response = client.create_secret(
                create_secret_details=request.pop(util.camelize('CreateSecretDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'vault',
            'CreateSecret',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'secret',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_vault_us_grp@oracle.com" jiraProject="SECSVC" opsJiraProject="SI"
def test_get_secret(testing_service_client):
    if not testing_service_client.is_api_enabled('vault', 'GetSecret'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('vault', util.camelize('vaults'), 'GetSecret')
    )

    request_containers = testing_service_client.get_requests(service_name='vault', api_name='GetSecret')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.vault.VaultsClient(config, service_endpoint=service_endpoint)
            response = client.get_secret(
                secret_id=request.pop(util.camelize('secretId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'vault',
            'GetSecret',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'secret',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_vault_us_grp@oracle.com" jiraProject="SECSVC" opsJiraProject="SI"
def test_get_secret_version(testing_service_client):
    if not testing_service_client.is_api_enabled('vault', 'GetSecretVersion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('vault', util.camelize('vaults'), 'GetSecretVersion')
    )

    request_containers = testing_service_client.get_requests(service_name='vault', api_name='GetSecretVersion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.vault.VaultsClient(config, service_endpoint=service_endpoint)
            response = client.get_secret_version(
                secret_id=request.pop(util.camelize('secretId')),
                secret_version_number=request.pop(util.camelize('secretVersionNumber')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'vault',
            'GetSecretVersion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'secretVersion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_vault_us_grp@oracle.com" jiraProject="SECSVC" opsJiraProject="SI"
def test_list_secret_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('vault', 'ListSecretVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('vault', util.camelize('vaults'), 'ListSecretVersions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='vault', api_name='ListSecretVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.vault.VaultsClient(config, service_endpoint=service_endpoint)
            response = client.list_secret_versions(
                secret_id=request.pop(util.camelize('secretId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_secret_versions(
                    secret_id=request.pop(util.camelize('secretId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_secret_versions(
                        secret_id=request.pop(util.camelize('secretId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'vault',
            'ListSecretVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'secretVersionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_vault_us_grp@oracle.com" jiraProject="SECSVC" opsJiraProject="SI"
def test_list_secrets(testing_service_client):
    if not testing_service_client.is_api_enabled('vault', 'ListSecrets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('vault', util.camelize('vaults'), 'ListSecrets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='vault', api_name='ListSecrets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.vault.VaultsClient(config, service_endpoint=service_endpoint)
            response = client.list_secrets(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_secrets(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_secrets(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'vault',
            'ListSecrets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'secretSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_vault_us_grp@oracle.com" jiraProject="SECSVC" opsJiraProject="SI"
def test_schedule_secret_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('vault', 'ScheduleSecretDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('vault', util.camelize('vaults'), 'ScheduleSecretDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='vault', api_name='ScheduleSecretDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.vault.VaultsClient(config, service_endpoint=service_endpoint)
            response = client.schedule_secret_deletion(
                secret_id=request.pop(util.camelize('secretId')),
                schedule_secret_deletion_details=request.pop(util.camelize('ScheduleSecretDeletionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'vault',
            'ScheduleSecretDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schedule_secret_deletion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_vault_us_grp@oracle.com" jiraProject="SECSVC" opsJiraProject="SI"
def test_schedule_secret_version_deletion(testing_service_client):
    if not testing_service_client.is_api_enabled('vault', 'ScheduleSecretVersionDeletion'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('vault', util.camelize('vaults'), 'ScheduleSecretVersionDeletion')
    )

    request_containers = testing_service_client.get_requests(service_name='vault', api_name='ScheduleSecretVersionDeletion')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.vault.VaultsClient(config, service_endpoint=service_endpoint)
            response = client.schedule_secret_version_deletion(
                secret_id=request.pop(util.camelize('secretId')),
                secret_version_number=request.pop(util.camelize('secretVersionNumber')),
                schedule_secret_version_deletion_details=request.pop(util.camelize('ScheduleSecretVersionDeletionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'vault',
            'ScheduleSecretVersionDeletion',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schedule_secret_version_deletion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_vault_us_grp@oracle.com" jiraProject="SECSVC" opsJiraProject="SI"
def test_update_secret(testing_service_client):
    if not testing_service_client.is_api_enabled('vault', 'UpdateSecret'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('vault', util.camelize('vaults'), 'UpdateSecret')
    )

    request_containers = testing_service_client.get_requests(service_name='vault', api_name='UpdateSecret')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.vault.VaultsClient(config, service_endpoint=service_endpoint)
            response = client.update_secret(
                secret_id=request.pop(util.camelize('secretId')),
                update_secret_details=request.pop(util.camelize('UpdateSecretDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'vault',
            'UpdateSecret',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'secret',
            False,
            False
        )
