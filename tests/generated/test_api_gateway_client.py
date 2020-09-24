# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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
def test_change_certificate_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('apigateway', 'ChangeCertificateCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apigateway', util.camelize('api_gateway'), 'ChangeCertificateCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='apigateway', api_name='ChangeCertificateCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apigateway.ApiGatewayClient(config, service_endpoint=service_endpoint)
            response = client.change_certificate_compartment(
                certificate_id=request.pop(util.camelize('certificateId')),
                change_certificate_compartment_details=request.pop(util.camelize('ChangeCertificateCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apigateway',
            'ChangeCertificateCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_certificate_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_apigw_ww_grp@oracle.com" jiraProject="APIGW" opsJiraProject="APIGW"
def test_create_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('apigateway', 'CreateCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apigateway', util.camelize('api_gateway'), 'CreateCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='apigateway', api_name='CreateCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apigateway.ApiGatewayClient(config, service_endpoint=service_endpoint)
            response = client.create_certificate(
                create_certificate_details=request.pop(util.camelize('CreateCertificateDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apigateway',
            'CreateCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_apigw_ww_grp@oracle.com" jiraProject="APIGW" opsJiraProject="APIGW"
def test_delete_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('apigateway', 'DeleteCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apigateway', util.camelize('api_gateway'), 'DeleteCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='apigateway', api_name='DeleteCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apigateway.ApiGatewayClient(config, service_endpoint=service_endpoint)
            response = client.delete_certificate(
                certificate_id=request.pop(util.camelize('certificateId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apigateway',
            'DeleteCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_certificate',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_apigw_ww_grp@oracle.com" jiraProject="APIGW" opsJiraProject="APIGW"
def test_get_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('apigateway', 'GetCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apigateway', util.camelize('api_gateway'), 'GetCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='apigateway', api_name='GetCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apigateway.ApiGatewayClient(config, service_endpoint=service_endpoint)
            response = client.get_certificate(
                certificate_id=request.pop(util.camelize('certificateId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apigateway',
            'GetCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_apigw_ww_grp@oracle.com" jiraProject="APIGW" opsJiraProject="APIGW"
def test_list_certificates(testing_service_client):
    if not testing_service_client.is_api_enabled('apigateway', 'ListCertificates'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apigateway', util.camelize('api_gateway'), 'ListCertificates')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='apigateway', api_name='ListCertificates')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apigateway.ApiGatewayClient(config, service_endpoint=service_endpoint)
            response = client.list_certificates(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_certificates(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_certificates(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apigateway',
            'ListCertificates',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'certificateCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_apigw_ww_grp@oracle.com" jiraProject="APIGW" opsJiraProject="APIGW"
def test_update_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('apigateway', 'UpdateCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('apigateway', util.camelize('api_gateway'), 'UpdateCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='apigateway', api_name='UpdateCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.apigateway.ApiGatewayClient(config, service_endpoint=service_endpoint)
            response = client.update_certificate(
                certificate_id=request.pop(util.camelize('certificateId')),
                update_certificate_details=request.pop(util.camelize('UpdateCertificateDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'apigateway',
            'UpdateCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_certificate',
            False,
            False
        )
