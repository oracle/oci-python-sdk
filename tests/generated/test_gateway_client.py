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

        cassette_location = os.path.join('generated', 'apigateway_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_apigw_ww_grp@oracle.com" jiraProject="APIGW" opsJiraProject="APIGW"
def test_change_gateway_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('apigateway', 'ChangeGatewayCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apigateway', util.camelize('gateway'), 'ChangeGatewayCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='apigateway', api_name='ChangeGatewayCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apigateway.GatewayClient(config, service_endpoint=service_endpoint)
            response = client.change_gateway_compartment(
                gateway_id=request.pop(util.camelize('gatewayId')),
                change_gateway_compartment_details=request.pop(util.camelize('ChangeGatewayCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apigateway',
            'ChangeGatewayCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_gateway_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_apigw_ww_grp@oracle.com" jiraProject="APIGW" opsJiraProject="APIGW"
def test_create_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('apigateway', 'CreateGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apigateway', util.camelize('gateway'), 'CreateGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='apigateway', api_name='CreateGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apigateway.GatewayClient(config, service_endpoint=service_endpoint)
            response = client.create_gateway(
                create_gateway_details=request.pop(util.camelize('CreateGatewayDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apigateway',
            'CreateGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'gateway',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_apigw_ww_grp@oracle.com" jiraProject="APIGW" opsJiraProject="APIGW"
def test_delete_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('apigateway', 'DeleteGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apigateway', util.camelize('gateway'), 'DeleteGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='apigateway', api_name='DeleteGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apigateway.GatewayClient(config, service_endpoint=service_endpoint)
            response = client.delete_gateway(
                gateway_id=request.pop(util.camelize('gatewayId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apigateway',
            'DeleteGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_gateway',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_apigw_ww_grp@oracle.com" jiraProject="APIGW" opsJiraProject="APIGW"
def test_get_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('apigateway', 'GetGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apigateway', util.camelize('gateway'), 'GetGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='apigateway', api_name='GetGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apigateway.GatewayClient(config, service_endpoint=service_endpoint)
            response = client.get_gateway(
                gateway_id=request.pop(util.camelize('gatewayId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apigateway',
            'GetGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'gateway',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_apigw_ww_grp@oracle.com" jiraProject="APIGW" opsJiraProject="APIGW"
def test_list_gateways(testing_service_client):
    if not testing_service_client.is_api_enabled('apigateway', 'ListGateways'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apigateway', util.camelize('gateway'), 'ListGateways')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='apigateway', api_name='ListGateways')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apigateway.GatewayClient(config, service_endpoint=service_endpoint)
            response = client.list_gateways(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_gateways(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_gateways(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apigateway',
            'ListGateways',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'gatewayCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_apigw_ww_grp@oracle.com" jiraProject="APIGW" opsJiraProject="APIGW"
def test_update_gateway(testing_service_client):
    if not testing_service_client.is_api_enabled('apigateway', 'UpdateGateway'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apigateway', util.camelize('gateway'), 'UpdateGateway')
    )

    request_containers = testing_service_client.get_requests(service_name='apigateway', api_name='UpdateGateway')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apigateway.GatewayClient(config, service_endpoint=service_endpoint)
            response = client.update_gateway(
                gateway_id=request.pop(util.camelize('gatewayId')),
                update_gateway_details=request.pop(util.camelize('UpdateGatewayDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apigateway',
            'UpdateGateway',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_gateway',
            False,
            False
        )
