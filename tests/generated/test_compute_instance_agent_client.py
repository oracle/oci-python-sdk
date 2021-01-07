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

        cassette_location = os.path.join('generated', 'compute_instance_agent_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="computeInstanceAgent" email="oci_osi_grp@oracle.com" jiraProject="OSI" opsJiraProject="IMAGE"
def test_cancel_instance_agent_command(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_instance_agent', 'CancelInstanceAgentCommand'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_instance_agent', util.camelize('compute_instance_agent'), 'CancelInstanceAgentCommand')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_instance_agent', api_name='CancelInstanceAgentCommand')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_instance_agent.ComputeInstanceAgentClient(config, service_endpoint=service_endpoint)
            response = client.cancel_instance_agent_command(
                instance_agent_command_id=request.pop(util.camelize('instanceAgentCommandId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_instance_agent',
            'CancelInstanceAgentCommand',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_instance_agent_command',
            True,
            False
        )


# IssueRoutingInfo tag="computeInstanceAgent" email="oci_osi_grp@oracle.com" jiraProject="OSI" opsJiraProject="IMAGE"
def test_create_instance_agent_command(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_instance_agent', 'CreateInstanceAgentCommand'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_instance_agent', util.camelize('compute_instance_agent'), 'CreateInstanceAgentCommand')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_instance_agent', api_name='CreateInstanceAgentCommand')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_instance_agent.ComputeInstanceAgentClient(config, service_endpoint=service_endpoint)
            response = client.create_instance_agent_command(
                create_instance_agent_command_details=request.pop(util.camelize('CreateInstanceAgentCommandDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_instance_agent',
            'CreateInstanceAgentCommand',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceAgentCommand',
            False,
            False
        )


# IssueRoutingInfo tag="computeInstanceAgent" email="oci_osi_grp@oracle.com" jiraProject="OSI" opsJiraProject="IMAGE"
def test_get_instance_agent_command(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_instance_agent', 'GetInstanceAgentCommand'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_instance_agent', util.camelize('compute_instance_agent'), 'GetInstanceAgentCommand')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_instance_agent', api_name='GetInstanceAgentCommand')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_instance_agent.ComputeInstanceAgentClient(config, service_endpoint=service_endpoint)
            response = client.get_instance_agent_command(
                instance_agent_command_id=request.pop(util.camelize('instanceAgentCommandId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_instance_agent',
            'GetInstanceAgentCommand',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceAgentCommand',
            False,
            False
        )


# IssueRoutingInfo tag="computeInstanceAgent" email="oci_osi_grp@oracle.com" jiraProject="OSI" opsJiraProject="IMAGE"
def test_get_instance_agent_command_execution(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_instance_agent', 'GetInstanceAgentCommandExecution'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_instance_agent', util.camelize('compute_instance_agent'), 'GetInstanceAgentCommandExecution')
    )

    request_containers = testing_service_client.get_requests(service_name='compute_instance_agent', api_name='GetInstanceAgentCommandExecution')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_instance_agent.ComputeInstanceAgentClient(config, service_endpoint=service_endpoint)
            response = client.get_instance_agent_command_execution(
                instance_agent_command_id=request.pop(util.camelize('instanceAgentCommandId')),
                instance_id=request.pop(util.camelize('instanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_instance_agent',
            'GetInstanceAgentCommandExecution',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceAgentCommandExecution',
            False,
            False
        )


# IssueRoutingInfo tag="computeInstanceAgent" email="oci_osi_grp@oracle.com" jiraProject="OSI" opsJiraProject="IMAGE"
def test_list_instance_agent_command_executions(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_instance_agent', 'ListInstanceAgentCommandExecutions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_instance_agent', util.camelize('compute_instance_agent'), 'ListInstanceAgentCommandExecutions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='compute_instance_agent', api_name='ListInstanceAgentCommandExecutions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_instance_agent.ComputeInstanceAgentClient(config, service_endpoint=service_endpoint)
            response = client.list_instance_agent_command_executions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                instance_id=request.pop(util.camelize('instanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_instance_agent_command_executions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    instance_id=request.pop(util.camelize('instanceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_instance_agent_command_executions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        instance_id=request.pop(util.camelize('instanceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_instance_agent',
            'ListInstanceAgentCommandExecutions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceAgentCommandExecutionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="computeInstanceAgent" email="oci_osi_grp@oracle.com" jiraProject="OSI" opsJiraProject="IMAGE"
def test_list_instance_agent_commands(testing_service_client):
    if not testing_service_client.is_api_enabled('compute_instance_agent', 'ListInstanceAgentCommands'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('compute_instance_agent', util.camelize('compute_instance_agent'), 'ListInstanceAgentCommands')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='compute_instance_agent', api_name='ListInstanceAgentCommands')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.compute_instance_agent.ComputeInstanceAgentClient(config, service_endpoint=service_endpoint)
            response = client.list_instance_agent_commands(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_instance_agent_commands(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_instance_agent_commands(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'compute_instance_agent',
            'ListInstanceAgentCommands',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'instanceAgentCommandSummary',
            False,
            True
        )
