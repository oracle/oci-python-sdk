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

        cassette_location = os.path.join('generated', 'container_engine_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_cluster_migrate_to_native_vcn(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'ClusterMigrateToNativeVcn'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'ClusterMigrateToNativeVcn')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ClusterMigrateToNativeVcn')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.cluster_migrate_to_native_vcn(
                cluster_id=request.pop(util.camelize('clusterId')),
                cluster_migrate_to_native_vcn_details=request.pop(util.camelize('ClusterMigrateToNativeVcnDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ClusterMigrateToNativeVcn',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cluster_migrate_to_native_vcn',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_complete_credential_rotation(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'CompleteCredentialRotation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'CompleteCredentialRotation')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='CompleteCredentialRotation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.complete_credential_rotation(
                cluster_id=request.pop(util.camelize('clusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'CompleteCredentialRotation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'complete_credential_rotation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_create_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'CreateCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'CreateCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='CreateCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.create_cluster(
                create_cluster_details=request.pop(util.camelize('CreateClusterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'CreateCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_create_kubeconfig(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'CreateKubeconfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'CreateKubeconfig')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='CreateKubeconfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.create_kubeconfig(
                cluster_id=request.pop(util.camelize('clusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'CreateKubeconfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_create_node_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'CreateNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'CreateNodePool')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='CreateNodePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.create_node_pool(
                create_node_pool_details=request.pop(util.camelize('CreateNodePoolDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'CreateNodePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_node_pool',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_create_virtual_node_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'CreateVirtualNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'CreateVirtualNodePool')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='CreateVirtualNodePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.create_virtual_node_pool(
                create_virtual_node_pool_details=request.pop(util.camelize('CreateVirtualNodePoolDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'CreateVirtualNodePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_virtual_node_pool',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_create_workload_mapping(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'CreateWorkloadMapping'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'CreateWorkloadMapping')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='CreateWorkloadMapping')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.create_workload_mapping(
                cluster_id=request.pop(util.camelize('clusterId')),
                create_workload_mapping_details=request.pop(util.camelize('CreateWorkloadMappingDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'CreateWorkloadMapping',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workloadMapping',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_delete_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'DeleteCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'DeleteCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='DeleteCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.delete_cluster(
                cluster_id=request.pop(util.camelize('clusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'DeleteCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_cluster',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_delete_node(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'DeleteNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'DeleteNode')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='DeleteNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.delete_node(
                node_pool_id=request.pop(util.camelize('nodePoolId')),
                node_id=request.pop(util.camelize('nodeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'DeleteNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_node',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_delete_node_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'DeleteNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'DeleteNodePool')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='DeleteNodePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.delete_node_pool(
                node_pool_id=request.pop(util.camelize('nodePoolId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'DeleteNodePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_node_pool',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_delete_virtual_node_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'DeleteVirtualNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'DeleteVirtualNodePool')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='DeleteVirtualNodePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.delete_virtual_node_pool(
                virtual_node_pool_id=request.pop(util.camelize('virtualNodePoolId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'DeleteVirtualNodePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_virtual_node_pool',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_delete_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'DeleteWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'DeleteWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='DeleteWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.delete_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'DeleteWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_delete_workload_mapping(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'DeleteWorkloadMapping'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'DeleteWorkloadMapping')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='DeleteWorkloadMapping')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.delete_workload_mapping(
                cluster_id=request.pop(util.camelize('clusterId')),
                workload_mapping_id=request.pop(util.camelize('workloadMappingId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'DeleteWorkloadMapping',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_workload_mapping',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_disable_addon(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'DisableAddon'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'DisableAddon')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='DisableAddon')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.disable_addon(
                cluster_id=request.pop(util.camelize('clusterId')),
                addon_name=request.pop(util.camelize('addonName')),
                is_remove_existing_add_on=request.pop(util.camelize('isRemoveExistingAddOn')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'DisableAddon',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'disable_addon',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_get_addon(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'GetAddon'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'GetAddon')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetAddon')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.get_addon(
                cluster_id=request.pop(util.camelize('clusterId')),
                addon_name=request.pop(util.camelize('addonName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetAddon',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addon',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_get_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'GetCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'GetCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.get_cluster(
                cluster_id=request.pop(util.camelize('clusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_get_cluster_migrate_to_native_vcn_status(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'GetClusterMigrateToNativeVcnStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'GetClusterMigrateToNativeVcnStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetClusterMigrateToNativeVcnStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.get_cluster_migrate_to_native_vcn_status(
                cluster_id=request.pop(util.camelize('clusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetClusterMigrateToNativeVcnStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'clusterMigrateToNativeVcnStatus',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_get_cluster_options(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'GetClusterOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'GetClusterOptions')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetClusterOptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.get_cluster_options(
                cluster_option_id=request.pop(util.camelize('clusterOptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetClusterOptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'clusterOptions',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_get_credential_rotation_status(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'GetCredentialRotationStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'GetCredentialRotationStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetCredentialRotationStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.get_credential_rotation_status(
                cluster_id=request.pop(util.camelize('clusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetCredentialRotationStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'credentialRotationStatus',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_get_node_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'GetNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'GetNodePool')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetNodePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.get_node_pool(
                node_pool_id=request.pop(util.camelize('nodePoolId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetNodePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'nodePool',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_get_node_pool_options(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'GetNodePoolOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'GetNodePoolOptions')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetNodePoolOptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.get_node_pool_options(
                node_pool_option_id=request.pop(util.camelize('nodePoolOptionId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetNodePoolOptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'nodePoolOptions',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_get_virtual_node(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'GetVirtualNode'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'GetVirtualNode')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetVirtualNode')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.get_virtual_node(
                virtual_node_pool_id=request.pop(util.camelize('virtualNodePoolId')),
                virtual_node_id=request.pop(util.camelize('virtualNodeId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetVirtualNode',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualNode',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_get_virtual_node_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'GetVirtualNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'GetVirtualNodePool')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetVirtualNodePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.get_virtual_node_pool(
                virtual_node_pool_id=request.pop(util.camelize('virtualNodePoolId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetVirtualNodePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualNodePool',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_get_workload_mapping(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'GetWorkloadMapping'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'GetWorkloadMapping')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='GetWorkloadMapping')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.get_workload_mapping(
                cluster_id=request.pop(util.camelize('clusterId')),
                workload_mapping_id=request.pop(util.camelize('workloadMappingId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'GetWorkloadMapping',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workloadMapping',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_install_addon(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'InstallAddon'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'InstallAddon')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='InstallAddon')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.install_addon(
                cluster_id=request.pop(util.camelize('clusterId')),
                install_addon_details=request.pop(util.camelize('InstallAddonDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'InstallAddon',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'install_addon',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_list_addon_options(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'ListAddonOptions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'ListAddonOptions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListAddonOptions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.list_addon_options(
                kubernetes_version=request.pop(util.camelize('kubernetesVersion')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_addon_options(
                    kubernetes_version=request.pop(util.camelize('kubernetesVersion')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_addon_options(
                        kubernetes_version=request.pop(util.camelize('kubernetesVersion')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListAddonOptions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addonOptionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_list_addons(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'ListAddons'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'ListAddons')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListAddons')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.list_addons(
                cluster_id=request.pop(util.camelize('clusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_addons(
                    cluster_id=request.pop(util.camelize('clusterId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_addons(
                        cluster_id=request.pop(util.camelize('clusterId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListAddons',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'addonSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_list_clusters(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'ListClusters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'ListClusters')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListClusters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.list_clusters(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_clusters(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_clusters(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListClusters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'clusterSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_list_node_pools(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'ListNodePools'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'ListNodePools')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListNodePools')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.list_node_pools(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_node_pools(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_node_pools(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListNodePools',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'nodePoolSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_list_pod_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'ListPodShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'ListPodShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListPodShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.list_pod_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_pod_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_pod_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListPodShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'podShapeSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_list_virtual_node_pools(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'ListVirtualNodePools'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'ListVirtualNodePools')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListVirtualNodePools')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.list_virtual_node_pools(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_virtual_node_pools(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_virtual_node_pools(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListVirtualNodePools',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualNodePoolSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_list_virtual_nodes(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'ListVirtualNodes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'ListVirtualNodes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListVirtualNodes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.list_virtual_nodes(
                virtual_node_pool_id=request.pop(util.camelize('virtualNodePoolId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_virtual_nodes(
                    virtual_node_pool_id=request.pop(util.camelize('virtualNodePoolId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_virtual_nodes(
                        virtual_node_pool_id=request.pop(util.camelize('virtualNodePoolId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListVirtualNodes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'virtualNodeSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'ListWorkRequestErrors')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                compartment_id=request.pop(util.camelize('compartmentId')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'ListWorkRequestLogs')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
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
            'container_engine',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_list_workload_mappings(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'ListWorkloadMappings'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'ListWorkloadMappings')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='ListWorkloadMappings')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.list_workload_mappings(
                cluster_id=request.pop(util.camelize('clusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_workload_mappings(
                    cluster_id=request.pop(util.camelize('clusterId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_workload_mappings(
                        cluster_id=request.pop(util.camelize('clusterId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'ListWorkloadMappings',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workloadMappingSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_start_credential_rotation(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'StartCredentialRotation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'StartCredentialRotation')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='StartCredentialRotation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.start_credential_rotation(
                cluster_id=request.pop(util.camelize('clusterId')),
                start_credential_rotation_details=request.pop(util.camelize('StartCredentialRotationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'StartCredentialRotation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_credential_rotation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_update_addon(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'UpdateAddon'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'UpdateAddon')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='UpdateAddon')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.update_addon(
                cluster_id=request.pop(util.camelize('clusterId')),
                addon_name=request.pop(util.camelize('addonName')),
                update_addon_details=request.pop(util.camelize('UpdateAddonDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'UpdateAddon',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_addon',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_update_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'UpdateCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'UpdateCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='UpdateCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.update_cluster(
                cluster_id=request.pop(util.camelize('clusterId')),
                update_cluster_details=request.pop(util.camelize('UpdateClusterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'UpdateCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_update_cluster_endpoint_config(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'UpdateClusterEndpointConfig'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'UpdateClusterEndpointConfig')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='UpdateClusterEndpointConfig')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.update_cluster_endpoint_config(
                cluster_id=request.pop(util.camelize('clusterId')),
                update_cluster_endpoint_config_details=request.pop(util.camelize('UpdateClusterEndpointConfigDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'UpdateClusterEndpointConfig',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_cluster_endpoint_config',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_update_node_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'UpdateNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'UpdateNodePool')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='UpdateNodePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.update_node_pool(
                node_pool_id=request.pop(util.camelize('nodePoolId')),
                update_node_pool_details=request.pop(util.camelize('UpdateNodePoolDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'UpdateNodePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_node_pool',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_update_virtual_node_pool(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'UpdateVirtualNodePool'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'UpdateVirtualNodePool')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='UpdateVirtualNodePool')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.update_virtual_node_pool(
                virtual_node_pool_id=request.pop(util.camelize('virtualNodePoolId')),
                update_virtual_node_pool_details=request.pop(util.camelize('UpdateVirtualNodePoolDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'UpdateVirtualNodePool',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_virtual_node_pool',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oke_control_plane_ww_grp@oracle.com" jiraProject="OKE" opsJiraProject="OKE"
def test_update_workload_mapping(testing_service_client):
    if not testing_service_client.is_api_enabled('container_engine', 'UpdateWorkloadMapping'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('container_engine', util.camelize('container_engine'), 'UpdateWorkloadMapping')
    )

    request_containers = testing_service_client.get_requests(service_name='container_engine', api_name='UpdateWorkloadMapping')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.container_engine.ContainerEngineClient(config, service_endpoint=service_endpoint)
            response = client.update_workload_mapping(
                cluster_id=request.pop(util.camelize('clusterId')),
                workload_mapping_id=request.pop(util.camelize('workloadMappingId')),
                update_workload_mapping_details=request.pop(util.camelize('UpdateWorkloadMappingDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'container_engine',
            'UpdateWorkloadMapping',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workloadMapping',
            False,
            False
        )
