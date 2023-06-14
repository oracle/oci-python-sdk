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

        cassette_location = os.path.join('generated', 'rover_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_rover_cluster_rover_bundle_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'ListRoverClusterRoverBundleRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_bundle'), 'ListRoverClusterRoverBundleRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='ListRoverClusterRoverBundleRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverBundleClient(config, service_endpoint=service_endpoint)
            response = client.list_rover_cluster_rover_bundle_requests(
                rover_cluster_id=request.pop(util.camelize('roverClusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_rover_cluster_rover_bundle_requests(
                    rover_cluster_id=request.pop(util.camelize('roverClusterId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_rover_cluster_rover_bundle_requests(
                        rover_cluster_id=request.pop(util.camelize('roverClusterId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'ListRoverClusterRoverBundleRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverBundleRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_rover_node_rover_bundle_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'ListRoverNodeRoverBundleRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_bundle'), 'ListRoverNodeRoverBundleRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='ListRoverNodeRoverBundleRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverBundleClient(config, service_endpoint=service_endpoint)
            response = client.list_rover_node_rover_bundle_requests(
                rover_node_id=request.pop(util.camelize('roverNodeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_rover_node_rover_bundle_requests(
                    rover_node_id=request.pop(util.camelize('roverNodeId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_rover_node_rover_bundle_requests(
                        rover_node_id=request.pop(util.camelize('roverNodeId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'ListRoverNodeRoverBundleRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverBundleRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_request_bundle_rover_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'RequestBundleRoverCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_bundle'), 'RequestBundleRoverCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='RequestBundleRoverCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverBundleClient(config, service_endpoint=service_endpoint)
            response = client.request_bundle_rover_cluster(
                request_rover_bundle_details=request.pop(util.camelize('RequestRoverBundleDetails')),
                rover_cluster_id=request.pop(util.camelize('roverClusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'RequestBundleRoverCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'request_bundle_rover_cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_request_bundle_rover_node(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'RequestBundleRoverNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_bundle'), 'RequestBundleRoverNode')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='RequestBundleRoverNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverBundleClient(config, service_endpoint=service_endpoint)
            response = client.request_bundle_rover_node(
                request_rover_bundle_details=request.pop(util.camelize('RequestRoverBundleDetails')),
                rover_node_id=request.pop(util.camelize('roverNodeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'RequestBundleRoverNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'request_bundle_rover_node',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_retrieve_available_bundle_versions_rover_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'RetrieveAvailableBundleVersionsRoverCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_bundle'), 'RetrieveAvailableBundleVersionsRoverCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='RetrieveAvailableBundleVersionsRoverCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverBundleClient(config, service_endpoint=service_endpoint)
            response = client.retrieve_available_bundle_versions_rover_cluster(
                current_rover_bundle_details=request.pop(util.camelize('CurrentRoverBundleDetails')),
                rover_cluster_id=request.pop(util.camelize('roverClusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'RetrieveAvailableBundleVersionsRoverCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverBundleVersion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_retrieve_available_bundle_versions_rover_node(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'RetrieveAvailableBundleVersionsRoverNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_bundle'), 'RetrieveAvailableBundleVersionsRoverNode')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='RetrieveAvailableBundleVersionsRoverNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverBundleClient(config, service_endpoint=service_endpoint)
            response = client.retrieve_available_bundle_versions_rover_node(
                current_rover_bundle_details=request.pop(util.camelize('CurrentRoverBundleDetails')),
                rover_node_id=request.pop(util.camelize('roverNodeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'RetrieveAvailableBundleVersionsRoverNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverBundleVersion',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_retrieve_bundle_status_rover_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'RetrieveBundleStatusRoverCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_bundle'), 'RetrieveBundleStatusRoverCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='RetrieveBundleStatusRoverCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverBundleClient(config, service_endpoint=service_endpoint)
            response = client.retrieve_bundle_status_rover_cluster(
                rover_bundle_status_details=request.pop(util.camelize('RoverBundleStatusDetails')),
                rover_cluster_id=request.pop(util.camelize('roverClusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'RetrieveBundleStatusRoverCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverBundleStatus',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_retrieve_bundle_status_rover_node(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'RetrieveBundleStatusRoverNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_bundle'), 'RetrieveBundleStatusRoverNode')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='RetrieveBundleStatusRoverNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverBundleClient(config, service_endpoint=service_endpoint)
            response = client.retrieve_bundle_status_rover_node(
                rover_bundle_status_details=request.pop(util.camelize('RoverBundleStatusDetails')),
                rover_node_id=request.pop(util.camelize('roverNodeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'RetrieveBundleStatusRoverNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverBundleStatus',
            False,
            False
        )
