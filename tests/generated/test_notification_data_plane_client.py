# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

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
def test_change_subscription_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'ChangeSubscriptionCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_data_plane'), 'ChangeSubscriptionCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='ChangeSubscriptionCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationDataPlaneClient(config, service_endpoint=service_endpoint)
            response = client.change_subscription_compartment(
                subscription_id=request.pop(util.camelize('subscriptionId')),
                change_subscription_compartment_details=request.pop(util.camelize('ChangeSubscriptionCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'ChangeSubscriptionCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_subscription_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_create_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'CreateSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_data_plane'), 'CreateSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='CreateSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationDataPlaneClient(config, service_endpoint=service_endpoint)
            response = client.create_subscription(
                create_subscription_details=request.pop(util.camelize('CreateSubscriptionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'CreateSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscription',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_delete_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'DeleteSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_data_plane'), 'DeleteSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='DeleteSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationDataPlaneClient(config, service_endpoint=service_endpoint)
            response = client.delete_subscription(
                subscription_id=request.pop(util.camelize('subscriptionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'DeleteSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_subscription',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_get_confirm_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'GetConfirmSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_data_plane'), 'GetConfirmSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='GetConfirmSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationDataPlaneClient(config, service_endpoint=service_endpoint)
            response = client.get_confirm_subscription(
                id=request.pop(util.camelize('id')),
                token=request.pop(util.camelize('token')),
                protocol=request.pop(util.camelize('protocol')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'GetConfirmSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'confirmationResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_get_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'GetSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_data_plane'), 'GetSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='GetSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationDataPlaneClient(config, service_endpoint=service_endpoint)
            response = client.get_subscription(
                subscription_id=request.pop(util.camelize('subscriptionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'GetSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscription',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_get_unsubscription(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'GetUnsubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_data_plane'), 'GetUnsubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='GetUnsubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationDataPlaneClient(config, service_endpoint=service_endpoint)
            response = client.get_unsubscription(
                id=request.pop(util.camelize('id')),
                token=request.pop(util.camelize('token')),
                protocol=request.pop(util.camelize('protocol')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'GetUnsubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'str',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_list_subscriptions(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'ListSubscriptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_data_plane'), 'ListSubscriptions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='ListSubscriptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationDataPlaneClient(config, service_endpoint=service_endpoint)
            response = client.list_subscriptions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_subscriptions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_subscriptions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'ListSubscriptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscriptionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_publish_message(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'PublishMessage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_data_plane'), 'PublishMessage')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='PublishMessage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationDataPlaneClient(config, service_endpoint=service_endpoint)
            response = client.publish_message(
                topic_id=request.pop(util.camelize('topicId')),
                message_details=request.pop(util.camelize('MessageDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'PublishMessage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publishResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_resend_subscription_confirmation(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'ResendSubscriptionConfirmation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_data_plane'), 'ResendSubscriptionConfirmation')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='ResendSubscriptionConfirmation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationDataPlaneClient(config, service_endpoint=service_endpoint)
            response = client.resend_subscription_confirmation(
                id=request.pop(util.camelize('id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'ResendSubscriptionConfirmation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscription',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="team_oci_ons_us_grp@oracle.com" jiraProject="ONS" opsJiraProject="ONS"
def test_update_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('ons', 'UpdateSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ons', util.camelize('notification_data_plane'), 'UpdateSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='ons', api_name='UpdateSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ons.NotificationDataPlaneClient(config, service_endpoint=service_endpoint)
            response = client.update_subscription(
                subscription_id=request.pop(util.camelize('subscriptionId')),
                update_subscription_details=request.pop(util.camelize('UpdateSubscriptionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ons',
            'UpdateSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'updateSubscriptionDetails',
            False,
            False
        )
