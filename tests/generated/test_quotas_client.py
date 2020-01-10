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
    # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
    # instead of 'query' matcher (which ignores sessionId in the url)
    # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
    custom_vcr = test_config_container.create_vcr()
    custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

    cassette_location = os.path.join('generated', 'limits_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


# IssueRoutingInfo tag="default" email="platform_limits_grp@oracle.com" jiraProject="LIM" opsJiraProject="LIM"
def test_create_quota(testing_service_client):
    if not testing_service_client.is_api_enabled('limits', 'CreateQuota'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('limits', util.camelize('quotas'), 'CreateQuota')
    )

    request_containers = testing_service_client.get_requests(service_name='limits', api_name='CreateQuota')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.limits.QuotasClient(config, service_endpoint=service_endpoint)
            response = client.create_quota(
                create_quota_details=request.pop(util.camelize('create_quota_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'limits',
            'CreateQuota',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'quota',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="platform_limits_grp@oracle.com" jiraProject="LIM" opsJiraProject="LIM"
def test_delete_quota(testing_service_client):
    if not testing_service_client.is_api_enabled('limits', 'DeleteQuota'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('limits', util.camelize('quotas'), 'DeleteQuota')
    )

    request_containers = testing_service_client.get_requests(service_name='limits', api_name='DeleteQuota')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.limits.QuotasClient(config, service_endpoint=service_endpoint)
            response = client.delete_quota(
                quota_id=request.pop(util.camelize('quota_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'limits',
            'DeleteQuota',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_quota',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="platform_limits_grp@oracle.com" jiraProject="LIM" opsJiraProject="LIM"
def test_get_quota(testing_service_client):
    if not testing_service_client.is_api_enabled('limits', 'GetQuota'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('limits', util.camelize('quotas'), 'GetQuota')
    )

    request_containers = testing_service_client.get_requests(service_name='limits', api_name='GetQuota')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.limits.QuotasClient(config, service_endpoint=service_endpoint)
            response = client.get_quota(
                quota_id=request.pop(util.camelize('quota_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'limits',
            'GetQuota',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'quota',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="platform_limits_grp@oracle.com" jiraProject="LIM" opsJiraProject="LIM"
def test_list_quotas(testing_service_client):
    if not testing_service_client.is_api_enabled('limits', 'ListQuotas'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('limits', util.camelize('quotas'), 'ListQuotas')
    )

    request_containers = testing_service_client.get_requests(service_name='limits', api_name='ListQuotas')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.limits.QuotasClient(config, service_endpoint=service_endpoint)
            response = client.list_quotas(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_quotas(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_quotas(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'limits',
            'ListQuotas',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'quotaSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="platform_limits_grp@oracle.com" jiraProject="LIM" opsJiraProject="LIM"
def test_update_quota(testing_service_client):
    if not testing_service_client.is_api_enabled('limits', 'UpdateQuota'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('limits', util.camelize('quotas'), 'UpdateQuota')
    )

    request_containers = testing_service_client.get_requests(service_name='limits', api_name='UpdateQuota')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.limits.QuotasClient(config, service_endpoint=service_endpoint)
            response = client.update_quota(
                quota_id=request.pop(util.camelize('quota_id')),
                update_quota_details=request.pop(util.camelize('update_quota_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'limits',
            'UpdateQuota',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'quota',
            False,
            False
        )