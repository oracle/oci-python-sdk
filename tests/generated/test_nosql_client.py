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

        cassette_location = os.path.join('generated', 'nosql_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_change_table_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'ChangeTableCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'ChangeTableCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='ChangeTableCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.change_table_compartment(
                table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                change_table_compartment_details=request.pop(util.camelize('ChangeTableCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'ChangeTableCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_table_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_create_index(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'CreateIndex'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'CreateIndex')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='CreateIndex')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.create_index(
                table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                create_index_details=request.pop(util.camelize('CreateIndexDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'CreateIndex',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_index',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_create_table(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'CreateTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'CreateTable')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='CreateTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.create_table(
                create_table_details=request.pop(util.camelize('CreateTableDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'CreateTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_table',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_delete_index(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'DeleteIndex'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'DeleteIndex')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='DeleteIndex')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.delete_index(
                table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                index_name=request.pop(util.camelize('indexName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'DeleteIndex',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_index',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_delete_row(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'DeleteRow'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'DeleteRow')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='DeleteRow')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.delete_row(
                table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                key=request.pop(util.camelize('key')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'DeleteRow',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deleteRowResult',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_delete_table(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'DeleteTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'DeleteTable')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='DeleteTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.delete_table(
                table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'DeleteTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_table',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_delete_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'DeleteWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'DeleteWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='DeleteWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.delete_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'DeleteWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_get_index(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'GetIndex'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'GetIndex')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='GetIndex')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.get_index(
                table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                index_name=request.pop(util.camelize('indexName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'GetIndex',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'index',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_get_row(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'GetRow'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'GetRow')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='GetRow')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.get_row(
                table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                key=request.pop(util.camelize('key')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'GetRow',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'row',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_get_table(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'GetTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'GetTable')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='GetTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.get_table(
                table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'GetTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'table',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_list_indexes(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'ListIndexes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'ListIndexes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='ListIndexes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.list_indexes(
                table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_indexes(
                    table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_indexes(
                        table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'ListIndexes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'indexCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_list_table_usage(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'ListTableUsage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'ListTableUsage')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='ListTableUsage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.list_table_usage(
                table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_table_usage(
                    table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_table_usage(
                        table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'ListTableUsage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tableUsageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_list_tables(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'ListTables'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'ListTables')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='ListTables')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.list_tables(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tables(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tables(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'ListTables',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'tableCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
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
            'nosql',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
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
            'nosql',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
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
            'nosql',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_prepare_statement(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'PrepareStatement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'PrepareStatement')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='PrepareStatement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.prepare_statement(
                compartment_id=request.pop(util.camelize('compartmentId')),
                statement=request.pop(util.camelize('statement')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'PrepareStatement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'preparedStatement',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_query(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'Query'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'Query')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='Query')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.query(
                query_details=request.pop(util.camelize('QueryDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.query(
                    query_details=request.pop(util.camelize('QueryDetails')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.query(
                        query_details=request.pop(util.camelize('QueryDetails')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'Query',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'queryResultCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_summarize_statement(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'SummarizeStatement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'SummarizeStatement')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='SummarizeStatement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.summarize_statement(
                compartment_id=request.pop(util.camelize('compartmentId')),
                statement=request.pop(util.camelize('statement')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'SummarizeStatement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'statementSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_update_row(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'UpdateRow'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'UpdateRow')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='UpdateRow')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.update_row(
                table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                update_row_details=request.pop(util.camelize('UpdateRowDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'UpdateRow',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'updateRowResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="andc_ops_ww_grp@oracle.com" jiraProject="NOSQL" opsJiraProject="NOSQL"
def test_update_table(testing_service_client):
    if not testing_service_client.is_api_enabled('nosql', 'UpdateTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('nosql', util.camelize('nosql'), 'UpdateTable')
    )

    request_containers = testing_service_client.get_requests(service_name='nosql', api_name='UpdateTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.nosql.NosqlClient(config, service_endpoint=service_endpoint)
            response = client.update_table(
                table_name_or_id=request.pop(util.camelize('tableNameOrId')),
                update_table_details=request.pop(util.camelize('UpdateTableDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'nosql',
            'UpdateTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_table',
            False,
            False
        )
