# Code generated. DO NOT EDIT.
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
    if test_config_container.test_mode == 'mock':
        yield
    else:
        # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
        # instead of 'query' matcher (which ignores sessionId in the url)
        # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
        custom_vcr = test_config_container.create_vcr()
        custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

        cassette_location = os.path.join('generated', 'audit_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_events_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/SA" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/SA"
def test_get_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('audit', 'GetConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('audit', util.camelize('audit'), 'GetConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='audit', api_name='GetConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.audit.AuditClient(config, service_endpoint=service_endpoint)
            response = client.get_configuration(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'audit',
            'GetConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_events_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/SA" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/SA"
def test_list_events(testing_service_client):
    if not testing_service_client.is_api_enabled('audit', 'ListEvents'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('audit', util.camelize('audit'), 'ListEvents')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='audit', api_name='ListEvents')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.audit.AuditClient(config, service_endpoint=service_endpoint)
            response = client.list_events(
                compartment_id=request.pop(util.camelize('compartmentId')),
                start_time=request.pop(util.camelize('startTime')),
                end_time=request.pop(util.camelize('endTime')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_events(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    start_time=request.pop(util.camelize('startTime')),
                    end_time=request.pop(util.camelize('endTime')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_events(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        start_time=request.pop(util.camelize('startTime')),
                        end_time=request.pop(util.camelize('endTime')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'audit',
            'ListEvents',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'auditEvent',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_events_dev_grp@oracle.com" jiraProject="https://jira.oci.oraclecorp.com/projects/SA" opsJiraProject="https://jira-sd.mc1.oracleiaas.com/projects/SA"
def test_update_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('audit', 'UpdateConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('audit', util.camelize('audit'), 'UpdateConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='audit', api_name='UpdateConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.audit.AuditClient(config, service_endpoint=service_endpoint)
            response = client.update_configuration(
                compartment_id=request.pop(util.camelize('compartmentId')),
                update_configuration_details=request.pop(util.camelize('UpdateConfigurationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'audit',
            'UpdateConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_configuration',
            False,
            False
        )
