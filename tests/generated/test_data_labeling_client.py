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

        cassette_location = os.path.join('generated', 'data_labeling_service_dataplane_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_annotation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'CreateAnnotation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'CreateAnnotation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='CreateAnnotation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.create_annotation(
                create_annotation_details=request.pop(util.camelize('CreateAnnotationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'CreateAnnotation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'annotation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_record(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'CreateRecord'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'CreateRecord')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='CreateRecord')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.create_record(
                create_record_details=request.pop(util.camelize('CreateRecordDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'CreateRecord',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'record',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_annotation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'DeleteAnnotation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'DeleteAnnotation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='DeleteAnnotation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.delete_annotation(
                annotation_id=request.pop(util.camelize('annotationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'DeleteAnnotation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_annotation',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_record(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'DeleteRecord'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'DeleteRecord')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='DeleteRecord')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.delete_record(
                record_id=request.pop(util.camelize('recordId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'DeleteRecord',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_record',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_annotation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'GetAnnotation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'GetAnnotation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='GetAnnotation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.get_annotation(
                annotation_id=request.pop(util.camelize('annotationId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'GetAnnotation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'annotation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_dataset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'GetDataset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'GetDataset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='GetDataset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.get_dataset(
                dataset_id=request.pop(util.camelize('datasetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'GetDataset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_record(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'GetRecord'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'GetRecord')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='GetRecord')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.get_record(
                record_id=request.pop(util.camelize('recordId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'GetRecord',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'record',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_record_content(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'GetRecordContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'GetRecordContent')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='GetRecordContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.get_record_content(
                record_id=request.pop(util.camelize('recordId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'GetRecordContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_record_preview_content(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'GetRecordPreviewContent'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'GetRecordPreviewContent')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='GetRecordPreviewContent')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.get_record_preview_content(
                record_id=request.pop(util.camelize('recordId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'GetRecordPreviewContent',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_annotations(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'ListAnnotations'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'ListAnnotations')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='ListAnnotations')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.list_annotations(
                compartment_id=request.pop(util.camelize('compartmentId')),
                dataset_id=request.pop(util.camelize('datasetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_annotations(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    dataset_id=request.pop(util.camelize('datasetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_annotations(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        dataset_id=request.pop(util.camelize('datasetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'ListAnnotations',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'annotationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_records(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'ListRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'ListRecords')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='ListRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.list_records(
                compartment_id=request.pop(util.camelize('compartmentId')),
                dataset_id=request.pop(util.camelize('datasetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_records(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    dataset_id=request.pop(util.camelize('datasetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_records(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        dataset_id=request.pop(util.camelize('datasetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'ListRecords',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recordCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_summarize_annotation_analytics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'SummarizeAnnotationAnalytics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'SummarizeAnnotationAnalytics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='SummarizeAnnotationAnalytics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.summarize_annotation_analytics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                dataset_id=request.pop(util.camelize('datasetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_annotation_analytics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    dataset_id=request.pop(util.camelize('datasetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_annotation_analytics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        dataset_id=request.pop(util.camelize('datasetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'SummarizeAnnotationAnalytics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'annotationAnalyticsAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_summarize_record_analytics(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'SummarizeRecordAnalytics'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'SummarizeRecordAnalytics')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='SummarizeRecordAnalytics')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.summarize_record_analytics(
                compartment_id=request.pop(util.camelize('compartmentId')),
                dataset_id=request.pop(util.camelize('datasetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.summarize_record_analytics(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    dataset_id=request.pop(util.camelize('datasetId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.summarize_record_analytics(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        dataset_id=request.pop(util.camelize('datasetId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'SummarizeRecordAnalytics',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'recordAnalyticsAggregationCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_annotation(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'UpdateAnnotation'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'UpdateAnnotation')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='UpdateAnnotation')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.update_annotation(
                annotation_id=request.pop(util.camelize('annotationId')),
                update_annotation_details=request.pop(util.camelize('UpdateAnnotationDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'UpdateAnnotation',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'annotation',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="data_labeling_ww_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_record(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service_dataplane', 'UpdateRecord'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service_dataplane', util.camelize('data_labeling'), 'UpdateRecord')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service_dataplane', api_name='UpdateRecord')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service_dataplane.DataLabelingClient(config, service_endpoint=service_endpoint)
            response = client.update_record(
                record_id=request.pop(util.camelize('recordId')),
                update_record_details=request.pop(util.camelize('UpdateRecordDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service_dataplane',
            'UpdateRecord',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'record',
            False,
            False
        )
