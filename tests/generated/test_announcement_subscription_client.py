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

        cassette_location = os.path.join('generated', 'announcements_service_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="announcement_service_engg_team_us_grp@oracle.com" jiraProject="AS" opsJiraProject="AS"
def test_change_announcement_subscription_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('announcements_service', 'ChangeAnnouncementSubscriptionCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('announcements_service', util.camelize('announcement_subscription'), 'ChangeAnnouncementSubscriptionCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='announcements_service', api_name='ChangeAnnouncementSubscriptionCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.announcements_service.AnnouncementSubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.change_announcement_subscription_compartment(
                announcement_subscription_id=request.pop(util.camelize('announcementSubscriptionId')),
                change_announcement_subscription_compartment_details=request.pop(util.camelize('ChangeAnnouncementSubscriptionCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'announcements_service',
            'ChangeAnnouncementSubscriptionCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_announcement_subscription_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="announcement_service_engg_team_us_grp@oracle.com" jiraProject="AS" opsJiraProject="AS"
def test_create_announcement_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('announcements_service', 'CreateAnnouncementSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('announcements_service', util.camelize('announcement_subscription'), 'CreateAnnouncementSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='announcements_service', api_name='CreateAnnouncementSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.announcements_service.AnnouncementSubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.create_announcement_subscription(
                create_announcement_subscription_details=request.pop(util.camelize('CreateAnnouncementSubscriptionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'announcements_service',
            'CreateAnnouncementSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'announcementSubscription',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="announcement_service_engg_team_us_grp@oracle.com" jiraProject="AS" opsJiraProject="AS"
def test_create_filter_group(testing_service_client):
    if not testing_service_client.is_api_enabled('announcements_service', 'CreateFilterGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('announcements_service', util.camelize('announcement_subscription'), 'CreateFilterGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='announcements_service', api_name='CreateFilterGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.announcements_service.AnnouncementSubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.create_filter_group(
                announcement_subscription_id=request.pop(util.camelize('announcementSubscriptionId')),
                create_filter_group_details=request.pop(util.camelize('CreateFilterGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'announcements_service',
            'CreateFilterGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'filterGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="announcement_service_engg_team_us_grp@oracle.com" jiraProject="AS" opsJiraProject="AS"
def test_delete_announcement_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('announcements_service', 'DeleteAnnouncementSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('announcements_service', util.camelize('announcement_subscription'), 'DeleteAnnouncementSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='announcements_service', api_name='DeleteAnnouncementSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.announcements_service.AnnouncementSubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.delete_announcement_subscription(
                announcement_subscription_id=request.pop(util.camelize('announcementSubscriptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'announcements_service',
            'DeleteAnnouncementSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_announcement_subscription',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="announcement_service_engg_team_us_grp@oracle.com" jiraProject="AS" opsJiraProject="AS"
def test_delete_filter_group(testing_service_client):
    if not testing_service_client.is_api_enabled('announcements_service', 'DeleteFilterGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('announcements_service', util.camelize('announcement_subscription'), 'DeleteFilterGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='announcements_service', api_name='DeleteFilterGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.announcements_service.AnnouncementSubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.delete_filter_group(
                announcement_subscription_id=request.pop(util.camelize('announcementSubscriptionId')),
                filter_group_name=request.pop(util.camelize('filterGroupName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'announcements_service',
            'DeleteFilterGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_filter_group',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="announcement_service_engg_team_us_grp@oracle.com" jiraProject="AS" opsJiraProject="AS"
def test_get_announcement_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('announcements_service', 'GetAnnouncementSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('announcements_service', util.camelize('announcement_subscription'), 'GetAnnouncementSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='announcements_service', api_name='GetAnnouncementSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.announcements_service.AnnouncementSubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.get_announcement_subscription(
                announcement_subscription_id=request.pop(util.camelize('announcementSubscriptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'announcements_service',
            'GetAnnouncementSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'announcementSubscription',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="announcement_service_engg_team_us_grp@oracle.com" jiraProject="AS" opsJiraProject="AS"
def test_list_announcement_subscriptions(testing_service_client):
    if not testing_service_client.is_api_enabled('announcements_service', 'ListAnnouncementSubscriptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('announcements_service', util.camelize('announcement_subscription'), 'ListAnnouncementSubscriptions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='announcements_service', api_name='ListAnnouncementSubscriptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.announcements_service.AnnouncementSubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.list_announcement_subscriptions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_announcement_subscriptions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_announcement_subscriptions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'announcements_service',
            'ListAnnouncementSubscriptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'announcementSubscriptionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="announcement_service_engg_team_us_grp@oracle.com" jiraProject="AS" opsJiraProject="AS"
def test_update_announcement_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('announcements_service', 'UpdateAnnouncementSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('announcements_service', util.camelize('announcement_subscription'), 'UpdateAnnouncementSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='announcements_service', api_name='UpdateAnnouncementSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.announcements_service.AnnouncementSubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.update_announcement_subscription(
                announcement_subscription_id=request.pop(util.camelize('announcementSubscriptionId')),
                update_announcement_subscription_details=request.pop(util.camelize('UpdateAnnouncementSubscriptionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'announcements_service',
            'UpdateAnnouncementSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'announcementSubscription',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="announcement_service_engg_team_us_grp@oracle.com" jiraProject="AS" opsJiraProject="AS"
def test_update_filter_group(testing_service_client):
    if not testing_service_client.is_api_enabled('announcements_service', 'UpdateFilterGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('announcements_service', util.camelize('announcement_subscription'), 'UpdateFilterGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='announcements_service', api_name='UpdateFilterGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.announcements_service.AnnouncementSubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.update_filter_group(
                announcement_subscription_id=request.pop(util.camelize('announcementSubscriptionId')),
                filter_group_name=request.pop(util.camelize('filterGroupName')),
                update_filter_group_details=request.pop(util.camelize('UpdateFilterGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'announcements_service',
            'UpdateFilterGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'filterGroup',
            False,
            False
        )
