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

        cassette_location = os.path.join('generated', 'integration_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="&lt;tbd&gt;_ww@oracle.com" jiraProject="&lt;tbc&gt;" opsJiraProject="&lt;tbd&gt;"
def test_change_integration_instance_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('integration', 'ChangeIntegrationInstanceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('integration', util.camelize('integration_instance'), 'ChangeIntegrationInstanceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='integration', api_name='ChangeIntegrationInstanceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.integration.IntegrationInstanceClient(config, service_endpoint=service_endpoint)
            response = client.change_integration_instance_compartment(
                integration_instance_id=request.pop(util.camelize('integrationInstanceId')),
                change_integration_instance_compartment_details=request.pop(util.camelize('ChangeIntegrationInstanceCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'integration',
            'ChangeIntegrationInstanceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_integration_instance_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="&lt;tbd&gt;_ww@oracle.com" jiraProject="&lt;tbc&gt;" opsJiraProject="&lt;tbd&gt;"
def test_change_integration_instance_network_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('integration', 'ChangeIntegrationInstanceNetworkEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('integration', util.camelize('integration_instance'), 'ChangeIntegrationInstanceNetworkEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='integration', api_name='ChangeIntegrationInstanceNetworkEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.integration.IntegrationInstanceClient(config, service_endpoint=service_endpoint)
            response = client.change_integration_instance_network_endpoint(
                integration_instance_id=request.pop(util.camelize('integrationInstanceId')),
                change_integration_instance_network_endpoint_details=request.pop(util.camelize('ChangeIntegrationInstanceNetworkEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'integration',
            'ChangeIntegrationInstanceNetworkEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_integration_instance_network_endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="&lt;tbd&gt;_ww@oracle.com" jiraProject="&lt;tbc&gt;" opsJiraProject="&lt;tbd&gt;"
def test_create_integration_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('integration', 'CreateIntegrationInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('integration', util.camelize('integration_instance'), 'CreateIntegrationInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='integration', api_name='CreateIntegrationInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.integration.IntegrationInstanceClient(config, service_endpoint=service_endpoint)
            response = client.create_integration_instance(
                create_integration_instance_details=request.pop(util.camelize('CreateIntegrationInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'integration',
            'CreateIntegrationInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_integration_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="&lt;tbd&gt;_ww@oracle.com" jiraProject="&lt;tbc&gt;" opsJiraProject="&lt;tbd&gt;"
def test_delete_integration_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('integration', 'DeleteIntegrationInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('integration', util.camelize('integration_instance'), 'DeleteIntegrationInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='integration', api_name='DeleteIntegrationInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.integration.IntegrationInstanceClient(config, service_endpoint=service_endpoint)
            response = client.delete_integration_instance(
                integration_instance_id=request.pop(util.camelize('integrationInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'integration',
            'DeleteIntegrationInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_integration_instance',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="&lt;tbd&gt;_ww@oracle.com" jiraProject="&lt;tbc&gt;" opsJiraProject="&lt;tbd&gt;"
def test_get_integration_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('integration', 'GetIntegrationInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('integration', util.camelize('integration_instance'), 'GetIntegrationInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='integration', api_name='GetIntegrationInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.integration.IntegrationInstanceClient(config, service_endpoint=service_endpoint)
            response = client.get_integration_instance(
                integration_instance_id=request.pop(util.camelize('integrationInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'integration',
            'GetIntegrationInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'integrationInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="&lt;tbd&gt;_ww@oracle.com" jiraProject="&lt;tbc&gt;" opsJiraProject="&lt;tbd&gt;"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('integration', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('integration', util.camelize('integration_instance'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='integration', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.integration.IntegrationInstanceClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'integration',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="&lt;tbd&gt;_ww@oracle.com" jiraProject="&lt;tbc&gt;" opsJiraProject="&lt;tbd&gt;"
def test_list_integration_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('integration', 'ListIntegrationInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('integration', util.camelize('integration_instance'), 'ListIntegrationInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='integration', api_name='ListIntegrationInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.integration.IntegrationInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_integration_instances(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_integration_instances(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_integration_instances(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'integration',
            'ListIntegrationInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'integrationInstanceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="&lt;tbd&gt;_ww@oracle.com" jiraProject="&lt;tbc&gt;" opsJiraProject="&lt;tbd&gt;"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('integration', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('integration', util.camelize('integration_instance'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='integration', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.integration.IntegrationInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                compartment_id=request.pop(util.camelize('compartmentId')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    compartment_id=request.pop(util.camelize('compartmentId')),
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
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'integration',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="&lt;tbd&gt;_ww@oracle.com" jiraProject="&lt;tbc&gt;" opsJiraProject="&lt;tbd&gt;"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('integration', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('integration', util.camelize('integration_instance'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='integration', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.integration.IntegrationInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
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
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'integration',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="&lt;tbd&gt;_ww@oracle.com" jiraProject="&lt;tbc&gt;" opsJiraProject="&lt;tbd&gt;"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('integration', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('integration', util.camelize('integration_instance'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='integration', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.integration.IntegrationInstanceClient(config, service_endpoint=service_endpoint)
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
            'integration',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="&lt;tbd&gt;_ww@oracle.com" jiraProject="&lt;tbc&gt;" opsJiraProject="&lt;tbd&gt;"
def test_start_integration_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('integration', 'StartIntegrationInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('integration', util.camelize('integration_instance'), 'StartIntegrationInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='integration', api_name='StartIntegrationInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.integration.IntegrationInstanceClient(config, service_endpoint=service_endpoint)
            response = client.start_integration_instance(
                integration_instance_id=request.pop(util.camelize('integrationInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'integration',
            'StartIntegrationInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_integration_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="&lt;tbd&gt;_ww@oracle.com" jiraProject="&lt;tbc&gt;" opsJiraProject="&lt;tbd&gt;"
def test_stop_integration_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('integration', 'StopIntegrationInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('integration', util.camelize('integration_instance'), 'StopIntegrationInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='integration', api_name='StopIntegrationInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.integration.IntegrationInstanceClient(config, service_endpoint=service_endpoint)
            response = client.stop_integration_instance(
                integration_instance_id=request.pop(util.camelize('integrationInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'integration',
            'StopIntegrationInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stop_integration_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="&lt;tbd&gt;_ww@oracle.com" jiraProject="&lt;tbc&gt;" opsJiraProject="&lt;tbd&gt;"
def test_update_integration_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('integration', 'UpdateIntegrationInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('integration', util.camelize('integration_instance'), 'UpdateIntegrationInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='integration', api_name='UpdateIntegrationInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.integration.IntegrationInstanceClient(config, service_endpoint=service_endpoint)
            response = client.update_integration_instance(
                integration_instance_id=request.pop(util.camelize('integrationInstanceId')),
                update_integration_instance_details=request.pop(util.camelize('UpdateIntegrationInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'integration',
            'UpdateIntegrationInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_integration_instance',
            False,
            False
        )
