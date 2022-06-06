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

        cassette_location = os.path.join('generated', 'tenant_manager_control_plane_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_create_subscription_mapping(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'CreateSubscriptionMapping'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('subscription'), 'CreateSubscriptionMapping')
    )

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='CreateSubscriptionMapping')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.SubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.create_subscription_mapping(
                create_subscription_mapping_details=request.pop(util.camelize('CreateSubscriptionMappingDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'CreateSubscriptionMapping',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscriptionMapping',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_delete_subscription_mapping(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'DeleteSubscriptionMapping'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('subscription'), 'DeleteSubscriptionMapping')
    )

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='DeleteSubscriptionMapping')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.SubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.delete_subscription_mapping(
                subscription_mapping_id=request.pop(util.camelize('subscriptionMappingId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'DeleteSubscriptionMapping',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_subscription_mapping',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_get_assigned_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'GetAssignedSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('subscription'), 'GetAssignedSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='GetAssignedSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.SubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.get_assigned_subscription(
                assigned_subscription_id=request.pop(util.camelize('assignedSubscriptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'GetAssignedSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'assignedSubscription',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_get_subscription(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'GetSubscription'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('subscription'), 'GetSubscription')
    )

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='GetSubscription')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.SubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.get_subscription(
                subscription_id=request.pop(util.camelize('subscriptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'GetSubscription',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscription',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_get_subscription_mapping(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'GetSubscriptionMapping'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('subscription'), 'GetSubscriptionMapping')
    )

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='GetSubscriptionMapping')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.SubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.get_subscription_mapping(
                subscription_mapping_id=request.pop(util.camelize('subscriptionMappingId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'GetSubscriptionMapping',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscriptionMapping',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_list_assigned_subscriptions(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'ListAssignedSubscriptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('subscription'), 'ListAssignedSubscriptions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='ListAssignedSubscriptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.SubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.list_assigned_subscriptions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_assigned_subscriptions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_assigned_subscriptions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'ListAssignedSubscriptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'assignedSubscriptionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_list_available_regions(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'ListAvailableRegions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('subscription'), 'ListAvailableRegions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='ListAvailableRegions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.SubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.list_available_regions(
                subscription_id=request.pop(util.camelize('subscriptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_available_regions(
                    subscription_id=request.pop(util.camelize('subscriptionId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_available_regions(
                        subscription_id=request.pop(util.camelize('subscriptionId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'ListAvailableRegions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'availableRegionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_list_subscription_mappings(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'ListSubscriptionMappings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('subscription'), 'ListSubscriptionMappings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='ListSubscriptionMappings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.SubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.list_subscription_mappings(
                subscription_id=request.pop(util.camelize('subscriptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_subscription_mappings(
                    subscription_id=request.pop(util.camelize('subscriptionId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_subscription_mappings(
                        subscription_id=request.pop(util.camelize('subscriptionId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'ListSubscriptionMappings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscriptionMappingCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="acc_customer_tools_us_grp@oracle.com" jiraProject="ACCMGMT" opsJiraProject="ACCMGMT"
def test_list_subscriptions(testing_service_client):
    if not testing_service_client.is_api_enabled('tenant_manager_control_plane', 'ListSubscriptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('tenant_manager_control_plane', util.camelize('subscription'), 'ListSubscriptions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='tenant_manager_control_plane', api_name='ListSubscriptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.tenant_manager_control_plane.SubscriptionClient(config, service_endpoint=service_endpoint)
            response = client.list_subscriptions(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_subscriptions(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_subscriptions(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'tenant_manager_control_plane',
            'ListSubscriptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscriptionCollection',
            False,
            True
        )