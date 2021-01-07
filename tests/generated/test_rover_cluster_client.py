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

        cassette_location = os.path.join('generated', 'rover_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_rover_cluster_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'ChangeRoverClusterCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_cluster'), 'ChangeRoverClusterCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='ChangeRoverClusterCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverClusterClient(config, service_endpoint=service_endpoint)
            response = client.change_rover_cluster_compartment(
                rover_cluster_id=request.pop(util.camelize('roverClusterId')),
                change_rover_cluster_compartment_details=request.pop(util.camelize('ChangeRoverClusterCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'ChangeRoverClusterCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_rover_cluster_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_rover_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'CreateRoverCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_cluster'), 'CreateRoverCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='CreateRoverCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverClusterClient(config, service_endpoint=service_endpoint)
            response = client.create_rover_cluster(
                create_rover_cluster_details=request.pop(util.camelize('CreateRoverClusterDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'CreateRoverCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverCluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_rover_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'DeleteRoverCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_cluster'), 'DeleteRoverCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='DeleteRoverCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverClusterClient(config, service_endpoint=service_endpoint)
            response = client.delete_rover_cluster(
                rover_cluster_id=request.pop(util.camelize('roverClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'DeleteRoverCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_rover_cluster',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_rover_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'GetRoverCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_cluster'), 'GetRoverCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='GetRoverCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverClusterClient(config, service_endpoint=service_endpoint)
            response = client.get_rover_cluster(
                rover_cluster_id=request.pop(util.camelize('roverClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'GetRoverCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverCluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_rover_cluster_certificate(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'GetRoverClusterCertificate'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_cluster'), 'GetRoverClusterCertificate')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='GetRoverClusterCertificate')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverClusterClient(config, service_endpoint=service_endpoint)
            response = client.get_rover_cluster_certificate(
                rover_cluster_id=request.pop(util.camelize('roverClusterId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'GetRoverClusterCertificate',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverClusterCertificate',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_rover_clusters(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'ListRoverClusters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_cluster'), 'ListRoverClusters')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='ListRoverClusters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverClusterClient(config, service_endpoint=service_endpoint)
            response = client.list_rover_clusters(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_rover_clusters(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_rover_clusters(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'ListRoverClusters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverClusterCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="edge_rover_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_rover_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('rover', 'UpdateRoverCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('rover', util.camelize('rover_cluster'), 'UpdateRoverCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='rover', api_name='UpdateRoverCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.rover.RoverClusterClient(config, service_endpoint=service_endpoint)
            response = client.update_rover_cluster(
                rover_cluster_id=request.pop(util.camelize('roverClusterId')),
                update_rover_cluster_details=request.pop(util.camelize('UpdateRoverClusterDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'rover',
            'UpdateRoverCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'roverCluster',
            False,
            False
        )
