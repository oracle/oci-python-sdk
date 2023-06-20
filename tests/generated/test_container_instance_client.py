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

        cassette_location = os.path.join('generated', 'container_instances_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_change_container_instance_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'ChangeContainerInstanceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'ChangeContainerInstanceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='ChangeContainerInstanceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.change_container_instance_compartment(
                container_instance_id=request.pop(util.camelize('containerInstanceId')),
                change_container_instance_compartment_details=request.pop(util.camelize('ChangeContainerInstanceCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'ChangeContainerInstanceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_container_instance_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_create_container_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'CreateContainerInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'CreateContainerInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='CreateContainerInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.create_container_instance(
                create_container_instance_details=request.pop(util.camelize('CreateContainerInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'CreateContainerInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_delete_container_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'DeleteContainerInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'DeleteContainerInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='DeleteContainerInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.delete_container_instance(
                container_instance_id=request.pop(util.camelize('containerInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'DeleteContainerInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_container_instance',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_get_container(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'GetContainer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'GetContainer')
    )

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='GetContainer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.get_container(
                container_id=request.pop(util.camelize('containerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'GetContainer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'container',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_get_container_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'GetContainerInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'GetContainerInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='GetContainerInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.get_container_instance(
                container_instance_id=request.pop(util.camelize('containerInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'GetContainerInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_list_container_instance_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'ListContainerInstanceShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'ListContainerInstanceShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='ListContainerInstanceShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_container_instance_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_container_instance_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_container_instance_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'ListContainerInstanceShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerInstanceShapeCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_list_container_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'ListContainerInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'ListContainerInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='ListContainerInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_container_instances(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_container_instances(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_container_instances(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'ListContainerInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerInstanceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_list_containers(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'ListContainers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'ListContainers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='ListContainers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_containers(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_containers(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_containers(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'ListContainers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'containerCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_restart_container_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'RestartContainerInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'RestartContainerInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='RestartContainerInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.restart_container_instance(
                container_instance_id=request.pop(util.camelize('containerInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'RestartContainerInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'restart_container_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_retrieve_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'RetrieveLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'RetrieveLogs')
    )

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='RetrieveLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.retrieve_logs(
                container_id=request.pop(util.camelize('containerId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'RetrieveLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_start_container_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'StartContainerInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'StartContainerInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='StartContainerInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.start_container_instance(
                container_instance_id=request.pop(util.camelize('containerInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'StartContainerInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_container_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_stop_container_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'StopContainerInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'StopContainerInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='StopContainerInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.stop_container_instance(
                container_instance_id=request.pop(util.camelize('containerInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'StopContainerInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stop_container_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_update_container(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'UpdateContainer'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'UpdateContainer')
    )

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='UpdateContainer')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.update_container(
                container_id=request.pop(util.camelize('containerId')),
                update_container_details=request.pop(util.camelize('UpdateContainerDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'UpdateContainer',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_container',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="container_vm_control_plane_grp@oracle.com" jiraProject="CVM" opsJiraProject="CVMS"
def test_update_container_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('container_instances', 'UpdateContainerInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_instances', util.camelize('container_instance'), 'UpdateContainerInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='container_instances', api_name='UpdateContainerInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_instances.ContainerInstanceClient(config, service_endpoint=service_endpoint)
            response = client.update_container_instance(
                container_instance_id=request.pop(util.camelize('containerInstanceId')),
                update_container_instance_details=request.pop(util.camelize('UpdateContainerInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_instances',
            'UpdateContainerInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_container_instance',
            False,
            False
        )