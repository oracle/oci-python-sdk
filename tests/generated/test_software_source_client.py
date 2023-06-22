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
def test_change_availability_of_software_sources(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ChangeAvailabilityOfSoftwareSources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'ChangeAvailabilityOfSoftwareSources')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ChangeAvailabilityOfSoftwareSources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.change_availability_of_software_sources(
                change_availability_of_software_sources_details=request.pop(util.camelize('ChangeAvailabilityOfSoftwareSourcesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ChangeAvailabilityOfSoftwareSources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_availability_of_software_sources',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_create_entitlement(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'CreateEntitlement'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'CreateEntitlement')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='CreateEntitlement')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.create_entitlement(
                create_entitlement_details=request.pop(util.camelize('CreateEntitlementDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'CreateEntitlement',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_entitlement',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_create_software_source(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'CreateSoftwareSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'CreateSoftwareSource')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='CreateSoftwareSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.create_software_source(
                create_software_source_details=request.pop(util.camelize('CreateSoftwareSourceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'CreateSoftwareSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwareSource',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_delete_software_source(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'DeleteSoftwareSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'DeleteSoftwareSource')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='DeleteSoftwareSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.delete_software_source(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'DeleteSoftwareSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_software_source',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_get_erratum(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'GetErratum'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'GetErratum')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='GetErratum')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.get_erratum(
                compartment_id=request.pop(util.camelize('compartmentId')),
                name=request.pop(util.camelize('name')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'GetErratum',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'erratum',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_get_module_stream(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'GetModuleStream'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'GetModuleStream')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='GetModuleStream')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.get_module_stream(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                module_name=request.pop(util.camelize('moduleName')),
                stream_name=request.pop(util.camelize('streamName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'GetModuleStream',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'moduleStream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_get_module_stream_profile(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'GetModuleStreamProfile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'GetModuleStreamProfile')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='GetModuleStreamProfile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.get_module_stream_profile(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                profile_name=request.pop(util.camelize('profileName')),
                module_name=request.pop(util.camelize('moduleName')),
                stream_name=request.pop(util.camelize('streamName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'GetModuleStreamProfile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'moduleStreamProfile',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_get_package_group(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'GetPackageGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'GetPackageGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='GetPackageGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.get_package_group(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                package_group_id=request.pop(util.camelize('packageGroupId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'GetPackageGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'packageGroup',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_get_software_package(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'GetSoftwarePackage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'GetSoftwarePackage')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='GetSoftwarePackage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.get_software_package(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                software_package_name=request.pop(util.camelize('softwarePackageName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'GetSoftwarePackage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwarePackage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_get_software_source(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'GetSoftwareSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'GetSoftwareSource')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='GetSoftwareSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.get_software_source(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'GetSoftwareSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwareSource',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_entitlements(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListEntitlements'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'ListEntitlements')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListEntitlements')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.list_entitlements(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_entitlements(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_entitlements(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListEntitlements',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'entitlementCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_errata(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListErrata'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'ListErrata')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListErrata')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.list_errata(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_errata(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_errata(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListErrata',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'erratumCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_module_stream_profiles(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListModuleStreamProfiles'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'ListModuleStreamProfiles')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListModuleStreamProfiles')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.list_module_stream_profiles(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_module_stream_profiles(
                    software_source_id=request.pop(util.camelize('softwareSourceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_module_stream_profiles(
                        software_source_id=request.pop(util.camelize('softwareSourceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListModuleStreamProfiles',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'moduleStreamProfileCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_module_streams(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListModuleStreams'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'ListModuleStreams')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListModuleStreams')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.list_module_streams(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_module_streams(
                    software_source_id=request.pop(util.camelize('softwareSourceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_module_streams(
                        software_source_id=request.pop(util.camelize('softwareSourceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListModuleStreams',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'moduleStreamCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_package_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListPackageGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'ListPackageGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListPackageGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.list_package_groups(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_package_groups(
                    software_source_id=request.pop(util.camelize('softwareSourceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_package_groups(
                        software_source_id=request.pop(util.camelize('softwareSourceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListPackageGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'packageGroupCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_software_packages(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListSoftwarePackages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'ListSoftwarePackages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListSoftwarePackages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.list_software_packages(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_software_packages(
                    software_source_id=request.pop(util.camelize('softwareSourceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_software_packages(
                        software_source_id=request.pop(util.camelize('softwareSourceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListSoftwarePackages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwarePackageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_software_source_vendors(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListSoftwareSourceVendors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'ListSoftwareSourceVendors')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListSoftwareSourceVendors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.list_software_source_vendors(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListSoftwareSourceVendors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwareSourceVendorCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_software_sources(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListSoftwareSources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'ListSoftwareSources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListSoftwareSources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.list_software_sources(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_software_sources(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_software_sources(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListSoftwareSources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwareSourceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_search_software_source_module_streams(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'SearchSoftwareSourceModuleStreams'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'SearchSoftwareSourceModuleStreams')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='SearchSoftwareSourceModuleStreams')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.search_software_source_module_streams(
                search_software_source_module_streams_details=request.pop(util.camelize('SearchSoftwareSourceModuleStreamsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_software_source_module_streams(
                    search_software_source_module_streams_details=request.pop(util.camelize('SearchSoftwareSourceModuleStreamsDetails')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_software_source_module_streams(
                        search_software_source_module_streams_details=request.pop(util.camelize('SearchSoftwareSourceModuleStreamsDetails')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'SearchSoftwareSourceModuleStreams',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'moduleStreamCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_search_software_source_modules(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'SearchSoftwareSourceModules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'SearchSoftwareSourceModules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='SearchSoftwareSourceModules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.search_software_source_modules(
                search_software_source_modules_details=request.pop(util.camelize('SearchSoftwareSourceModulesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_software_source_modules(
                    search_software_source_modules_details=request.pop(util.camelize('SearchSoftwareSourceModulesDetails')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_software_source_modules(
                        search_software_source_modules_details=request.pop(util.camelize('SearchSoftwareSourceModulesDetails')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'SearchSoftwareSourceModules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'moduleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_search_software_source_package_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'SearchSoftwareSourcePackageGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'SearchSoftwareSourcePackageGroups')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='SearchSoftwareSourcePackageGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.search_software_source_package_groups(
                search_software_source_package_groups_details=request.pop(util.camelize('SearchSoftwareSourcePackageGroupsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.search_software_source_package_groups(
                    search_software_source_package_groups_details=request.pop(util.camelize('SearchSoftwareSourcePackageGroupsDetails')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.search_software_source_package_groups(
                        search_software_source_package_groups_details=request.pop(util.camelize('SearchSoftwareSourcePackageGroupsDetails')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'SearchSoftwareSourcePackageGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'packageGroupCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_update_software_source(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'UpdateSoftwareSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('software_source'), 'UpdateSoftwareSource')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='UpdateSoftwareSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.SoftwareSourceClient(config, service_endpoint=service_endpoint)
            response = client.update_software_source(
                software_source_id=request.pop(util.camelize('softwareSourceId')),
                update_software_source_details=request.pop(util.camelize('UpdateSoftwareSourceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'UpdateSoftwareSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'softwareSource',
            False,
            False
        )
