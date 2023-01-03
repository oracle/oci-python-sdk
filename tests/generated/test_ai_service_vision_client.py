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

        cassette_location = os.path.join('generated', 'ai_vision_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_analyze_document(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'AnalyzeDocument'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'AnalyzeDocument')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='AnalyzeDocument')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.analyze_document(
                analyze_document_details=request.pop(util.camelize('AnalyzeDocumentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'AnalyzeDocument',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'analyzeDocumentResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_analyze_image(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'AnalyzeImage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'AnalyzeImage')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='AnalyzeImage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.analyze_image(
                analyze_image_details=request.pop(util.camelize('AnalyzeImageDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'AnalyzeImage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'analyzeImageResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_cancel_document_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'CancelDocumentJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'CancelDocumentJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='CancelDocumentJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.cancel_document_job(
                document_job_id=request.pop(util.camelize('documentJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'CancelDocumentJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_document_job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_cancel_image_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'CancelImageJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'CancelImageJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='CancelImageJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.cancel_image_job(
                image_job_id=request.pop(util.camelize('imageJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'CancelImageJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_image_job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_cancel_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'CancelWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='CancelWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.cancel_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'CancelWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_change_model_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'ChangeModelCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'ChangeModelCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='ChangeModelCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.change_model_compartment(
                model_id=request.pop(util.camelize('modelId')),
                change_model_compartment_details=request.pop(util.camelize('ChangeModelCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'ChangeModelCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_model_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_change_project_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'ChangeProjectCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'ChangeProjectCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='ChangeProjectCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.change_project_compartment(
                project_id=request.pop(util.camelize('projectId')),
                change_project_compartment_details=request.pop(util.camelize('ChangeProjectCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'ChangeProjectCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_project_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_create_document_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'CreateDocumentJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'CreateDocumentJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='CreateDocumentJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.create_document_job(
                create_document_job_details=request.pop(util.camelize('CreateDocumentJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'CreateDocumentJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'documentJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_create_image_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'CreateImageJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'CreateImageJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='CreateImageJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.create_image_job(
                create_image_job_details=request.pop(util.camelize('CreateImageJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'CreateImageJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'imageJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_create_model(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'CreateModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'CreateModel')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='CreateModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.create_model(
                create_model_details=request.pop(util.camelize('CreateModelDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'CreateModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'model',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_create_project(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'CreateProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'CreateProject')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='CreateProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.create_project(
                create_project_details=request.pop(util.camelize('CreateProjectDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'CreateProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_delete_model(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'DeleteModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'DeleteModel')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='DeleteModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.delete_model(
                model_id=request.pop(util.camelize('modelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'DeleteModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_model',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_delete_project(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'DeleteProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'DeleteProject')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='DeleteProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.delete_project(
                project_id=request.pop(util.camelize('projectId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'DeleteProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_project',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_get_document_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'GetDocumentJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'GetDocumentJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='GetDocumentJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.get_document_job(
                document_job_id=request.pop(util.camelize('documentJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'GetDocumentJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'documentJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_get_image_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'GetImageJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'GetImageJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='GetImageJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.get_image_job(
                image_job_id=request.pop(util.camelize('imageJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'GetImageJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'imageJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_get_model(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'GetModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'GetModel')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='GetModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.get_model(
                model_id=request.pop(util.camelize('modelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'GetModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'model',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_get_project(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'GetProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'GetProject')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='GetProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.get_project(
                project_id=request.pop(util.camelize('projectId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'GetProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_list_models(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'ListModels'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'ListModels')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='ListModels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.list_models(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_models(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_models(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'ListModels',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'modelCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_list_projects(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'ListProjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'ListProjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='ListProjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.list_projects(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_projects(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_projects(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'ListProjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'projectCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
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
            'ai_vision',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
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
            'ai_vision',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.list_work_requests(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_update_model(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'UpdateModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'UpdateModel')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='UpdateModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.update_model(
                model_id=request.pop(util.camelize('modelId')),
                update_model_details=request.pop(util.camelize('UpdateModelDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'UpdateModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_model',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="junqian_org_ww@oracle.com" jiraProject="OCASVS" opsJiraProject="OCASVS"
def test_update_project(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_vision', 'UpdateProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_vision', util.camelize('ai_service_vision'), 'UpdateProject')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_vision', api_name='UpdateProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_vision.AIServiceVisionClient(config, service_endpoint=service_endpoint)
            response = client.update_project(
                project_id=request.pop(util.camelize('projectId')),
                update_project_details=request.pop(util.camelize('UpdateProjectDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_vision',
            'UpdateProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_project',
            False,
            False
        )
