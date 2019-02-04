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

    cassette_location = os.path.join('generated', 'resource_search_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


def test_get_resource_type(testing_service_client, config):
    if not testing_service_client.is_api_enabled('resource_search', 'GetResourceType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='resource_search', api_name='GetResourceType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.resource_search.ResourceSearchClient(config)
            response = client.get_resource_type(
                name=request.pop(util.camelize('name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_search',
            'GetResourceType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceType',
            False,
            False
        )


def test_list_resource_types(testing_service_client, config):
    if not testing_service_client.is_api_enabled('resource_search', 'ListResourceTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='resource_search', api_name='ListResourceTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.resource_search.ResourceSearchClient(config)
            response = client.list_resource_types(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_resource_types(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_resource_types(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_search',
            'ListResourceTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceType',
            False,
            True
        )


def test_search_resources(testing_service_client, config):
    if not testing_service_client.is_api_enabled('resource_search', 'SearchResources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='resource_search', api_name='SearchResources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.resource_search.ResourceSearchClient(config)
            response = client.search_resources(
                search_details=request.pop(util.camelize('search_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_resources(
                    search_details=request.pop(util.camelize('search_details')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_resources(
                        search_details=request.pop(util.camelize('search_details')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'resource_search',
            'SearchResources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resourceSummaryCollection',
            False,
            True
        )
