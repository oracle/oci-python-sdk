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

        cassette_location = os.path.join('generated', 'waas_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_change_http_redirect_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ChangeHttpRedirectCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('redirect'), 'ChangeHttpRedirectCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ChangeHttpRedirectCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waas.RedirectClient(config, service_endpoint=service_endpoint)
            response = client.change_http_redirect_compartment(
                http_redirect_id=request.pop(util.camelize('httpRedirectId')),
                change_http_redirect_compartment_details=request.pop(util.camelize('ChangeHttpRedirectCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ChangeHttpRedirectCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_http_redirect_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_create_http_redirect(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'CreateHttpRedirect'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('redirect'), 'CreateHttpRedirect')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='CreateHttpRedirect')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waas.RedirectClient(config, service_endpoint=service_endpoint)
            response = client.create_http_redirect(
                create_http_redirect_details=request.pop(util.camelize('CreateHttpRedirectDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'CreateHttpRedirect',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_http_redirect',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_delete_http_redirect(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'DeleteHttpRedirect'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('redirect'), 'DeleteHttpRedirect')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='DeleteHttpRedirect')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waas.RedirectClient(config, service_endpoint=service_endpoint)
            response = client.delete_http_redirect(
                http_redirect_id=request.pop(util.camelize('httpRedirectId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'DeleteHttpRedirect',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_http_redirect',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_get_http_redirect(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'GetHttpRedirect'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('redirect'), 'GetHttpRedirect')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='GetHttpRedirect')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waas.RedirectClient(config, service_endpoint=service_endpoint)
            response = client.get_http_redirect(
                http_redirect_id=request.pop(util.camelize('httpRedirectId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'GetHttpRedirect',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'httpRedirect',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_list_http_redirects(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'ListHttpRedirects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('redirect'), 'ListHttpRedirects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='ListHttpRedirects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waas.RedirectClient(config, service_endpoint=service_endpoint)
            response = client.list_http_redirects(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_http_redirects(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_http_redirects(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'ListHttpRedirects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'httpRedirectSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_waas_dev_us_grp@oracle.com" jiraProject="WAAS" opsJiraProject="WAF"
def test_update_http_redirect(testing_service_client):
    if not testing_service_client.is_api_enabled('waas', 'UpdateHttpRedirect'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('waas', util.camelize('redirect'), 'UpdateHttpRedirect')
    )

    request_containers = testing_service_client.get_requests(service_name='waas', api_name='UpdateHttpRedirect')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.waas.RedirectClient(config, service_endpoint=service_endpoint)
            response = client.update_http_redirect(
                http_redirect_id=request.pop(util.camelize('httpRedirectId')),
                update_http_redirect_details=request.pop(util.camelize('UpdateHttpRedirectDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'waas',
            'UpdateHttpRedirect',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_http_redirect',
            False,
            False
        )
