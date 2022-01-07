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
