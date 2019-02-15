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


def test_consumer_commit(testing_service_client, config):
    if not testing_service_client.is_api_enabled('streaming', 'ConsumerCommit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='ConsumerCommit')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.streaming.StreamClient(config)
            response = client.consumer_commit(
                stream_id=request.pop(util.camelize('stream_id')),
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


def test_consumer_heartbeat(testing_service_client, config):
    if not testing_service_client.is_api_enabled('streaming', 'ConsumerHeartbeat'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='ConsumerHeartbeat')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.streaming.StreamClient(config)
            response = client.consumer_heartbeat(
                stream_id=request.pop(util.camelize('stream_id')),
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


def test_create_cursor(testing_service_client, config):
    if not testing_service_client.is_api_enabled('streaming', 'CreateCursor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='CreateCursor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.streaming.StreamClient(config)
            response = client.create_cursor(
                stream_id=request.pop(util.camelize('stream_id')),
                create_cursor_details=request.pop(util.camelize('create_cursor_details')),
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


def test_create_group_cursor(testing_service_client, config):
    if not testing_service_client.is_api_enabled('streaming', 'CreateGroupCursor'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='CreateGroupCursor')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.streaming.StreamClient(config)
            response = client.create_group_cursor(
                stream_id=request.pop(util.camelize('stream_id')),
                create_group_cursor_details=request.pop(util.camelize('create_group_cursor_details')),
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


def test_get_group(testing_service_client, config):
    if not testing_service_client.is_api_enabled('streaming', 'GetGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='GetGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.streaming.StreamClient(config)
            response = client.get_group(
                stream_id=request.pop(util.camelize('stream_id')),
                group_name=request.pop(util.camelize('group_name')),
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


def test_get_messages(testing_service_client, config):
    if not testing_service_client.is_api_enabled('streaming', 'GetMessages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='GetMessages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.streaming.StreamClient(config)
            response = client.get_messages(
                stream_id=request.pop(util.camelize('stream_id')),
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


def test_put_messages(testing_service_client, config):
    if not testing_service_client.is_api_enabled('streaming', 'PutMessages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='PutMessages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.streaming.StreamClient(config)
            response = client.put_messages(
                stream_id=request.pop(util.camelize('stream_id')),
                put_messages_details=request.pop(util.camelize('put_messages_details')),
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


def test_update_group(testing_service_client, config):
    if not testing_service_client.is_api_enabled('streaming', 'UpdateGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    request_containers = testing_service_client.get_requests(service_name='streaming', api_name='UpdateGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
            if pass_phrase:
                config['pass_phrase'] = pass_phrase
            client = oci.streaming.StreamClient(config)
            response = client.update_group(
                stream_id=request.pop(util.camelize('stream_id')),
                group_name=request.pop(util.camelize('group_name')),
                update_group_details=request.pop(util.camelize('update_group_details')),
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
