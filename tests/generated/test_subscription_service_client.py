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

        cassette_location = os.path.join('generated', 'osp_gateway_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="osp_team_oci_cam_ww_grp@oracle.com" jiraProject="OSP" opsJiraProject="OSP"
def test_authorize_subscription_payment(testing_service_client):
    if not testing_service_client.is_api_enabled('osp_gateway', 'AuthorizeSubscriptionPayment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('osp_gateway', util.camelize('subscription_service'), 'AuthorizeSubscriptionPayment')
    )

    request_containers = testing_service_client.get_requests(service_name='osp_gateway', api_name='AuthorizeSubscriptionPayment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.osp_gateway.SubscriptionServiceClient(config, service_endpoint=service_endpoint)
            response = client.authorize_subscription_payment(
                osp_home_region=request.pop(util.camelize('ospHomeRegion')),
                subscription_id=request.pop(util.camelize('subscriptionId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                authorize_subscription_payment_details=request.pop(util.camelize('AuthorizeSubscriptionPaymentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'osp_gateway',
            'AuthorizeSubscriptionPayment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'authorizeSubscriptionPaymentReceipt',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osp_team_oci_cam_ww_grp@oracle.com" jiraProject="OSP" opsJiraProject="OSP"
def test_get_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('osp_gateway', 'GetSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('osp_gateway', util.camelize('subscription_service'), 'GetSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='osp_gateway', api_name='GetSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.osp_gateway.SubscriptionServiceClient(config, service_endpoint=service_endpoint)
            response = client.get_subscription(
                subscription_id=request.pop(util.camelize('subscriptionId')),
                osp_home_region=request.pop(util.camelize('ospHomeRegion')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'osp_gateway',
            'GetSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscription',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osp_team_oci_cam_ww_grp@oracle.com" jiraProject="OSP" opsJiraProject="OSP"
def test_list_subscriptions(testing_service_client):
    if not testing_service_client.is_api_enabled('osp_gateway', 'ListSubscriptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('osp_gateway', util.camelize('subscription_service'), 'ListSubscriptions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='osp_gateway', api_name='ListSubscriptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.osp_gateway.SubscriptionServiceClient(config, service_endpoint=service_endpoint)
            response = client.list_subscriptions(
                osp_home_region=request.pop(util.camelize('ospHomeRegion')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_subscriptions(
                    osp_home_region=request.pop(util.camelize('ospHomeRegion')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_subscriptions(
                        osp_home_region=request.pop(util.camelize('ospHomeRegion')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'osp_gateway',
            'ListSubscriptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscriptionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osp_team_oci_cam_ww_grp@oracle.com" jiraProject="OSP" opsJiraProject="OSP"
def test_pay_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('osp_gateway', 'PaySubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('osp_gateway', util.camelize('subscription_service'), 'PaySubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='osp_gateway', api_name='PaySubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.osp_gateway.SubscriptionServiceClient(config, service_endpoint=service_endpoint)
            response = client.pay_subscription(
                osp_home_region=request.pop(util.camelize('ospHomeRegion')),
                subscription_id=request.pop(util.camelize('subscriptionId')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                pay_subscription_details=request.pop(util.camelize('PaySubscriptionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'osp_gateway',
            'PaySubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'paySubscriptionReceipt',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osp_team_oci_cam_ww_grp@oracle.com" jiraProject="OSP" opsJiraProject="OSP"
def test_update_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('osp_gateway', 'UpdateSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('osp_gateway', util.camelize('subscription_service'), 'UpdateSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='osp_gateway', api_name='UpdateSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.osp_gateway.SubscriptionServiceClient(config, service_endpoint=service_endpoint)
            response = client.update_subscription(
                subscription_id=request.pop(util.camelize('subscriptionId')),
                osp_home_region=request.pop(util.camelize('ospHomeRegion')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                update_subscription_details=request.pop(util.camelize('UpdateSubscriptionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'osp_gateway',
            'UpdateSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscription',
            False,
            False
        )
