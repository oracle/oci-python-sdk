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
def test_attach_managed_instances_to_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'AttachManagedInstancesToManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'AttachManagedInstancesToManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='AttachManagedInstancesToManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.attach_managed_instances_to_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                attach_managed_instances_to_managed_instance_group_details=request.pop(util.camelize('AttachManagedInstancesToManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'AttachManagedInstancesToManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attach_managed_instances_to_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_attach_software_sources_to_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'AttachSoftwareSourcesToManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'AttachSoftwareSourcesToManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='AttachSoftwareSourcesToManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.attach_software_sources_to_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                attach_software_sources_to_managed_instance_group_details=request.pop(util.camelize('AttachSoftwareSourcesToManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'AttachSoftwareSourcesToManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attach_software_sources_to_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_create_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'CreateManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'CreateManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='CreateManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.create_managed_instance_group(
                create_managed_instance_group_details=request.pop(util.camelize('CreateManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'CreateManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_delete_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'DeleteManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'DeleteManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='DeleteManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.delete_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'DeleteManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_managed_instance_group',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_detach_managed_instances_from_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'DetachManagedInstancesFromManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'DetachManagedInstancesFromManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='DetachManagedInstancesFromManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.detach_managed_instances_from_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                detach_managed_instances_from_managed_instance_group_details=request.pop(util.camelize('DetachManagedInstancesFromManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'DetachManagedInstancesFromManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detach_managed_instances_from_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_detach_software_sources_from_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'DetachSoftwareSourcesFromManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'DetachSoftwareSourcesFromManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='DetachSoftwareSourcesFromManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.detach_software_sources_from_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                detach_software_sources_from_managed_instance_group_details=request.pop(util.camelize('DetachSoftwareSourcesFromManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'DetachSoftwareSourcesFromManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detach_software_sources_from_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_disable_module_stream_on_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'DisableModuleStreamOnManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'DisableModuleStreamOnManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='DisableModuleStreamOnManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.disable_module_stream_on_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                disable_module_stream_on_managed_instance_group_details=request.pop(util.camelize('DisableModuleStreamOnManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'DisableModuleStreamOnManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'disable_module_stream_on_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_enable_module_stream_on_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'EnableModuleStreamOnManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'EnableModuleStreamOnManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='EnableModuleStreamOnManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.enable_module_stream_on_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                enable_module_stream_on_managed_instance_group_details=request.pop(util.camelize('EnableModuleStreamOnManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'EnableModuleStreamOnManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enable_module_stream_on_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_get_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'GetManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'GetManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='GetManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.get_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'GetManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_install_module_stream_profile_on_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'InstallModuleStreamProfileOnManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'InstallModuleStreamProfileOnManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='InstallModuleStreamProfileOnManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.install_module_stream_profile_on_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                install_module_stream_profile_on_managed_instance_group_details=request.pop(util.camelize('InstallModuleStreamProfileOnManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'InstallModuleStreamProfileOnManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'install_module_stream_profile_on_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_install_packages_on_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'InstallPackagesOnManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'InstallPackagesOnManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='InstallPackagesOnManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.install_packages_on_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                install_packages_on_managed_instance_group_details=request.pop(util.camelize('InstallPackagesOnManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'InstallPackagesOnManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'install_packages_on_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_managed_instance_group_available_modules(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagedInstanceGroupAvailableModules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'ListManagedInstanceGroupAvailableModules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagedInstanceGroupAvailableModules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instance_group_available_modules(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instance_group_available_modules(
                    managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instance_group_available_modules(
                        managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagedInstanceGroupAvailableModules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceGroupAvailableModuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_managed_instance_group_available_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagedInstanceGroupAvailablePackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'ListManagedInstanceGroupAvailablePackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagedInstanceGroupAvailablePackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instance_group_available_packages(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instance_group_available_packages(
                    managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instance_group_available_packages(
                        managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagedInstanceGroupAvailablePackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceGroupAvailablePackageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_managed_instance_group_available_software_sources(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagedInstanceGroupAvailableSoftwareSources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'ListManagedInstanceGroupAvailableSoftwareSources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagedInstanceGroupAvailableSoftwareSources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instance_group_available_software_sources(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instance_group_available_software_sources(
                    managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instance_group_available_software_sources(
                        managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagedInstanceGroupAvailableSoftwareSources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'availableSoftwareSourceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_managed_instance_group_installed_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagedInstanceGroupInstalledPackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'ListManagedInstanceGroupInstalledPackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagedInstanceGroupInstalledPackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instance_group_installed_packages(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instance_group_installed_packages(
                    managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instance_group_installed_packages(
                        managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagedInstanceGroupInstalledPackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceGroupInstalledPackageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_managed_instance_group_modules(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagedInstanceGroupModules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'ListManagedInstanceGroupModules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagedInstanceGroupModules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instance_group_modules(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instance_group_modules(
                    managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instance_group_modules(
                        managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagedInstanceGroupModules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceGroupModuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_managed_instance_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagedInstanceGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'ListManagedInstanceGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagedInstanceGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instance_groups(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instance_groups(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instance_groups(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagedInstanceGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceGroupCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_manage_module_streams_on_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ManageModuleStreamsOnManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'ManageModuleStreamsOnManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ManageModuleStreamsOnManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.manage_module_streams_on_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                manage_module_streams_on_managed_instance_group_details=request.pop(util.camelize('ManageModuleStreamsOnManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ManageModuleStreamsOnManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'manage_module_streams_on_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_remove_module_stream_profile_from_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'RemoveModuleStreamProfileFromManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'RemoveModuleStreamProfileFromManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='RemoveModuleStreamProfileFromManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.remove_module_stream_profile_from_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                remove_module_stream_profile_from_managed_instance_group_details=request.pop(util.camelize('RemoveModuleStreamProfileFromManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'RemoveModuleStreamProfileFromManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_module_stream_profile_from_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_remove_packages_from_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'RemovePackagesFromManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'RemovePackagesFromManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='RemovePackagesFromManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.remove_packages_from_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                remove_packages_from_managed_instance_group_details=request.pop(util.camelize('RemovePackagesFromManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'RemovePackagesFromManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_packages_from_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_update_all_packages_on_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'UpdateAllPackagesOnManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'UpdateAllPackagesOnManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='UpdateAllPackagesOnManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.update_all_packages_on_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                update_all_packages_on_managed_instance_group_details=request.pop(util.camelize('UpdateAllPackagesOnManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'UpdateAllPackagesOnManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_all_packages_on_managed_instance_group',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_update_managed_instance_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'UpdateManagedInstanceGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance_group'), 'UpdateManagedInstanceGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='UpdateManagedInstanceGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceGroupClient(config, service_endpoint=service_endpoint)
            response = client.update_managed_instance_group(
                managed_instance_group_id=request.pop(util.camelize('managedInstanceGroupId')),
                update_managed_instance_group_details=request.pop(util.camelize('UpdateManagedInstanceGroupDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'UpdateManagedInstanceGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceGroup',
            False,
            False
        )
