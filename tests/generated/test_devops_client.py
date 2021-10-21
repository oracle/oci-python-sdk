# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'devops_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_approve_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ApproveDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ApproveDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ApproveDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.approve_deployment(
                deployment_id=request.pop(util.camelize('deploymentId')),
                approve_deployment_details=request.pop(util.camelize('ApproveDeploymentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ApproveDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_cancel_build_run(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CancelBuildRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CancelBuildRun')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CancelBuildRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.cancel_build_run(
                cancel_build_run_details=request.pop(util.camelize('CancelBuildRunDetails')),
                build_run_id=request.pop(util.camelize('buildRunId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CancelBuildRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'buildRun',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_cancel_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CancelDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CancelDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CancelDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.cancel_deployment(
                deployment_id=request.pop(util.camelize('deploymentId')),
                cancel_deployment_details=request.pop(util.camelize('CancelDeploymentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CancelDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_project_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ChangeProjectCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ChangeProjectCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ChangeProjectCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.change_project_compartment(
                project_id=request.pop(util.camelize('projectId')),
                change_project_compartment_details=request.pop(util.camelize('ChangeProjectCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ChangeProjectCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_project_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_build_pipeline(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CreateBuildPipeline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CreateBuildPipeline')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CreateBuildPipeline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.create_build_pipeline(
                create_build_pipeline_details=request.pop(util.camelize('CreateBuildPipelineDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CreateBuildPipeline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'buildPipeline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_build_pipeline_stage(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CreateBuildPipelineStage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CreateBuildPipelineStage')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CreateBuildPipelineStage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.create_build_pipeline_stage(
                create_build_pipeline_stage_details=request.pop(util.camelize('CreateBuildPipelineStageDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CreateBuildPipelineStage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'buildPipelineStage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_build_run(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CreateBuildRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CreateBuildRun')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CreateBuildRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.create_build_run(
                create_build_run_details=request.pop(util.camelize('CreateBuildRunDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CreateBuildRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'buildRun',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CreateConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CreateConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CreateConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.create_connection(
                create_connection_details=request.pop(util.camelize('CreateConnectionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CreateConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_deploy_artifact(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CreateDeployArtifact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CreateDeployArtifact')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CreateDeployArtifact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.create_deploy_artifact(
                create_deploy_artifact_details=request.pop(util.camelize('CreateDeployArtifactDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CreateDeployArtifact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployArtifact',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_deploy_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CreateDeployEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CreateDeployEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CreateDeployEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.create_deploy_environment(
                create_deploy_environment_details=request.pop(util.camelize('CreateDeployEnvironmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CreateDeployEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployEnvironment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_deploy_pipeline(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CreateDeployPipeline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CreateDeployPipeline')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CreateDeployPipeline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.create_deploy_pipeline(
                create_deploy_pipeline_details=request.pop(util.camelize('CreateDeployPipelineDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CreateDeployPipeline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployPipeline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_deploy_stage(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CreateDeployStage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CreateDeployStage')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CreateDeployStage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.create_deploy_stage(
                create_deploy_stage_details=request.pop(util.camelize('CreateDeployStageDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CreateDeployStage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployStage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CreateDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CreateDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CreateDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.create_deployment(
                create_deployment_details=request.pop(util.camelize('CreateDeploymentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CreateDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_project(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CreateProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CreateProject')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CreateProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.create_project(
                create_project_details=request.pop(util.camelize('CreateProjectDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CreateProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_repository(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CreateRepository'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CreateRepository')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CreateRepository')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.create_repository(
                create_repository_details=request.pop(util.camelize('CreateRepositoryDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CreateRepository',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repository',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_trigger(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'CreateTrigger'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'CreateTrigger')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='CreateTrigger')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.create_trigger(
                create_trigger_details=request.pop(util.camelize('CreateTriggerDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'CreateTrigger',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'triggerCreateResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_build_pipeline(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'DeleteBuildPipeline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'DeleteBuildPipeline')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='DeleteBuildPipeline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.delete_build_pipeline(
                build_pipeline_id=request.pop(util.camelize('buildPipelineId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'DeleteBuildPipeline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_build_pipeline',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_build_pipeline_stage(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'DeleteBuildPipelineStage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'DeleteBuildPipelineStage')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='DeleteBuildPipelineStage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.delete_build_pipeline_stage(
                build_pipeline_stage_id=request.pop(util.camelize('buildPipelineStageId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'DeleteBuildPipelineStage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_build_pipeline_stage',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'DeleteConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'DeleteConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='DeleteConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.delete_connection(
                connection_id=request.pop(util.camelize('connectionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'DeleteConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_connection',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_deploy_artifact(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'DeleteDeployArtifact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'DeleteDeployArtifact')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='DeleteDeployArtifact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.delete_deploy_artifact(
                deploy_artifact_id=request.pop(util.camelize('deployArtifactId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'DeleteDeployArtifact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_deploy_artifact',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_deploy_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'DeleteDeployEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'DeleteDeployEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='DeleteDeployEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.delete_deploy_environment(
                deploy_environment_id=request.pop(util.camelize('deployEnvironmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'DeleteDeployEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_deploy_environment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_deploy_pipeline(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'DeleteDeployPipeline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'DeleteDeployPipeline')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='DeleteDeployPipeline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.delete_deploy_pipeline(
                deploy_pipeline_id=request.pop(util.camelize('deployPipelineId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'DeleteDeployPipeline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_deploy_pipeline',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_deploy_stage(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'DeleteDeployStage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'DeleteDeployStage')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='DeleteDeployStage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.delete_deploy_stage(
                deploy_stage_id=request.pop(util.camelize('deployStageId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'DeleteDeployStage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_deploy_stage',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_project(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'DeleteProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'DeleteProject')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='DeleteProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.delete_project(
                project_id=request.pop(util.camelize('projectId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'DeleteProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_project',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_ref(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'DeleteRef'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'DeleteRef')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='DeleteRef')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.delete_ref(
                repository_id=request.pop(util.camelize('repositoryId')),
                ref_name=request.pop(util.camelize('refName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'DeleteRef',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_ref',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_repository(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'DeleteRepository'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'DeleteRepository')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='DeleteRepository')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.delete_repository(
                repository_id=request.pop(util.camelize('repositoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'DeleteRepository',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_repository',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_trigger(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'DeleteTrigger'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'DeleteTrigger')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='DeleteTrigger')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.delete_trigger(
                trigger_id=request.pop(util.camelize('triggerId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'DeleteTrigger',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_trigger',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_build_pipeline(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetBuildPipeline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetBuildPipeline')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetBuildPipeline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_build_pipeline(
                build_pipeline_id=request.pop(util.camelize('buildPipelineId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetBuildPipeline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'buildPipeline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_build_pipeline_stage(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetBuildPipelineStage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetBuildPipelineStage')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetBuildPipelineStage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_build_pipeline_stage(
                build_pipeline_stage_id=request.pop(util.camelize('buildPipelineStageId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetBuildPipelineStage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'buildPipelineStage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_build_run(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetBuildRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetBuildRun')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetBuildRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_build_run(
                build_run_id=request.pop(util.camelize('buildRunId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetBuildRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'buildRun',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_commit(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetCommit'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetCommit')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetCommit')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_commit(
                repository_id=request.pop(util.camelize('repositoryId')),
                commit_id=request.pop(util.camelize('commitId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetCommit',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repositoryCommit',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_commit_diff(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetCommitDiff'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetCommitDiff')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetCommitDiff')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_commit_diff(
                repository_id=request.pop(util.camelize('repositoryId')),
                target_version=request.pop(util.camelize('targetVersion')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetCommitDiff',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'diffResponse',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_connection(
                connection_id=request.pop(util.camelize('connectionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_deploy_artifact(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetDeployArtifact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetDeployArtifact')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetDeployArtifact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_deploy_artifact(
                deploy_artifact_id=request.pop(util.camelize('deployArtifactId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetDeployArtifact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployArtifact',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_deploy_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetDeployEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetDeployEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetDeployEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_deploy_environment(
                deploy_environment_id=request.pop(util.camelize('deployEnvironmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetDeployEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployEnvironment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_deploy_pipeline(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetDeployPipeline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetDeployPipeline')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetDeployPipeline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_deploy_pipeline(
                deploy_pipeline_id=request.pop(util.camelize('deployPipelineId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetDeployPipeline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployPipeline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_deploy_stage(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetDeployStage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetDeployStage')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetDeployStage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_deploy_stage(
                deploy_stage_id=request.pop(util.camelize('deployStageId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetDeployStage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployStage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_deployment(
                deployment_id=request.pop(util.camelize('deploymentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_file_diff(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetFileDiff'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetFileDiff')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetFileDiff')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_file_diff(
                repository_id=request.pop(util.camelize('repositoryId')),
                file_path=request.pop(util.camelize('filePath')),
                base_version=request.pop(util.camelize('baseVersion')),
                target_version=request.pop(util.camelize('targetVersion')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetFileDiff',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fileDiffResponse',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_mirror_record(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetMirrorRecord'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetMirrorRecord')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetMirrorRecord')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_mirror_record(
                repository_id=request.pop(util.camelize('repositoryId')),
                mirror_record_type=request.pop(util.camelize('mirrorRecordType')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetMirrorRecord',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repositoryMirrorRecord',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_object(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetObject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetObject')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetObject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_object(
                repository_id=request.pop(util.camelize('repositoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetObject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repositoryObject',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_object_content(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetObjectContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetObjectContent')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetObjectContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_object_content(
                repository_id=request.pop(util.camelize('repositoryId')),
                sha=request.pop(util.camelize('sha')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetObjectContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_project(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetProject')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_project(
                project_id=request.pop(util.camelize('projectId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_ref(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetRef'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetRef')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetRef')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_ref(
                repository_id=request.pop(util.camelize('repositoryId')),
                ref_name=request.pop(util.camelize('refName')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetRef',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repositoryRef',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_repository(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetRepository'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetRepository')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetRepository')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_repository(
                repository_id=request.pop(util.camelize('repositoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetRepository',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repository',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_repository_archive_content(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetRepositoryArchiveContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetRepositoryArchiveContent')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetRepositoryArchiveContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_repository_archive_content(
                repository_id=request.pop(util.camelize('repositoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetRepositoryArchiveContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_repository_file_lines(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetRepositoryFileLines'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetRepositoryFileLines')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetRepositoryFileLines')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_repository_file_lines(
                repository_id=request.pop(util.camelize('repositoryId')),
                file_path=request.pop(util.camelize('filePath')),
                revision=request.pop(util.camelize('revision')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetRepositoryFileLines',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repositoryFileLines',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_trigger(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetTrigger'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetTrigger')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetTrigger')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_trigger(
                trigger_id=request.pop(util.camelize('triggerId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetTrigger',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'trigger',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_authors(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListAuthors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListAuthors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListAuthors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_authors(
                repository_id=request.pop(util.camelize('repositoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_authors(
                    repository_id=request.pop(util.camelize('repositoryId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_authors(
                        repository_id=request.pop(util.camelize('repositoryId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListAuthors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repositoryAuthorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_build_pipeline_stages(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListBuildPipelineStages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListBuildPipelineStages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListBuildPipelineStages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_build_pipeline_stages(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_build_pipeline_stages(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_build_pipeline_stages(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListBuildPipelineStages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'buildPipelineStageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_build_pipelines(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListBuildPipelines'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListBuildPipelines')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListBuildPipelines')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_build_pipelines(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_build_pipelines(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_build_pipelines(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListBuildPipelines',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'buildPipelineCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_build_runs(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListBuildRuns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListBuildRuns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListBuildRuns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_build_runs(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_build_runs(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_build_runs(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListBuildRuns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'buildRunSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_commit_diffs(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListCommitDiffs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListCommitDiffs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListCommitDiffs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_commit_diffs(
                repository_id=request.pop(util.camelize('repositoryId')),
                base_version=request.pop(util.camelize('baseVersion')),
                target_version=request.pop(util.camelize('targetVersion')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_commit_diffs(
                    repository_id=request.pop(util.camelize('repositoryId')),
                    base_version=request.pop(util.camelize('baseVersion')),
                    target_version=request.pop(util.camelize('targetVersion')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_commit_diffs(
                        repository_id=request.pop(util.camelize('repositoryId')),
                        base_version=request.pop(util.camelize('baseVersion')),
                        target_version=request.pop(util.camelize('targetVersion')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListCommitDiffs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'diffCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_commits(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListCommits'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListCommits')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListCommits')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_commits(
                repository_id=request.pop(util.camelize('repositoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_commits(
                    repository_id=request.pop(util.camelize('repositoryId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_commits(
                        repository_id=request.pop(util.camelize('repositoryId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListCommits',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repositoryCommitCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_connections(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListConnections'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListConnections')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListConnections')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_connections(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_connections(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_connections(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListConnections',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connectionCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_deploy_artifacts(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListDeployArtifacts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListDeployArtifacts')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListDeployArtifacts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_deploy_artifacts(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_deploy_artifacts(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_deploy_artifacts(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListDeployArtifacts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployArtifactCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_deploy_environments(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListDeployEnvironments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListDeployEnvironments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListDeployEnvironments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_deploy_environments(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_deploy_environments(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_deploy_environments(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListDeployEnvironments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployEnvironmentCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_deploy_pipelines(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListDeployPipelines'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListDeployPipelines')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListDeployPipelines')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_deploy_pipelines(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_deploy_pipelines(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_deploy_pipelines(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListDeployPipelines',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployPipelineCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_deploy_stages(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListDeployStages'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListDeployStages')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListDeployStages')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_deploy_stages(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_deploy_stages(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_deploy_stages(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListDeployStages',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployStageCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_deployments(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListDeployments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListDeployments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListDeployments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_deployments(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_deployments(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_deployments(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListDeployments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deploymentCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_mirror_records(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListMirrorRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListMirrorRecords')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListMirrorRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_mirror_records(
                repository_id=request.pop(util.camelize('repositoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_mirror_records(
                    repository_id=request.pop(util.camelize('repositoryId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_mirror_records(
                        repository_id=request.pop(util.camelize('repositoryId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListMirrorRecords',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repositoryMirrorRecordCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_paths(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListPaths'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListPaths')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListPaths')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_paths(
                repository_id=request.pop(util.camelize('repositoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_paths(
                    repository_id=request.pop(util.camelize('repositoryId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_paths(
                        repository_id=request.pop(util.camelize('repositoryId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListPaths',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repositoryPathCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_projects(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListProjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListProjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListProjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_projects(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_projects(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_projects(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListProjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'projectCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_refs(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListRefs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListRefs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListRefs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_refs(
                repository_id=request.pop(util.camelize('repositoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_refs(
                    repository_id=request.pop(util.camelize('repositoryId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_refs(
                        repository_id=request.pop(util.camelize('repositoryId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListRefs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repositoryRefCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_repositories(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListRepositories'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListRepositories')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListRepositories')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_repositories(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_repositories(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_repositories(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListRepositories',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repositoryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_triggers(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListTriggers'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListTriggers')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListTriggers')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.list_triggers(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_triggers(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_triggers(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'ListTriggers',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'triggerCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
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
            'devops',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
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
            'devops',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
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
            'devops',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_mirror_repository(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'MirrorRepository'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'MirrorRepository')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='MirrorRepository')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.mirror_repository(
                repository_id=request.pop(util.camelize('repositoryId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'MirrorRepository',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mirror_repository',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_put_repository_ref(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'PutRepositoryRef'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'PutRepositoryRef')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='PutRepositoryRef')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.put_repository_ref(
                repository_id=request.pop(util.camelize('repositoryId')),
                ref_name=request.pop(util.camelize('refName')),
                put_repository_ref_details=request.pop(util.camelize('PutRepositoryRefDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'PutRepositoryRef',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repositoryRef',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_build_pipeline(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'UpdateBuildPipeline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'UpdateBuildPipeline')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='UpdateBuildPipeline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.update_build_pipeline(
                build_pipeline_id=request.pop(util.camelize('buildPipelineId')),
                update_build_pipeline_details=request.pop(util.camelize('UpdateBuildPipelineDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'UpdateBuildPipeline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'buildPipeline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_build_pipeline_stage(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'UpdateBuildPipelineStage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'UpdateBuildPipelineStage')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='UpdateBuildPipelineStage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.update_build_pipeline_stage(
                build_pipeline_stage_id=request.pop(util.camelize('buildPipelineStageId')),
                update_build_pipeline_stage_details=request.pop(util.camelize('UpdateBuildPipelineStageDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'UpdateBuildPipelineStage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'buildPipelineStage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_build_run(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'UpdateBuildRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'UpdateBuildRun')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='UpdateBuildRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.update_build_run(
                build_run_id=request.pop(util.camelize('buildRunId')),
                update_build_run_details=request.pop(util.camelize('UpdateBuildRunDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'UpdateBuildRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'buildRun',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_connection(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'UpdateConnection'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'UpdateConnection')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='UpdateConnection')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.update_connection(
                connection_id=request.pop(util.camelize('connectionId')),
                update_connection_details=request.pop(util.camelize('UpdateConnectionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'UpdateConnection',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'connection',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_deploy_artifact(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'UpdateDeployArtifact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'UpdateDeployArtifact')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='UpdateDeployArtifact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.update_deploy_artifact(
                deploy_artifact_id=request.pop(util.camelize('deployArtifactId')),
                update_deploy_artifact_details=request.pop(util.camelize('UpdateDeployArtifactDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'UpdateDeployArtifact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployArtifact',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_deploy_environment(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'UpdateDeployEnvironment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'UpdateDeployEnvironment')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='UpdateDeployEnvironment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.update_deploy_environment(
                deploy_environment_id=request.pop(util.camelize('deployEnvironmentId')),
                update_deploy_environment_details=request.pop(util.camelize('UpdateDeployEnvironmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'UpdateDeployEnvironment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployEnvironment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_deploy_pipeline(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'UpdateDeployPipeline'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'UpdateDeployPipeline')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='UpdateDeployPipeline')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.update_deploy_pipeline(
                deploy_pipeline_id=request.pop(util.camelize('deployPipelineId')),
                update_deploy_pipeline_details=request.pop(util.camelize('UpdateDeployPipelineDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'UpdateDeployPipeline',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployPipeline',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_deploy_stage(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'UpdateDeployStage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'UpdateDeployStage')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='UpdateDeployStage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.update_deploy_stage(
                deploy_stage_id=request.pop(util.camelize('deployStageId')),
                update_deploy_stage_details=request.pop(util.camelize('UpdateDeployStageDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'UpdateDeployStage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployStage',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'UpdateDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'UpdateDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='UpdateDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.update_deployment(
                deployment_id=request.pop(util.camelize('deploymentId')),
                update_deployment_details=request.pop(util.camelize('UpdateDeploymentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'UpdateDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_project(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'UpdateProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'UpdateProject')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='UpdateProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.update_project(
                project_id=request.pop(util.camelize('projectId')),
                update_project_details=request.pop(util.camelize('UpdateProjectDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'UpdateProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_repository(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'UpdateRepository'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'UpdateRepository')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='UpdateRepository')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.update_repository(
                repository_id=request.pop(util.camelize('repositoryId')),
                update_repository_details=request.pop(util.camelize('UpdateRepositoryDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'UpdateRepository',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'repository',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_devlifecycle_group_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_trigger(testing_service_client):
    if not testing_service_client.is_api_enabled('devops', 'UpdateTrigger'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('devops', util.camelize('devops'), 'UpdateTrigger')
    )

    request_containers = testing_service_client.get_requests(service_name='devops', api_name='UpdateTrigger')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.devops.DevopsClient(config, service_endpoint=service_endpoint)
            response = client.update_trigger(
                trigger_id=request.pop(util.camelize('triggerId')),
                update_trigger_details=request.pop(util.camelize('UpdateTriggerDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'devops',
            'UpdateTrigger',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'trigger',
            False,
            False
        )
