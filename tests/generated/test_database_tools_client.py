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

        cassette_location = os.path.join('generated', 'database_tools_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_change_database_tools_connection_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'ChangeDatabaseToolsConnectionCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'ChangeDatabaseToolsConnectionCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='ChangeDatabaseToolsConnectionCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.change_database_tools_connection_compartment(
                database_tools_connection_id=request.pop(util.camelize('databaseToolsConnectionId')),
                change_database_tools_connection_compartment_details=request.pop(util.camelize('ChangeDatabaseToolsConnectionCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'ChangeDatabaseToolsConnectionCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_database_tools_connection_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_change_database_tools_private_endpoint_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'ChangeDatabaseToolsPrivateEndpointCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'ChangeDatabaseToolsPrivateEndpointCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='ChangeDatabaseToolsPrivateEndpointCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.change_database_tools_private_endpoint_compartment(
                database_tools_private_endpoint_id=request.pop(util.camelize('databaseToolsPrivateEndpointId')),
                change_database_tools_private_endpoint_compartment_details=request.pop(util.camelize('ChangeDatabaseToolsPrivateEndpointCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'ChangeDatabaseToolsPrivateEndpointCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_database_tools_private_endpoint_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_create_database_tools_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'CreateDatabaseToolsConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'CreateDatabaseToolsConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='CreateDatabaseToolsConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.create_database_tools_connection(
                create_database_tools_connection_details=request.pop(util.camelize('CreateDatabaseToolsConnectionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'CreateDatabaseToolsConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseToolsConnection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_create_database_tools_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'CreateDatabaseToolsPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'CreateDatabaseToolsPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='CreateDatabaseToolsPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.create_database_tools_private_endpoint(
                create_database_tools_private_endpoint_details=request.pop(util.camelize('CreateDatabaseToolsPrivateEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'CreateDatabaseToolsPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseToolsPrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_delete_database_tools_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'DeleteDatabaseToolsConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'DeleteDatabaseToolsConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='DeleteDatabaseToolsConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.delete_database_tools_connection(
                database_tools_connection_id=request.pop(util.camelize('databaseToolsConnectionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'DeleteDatabaseToolsConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_database_tools_connection',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_delete_database_tools_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'DeleteDatabaseToolsPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'DeleteDatabaseToolsPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='DeleteDatabaseToolsPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.delete_database_tools_private_endpoint(
                database_tools_private_endpoint_id=request.pop(util.camelize('databaseToolsPrivateEndpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'DeleteDatabaseToolsPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_database_tools_private_endpoint',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_get_database_tools_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'GetDatabaseToolsConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'GetDatabaseToolsConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='GetDatabaseToolsConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.get_database_tools_connection(
                database_tools_connection_id=request.pop(util.camelize('databaseToolsConnectionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'GetDatabaseToolsConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseToolsConnection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_get_database_tools_endpoint_service(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'GetDatabaseToolsEndpointService'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'GetDatabaseToolsEndpointService')
    )

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='GetDatabaseToolsEndpointService')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.get_database_tools_endpoint_service(
                database_tools_endpoint_service_id=request.pop(util.camelize('databaseToolsEndpointServiceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'GetDatabaseToolsEndpointService',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseToolsEndpointService',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_get_database_tools_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'GetDatabaseToolsPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'GetDatabaseToolsPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='GetDatabaseToolsPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.get_database_tools_private_endpoint(
                database_tools_private_endpoint_id=request.pop(util.camelize('databaseToolsPrivateEndpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'GetDatabaseToolsPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseToolsPrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_list_database_tools_connections(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'ListDatabaseToolsConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'ListDatabaseToolsConnections')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='ListDatabaseToolsConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.list_database_tools_connections(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_database_tools_connections(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_database_tools_connections(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'ListDatabaseToolsConnections',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseToolsConnectionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_list_database_tools_endpoint_services(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'ListDatabaseToolsEndpointServices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'ListDatabaseToolsEndpointServices')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='ListDatabaseToolsEndpointServices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.list_database_tools_endpoint_services(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_database_tools_endpoint_services(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_database_tools_endpoint_services(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'ListDatabaseToolsEndpointServices',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseToolsEndpointServiceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_list_database_tools_private_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'ListDatabaseToolsPrivateEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'ListDatabaseToolsPrivateEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='ListDatabaseToolsPrivateEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.list_database_tools_private_endpoints(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_database_tools_private_endpoints(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_database_tools_private_endpoints(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'ListDatabaseToolsPrivateEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'databaseToolsPrivateEndpointCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
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
            'database_tools',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
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
            'database_tools',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
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
            'database_tools',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_update_database_tools_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'UpdateDatabaseToolsConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'UpdateDatabaseToolsConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='UpdateDatabaseToolsConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.update_database_tools_connection(
                database_tools_connection_id=request.pop(util.camelize('databaseToolsConnectionId')),
                update_database_tools_connection_details=request.pop(util.camelize('UpdateDatabaseToolsConnectionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'UpdateDatabaseToolsConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_database_tools_connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_update_database_tools_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'UpdateDatabaseToolsPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'UpdateDatabaseToolsPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='UpdateDatabaseToolsPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.update_database_tools_private_endpoint(
                database_tools_private_endpoint_id=request.pop(util.camelize('databaseToolsPrivateEndpointId')),
                update_database_tools_private_endpoint_details=request.pop(util.camelize('UpdateDatabaseToolsPrivateEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'UpdateDatabaseToolsPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_database_tools_private_endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dbtools_dev_ww_grp@oracle.com" jiraProject="DBTOOLS" opsJiraProject="DBTOOLS"
def test_validate_database_tools_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('database_tools', 'ValidateDatabaseToolsConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('database_tools', util.camelize('database_tools'), 'ValidateDatabaseToolsConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='database_tools', api_name='ValidateDatabaseToolsConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.database_tools.DatabaseToolsClient(config, service_endpoint=service_endpoint)
            response = client.validate_database_tools_connection(
                database_tools_connection_id=request.pop(util.camelize('databaseToolsConnectionId')),
                validate_database_tools_connection_details=request.pop(util.camelize('ValidateDatabaseToolsConnectionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'database_tools',
            'ValidateDatabaseToolsConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'validateDatabaseToolsConnectionResult',
            False,
            False
        )
