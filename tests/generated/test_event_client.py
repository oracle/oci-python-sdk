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

        cassette_location = os.path.join('generated', 'os_management_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_delete_event_content(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'DeleteEventContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('event'), 'DeleteEventContent')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='DeleteEventContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.EventClient(config, service_endpoint=service_endpoint)
            response = client.delete_event_content(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                event_id=request.pop(util.camelize('eventId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'DeleteEventContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_event_content',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_get_event(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'GetEvent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('event'), 'GetEvent')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='GetEvent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.EventClient(config, service_endpoint=service_endpoint)
            response = client.get_event(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                event_id=request.pop(util.camelize('eventId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'GetEvent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'event',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_get_event_content(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'GetEventContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('event'), 'GetEventContent')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='GetEventContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.EventClient(config, service_endpoint=service_endpoint)
            response = client.get_event_content(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                event_id=request.pop(util.camelize('eventId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'GetEventContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_get_event_report(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'GetEventReport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('event'), 'GetEventReport')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='GetEventReport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.EventClient(config, service_endpoint=service_endpoint)
            response = client.get_event_report(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'GetEventReport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'eventReport',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_events(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListEvents'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('event'), 'ListEvents')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListEvents')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.EventClient(config, service_endpoint=service_endpoint)
            response = client.list_events(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_events(
                    managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_events(
                        managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListEvents',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'eventCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_list_related_events(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'ListRelatedEvents'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('event'), 'ListRelatedEvents')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='ListRelatedEvents')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.EventClient(config, service_endpoint=service_endpoint)
            response = client.list_related_events(
                event_fingerprint=request.pop(util.camelize('eventFingerprint')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_related_events(
                    event_fingerprint=request.pop(util.camelize('eventFingerprint')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_related_events(
                        event_fingerprint=request.pop(util.camelize('eventFingerprint')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'ListRelatedEvents',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'relatedEventCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_update_event(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'UpdateEvent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('event'), 'UpdateEvent')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='UpdateEvent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.EventClient(config, service_endpoint=service_endpoint)
            response = client.update_event(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                event_id=request.pop(util.camelize('eventId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                update_event_details=request.pop(util.camelize('UpdateEventDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'UpdateEvent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'event',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_osms_us_grp@oracle.com" jiraProject="OSMS" opsJiraProject="OSMS"
def test_upload_event_content(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management', 'UploadEventContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management', util.camelize('event'), 'UploadEventContent')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management', api_name='UploadEventContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management.EventClient(config, service_endpoint=service_endpoint)
            response = client.upload_event_content(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                event_id=request.pop(util.camelize('eventId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management',
            'UploadEventContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'upload_event_content',
            False,
            False
        )