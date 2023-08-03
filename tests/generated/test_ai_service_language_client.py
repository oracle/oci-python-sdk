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

        cassette_location = os.path.join('generated', 'ai_language_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_batch_detect_dominant_language(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'BatchDetectDominantLanguage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'BatchDetectDominantLanguage')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='BatchDetectDominantLanguage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.batch_detect_dominant_language(
                batch_detect_dominant_language_details=request.pop(util.camelize('BatchDetectDominantLanguageDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'BatchDetectDominantLanguage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'batchDetectDominantLanguageResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_batch_detect_language_entities(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'BatchDetectLanguageEntities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'BatchDetectLanguageEntities')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='BatchDetectLanguageEntities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.batch_detect_language_entities(
                batch_detect_language_entities_details=request.pop(util.camelize('BatchDetectLanguageEntitiesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'BatchDetectLanguageEntities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'batchDetectLanguageEntitiesResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_batch_detect_language_key_phrases(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'BatchDetectLanguageKeyPhrases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'BatchDetectLanguageKeyPhrases')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='BatchDetectLanguageKeyPhrases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.batch_detect_language_key_phrases(
                batch_detect_language_key_phrases_details=request.pop(util.camelize('BatchDetectLanguageKeyPhrasesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'BatchDetectLanguageKeyPhrases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'batchDetectLanguageKeyPhrasesResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_batch_detect_language_pii_entities(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'BatchDetectLanguagePiiEntities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'BatchDetectLanguagePiiEntities')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='BatchDetectLanguagePiiEntities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.batch_detect_language_pii_entities(
                batch_detect_language_pii_entities_details=request.pop(util.camelize('BatchDetectLanguagePiiEntitiesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'BatchDetectLanguagePiiEntities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'batchDetectLanguagePiiEntitiesResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_batch_detect_language_sentiments(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'BatchDetectLanguageSentiments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'BatchDetectLanguageSentiments')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='BatchDetectLanguageSentiments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.batch_detect_language_sentiments(
                batch_detect_language_sentiments_details=request.pop(util.camelize('BatchDetectLanguageSentimentsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'BatchDetectLanguageSentiments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'batchDetectLanguageSentimentsResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_batch_detect_language_text_classification(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'BatchDetectLanguageTextClassification'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'BatchDetectLanguageTextClassification')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='BatchDetectLanguageTextClassification')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.batch_detect_language_text_classification(
                batch_detect_language_text_classification_details=request.pop(util.camelize('BatchDetectLanguageTextClassificationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'BatchDetectLanguageTextClassification',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'batchDetectLanguageTextClassificationResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_batch_language_translation(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'BatchLanguageTranslation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'BatchLanguageTranslation')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='BatchLanguageTranslation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.batch_language_translation(
                batch_language_translation_details=request.pop(util.camelize('BatchLanguageTranslationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'BatchLanguageTranslation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'batchLanguageTranslationResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_change_endpoint_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'ChangeEndpointCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'ChangeEndpointCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='ChangeEndpointCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
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
            'ai_language',
            'ChangeEndpointCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_endpoint_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_change_model_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'ChangeModelCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'ChangeModelCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='ChangeModelCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
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
            'ai_language',
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
    if not testing_service_client.is_api_enabled('ai_language', 'ChangeProjectCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'ChangeProjectCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='ChangeProjectCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
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
            'ai_language',
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
def test_create_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'CreateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'CreateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='CreateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.create_endpoint(
                create_endpoint_details=request.pop(util.camelize('CreateEndpointDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'CreateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_create_model(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'CreateModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'CreateModel')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='CreateModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.create_model(
                create_model_details=request.pop(util.camelize('CreateModelDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
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
    if not testing_service_client.is_api_enabled('ai_language', 'CreateProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'CreateProject')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='CreateProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.create_project(
                create_project_details=request.pop(util.camelize('CreateProjectDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
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
def test_delete_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'DeleteEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'DeleteEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='DeleteEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.delete_endpoint(
                endpoint_id=request.pop(util.camelize('endpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'DeleteEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_endpoint',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_delete_model(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'DeleteModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'DeleteModel')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='DeleteModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.delete_model(
                model_id=request.pop(util.camelize('modelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
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
    if not testing_service_client.is_api_enabled('ai_language', 'DeleteProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'DeleteProject')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='DeleteProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.delete_project(
                project_id=request.pop(util.camelize('projectId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
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
def test_detect_dominant_language(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'DetectDominantLanguage'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'DetectDominantLanguage')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='DetectDominantLanguage')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.detect_dominant_language(
                detect_dominant_language_details=request.pop(util.camelize('DetectDominantLanguageDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'DetectDominantLanguage',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectDominantLanguageResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_detect_language_entities(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'DetectLanguageEntities'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'DetectLanguageEntities')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='DetectLanguageEntities')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.detect_language_entities(
                detect_language_entities_details=request.pop(util.camelize('DetectLanguageEntitiesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'DetectLanguageEntities',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectLanguageEntitiesResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_detect_language_key_phrases(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'DetectLanguageKeyPhrases'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'DetectLanguageKeyPhrases')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='DetectLanguageKeyPhrases')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.detect_language_key_phrases(
                detect_language_key_phrases_details=request.pop(util.camelize('DetectLanguageKeyPhrasesDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'DetectLanguageKeyPhrases',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectLanguageKeyPhrasesResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_detect_language_sentiments(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'DetectLanguageSentiments'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'DetectLanguageSentiments')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='DetectLanguageSentiments')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.detect_language_sentiments(
                detect_language_sentiments_details=request.pop(util.camelize('DetectLanguageSentimentsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'DetectLanguageSentiments',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectLanguageSentimentsResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_detect_language_text_classification(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'DetectLanguageTextClassification'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'DetectLanguageTextClassification')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='DetectLanguageTextClassification')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.detect_language_text_classification(
                detect_language_text_classification_details=request.pop(util.camelize('DetectLanguageTextClassificationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'DetectLanguageTextClassification',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'detectLanguageTextClassificationResult',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_get_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'GetEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'GetEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='GetEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.get_endpoint(
                endpoint_id=request.pop(util.camelize('endpointId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'GetEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_get_model(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'GetModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'GetModel')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='GetModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.get_model(
                model_id=request.pop(util.camelize('modelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
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
def test_get_model_type(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'GetModelType'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'GetModelType')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='GetModelType')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.get_model_type(
                model_type=request.pop(util.camelize('modelType')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'GetModelType',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'modelTypeInfo',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_get_project(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'GetProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'GetProject')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='GetProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.get_project(
                project_id=request.pop(util.camelize('projectId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
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
    if not testing_service_client.is_api_enabled('ai_language', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
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
def test_list_endpoints(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'ListEndpoints'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'ListEndpoints')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='ListEndpoints')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
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
            'ai_language',
            'ListEndpoints',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'endpointCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_list_evaluation_results(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'ListEvaluationResults'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'ListEvaluationResults')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='ListEvaluationResults')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
            response = client.list_evaluation_results(
                model_id=request.pop(util.camelize('modelId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_evaluation_results(
                    model_id=request.pop(util.camelize('modelId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_evaluation_results(
                        model_id=request.pop(util.camelize('modelId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'ai_language',
            'ListEvaluationResults',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'evaluationResultCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_list_models(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'ListModels'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'ListModels')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='ListModels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
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
            'ai_language',
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
    if not testing_service_client.is_api_enabled('ai_language', 'ListProjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'ListProjects')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='ListProjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
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
            'ai_language',
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
    if not testing_service_client.is_api_enabled('ai_language', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
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
            'ai_language',
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
    if not testing_service_client.is_api_enabled('ai_language', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
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
            'ai_language',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
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
            'ai_language',
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
def test_update_endpoint(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'UpdateEndpoint'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'UpdateEndpoint')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='UpdateEndpoint')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
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
            'ai_language',
            'UpdateEndpoint',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_endpoint',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci_ocas_ops_ww_grp@oracle.com" jiraProject="OCAS" opsJiraProject="OCAS"
def test_update_model(testing_service_client):
    if not testing_service_client.is_api_enabled('ai_language', 'UpdateModel'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'UpdateModel')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='UpdateModel')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
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
            'ai_language',
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
    if not testing_service_client.is_api_enabled('ai_language', 'UpdateProject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('ai_language', util.camelize('ai_service_language'), 'UpdateProject')
    )

    request_containers = testing_service_client.get_requests(service_name='ai_language', api_name='UpdateProject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.ai_language.AIServiceLanguageClient(config, service_endpoint=service_endpoint)
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
            'ai_language',
            'UpdateProject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_project',
            False,
            False
        )
