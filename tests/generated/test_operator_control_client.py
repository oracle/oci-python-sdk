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

        cassette_location = os.path.join('generated', 'operator_access_control_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="adbd_admins_us_grp@oracle.com" jiraProject="CCA" opsJiraProject="OPCTL"
def test_change_operator_control_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('operator_access_control', 'ChangeOperatorControlCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('operator_access_control', util.camelize('operator_control'), 'ChangeOperatorControlCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='operator_access_control', api_name='ChangeOperatorControlCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.operator_access_control.OperatorControlClient(config, service_endpoint=service_endpoint)
            response = client.change_operator_control_compartment(
                operator_control_id=request.pop(util.camelize('operatorControlId')),
                change_operator_control_compartment_details=request.pop(util.camelize('ChangeOperatorControlCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'operator_access_control',
            'ChangeOperatorControlCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_operator_control_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="adbd_admins_us_grp@oracle.com" jiraProject="CCA" opsJiraProject="OPCTL"
def test_create_operator_control(testing_service_client):
    if not testing_service_client.is_api_enabled('operator_access_control', 'CreateOperatorControl'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('operator_access_control', util.camelize('operator_control'), 'CreateOperatorControl')
    )

    request_containers = testing_service_client.get_requests(service_name='operator_access_control', api_name='CreateOperatorControl')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.operator_access_control.OperatorControlClient(config, service_endpoint=service_endpoint)
            response = client.create_operator_control(
                create_operator_control_details=request.pop(util.camelize('CreateOperatorControlDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'operator_access_control',
            'CreateOperatorControl',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operatorControl',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="adbd_admins_us_grp@oracle.com" jiraProject="CCA" opsJiraProject="OPCTL"
def test_delete_operator_control(testing_service_client):
    if not testing_service_client.is_api_enabled('operator_access_control', 'DeleteOperatorControl'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('operator_access_control', util.camelize('operator_control'), 'DeleteOperatorControl')
    )

    request_containers = testing_service_client.get_requests(service_name='operator_access_control', api_name='DeleteOperatorControl')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.operator_access_control.OperatorControlClient(config, service_endpoint=service_endpoint)
            response = client.delete_operator_control(
                operator_control_id=request.pop(util.camelize('operatorControlId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'operator_access_control',
            'DeleteOperatorControl',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_operator_control',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="adbd_admins_us_grp@oracle.com" jiraProject="CCA" opsJiraProject="OPCTL"
def test_get_operator_control(testing_service_client):
    if not testing_service_client.is_api_enabled('operator_access_control', 'GetOperatorControl'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('operator_access_control', util.camelize('operator_control'), 'GetOperatorControl')
    )

    request_containers = testing_service_client.get_requests(service_name='operator_access_control', api_name='GetOperatorControl')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.operator_access_control.OperatorControlClient(config, service_endpoint=service_endpoint)
            response = client.get_operator_control(
                operator_control_id=request.pop(util.camelize('operatorControlId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'operator_access_control',
            'GetOperatorControl',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operatorControl',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="adbd_admins_us_grp@oracle.com" jiraProject="CCA" opsJiraProject="OPCTL"
def test_list_operator_controls(testing_service_client):
    if not testing_service_client.is_api_enabled('operator_access_control', 'ListOperatorControls'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('operator_access_control', util.camelize('operator_control'), 'ListOperatorControls')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='operator_access_control', api_name='ListOperatorControls')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.operator_access_control.OperatorControlClient(config, service_endpoint=service_endpoint)
            response = client.list_operator_controls(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_operator_controls(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_operator_controls(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'operator_access_control',
            'ListOperatorControls',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operatorControlCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="adbd_admins_us_grp@oracle.com" jiraProject="CCA" opsJiraProject="OPCTL"
def test_update_operator_control(testing_service_client):
    if not testing_service_client.is_api_enabled('operator_access_control', 'UpdateOperatorControl'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('operator_access_control', util.camelize('operator_control'), 'UpdateOperatorControl')
    )

    request_containers = testing_service_client.get_requests(service_name='operator_access_control', api_name='UpdateOperatorControl')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.operator_access_control.OperatorControlClient(config, service_endpoint=service_endpoint)
            response = client.update_operator_control(
                operator_control_id=request.pop(util.camelize('operatorControlId')),
                update_operator_control_details=request.pop(util.camelize('UpdateOperatorControlDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'operator_access_control',
            'UpdateOperatorControl',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operatorControl',
            False,
            False
        )
