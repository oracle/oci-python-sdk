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
def test_change_queue_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'ChangeQueueCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue_admin'), 'ChangeQueueCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='ChangeQueueCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueAdminClient(config, service_endpoint=service_endpoint)
            response = client.change_queue_compartment(
                queue_id=request.pop(util.camelize('queueId')),
                change_queue_compartment_details=request.pop(util.camelize('ChangeQueueCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'ChangeQueueCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_queue_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_create_queue(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'CreateQueue'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue_admin'), 'CreateQueue')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='CreateQueue')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueAdminClient(config, service_endpoint=service_endpoint)
            response = client.create_queue(
                create_queue_details=request.pop(util.camelize('CreateQueueDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'CreateQueue',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_queue',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_delete_queue(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'DeleteQueue'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue_admin'), 'DeleteQueue')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='DeleteQueue')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueAdminClient(config, service_endpoint=service_endpoint)
            response = client.delete_queue(
                queue_id=request.pop(util.camelize('queueId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'DeleteQueue',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_queue',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_get_queue(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'GetQueue'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue_admin'), 'GetQueue')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='GetQueue')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueAdminClient(config, service_endpoint=service_endpoint)
            response = client.get_queue(
                queue_id=request.pop(util.camelize('queueId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'GetQueue',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'queue',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue_admin'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueAdminClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_list_queues(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'ListQueues'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue_admin'), 'ListQueues')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='ListQueues')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueAdminClient(config, service_endpoint=service_endpoint)
            response = client.list_queues(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_queues(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_queues(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'ListQueues',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'queueCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue_admin'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueAdminClient(config, service_endpoint=service_endpoint)
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
            'queue',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue_admin'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueAdminClient(config, service_endpoint=service_endpoint)
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
            'queue',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue_admin'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueAdminClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_purge_queue(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'PurgeQueue'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue_admin'), 'PurgeQueue')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='PurgeQueue')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueAdminClient(config, service_endpoint=service_endpoint)
            response = client.purge_queue(
                queue_id=request.pop(util.camelize('queueId')),
                purge_queue_details=request.pop(util.camelize('PurgeQueueDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'PurgeQueue',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'purge_queue',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="queue_us_grp@oracle.com" jiraProject="QS" opsJiraProject="QUEUE"
def test_update_queue(testing_service_client):
    if not testing_service_client.is_api_enabled('queue', 'UpdateQueue'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('queue', util.camelize('queue_admin'), 'UpdateQueue')
    )

    request_containers = testing_service_client.get_requests(service_name='queue', api_name='UpdateQueue')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.queue.QueueAdminClient(config, service_endpoint=service_endpoint)
            response = client.update_queue(
                queue_id=request.pop(util.camelize('queueId')),
                update_queue_details=request.pop(util.camelize('UpdateQueueDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'queue',
            'UpdateQueue',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_queue',
            False,
            False
        )
