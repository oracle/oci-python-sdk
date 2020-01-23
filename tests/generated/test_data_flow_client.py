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

        cassette_location = os.path.join('generated', 'data_flow_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_create_application(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'CreateApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'CreateApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='CreateApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.create_application(
                create_application_details=request.pop(util.camelize('CreateApplicationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'CreateApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'application',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_create_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'CreateRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'CreateRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='CreateRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.create_run(
                create_run_details=request.pop(util.camelize('CreateRunDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'CreateRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'run',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_delete_application(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'DeleteApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'DeleteApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='DeleteApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.delete_application(
                application_id=request.pop(util.camelize('applicationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'DeleteApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_application',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_delete_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'DeleteRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'DeleteRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='DeleteRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.delete_run(
                run_id=request.pop(util.camelize('runId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'DeleteRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_run',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_get_application(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'GetApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'GetApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='GetApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.get_application(
                application_id=request.pop(util.camelize('applicationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'GetApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'application',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_get_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'GetRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'GetRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='GetRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.get_run(
                run_id=request.pop(util.camelize('runId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'GetRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'run',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_get_run_log(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'GetRunLog'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'GetRunLog')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='GetRunLog')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.get_run_log(
                run_id=request.pop(util.camelize('runId')),
                name=request.pop(util.camelize('name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'GetRunLog',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_list_applications(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ListApplications'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ListApplications')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ListApplications')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.list_applications(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_applications(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_applications(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'ListApplications',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'applicationSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_list_run_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ListRunLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ListRunLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ListRunLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.list_run_logs(
                run_id=request.pop(util.camelize('runId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_run_logs(
                    run_id=request.pop(util.camelize('runId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_run_logs(
                        run_id=request.pop(util.camelize('runId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'ListRunLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'runLogSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_list_runs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'ListRuns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'ListRuns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='ListRuns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.list_runs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_runs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_runs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'ListRuns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'runSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_update_application(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'UpdateApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'UpdateApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='UpdateApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.update_application(
                update_application_details=request.pop(util.camelize('UpdateApplicationDetails')),
                application_id=request.pop(util.camelize('applicationId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'UpdateApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'application',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sss_dev_ww_grp@oracle.com" jiraProject="SSS" opsJiraProject="SSS"
def test_update_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_flow', 'UpdateRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_flow', util.camelize('data_flow'), 'UpdateRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_flow', api_name='UpdateRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_flow.DataFlowClient(config, service_endpoint=service_endpoint)
            response = client.update_run(
                update_run_details=request.pop(util.camelize('UpdateRunDetails')),
                run_id=request.pop(util.camelize('runId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_flow',
            'UpdateRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'run',
            False,
            False
        )
