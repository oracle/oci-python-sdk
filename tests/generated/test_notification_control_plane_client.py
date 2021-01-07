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

        cassette_location = os.path.join('generated', 'ons_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_change_topic_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'ChangeTopicCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_control_plane'), 'ChangeTopicCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='ChangeTopicCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationControlPlaneClient(config, service_endpoint=service_endpoint)
            response = client.change_topic_compartment(
                topic_id=request.pop(util.camelize('topicId')),
                change_topic_compartment_details=request.pop(util.camelize('ChangeTopicCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'ChangeTopicCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_topic_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_create_topic(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'CreateTopic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_control_plane'), 'CreateTopic')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='CreateTopic')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationControlPlaneClient(config, service_endpoint=service_endpoint)
            response = client.create_topic(
                create_topic_details=request.pop(util.camelize('CreateTopicDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'CreateTopic',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'notificationTopic',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_delete_topic(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'DeleteTopic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_control_plane'), 'DeleteTopic')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='DeleteTopic')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationControlPlaneClient(config, service_endpoint=service_endpoint)
            response = client.delete_topic(
                topic_id=request.pop(util.camelize('topicId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'DeleteTopic',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_topic',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_get_topic(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'GetTopic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_control_plane'), 'GetTopic')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='GetTopic')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationControlPlaneClient(config, service_endpoint=service_endpoint)
            response = client.get_topic(
                topic_id=request.pop(util.camelize('topicId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'GetTopic',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'notificationTopic',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_list_topics(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'ListTopics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_control_plane'), 'ListTopics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='ListTopics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationControlPlaneClient(config, service_endpoint=service_endpoint)
            response = client.list_topics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_topics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_topics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'ListTopics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'notificationTopicSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_update_topic(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'UpdateTopic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_control_plane'), 'UpdateTopic')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='UpdateTopic')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationControlPlaneClient(config, service_endpoint=service_endpoint)
            response = client.update_topic(
                topic_id=request.pop(util.camelize('topicId')),
                topic_attributes_details=request.pop(util.camelize('TopicAttributesDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'UpdateTopic',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'notificationTopic',
            False,
            False
        )
