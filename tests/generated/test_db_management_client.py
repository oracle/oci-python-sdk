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

        cassette_location = os.path.join('generated', 'database_management_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


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
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_job_executions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_job_executions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
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
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_job_runs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_job_runs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
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
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_jobs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_jobs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
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
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_database_groups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_database_groups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
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
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_databases(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_databases(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
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
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tablespaces(
                    managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tablespaces(
                        managed_database_id=request.pop(util.camelize('managedDatabaseId')),
                        page=next_response.headers[prev_page],
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
