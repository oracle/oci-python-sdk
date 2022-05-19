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

        cassette_location = os.path.join('generated', 'rover_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_rover_node_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'ChangeRoverNodeCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_node'), 'ChangeRoverNodeCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='ChangeRoverNodeCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverNodeClient(config, service_endpoint=service_endpoint)
            response = client.change_rover_node_compartment(
                rover_node_id=request.pop(util.camelize('roverNodeId')),
                change_rover_node_compartment_details=request.pop(util.camelize('ChangeRoverNodeCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'ChangeRoverNodeCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_rover_node_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_rover_node(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'CreateRoverNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_node'), 'CreateRoverNode')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='CreateRoverNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverNodeClient(config, service_endpoint=service_endpoint)
            response = client.create_rover_node(
                create_rover_node_details=request.pop(util.camelize('CreateRoverNodeDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'CreateRoverNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverNode',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_rover_node(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'DeleteRoverNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_node'), 'DeleteRoverNode')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='DeleteRoverNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverNodeClient(config, service_endpoint=service_endpoint)
            response = client.delete_rover_node(
                rover_node_id=request.pop(util.camelize('roverNodeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'DeleteRoverNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_rover_node',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_rover_node(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'GetRoverNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_node'), 'GetRoverNode')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='GetRoverNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverNodeClient(config, service_endpoint=service_endpoint)
            response = client.get_rover_node(
                rover_node_id=request.pop(util.camelize('roverNodeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'GetRoverNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverNode',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_rover_node_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'GetRoverNodeCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_node'), 'GetRoverNodeCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='GetRoverNodeCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverNodeClient(config, service_endpoint=service_endpoint)
            response = client.get_rover_node_certificate(
                rover_node_id=request.pop(util.camelize('roverNodeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'GetRoverNodeCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverNodeCertificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_rover_node_encryption_key(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'GetRoverNodeEncryptionKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_node'), 'GetRoverNodeEncryptionKey')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='GetRoverNodeEncryptionKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverNodeClient(config, service_endpoint=service_endpoint)
            response = client.get_rover_node_encryption_key(
                rover_node_id=request.pop(util.camelize('roverNodeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'GetRoverNodeEncryptionKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverNodeEncryptionKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_rover_node_get_rpt(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'GetRoverNodeGetRpt'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_node'), 'GetRoverNodeGetRpt')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='GetRoverNodeGetRpt')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverNodeClient(config, service_endpoint=service_endpoint)
            response = client.get_rover_node_get_rpt(
                rover_node_id=request.pop(util.camelize('roverNodeId')),
                jwt=request.pop(util.camelize('jwt')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'GetRoverNodeGetRpt',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverNodeGetRpt',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_rover_nodes(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'ListRoverNodes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_node'), 'ListRoverNodes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='ListRoverNodes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverNodeClient(config, service_endpoint=service_endpoint)
            response = client.list_rover_nodes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_rover_nodes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_rover_nodes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'ListRoverNodes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverNodeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_rover_node_action_set_key(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'RoverNodeActionSetKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_node'), 'RoverNodeActionSetKey')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='RoverNodeActionSetKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverNodeClient(config, service_endpoint=service_endpoint)
            response = client.rover_node_action_set_key(
                rover_node_id=request.pop(util.camelize('roverNodeId')),
                jwt=request.pop(util.camelize('jwt')),
                rover_node_action_set_key_details=request.pop(util.camelize('RoverNodeActionSetKeyDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'RoverNodeActionSetKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverNodeSetKey',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_rover_node(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'UpdateRoverNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_node'), 'UpdateRoverNode')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='UpdateRoverNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverNodeClient(config, service_endpoint=service_endpoint)
            response = client.update_rover_node(
                rover_node_id=request.pop(util.camelize('roverNodeId')),
                update_rover_node_details=request.pop(util.camelize('UpdateRoverNodeDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'UpdateRoverNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverNode',
            False,
            False
        )
