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

        cassette_location = os.path.join('generated', 'sch_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="och_us-grp@oracle.com" jiraProject="OCH" opsJiraProject="OCH"
def test_activate_service_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('sch', 'ActivateServiceConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('sch', util.camelize('service_connector'), 'ActivateServiceConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='sch', api_name='ActivateServiceConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.sch.ServiceConnectorClient(config, service_endpoint=service_endpoint)
            response = client.activate_service_connector(
                service_connector_id=request.pop(util.camelize('serviceConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'sch',
            'ActivateServiceConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'activate_service_connector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="och_us-grp@oracle.com" jiraProject="OCH" opsJiraProject="OCH"
def test_change_service_connector_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('sch', 'ChangeServiceConnectorCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('sch', util.camelize('service_connector'), 'ChangeServiceConnectorCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='sch', api_name='ChangeServiceConnectorCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.sch.ServiceConnectorClient(config, service_endpoint=service_endpoint)
            response = client.change_service_connector_compartment(
                service_connector_id=request.pop(util.camelize('serviceConnectorId')),
                change_service_connector_compartment_details=request.pop(util.camelize('ChangeServiceConnectorCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'sch',
            'ChangeServiceConnectorCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_service_connector_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="och_us-grp@oracle.com" jiraProject="OCH" opsJiraProject="OCH"
def test_create_service_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('sch', 'CreateServiceConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('sch', util.camelize('service_connector'), 'CreateServiceConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='sch', api_name='CreateServiceConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.sch.ServiceConnectorClient(config, service_endpoint=service_endpoint)
            response = client.create_service_connector(
                create_service_connector_details=request.pop(util.camelize('CreateServiceConnectorDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'sch',
            'CreateServiceConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_service_connector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="och_us-grp@oracle.com" jiraProject="OCH" opsJiraProject="OCH"
def test_deactivate_service_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('sch', 'DeactivateServiceConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('sch', util.camelize('service_connector'), 'DeactivateServiceConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='sch', api_name='DeactivateServiceConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.sch.ServiceConnectorClient(config, service_endpoint=service_endpoint)
            response = client.deactivate_service_connector(
                service_connector_id=request.pop(util.camelize('serviceConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'sch',
            'DeactivateServiceConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deactivate_service_connector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="och_us-grp@oracle.com" jiraProject="OCH" opsJiraProject="OCH"
def test_delete_service_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('sch', 'DeleteServiceConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('sch', util.camelize('service_connector'), 'DeleteServiceConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='sch', api_name='DeleteServiceConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.sch.ServiceConnectorClient(config, service_endpoint=service_endpoint)
            response = client.delete_service_connector(
                service_connector_id=request.pop(util.camelize('serviceConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'sch',
            'DeleteServiceConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_service_connector',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="och_us-grp@oracle.com" jiraProject="OCH" opsJiraProject="OCH"
def test_get_service_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('sch', 'GetServiceConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('sch', util.camelize('service_connector'), 'GetServiceConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='sch', api_name='GetServiceConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.sch.ServiceConnectorClient(config, service_endpoint=service_endpoint)
            response = client.get_service_connector(
                service_connector_id=request.pop(util.camelize('serviceConnectorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'sch',
            'GetServiceConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceConnector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="och_us-grp@oracle.com" jiraProject="OCH" opsJiraProject="OCH"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('sch', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('sch', util.camelize('service_connector'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='sch', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.sch.ServiceConnectorClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'sch',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="och_us-grp@oracle.com" jiraProject="OCH" opsJiraProject="OCH"
def test_list_service_connectors(testing_service_client):
    if not testing_service_client.is_api_enabled('sch', 'ListServiceConnectors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('sch', util.camelize('service_connector'), 'ListServiceConnectors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='sch', api_name='ListServiceConnectors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.sch.ServiceConnectorClient(config, service_endpoint=service_endpoint)
            response = client.list_service_connectors(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_service_connectors(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_service_connectors(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'sch',
            'ListServiceConnectors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'serviceConnectorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="och_us-grp@oracle.com" jiraProject="OCH" opsJiraProject="OCH"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('sch', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('sch', util.camelize('service_connector'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='sch', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.sch.ServiceConnectorClient(config, service_endpoint=service_endpoint)
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
            'sch',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="och_us-grp@oracle.com" jiraProject="OCH" opsJiraProject="OCH"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('sch', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('sch', util.camelize('service_connector'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='sch', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.sch.ServiceConnectorClient(config, service_endpoint=service_endpoint)
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
            'sch',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="och_us-grp@oracle.com" jiraProject="OCH" opsJiraProject="OCH"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('sch', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('sch', util.camelize('service_connector'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='sch', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.sch.ServiceConnectorClient(config, service_endpoint=service_endpoint)
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
            'sch',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="och_us-grp@oracle.com" jiraProject="OCH" opsJiraProject="OCH"
def test_update_service_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('sch', 'UpdateServiceConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('sch', util.camelize('service_connector'), 'UpdateServiceConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='sch', api_name='UpdateServiceConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.sch.ServiceConnectorClient(config, service_endpoint=service_endpoint)
            response = client.update_service_connector(
                service_connector_id=request.pop(util.camelize('serviceConnectorId')),
                update_service_connector_details=request.pop(util.camelize('UpdateServiceConnectorDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'sch',
            'UpdateServiceConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_service_connector',
            False,
            False
        )
