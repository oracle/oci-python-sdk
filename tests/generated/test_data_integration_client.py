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

        cassette_location = os.path.join('generated', 'data_integration_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_change_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ChangeCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ChangeCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ChangeCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.change_compartment(
                workspace_id=request.pop(util.camelize('workspaceId')),
                change_compartment_details=request.pop(util.camelize('ChangeCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ChangeCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_application(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_application(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_application_details=request.pop(util.camelize('CreateApplicationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'application',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_connection(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_connection_details=request.pop(util.camelize('CreateConnectionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_connection_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateConnectionValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateConnectionValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateConnectionValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_connection_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_connection_validation_details=request.pop(util.camelize('CreateConnectionValidationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateConnectionValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectionValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_data_asset(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_data_asset_details=request.pop(util.camelize('CreateDataAssetDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_data_flow(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateDataFlow'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateDataFlow')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateDataFlow')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_data_flow(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_data_flow_details=request.pop(util.camelize('CreateDataFlowDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateDataFlow',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataFlow',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_data_flow_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateDataFlowValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateDataFlowValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateDataFlowValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_data_flow_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_data_flow_validation_details=request.pop(util.camelize('CreateDataFlowValidationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateDataFlowValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataFlowValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_entity_shape(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateEntityShape'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateEntityShape')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateEntityShape')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_entity_shape(
                workspace_id=request.pop(util.camelize('workspaceId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                create_entity_shape_details=request.pop(util.camelize('CreateEntityShapeDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateEntityShape',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'entityShape',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_external_publication(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateExternalPublication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateExternalPublication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateExternalPublication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_external_publication(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_key=request.pop(util.camelize('taskKey')),
                create_external_publication_details=request.pop(util.camelize('CreateExternalPublicationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateExternalPublication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalPublication',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_external_publication_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateExternalPublicationValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateExternalPublicationValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateExternalPublicationValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_external_publication_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_key=request.pop(util.camelize('taskKey')),
                create_external_publication_validation_details=request.pop(util.camelize('CreateExternalPublicationValidationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateExternalPublicationValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalPublicationValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_folder(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateFolder'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateFolder')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateFolder')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_folder(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_folder_details=request.pop(util.camelize('CreateFolderDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateFolder',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folder',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_function_library(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateFunctionLibrary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateFunctionLibrary')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateFunctionLibrary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_function_library(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_function_library_details=request.pop(util.camelize('CreateFunctionLibraryDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateFunctionLibrary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'functionLibrary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_patch(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreatePatch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreatePatch')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreatePatch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_patch(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                create_patch_details=request.pop(util.camelize('CreatePatchDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreatePatch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patch',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_pipeline(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreatePipeline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreatePipeline')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreatePipeline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_pipeline(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_pipeline_details=request.pop(util.camelize('CreatePipelineDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreatePipeline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pipeline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_pipeline_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreatePipelineValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreatePipelineValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreatePipelineValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_pipeline_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_pipeline_validation_details=request.pop(util.camelize('CreatePipelineValidationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreatePipelineValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pipelineValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_project(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateProject')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_project(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_project_details=request.pop(util.camelize('CreateProjectDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_schedule(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                create_schedule_details=request.pop(util.camelize('CreateScheduleDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schedule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_task(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateTask')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_task(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_task_details=request.pop(util.camelize('CreateTaskDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'task',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_task_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateTaskRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateTaskRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateTaskRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_task_run(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                create_task_run_details=request.pop(util.camelize('CreateTaskRunDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateTaskRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taskRun',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_task_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateTaskSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateTaskSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateTaskSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_task_schedule(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                create_task_schedule_details=request.pop(util.camelize('CreateTaskScheduleDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateTaskSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taskSchedule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_task_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateTaskValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateTaskValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateTaskValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_task_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_task_validation_details=request.pop(util.camelize('CreateTaskValidationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateTaskValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taskValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_user_defined_function(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateUserDefinedFunction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateUserDefinedFunction')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateUserDefinedFunction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_user_defined_function(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_user_defined_function_details=request.pop(util.camelize('CreateUserDefinedFunctionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateUserDefinedFunction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userDefinedFunction',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_user_defined_function_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateUserDefinedFunctionValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateUserDefinedFunctionValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateUserDefinedFunctionValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_user_defined_function_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                create_user_defined_function_validation_details=request.pop(util.camelize('CreateUserDefinedFunctionValidationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateUserDefinedFunctionValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userDefinedFunctionValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_create_workspace(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'CreateWorkspace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'CreateWorkspace')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='CreateWorkspace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.create_workspace(
                create_workspace_details=request.pop(util.camelize('CreateWorkspaceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'CreateWorkspace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_workspace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_application(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_application(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_application',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_connection(
                workspace_id=request.pop(util.camelize('workspaceId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_connection',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_connection_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteConnectionValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteConnectionValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteConnectionValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_connection_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                connection_validation_key=request.pop(util.camelize('connectionValidationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteConnectionValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_connection_validation',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_data_asset(
                workspace_id=request.pop(util.camelize('workspaceId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_data_asset',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_data_flow(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteDataFlow'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteDataFlow')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteDataFlow')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_data_flow(
                workspace_id=request.pop(util.camelize('workspaceId')),
                data_flow_key=request.pop(util.camelize('dataFlowKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteDataFlow',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_data_flow',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_data_flow_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteDataFlowValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteDataFlowValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteDataFlowValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_data_flow_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                data_flow_validation_key=request.pop(util.camelize('dataFlowValidationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteDataFlowValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_data_flow_validation',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_external_publication(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteExternalPublication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteExternalPublication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteExternalPublication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_external_publication(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_key=request.pop(util.camelize('taskKey')),
                external_publications_key=request.pop(util.camelize('externalPublicationsKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteExternalPublication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_external_publication',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_external_publication_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteExternalPublicationValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteExternalPublicationValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteExternalPublicationValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_external_publication_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_key=request.pop(util.camelize('taskKey')),
                external_publication_validation_key=request.pop(util.camelize('externalPublicationValidationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteExternalPublicationValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_external_publication_validation',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_folder(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteFolder'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteFolder')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteFolder')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_folder(
                workspace_id=request.pop(util.camelize('workspaceId')),
                folder_key=request.pop(util.camelize('folderKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteFolder',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_folder',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_function_library(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteFunctionLibrary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteFunctionLibrary')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteFunctionLibrary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_function_library(
                workspace_id=request.pop(util.camelize('workspaceId')),
                function_library_key=request.pop(util.camelize('functionLibraryKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteFunctionLibrary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_function_library',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_patch(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeletePatch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeletePatch')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeletePatch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_patch(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                patch_key=request.pop(util.camelize('patchKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeletePatch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_patch',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_pipeline(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeletePipeline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeletePipeline')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeletePipeline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_pipeline(
                workspace_id=request.pop(util.camelize('workspaceId')),
                pipeline_key=request.pop(util.camelize('pipelineKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeletePipeline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_pipeline',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_pipeline_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeletePipelineValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeletePipelineValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeletePipelineValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_pipeline_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                pipeline_validation_key=request.pop(util.camelize('pipelineValidationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeletePipelineValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_pipeline_validation',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_project(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteProject')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_project(
                workspace_id=request.pop(util.camelize('workspaceId')),
                project_key=request.pop(util.camelize('projectKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_project',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_schedule(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                schedule_key=request.pop(util.camelize('scheduleKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_schedule',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_task(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteTask')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_task(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_key=request.pop(util.camelize('taskKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_task',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_task_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteTaskRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteTaskRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteTaskRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_task_run(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                task_run_key=request.pop(util.camelize('taskRunKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteTaskRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_task_run',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_task_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteTaskSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteTaskSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteTaskSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_task_schedule(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                task_schedule_key=request.pop(util.camelize('taskScheduleKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteTaskSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_task_schedule',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_task_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteTaskValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteTaskValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteTaskValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_task_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_validation_key=request.pop(util.camelize('taskValidationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteTaskValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_task_validation',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_user_defined_function(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteUserDefinedFunction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteUserDefinedFunction')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteUserDefinedFunction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_user_defined_function(
                workspace_id=request.pop(util.camelize('workspaceId')),
                user_defined_function_key=request.pop(util.camelize('userDefinedFunctionKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteUserDefinedFunction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_user_defined_function',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_user_defined_function_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteUserDefinedFunctionValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteUserDefinedFunctionValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteUserDefinedFunctionValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_user_defined_function_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                user_defined_function_validation_key=request.pop(util.camelize('userDefinedFunctionValidationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteUserDefinedFunctionValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_user_defined_function_validation',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_delete_workspace(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'DeleteWorkspace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'DeleteWorkspace')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='DeleteWorkspace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.delete_workspace(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'DeleteWorkspace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_workspace',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_application(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_application(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'application',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_connection(
                workspace_id=request.pop(util.camelize('workspaceId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_connection_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetConnectionValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetConnectionValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetConnectionValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_connection_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                connection_validation_key=request.pop(util.camelize('connectionValidationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetConnectionValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectionValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_count_statistic(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetCountStatistic'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetCountStatistic')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetCountStatistic')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_count_statistic(
                workspace_id=request.pop(util.camelize('workspaceId')),
                count_statistic_key=request.pop(util.camelize('countStatisticKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetCountStatistic',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'countStatistic',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_data_asset(
                workspace_id=request.pop(util.camelize('workspaceId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_data_entity(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetDataEntity'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetDataEntity')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetDataEntity')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_data_entity(
                workspace_id=request.pop(util.camelize('workspaceId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                data_entity_key=request.pop(util.camelize('dataEntityKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetDataEntity',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataEntity',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_data_flow(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetDataFlow'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetDataFlow')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetDataFlow')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_data_flow(
                workspace_id=request.pop(util.camelize('workspaceId')),
                data_flow_key=request.pop(util.camelize('dataFlowKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetDataFlow',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataFlow',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_data_flow_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetDataFlowValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetDataFlowValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetDataFlowValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_data_flow_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                data_flow_validation_key=request.pop(util.camelize('dataFlowValidationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetDataFlowValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataFlowValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_dependent_object(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetDependentObject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetDependentObject')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetDependentObject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_dependent_object(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                dependent_object_key=request.pop(util.camelize('dependentObjectKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetDependentObject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dependentObject',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_external_publication(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetExternalPublication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetExternalPublication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetExternalPublication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_external_publication(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_key=request.pop(util.camelize('taskKey')),
                external_publications_key=request.pop(util.camelize('externalPublicationsKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetExternalPublication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalPublication',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_external_publication_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetExternalPublicationValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetExternalPublicationValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetExternalPublicationValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_external_publication_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_key=request.pop(util.camelize('taskKey')),
                external_publication_validation_key=request.pop(util.camelize('externalPublicationValidationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetExternalPublicationValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalPublicationValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_folder(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetFolder'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetFolder')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetFolder')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_folder(
                workspace_id=request.pop(util.camelize('workspaceId')),
                folder_key=request.pop(util.camelize('folderKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetFolder',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folder',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_function_library(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetFunctionLibrary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetFunctionLibrary')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetFunctionLibrary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_function_library(
                workspace_id=request.pop(util.camelize('workspaceId')),
                function_library_key=request.pop(util.camelize('functionLibraryKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetFunctionLibrary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'functionLibrary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_patch(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetPatch'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetPatch')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetPatch')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_patch(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                patch_key=request.pop(util.camelize('patchKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetPatch',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patch',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_pipeline(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetPipeline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetPipeline')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetPipeline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_pipeline(
                workspace_id=request.pop(util.camelize('workspaceId')),
                pipeline_key=request.pop(util.camelize('pipelineKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetPipeline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pipeline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_pipeline_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetPipelineValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetPipelineValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetPipelineValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_pipeline_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                pipeline_validation_key=request.pop(util.camelize('pipelineValidationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetPipelineValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pipelineValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_project(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetProject')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_project(
                workspace_id=request.pop(util.camelize('workspaceId')),
                project_key=request.pop(util.camelize('projectKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_published_object(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetPublishedObject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetPublishedObject')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetPublishedObject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_published_object(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                published_object_key=request.pop(util.camelize('publishedObjectKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetPublishedObject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publishedObject',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_reference(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetReference'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetReference')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetReference')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_reference(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                reference_key=request.pop(util.camelize('referenceKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetReference',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'reference',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_schedule(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                schedule_key=request.pop(util.camelize('scheduleKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schedule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_schema(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetSchema'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetSchema')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetSchema')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_schema(
                workspace_id=request.pop(util.camelize('workspaceId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetSchema',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schema',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_task(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetTask')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_task(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_key=request.pop(util.camelize('taskKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'task',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_task_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetTaskRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetTaskRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetTaskRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_task_run(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                task_run_key=request.pop(util.camelize('taskRunKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetTaskRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taskRun',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_task_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetTaskSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetTaskSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetTaskSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_task_schedule(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                task_schedule_key=request.pop(util.camelize('taskScheduleKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetTaskSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taskSchedule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_task_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetTaskValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetTaskValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetTaskValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_task_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_validation_key=request.pop(util.camelize('taskValidationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetTaskValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taskValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_user_defined_function(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetUserDefinedFunction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetUserDefinedFunction')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetUserDefinedFunction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_user_defined_function(
                workspace_id=request.pop(util.camelize('workspaceId')),
                user_defined_function_key=request.pop(util.camelize('userDefinedFunctionKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetUserDefinedFunction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userDefinedFunction',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_user_defined_function_validation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetUserDefinedFunctionValidation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetUserDefinedFunctionValidation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetUserDefinedFunctionValidation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_user_defined_function_validation(
                workspace_id=request.pop(util.camelize('workspaceId')),
                user_defined_function_validation_key=request.pop(util.camelize('userDefinedFunctionValidationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetUserDefinedFunctionValidation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userDefinedFunctionValidation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_get_workspace(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'GetWorkspace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'GetWorkspace')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='GetWorkspace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.get_workspace(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'GetWorkspace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workspace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_applications(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListApplications'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListApplications')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListApplications')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_applications(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_applications(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_applications(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListApplications',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'applicationSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_connection_validations(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListConnectionValidations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListConnectionValidations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListConnectionValidations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_connection_validations(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_connection_validations(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_connection_validations(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListConnectionValidations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectionValidationSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_connections(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListConnections')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_connections(
                workspace_id=request.pop(util.camelize('workspaceId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_connections(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    data_asset_key=request.pop(util.camelize('dataAssetKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_connections(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        data_asset_key=request.pop(util.camelize('dataAssetKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListConnections',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectionSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_data_assets(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListDataAssets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListDataAssets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListDataAssets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_data_assets(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_assets(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_assets(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListDataAssets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAssetSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_data_entities(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListDataEntities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListDataEntities')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListDataEntities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_data_entities(
                workspace_id=request.pop(util.camelize('workspaceId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_entities(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    connection_key=request.pop(util.camelize('connectionKey')),
                    schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_entities(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        connection_key=request.pop(util.camelize('connectionKey')),
                        schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListDataEntities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataEntitySummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_data_flow_validations(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListDataFlowValidations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListDataFlowValidations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListDataFlowValidations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_data_flow_validations(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_flow_validations(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_flow_validations(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListDataFlowValidations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataFlowValidationSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_data_flows(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListDataFlows'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListDataFlows')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListDataFlows')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_data_flows(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_flows(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_flows(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListDataFlows',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataFlowSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_dependent_objects(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListDependentObjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListDependentObjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListDependentObjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_dependent_objects(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_dependent_objects(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    application_key=request.pop(util.camelize('applicationKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_dependent_objects(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        application_key=request.pop(util.camelize('applicationKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListDependentObjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dependentObjectSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_external_publication_validations(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListExternalPublicationValidations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListExternalPublicationValidations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListExternalPublicationValidations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_external_publication_validations(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_key=request.pop(util.camelize('taskKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_publication_validations(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    task_key=request.pop(util.camelize('taskKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_publication_validations(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        task_key=request.pop(util.camelize('taskKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListExternalPublicationValidations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalPublicationValidationSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_external_publications(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListExternalPublications'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListExternalPublications')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListExternalPublications')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_external_publications(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_key=request.pop(util.camelize('taskKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_external_publications(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    task_key=request.pop(util.camelize('taskKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_external_publications(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        task_key=request.pop(util.camelize('taskKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListExternalPublications',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalPublicationSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_folders(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListFolders'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListFolders')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListFolders')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_folders(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_folders(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_folders(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListFolders',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folderSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_function_libraries(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListFunctionLibraries'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListFunctionLibraries')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListFunctionLibraries')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_function_libraries(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_function_libraries(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_function_libraries(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListFunctionLibraries',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'functionLibrarySummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_patch_changes(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListPatchChanges'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListPatchChanges')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListPatchChanges')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_patch_changes(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_patch_changes(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    application_key=request.pop(util.camelize('applicationKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_patch_changes(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        application_key=request.pop(util.camelize('applicationKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListPatchChanges',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patchChangeSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_patches(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListPatches'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListPatches')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListPatches')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_patches(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_patches(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    application_key=request.pop(util.camelize('applicationKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_patches(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        application_key=request.pop(util.camelize('applicationKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListPatches',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'patchSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_pipeline_validations(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListPipelineValidations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListPipelineValidations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListPipelineValidations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_pipeline_validations(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_pipeline_validations(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_pipeline_validations(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListPipelineValidations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pipelineValidationSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_pipelines(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListPipelines'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListPipelines')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListPipelines')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_pipelines(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_pipelines(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_pipelines(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListPipelines',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pipelineSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_projects(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListProjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListProjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListProjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_projects(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_projects(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_projects(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListProjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'projectSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_published_objects(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListPublishedObjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListPublishedObjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListPublishedObjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_published_objects(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_published_objects(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    application_key=request.pop(util.camelize('applicationKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_published_objects(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        application_key=request.pop(util.camelize('applicationKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListPublishedObjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'publishedObjectSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_references(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListReferences'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListReferences')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListReferences')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_references(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_references(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    application_key=request.pop(util.camelize('applicationKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_references(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        application_key=request.pop(util.camelize('applicationKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListReferences',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'referenceSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_schedules(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListSchedules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListSchedules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListSchedules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_schedules(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_schedules(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    application_key=request.pop(util.camelize('applicationKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_schedules(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        application_key=request.pop(util.camelize('applicationKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListSchedules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'scheduleSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_schemas(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListSchemas'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListSchemas')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListSchemas')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_schemas(
                workspace_id=request.pop(util.camelize('workspaceId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_schemas(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    connection_key=request.pop(util.camelize('connectionKey')),
                    schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_schemas(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        connection_key=request.pop(util.camelize('connectionKey')),
                        schema_resource_name=request.pop(util.camelize('schemaResourceName')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListSchemas',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schemaSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_task_run_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListTaskRunLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListTaskRunLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListTaskRunLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_task_run_logs(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                task_run_key=request.pop(util.camelize('taskRunKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_task_run_logs(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    application_key=request.pop(util.camelize('applicationKey')),
                    task_run_key=request.pop(util.camelize('taskRunKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_task_run_logs(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        application_key=request.pop(util.camelize('applicationKey')),
                        task_run_key=request.pop(util.camelize('taskRunKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListTaskRunLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taskRunLogSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_task_runs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListTaskRuns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListTaskRuns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListTaskRuns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_task_runs(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_task_runs(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    application_key=request.pop(util.camelize('applicationKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_task_runs(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        application_key=request.pop(util.camelize('applicationKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListTaskRuns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taskRunSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_task_schedules(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListTaskSchedules'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListTaskSchedules')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListTaskSchedules')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_task_schedules(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_task_schedules(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    application_key=request.pop(util.camelize('applicationKey')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_task_schedules(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        application_key=request.pop(util.camelize('applicationKey')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListTaskSchedules',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taskScheduleSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_task_validations(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListTaskValidations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListTaskValidations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListTaskValidations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_task_validations(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_task_validations(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_task_validations(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListTaskValidations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taskValidationSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_tasks(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListTasks'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListTasks')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListTasks')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_tasks(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_tasks(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_tasks(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListTasks',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taskSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_user_defined_function_validations(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListUserDefinedFunctionValidations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListUserDefinedFunctionValidations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListUserDefinedFunctionValidations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_user_defined_function_validations(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_user_defined_function_validations(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_user_defined_function_validations(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListUserDefinedFunctionValidations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userDefinedFunctionValidationSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_user_defined_functions(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListUserDefinedFunctions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListUserDefinedFunctions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListUserDefinedFunctions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_user_defined_functions(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_user_defined_functions(
                    workspace_id=request.pop(util.camelize('workspaceId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_user_defined_functions(
                        workspace_id=request.pop(util.camelize('workspaceId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListUserDefinedFunctions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userDefinedFunctionSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('workRequestId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('workRequestId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_list_workspaces(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'ListWorkspaces'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'ListWorkspaces')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='ListWorkspaces')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.list_workspaces(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_workspaces(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_workspaces(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'ListWorkspaces',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workspaceSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_start_workspace(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'StartWorkspace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'StartWorkspace')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='StartWorkspace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.start_workspace(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'StartWorkspace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'start_workspace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_stop_workspace(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'StopWorkspace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'StopWorkspace')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='StopWorkspace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.stop_workspace(
                workspace_id=request.pop(util.camelize('workspaceId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'StopWorkspace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stop_workspace',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_application(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateApplication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateApplication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateApplication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_application(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                update_application_details=request.pop(util.camelize('UpdateApplicationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateApplication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'application',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_connection(
                workspace_id=request.pop(util.camelize('workspaceId')),
                connection_key=request.pop(util.camelize('connectionKey')),
                update_connection_details=request.pop(util.camelize('UpdateConnectionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_data_asset(
                workspace_id=request.pop(util.camelize('workspaceId')),
                data_asset_key=request.pop(util.camelize('dataAssetKey')),
                update_data_asset_details=request.pop(util.camelize('UpdateDataAssetDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_data_flow(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateDataFlow'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateDataFlow')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateDataFlow')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_data_flow(
                workspace_id=request.pop(util.camelize('workspaceId')),
                data_flow_key=request.pop(util.camelize('dataFlowKey')),
                update_data_flow_details=request.pop(util.camelize('UpdateDataFlowDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateDataFlow',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataFlow',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_external_publication(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateExternalPublication'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateExternalPublication')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateExternalPublication')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_external_publication(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_key=request.pop(util.camelize('taskKey')),
                external_publications_key=request.pop(util.camelize('externalPublicationsKey')),
                update_external_publication_details=request.pop(util.camelize('UpdateExternalPublicationDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateExternalPublication',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'externalPublication',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_folder(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateFolder'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateFolder')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateFolder')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_folder(
                workspace_id=request.pop(util.camelize('workspaceId')),
                folder_key=request.pop(util.camelize('folderKey')),
                update_folder_details=request.pop(util.camelize('UpdateFolderDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateFolder',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'folder',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_function_library(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateFunctionLibrary'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateFunctionLibrary')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateFunctionLibrary')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_function_library(
                workspace_id=request.pop(util.camelize('workspaceId')),
                function_library_key=request.pop(util.camelize('functionLibraryKey')),
                update_function_library_details=request.pop(util.camelize('UpdateFunctionLibraryDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateFunctionLibrary',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'functionLibrary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_pipeline(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdatePipeline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdatePipeline')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdatePipeline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_pipeline(
                workspace_id=request.pop(util.camelize('workspaceId')),
                pipeline_key=request.pop(util.camelize('pipelineKey')),
                update_pipeline_details=request.pop(util.camelize('UpdatePipelineDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdatePipeline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'pipeline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_project(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateProject')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_project(
                workspace_id=request.pop(util.camelize('workspaceId')),
                project_key=request.pop(util.camelize('projectKey')),
                update_project_details=request.pop(util.camelize('UpdateProjectDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_reference(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateReference'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateReference')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateReference')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_reference(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                reference_key=request.pop(util.camelize('referenceKey')),
                update_reference_details=request.pop(util.camelize('UpdateReferenceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateReference',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'reference',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_schedule(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                schedule_key=request.pop(util.camelize('scheduleKey')),
                update_schedule_details=request.pop(util.camelize('UpdateScheduleDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'schedule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_task(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateTask')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_task(
                workspace_id=request.pop(util.camelize('workspaceId')),
                task_key=request.pop(util.camelize('taskKey')),
                update_task_details=request.pop(util.camelize('UpdateTaskDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'task',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_task_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateTaskRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateTaskRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateTaskRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_task_run(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                task_run_key=request.pop(util.camelize('taskRunKey')),
                update_task_run_details=request.pop(util.camelize('UpdateTaskRunDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateTaskRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taskRunDetails',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_task_schedule(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateTaskSchedule'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateTaskSchedule')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateTaskSchedule')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_task_schedule(
                workspace_id=request.pop(util.camelize('workspaceId')),
                application_key=request.pop(util.camelize('applicationKey')),
                task_schedule_key=request.pop(util.camelize('taskScheduleKey')),
                update_task_schedule_details=request.pop(util.camelize('UpdateTaskScheduleDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateTaskSchedule',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'taskSchedule',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_user_defined_function(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateUserDefinedFunction'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateUserDefinedFunction')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateUserDefinedFunction')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_user_defined_function(
                workspace_id=request.pop(util.camelize('workspaceId')),
                user_defined_function_key=request.pop(util.camelize('userDefinedFunctionKey')),
                update_user_defined_function_details=request.pop(util.camelize('UpdateUserDefinedFunctionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateUserDefinedFunction',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'userDefinedFunction',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="di_dis_ww_grp@oracle.com" jiraProject="DI" opsJiraProject="DIS"
def test_update_workspace(testing_service_client):
    if not testing_service_client.is_api_enabled('data_integration', 'UpdateWorkspace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_integration', util.camelize('data_integration'), 'UpdateWorkspace')
    )

    request_containers = testing_service_client.get_requests(service_name='data_integration', api_name='UpdateWorkspace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_integration.DataIntegrationClient(config, service_endpoint=service_endpoint)
            response = client.update_workspace(
                workspace_id=request.pop(util.camelize('workspaceId')),
                update_workspace_details=request.pop(util.camelize('UpdateWorkspaceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_integration',
            'UpdateWorkspace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workspace',
            False,
            False
        )
