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

        cassette_location = os.path.join('generated', 'fusion_apps_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_change_fusion_environment_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'ChangeFusionEnvironmentCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'ChangeFusionEnvironmentCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='ChangeFusionEnvironmentCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.change_fusion_environment_compartment(
                fusion_environment_id=request.pop(util.camelize('fusionEnvironmentId')),
                change_fusion_environment_compartment_details=request.pop(util.camelize('ChangeFusionEnvironmentCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'ChangeFusionEnvironmentCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_fusion_environment_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_create_fusion_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'CreateFusionEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'CreateFusionEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='CreateFusionEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.create_fusion_environment(
                create_fusion_environment_details=request.pop(util.camelize('CreateFusionEnvironmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'CreateFusionEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_fusion_environment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_create_fusion_environment_admin_user(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'CreateFusionEnvironmentAdminUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'CreateFusionEnvironmentAdminUser')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='CreateFusionEnvironmentAdminUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.create_fusion_environment_admin_user(
                create_fusion_environment_admin_user_details=request.pop(util.camelize('CreateFusionEnvironmentAdminUserDetails')),
                fusion_environment_id=request.pop(util.camelize('fusionEnvironmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'CreateFusionEnvironmentAdminUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_fusion_environment_admin_user',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_delete_fusion_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'DeleteFusionEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'DeleteFusionEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='DeleteFusionEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.delete_fusion_environment(
                fusion_environment_id=request.pop(util.camelize('fusionEnvironmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'DeleteFusionEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_fusion_environment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_delete_fusion_environment_admin_user(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'DeleteFusionEnvironmentAdminUser'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'DeleteFusionEnvironmentAdminUser')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='DeleteFusionEnvironmentAdminUser')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.delete_fusion_environment_admin_user(
                admin_username=request.pop(util.camelize('adminUsername')),
                fusion_environment_id=request.pop(util.camelize('fusionEnvironmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'DeleteFusionEnvironmentAdminUser',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_fusion_environment_admin_user',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_get_fusion_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'GetFusionEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'GetFusionEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='GetFusionEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.get_fusion_environment(
                fusion_environment_id=request.pop(util.camelize('fusionEnvironmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'GetFusionEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fusionEnvironment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_get_fusion_environment_status(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'GetFusionEnvironmentStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'GetFusionEnvironmentStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='GetFusionEnvironmentStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.get_fusion_environment_status(
                fusion_environment_id=request.pop(util.camelize('fusionEnvironmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'GetFusionEnvironmentStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fusionEnvironmentStatus',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_list_admin_users(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'ListAdminUsers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'ListAdminUsers')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='ListAdminUsers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.list_admin_users(
                fusion_environment_id=request.pop(util.camelize('fusionEnvironmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'ListAdminUsers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'adminUserCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_list_fusion_environments(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'ListFusionEnvironments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'ListFusionEnvironments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='ListFusionEnvironments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.list_fusion_environments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_fusion_environments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_fusion_environments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'ListFusionEnvironments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fusionEnvironmentCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
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
            'fusion_apps',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
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
            'fusion_apps',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
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
            'fusion_apps',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_reset_fusion_environment_password(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'ResetFusionEnvironmentPassword'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'ResetFusionEnvironmentPassword')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='ResetFusionEnvironmentPassword')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.reset_fusion_environment_password(
                reset_fusion_environment_password_details=request.pop(util.camelize('ResetFusionEnvironmentPasswordDetails')),
                fusion_environment_id=request.pop(util.camelize('fusionEnvironmentId')),
                admin_username=request.pop(util.camelize('adminUsername')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'ResetFusionEnvironmentPassword',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'reset_fusion_environment_password',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="fa-control-plane_us_grp@oracle.com" jiraProject="FACP" opsJiraProject="FACP"
def test_update_fusion_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('fusion_apps', 'UpdateFusionEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('fusion_apps', util.camelize('fusion_environment'), 'UpdateFusionEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='fusion_apps', api_name='UpdateFusionEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.fusion_apps.FusionEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.update_fusion_environment(
                fusion_environment_id=request.pop(util.camelize('fusionEnvironmentId')),
                update_fusion_environment_details=request.pop(util.camelize('UpdateFusionEnvironmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'fusion_apps',
            'UpdateFusionEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_fusion_environment',
            False,
            False
        )
