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
def test_attach_software_sources_to_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'AttachSoftwareSourcesToManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'AttachSoftwareSourcesToManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='AttachSoftwareSourcesToManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.attach_software_sources_to_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                attach_software_sources_to_managed_instance_details=request.pop(util.camelize('AttachSoftwareSourcesToManagedInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'AttachSoftwareSourcesToManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attach_software_sources_to_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_detach_software_sources_from_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'DetachSoftwareSourcesFromManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'DetachSoftwareSourcesFromManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='DetachSoftwareSourcesFromManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.detach_software_sources_from_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                detach_software_sources_from_managed_instance_details=request.pop(util.camelize('DetachSoftwareSourcesFromManagedInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'DetachSoftwareSourcesFromManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detach_software_sources_from_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_disable_module_stream_on_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'DisableModuleStreamOnManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'DisableModuleStreamOnManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='DisableModuleStreamOnManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.disable_module_stream_on_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                disable_module_stream_on_managed_instance_details=request.pop(util.camelize('DisableModuleStreamOnManagedInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'DisableModuleStreamOnManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'disable_module_stream_on_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_enable_module_stream_on_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'EnableModuleStreamOnManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'EnableModuleStreamOnManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='EnableModuleStreamOnManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.enable_module_stream_on_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                enable_module_stream_on_managed_instance_details=request.pop(util.camelize('EnableModuleStreamOnManagedInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'EnableModuleStreamOnManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'enable_module_stream_on_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_get_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'GetManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'GetManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='GetManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.get_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'GetManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_install_module_stream_profile_on_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'InstallModuleStreamProfileOnManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'InstallModuleStreamProfileOnManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='InstallModuleStreamProfileOnManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.install_module_stream_profile_on_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                install_module_stream_profile_on_managed_instance_details=request.pop(util.camelize('InstallModuleStreamProfileOnManagedInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'InstallModuleStreamProfileOnManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'install_module_stream_profile_on_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_install_packages_on_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'InstallPackagesOnManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'InstallPackagesOnManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='InstallPackagesOnManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.install_packages_on_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                install_packages_on_managed_instance_details=request.pop(util.camelize('InstallPackagesOnManagedInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'InstallPackagesOnManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'install_packages_on_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_managed_instance_available_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagedInstanceAvailablePackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'ListManagedInstanceAvailablePackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagedInstanceAvailablePackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instance_available_packages(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instance_available_packages(
                    managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instance_available_packages(
                        managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagedInstanceAvailablePackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'availablePackageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_managed_instance_available_software_sources(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagedInstanceAvailableSoftwareSources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'ListManagedInstanceAvailableSoftwareSources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagedInstanceAvailableSoftwareSources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instance_available_software_sources(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instance_available_software_sources(
                    managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instance_available_software_sources(
                        managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagedInstanceAvailableSoftwareSources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'availableSoftwareSourceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_managed_instance_errata(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagedInstanceErrata'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'ListManagedInstanceErrata')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagedInstanceErrata')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instance_errata(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instance_errata(
                    managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instance_errata(
                        managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagedInstanceErrata',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceErratumSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_managed_instance_installed_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagedInstanceInstalledPackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'ListManagedInstanceInstalledPackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagedInstanceInstalledPackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instance_installed_packages(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instance_installed_packages(
                    managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instance_installed_packages(
                        managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagedInstanceInstalledPackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'installedPackageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_managed_instance_modules(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagedInstanceModules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'ListManagedInstanceModules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagedInstanceModules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instance_modules(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instance_modules(
                    managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instance_modules(
                        managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagedInstanceModules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceModuleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_managed_instance_updatable_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagedInstanceUpdatablePackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'ListManagedInstanceUpdatablePackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagedInstanceUpdatablePackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instance_updatable_packages(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instance_updatable_packages(
                    managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instance_updatable_packages(
                        managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagedInstanceUpdatablePackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'updatablePackageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_managed_instances(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagedInstances'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'ListManagedInstances')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagedInstances')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.list_managed_instances(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_managed_instances(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_managed_instances(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagedInstances',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstanceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_manage_module_streams_on_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ManageModuleStreamsOnManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'ManageModuleStreamsOnManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ManageModuleStreamsOnManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.manage_module_streams_on_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                manage_module_streams_on_managed_instance_details=request.pop(util.camelize('ManageModuleStreamsOnManagedInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ManageModuleStreamsOnManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'manage_module_streams_on_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_refresh_software_on_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'RefreshSoftwareOnManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'RefreshSoftwareOnManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='RefreshSoftwareOnManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.refresh_software_on_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'RefreshSoftwareOnManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'refresh_software_on_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_remove_module_stream_profile_from_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'RemoveModuleStreamProfileFromManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'RemoveModuleStreamProfileFromManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='RemoveModuleStreamProfileFromManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.remove_module_stream_profile_from_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                remove_module_stream_profile_from_managed_instance_details=request.pop(util.camelize('RemoveModuleStreamProfileFromManagedInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'RemoveModuleStreamProfileFromManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_module_stream_profile_from_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_remove_packages_from_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'RemovePackagesFromManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'RemovePackagesFromManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='RemovePackagesFromManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.remove_packages_from_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                remove_packages_from_managed_instance_details=request.pop(util.camelize('RemovePackagesFromManagedInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'RemovePackagesFromManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_packages_from_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_switch_module_stream_on_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'SwitchModuleStreamOnManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'SwitchModuleStreamOnManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='SwitchModuleStreamOnManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.switch_module_stream_on_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                switch_module_stream_on_managed_instance_details=request.pop(util.camelize('SwitchModuleStreamOnManagedInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'SwitchModuleStreamOnManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'switch_module_stream_on_managed_instance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_update_all_packages_on_managed_instances_in_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'UpdateAllPackagesOnManagedInstancesInCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'UpdateAllPackagesOnManagedInstancesInCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='UpdateAllPackagesOnManagedInstancesInCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.update_all_packages_on_managed_instances_in_compartment(
                update_all_packages_on_managed_instances_in_compartment_details=request.pop(util.camelize('UpdateAllPackagesOnManagedInstancesInCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'UpdateAllPackagesOnManagedInstancesInCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_all_packages_on_managed_instances_in_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_update_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'UpdateManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'UpdateManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='UpdateManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.update_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                update_managed_instance_details=request.pop(util.camelize('UpdateManagedInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'UpdateManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managedInstance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_update_packages_on_managed_instance(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'UpdatePackagesOnManagedInstance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('managed_instance'), 'UpdatePackagesOnManagedInstance')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='UpdatePackagesOnManagedInstance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagedInstanceClient(config, service_endpoint=service_endpoint)
            response = client.update_packages_on_managed_instance(
                managed_instance_id=request.pop(util.camelize('managedInstanceId')),
                update_packages_on_managed_instance_details=request.pop(util.camelize('UpdatePackagesOnManagedInstanceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'UpdatePackagesOnManagedInstance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_packages_on_managed_instance',
            False,
            False
        )
