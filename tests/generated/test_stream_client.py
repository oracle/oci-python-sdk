# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'streaming_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_consumer_commit(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'ConsumerCommit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream'), 'ConsumerCommit')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='ConsumerCommit')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("streaming", "StreamClient", "ConsumerCommit")
            client = oci.streaming.StreamClient(config, service_endpoint=service_endpoint)
            response = client.consumer_commit(
                stream_id=request.pop(util.camelize('streamId')),
                cursor=request.pop(util.camelize('cursor')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'ConsumerCommit',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cursor',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_consumer_heartbeat(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'ConsumerHeartbeat'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream'), 'ConsumerHeartbeat')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='ConsumerHeartbeat')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("streaming", "StreamClient", "ConsumerHeartbeat")
            client = oci.streaming.StreamClient(config, service_endpoint=service_endpoint)
            response = client.consumer_heartbeat(
                stream_id=request.pop(util.camelize('streamId')),
                cursor=request.pop(util.camelize('cursor')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'ConsumerHeartbeat',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cursor',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_create_cursor(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'CreateCursor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream'), 'CreateCursor')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='CreateCursor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("streaming", "StreamClient", "CreateCursor")
            client = oci.streaming.StreamClient(config, service_endpoint=service_endpoint)
            response = client.create_cursor(
                stream_id=request.pop(util.camelize('streamId')),
                create_cursor_details=request.pop(util.camelize('CreateCursorDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'CreateCursor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cursor',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_create_group_cursor(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'CreateGroupCursor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream'), 'CreateGroupCursor')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='CreateGroupCursor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("streaming", "StreamClient", "CreateGroupCursor")
            client = oci.streaming.StreamClient(config, service_endpoint=service_endpoint)
            response = client.create_group_cursor(
                stream_id=request.pop(util.camelize('streamId')),
                create_group_cursor_details=request.pop(util.camelize('CreateGroupCursorDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'CreateGroupCursor',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cursor',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_get_group(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'GetGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream'), 'GetGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='GetGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("streaming", "StreamClient", "GetGroup")
            client = oci.streaming.StreamClient(config, service_endpoint=service_endpoint)
            response = client.get_group(
                stream_id=request.pop(util.camelize('streamId')),
                group_name=request.pop(util.camelize('groupName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'GetGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_get_messages(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'GetMessages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream'), 'GetMessages')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='GetMessages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("streaming", "StreamClient", "GetMessages")
            client = oci.streaming.StreamClient(config, service_endpoint=service_endpoint)
            response = client.get_messages(
                stream_id=request.pop(util.camelize('streamId')),
                cursor=request.pop(util.camelize('cursor')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'GetMessages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'message',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_put_messages(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'PutMessages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream'), 'PutMessages')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='PutMessages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("streaming", "StreamClient", "PutMessages")
            client = oci.streaming.StreamClient(config, service_endpoint=service_endpoint)
            response = client.put_messages(
                stream_id=request.pop(util.camelize('streamId')),
                put_messages_details=request.pop(util.camelize('PutMessagesDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'PutMessages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'putMessagesResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_streaming_us_grp@oracle.com" jiraProject="STREAMSTR" opsJiraProject="STREAMOSS"
def test_update_group(testing_service_client):
    if not testing_service_client.is_api_enabled('streaming', 'UpdateGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('streaming', util.camelize('stream'), 'UpdateGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='UpdateGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = testing_service_client.get_endpoint("streaming", "StreamClient", "UpdateGroup")
            client = oci.streaming.StreamClient(config, service_endpoint=service_endpoint)
            response = client.update_group(
                stream_id=request.pop(util.camelize('streamId')),
                group_name=request.pop(util.camelize('groupName')),
                update_group_details=request.pop(util.camelize('UpdateGroupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'streaming',
            'UpdateGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_group',
            False,
            False
        )
