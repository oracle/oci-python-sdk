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

        cassette_location = os.path.join('generated', 'usage_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_create_redeemable_user(testing_service_client):
    if not testing_service_client.is_api_enabled('usage', 'CreateRedeemableUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage', util.camelize('rewards'), 'CreateRedeemableUser')
    )

    request_containers = testing_service_client.get_requests(service_name='usage', api_name='CreateRedeemableUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage.RewardsClient(config, service_endpoint=service_endpoint)
            response = client.create_redeemable_user(
                create_redeemable_user_details=request.pop(util.camelize('CreateRedeemableUserDetails')),
                tenancy_id=request.pop(util.camelize('tenancyId')),
                subscription_id=request.pop(util.camelize('subscriptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage',
            'CreateRedeemableUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'redeemableUserCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_delete_redeemable_user(testing_service_client):
    if not testing_service_client.is_api_enabled('usage', 'DeleteRedeemableUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage', util.camelize('rewards'), 'DeleteRedeemableUser')
    )

    request_containers = testing_service_client.get_requests(service_name='usage', api_name='DeleteRedeemableUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage.RewardsClient(config, service_endpoint=service_endpoint)
            response = client.delete_redeemable_user(
                email_id=request.pop(util.camelize('emailId')),
                tenancy_id=request.pop(util.camelize('tenancyId')),
                subscription_id=request.pop(util.camelize('subscriptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage',
            'DeleteRedeemableUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_redeemable_user',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_list_products(testing_service_client):
    if not testing_service_client.is_api_enabled('usage', 'ListProducts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage', util.camelize('rewards'), 'ListProducts')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='usage', api_name='ListProducts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage.RewardsClient(config, service_endpoint=service_endpoint)
            response = client.list_products(
                tenancy_id=request.pop(util.camelize('tenancyId')),
                subscription_id=request.pop(util.camelize('subscriptionId')),
                usage_period_key=request.pop(util.camelize('usagePeriodKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_products(
                    tenancy_id=request.pop(util.camelize('tenancyId')),
                    subscription_id=request.pop(util.camelize('subscriptionId')),
                    usage_period_key=request.pop(util.camelize('usagePeriodKey')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_products(
                        tenancy_id=request.pop(util.camelize('tenancyId')),
                        subscription_id=request.pop(util.camelize('subscriptionId')),
                        usage_period_key=request.pop(util.camelize('usagePeriodKey')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage',
            'ListProducts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'productCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_list_redeemable_users(testing_service_client):
    if not testing_service_client.is_api_enabled('usage', 'ListRedeemableUsers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage', util.camelize('rewards'), 'ListRedeemableUsers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='usage', api_name='ListRedeemableUsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage.RewardsClient(config, service_endpoint=service_endpoint)
            response = client.list_redeemable_users(
                tenancy_id=request.pop(util.camelize('tenancyId')),
                subscription_id=request.pop(util.camelize('subscriptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_redeemable_users(
                    tenancy_id=request.pop(util.camelize('tenancyId')),
                    subscription_id=request.pop(util.camelize('subscriptionId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_redeemable_users(
                        tenancy_id=request.pop(util.camelize('tenancyId')),
                        subscription_id=request.pop(util.camelize('subscriptionId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage',
            'ListRedeemableUsers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'redeemableUserCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_list_redemptions(testing_service_client):
    if not testing_service_client.is_api_enabled('usage', 'ListRedemptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage', util.camelize('rewards'), 'ListRedemptions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='usage', api_name='ListRedemptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage.RewardsClient(config, service_endpoint=service_endpoint)
            response = client.list_redemptions(
                tenancy_id=request.pop(util.camelize('tenancyId')),
                subscription_id=request.pop(util.camelize('subscriptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_redemptions(
                    tenancy_id=request.pop(util.camelize('tenancyId')),
                    subscription_id=request.pop(util.camelize('subscriptionId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_redemptions(
                        tenancy_id=request.pop(util.camelize('tenancyId')),
                        subscription_id=request.pop(util.camelize('subscriptionId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage',
            'ListRedemptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'redemptionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_metering_team_us_grp@oracle.com" jiraProject="METER" opsJiraProject="MTRC"
def test_list_rewards(testing_service_client):
    if not testing_service_client.is_api_enabled('usage', 'ListRewards'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('usage', util.camelize('rewards'), 'ListRewards')
    )

    request_containers = testing_service_client.get_requests(service_name='usage', api_name='ListRewards')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.usage.RewardsClient(config, service_endpoint=service_endpoint)
            response = client.list_rewards(
                tenancy_id=request.pop(util.camelize('tenancyId')),
                subscription_id=request.pop(util.camelize('subscriptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'usage',
            'ListRewards',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'rewardCollection',
            False,
            False
        )
