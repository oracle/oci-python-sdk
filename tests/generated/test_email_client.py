# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'email_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="email-dev_us_grp@oracle.com" jiraProject="ED" opsJiraProject="ED"
def test_change_sender_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('email', 'ChangeSenderCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('email', util.camelize('email'), 'ChangeSenderCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='email', api_name='ChangeSenderCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.email.EmailClient(config, service_endpoint=service_endpoint)
            response = client.change_sender_compartment(
                sender_id=request.pop(util.camelize('senderId')),
                change_sender_compartment_details=request.pop(util.camelize('ChangeSenderCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'email',
            'ChangeSenderCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_sender_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="email-dev_us_grp@oracle.com" jiraProject="ED" opsJiraProject="ED"
def test_create_sender(testing_service_client):
    if not testing_service_client.is_api_enabled('email', 'CreateSender'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('email', util.camelize('email'), 'CreateSender')
    )

    request_containers = testing_service_client.get_requests(service_name='email', api_name='CreateSender')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.email.EmailClient(config, service_endpoint=service_endpoint)
            response = client.create_sender(
                create_sender_details=request.pop(util.camelize('CreateSenderDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'email',
            'CreateSender',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sender',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="email-dev_us_grp@oracle.com" jiraProject="ED" opsJiraProject="ED"
def test_create_suppression(testing_service_client):
    if not testing_service_client.is_api_enabled('email', 'CreateSuppression'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('email', util.camelize('email'), 'CreateSuppression')
    )

    request_containers = testing_service_client.get_requests(service_name='email', api_name='CreateSuppression')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.email.EmailClient(config, service_endpoint=service_endpoint)
            response = client.create_suppression(
                create_suppression_details=request.pop(util.camelize('CreateSuppressionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'email',
            'CreateSuppression',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'suppression',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="email-dev_us_grp@oracle.com" jiraProject="ED" opsJiraProject="ED"
def test_delete_sender(testing_service_client):
    if not testing_service_client.is_api_enabled('email', 'DeleteSender'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('email', util.camelize('email'), 'DeleteSender')
    )

    request_containers = testing_service_client.get_requests(service_name='email', api_name='DeleteSender')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.email.EmailClient(config, service_endpoint=service_endpoint)
            response = client.delete_sender(
                sender_id=request.pop(util.camelize('senderId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'email',
            'DeleteSender',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_sender',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="email-dev_us_grp@oracle.com" jiraProject="ED" opsJiraProject="ED"
def test_delete_suppression(testing_service_client):
    if not testing_service_client.is_api_enabled('email', 'DeleteSuppression'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('email', util.camelize('email'), 'DeleteSuppression')
    )

    request_containers = testing_service_client.get_requests(service_name='email', api_name='DeleteSuppression')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.email.EmailClient(config, service_endpoint=service_endpoint)
            response = client.delete_suppression(
                suppression_id=request.pop(util.camelize('suppressionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'email',
            'DeleteSuppression',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_suppression',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="email-dev_us_grp@oracle.com" jiraProject="ED" opsJiraProject="ED"
def test_get_sender(testing_service_client):
    if not testing_service_client.is_api_enabled('email', 'GetSender'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('email', util.camelize('email'), 'GetSender')
    )

    request_containers = testing_service_client.get_requests(service_name='email', api_name='GetSender')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.email.EmailClient(config, service_endpoint=service_endpoint)
            response = client.get_sender(
                sender_id=request.pop(util.camelize('senderId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'email',
            'GetSender',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sender',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="email-dev_us_grp@oracle.com" jiraProject="ED" opsJiraProject="ED"
def test_get_suppression(testing_service_client):
    if not testing_service_client.is_api_enabled('email', 'GetSuppression'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('email', util.camelize('email'), 'GetSuppression')
    )

    request_containers = testing_service_client.get_requests(service_name='email', api_name='GetSuppression')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.email.EmailClient(config, service_endpoint=service_endpoint)
            response = client.get_suppression(
                suppression_id=request.pop(util.camelize('suppressionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'email',
            'GetSuppression',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'suppression',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="email-dev_us_grp@oracle.com" jiraProject="ED" opsJiraProject="ED"
def test_list_senders(testing_service_client):
    if not testing_service_client.is_api_enabled('email', 'ListSenders'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('email', util.camelize('email'), 'ListSenders')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='email', api_name='ListSenders')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.email.EmailClient(config, service_endpoint=service_endpoint)
            response = client.list_senders(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_senders(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_senders(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'email',
            'ListSenders',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'senderSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="email-dev_us_grp@oracle.com" jiraProject="ED" opsJiraProject="ED"
def test_list_suppressions(testing_service_client):
    if not testing_service_client.is_api_enabled('email', 'ListSuppressions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('email', util.camelize('email'), 'ListSuppressions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='email', api_name='ListSuppressions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.email.EmailClient(config, service_endpoint=service_endpoint)
            response = client.list_suppressions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_suppressions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_suppressions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'email',
            'ListSuppressions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'suppressionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="email-dev_us_grp@oracle.com" jiraProject="ED" opsJiraProject="ED"
def test_update_sender(testing_service_client):
    if not testing_service_client.is_api_enabled('email', 'UpdateSender'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('email', util.camelize('email'), 'UpdateSender')
    )

    request_containers = testing_service_client.get_requests(service_name='email', api_name='UpdateSender')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.email.EmailClient(config, service_endpoint=service_endpoint)
            response = client.update_sender(
                sender_id=request.pop(util.camelize('senderId')),
                update_sender_details=request.pop(util.camelize('UpdateSenderDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'email',
            'UpdateSender',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'sender',
            False,
            False
        )
