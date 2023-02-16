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

        cassette_location = os.path.join('generated', 'ai_anomaly_detection_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_cancel_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'CancelWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='CancelWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.cancel_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'CancelWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_change_ai_private_endpoint_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'ChangeAiPrivateEndpointCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'ChangeAiPrivateEndpointCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='ChangeAiPrivateEndpointCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.change_ai_private_endpoint_compartment(
                ai_private_endpoint_id=request.pop(util.camelize('aiPrivateEndpointId')),
                change_ai_private_endpoint_compartment_details=request.pop(util.camelize('ChangeAiPrivateEndpointCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'ChangeAiPrivateEndpointCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_ai_private_endpoint_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_change_data_asset_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'ChangeDataAssetCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'ChangeDataAssetCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='ChangeDataAssetCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.change_data_asset_compartment(
                data_asset_id=request.pop(util.camelize('dataAssetId')),
                change_data_asset_compartment_details=request.pop(util.camelize('ChangeDataAssetCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'ChangeDataAssetCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_change_detect_anomaly_job_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'ChangeDetectAnomalyJobCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'ChangeDetectAnomalyJobCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='ChangeDetectAnomalyJobCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.change_detect_anomaly_job_compartment(
                detect_anomaly_job_id=request.pop(util.camelize('detectAnomalyJobId')),
                change_detect_anomaly_job_compartment_details=request.pop(util.camelize('ChangeDetectAnomalyJobCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'ChangeDetectAnomalyJobCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_detect_anomaly_job_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_change_model_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'ChangeModelCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'ChangeModelCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='ChangeModelCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
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
            'ai_anomaly_detection',
            'ChangeModelCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_model_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_change_project_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'ChangeProjectCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'ChangeProjectCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='ChangeProjectCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
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
            'ai_anomaly_detection',
            'ChangeProjectCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_project_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_create_ai_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'CreateAiPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'CreateAiPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='CreateAiPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.create_ai_private_endpoint(
                create_ai_private_endpoint_details=request.pop(util.camelize('CreateAiPrivateEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'CreateAiPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_ai_private_endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_create_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'CreateDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'CreateDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='CreateDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.create_data_asset(
                create_data_asset_details=request.pop(util.camelize('CreateDataAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'CreateDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_create_detect_anomaly_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'CreateDetectAnomalyJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'CreateDetectAnomalyJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='CreateDetectAnomalyJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.create_detect_anomaly_job(
                create_detect_anomaly_job_details=request.pop(util.camelize('CreateDetectAnomalyJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'CreateDetectAnomalyJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectAnomalyJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_create_model(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'CreateModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'CreateModel')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='CreateModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.create_model(
                create_model_details=request.pop(util.camelize('CreateModelDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'CreateModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'model',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_create_project(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'CreateProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'CreateProject')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='CreateProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.create_project(
                create_project_details=request.pop(util.camelize('CreateProjectDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'CreateProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_delete_ai_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'DeleteAiPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'DeleteAiPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='DeleteAiPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.delete_ai_private_endpoint(
                ai_private_endpoint_id=request.pop(util.camelize('aiPrivateEndpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'DeleteAiPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_ai_private_endpoint',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_delete_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'DeleteDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'DeleteDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='DeleteDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.delete_data_asset(
                data_asset_id=request.pop(util.camelize('dataAssetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'DeleteDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_data_asset',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_delete_detect_anomaly_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'DeleteDetectAnomalyJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'DeleteDetectAnomalyJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='DeleteDetectAnomalyJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.delete_detect_anomaly_job(
                detect_anomaly_job_id=request.pop(util.camelize('detectAnomalyJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'DeleteDetectAnomalyJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_detect_anomaly_job',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_delete_model(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'DeleteModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'DeleteModel')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='DeleteModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.delete_model(
                model_id=request.pop(util.camelize('modelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'DeleteModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_model',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_delete_project(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'DeleteProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'DeleteProject')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='DeleteProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.delete_project(
                project_id=request.pop(util.camelize('projectId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'DeleteProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_project',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_detect_anomalies(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'DetectAnomalies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'DetectAnomalies')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='DetectAnomalies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.detect_anomalies(
                detect_anomalies_details=request.pop(util.camelize('DetectAnomaliesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'DetectAnomalies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'anomalyDetectResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_get_ai_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'GetAiPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'GetAiPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='GetAiPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.get_ai_private_endpoint(
                ai_private_endpoint_id=request.pop(util.camelize('aiPrivateEndpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'GetAiPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'aiPrivateEndpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_get_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'GetDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'GetDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='GetDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.get_data_asset(
                data_asset_id=request.pop(util.camelize('dataAssetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'GetDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_get_detect_anomaly_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'GetDetectAnomalyJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'GetDetectAnomalyJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='GetDetectAnomalyJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.get_detect_anomaly_job(
                detect_anomaly_job_id=request.pop(util.camelize('detectAnomalyJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'GetDetectAnomalyJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectAnomalyJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_get_model(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'GetModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'GetModel')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='GetModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.get_model(
                model_id=request.pop(util.camelize('modelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'GetModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'model',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_get_project(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'GetProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'GetProject')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='GetProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.get_project(
                project_id=request.pop(util.camelize('projectId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'GetProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_list_ai_private_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'ListAiPrivateEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'ListAiPrivateEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='ListAiPrivateEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.list_ai_private_endpoints(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_ai_private_endpoints(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_ai_private_endpoints(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'ListAiPrivateEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'aiPrivateEndpointCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_list_data_assets(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'ListDataAssets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'ListDataAssets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='ListDataAssets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.list_data_assets(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_data_assets(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_data_assets(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'ListDataAssets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAssetCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_list_detect_anomaly_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'ListDetectAnomalyJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'ListDetectAnomalyJobs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='ListDetectAnomalyJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.list_detect_anomaly_jobs(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_detect_anomaly_jobs(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_detect_anomaly_jobs(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'ListDetectAnomalyJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectAnomalyJobCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_list_models(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'ListModels'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'ListModels')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='ListModels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.list_models(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_models(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_models(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'ListModels',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'modelCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_list_projects(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'ListProjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'ListProjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='ListProjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.list_projects(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_projects(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_projects(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'ListProjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'projectCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
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
            'ai_anomaly_detection',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
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
            'ai_anomaly_detection',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
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
            'ai_anomaly_detection',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_update_ai_private_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'UpdateAiPrivateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'UpdateAiPrivateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='UpdateAiPrivateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.update_ai_private_endpoint(
                ai_private_endpoint_id=request.pop(util.camelize('aiPrivateEndpointId')),
                update_ai_private_endpoint_details=request.pop(util.camelize('UpdateAiPrivateEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'UpdateAiPrivateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_ai_private_endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_update_data_asset(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'UpdateDataAsset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'UpdateDataAsset')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='UpdateDataAsset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.update_data_asset(
                data_asset_id=request.pop(util.camelize('dataAssetId')),
                update_data_asset_details=request.pop(util.camelize('UpdateDataAssetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'UpdateDataAsset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataAsset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_update_detect_anomaly_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'UpdateDetectAnomalyJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'UpdateDetectAnomalyJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='UpdateDetectAnomalyJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
            response = client.update_detect_anomaly_job(
                detect_anomaly_job_id=request.pop(util.camelize('detectAnomalyJobId')),
                update_detect_anomaly_job_details=request.pop(util.camelize('UpdateDetectAnomalyJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_anomaly_detection',
            'UpdateDetectAnomalyJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectAnomalyJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_update_model(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'UpdateModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'UpdateModel')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='UpdateModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
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
            'ai_anomaly_detection',
            'UpdateModel',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_model',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_update_project(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_anomaly_detection', 'UpdateProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_anomaly_detection', util.camelize('anomaly_detection'), 'UpdateProject')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_anomaly_detection', api_name='UpdateProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_anomaly_detection.AnomalyDetectionClient(config, service_endpoint=service_endpoint)
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
            'ai_anomaly_detection',
            'UpdateProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'project',
            False,
            False
        )
