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

        cassette_location = os.path.join('generated', 'data_safe_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_data_safe_private_endpoint_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeDataSafePrivateEndpointCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeDataSafePrivateEndpointCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeDataSafePrivateEndpointCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_data_safe_private_endpoint_compartment(
                data_safe_private_endpoint_id=request.pop(util.camelize('dataSafePrivateEndpointId')),
                change_data_safe_private_endpoint_compartment_details=request.pop(util.camelize('ChangeDataSafePrivateEndpointCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeDataSafePrivateEndpointCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_data_safe_private_endpoint_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_change_on_prem_connector_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ChangeOnPremConnectorCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ChangeOnPremConnectorCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ChangeOnPremConnectorCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.change_on_prem_connector_compartment(
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                change_on_prem_connector_compartment_details=request.pop(util.camelize('ChangeOnPremConnectorCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ChangeOnPremConnectorCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_on_prem_connector_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_data_safe_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateDataSafePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateDataSafePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateDataSafePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_data_safe_private_endpoint(
                create_data_safe_private_endpoint_details=request.pop(util.camelize('CreateDataSafePrivateEndpointDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateDataSafePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataSafePrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_create_on_prem_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'CreateOnPremConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'CreateOnPremConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='CreateOnPremConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.create_on_prem_connector(
                create_on_prem_connector_details=request.pop(util.camelize('CreateOnPremConnectorDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'CreateOnPremConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'onPremConnector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_data_safe_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteDataSafePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteDataSafePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteDataSafePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_data_safe_private_endpoint(
                data_safe_private_endpoint_id=request.pop(util.camelize('dataSafePrivateEndpointId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteDataSafePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_data_safe_private_endpoint',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_delete_on_prem_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'DeleteOnPremConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'DeleteOnPremConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='DeleteOnPremConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.delete_on_prem_connector(
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'DeleteOnPremConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_on_prem_connector',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_enable_data_safe_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'EnableDataSafeConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'EnableDataSafeConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='EnableDataSafeConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.enable_data_safe_configuration(
                enable_data_safe_configuration_details=request.pop(util.camelize('EnableDataSafeConfigurationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'EnableDataSafeConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enable_data_safe_configuration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_generate_on_prem_connector_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GenerateOnPremConnectorConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GenerateOnPremConnectorConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GenerateOnPremConnectorConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.generate_on_prem_connector_configuration(
                generate_on_prem_connector_configuration_details=request.pop(util.camelize('GenerateOnPremConnectorConfigurationDetails')),
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GenerateOnPremConnectorConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_data_safe_configuration(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetDataSafeConfiguration'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetDataSafeConfiguration')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetDataSafeConfiguration')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_data_safe_configuration(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetDataSafeConfiguration',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataSafeConfiguration',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_data_safe_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetDataSafePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetDataSafePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetDataSafePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_data_safe_private_endpoint(
                data_safe_private_endpoint_id=request.pop(util.camelize('dataSafePrivateEndpointId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetDataSafePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataSafePrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_on_prem_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetOnPremConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetOnPremConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetOnPremConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_on_prem_connector(
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetOnPremConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'onPremConnector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_data_safe_private_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListDataSafePrivateEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListDataSafePrivateEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListDataSafePrivateEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_data_safe_private_endpoints(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_safe_private_endpoints(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_safe_private_endpoints(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListDataSafePrivateEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataSafePrivateEndpointSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_on_prem_connectors(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListOnPremConnectors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListOnPremConnectors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListOnPremConnectors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_on_prem_connectors(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_on_prem_connectors(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_on_prem_connectors(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListOnPremConnectors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'onPremConnectorSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_data_safe_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateDataSafePrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateDataSafePrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateDataSafePrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_data_safe_private_endpoint(
                data_safe_private_endpoint_id=request.pop(util.camelize('dataSafePrivateEndpointId')),
                update_data_safe_private_endpoint_details=request.pop(util.camelize('UpdateDataSafePrivateEndpointDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateDataSafePrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_data_safe_private_endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_on_prem_connector(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateOnPremConnector'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateOnPremConnector')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateOnPremConnector')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_on_prem_connector(
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                update_on_prem_connector_details=request.pop(util.camelize('UpdateOnPremConnectorDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateOnPremConnector',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_on_prem_connector',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datasafe_dex_ww_grp@oracle.com" jiraProject="DS" opsJiraProject="ADS"
def test_update_on_prem_connector_wallet(testing_service_client):
    if not testing_service_client.is_api_enabled('data_safe', 'UpdateOnPremConnectorWallet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_safe', util.camelize('data_safe'), 'UpdateOnPremConnectorWallet')
    )

    request_containers = testing_service_client.get_requests(service_name='data_safe', api_name='UpdateOnPremConnectorWallet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_safe.DataSafeClient(config, service_endpoint=service_endpoint)
            response = client.update_on_prem_connector_wallet(
                update_on_prem_connector_wallet_details=request.pop(util.camelize('UpdateOnPremConnectorWalletDetails')),
                on_prem_connector_id=request.pop(util.camelize('onPremConnectorId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_safe',
            'UpdateOnPremConnectorWallet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_on_prem_connector_wallet',
            False,
            False
        )
