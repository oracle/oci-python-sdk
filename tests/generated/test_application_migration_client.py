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

        cassette_location = os.path.join('generated', 'application_migration_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_cancel_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'CancelWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='CancelWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
            response = client.cancel_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'application_migration',
            'CancelWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_change_migration_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'ChangeMigrationCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'ChangeMigrationCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='ChangeMigrationCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
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
            'application_migration',
            'ChangeMigrationCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_migration_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_change_source_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'ChangeSourceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'ChangeSourceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='ChangeSourceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
            response = client.change_source_compartment(
                source_id=request.pop(util.camelize('sourceId')),
                change_source_compartment_details=request.pop(util.camelize('ChangeSourceCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'application_migration',
            'ChangeSourceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_source_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_create_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'CreateMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'CreateMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='CreateMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
            response = client.create_migration(
                create_migration_details=request.pop(util.camelize('CreateMigrationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'application_migration',
            'CreateMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_create_source(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'CreateSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'CreateSource')
    )

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='CreateSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
            response = client.create_source(
                create_source_details=request.pop(util.camelize('CreateSourceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'application_migration',
            'CreateSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'source',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_delete_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'DeleteMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'DeleteMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='DeleteMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_migration(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'application_migration',
            'DeleteMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_migration',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_delete_source(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'DeleteSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'DeleteSource')
    )

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='DeleteSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_source(
                source_id=request.pop(util.camelize('sourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'application_migration',
            'DeleteSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_source',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_get_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'GetMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'GetMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='GetMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_migration(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'application_migration',
            'GetMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_get_source(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'GetSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'GetSource')
    )

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='GetSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_source(
                source_id=request.pop(util.camelize('sourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'application_migration',
            'GetSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'source',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'application_migration',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_list_migrations(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'ListMigrations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'ListMigrations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='ListMigrations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
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
            'application_migration',
            'ListMigrations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrationSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_list_source_applications(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'ListSourceApplications'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'ListSourceApplications')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='ListSourceApplications')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_source_applications(
                source_id=request.pop(util.camelize('sourceId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_source_applications(
                    source_id=request.pop(util.camelize('sourceId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_source_applications(
                        source_id=request.pop(util.camelize('sourceId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'application_migration',
            'ListSourceApplications',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sourceApplicationSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_list_sources(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'ListSources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'ListSources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='ListSources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
            response = client.list_sources(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_sources(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_sources(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'application_migration',
            'ListSources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sourceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
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
            'application_migration',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
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
            'application_migration',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
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
            'application_migration',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_migrate_application(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'MigrateApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'MigrateApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='MigrateApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
            response = client.migrate_application(
                migration_id=request.pop(util.camelize('migrationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'application_migration',
            'MigrateApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'migrate_application',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_update_migration(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'UpdateMigration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'UpdateMigration')
    )

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='UpdateMigration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
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
            'application_migration',
            'UpdateMigration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_migration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-ams-dev_ww_grp@oracle.com" jiraProject="MIGRATE" opsJiraProject="MIGRATE"
def test_update_source(testing_service_client):
    if not testing_service_client.is_api_enabled('application_migration', 'UpdateSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('application_migration', util.camelize('application_migration'), 'UpdateSource')
    )

    request_containers = testing_service_client.get_requests(service_name='application_migration', api_name='UpdateSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.application_migration.ApplicationMigrationClient(config, service_endpoint=service_endpoint)
            response = client.update_source(
                source_id=request.pop(util.camelize('sourceId')),
                update_source_details=request.pop(util.camelize('UpdateSourceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'application_migration',
            'UpdateSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_source',
            False,
            False
        )
