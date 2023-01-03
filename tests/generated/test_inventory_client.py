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

        cassette_location = os.path.join('generated', 'cloud_bridge_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_analyze_assets(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'AnalyzeAssets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'AnalyzeAssets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='AnalyzeAssets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.analyze_assets(
                compartment_id=request.pop(util.camelize('compartmentId')),
                aggregation_properties=request.pop(util.camelize('aggregationProperties')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.analyze_assets(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    aggregation_properties=request.pop(util.camelize('aggregationProperties')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.analyze_assets(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        aggregation_properties=request.pop(util.camelize('aggregationProperties')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'AnalyzeAssets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'assetAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_asset_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ChangeAssetCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'ChangeAssetCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ChangeAssetCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.change_asset_compartment(
                asset_id=request.pop(util.camelize('assetId')),
                change_asset_compartment_details=request.pop(util.camelize('ChangeAssetCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ChangeAssetCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_asset_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_asset_tags(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ChangeAssetTags'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'ChangeAssetTags')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ChangeAssetTags')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.change_asset_tags(
                asset_id=request.pop(util.camelize('assetId')),
                change_asset_tags_details=request.pop(util.camelize('ChangeAssetTagsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ChangeAssetTags',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'asset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'CreateAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'CreateAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='CreateAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.create_asset(
                create_asset_details=request.pop(util.camelize('CreateAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'CreateAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'asset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_inventory(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'CreateInventory'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'CreateInventory')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='CreateInventory')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.create_inventory(
                create_inventory_details=request.pop(util.camelize('CreateInventoryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'CreateInventory',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_inventory',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'DeleteAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'DeleteAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='DeleteAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.delete_asset(
                asset_id=request.pop(util.camelize('assetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'DeleteAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_asset',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_inventory(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'DeleteInventory'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'DeleteInventory')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='DeleteInventory')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.delete_inventory(
                inventory_id=request.pop(util.camelize('inventoryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'DeleteInventory',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_inventory',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'GetAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'GetAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='GetAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.get_asset(
                asset_id=request.pop(util.camelize('assetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'GetAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'asset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_inventory(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'GetInventory'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'GetInventory')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='GetInventory')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.get_inventory(
                inventory_id=request.pop(util.camelize('inventoryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'GetInventory',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'inventory',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_import_inventory(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ImportInventory'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'ImportInventory')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ImportInventory')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.import_inventory(
                import_inventory_details=request.pop(util.camelize('ImportInventoryDetails')),
                inventory_id=request.pop(util.camelize('inventoryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ImportInventory',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'import_inventory',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_assets(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ListAssets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'ListAssets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ListAssets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.list_assets(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_assets(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_assets(
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
            'ListAssets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'assetCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_historical_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ListHistoricalMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'ListHistoricalMetrics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ListHistoricalMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.list_historical_metrics(
                asset_id=request.pop(util.camelize('assetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_historical_metrics(
                    asset_id=request.pop(util.camelize('assetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_historical_metrics(
                        asset_id=request.pop(util.camelize('assetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'ListHistoricalMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'historicalMetricCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_inventories(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'ListInventories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'ListInventories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='ListInventories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.list_inventories(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_inventories(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_inventories(
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
            'ListInventories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'inventoryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_submit_historical_metrics(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'SubmitHistoricalMetrics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'SubmitHistoricalMetrics')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='SubmitHistoricalMetrics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.submit_historical_metrics(
                submit_historical_metrics_details=request.pop(util.camelize('SubmitHistoricalMetricsDetails')),
                asset_id=request.pop(util.camelize('assetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'SubmitHistoricalMetrics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'historicalMetricCollection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'UpdateAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'UpdateAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='UpdateAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.update_asset(
                asset_id=request.pop(util.camelize('assetId')),
                update_asset_details=request.pop(util.camelize('UpdateAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'UpdateAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'asset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="us_grp_oci_ocb_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_inventory(testing_service_client):
    if not testing_service_client.is_api_enabled('cloud_bridge', 'UpdateInventory'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('cloud_bridge', util.camelize('inventory'), 'UpdateInventory')
    )

    request_containers = testing_service_client.get_requests(service_name='cloud_bridge', api_name='UpdateInventory')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.cloud_bridge.InventoryClient(config, service_endpoint=service_endpoint)
            response = client.update_inventory(
                inventory_id=request.pop(util.camelize('inventoryId')),
                update_inventory_details=request.pop(util.camelize('UpdateInventoryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'cloud_bridge',
            'UpdateInventory',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'inventory',
            False,
            False
        )
