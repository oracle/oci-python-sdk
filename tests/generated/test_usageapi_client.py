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

        cassette_location = os.path.join('generated', 'usage_api_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_create_custom_table(testing_service_client):
    if not testing_service_client.is_api_enabled('usage_api', 'CreateCustomTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage_api', util.camelize('usageapi'), 'CreateCustomTable')
    )

    request_containers = testing_service_client.get_requests(service_name='usage_api', api_name='CreateCustomTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage_api.UsageapiClient(config, service_endpoint=service_endpoint)
            response = client.create_custom_table(
                create_custom_table_details=request.pop(util.camelize('CreateCustomTableDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage_api',
            'CreateCustomTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customTable',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_create_query(testing_service_client):
    if not testing_service_client.is_api_enabled('usage_api', 'CreateQuery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage_api', util.camelize('usageapi'), 'CreateQuery')
    )

    request_containers = testing_service_client.get_requests(service_name='usage_api', api_name='CreateQuery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage_api.UsageapiClient(config, service_endpoint=service_endpoint)
            response = client.create_query(
                create_query_details=request.pop(util.camelize('CreateQueryDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage_api',
            'CreateQuery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'query',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_delete_custom_table(testing_service_client):
    if not testing_service_client.is_api_enabled('usage_api', 'DeleteCustomTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage_api', util.camelize('usageapi'), 'DeleteCustomTable')
    )

    request_containers = testing_service_client.get_requests(service_name='usage_api', api_name='DeleteCustomTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage_api.UsageapiClient(config, service_endpoint=service_endpoint)
            response = client.delete_custom_table(
                custom_table_id=request.pop(util.camelize('customTableId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage_api',
            'DeleteCustomTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_custom_table',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_delete_query(testing_service_client):
    if not testing_service_client.is_api_enabled('usage_api', 'DeleteQuery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage_api', util.camelize('usageapi'), 'DeleteQuery')
    )

    request_containers = testing_service_client.get_requests(service_name='usage_api', api_name='DeleteQuery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage_api.UsageapiClient(config, service_endpoint=service_endpoint)
            response = client.delete_query(
                query_id=request.pop(util.camelize('queryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage_api',
            'DeleteQuery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_query',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_get_custom_table(testing_service_client):
    if not testing_service_client.is_api_enabled('usage_api', 'GetCustomTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage_api', util.camelize('usageapi'), 'GetCustomTable')
    )

    request_containers = testing_service_client.get_requests(service_name='usage_api', api_name='GetCustomTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage_api.UsageapiClient(config, service_endpoint=service_endpoint)
            response = client.get_custom_table(
                custom_table_id=request.pop(util.camelize('customTableId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage_api',
            'GetCustomTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customTable',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_get_query(testing_service_client):
    if not testing_service_client.is_api_enabled('usage_api', 'GetQuery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage_api', util.camelize('usageapi'), 'GetQuery')
    )

    request_containers = testing_service_client.get_requests(service_name='usage_api', api_name='GetQuery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage_api.UsageapiClient(config, service_endpoint=service_endpoint)
            response = client.get_query(
                query_id=request.pop(util.camelize('queryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage_api',
            'GetQuery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'query',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_list_custom_tables(testing_service_client):
    if not testing_service_client.is_api_enabled('usage_api', 'ListCustomTables'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage_api', util.camelize('usageapi'), 'ListCustomTables')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='usage_api', api_name='ListCustomTables')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage_api.UsageapiClient(config, service_endpoint=service_endpoint)
            response = client.list_custom_tables(
                compartment_id=request.pop(util.camelize('compartmentId')),
                saved_report_id=request.pop(util.camelize('savedReportId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_custom_tables(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    saved_report_id=request.pop(util.camelize('savedReportId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_custom_tables(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        saved_report_id=request.pop(util.camelize('savedReportId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage_api',
            'ListCustomTables',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customTableCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_list_queries(testing_service_client):
    if not testing_service_client.is_api_enabled('usage_api', 'ListQueries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage_api', util.camelize('usageapi'), 'ListQueries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='usage_api', api_name='ListQueries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage_api.UsageapiClient(config, service_endpoint=service_endpoint)
            response = client.list_queries(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_queries(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_queries(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage_api',
            'ListQueries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'queryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_request_summarized_configurations(testing_service_client):
    if not testing_service_client.is_api_enabled('usage_api', 'RequestSummarizedConfigurations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage_api', util.camelize('usageapi'), 'RequestSummarizedConfigurations')
    )

    request_containers = testing_service_client.get_requests(service_name='usage_api', api_name='RequestSummarizedConfigurations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage_api.UsageapiClient(config, service_endpoint=service_endpoint)
            response = client.request_summarized_configurations(
                tenant_id=request.pop(util.camelize('tenantId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage_api',
            'RequestSummarizedConfigurations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'configurationAggregation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_request_summarized_usages(testing_service_client):
    if not testing_service_client.is_api_enabled('usage_api', 'RequestSummarizedUsages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage_api', util.camelize('usageapi'), 'RequestSummarizedUsages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='usage_api', api_name='RequestSummarizedUsages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage_api.UsageapiClient(config, service_endpoint=service_endpoint)
            response = client.request_summarized_usages(
                request_summarized_usages_details=request.pop(util.camelize('RequestSummarizedUsagesDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.request_summarized_usages(
                    request_summarized_usages_details=request.pop(util.camelize('RequestSummarizedUsagesDetails')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.request_summarized_usages(
                        request_summarized_usages_details=request.pop(util.camelize('RequestSummarizedUsagesDetails')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage_api',
            'RequestSummarizedUsages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'usageAggregation',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_update_custom_table(testing_service_client):
    if not testing_service_client.is_api_enabled('usage_api', 'UpdateCustomTable'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage_api', util.camelize('usageapi'), 'UpdateCustomTable')
    )

    request_containers = testing_service_client.get_requests(service_name='usage_api', api_name='UpdateCustomTable')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage_api.UsageapiClient(config, service_endpoint=service_endpoint)
            response = client.update_custom_table(
                update_custom_table_details=request.pop(util.camelize('UpdateCustomTableDetails')),
                custom_table_id=request.pop(util.camelize('customTableId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage_api',
            'UpdateCustomTable',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'customTable',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_update_query(testing_service_client):
    if not testing_service_client.is_api_enabled('usage_api', 'UpdateQuery'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage_api', util.camelize('usageapi'), 'UpdateQuery')
    )

    request_containers = testing_service_client.get_requests(service_name='usage_api', api_name='UpdateQuery')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage_api.UsageapiClient(config, service_endpoint=service_endpoint)
            response = client.update_query(
                update_query_details=request.pop(util.camelize('UpdateQueryDetails')),
                query_id=request.pop(util.camelize('queryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage_api',
            'UpdateQuery',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'query',
            False,
            False
        )
