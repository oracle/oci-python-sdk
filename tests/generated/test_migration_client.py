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

        cassette_location = os.path.join('generated', 'cloud_migrations_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_cancel_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'CancelWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='CancelWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.cancel_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'CancelWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_migration_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ChangeMigrationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ChangeMigrationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ChangeMigrationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
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
            'cloud_migrations',
            'ChangeMigrationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_migration_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_migration_plan_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ChangeMigrationPlanCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ChangeMigrationPlanCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ChangeMigrationPlanCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.change_migration_plan_compartment(
                migration_plan_id=request.pop(util.camelize('migrationPlanId')),
                change_migration_plan_compartment_details=request.pop(util.camelize('ChangeMigrationPlanCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'ChangeMigrationPlanCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_migration_plan_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_replication_schedule_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ChangeReplicationScheduleCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ChangeReplicationScheduleCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ChangeReplicationScheduleCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.change_replication_schedule_compartment(
                replication_schedule_id=request.pop(util.camelize('replicationScheduleId')),
                change_replication_schedule_compartment_details=request.pop(util.camelize('ChangeReplicationScheduleCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'ChangeReplicationScheduleCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_replication_schedule_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'CreateMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'CreateMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='CreateMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.create_migration(
                create_migration_details=request.pop(util.camelize('CreateMigrationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'CreateMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_migration_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'CreateMigrationAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'CreateMigrationAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='CreateMigrationAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.create_migration_asset(
                create_migration_asset_details=request.pop(util.camelize('CreateMigrationAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'CreateMigrationAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrationAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_migration_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'CreateMigrationPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'CreateMigrationPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='CreateMigrationPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.create_migration_plan(
                create_migration_plan_details=request.pop(util.camelize('CreateMigrationPlanDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'CreateMigrationPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrationPlan',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_replication_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'CreateReplicationSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'CreateReplicationSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='CreateReplicationSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.create_replication_schedule(
                create_replication_schedule_details=request.pop(util.camelize('CreateReplicationScheduleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'CreateReplicationSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'replicationSchedule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_target_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'CreateTargetAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'CreateTargetAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='CreateTargetAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.create_target_asset(
                create_target_asset_details=request.pop(util.camelize('CreateTargetAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'CreateTargetAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'DeleteMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'DeleteMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='DeleteMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_migration(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'DeleteMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_migration',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_migration_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'DeleteMigrationAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'DeleteMigrationAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='DeleteMigrationAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_migration_asset(
                migration_asset_id=request.pop(util.camelize('migrationAssetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'DeleteMigrationAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_migration_asset',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_migration_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'DeleteMigrationPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'DeleteMigrationPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='DeleteMigrationPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_migration_plan(
                migration_plan_id=request.pop(util.camelize('migrationPlanId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'DeleteMigrationPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_migration_plan',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_replication_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'DeleteReplicationSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'DeleteReplicationSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='DeleteReplicationSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_replication_schedule(
                replication_schedule_id=request.pop(util.camelize('replicationScheduleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'DeleteReplicationSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_replication_schedule',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_target_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'DeleteTargetAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'DeleteTargetAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='DeleteTargetAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_target_asset(
                target_asset_id=request.pop(util.camelize('targetAssetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'DeleteTargetAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_target_asset',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_execute_migration_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ExecuteMigrationPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ExecuteMigrationPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ExecuteMigrationPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.execute_migration_plan(
                migration_plan_id=request.pop(util.camelize('migrationPlanId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'ExecuteMigrationPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'execute_migration_plan',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_export_migration_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ExportMigrationPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ExportMigrationPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ExportMigrationPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.export_migration_plan(
                migration_plan_id=request.pop(util.camelize('migrationPlanId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'ExportMigrationPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'GetMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'GetMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='GetMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_migration(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'GetMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_migration_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'GetMigrationAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'GetMigrationAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='GetMigrationAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_migration_asset(
                migration_asset_id=request.pop(util.camelize('migrationAssetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'GetMigrationAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrationAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_migration_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'GetMigrationPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'GetMigrationPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='GetMigrationPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_migration_plan(
                migration_plan_id=request.pop(util.camelize('migrationPlanId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'GetMigrationPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrationPlan',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_replication_progress(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'GetReplicationProgress'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'GetReplicationProgress')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='GetReplicationProgress')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_replication_progress(
                migration_asset_id=request.pop(util.camelize('migrationAssetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'GetReplicationProgress',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'replicationProgress',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_replication_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'GetReplicationSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'GetReplicationSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='GetReplicationSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_replication_schedule(
                replication_schedule_id=request.pop(util.camelize('replicationScheduleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'GetReplicationSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'replicationSchedule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_target_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'GetTargetAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'GetTargetAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='GetTargetAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_target_asset(
                target_asset_id=request.pop(util.camelize('targetAssetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'GetTargetAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_import_migration_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ImportMigrationPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ImportMigrationPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ImportMigrationPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.import_migration_plan(
                migration_plan_id=request.pop(util.camelize('migrationPlanId')),
                import_migration_plan_details=request.pop(util.camelize('ImportMigrationPlanDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'ImportMigrationPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'import_migration_plan',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_available_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ListAvailableShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ListAvailableShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ListAvailableShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_available_shapes(
                migration_plan_id=request.pop(util.camelize('migrationPlanId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_available_shapes(
                    migration_plan_id=request.pop(util.camelize('migrationPlanId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_available_shapes(
                        migration_plan_id=request.pop(util.camelize('migrationPlanId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'ListAvailableShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'availableShapesCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_migration_assets(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ListMigrationAssets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ListMigrationAssets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ListMigrationAssets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_migration_assets(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_migration_assets(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_migration_assets(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'ListMigrationAssets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrationAssetCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_migration_plans(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ListMigrationPlans'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ListMigrationPlans')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ListMigrationPlans')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_migration_plans(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_migration_plans(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_migration_plans(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'ListMigrationPlans',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrationPlanCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_migrations(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ListMigrations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ListMigrations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ListMigrations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_migrations(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_migrations(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_migrations(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'ListMigrations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_replication_schedules(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ListReplicationSchedules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ListReplicationSchedules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ListReplicationSchedules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_replication_schedules(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_replication_schedules(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_replication_schedules(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'ListReplicationSchedules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'replicationScheduleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_target_assets(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ListTargetAssets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ListTargetAssets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ListTargetAssets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_target_assets(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_target_assets(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_target_assets(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'ListTargetAssets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'targetAssetCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
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
            'cloud_migrations',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
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
            'cloud_migrations',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_refresh_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'RefreshMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'RefreshMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='RefreshMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.refresh_migration(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'RefreshMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'refresh_migration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_refresh_migration_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'RefreshMigrationAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'RefreshMigrationAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='RefreshMigrationAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.refresh_migration_asset(
                migration_asset_id=request.pop(util.camelize('migrationAssetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'RefreshMigrationAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'refresh_migration_asset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_refresh_migration_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'RefreshMigrationPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'RefreshMigrationPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='RefreshMigrationPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.refresh_migration_plan(
                migration_plan_id=request.pop(util.camelize('migrationPlanId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'RefreshMigrationPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'refresh_migration_plan',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_start_asset_replication(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'StartAssetReplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'StartAssetReplication')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='StartAssetReplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.start_asset_replication(
                migration_asset_id=request.pop(util.camelize('migrationAssetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'StartAssetReplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_asset_replication',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_start_migration_replication(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'StartMigrationReplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'StartMigrationReplication')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='StartMigrationReplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.start_migration_replication(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'StartMigrationReplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_migration_replication',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'UpdateMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'UpdateMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='UpdateMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
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
            'cloud_migrations',
            'UpdateMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_migration_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'UpdateMigrationAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'UpdateMigrationAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='UpdateMigrationAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.update_migration_asset(
                migration_asset_id=request.pop(util.camelize('migrationAssetId')),
                update_migration_asset_details=request.pop(util.camelize('UpdateMigrationAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'UpdateMigrationAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrationAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_migration_plan(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'UpdateMigrationPlan'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'UpdateMigrationPlan')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='UpdateMigrationPlan')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.update_migration_plan(
                migration_plan_id=request.pop(util.camelize('migrationPlanId')),
                update_migration_plan_details=request.pop(util.camelize('UpdateMigrationPlanDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'UpdateMigrationPlan',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_migration_plan',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_replication_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'UpdateReplicationSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'UpdateReplicationSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='UpdateReplicationSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.update_replication_schedule(
                replication_schedule_id=request.pop(util.camelize('replicationScheduleId')),
                update_replication_schedule_details=request.pop(util.camelize('UpdateReplicationScheduleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'UpdateReplicationSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_replication_schedule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_customer_migration_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_target_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_migrations', 'UpdateTargetAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_migrations', util.camelize('migration'), 'UpdateTargetAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_migrations', api_name='UpdateTargetAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_migrations.MigrationClient(config, service_endpoint=service_endpoint)
            response = client.update_target_asset(
                target_asset_id=request.pop(util.camelize('targetAssetId')),
                update_target_asset_details=request.pop(util.camelize('UpdateTargetAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_migrations',
            'UpdateTargetAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_target_asset',
            False,
            False
        )
