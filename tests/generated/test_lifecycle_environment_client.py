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

        cassette_location = os.path.join('generated', 'os_management_hub_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_attach_managed_instances_to_lifecycle_stage(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'AttachManagedInstancesToLifecycleStage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('lifecycle_environment'), 'AttachManagedInstancesToLifecycleStage')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='AttachManagedInstancesToLifecycleStage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.LifecycleEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.attach_managed_instances_to_lifecycle_stage(
                lifecycle_stage_id=request.pop(util.camelize('lifecycleStageId')),
                attach_managed_instances_to_lifecycle_stage_details=request.pop(util.camelize('AttachManagedInstancesToLifecycleStageDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'AttachManagedInstancesToLifecycleStage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attach_managed_instances_to_lifecycle_stage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_create_lifecycle_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'CreateLifecycleEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('lifecycle_environment'), 'CreateLifecycleEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='CreateLifecycleEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.LifecycleEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.create_lifecycle_environment(
                create_lifecycle_environment_details=request.pop(util.camelize('CreateLifecycleEnvironmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'CreateLifecycleEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'lifecycleEnvironment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_delete_lifecycle_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'DeleteLifecycleEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('lifecycle_environment'), 'DeleteLifecycleEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='DeleteLifecycleEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.LifecycleEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.delete_lifecycle_environment(
                lifecycle_environment_id=request.pop(util.camelize('lifecycleEnvironmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'DeleteLifecycleEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_lifecycle_environment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_detach_managed_instances_from_lifecycle_stage(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'DetachManagedInstancesFromLifecycleStage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('lifecycle_environment'), 'DetachManagedInstancesFromLifecycleStage')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='DetachManagedInstancesFromLifecycleStage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.LifecycleEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.detach_managed_instances_from_lifecycle_stage(
                lifecycle_stage_id=request.pop(util.camelize('lifecycleStageId')),
                detach_managed_instances_from_lifecycle_stage_details=request.pop(util.camelize('DetachManagedInstancesFromLifecycleStageDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'DetachManagedInstancesFromLifecycleStage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detach_managed_instances_from_lifecycle_stage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_get_lifecycle_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'GetLifecycleEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('lifecycle_environment'), 'GetLifecycleEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='GetLifecycleEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.LifecycleEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.get_lifecycle_environment(
                lifecycle_environment_id=request.pop(util.camelize('lifecycleEnvironmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'GetLifecycleEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'lifecycleEnvironment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_get_lifecycle_stage(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'GetLifecycleStage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('lifecycle_environment'), 'GetLifecycleStage')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='GetLifecycleStage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.LifecycleEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.get_lifecycle_stage(
                lifecycle_stage_id=request.pop(util.camelize('lifecycleStageId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'GetLifecycleStage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'lifecycleStage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_lifecycle_environments(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListLifecycleEnvironments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('lifecycle_environment'), 'ListLifecycleEnvironments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListLifecycleEnvironments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.LifecycleEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.list_lifecycle_environments(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_lifecycle_environments(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_lifecycle_environments(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListLifecycleEnvironments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'lifecycleEnvironmentCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_lifecycle_stage_installed_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListLifecycleStageInstalledPackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('lifecycle_environment'), 'ListLifecycleStageInstalledPackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListLifecycleStageInstalledPackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.LifecycleEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.list_lifecycle_stage_installed_packages(
                lifecycle_stage_id=request.pop(util.camelize('lifecycleStageId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_lifecycle_stage_installed_packages(
                    lifecycle_stage_id=request.pop(util.camelize('lifecycleStageId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_lifecycle_stage_installed_packages(
                        lifecycle_stage_id=request.pop(util.camelize('lifecycleStageId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListLifecycleStageInstalledPackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'installedPackageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_lifecycle_stages(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListLifecycleStages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('lifecycle_environment'), 'ListLifecycleStages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListLifecycleStages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.LifecycleEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.list_lifecycle_stages(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_lifecycle_stages(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_lifecycle_stages(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListLifecycleStages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'lifecycleStageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_promote_software_source_to_lifecycle_stage(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'PromoteSoftwareSourceToLifecycleStage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('lifecycle_environment'), 'PromoteSoftwareSourceToLifecycleStage')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='PromoteSoftwareSourceToLifecycleStage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.LifecycleEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.promote_software_source_to_lifecycle_stage(
                lifecycle_stage_id=request.pop(util.camelize('lifecycleStageId')),
                promote_software_source_to_lifecycle_stage_details=request.pop(util.camelize('PromoteSoftwareSourceToLifecycleStageDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'PromoteSoftwareSourceToLifecycleStage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'promote_software_source_to_lifecycle_stage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_update_lifecycle_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'UpdateLifecycleEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('lifecycle_environment'), 'UpdateLifecycleEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='UpdateLifecycleEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.LifecycleEnvironmentClient(config, service_endpoint=service_endpoint)
            response = client.update_lifecycle_environment(
                lifecycle_environment_id=request.pop(util.camelize('lifecycleEnvironmentId')),
                update_lifecycle_environment_details=request.pop(util.camelize('UpdateLifecycleEnvironmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'UpdateLifecycleEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'lifecycleEnvironment',
            False,
            False
        )
