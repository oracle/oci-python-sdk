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

    cassette_location = os.path.join('generated', 'streaming_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


# IssueRoutingInfo tag="" email="" jiraProject="" opsJiraProject=""
def test_create_stream(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'CreateStream'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'CreateStream')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='CreateStream')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.streaming.StreamAdminClient(config)
            response = client.create_stream(
                create_stream_details=request.pop(util.camelize('create_stream_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'CreateStream',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="" email="" jiraProject="" opsJiraProject=""
def test_delete_stream(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'DeleteStream'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'DeleteStream')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='DeleteStream')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.streaming.StreamAdminClient(config)
            response = client.delete_stream(
                stream_id=request.pop(util.camelize('stream_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'DeleteStream',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_stream',
            True,
            False
        )


# IssueRoutingInfo tag="" email="" jiraProject="" opsJiraProject=""
def test_get_stream(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'GetStream'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'GetStream')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='GetStream')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.streaming.StreamAdminClient(config)
            response = client.get_stream(
                stream_id=request.pop(util.camelize('stream_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'GetStream',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="" email="" jiraProject="" opsJiraProject=""
def test_list_streams(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'ListStreams'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'ListStreams')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='ListStreams')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.streaming.StreamAdminClient(config)
            response = client.list_streams(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_streams(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_streams(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'ListStreams',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'streamSummary',
            False,
            True
        )


# IssueRoutingInfo tag="" email="" jiraProject="" opsJiraProject=""
def test_update_stream(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'UpdateStream'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream_admin'), 'UpdateStream')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='UpdateStream')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.streaming.StreamAdminClient(config)
            response = client.update_stream(
                stream_id=request.pop(util.camelize('stream_id')),
                update_stream_details=request.pop(util.camelize('update_stream_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'UpdateStream',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )
