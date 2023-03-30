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

        cassette_location = os.path.join('generated', 'onesubscription_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="kuaskum_org_ww@oracle.com" jiraProject="OSUB" opsJiraProject="OSUB"
def test_get_subscribed_service(testing_service_client):
    if not testing_service_client.is_api_enabled('onesubscription', 'GetSubscribedService'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('onesubscription', util.camelize('subscribed_service'), 'GetSubscribedService')
    )

    request_containers = testing_service_client.get_requests(service_name='onesubscription', api_name='GetSubscribedService')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.onesubscription.SubscribedServiceClient(config, service_endpoint=service_endpoint)
            response = client.get_subscribed_service(
                subscribed_service_id=request.pop(util.camelize('subscribedServiceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'onesubscription',
            'GetSubscribedService',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscribedService',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="kuaskum_org_ww@oracle.com" jiraProject="OSUB" opsJiraProject="OSUB"
def test_list_subscribed_services(testing_service_client):
    if not testing_service_client.is_api_enabled('onesubscription', 'ListSubscribedServices'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('onesubscription', util.camelize('subscribed_service'), 'ListSubscribedServices')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='onesubscription', api_name='ListSubscribedServices')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.onesubscription.SubscribedServiceClient(config, service_endpoint=service_endpoint)
            response = client.list_subscribed_services(
                compartment_id=request.pop(util.camelize('compartmentId')),
                subscription_id=request.pop(util.camelize('subscriptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_subscribed_services(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    subscription_id=request.pop(util.camelize('subscriptionId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_subscribed_services(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        subscription_id=request.pop(util.camelize('subscriptionId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'onesubscription',
            'ListSubscribedServices',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'subscribedServiceSummary',
            False,
            True
        )