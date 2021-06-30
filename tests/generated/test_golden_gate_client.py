# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'golden_gate_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_change_database_registration_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'ChangeDatabaseRegistrationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'ChangeDatabaseRegistrationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='ChangeDatabaseRegistrationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.change_database_registration_compartment(
                database_registration_id=request.pop(util.camelize('databaseRegistrationId')),
                change_database_registration_compartment_details=request.pop(util.camelize('ChangeDatabaseRegistrationCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'ChangeDatabaseRegistrationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_database_registration_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_change_deployment_backup_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'ChangeDeploymentBackupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'ChangeDeploymentBackupCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='ChangeDeploymentBackupCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.change_deployment_backup_compartment(
                deployment_backup_id=request.pop(util.camelize('deploymentBackupId')),
                change_deployment_backup_compartment_details=request.pop(util.camelize('ChangeDeploymentBackupCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'ChangeDeploymentBackupCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_deployment_backup_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_change_deployment_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'ChangeDeploymentCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'ChangeDeploymentCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='ChangeDeploymentCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.change_deployment_compartment(
                deployment_id=request.pop(util.camelize('deploymentId')),
                change_deployment_compartment_details=request.pop(util.camelize('ChangeDeploymentCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'ChangeDeploymentCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_deployment_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_create_database_registration(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'CreateDatabaseRegistration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'CreateDatabaseRegistration')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='CreateDatabaseRegistration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.create_database_registration(
                create_database_registration_details=request.pop(util.camelize('CreateDatabaseRegistrationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'CreateDatabaseRegistration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseRegistration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_create_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'CreateDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'CreateDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='CreateDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.create_deployment(
                create_deployment_details=request.pop(util.camelize('CreateDeploymentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'CreateDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_create_deployment_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'CreateDeploymentBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'CreateDeploymentBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='CreateDeploymentBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.create_deployment_backup(
                create_deployment_backup_details=request.pop(util.camelize('CreateDeploymentBackupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'CreateDeploymentBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_deployment_backup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_delete_database_registration(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'DeleteDatabaseRegistration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'DeleteDatabaseRegistration')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='DeleteDatabaseRegistration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.delete_database_registration(
                database_registration_id=request.pop(util.camelize('databaseRegistrationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'DeleteDatabaseRegistration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_database_registration',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_delete_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'DeleteDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'DeleteDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='DeleteDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.delete_deployment(
                deployment_id=request.pop(util.camelize('deploymentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'DeleteDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_deployment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_delete_deployment_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'DeleteDeploymentBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'DeleteDeploymentBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='DeleteDeploymentBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.delete_deployment_backup(
                deployment_backup_id=request.pop(util.camelize('deploymentBackupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'DeleteDeploymentBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_deployment_backup',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_get_database_registration(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'GetDatabaseRegistration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'GetDatabaseRegistration')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='GetDatabaseRegistration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.get_database_registration(
                database_registration_id=request.pop(util.camelize('databaseRegistrationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'GetDatabaseRegistration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseRegistration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_get_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'GetDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'GetDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='GetDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.get_deployment(
                deployment_id=request.pop(util.camelize('deploymentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'GetDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_get_deployment_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'GetDeploymentBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'GetDeploymentBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='GetDeploymentBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.get_deployment_backup(
                deployment_backup_id=request.pop(util.camelize('deploymentBackupId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'GetDeploymentBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deploymentBackup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_list_database_registrations(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'ListDatabaseRegistrations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'ListDatabaseRegistrations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='ListDatabaseRegistrations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.list_database_registrations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_database_registrations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_database_registrations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'ListDatabaseRegistrations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseRegistrationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_list_deployment_backups(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'ListDeploymentBackups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'ListDeploymentBackups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='ListDeploymentBackups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.list_deployment_backups(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_deployment_backups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_deployment_backups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'ListDeploymentBackups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deploymentBackupCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_list_deployments(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'ListDeployments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'ListDeployments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='ListDeployments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.list_deployments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_deployments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_deployments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'ListDeployments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deploymentCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_restore_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'RestoreDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'RestoreDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='RestoreDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.restore_deployment(
                deployment_backup_id=request.pop(util.camelize('deploymentBackupId')),
                restore_deployment_details=request.pop(util.camelize('RestoreDeploymentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'RestoreDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'restore_deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_start_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'StartDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'StartDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='StartDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.start_deployment(
                deployment_id=request.pop(util.camelize('deploymentId')),
                start_deployment_details=request.pop(util.camelize('StartDeploymentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'StartDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_stop_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'StopDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'StopDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='StopDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.stop_deployment(
                deployment_id=request.pop(util.camelize('deploymentId')),
                stop_deployment_details=request.pop(util.camelize('StopDeploymentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'StopDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stop_deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_update_database_registration(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'UpdateDatabaseRegistration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'UpdateDatabaseRegistration')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='UpdateDatabaseRegistration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.update_database_registration(
                database_registration_id=request.pop(util.camelize('databaseRegistrationId')),
                update_database_registration_details=request.pop(util.camelize('UpdateDatabaseRegistrationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'UpdateDatabaseRegistration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_database_registration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_update_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'UpdateDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'UpdateDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='UpdateDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.update_deployment(
                deployment_id=request.pop(util.camelize('deploymentId')),
                update_deployment_details=request.pop(util.camelize('UpdateDeploymentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'UpdateDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_update_deployment_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'UpdateDeploymentBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'UpdateDeploymentBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='UpdateDeploymentBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.update_deployment_backup(
                deployment_backup_id=request.pop(util.camelize('deploymentBackupId')),
                update_deployment_backup_details=request.pop(util.camelize('UpdateDeploymentBackupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'UpdateDeploymentBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deploymentBackup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="ggs_team_ww_grp@oracle.com" jiraProject="GGS" opsJiraProject="GGS"
def test_upgrade_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('golden_gate', 'UpgradeDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('golden_gate', util.camelize('golden_gate'), 'UpgradeDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='golden_gate', api_name='UpgradeDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.golden_gate.GoldenGateClient(config, service_endpoint=service_endpoint)
            response = client.upgrade_deployment(
                deployment_id=request.pop(util.camelize('deploymentId')),
                upgrade_deployment_details=request.pop(util.camelize('UpgradeDeploymentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'golden_gate',
            'UpgradeDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'upgrade_deployment',
            False,
            False
        )