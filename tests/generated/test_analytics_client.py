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

        cassette_location = os.path.join('generated', 'analytics_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_change_analytics_instance_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'ChangeAnalyticsInstanceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'ChangeAnalyticsInstanceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='ChangeAnalyticsInstanceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.change_analytics_instance_compartment(
                analytics_instance_id=request.pop(util.camelize('analyticsInstanceId')),
                change_compartment_details=request.pop(util.camelize('ChangeCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'analytics',
            'ChangeAnalyticsInstanceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_analytics_instance_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_create_analytics_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'CreateAnalyticsInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'CreateAnalyticsInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='CreateAnalyticsInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.create_analytics_instance(
                create_analytics_instance_details=request.pop(util.camelize('CreateAnalyticsInstanceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'analytics',
            'CreateAnalyticsInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'analyticsInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_delete_analytics_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'DeleteAnalyticsInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'DeleteAnalyticsInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='DeleteAnalyticsInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_analytics_instance(
                analytics_instance_id=request.pop(util.camelize('analyticsInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'analytics',
            'DeleteAnalyticsInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_analytics_instance',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_delete_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'DeleteWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'DeleteWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='DeleteWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.delete_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'analytics',
            'DeleteWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_get_analytics_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'GetAnalyticsInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'GetAnalyticsInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='GetAnalyticsInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_analytics_instance(
                analytics_instance_id=request.pop(util.camelize('analyticsInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'analytics',
            'GetAnalyticsInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'analyticsInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'analytics',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_list_analytics_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'ListAnalyticsInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'ListAnalyticsInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='ListAnalyticsInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.list_analytics_instances(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_analytics_instances(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_analytics_instances(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'analytics',
            'ListAnalyticsInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'analyticsInstanceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
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
            'analytics',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
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
            'analytics',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLog',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
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
            'analytics',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_scale_analytics_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'ScaleAnalyticsInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'ScaleAnalyticsInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='ScaleAnalyticsInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.scale_analytics_instance(
                analytics_instance_id=request.pop(util.camelize('analyticsInstanceId')),
                scale_analytics_instance_details=request.pop(util.camelize('ScaleAnalyticsInstanceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'analytics',
            'ScaleAnalyticsInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scale_analytics_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_start_analytics_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'StartAnalyticsInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'StartAnalyticsInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='StartAnalyticsInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.start_analytics_instance(
                analytics_instance_id=request.pop(util.camelize('analyticsInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'analytics',
            'StartAnalyticsInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_analytics_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_stop_analytics_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'StopAnalyticsInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'StopAnalyticsInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='StopAnalyticsInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.stop_analytics_instance(
                analytics_instance_id=request.pop(util.camelize('analyticsInstanceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'analytics',
            'StopAnalyticsInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stop_analytics_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_oac_ww_grp@oracle.com" jiraProject="OB" opsJiraProject="AOAC"
def test_update_analytics_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('analytics', 'UpdateAnalyticsInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('analytics', util.camelize('analytics'), 'UpdateAnalyticsInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='analytics', api_name='UpdateAnalyticsInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.analytics.AnalyticsClient(config, service_endpoint=service_endpoint)
            response = client.update_analytics_instance(
                analytics_instance_id=request.pop(util.camelize('analyticsInstanceId')),
                update_analytics_instance_details=request.pop(util.camelize('UpdateAnalyticsInstanceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'analytics',
            'UpdateAnalyticsInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'analyticsInstance',
            False,
            False
        )
