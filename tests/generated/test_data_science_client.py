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

        cassette_location = os.path.join('generated', 'data_science_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_activate_model(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ActivateModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ActivateModel')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ActivateModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.activate_model(
                model_id=request.pop(util.camelize('modelId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ActivateModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'model',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_activate_model_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ActivateModelDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ActivateModelDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ActivateModelDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.activate_model_deployment(
                model_deployment_id=request.pop(util.camelize('modelDeploymentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ActivateModelDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'activate_model_deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_activate_notebook_session(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ActivateNotebookSession'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ActivateNotebookSession')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ActivateNotebookSession')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.activate_notebook_session(
                notebook_session_id=request.pop(util.camelize('notebookSessionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ActivateNotebookSession',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'activate_notebook_session',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_cancel_job_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'CancelJobRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'CancelJobRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='CancelJobRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.cancel_job_run(
                job_run_id=request.pop(util.camelize('jobRunId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'CancelJobRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_job_run',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_cancel_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'CancelWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='CancelWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.cancel_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'CancelWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_change_job_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ChangeJobCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ChangeJobCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ChangeJobCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.change_job_compartment(
                job_id=request.pop(util.camelize('jobId')),
                change_job_compartment_details=request.pop(util.camelize('ChangeJobCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ChangeJobCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_job_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_change_job_run_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ChangeJobRunCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ChangeJobRunCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ChangeJobRunCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.change_job_run_compartment(
                job_run_id=request.pop(util.camelize('jobRunId')),
                change_job_run_compartment_details=request.pop(util.camelize('ChangeJobRunCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ChangeJobRunCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_job_run_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_change_model_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ChangeModelCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ChangeModelCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ChangeModelCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.change_model_compartment(
                model_id=request.pop(util.camelize('modelId')),
                change_model_compartment_details=request.pop(util.camelize('ChangeModelCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ChangeModelCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_model_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_change_model_deployment_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ChangeModelDeploymentCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ChangeModelDeploymentCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ChangeModelDeploymentCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.change_model_deployment_compartment(
                model_deployment_id=request.pop(util.camelize('modelDeploymentId')),
                change_model_deployment_compartment_details=request.pop(util.camelize('ChangeModelDeploymentCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ChangeModelDeploymentCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_model_deployment_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_change_notebook_session_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ChangeNotebookSessionCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ChangeNotebookSessionCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ChangeNotebookSessionCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.change_notebook_session_compartment(
                notebook_session_id=request.pop(util.camelize('notebookSessionId')),
                change_notebook_session_compartment_details=request.pop(util.camelize('ChangeNotebookSessionCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ChangeNotebookSessionCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_notebook_session_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_change_project_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ChangeProjectCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ChangeProjectCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ChangeProjectCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.change_project_compartment(
                project_id=request.pop(util.camelize('projectId')),
                change_project_compartment_details=request.pop(util.camelize('ChangeProjectCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ChangeProjectCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_project_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_create_job(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'CreateJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'CreateJob')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='CreateJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.create_job(
                create_job_details=request.pop(util.camelize('CreateJobDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'CreateJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_create_job_artifact(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'CreateJobArtifact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'CreateJobArtifact')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='CreateJobArtifact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.create_job_artifact(
                job_id=request.pop(util.camelize('jobId')),
                job_artifact=request.pop(util.camelize('JobArtifact')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'CreateJobArtifact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_job_artifact',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_create_job_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'CreateJobRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'CreateJobRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='CreateJobRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.create_job_run(
                create_job_run_details=request.pop(util.camelize('CreateJobRunDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'CreateJobRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobRun',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_create_model(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'CreateModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'CreateModel')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='CreateModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.create_model(
                create_model_details=request.pop(util.camelize('CreateModelDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'CreateModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'model',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_create_model_artifact(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'CreateModelArtifact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'CreateModelArtifact')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='CreateModelArtifact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.create_model_artifact(
                model_id=request.pop(util.camelize('modelId')),
                model_artifact=request.pop(util.camelize('ModelArtifact')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'CreateModelArtifact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_model_artifact',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_create_model_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'CreateModelDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'CreateModelDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='CreateModelDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.create_model_deployment(
                create_model_deployment_details=request.pop(util.camelize('CreateModelDeploymentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'CreateModelDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'modelDeployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_create_model_provenance(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'CreateModelProvenance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'CreateModelProvenance')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='CreateModelProvenance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.create_model_provenance(
                model_id=request.pop(util.camelize('modelId')),
                create_model_provenance_details=request.pop(util.camelize('CreateModelProvenanceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'CreateModelProvenance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'modelProvenance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_create_notebook_session(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'CreateNotebookSession'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'CreateNotebookSession')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='CreateNotebookSession')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.create_notebook_session(
                create_notebook_session_details=request.pop(util.camelize('CreateNotebookSessionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'CreateNotebookSession',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'notebookSession',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_create_project(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'CreateProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'CreateProject')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='CreateProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.create_project(
                create_project_details=request.pop(util.camelize('CreateProjectDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'CreateProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_deactivate_model(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'DeactivateModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'DeactivateModel')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='DeactivateModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.deactivate_model(
                model_id=request.pop(util.camelize('modelId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'DeactivateModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'model',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_deactivate_model_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'DeactivateModelDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'DeactivateModelDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='DeactivateModelDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.deactivate_model_deployment(
                model_deployment_id=request.pop(util.camelize('modelDeploymentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'DeactivateModelDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deactivate_model_deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_deactivate_notebook_session(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'DeactivateNotebookSession'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'DeactivateNotebookSession')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='DeactivateNotebookSession')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.deactivate_notebook_session(
                notebook_session_id=request.pop(util.camelize('notebookSessionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'DeactivateNotebookSession',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'deactivate_notebook_session',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_delete_job(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'DeleteJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'DeleteJob')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='DeleteJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.delete_job(
                job_id=request.pop(util.camelize('jobId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'DeleteJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_job',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_delete_job_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'DeleteJobRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'DeleteJobRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='DeleteJobRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.delete_job_run(
                job_run_id=request.pop(util.camelize('jobRunId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'DeleteJobRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_job_run',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_delete_model(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'DeleteModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'DeleteModel')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='DeleteModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.delete_model(
                model_id=request.pop(util.camelize('modelId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'DeleteModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_model',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_delete_model_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'DeleteModelDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'DeleteModelDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='DeleteModelDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.delete_model_deployment(
                model_deployment_id=request.pop(util.camelize('modelDeploymentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'DeleteModelDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_model_deployment',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_delete_notebook_session(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'DeleteNotebookSession'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'DeleteNotebookSession')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='DeleteNotebookSession')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.delete_notebook_session(
                notebook_session_id=request.pop(util.camelize('notebookSessionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'DeleteNotebookSession',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_notebook_session',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_delete_project(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'DeleteProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'DeleteProject')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='DeleteProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.delete_project(
                project_id=request.pop(util.camelize('projectId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'DeleteProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_project',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_get_job(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'GetJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'GetJob')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='GetJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.get_job(
                job_id=request.pop(util.camelize('jobId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'GetJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_get_job_artifact_content(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'GetJobArtifactContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'GetJobArtifactContent')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='GetJobArtifactContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.get_job_artifact_content(
                job_id=request.pop(util.camelize('jobId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'GetJobArtifactContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_get_job_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'GetJobRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'GetJobRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='GetJobRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.get_job_run(
                job_run_id=request.pop(util.camelize('jobRunId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'GetJobRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobRun',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_get_model(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'GetModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'GetModel')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='GetModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.get_model(
                model_id=request.pop(util.camelize('modelId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'GetModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'model',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_get_model_artifact_content(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'GetModelArtifactContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'GetModelArtifactContent')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='GetModelArtifactContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.get_model_artifact_content(
                model_id=request.pop(util.camelize('modelId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'GetModelArtifactContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_get_model_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'GetModelDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'GetModelDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='GetModelDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.get_model_deployment(
                model_deployment_id=request.pop(util.camelize('modelDeploymentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'GetModelDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'modelDeployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_get_model_provenance(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'GetModelProvenance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'GetModelProvenance')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='GetModelProvenance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.get_model_provenance(
                model_id=request.pop(util.camelize('modelId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'GetModelProvenance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'modelProvenance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_get_notebook_session(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'GetNotebookSession'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'GetNotebookSession')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='GetNotebookSession')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.get_notebook_session(
                notebook_session_id=request.pop(util.camelize('notebookSessionId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'GetNotebookSession',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'notebookSession',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_get_project(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'GetProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'GetProject')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='GetProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.get_project(
                project_id=request.pop(util.camelize('projectId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'GetProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_head_job_artifact(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'HeadJobArtifact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'HeadJobArtifact')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='HeadJobArtifact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.head_job_artifact(
                job_id=request.pop(util.camelize('jobId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'HeadJobArtifact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'head_job_artifact',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_head_model_artifact(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'HeadModelArtifact'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'HeadModelArtifact')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='HeadModelArtifact')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.head_model_artifact(
                model_id=request.pop(util.camelize('modelId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'HeadModelArtifact',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'head_model_artifact',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_list_job_runs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ListJobRuns'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ListJobRuns')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ListJobRuns')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.list_job_runs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_job_runs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_job_runs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ListJobRuns',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobRunSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_list_job_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ListJobShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ListJobShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ListJobShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.list_job_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_job_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_job_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ListJobShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobShapeSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_list_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ListJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ListJobs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ListJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.list_jobs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_jobs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_jobs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ListJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_list_model_deployment_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ListModelDeploymentShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ListModelDeploymentShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ListModelDeploymentShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.list_model_deployment_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_model_deployment_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_model_deployment_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ListModelDeploymentShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'modelDeploymentShapeSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_list_model_deployments(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ListModelDeployments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ListModelDeployments')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ListModelDeployments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.list_model_deployments(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_model_deployments(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_model_deployments(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ListModelDeployments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'modelDeploymentSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_list_models(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ListModels'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ListModels')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ListModels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.list_models(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_models(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_models(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ListModels',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'modelSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_list_notebook_session_shapes(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ListNotebookSessionShapes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ListNotebookSessionShapes')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ListNotebookSessionShapes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.list_notebook_session_shapes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_notebook_session_shapes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_notebook_session_shapes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ListNotebookSessionShapes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'notebookSessionShapeSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_list_notebook_sessions(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ListNotebookSessions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ListNotebookSessions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ListNotebookSessions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.list_notebook_sessions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_notebook_sessions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_notebook_sessions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ListNotebookSessions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'notebookSessionSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_list_projects(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ListProjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ListProjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ListProjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
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
            'data_science',
            'ListProjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'projectSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ListWorkRequestErrors')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ListWorkRequestLogs')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('workRequestId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
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
            'data_science',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_update_job(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'UpdateJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'UpdateJob')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='UpdateJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.update_job(
                job_id=request.pop(util.camelize('jobId')),
                update_job_details=request.pop(util.camelize('UpdateJobDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'UpdateJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_update_job_run(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'UpdateJobRun'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'UpdateJobRun')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='UpdateJobRun')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.update_job_run(
                job_run_id=request.pop(util.camelize('jobRunId')),
                update_job_run_details=request.pop(util.camelize('UpdateJobRunDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'UpdateJobRun',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'jobRun',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_update_model(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'UpdateModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'UpdateModel')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='UpdateModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.update_model(
                model_id=request.pop(util.camelize('modelId')),
                update_model_details=request.pop(util.camelize('UpdateModelDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'UpdateModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'model',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_update_model_deployment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'UpdateModelDeployment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'UpdateModelDeployment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='UpdateModelDeployment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.update_model_deployment(
                model_deployment_id=request.pop(util.camelize('modelDeploymentId')),
                update_model_deployment_details=request.pop(util.camelize('UpdateModelDeploymentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'UpdateModelDeployment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_model_deployment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_update_model_provenance(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'UpdateModelProvenance'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'UpdateModelProvenance')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='UpdateModelProvenance')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.update_model_provenance(
                model_id=request.pop(util.camelize('modelId')),
                update_model_provenance_details=request.pop(util.camelize('UpdateModelProvenanceDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'UpdateModelProvenance',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'modelProvenance',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_update_notebook_session(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'UpdateNotebookSession'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'UpdateNotebookSession')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='UpdateNotebookSession')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.update_notebook_session(
                notebook_session_id=request.pop(util.camelize('notebookSessionId')),
                update_notebook_session_details=request.pop(util.camelize('UpdateNotebookSessionDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'UpdateNotebookSession',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'notebookSession',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="datascience_grp@oracle.com" jiraProject="ODSC" opsJiraProject="ODSC"
def test_update_project(testing_service_client):
    if not testing_service_client.is_api_enabled('data_science', 'UpdateProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_science', util.camelize('data_science'), 'UpdateProject')
    )

    request_containers = testing_service_client.get_requests(service_name='data_science', api_name='UpdateProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_science.DataScienceClient(config, service_endpoint=service_endpoint)
            response = client.update_project(
                project_id=request.pop(util.camelize('projectId')),
                update_project_details=request.pop(util.camelize('UpdateProjectDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_science',
            'UpdateProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )
