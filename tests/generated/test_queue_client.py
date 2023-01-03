# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'queue_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_delete_message(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'DeleteMessage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue'), 'DeleteMessage')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='DeleteMessage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueClient(config, service_endpoint=service_endpoint)
            response = client.delete_message(
                queue_id=request.pop(util.camelize('queueId')),
                message_receipt=request.pop(util.camelize('messageReceipt')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'DeleteMessage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_message',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_delete_messages(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'DeleteMessages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue'), 'DeleteMessages')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='DeleteMessages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueClient(config, service_endpoint=service_endpoint)
            response = client.delete_messages(
                queue_id=request.pop(util.camelize('queueId')),
                delete_messages_details=request.pop(util.camelize('DeleteMessagesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'DeleteMessages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deleteMessagesResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_get_messages(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'GetMessages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue'), 'GetMessages')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='GetMessages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueClient(config, service_endpoint=service_endpoint)
            response = client.get_messages(
                queue_id=request.pop(util.camelize('queueId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'GetMessages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'getMessages',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_get_stats(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'GetStats'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue'), 'GetStats')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='GetStats')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueClient(config, service_endpoint=service_endpoint)
            response = client.get_stats(
                queue_id=request.pop(util.camelize('queueId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'GetStats',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'queueStats',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_put_messages(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'PutMessages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue'), 'PutMessages')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='PutMessages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueClient(config, service_endpoint=service_endpoint)
            response = client.put_messages(
                queue_id=request.pop(util.camelize('queueId')),
                put_messages_details=request.pop(util.camelize('PutMessagesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'PutMessages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'putMessages',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_update_message(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'UpdateMessage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue'), 'UpdateMessage')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='UpdateMessage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueClient(config, service_endpoint=service_endpoint)
            response = client.update_message(
                queue_id=request.pop(util.camelize('queueId')),
                message_receipt=request.pop(util.camelize('messageReceipt')),
                update_message_details=request.pop(util.camelize('UpdateMessageDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'UpdateMessage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'updatedMessage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_update_messages(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'UpdateMessages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue'), 'UpdateMessages')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='UpdateMessages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueClient(config, service_endpoint=service_endpoint)
            response = client.update_messages(
                queue_id=request.pop(util.camelize('queueId')),
                update_messages_details=request.pop(util.camelize('UpdateMessagesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'UpdateMessages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'updateMessagesResult',
            False,
            False
        )
