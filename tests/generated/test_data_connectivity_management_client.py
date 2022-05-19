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

        cassette_location = os.path.join('generated', 'data_connectivity_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_change_endpoint_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ChangeEndpointCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ChangeEndpointCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ChangeEndpointCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_endpoint_compartment(
                endpoint_id=request.pop(util.camelize('endpointId')),
                change_endpoint_compartment_details=request.pop(util.camelize('ChangeEndpointCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ChangeEndpointCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_endpoint_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_change_registry_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ChangeRegistryCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ChangeRegistryCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ChangeRegistryCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_registry_compartment(
                registry_id=request.pop(util.camelize('registryId')),
                change_registry_compartment_details=request.pop(util.camelize('ChangeRegistryCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ChangeRegistryCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_registry_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_attach_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateAttachDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateAttachDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateAttachDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_attach_data_asset(
                registry_id=request.pop(util.camelize('registryId')),
                endpoint_id=request.pop(util.camelize('endpointId')),
                create_attach_data_asset_details=request.pop(util.camelize('CreateAttachDataAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateAttachDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'attachDataAssetInfo',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_connection(
                registry_id=request.pop(util.camelize('registryId')),
                create_connection_details=request.pop(util.camelize('CreateConnectionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_connection_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateConnectionValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateConnectionValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateConnectionValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_connection_validation(
                registry_id=request.pop(util.camelize('registryId')),
                create_connection_validation_details=request.pop(util.camelize('CreateConnectionValidationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateConnectionValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectionValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_connectivity_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateConnectivityValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateConnectivityValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateConnectivityValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_connectivity_validation(
                registry_id=request.pop(util.camelize('registryId')),
                create_connectivity_validation_details=request.pop(util.camelize('CreateConnectivityValidationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateConnectivityValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectivityValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_data_asset(
                registry_id=request.pop(util.camelize('registryId')),
                create_data_asset_details=request.pop(util.camelize('CreateDataAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_data_preview(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateDataPreview'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateDataPreview')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateDataPreview')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_data_preview(
                registry_id=request.pop(util.camelize('registryId')),
                create_data_preview_details=request.pop(util.camelize('CreateDataPreviewDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateDataPreview',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataPreview',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_data_profile(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateDataProfile'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateDataProfile')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateDataProfile')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_data_profile(
                registry_id=request.pop(util.camelize('registryId')),
                create_data_profile_details=request.pop(util.camelize('CreateDataProfileDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateDataProfile',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataProfile',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_de_reference_artifact(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateDeReferenceArtifact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateDeReferenceArtifact')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateDeReferenceArtifact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_de_reference_artifact(
                registry_id=request.pop(util.camelize('registryId')),
                dcms_artifact_id=request.pop(util.camelize('dcmsArtifactId')),
                create_de_reference_artifact_details=request.pop(util.camelize('CreateDeReferenceArtifactDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateDeReferenceArtifact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deReferenceInfo',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_detach_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateDetachDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateDetachDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateDetachDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_detach_data_asset(
                registry_id=request.pop(util.camelize('registryId')),
                endpoint_id=request.pop(util.camelize('endpointId')),
                create_detach_data_asset_details=request.pop(util.camelize('CreateDetachDataAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateDetachDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detachDataAssetInfo',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_endpoint(
                create_endpoint_details=request.pop(util.camelize('CreateEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_entity_shape(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateEntityShape'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateEntityShape')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateEntityShape')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_entity_shape(
                registry_id=request.pop(util.camelize('registryId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                create_entity_shape_details=request.pop(util.camelize('CreateEntityShapeDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateEntityShape',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'entityShape',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_execute_operation_job(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateExecuteOperationJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateExecuteOperationJob')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateExecuteOperationJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_execute_operation_job(
                registry_id=request.pop(util.camelize('registryId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                create_execute_operation_job_details=request.pop(util.camelize('CreateExecuteOperationJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateExecuteOperationJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'executeOperationJobDetails',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_folder(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateFolder'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateFolder')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateFolder')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_folder(
                registry_id=request.pop(util.camelize('registryId')),
                create_folder_details=request.pop(util.camelize('CreateFolderDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateFolder',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folder',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_full_push_down_task(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateFullPushDownTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateFullPushDownTask')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateFullPushDownTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_full_push_down_task(
                registry_id=request.pop(util.camelize('registryId')),
                create_full_push_down_task_details=request.pop(util.camelize('CreateFullPushDownTaskDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateFullPushDownTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fullPushDownTaskResponse',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_reference_artifact(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateReferenceArtifact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateReferenceArtifact')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateReferenceArtifact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_reference_artifact(
                registry_id=request.pop(util.camelize('registryId')),
                dcms_artifact_id=request.pop(util.camelize('dcmsArtifactId')),
                create_reference_artifact_details=request.pop(util.camelize('CreateReferenceArtifactDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateReferenceArtifact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'referenceInfo',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_registry(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateRegistry'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateRegistry')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateRegistry')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_registry(
                create_registry_details=request.pop(util.camelize('CreateRegistryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateRegistry',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_registry',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_create_test_network_connectivity(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'CreateTestNetworkConnectivity'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'CreateTestNetworkConnectivity')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='CreateTestNetworkConnectivity')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_test_network_connectivity(
                registry_id=request.pop(util.camelize('registryId')),
                create_test_network_connectivity_details=request.pop(util.camelize('CreateTestNetworkConnectivityDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'CreateTestNetworkConnectivity',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'testNetworkConnectivity',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_delete_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'DeleteConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'DeleteConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='DeleteConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_connection(
                registry_id=request.pop(util.camelize('registryId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'DeleteConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_connection',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_delete_connection_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'DeleteConnectionValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'DeleteConnectionValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='DeleteConnectionValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_connection_validation(
                registry_id=request.pop(util.camelize('registryId')),
                connection_validation_key=request.pop(util.camelize('connectionValidationKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'DeleteConnectionValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_connection_validation',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_delete_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'DeleteDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'DeleteDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='DeleteDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_data_asset(
                registry_id=request.pop(util.camelize('registryId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'DeleteDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_data_asset',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_delete_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'DeleteEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'DeleteEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='DeleteEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_endpoint(
                endpoint_id=request.pop(util.camelize('endpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'DeleteEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_endpoint',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_delete_folder(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'DeleteFolder'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'DeleteFolder')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='DeleteFolder')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_folder(
                registry_id=request.pop(util.camelize('registryId')),
                folder_key=request.pop(util.camelize('folderKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'DeleteFolder',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_folder',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_delete_network_connectivity_status(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'DeleteNetworkConnectivityStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'DeleteNetworkConnectivityStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='DeleteNetworkConnectivityStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_network_connectivity_status(
                registry_id=request.pop(util.camelize('registryId')),
                network_validation_status_key=request.pop(util.camelize('networkValidationStatusKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'DeleteNetworkConnectivityStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_network_connectivity_status',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_delete_registry(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'DeleteRegistry'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'DeleteRegistry')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='DeleteRegistry')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_registry(
                registry_id=request.pop(util.camelize('registryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'DeleteRegistry',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_registry',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_get_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'GetConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'GetConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='GetConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_connection(
                registry_id=request.pop(util.camelize('registryId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'GetConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_get_connection_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'GetConnectionValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'GetConnectionValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='GetConnectionValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_connection_validation(
                registry_id=request.pop(util.camelize('registryId')),
                connection_validation_key=request.pop(util.camelize('connectionValidationKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'GetConnectionValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectionValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_get_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'GetDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'GetDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='GetDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_data_asset(
                registry_id=request.pop(util.camelize('registryId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'GetDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_get_data_entity(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'GetDataEntity'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'GetDataEntity')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='GetDataEntity')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_data_entity(
                registry_id=request.pop(util.camelize('registryId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                data_entity_key=request.pop(util.camelize('dataEntityKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'GetDataEntity',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataEntity',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_get_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'GetEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'GetEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='GetEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_endpoint(
                endpoint_id=request.pop(util.camelize('endpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'GetEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_get_execute_operation_job(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'GetExecuteOperationJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'GetExecuteOperationJob')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='GetExecuteOperationJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_execute_operation_job(
                registry_id=request.pop(util.camelize('registryId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                execute_operation_job_key=request.pop(util.camelize('executeOperationJobKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'GetExecuteOperationJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'executeOperationJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_get_folder(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'GetFolder'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'GetFolder')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='GetFolder')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_folder(
                registry_id=request.pop(util.camelize('registryId')),
                folder_key=request.pop(util.camelize('folderKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'GetFolder',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folder',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_get_network_connectivity_status(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'GetNetworkConnectivityStatus'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'GetNetworkConnectivityStatus')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='GetNetworkConnectivityStatus')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_network_connectivity_status(
                registry_id=request.pop(util.camelize('registryId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'GetNetworkConnectivityStatus',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'networkConnectivityStatus',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_get_operation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'GetOperation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'GetOperation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='GetOperation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_operation(
                registry_id=request.pop(util.camelize('registryId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                operation_resource_name=request.pop(util.camelize('operationResourceName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'GetOperation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_get_registry(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'GetRegistry'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'GetRegistry')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='GetRegistry')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_registry(
                registry_id=request.pop(util.camelize('registryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'GetRegistry',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'registry',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_get_schema(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'GetSchema'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'GetSchema')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='GetSchema')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_schema(
                registry_id=request.pop(util.camelize('registryId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'GetSchema',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schema',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_get_type(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'GetType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'GetType')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='GetType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_type(
                registry_id=request.pop(util.camelize('registryId')),
                type_key=request.pop(util.camelize('typeKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'GetType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'type',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_connection_validations(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListConnectionValidations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListConnectionValidations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListConnectionValidations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_connection_validations(
                registry_id=request.pop(util.camelize('registryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_connection_validations(
                    registry_id=request.pop(util.camelize('registryId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_connection_validations(
                        registry_id=request.pop(util.camelize('registryId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ListConnectionValidations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectionValidationSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_connections(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListConnections')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_connections(
                registry_id=request.pop(util.camelize('registryId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_connections(
                    registry_id=request.pop(util.camelize('registryId')),
                    data_asset_key=request.pop(util.camelize('dataAssetKey')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_connections(
                        registry_id=request.pop(util.camelize('registryId')),
                        data_asset_key=request.pop(util.camelize('dataAssetKey')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ListConnections',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectionSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_data_assets(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListDataAssets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListDataAssets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListDataAssets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_data_assets(
                registry_id=request.pop(util.camelize('registryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_assets(
                    registry_id=request.pop(util.camelize('registryId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_assets(
                        registry_id=request.pop(util.camelize('registryId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ListDataAssets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAssetSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_data_entities(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListDataEntities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListDataEntities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListDataEntities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_data_entities(
                registry_id=request.pop(util.camelize('registryId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_entities(
                    registry_id=request.pop(util.camelize('registryId')),
                    connection_key=request.pop(util.camelize('connectionKey')),
                    schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_entities(
                        registry_id=request.pop(util.camelize('registryId')),
                        connection_key=request.pop(util.camelize('connectionKey')),
                        schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ListDataEntities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataEntitySummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_endpoints(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_endpoints(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_endpoints(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ListEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'endpointSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_folders(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListFolders'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListFolders')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListFolders')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_folders(
                registry_id=request.pop(util.camelize('registryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_folders(
                    registry_id=request.pop(util.camelize('registryId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_folders(
                        registry_id=request.pop(util.camelize('registryId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ListFolders',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folderSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_operations(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListOperations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListOperations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListOperations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_operations(
                registry_id=request.pop(util.camelize('registryId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_operations(
                    registry_id=request.pop(util.camelize('registryId')),
                    connection_key=request.pop(util.camelize('connectionKey')),
                    schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_operations(
                        registry_id=request.pop(util.camelize('registryId')),
                        connection_key=request.pop(util.camelize('connectionKey')),
                        schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ListOperations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'operationSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_reference_artifacts(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListReferenceArtifacts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListReferenceArtifacts')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListReferenceArtifacts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_reference_artifacts(
                registry_id=request.pop(util.camelize('registryId')),
                dcms_artifact_id=request.pop(util.camelize('dcmsArtifactId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_reference_artifacts(
                    registry_id=request.pop(util.camelize('registryId')),
                    dcms_artifact_id=request.pop(util.camelize('dcmsArtifactId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_reference_artifacts(
                        registry_id=request.pop(util.camelize('registryId')),
                        dcms_artifact_id=request.pop(util.camelize('dcmsArtifactId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ListReferenceArtifacts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'referenceArtifactSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_registries(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListRegistries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListRegistries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListRegistries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_registries(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_registries(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_registries(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ListRegistries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'registrySummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_schemas(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListSchemas'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListSchemas')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListSchemas')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_schemas(
                registry_id=request.pop(util.camelize('registryId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_schemas(
                    registry_id=request.pop(util.camelize('registryId')),
                    connection_key=request.pop(util.camelize('connectionKey')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_schemas(
                        registry_id=request.pop(util.camelize('registryId')),
                        connection_key=request.pop(util.camelize('connectionKey')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ListSchemas',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schemaSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_types(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListTypes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListTypes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListTypes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_types(
                registry_id=request.pop(util.camelize('registryId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_types(
                    registry_id=request.pop(util.camelize('registryId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_types(
                        registry_id=request.pop(util.camelize('registryId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ListTypes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'typesSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
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
            'data_connectivity',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
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
            'data_connectivity',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
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
            'data_connectivity',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_update_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'UpdateConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'UpdateConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='UpdateConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_connection(
                registry_id=request.pop(util.camelize('registryId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                update_connection_details=request.pop(util.camelize('UpdateConnectionDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'UpdateConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_update_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'UpdateDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'UpdateDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='UpdateDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_data_asset(
                registry_id=request.pop(util.camelize('registryId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                update_data_asset_details=request.pop(util.camelize('UpdateDataAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'UpdateDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_update_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'UpdateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'UpdateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='UpdateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_endpoint(
                endpoint_id=request.pop(util.camelize('endpointId')),
                update_endpoint_details=request.pop(util.camelize('UpdateEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'UpdateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_update_folder(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'UpdateFolder'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'UpdateFolder')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='UpdateFolder')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_folder(
                registry_id=request.pop(util.camelize('registryId')),
                folder_key=request.pop(util.camelize('folderKey')),
                update_folder_details=request.pop(util.camelize('UpdateFolderDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'UpdateFolder',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folder',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_update_registry(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'UpdateRegistry'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'UpdateRegistry')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='UpdateRegistry')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_registry(
                registry_id=request.pop(util.camelize('registryId')),
                update_registry_details=request.pop(util.camelize('UpdateRegistryDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'UpdateRegistry',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'registry',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dcms_dev_ww_grp@oracle.com" jiraProject="DCMS" opsJiraProject="DCMS"
def test_validate_data_asset_network_reachablity(testing_service_client):
    if not testing_service_client.is_api_enabled('data_connectivity', 'ValidateDataAssetNetworkReachablity'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_connectivity', util.camelize('data_connectivity_management'), 'ValidateDataAssetNetworkReachablity')
    )

    request_containers = testing_service_client.get_requests(service_name='data_connectivity', api_name='ValidateDataAssetNetworkReachablity')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_connectivity.DataConnectivityManagementClient(config, service_endpoint=service_endpoint)
            response = client.validate_data_asset_network_reachablity(
                endpoint_id=request.pop(util.camelize('endpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_connectivity',
            'ValidateDataAssetNetworkReachablity',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'validate_data_asset_network_reachablity',
            False,
            False
        )
