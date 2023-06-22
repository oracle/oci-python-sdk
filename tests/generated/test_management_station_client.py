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
def test_create_management_station(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'CreateManagementStation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('management_station'), 'CreateManagementStation')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='CreateManagementStation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagementStationClient(config, service_endpoint=service_endpoint)
            response = client.create_management_station(
                create_management_station_details=request.pop(util.camelize('CreateManagementStationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'CreateManagementStation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementStation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_delete_management_station(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'DeleteManagementStation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('management_station'), 'DeleteManagementStation')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='DeleteManagementStation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagementStationClient(config, service_endpoint=service_endpoint)
            response = client.delete_management_station(
                management_station_id=request.pop(util.camelize('managementStationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'DeleteManagementStation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_management_station',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_get_management_station(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'GetManagementStation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('management_station'), 'GetManagementStation')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='GetManagementStation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagementStationClient(config, service_endpoint=service_endpoint)
            response = client.get_management_station(
                management_station_id=request.pop(util.camelize('managementStationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'GetManagementStation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementStation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_management_stations(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListManagementStations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('management_station'), 'ListManagementStations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListManagementStations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagementStationClient(config, service_endpoint=service_endpoint)
            response = client.list_management_stations(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_management_stations(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_management_stations(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListManagementStations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementStationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_list_mirrors(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'ListMirrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('management_station'), 'ListMirrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='ListMirrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagementStationClient(config, service_endpoint=service_endpoint)
            response = client.list_mirrors(
                management_station_id=request.pop(util.camelize('managementStationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_mirrors(
                    management_station_id=request.pop(util.camelize('managementStationId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_mirrors(
                        management_station_id=request.pop(util.camelize('managementStationId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'ListMirrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mirrorsCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_synchronize_mirrors(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'SynchronizeMirrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('management_station'), 'SynchronizeMirrors')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='SynchronizeMirrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagementStationClient(config, service_endpoint=service_endpoint)
            response = client.synchronize_mirrors(
                management_station_id=request.pop(util.camelize('managementStationId')),
                synchronize_mirrors_details=request.pop(util.camelize('SynchronizeMirrorsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'SynchronizeMirrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'synchronize_mirrors',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_synchronize_single_mirrors(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'SynchronizeSingleMirrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('management_station'), 'SynchronizeSingleMirrors')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='SynchronizeSingleMirrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagementStationClient(config, service_endpoint=service_endpoint)
            response = client.synchronize_single_mirrors(
                management_station_id=request.pop(util.camelize('managementStationId')),
                mirror_id=request.pop(util.camelize('mirrorId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'SynchronizeSingleMirrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'synchronize_single_mirrors',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="osmh_team_ww_grp@oracle.com" jiraProject="OSMH" opsJiraProject="OSMH"
def test_update_management_station(testing_service_client):
    if not testing_service_client.is_api_enabled('os_management_hub', 'UpdateManagementStation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('os_management_hub', util.camelize('management_station'), 'UpdateManagementStation')
    )

    request_containers = testing_service_client.get_requests(service_name='os_management_hub', api_name='UpdateManagementStation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.os_management_hub.ManagementStationClient(config, service_endpoint=service_endpoint)
            response = client.update_management_station(
                management_station_id=request.pop(util.camelize('managementStationId')),
                update_management_station_details=request.pop(util.camelize('UpdateManagementStationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'os_management_hub',
            'UpdateManagementStation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'managementStation',
            False,
            False
        )
