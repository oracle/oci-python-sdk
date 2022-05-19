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

        cassette_location = os.path.join('generated', 'ai_speech_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="mkennewi_org_ww@oracle.com" jiraProject="SPEECHAI" opsJiraProject="SPEECHAIOP"
def test_cancel_transcription_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_speech', 'CancelTranscriptionJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_speech', util.camelize('ai_service_speech'), 'CancelTranscriptionJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_speech', api_name='CancelTranscriptionJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_speech.AIServiceSpeechClient(config, service_endpoint=service_endpoint)
            response = client.cancel_transcription_job(
                transcription_job_id=request.pop(util.camelize('transcriptionJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_speech',
            'CancelTranscriptionJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_transcription_job',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mkennewi_org_ww@oracle.com" jiraProject="SPEECHAI" opsJiraProject="SPEECHAIOP"
def test_cancel_transcription_task(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_speech', 'CancelTranscriptionTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_speech', util.camelize('ai_service_speech'), 'CancelTranscriptionTask')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_speech', api_name='CancelTranscriptionTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_speech.AIServiceSpeechClient(config, service_endpoint=service_endpoint)
            response = client.cancel_transcription_task(
                transcription_job_id=request.pop(util.camelize('transcriptionJobId')),
                transcription_task_id=request.pop(util.camelize('transcriptionTaskId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_speech',
            'CancelTranscriptionTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_transcription_task',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mkennewi_org_ww@oracle.com" jiraProject="SPEECHAI" opsJiraProject="SPEECHAIOP"
def test_change_transcription_job_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_speech', 'ChangeTranscriptionJobCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_speech', util.camelize('ai_service_speech'), 'ChangeTranscriptionJobCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_speech', api_name='ChangeTranscriptionJobCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_speech.AIServiceSpeechClient(config, service_endpoint=service_endpoint)
            response = client.change_transcription_job_compartment(
                transcription_job_id=request.pop(util.camelize('transcriptionJobId')),
                change_transcription_job_compartment_details=request.pop(util.camelize('ChangeTranscriptionJobCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_speech',
            'ChangeTranscriptionJobCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_transcription_job_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mkennewi_org_ww@oracle.com" jiraProject="SPEECHAI" opsJiraProject="SPEECHAIOP"
def test_create_transcription_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_speech', 'CreateTranscriptionJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_speech', util.camelize('ai_service_speech'), 'CreateTranscriptionJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_speech', api_name='CreateTranscriptionJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_speech.AIServiceSpeechClient(config, service_endpoint=service_endpoint)
            response = client.create_transcription_job(
                create_transcription_job_details=request.pop(util.camelize('CreateTranscriptionJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_speech',
            'CreateTranscriptionJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transcriptionJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mkennewi_org_ww@oracle.com" jiraProject="SPEECHAI" opsJiraProject="SPEECHAIOP"
def test_get_transcription_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_speech', 'GetTranscriptionJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_speech', util.camelize('ai_service_speech'), 'GetTranscriptionJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_speech', api_name='GetTranscriptionJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_speech.AIServiceSpeechClient(config, service_endpoint=service_endpoint)
            response = client.get_transcription_job(
                transcription_job_id=request.pop(util.camelize('transcriptionJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_speech',
            'GetTranscriptionJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transcriptionJob',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mkennewi_org_ww@oracle.com" jiraProject="SPEECHAI" opsJiraProject="SPEECHAIOP"
def test_get_transcription_task(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_speech', 'GetTranscriptionTask'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_speech', util.camelize('ai_service_speech'), 'GetTranscriptionTask')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_speech', api_name='GetTranscriptionTask')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_speech.AIServiceSpeechClient(config, service_endpoint=service_endpoint)
            response = client.get_transcription_task(
                transcription_job_id=request.pop(util.camelize('transcriptionJobId')),
                transcription_task_id=request.pop(util.camelize('transcriptionTaskId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_speech',
            'GetTranscriptionTask',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transcriptionTask',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="mkennewi_org_ww@oracle.com" jiraProject="SPEECHAI" opsJiraProject="SPEECHAIOP"
def test_list_transcription_jobs(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_speech', 'ListTranscriptionJobs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_speech', util.camelize('ai_service_speech'), 'ListTranscriptionJobs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_speech', api_name='ListTranscriptionJobs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_speech.AIServiceSpeechClient(config, service_endpoint=service_endpoint)
            response = client.list_transcription_jobs(
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_transcription_jobs(
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_transcription_jobs(
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_speech',
            'ListTranscriptionJobs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transcriptionJobCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="mkennewi_org_ww@oracle.com" jiraProject="SPEECHAI" opsJiraProject="SPEECHAIOP"
def test_list_transcription_tasks(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_speech', 'ListTranscriptionTasks'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_speech', util.camelize('ai_service_speech'), 'ListTranscriptionTasks')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_speech', api_name='ListTranscriptionTasks')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_speech.AIServiceSpeechClient(config, service_endpoint=service_endpoint)
            response = client.list_transcription_tasks(
                transcription_job_id=request.pop(util.camelize('transcriptionJobId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_transcription_tasks(
                    transcription_job_id=request.pop(util.camelize('transcriptionJobId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_transcription_tasks(
                        transcription_job_id=request.pop(util.camelize('transcriptionJobId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_speech',
            'ListTranscriptionTasks',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transcriptionTaskCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="mkennewi_org_ww@oracle.com" jiraProject="SPEECHAI" opsJiraProject="SPEECHAIOP"
def test_update_transcription_job(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_speech', 'UpdateTranscriptionJob'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_speech', util.camelize('ai_service_speech'), 'UpdateTranscriptionJob')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_speech', api_name='UpdateTranscriptionJob')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_speech.AIServiceSpeechClient(config, service_endpoint=service_endpoint)
            response = client.update_transcription_job(
                transcription_job_id=request.pop(util.camelize('transcriptionJobId')),
                update_transcription_job_details=request.pop(util.camelize('UpdateTranscriptionJobDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_speech',
            'UpdateTranscriptionJob',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'transcriptionJob',
            False,
            False
        )
