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

        cassette_location = os.path.join('generated', 'cloud_bridge_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_asset_source_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ChangeAssetSourceCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'ChangeAssetSourceCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ChangeAssetSourceCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.change_asset_source_compartment(
                asset_source_id=request.pop(util.camelize('assetSourceId')),
                change_asset_source_compartment_details=request.pop(util.camelize('ChangeAssetSourceCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ChangeAssetSourceCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_asset_source_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_discovery_schedule_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ChangeDiscoveryScheduleCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'ChangeDiscoveryScheduleCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ChangeDiscoveryScheduleCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.change_discovery_schedule_compartment(
                discovery_schedule_id=request.pop(util.camelize('discoveryScheduleId')),
                change_discovery_schedule_compartment_details=request.pop(util.camelize('ChangeDiscoveryScheduleCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ChangeDiscoveryScheduleCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_discovery_schedule_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_asset_source(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'CreateAssetSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'CreateAssetSource')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='CreateAssetSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.create_asset_source(
                create_asset_source_details=request.pop(util.camelize('CreateAssetSourceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'CreateAssetSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'assetSource',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_discovery_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'CreateDiscoverySchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'CreateDiscoverySchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='CreateDiscoverySchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.create_discovery_schedule(
                create_discovery_schedule_details=request.pop(util.camelize('CreateDiscoveryScheduleDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'CreateDiscoverySchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoverySchedule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_asset_source(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'DeleteAssetSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'DeleteAssetSource')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='DeleteAssetSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.delete_asset_source(
                asset_source_id=request.pop(util.camelize('assetSourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'DeleteAssetSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_asset_source',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_discovery_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'DeleteDiscoverySchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'DeleteDiscoverySchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='DeleteDiscoverySchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.delete_discovery_schedule(
                discovery_schedule_id=request.pop(util.camelize('discoveryScheduleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'DeleteDiscoverySchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_discovery_schedule',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_asset_source(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'GetAssetSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'GetAssetSource')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='GetAssetSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.get_asset_source(
                asset_source_id=request.pop(util.camelize('assetSourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'GetAssetSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'assetSource',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_discovery_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'GetDiscoverySchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'GetDiscoverySchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='GetDiscoverySchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.get_discovery_schedule(
                discovery_schedule_id=request.pop(util.camelize('discoveryScheduleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'GetDiscoverySchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoverySchedule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_asset_source_connections(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ListAssetSourceConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'ListAssetSourceConnections')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ListAssetSourceConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.list_asset_source_connections(
                asset_source_id=request.pop(util.camelize('assetSourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_asset_source_connections(
                    asset_source_id=request.pop(util.camelize('assetSourceId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_asset_source_connections(
                        asset_source_id=request.pop(util.camelize('assetSourceId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ListAssetSourceConnections',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'assetSourceConnectionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_asset_sources(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ListAssetSources'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'ListAssetSources')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ListAssetSources')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.list_asset_sources(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_asset_sources(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_asset_sources(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ListAssetSources',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'assetSourceCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_discovery_schedules(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ListDiscoverySchedules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'ListDiscoverySchedules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ListDiscoverySchedules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.list_discovery_schedules(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_discovery_schedules(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_discovery_schedules(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ListDiscoverySchedules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoveryScheduleCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_refresh_asset_source(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'RefreshAssetSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'RefreshAssetSource')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='RefreshAssetSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.refresh_asset_source(
                asset_source_id=request.pop(util.camelize('assetSourceId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'RefreshAssetSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'refresh_asset_source',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_asset_source(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'UpdateAssetSource'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'UpdateAssetSource')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='UpdateAssetSource')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.update_asset_source(
                asset_source_id=request.pop(util.camelize('assetSourceId')),
                update_asset_source_details=request.pop(util.camelize('UpdateAssetSourceDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'UpdateAssetSource',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_asset_source',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_discovery_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'UpdateDiscoverySchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('discovery'), 'UpdateDiscoverySchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='UpdateDiscoverySchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.DiscoveryClient(config, service_endpoint=service_endpoint)
            response = client.update_discovery_schedule(
                update_discovery_schedule_details=request.pop(util.camelize('UpdateDiscoveryScheduleDetails')),
                discovery_schedule_id=request.pop(util.camelize('discoveryScheduleId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'UpdateDiscoverySchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'discoverySchedule',
            False,
            False
        )
