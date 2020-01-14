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

        cassette_location = os.path.join('generated', 'oda_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_change_oda_instance_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ChangeOdaInstanceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('oda'), 'ChangeOdaInstanceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ChangeOdaInstanceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdaClient(config, service_endpoint=service_endpoint)
            response = client.change_oda_instance_compartment(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                change_oda_instance_compartment_details=request.pop(util.camelize('ChangeOdaInstanceCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ChangeOdaInstanceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_oda_instance_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_create_oda_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'CreateOdaInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('oda'), 'CreateOdaInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='CreateOdaInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdaClient(config, service_endpoint=service_endpoint)
            response = client.create_oda_instance(
                create_oda_instance_details=request.pop(util.camelize('CreateOdaInstanceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'CreateOdaInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'odaInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_delete_oda_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'DeleteOdaInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('oda'), 'DeleteOdaInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='DeleteOdaInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdaClient(config, service_endpoint=service_endpoint)
            response = client.delete_oda_instance(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'DeleteOdaInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_oda_instance',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_get_oda_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'GetOdaInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('oda'), 'GetOdaInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='GetOdaInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdaClient(config, service_endpoint=service_endpoint)
            response = client.get_oda_instance(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'GetOdaInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'odaInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('oda'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdaClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_list_oda_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ListOdaInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('oda'), 'ListOdaInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ListOdaInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdaClient(config, service_endpoint=service_endpoint)
            response = client.list_oda_instances(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_oda_instances(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_oda_instances(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'ListOdaInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'odaInstanceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('oda'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdaClient(config, service_endpoint=service_endpoint)
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
            'oda',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('oda'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdaClient(config, service_endpoint=service_endpoint)
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
            'oda',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('oda'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdaClient(config, service_endpoint=service_endpoint)
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
            'oda',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_start_oda_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'StartOdaInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('oda'), 'StartOdaInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='StartOdaInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdaClient(config, service_endpoint=service_endpoint)
            response = client.start_oda_instance(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'StartOdaInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_oda_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_stop_oda_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'StopOdaInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('oda'), 'StopOdaInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='StopOdaInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdaClient(config, service_endpoint=service_endpoint)
            response = client.stop_oda_instance(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'StopOdaInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stop_oda_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="omce_devops_hybrid_us_grp@oracle.com" jiraProject="ODA" opsJiraProject="ODA"
def test_update_oda_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('oda', 'UpdateOdaInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('oda', util.camelize('oda'), 'UpdateOdaInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='oda', api_name='UpdateOdaInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.oda.OdaClient(config, service_endpoint=service_endpoint)
            response = client.update_oda_instance(
                oda_instance_id=request.pop(util.camelize('odaInstanceId')),
                update_oda_instance_details=request.pop(util.camelize('UpdateOdaInstanceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'oda',
            'UpdateOdaInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'odaInstance',
            False,
            False
        )
