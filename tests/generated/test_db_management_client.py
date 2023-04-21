# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'database_management_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_add_data_files(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'AddDataFiles'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'AddDataFiles')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='AddDataFiles')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.add_data_files(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                tablespace_name=request.pop(util.camelize('tablespaceName')),
                add_data_files_details=request.pop(util.camelize('AddDataFilesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'AddDataFiles',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tablespaceAdminStatus',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_add_managed_database_to_managed_database_group(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'AddManagedDatabaseToManagedDatabaseGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'AddManagedDatabaseToManagedDatabaseGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='AddManagedDatabaseToManagedDatabaseGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.add_managed_database_to_managed_database_group(
                managed_database_group_id=request.pop(util.camelize('managedDatabaseGroupId')),
                add_managed_database_to_managed_database_group_details=request.pop(util.camelize('AddManagedDatabaseToManagedDatabaseGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'AddManagedDatabaseToManagedDatabaseGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_managed_database_to_managed_database_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_addm_tasks(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'AddmTasks'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'AddmTasks')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='AddmTasks')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.addm_tasks(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                time_start=request.pop(util.camelize('timeStart')),
                time_end=request.pop(util.camelize('timeEnd')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.addm_tasks(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    time_start=request.pop(util.camelize('timeStart')),
                    time_end=request.pop(util.camelize('timeEnd')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.addm_tasks(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        time_start=request.pop(util.camelize('timeStart')),
                        time_end=request.pop(util.camelize('timeEnd')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'AddmTasks',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addmTasksCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_change_database_parameters(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ChangeDatabaseParameters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ChangeDatabaseParameters')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ChangeDatabaseParameters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_database_parameters(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                change_database_parameters_details=request.pop(util.camelize('ChangeDatabaseParametersDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ChangeDatabaseParameters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'updateDatabaseParametersResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_change_db_management_private_endpoint_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ChangeDbManagementPrivateEndpointCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ChangeDbManagementPrivateEndpointCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ChangeDbManagementPrivateEndpointCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_db_management_private_endpoint_compartment(
                db_management_private_endpoint_id=request.pop(util.camelize('dbManagementPrivateEndpointId')),
                change_db_management_private_endpoint_compartment_details=request.pop(util.camelize('ChangeDbManagementPrivateEndpointCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ChangeDbManagementPrivateEndpointCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_db_management_private_endpoint_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_change_external_db_system_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ChangeExternalDbSystemCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ChangeExternalDbSystemCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ChangeExternalDbSystemCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_external_db_system_compartment(
                external_db_system_id=request.pop(util.camelize('externalDbSystemId')),
                change_external_db_system_compartment_details=request.pop(util.camelize('ChangeExternalDbSystemCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ChangeExternalDbSystemCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_external_db_system_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_change_external_exadata_infrastructure_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ChangeExternalExadataInfrastructureCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ChangeExternalExadataInfrastructureCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ChangeExternalExadataInfrastructureCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_external_exadata_infrastructure_compartment(
                external_exadata_infrastructure_id=request.pop(util.camelize('externalExadataInfrastructureId')),
                change_external_exadata_infrastructure_compartment_details=request.pop(util.camelize('ChangeExternalExadataInfrastructureCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ChangeExternalExadataInfrastructureCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_external_exadata_infrastructure_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_change_job_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ChangeJobCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ChangeJobCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ChangeJobCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_job_compartment(
                job_id=request.pop(util.camelize('jobId')),
                change_job_compartment_details=request.pop(util.camelize('ChangeJobCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ChangeJobCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_job_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_change_managed_database_group_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ChangeManagedDatabaseGroupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ChangeManagedDatabaseGroupCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ChangeManagedDatabaseGroupCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_managed_database_group_compartment(
                managed_database_group_id=request.pop(util.camelize('managedDatabaseGroupId')),
                change_managed_database_group_compartment_details=request.pop(util.camelize('ChangeManagedDatabaseGroupCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ChangeManagedDatabaseGroupCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_managed_database_group_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_check_external_db_system_connector_connection_status(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'CheckExternalDbSystemConnectorConnectionStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'CheckExternalDbSystemConnectorConnectionStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='CheckExternalDbSystemConnectorConnectionStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.check_external_db_system_connector_connection_status(
                external_db_system_connector_id=request.pop(util.camelize('externalDbSystemConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'CheckExternalDbSystemConnectorConnectionStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbSystemConnector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_check_external_exadata_storage_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'CheckExternalExadataStorageConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'CheckExternalExadataStorageConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='CheckExternalExadataStorageConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.check_external_exadata_storage_connector(
                external_exadata_storage_connector_id=request.pop(util.camelize('externalExadataStorageConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'CheckExternalExadataStorageConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalExadataStorageConnectorStatus',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_create_db_management_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'CreateDbManagementPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'CreateDbManagementPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='CreateDbManagementPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_db_management_private_endpoint(
                create_db_management_private_endpoint_details=request.pop(util.camelize('CreateDbManagementPrivateEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'CreateDbManagementPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbManagementPrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_create_external_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'CreateExternalDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'CreateExternalDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='CreateExternalDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_external_db_system(
                create_external_db_system_details=request.pop(util.camelize('CreateExternalDbSystemDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'CreateExternalDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbSystem',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_create_external_db_system_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'CreateExternalDbSystemConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'CreateExternalDbSystemConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='CreateExternalDbSystemConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_external_db_system_connector(
                create_external_db_system_connector_details=request.pop(util.camelize('CreateExternalDbSystemConnectorDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'CreateExternalDbSystemConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbSystemConnector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_create_external_db_system_discovery(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'CreateExternalDbSystemDiscovery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'CreateExternalDbSystemDiscovery')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='CreateExternalDbSystemDiscovery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_external_db_system_discovery(
                create_external_db_system_discovery_details=request.pop(util.camelize('CreateExternalDbSystemDiscoveryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'CreateExternalDbSystemDiscovery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbSystemDiscovery',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_create_external_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'CreateExternalExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'CreateExternalExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='CreateExternalExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_external_exadata_infrastructure(
                create_external_exadata_infrastructure_details=request.pop(util.camelize('CreateExternalExadataInfrastructureDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'CreateExternalExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalExadataInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_create_external_exadata_storage_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'CreateExternalExadataStorageConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'CreateExternalExadataStorageConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='CreateExternalExadataStorageConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_external_exadata_storage_connector(
                create_external_exadata_storage_connector_details=request.pop(util.camelize('CreateExternalExadataStorageConnectorDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'CreateExternalExadataStorageConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalExadataStorageConnector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_create_job(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'CreateJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'CreateJob')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='CreateJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_job(
                create_job_details=request.pop(util.camelize('CreateJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'CreateJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_create_managed_database_group(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'CreateManagedDatabaseGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'CreateManagedDatabaseGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='CreateManagedDatabaseGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_managed_database_group(
                create_managed_database_group_details=request.pop(util.camelize('CreateManagedDatabaseGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'CreateManagedDatabaseGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedDatabaseGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_create_tablespace(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'CreateTablespace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'CreateTablespace')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='CreateTablespace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_tablespace(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                create_tablespace_details=request.pop(util.camelize('CreateTablespaceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'CreateTablespace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tablespace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_delete_db_management_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DeleteDbManagementPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'DeleteDbManagementPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DeleteDbManagementPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_db_management_private_endpoint(
                db_management_private_endpoint_id=request.pop(util.camelize('dbManagementPrivateEndpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DeleteDbManagementPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_db_management_private_endpoint',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_delete_external_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DeleteExternalDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'DeleteExternalDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DeleteExternalDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_external_db_system(
                external_db_system_id=request.pop(util.camelize('externalDbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DeleteExternalDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_external_db_system',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_delete_external_db_system_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DeleteExternalDbSystemConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'DeleteExternalDbSystemConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DeleteExternalDbSystemConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_external_db_system_connector(
                external_db_system_connector_id=request.pop(util.camelize('externalDbSystemConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DeleteExternalDbSystemConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_external_db_system_connector',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_delete_external_db_system_discovery(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DeleteExternalDbSystemDiscovery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'DeleteExternalDbSystemDiscovery')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DeleteExternalDbSystemDiscovery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_external_db_system_discovery(
                external_db_system_discovery_id=request.pop(util.camelize('externalDbSystemDiscoveryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DeleteExternalDbSystemDiscovery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_external_db_system_discovery',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_delete_external_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DeleteExternalExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'DeleteExternalExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DeleteExternalExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_external_exadata_infrastructure(
                external_exadata_infrastructure_id=request.pop(util.camelize('externalExadataInfrastructureId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DeleteExternalExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_external_exadata_infrastructure',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_delete_external_exadata_storage_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DeleteExternalExadataStorageConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'DeleteExternalExadataStorageConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DeleteExternalExadataStorageConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_external_exadata_storage_connector(
                external_exadata_storage_connector_id=request.pop(util.camelize('externalExadataStorageConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DeleteExternalExadataStorageConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_external_exadata_storage_connector',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_delete_job(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DeleteJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'DeleteJob')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DeleteJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_job(
                job_id=request.pop(util.camelize('jobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DeleteJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_job',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_delete_managed_database_group(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DeleteManagedDatabaseGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'DeleteManagedDatabaseGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DeleteManagedDatabaseGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_managed_database_group(
                managed_database_group_id=request.pop(util.camelize('managedDatabaseGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DeleteManagedDatabaseGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_managed_database_group',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_delete_preferred_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DeletePreferredCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'DeletePreferredCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DeletePreferredCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_preferred_credential(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                credential_name=request.pop(util.camelize('credentialName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DeletePreferredCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_preferred_credential',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_disable_external_db_system_database_management(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DisableExternalDbSystemDatabaseManagement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'DisableExternalDbSystemDatabaseManagement')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DisableExternalDbSystemDatabaseManagement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.disable_external_db_system_database_management(
                external_db_system_id=request.pop(util.camelize('externalDbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DisableExternalDbSystemDatabaseManagement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'disable_external_db_system_database_management',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_disable_external_exadata_infrastructure_management(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DisableExternalExadataInfrastructureManagement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'DisableExternalExadataInfrastructureManagement')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DisableExternalExadataInfrastructureManagement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.disable_external_exadata_infrastructure_management(
                external_exadata_infrastructure_id=request.pop(util.camelize('externalExadataInfrastructureId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DisableExternalExadataInfrastructureManagement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'disable_external_exadata_infrastructure_management',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_discover_external_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DiscoverExternalExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'DiscoverExternalExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DiscoverExternalExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.discover_external_exadata_infrastructure(
                discover_external_exadata_infrastructure_details=request.pop(util.camelize('DiscoverExternalExadataInfrastructureDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DiscoverExternalExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalExadataInfrastructureDiscovery',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_drop_tablespace(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'DropTablespace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'DropTablespace')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='DropTablespace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.drop_tablespace(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                tablespace_name=request.pop(util.camelize('tablespaceName')),
                drop_tablespace_details=request.pop(util.camelize('DropTablespaceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'DropTablespace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tablespaceAdminStatus',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_enable_external_db_system_database_management(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'EnableExternalDbSystemDatabaseManagement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'EnableExternalDbSystemDatabaseManagement')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='EnableExternalDbSystemDatabaseManagement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.enable_external_db_system_database_management(
                external_db_system_id=request.pop(util.camelize('externalDbSystemId')),
                enable_external_db_system_database_management_details=request.pop(util.camelize('EnableExternalDbSystemDatabaseManagementDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'EnableExternalDbSystemDatabaseManagement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enable_external_db_system_database_management',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_enable_external_exadata_infrastructure_management(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'EnableExternalExadataInfrastructureManagement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'EnableExternalExadataInfrastructureManagement')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='EnableExternalExadataInfrastructureManagement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.enable_external_exadata_infrastructure_management(
                external_exadata_infrastructure_id=request.pop(util.camelize('externalExadataInfrastructureId')),
                enable_external_exadata_infrastructure_management_details=request.pop(util.camelize('EnableExternalExadataInfrastructureManagementDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'EnableExternalExadataInfrastructureManagement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enable_external_exadata_infrastructure_management',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_generate_awr_snapshot(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GenerateAwrSnapshot'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GenerateAwrSnapshot')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GenerateAwrSnapshot')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.generate_awr_snapshot(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GenerateAwrSnapshot',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'snapshotDetails',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_awr_db_report(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetAwrDbReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetAwrDbReport')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetAwrDbReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_awr_db_report(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                awr_db_id=request.pop(util.camelize('awrDbId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetAwrDbReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDbReport',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_awr_db_sql_report(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetAwrDbSqlReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetAwrDbSqlReport')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetAwrDbSqlReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_awr_db_sql_report(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                awr_db_id=request.pop(util.camelize('awrDbId')),
                sql_id=request.pop(util.camelize('sqlId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetAwrDbSqlReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDbSqlReport',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_cluster_cache_metric(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetClusterCacheMetric'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetClusterCacheMetric')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetClusterCacheMetric')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_cluster_cache_metric(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                start_time=request.pop(util.camelize('startTime')),
                end_time=request.pop(util.camelize('endTime')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetClusterCacheMetric',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'clusterCacheMetric',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_database_fleet_health_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetDatabaseFleetHealthMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetDatabaseFleetHealthMetrics')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetDatabaseFleetHealthMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_database_fleet_health_metrics(
                compare_baseline_time=request.pop(util.camelize('compareBaselineTime')),
                compare_target_time=request.pop(util.camelize('compareTargetTime')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetDatabaseFleetHealthMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseFleetHealthMetrics',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_database_home_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetDatabaseHomeMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetDatabaseHomeMetrics')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetDatabaseHomeMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_database_home_metrics(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                start_time=request.pop(util.camelize('startTime')),
                end_time=request.pop(util.camelize('endTime')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetDatabaseHomeMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseHomeMetrics',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_db_management_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetDbManagementPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetDbManagementPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetDbManagementPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_db_management_private_endpoint(
                db_management_private_endpoint_id=request.pop(util.camelize('dbManagementPrivateEndpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetDbManagementPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbManagementPrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_asm(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalAsm'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalAsm')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalAsm')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_asm(
                external_asm_id=request.pop(util.camelize('externalAsmId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalAsm',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalAsm',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_asm_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalAsmConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalAsmConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalAsmConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_asm_configuration(
                external_asm_id=request.pop(util.camelize('externalAsmId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalAsmConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalAsmConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_asm_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalAsmInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalAsmInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalAsmInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_asm_instance(
                external_asm_instance_id=request.pop(util.camelize('externalAsmInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalAsmInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalAsmInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_cluster(
                external_cluster_id=request.pop(util.camelize('externalClusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalCluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_cluster_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalClusterInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalClusterInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalClusterInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_cluster_instance(
                external_cluster_instance_id=request.pop(util.camelize('externalClusterInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalClusterInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalClusterInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_db_home(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalDbHome'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalDbHome')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalDbHome')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_db_home(
                external_db_home_id=request.pop(util.camelize('externalDbHomeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalDbHome',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbHome',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_db_node(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalDbNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalDbNode')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalDbNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_db_node(
                external_db_node_id=request.pop(util.camelize('externalDbNodeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalDbNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbNode',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_db_system(
                external_db_system_id=request.pop(util.camelize('externalDbSystemId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbSystem',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_db_system_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalDbSystemConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalDbSystemConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalDbSystemConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_db_system_connector(
                external_db_system_connector_id=request.pop(util.camelize('externalDbSystemConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalDbSystemConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbSystemConnector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_db_system_discovery(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalDbSystemDiscovery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalDbSystemDiscovery')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalDbSystemDiscovery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_db_system_discovery(
                external_db_system_discovery_id=request.pop(util.camelize('externalDbSystemDiscoveryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalDbSystemDiscovery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbSystemDiscovery',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_exadata_infrastructure(
                external_exadata_infrastructure_id=request.pop(util.camelize('externalExadataInfrastructureId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalExadataInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_exadata_storage_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalExadataStorageConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalExadataStorageConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalExadataStorageConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_exadata_storage_connector(
                external_exadata_storage_connector_id=request.pop(util.camelize('externalExadataStorageConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalExadataStorageConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalExadataStorageConnector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_exadata_storage_grid(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalExadataStorageGrid'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalExadataStorageGrid')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalExadataStorageGrid')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_exadata_storage_grid(
                external_exadata_storage_grid_id=request.pop(util.camelize('externalExadataStorageGridId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalExadataStorageGrid',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalExadataStorageGrid',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_exadata_storage_server(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalExadataStorageServer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalExadataStorageServer')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalExadataStorageServer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_exadata_storage_server(
                external_exadata_storage_server_id=request.pop(util.camelize('externalExadataStorageServerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalExadataStorageServer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalExadataStorageServer',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_external_listener(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetExternalListener'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetExternalListener')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetExternalListener')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_external_listener(
                external_listener_id=request.pop(util.camelize('externalListenerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetExternalListener',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalListener',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_iorm_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetIormPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetIormPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetIormPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_iorm_plan(
                external_exadata_storage_server_id=request.pop(util.camelize('externalExadataStorageServerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetIormPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'iormPlan',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_job(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetJob')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_job(
                job_id=request.pop(util.camelize('jobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_job_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetJobExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetJobExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetJobExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_job_execution(
                job_execution_id=request.pop(util.camelize('jobExecutionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetJobExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobExecution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_job_run(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetJobRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetJobRun')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetJobRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_job_run(
                job_run_id=request.pop(util.camelize('jobRunId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetJobRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobRun',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_managed_database(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetManagedDatabase'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetManagedDatabase')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetManagedDatabase')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_managed_database(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetManagedDatabase',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedDatabase',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_managed_database_group(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetManagedDatabaseGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetManagedDatabaseGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetManagedDatabaseGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_managed_database_group(
                managed_database_group_id=request.pop(util.camelize('managedDatabaseGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetManagedDatabaseGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedDatabaseGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_open_alert_history(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetOpenAlertHistory'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetOpenAlertHistory')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetOpenAlertHistory')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_open_alert_history(
                external_exadata_storage_server_id=request.pop(util.camelize('externalExadataStorageServerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetOpenAlertHistory',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'openAlertHistory',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_optimizer_statistics_advisor_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetOptimizerStatisticsAdvisorExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetOptimizerStatisticsAdvisorExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetOptimizerStatisticsAdvisorExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_optimizer_statistics_advisor_execution(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                execution_name=request.pop(util.camelize('executionName')),
                task_name=request.pop(util.camelize('taskName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetOptimizerStatisticsAdvisorExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'optimizerStatisticsAdvisorExecution',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_optimizer_statistics_advisor_execution_script(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetOptimizerStatisticsAdvisorExecutionScript'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetOptimizerStatisticsAdvisorExecutionScript')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetOptimizerStatisticsAdvisorExecutionScript')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_optimizer_statistics_advisor_execution_script(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                execution_name=request.pop(util.camelize('executionName')),
                task_name=request.pop(util.camelize('taskName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetOptimizerStatisticsAdvisorExecutionScript',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'optimizerStatisticsAdvisorExecutionScript',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_optimizer_statistics_collection_operation(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetOptimizerStatisticsCollectionOperation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetOptimizerStatisticsCollectionOperation')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetOptimizerStatisticsCollectionOperation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_optimizer_statistics_collection_operation(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                optimizer_statistics_collection_operation_id=request.pop(util.camelize('optimizerStatisticsCollectionOperationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetOptimizerStatisticsCollectionOperation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'optimizerStatisticsCollectionOperation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_pdb_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetPdbMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetPdbMetrics')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetPdbMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_pdb_metrics(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                start_time=request.pop(util.camelize('startTime')),
                end_time=request.pop(util.camelize('endTime')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetPdbMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pdbMetrics',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_preferred_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetPreferredCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetPreferredCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetPreferredCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_preferred_credential(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                credential_name=request.pop(util.camelize('credentialName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetPreferredCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'preferredCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_tablespace(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetTablespace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetTablespace')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetTablespace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_tablespace(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                tablespace_name=request.pop(util.camelize('tablespaceName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetTablespace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tablespace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_top_sql_cpu_activity(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetTopSqlCpuActivity'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetTopSqlCpuActivity')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetTopSqlCpuActivity')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_top_sql_cpu_activity(
                external_exadata_storage_server_id=request.pop(util.camelize('externalExadataStorageServerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetTopSqlCpuActivity',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'topSqlCpuActivity',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_user(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetUser')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_user(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                user_name=request.pop(util.camelize('userName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'user',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_implement_optimizer_statistics_advisor_recommendations(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ImplementOptimizerStatisticsAdvisorRecommendations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ImplementOptimizerStatisticsAdvisorRecommendations')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ImplementOptimizerStatisticsAdvisorRecommendations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.implement_optimizer_statistics_advisor_recommendations(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                execution_name=request.pop(util.camelize('executionName')),
                implement_optimizer_statistics_advisor_recommendations_details=request.pop(util.camelize('ImplementOptimizerStatisticsAdvisorRecommendationsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ImplementOptimizerStatisticsAdvisorRecommendations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_asm_properties(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListAsmProperties'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListAsmProperties')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListAsmProperties')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_asm_properties(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_asm_properties(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_asm_properties(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListAsmProperties',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'asmPropertyCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_associated_databases(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListAssociatedDatabases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListAssociatedDatabases')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListAssociatedDatabases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_associated_databases(
                db_management_private_endpoint_id=request.pop(util.camelize('dbManagementPrivateEndpointId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_associated_databases(
                    db_management_private_endpoint_id=request.pop(util.camelize('dbManagementPrivateEndpointId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_associated_databases(
                        db_management_private_endpoint_id=request.pop(util.camelize('dbManagementPrivateEndpointId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListAssociatedDatabases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'associatedDatabaseCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_awr_db_snapshots(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListAwrDbSnapshots'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListAwrDbSnapshots')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListAwrDbSnapshots')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_awr_db_snapshots(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                awr_db_id=request.pop(util.camelize('awrDbId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_awr_db_snapshots(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    awr_db_id=request.pop(util.camelize('awrDbId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_awr_db_snapshots(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        awr_db_id=request.pop(util.camelize('awrDbId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListAwrDbSnapshots',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDbSnapshotCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_awr_dbs(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListAwrDbs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListAwrDbs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListAwrDbs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_awr_dbs(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_awr_dbs(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_awr_dbs(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListAwrDbs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDbCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_consumer_group_privileges(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListConsumerGroupPrivileges'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListConsumerGroupPrivileges')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListConsumerGroupPrivileges')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_consumer_group_privileges(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                user_name=request.pop(util.camelize('userName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_consumer_group_privileges(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    user_name=request.pop(util.camelize('userName')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_consumer_group_privileges(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        user_name=request.pop(util.camelize('userName')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListConsumerGroupPrivileges',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'consumerGroupPrivilegeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_data_access_containers(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListDataAccessContainers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListDataAccessContainers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListDataAccessContainers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_data_access_containers(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                user_name=request.pop(util.camelize('userName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_access_containers(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    user_name=request.pop(util.camelize('userName')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_access_containers(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        user_name=request.pop(util.camelize('userName')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListDataAccessContainers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAccessContainerCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_database_parameters(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListDatabaseParameters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListDatabaseParameters')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListDatabaseParameters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_database_parameters(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListDatabaseParameters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseParametersCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_db_management_private_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListDbManagementPrivateEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListDbManagementPrivateEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListDbManagementPrivateEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_db_management_private_endpoints(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_db_management_private_endpoints(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_db_management_private_endpoints(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListDbManagementPrivateEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbManagementPrivateEndpointCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_asm_disk_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalAsmDiskGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalAsmDiskGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalAsmDiskGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_asm_disk_groups(
                external_asm_id=request.pop(util.camelize('externalAsmId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_asm_disk_groups(
                    external_asm_id=request.pop(util.camelize('externalAsmId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_asm_disk_groups(
                        external_asm_id=request.pop(util.camelize('externalAsmId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalAsmDiskGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalAsmDiskGroupCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_asm_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalAsmInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalAsmInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalAsmInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_asm_instances(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_asm_instances(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_asm_instances(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalAsmInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalAsmInstanceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_asm_users(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalAsmUsers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalAsmUsers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalAsmUsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_asm_users(
                external_asm_id=request.pop(util.camelize('externalAsmId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_asm_users(
                    external_asm_id=request.pop(util.camelize('externalAsmId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_asm_users(
                        external_asm_id=request.pop(util.camelize('externalAsmId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalAsmUsers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalAsmUserCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_asms(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalAsms'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalAsms')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalAsms')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_asms(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_asms(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_asms(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalAsms',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalAsmCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_cluster_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalClusterInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalClusterInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalClusterInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_cluster_instances(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_cluster_instances(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_cluster_instances(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalClusterInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalClusterInstanceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_clusters(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalClusters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalClusters')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalClusters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_clusters(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_clusters(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_clusters(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalClusters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalClusterCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_databases(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalDatabases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalDatabases')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalDatabases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_databases(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_databases(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_databases(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalDatabases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDatabaseCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_db_homes(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalDbHomes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalDbHomes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalDbHomes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_db_homes(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_db_homes(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_db_homes(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalDbHomes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbHomeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_db_nodes(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalDbNodes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalDbNodes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalDbNodes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_db_nodes(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_db_nodes(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_db_nodes(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalDbNodes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbNodeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_db_system_connectors(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalDbSystemConnectors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalDbSystemConnectors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalDbSystemConnectors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_db_system_connectors(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_db_system_connectors(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_db_system_connectors(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalDbSystemConnectors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbSystemConnectorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_db_system_discoveries(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalDbSystemDiscoveries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalDbSystemDiscoveries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalDbSystemDiscoveries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_db_system_discoveries(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_db_system_discoveries(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_db_system_discoveries(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalDbSystemDiscoveries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbSystemDiscoveryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_db_systems(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalDbSystems'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalDbSystems')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalDbSystems')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_db_systems(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_db_systems(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_db_systems(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalDbSystems',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbSystemCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_exadata_infrastructures(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalExadataInfrastructures'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalExadataInfrastructures')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalExadataInfrastructures')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_exadata_infrastructures(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_exadata_infrastructures(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_exadata_infrastructures(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalExadataInfrastructures',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalExadataInfrastructureCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_exadata_storage_connectors(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalExadataStorageConnectors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalExadataStorageConnectors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalExadataStorageConnectors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_exadata_storage_connectors(
                compartment_id=request.pop(util.camelize('compartmentId')),
                external_exadata_infrastructure_id=request.pop(util.camelize('externalExadataInfrastructureId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_exadata_storage_connectors(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    external_exadata_infrastructure_id=request.pop(util.camelize('externalExadataInfrastructureId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_exadata_storage_connectors(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        external_exadata_infrastructure_id=request.pop(util.camelize('externalExadataInfrastructureId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalExadataStorageConnectors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalExadataStorageConnectorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_exadata_storage_servers(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalExadataStorageServers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalExadataStorageServers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalExadataStorageServers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_exadata_storage_servers(
                compartment_id=request.pop(util.camelize('compartmentId')),
                external_exadata_infrastructure_id=request.pop(util.camelize('externalExadataInfrastructureId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_exadata_storage_servers(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    external_exadata_infrastructure_id=request.pop(util.camelize('externalExadataInfrastructureId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_exadata_storage_servers(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        external_exadata_infrastructure_id=request.pop(util.camelize('externalExadataInfrastructureId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalExadataStorageServers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalExadataStorageServerCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_listener_services(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalListenerServices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalListenerServices')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalListenerServices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_listener_services(
                external_listener_id=request.pop(util.camelize('externalListenerId')),
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_listener_services(
                    external_listener_id=request.pop(util.camelize('externalListenerId')),
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_listener_services(
                        external_listener_id=request.pop(util.camelize('externalListenerId')),
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalListenerServices',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalListenerServiceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_external_listeners(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListExternalListeners'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListExternalListeners')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListExternalListeners')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_external_listeners(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_listeners(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_listeners(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListExternalListeners',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalListenerCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_job_executions(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListJobExecutions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListJobExecutions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListJobExecutions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_job_executions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_job_executions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_job_executions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListJobExecutions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobExecutionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_job_runs(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListJobRuns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListJobRuns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListJobRuns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_job_runs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_job_runs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_job_runs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListJobRuns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobRunCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListJobs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_jobs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_jobs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_jobs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_managed_database_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListManagedDatabaseGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListManagedDatabaseGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListManagedDatabaseGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_database_groups(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_database_groups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_database_groups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListManagedDatabaseGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedDatabaseGroupCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_managed_databases(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListManagedDatabases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListManagedDatabases')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListManagedDatabases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_databases(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_databases(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_databases(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListManagedDatabases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedDatabaseCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_object_privileges(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListObjectPrivileges'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListObjectPrivileges')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListObjectPrivileges')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_object_privileges(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                user_name=request.pop(util.camelize('userName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_object_privileges(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    user_name=request.pop(util.camelize('userName')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_object_privileges(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        user_name=request.pop(util.camelize('userName')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListObjectPrivileges',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'objectPrivilegeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_optimizer_statistics_advisor_executions(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListOptimizerStatisticsAdvisorExecutions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListOptimizerStatisticsAdvisorExecutions')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListOptimizerStatisticsAdvisorExecutions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_optimizer_statistics_advisor_executions(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListOptimizerStatisticsAdvisorExecutions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'optimizerStatisticsAdvisorExecutionsCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_optimizer_statistics_collection_aggregations(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListOptimizerStatisticsCollectionAggregations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListOptimizerStatisticsCollectionAggregations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListOptimizerStatisticsCollectionAggregations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_optimizer_statistics_collection_aggregations(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                group_type=request.pop(util.camelize('groupType')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_optimizer_statistics_collection_aggregations(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    group_type=request.pop(util.camelize('groupType')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_optimizer_statistics_collection_aggregations(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        group_type=request.pop(util.camelize('groupType')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListOptimizerStatisticsCollectionAggregations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'optimizerStatisticsCollectionAggregationsCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_optimizer_statistics_collection_operations(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListOptimizerStatisticsCollectionOperations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListOptimizerStatisticsCollectionOperations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListOptimizerStatisticsCollectionOperations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_optimizer_statistics_collection_operations(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_optimizer_statistics_collection_operations(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_optimizer_statistics_collection_operations(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListOptimizerStatisticsCollectionOperations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'optimizerStatisticsCollectionOperationsCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_preferred_credentials(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListPreferredCredentials'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListPreferredCredentials')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListPreferredCredentials')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_preferred_credentials(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListPreferredCredentials',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'preferredCredentialCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_proxied_for_users(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListProxiedForUsers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListProxiedForUsers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListProxiedForUsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_proxied_for_users(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                user_name=request.pop(util.camelize('userName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_proxied_for_users(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    user_name=request.pop(util.camelize('userName')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_proxied_for_users(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        user_name=request.pop(util.camelize('userName')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListProxiedForUsers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'proxiedForUserCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_proxy_users(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListProxyUsers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListProxyUsers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListProxyUsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_proxy_users(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                user_name=request.pop(util.camelize('userName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_proxy_users(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    user_name=request.pop(util.camelize('userName')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_proxy_users(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        user_name=request.pop(util.camelize('userName')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListProxyUsers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'proxyUserCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_roles(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListRoles'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListRoles')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListRoles')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_roles(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                user_name=request.pop(util.camelize('userName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_roles(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    user_name=request.pop(util.camelize('userName')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_roles(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        user_name=request.pop(util.camelize('userName')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListRoles',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_system_privileges(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListSystemPrivileges'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListSystemPrivileges')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListSystemPrivileges')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_system_privileges(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                user_name=request.pop(util.camelize('userName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_system_privileges(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    user_name=request.pop(util.camelize('userName')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_system_privileges(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        user_name=request.pop(util.camelize('userName')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListSystemPrivileges',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'systemPrivilegeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_table_statistics(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListTableStatistics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListTableStatistics')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListTableStatistics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_table_statistics(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListTableStatistics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tableStatisticsCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_tablespaces(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListTablespaces'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListTablespaces')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListTablespaces')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_tablespaces(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tablespaces(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tablespaces(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListTablespaces',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tablespaceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_users(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListUsers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListUsers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListUsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_users(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_users(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_users(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListUsers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_patch_external_db_system_discovery(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'PatchExternalDbSystemDiscovery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'PatchExternalDbSystemDiscovery')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='PatchExternalDbSystemDiscovery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.patch_external_db_system_discovery(
                external_db_system_discovery_id=request.pop(util.camelize('externalDbSystemDiscoveryId')),
                patch_external_db_system_discovery_details=request.pop(util.camelize('PatchExternalDbSystemDiscoveryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'PatchExternalDbSystemDiscovery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbSystemDiscovery',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_remove_data_file(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'RemoveDataFile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'RemoveDataFile')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='RemoveDataFile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.remove_data_file(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                tablespace_name=request.pop(util.camelize('tablespaceName')),
                remove_data_file_details=request.pop(util.camelize('RemoveDataFileDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'RemoveDataFile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tablespaceAdminStatus',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_remove_managed_database_from_managed_database_group(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'RemoveManagedDatabaseFromManagedDatabaseGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'RemoveManagedDatabaseFromManagedDatabaseGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='RemoveManagedDatabaseFromManagedDatabaseGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.remove_managed_database_from_managed_database_group(
                managed_database_group_id=request.pop(util.camelize('managedDatabaseGroupId')),
                remove_managed_database_from_managed_database_group_details=request.pop(util.camelize('RemoveManagedDatabaseFromManagedDatabaseGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'RemoveManagedDatabaseFromManagedDatabaseGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_managed_database_from_managed_database_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_reset_database_parameters(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ResetDatabaseParameters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ResetDatabaseParameters')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ResetDatabaseParameters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.reset_database_parameters(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                reset_database_parameters_details=request.pop(util.camelize('ResetDatabaseParametersDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ResetDatabaseParameters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'updateDatabaseParametersResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_resize_data_file(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'ResizeDataFile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'ResizeDataFile')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='ResizeDataFile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.resize_data_file(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                tablespace_name=request.pop(util.camelize('tablespaceName')),
                resize_data_file_details=request.pop(util.camelize('ResizeDataFileDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'ResizeDataFile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tablespaceAdminStatus',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_run_historic_addm(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'RunHistoricAddm'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'RunHistoricAddm')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='RunHistoricAddm')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.run_historic_addm(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                run_historic_addm_details=request.pop(util.camelize('RunHistoricAddmDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'RunHistoricAddm',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'historicAddmResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_awr_db_cpu_usages(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeAwrDbCpuUsages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeAwrDbCpuUsages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeAwrDbCpuUsages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_db_cpu_usages(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                awr_db_id=request.pop(util.camelize('awrDbId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_db_cpu_usages(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    awr_db_id=request.pop(util.camelize('awrDbId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_db_cpu_usages(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        awr_db_id=request.pop(util.camelize('awrDbId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeAwrDbCpuUsages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDbCpuUsageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_awr_db_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeAwrDbMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeAwrDbMetrics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeAwrDbMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_db_metrics(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                awr_db_id=request.pop(util.camelize('awrDbId')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_db_metrics(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    awr_db_id=request.pop(util.camelize('awrDbId')),
                    name=request.pop(util.camelize('name')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_db_metrics(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        awr_db_id=request.pop(util.camelize('awrDbId')),
                        name=request.pop(util.camelize('name')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeAwrDbMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDbMetricCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_awr_db_parameter_changes(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeAwrDbParameterChanges'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeAwrDbParameterChanges')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeAwrDbParameterChanges')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_db_parameter_changes(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                awr_db_id=request.pop(util.camelize('awrDbId')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_db_parameter_changes(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    awr_db_id=request.pop(util.camelize('awrDbId')),
                    name=request.pop(util.camelize('name')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_db_parameter_changes(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        awr_db_id=request.pop(util.camelize('awrDbId')),
                        name=request.pop(util.camelize('name')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeAwrDbParameterChanges',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDbParameterChangeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_awr_db_parameters(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeAwrDbParameters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeAwrDbParameters')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeAwrDbParameters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_db_parameters(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                awr_db_id=request.pop(util.camelize('awrDbId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_db_parameters(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    awr_db_id=request.pop(util.camelize('awrDbId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_db_parameters(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        awr_db_id=request.pop(util.camelize('awrDbId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeAwrDbParameters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDbParameterCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_awr_db_snapshot_ranges(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeAwrDbSnapshotRanges'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeAwrDbSnapshotRanges')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeAwrDbSnapshotRanges')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_db_snapshot_ranges(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_db_snapshot_ranges(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_db_snapshot_ranges(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeAwrDbSnapshotRanges',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDbSnapshotRangeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_awr_db_sysstats(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeAwrDbSysstats'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeAwrDbSysstats')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeAwrDbSysstats')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_db_sysstats(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                awr_db_id=request.pop(util.camelize('awrDbId')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_db_sysstats(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    awr_db_id=request.pop(util.camelize('awrDbId')),
                    name=request.pop(util.camelize('name')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_db_sysstats(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        awr_db_id=request.pop(util.camelize('awrDbId')),
                        name=request.pop(util.camelize('name')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeAwrDbSysstats',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDbSysstatCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_awr_db_top_wait_events(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeAwrDbTopWaitEvents'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeAwrDbTopWaitEvents')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeAwrDbTopWaitEvents')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_db_top_wait_events(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                awr_db_id=request.pop(util.camelize('awrDbId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeAwrDbTopWaitEvents',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDbTopWaitEventCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_awr_db_wait_event_buckets(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeAwrDbWaitEventBuckets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeAwrDbWaitEventBuckets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeAwrDbWaitEventBuckets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_db_wait_event_buckets(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                awr_db_id=request.pop(util.camelize('awrDbId')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_db_wait_event_buckets(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    awr_db_id=request.pop(util.camelize('awrDbId')),
                    name=request.pop(util.camelize('name')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_db_wait_event_buckets(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        awr_db_id=request.pop(util.camelize('awrDbId')),
                        name=request.pop(util.camelize('name')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeAwrDbWaitEventBuckets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDbWaitEventBucketCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_awr_db_wait_events(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeAwrDbWaitEvents'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeAwrDbWaitEvents')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeAwrDbWaitEvents')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_awr_db_wait_events(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                awr_db_id=request.pop(util.camelize('awrDbId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_awr_db_wait_events(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    awr_db_id=request.pop(util.camelize('awrDbId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_awr_db_wait_events(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        awr_db_id=request.pop(util.camelize('awrDbId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeAwrDbWaitEvents',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'awrDbWaitEventCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_external_asm_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeExternalAsmMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeExternalAsmMetrics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeExternalAsmMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_external_asm_metrics(
                external_asm_id=request.pop(util.camelize('externalAsmId')),
                start_time=request.pop(util.camelize('startTime')),
                end_time=request.pop(util.camelize('endTime')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_external_asm_metrics(
                    external_asm_id=request.pop(util.camelize('externalAsmId')),
                    start_time=request.pop(util.camelize('startTime')),
                    end_time=request.pop(util.camelize('endTime')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_external_asm_metrics(
                        external_asm_id=request.pop(util.camelize('externalAsmId')),
                        start_time=request.pop(util.camelize('startTime')),
                        end_time=request.pop(util.camelize('endTime')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeExternalAsmMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'metricsAggregationRangeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_external_cluster_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeExternalClusterMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeExternalClusterMetrics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeExternalClusterMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_external_cluster_metrics(
                external_cluster_id=request.pop(util.camelize('externalClusterId')),
                start_time=request.pop(util.camelize('startTime')),
                end_time=request.pop(util.camelize('endTime')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_external_cluster_metrics(
                    external_cluster_id=request.pop(util.camelize('externalClusterId')),
                    start_time=request.pop(util.camelize('startTime')),
                    end_time=request.pop(util.camelize('endTime')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_external_cluster_metrics(
                        external_cluster_id=request.pop(util.camelize('externalClusterId')),
                        start_time=request.pop(util.camelize('startTime')),
                        end_time=request.pop(util.camelize('endTime')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeExternalClusterMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'metricsAggregationRangeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_external_db_node_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeExternalDbNodeMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeExternalDbNodeMetrics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeExternalDbNodeMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_external_db_node_metrics(
                external_db_node_id=request.pop(util.camelize('externalDbNodeId')),
                start_time=request.pop(util.camelize('startTime')),
                end_time=request.pop(util.camelize('endTime')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_external_db_node_metrics(
                    external_db_node_id=request.pop(util.camelize('externalDbNodeId')),
                    start_time=request.pop(util.camelize('startTime')),
                    end_time=request.pop(util.camelize('endTime')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_external_db_node_metrics(
                        external_db_node_id=request.pop(util.camelize('externalDbNodeId')),
                        start_time=request.pop(util.camelize('startTime')),
                        end_time=request.pop(util.camelize('endTime')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeExternalDbNodeMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'metricsAggregationRangeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_external_db_system_availability_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeExternalDbSystemAvailabilityMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeExternalDbSystemAvailabilityMetrics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeExternalDbSystemAvailabilityMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_external_db_system_availability_metrics(
                external_db_system_id=request.pop(util.camelize('externalDbSystemId')),
                start_time=request.pop(util.camelize('startTime')),
                end_time=request.pop(util.camelize('endTime')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_external_db_system_availability_metrics(
                    external_db_system_id=request.pop(util.camelize('externalDbSystemId')),
                    start_time=request.pop(util.camelize('startTime')),
                    end_time=request.pop(util.camelize('endTime')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_external_db_system_availability_metrics(
                        external_db_system_id=request.pop(util.camelize('externalDbSystemId')),
                        start_time=request.pop(util.camelize('startTime')),
                        end_time=request.pop(util.camelize('endTime')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeExternalDbSystemAvailabilityMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'metricsAggregationRangeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_external_listener_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeExternalListenerMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeExternalListenerMetrics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeExternalListenerMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_external_listener_metrics(
                external_listener_id=request.pop(util.camelize('externalListenerId')),
                start_time=request.pop(util.camelize('startTime')),
                end_time=request.pop(util.camelize('endTime')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_external_listener_metrics(
                    external_listener_id=request.pop(util.camelize('externalListenerId')),
                    start_time=request.pop(util.camelize('startTime')),
                    end_time=request.pop(util.camelize('endTime')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_external_listener_metrics(
                        external_listener_id=request.pop(util.camelize('externalListenerId')),
                        start_time=request.pop(util.camelize('startTime')),
                        end_time=request.pop(util.camelize('endTime')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeExternalListenerMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'metricsAggregationRangeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_job_executions_statuses(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeJobExecutionsStatuses'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeJobExecutionsStatuses')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeJobExecutionsStatuses')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_job_executions_statuses(
                compartment_id=request.pop(util.camelize('compartmentId')),
                start_time=request.pop(util.camelize('startTime')),
                end_time=request.pop(util.camelize('endTime')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeJobExecutionsStatuses',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobExecutionsStatusSummaryCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_summarize_managed_database_availability_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'SummarizeManagedDatabaseAvailabilityMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'SummarizeManagedDatabaseAvailabilityMetrics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='SummarizeManagedDatabaseAvailabilityMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.summarize_managed_database_availability_metrics(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                start_time=request.pop(util.camelize('startTime')),
                end_time=request.pop(util.camelize('endTime')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_managed_database_availability_metrics(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    start_time=request.pop(util.camelize('startTime')),
                    end_time=request.pop(util.camelize('endTime')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_managed_database_availability_metrics(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        start_time=request.pop(util.camelize('startTime')),
                        end_time=request.pop(util.camelize('endTime')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'SummarizeManagedDatabaseAvailabilityMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'metricsAggregationRangeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_test_preferred_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'TestPreferredCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'TestPreferredCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='TestPreferredCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.test_preferred_credential(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                credential_name=request.pop(util.camelize('credentialName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'TestPreferredCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'testPreferredCredentialStatus',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_db_management_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateDbManagementPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateDbManagementPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateDbManagementPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_db_management_private_endpoint(
                db_management_private_endpoint_id=request.pop(util.camelize('dbManagementPrivateEndpointId')),
                update_db_management_private_endpoint_details=request.pop(util.camelize('UpdateDbManagementPrivateEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateDbManagementPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dbManagementPrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_external_asm(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateExternalAsm'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateExternalAsm')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateExternalAsm')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_external_asm(
                external_asm_id=request.pop(util.camelize('externalAsmId')),
                update_external_asm_details=request.pop(util.camelize('UpdateExternalAsmDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateExternalAsm',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_external_asm',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_external_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateExternalCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateExternalCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateExternalCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_external_cluster(
                external_cluster_id=request.pop(util.camelize('externalClusterId')),
                update_external_cluster_details=request.pop(util.camelize('UpdateExternalClusterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateExternalCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_external_cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_external_cluster_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateExternalClusterInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateExternalClusterInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateExternalClusterInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_external_cluster_instance(
                external_cluster_instance_id=request.pop(util.camelize('externalClusterInstanceId')),
                update_external_cluster_instance_details=request.pop(util.camelize('UpdateExternalClusterInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateExternalClusterInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_external_cluster_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_external_db_node(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateExternalDbNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateExternalDbNode')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateExternalDbNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_external_db_node(
                external_db_node_id=request.pop(util.camelize('externalDbNodeId')),
                update_external_db_node_details=request.pop(util.camelize('UpdateExternalDbNodeDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateExternalDbNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_external_db_node',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_external_db_system(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateExternalDbSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateExternalDbSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateExternalDbSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_external_db_system(
                external_db_system_id=request.pop(util.camelize('externalDbSystemId')),
                update_external_db_system_details=request.pop(util.camelize('UpdateExternalDbSystemDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateExternalDbSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbSystem',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_external_db_system_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateExternalDbSystemConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateExternalDbSystemConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateExternalDbSystemConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_external_db_system_connector(
                external_db_system_connector_id=request.pop(util.camelize('externalDbSystemConnectorId')),
                update_external_db_system_connector_details=request.pop(util.camelize('UpdateExternalDbSystemConnectorDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateExternalDbSystemConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_external_db_system_connector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_external_db_system_discovery(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateExternalDbSystemDiscovery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateExternalDbSystemDiscovery')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateExternalDbSystemDiscovery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_external_db_system_discovery(
                external_db_system_discovery_id=request.pop(util.camelize('externalDbSystemDiscoveryId')),
                update_external_db_system_discovery_details=request.pop(util.camelize('UpdateExternalDbSystemDiscoveryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateExternalDbSystemDiscovery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalDbSystemDiscovery',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_external_exadata_infrastructure(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateExternalExadataInfrastructure'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateExternalExadataInfrastructure')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateExternalExadataInfrastructure')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_external_exadata_infrastructure(
                external_exadata_infrastructure_id=request.pop(util.camelize('externalExadataInfrastructureId')),
                update_external_exadata_infrastructure_details=request.pop(util.camelize('UpdateExternalExadataInfrastructureDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateExternalExadataInfrastructure',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalExadataInfrastructure',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_external_exadata_storage_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateExternalExadataStorageConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateExternalExadataStorageConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateExternalExadataStorageConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_external_exadata_storage_connector(
                external_exadata_storage_connector_id=request.pop(util.camelize('externalExadataStorageConnectorId')),
                update_external_exadata_storage_connector_details=request.pop(util.camelize('UpdateExternalExadataStorageConnectorDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateExternalExadataStorageConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalExadataStorageConnector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_external_listener(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateExternalListener'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateExternalListener')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateExternalListener')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_external_listener(
                external_listener_id=request.pop(util.camelize('externalListenerId')),
                update_external_listener_details=request.pop(util.camelize('UpdateExternalListenerDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateExternalListener',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_external_listener',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_job(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateJob')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_job(
                job_id=request.pop(util.camelize('jobId')),
                update_job_details=request.pop(util.camelize('UpdateJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_managed_database_group(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateManagedDatabaseGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateManagedDatabaseGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateManagedDatabaseGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_managed_database_group(
                managed_database_group_id=request.pop(util.camelize('managedDatabaseGroupId')),
                update_managed_database_group_details=request.pop(util.camelize('UpdateManagedDatabaseGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateManagedDatabaseGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedDatabaseGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_preferred_credential(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdatePreferredCredential'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdatePreferredCredential')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdatePreferredCredential')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_preferred_credential(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                credential_name=request.pop(util.camelize('credentialName')),
                update_preferred_credential_details=request.pop(util.camelize('UpdatePreferredCredentialDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdatePreferredCredential',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'preferredCredential',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="dpd_dev_grp@oracle.com" jiraProject="DPD" opsJiraProject="DPD"
def test_update_tablespace(testing_service_client):
    if not testing_service_client.is_api_enabled('database_management', 'UpdateTablespace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_management', util.camelize('db_management'), 'UpdateTablespace')
    )

    request_containers = testing_service_client.get_requests(service_name='database_management', api_name='UpdateTablespace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_management.DbManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_tablespace(
                managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                tablespace_name=request.pop(util.camelize('tablespaceName')),
                update_tablespace_details=request.pop(util.camelize('UpdateTablespaceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_management',
            'UpdateTablespace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tablespace',
            False,
            False
        )
