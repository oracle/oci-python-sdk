# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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
