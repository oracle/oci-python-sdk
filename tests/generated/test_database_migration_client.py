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

        cassette_location = os.path.join('generated', 'database_migration_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_abort_job(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'AbortJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'AbortJob')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='AbortJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.abort_job(
                job_id=request.pop(util.camelize('jobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'AbortJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_add_migration_objects(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'AddMigrationObjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'AddMigrationObjects')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='AddMigrationObjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.add_migration_objects(
                migration_id=request.pop(util.camelize('migrationId')),
                add_migration_objects_details=request.pop(util.camelize('AddMigrationObjectsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'AddMigrationObjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_migration_objects',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_change_agent_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ChangeAgentCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ChangeAgentCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ChangeAgentCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.change_agent_compartment(
                agent_id=request.pop(util.camelize('agentId')),
                change_agent_compartment_details=request.pop(util.camelize('ChangeAgentCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'ChangeAgentCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_agent_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_change_connection_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ChangeConnectionCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ChangeConnectionCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ChangeConnectionCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.change_connection_compartment(
                connection_id=request.pop(util.camelize('connectionId')),
                change_connection_compartment_details=request.pop(util.camelize('ChangeConnectionCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'ChangeConnectionCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_connection_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_change_migration_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ChangeMigrationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ChangeMigrationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ChangeMigrationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.change_migration_compartment(
                migration_id=request.pop(util.camelize('migrationId')),
                change_migration_compartment_details=request.pop(util.camelize('ChangeMigrationCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'ChangeMigrationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_migration_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_clone_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'CloneMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'CloneMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='CloneMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.clone_migration(
                migration_id=request.pop(util.camelize('migrationId')),
                clone_migration_details=request.pop(util.camelize('CloneMigrationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'CloneMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_create_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'CreateConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'CreateConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='CreateConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.create_connection(
                create_connection_details=request.pop(util.camelize('CreateConnectionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'CreateConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_create_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'CreateMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'CreateMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='CreateMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.create_migration(
                create_migration_details=request.pop(util.camelize('CreateMigrationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'CreateMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_delete_agent(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'DeleteAgent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'DeleteAgent')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='DeleteAgent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_agent(
                agent_id=request.pop(util.camelize('agentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'DeleteAgent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_agent',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_delete_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'DeleteConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'DeleteConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='DeleteConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_connection(
                connection_id=request.pop(util.camelize('connectionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'DeleteConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_connection',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_delete_job(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'DeleteJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'DeleteJob')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='DeleteJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_job(
                job_id=request.pop(util.camelize('jobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'DeleteJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_job',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_delete_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'DeleteMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'DeleteMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='DeleteMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_migration(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'DeleteMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_migration',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_evaluate_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'EvaluateMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'EvaluateMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='EvaluateMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.evaluate_migration(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'EvaluateMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_get_advisor_report(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'GetAdvisorReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'GetAdvisorReport')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='GetAdvisorReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_advisor_report(
                job_id=request.pop(util.camelize('jobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'GetAdvisorReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'advisorReport',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_get_agent(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'GetAgent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'GetAgent')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='GetAgent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_agent(
                agent_id=request.pop(util.camelize('agentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'GetAgent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'agent',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_get_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'GetConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'GetConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='GetConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_connection(
                connection_id=request.pop(util.camelize('connectionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'GetConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_get_job(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'GetJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'GetJob')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='GetJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_job(
                job_id=request.pop(util.camelize('jobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'GetJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_get_job_output_content(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'GetJobOutputContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'GetJobOutputContent')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='GetJobOutputContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_job_output_content(
                job_id=request.pop(util.camelize('jobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'GetJobOutputContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_get_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'GetMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'GetMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='GetMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_migration(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'GetMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_list_agent_images(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ListAgentImages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ListAgentImages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ListAgentImages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_agent_images(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_agent_images(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_agent_images(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'ListAgentImages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'agentImageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_list_agents(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ListAgents'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ListAgents')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ListAgents')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_agents(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_agents(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_agents(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'ListAgents',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'agentCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_list_connections(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ListConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ListConnections')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ListConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_connections(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_connections(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_connections(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'ListConnections',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_list_excluded_objects(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ListExcludedObjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ListExcludedObjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ListExcludedObjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_excluded_objects(
                job_id=request.pop(util.camelize('jobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_excluded_objects(
                    job_id=request.pop(util.camelize('jobId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_excluded_objects(
                        job_id=request.pop(util.camelize('jobId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'ListExcludedObjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'excludedObjectSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_list_job_outputs(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ListJobOutputs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ListJobOutputs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ListJobOutputs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_job_outputs(
                job_id=request.pop(util.camelize('jobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_job_outputs(
                    job_id=request.pop(util.camelize('jobId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_job_outputs(
                        job_id=request.pop(util.camelize('jobId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'ListJobOutputs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobOutputSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_list_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ListJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ListJobs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ListJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_jobs(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_jobs(
                    migration_id=request.pop(util.camelize('migrationId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_jobs(
                        migration_id=request.pop(util.camelize('migrationId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'ListJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_list_migration_object_types(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ListMigrationObjectTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ListMigrationObjectTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ListMigrationObjectTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_migration_object_types(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_migration_object_types(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_migration_object_types(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'ListMigrationObjectTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrationObjectTypeSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_list_migration_objects(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ListMigrationObjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ListMigrationObjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ListMigrationObjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_migration_objects(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_migration_objects(
                    migration_id=request.pop(util.camelize('migrationId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_migration_objects(
                        migration_id=request.pop(util.camelize('migrationId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'ListMigrationObjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrationObjectCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_list_migrations(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ListMigrations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ListMigrations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ListMigrations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_migrations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_migrations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_migrations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'ListMigrations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
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
            'database_migration',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
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
            'database_migration',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
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
            'database_migration',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_remove_migration_objects(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'RemoveMigrationObjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'RemoveMigrationObjects')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='RemoveMigrationObjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.remove_migration_objects(
                migration_id=request.pop(util.camelize('migrationId')),
                remove_migration_objects_details=request.pop(util.camelize('RemoveMigrationObjectsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'RemoveMigrationObjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_migration_objects',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_resume_job(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'ResumeJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'ResumeJob')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='ResumeJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.resume_job(
                job_id=request.pop(util.camelize('jobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'ResumeJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_retrieve_supported_phases(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'RetrieveSupportedPhases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'RetrieveSupportedPhases')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='RetrieveSupportedPhases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.retrieve_supported_phases(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'RetrieveSupportedPhases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrationPhaseCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_start_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'StartMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'StartMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='StartMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.start_migration(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'StartMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_update_agent(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'UpdateAgent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'UpdateAgent')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='UpdateAgent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.update_agent(
                agent_id=request.pop(util.camelize('agentId')),
                update_agent_details=request.pop(util.camelize('UpdateAgentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'UpdateAgent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'agent',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_update_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'UpdateConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'UpdateConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='UpdateConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.update_connection(
                connection_id=request.pop(util.camelize('connectionId')),
                update_connection_details=request.pop(util.camelize('UpdateConnectionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'UpdateConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_update_job(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'UpdateJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'UpdateJob')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='UpdateJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
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
            'database_migration',
            'UpdateJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="zdmdev_grp@oracle.com" jiraProject="ZDMCS" opsJiraProject="ZDMCS"
def test_update_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('database_migration', 'UpdateMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_migration', util.camelize('database_migration'), 'UpdateMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='database_migration', api_name='UpdateMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_migration.DatabaseMigrationClient(config, service_endpoint=service_endpoint)
            response = client.update_migration(
                migration_id=request.pop(util.camelize('migrationId')),
                update_migration_details=request.pop(util.camelize('UpdateMigrationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_migration',
            'UpdateMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_migration',
            False,
            False
        )
