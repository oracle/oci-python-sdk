# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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
    # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
    # instead of 'query' matcher (which ignores sessionId in the url)
    # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
    custom_vcr = test_config_container.create_vcr()
    custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

    cassette_location = os.path.join('generated', 'limits_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


# IssueRoutingInfo tag="default" email="platform_limits_grp@oracle.com" jiraProject="LIM" opsJiraProject="LIM"
def test_get_resource_availability(testing_service_client):
    if not testing_service_client.is_api_enabled('limits', 'GetResourceAvailability'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('limits', util.camelize('limits'), 'GetResourceAvailability')
    )

    request_containers = testing_service_client.get_requests(service_name='limits', api_name='GetResourceAvailability')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.limits.LimitsClient(config, service_endpoint=service_endpoint)
            response = client.get_resource_availability(
                service_name=request.pop(util.camelize('service_name')),
                limit_name=request.pop(util.camelize('limit_name')),
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'limits',
            'GetResourceAvailability',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceAvailability',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="platform_limits_grp@oracle.com" jiraProject="LIM" opsJiraProject="LIM"
def test_list_limit_definitions(testing_service_client):
    if not testing_service_client.is_api_enabled('limits', 'ListLimitDefinitions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('limits', util.camelize('limits'), 'ListLimitDefinitions')
    )

    request_containers = testing_service_client.get_requests(service_name='limits', api_name='ListLimitDefinitions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.limits.LimitsClient(config, service_endpoint=service_endpoint)
            response = client.list_limit_definitions(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_limit_definitions(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_limit_definitions(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'limits',
            'ListLimitDefinitions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'limitDefinitionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="platform_limits_grp@oracle.com" jiraProject="LIM" opsJiraProject="LIM"
def test_list_limit_values(testing_service_client):
    if not testing_service_client.is_api_enabled('limits', 'ListLimitValues'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('limits', util.camelize('limits'), 'ListLimitValues')
    )

    request_containers = testing_service_client.get_requests(service_name='limits', api_name='ListLimitValues')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.limits.LimitsClient(config, service_endpoint=service_endpoint)
            response = client.list_limit_values(
                compartment_id=request.pop(util.camelize('compartment_id')),
                service_name=request.pop(util.camelize('service_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_limit_values(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    service_name=request.pop(util.camelize('service_name')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_limit_values(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        service_name=request.pop(util.camelize('service_name')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'limits',
            'ListLimitValues',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'limitValueSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="platform_limits_grp@oracle.com" jiraProject="LIM" opsJiraProject="LIM"
def test_list_services(testing_service_client):
    if not testing_service_client.is_api_enabled('limits', 'ListServices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('limits', util.camelize('limits'), 'ListServices')
    )

    request_containers = testing_service_client.get_requests(service_name='limits', api_name='ListServices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.limits.LimitsClient(config, service_endpoint=service_endpoint)
            response = client.list_services(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_services(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_services(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'limits',
            'ListServices',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceSummary',
            False,
            True
        )