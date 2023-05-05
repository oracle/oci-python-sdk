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

        cassette_location = os.path.join('generated', 'access_governance_cp_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_agcs_ww_grp@oracle.com" jiraProject="AGCS" opsJiraProject="AGCS"
def test_change_governance_instance_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('access_governance_cp', 'ChangeGovernanceInstanceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('access_governance_cp', util.camelize('access_governance_cp'), 'ChangeGovernanceInstanceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='access_governance_cp', api_name='ChangeGovernanceInstanceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.access_governance_cp.AccessGovernanceCPClient(config, service_endpoint=service_endpoint)
            response = client.change_governance_instance_compartment(
                governance_instance_id=request.pop(util.camelize('governanceInstanceId')),
                change_governance_instance_compartment_details=request.pop(util.camelize('ChangeGovernanceInstanceCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'access_governance_cp',
            'ChangeGovernanceInstanceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_governance_instance_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_agcs_ww_grp@oracle.com" jiraProject="AGCS" opsJiraProject="AGCS"
def test_create_governance_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('access_governance_cp', 'CreateGovernanceInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('access_governance_cp', util.camelize('access_governance_cp'), 'CreateGovernanceInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='access_governance_cp', api_name='CreateGovernanceInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.access_governance_cp.AccessGovernanceCPClient(config, service_endpoint=service_endpoint)
            response = client.create_governance_instance(
                create_governance_instance_details=request.pop(util.camelize('CreateGovernanceInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'access_governance_cp',
            'CreateGovernanceInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'governanceInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_agcs_ww_grp@oracle.com" jiraProject="AGCS" opsJiraProject="AGCS"
def test_delete_governance_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('access_governance_cp', 'DeleteGovernanceInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('access_governance_cp', util.camelize('access_governance_cp'), 'DeleteGovernanceInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='access_governance_cp', api_name='DeleteGovernanceInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.access_governance_cp.AccessGovernanceCPClient(config, service_endpoint=service_endpoint)
            response = client.delete_governance_instance(
                governance_instance_id=request.pop(util.camelize('governanceInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'access_governance_cp',
            'DeleteGovernanceInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_governance_instance',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_agcs_ww_grp@oracle.com" jiraProject="AGCS" opsJiraProject="AGCS"
def test_get_governance_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('access_governance_cp', 'GetGovernanceInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('access_governance_cp', util.camelize('access_governance_cp'), 'GetGovernanceInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='access_governance_cp', api_name='GetGovernanceInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.access_governance_cp.AccessGovernanceCPClient(config, service_endpoint=service_endpoint)
            response = client.get_governance_instance(
                governance_instance_id=request.pop(util.camelize('governanceInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'access_governance_cp',
            'GetGovernanceInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'governanceInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_agcs_ww_grp@oracle.com" jiraProject="AGCS" opsJiraProject="AGCS"
def test_get_governance_instance_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('access_governance_cp', 'GetGovernanceInstanceConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('access_governance_cp', util.camelize('access_governance_cp'), 'GetGovernanceInstanceConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='access_governance_cp', api_name='GetGovernanceInstanceConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.access_governance_cp.AccessGovernanceCPClient(config, service_endpoint=service_endpoint)
            response = client.get_governance_instance_configuration(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'access_governance_cp',
            'GetGovernanceInstanceConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'governanceInstanceConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_agcs_ww_grp@oracle.com" jiraProject="AGCS" opsJiraProject="AGCS"
def test_list_governance_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('access_governance_cp', 'ListGovernanceInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('access_governance_cp', util.camelize('access_governance_cp'), 'ListGovernanceInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='access_governance_cp', api_name='ListGovernanceInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.access_governance_cp.AccessGovernanceCPClient(config, service_endpoint=service_endpoint)
            response = client.list_governance_instances(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_governance_instances(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_governance_instances(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'access_governance_cp',
            'ListGovernanceInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'governanceInstanceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_agcs_ww_grp@oracle.com" jiraProject="AGCS" opsJiraProject="AGCS"
def test_update_governance_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('access_governance_cp', 'UpdateGovernanceInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('access_governance_cp', util.camelize('access_governance_cp'), 'UpdateGovernanceInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='access_governance_cp', api_name='UpdateGovernanceInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.access_governance_cp.AccessGovernanceCPClient(config, service_endpoint=service_endpoint)
            response = client.update_governance_instance(
                update_governance_instance_details=request.pop(util.camelize('UpdateGovernanceInstanceDetails')),
                governance_instance_id=request.pop(util.camelize('governanceInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'access_governance_cp',
            'UpdateGovernanceInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'governanceInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_agcs_ww_grp@oracle.com" jiraProject="AGCS" opsJiraProject="AGCS"
def test_update_governance_instance_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('access_governance_cp', 'UpdateGovernanceInstanceConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('access_governance_cp', util.camelize('access_governance_cp'), 'UpdateGovernanceInstanceConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='access_governance_cp', api_name='UpdateGovernanceInstanceConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.access_governance_cp.AccessGovernanceCPClient(config, service_endpoint=service_endpoint)
            response = client.update_governance_instance_configuration(
                update_governance_instance_configuration_details=request.pop(util.camelize('UpdateGovernanceInstanceConfigurationDetails')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'access_governance_cp',
            'UpdateGovernanceInstanceConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'governanceInstanceConfiguration',
            False,
            False
        )
