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

        cassette_location = os.path.join('generated', 'data_labeling_service_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_add_dataset_labels(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'AddDatasetLabels'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'AddDatasetLabels')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='AddDatasetLabels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.add_dataset_labels(
                dataset_id=request.pop(util.camelize('datasetId')),
                add_dataset_labels_details=request.pop(util.camelize('AddDatasetLabelsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'AddDatasetLabels',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'add_dataset_labels',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_change_dataset_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'ChangeDatasetCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'ChangeDatasetCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='ChangeDatasetCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.change_dataset_compartment(
                dataset_id=request.pop(util.camelize('datasetId')),
                change_dataset_compartment_details=request.pop(util.camelize('ChangeDatasetCompartmentDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'ChangeDatasetCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_dataset_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_dataset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'CreateDataset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'CreateDataset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='CreateDataset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.create_dataset(
                create_dataset_details=request.pop(util.camelize('CreateDatasetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'CreateDataset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_dataset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'DeleteDataset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'DeleteDataset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='DeleteDataset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.delete_dataset(
                dataset_id=request.pop(util.camelize('datasetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'DeleteDataset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_dataset',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_generate_dataset_records(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'GenerateDatasetRecords'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'GenerateDatasetRecords')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='GenerateDatasetRecords')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.generate_dataset_records(
                dataset_id=request.pop(util.camelize('datasetId')),
                generate_dataset_records_details=request.pop(util.camelize('GenerateDatasetRecordsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'GenerateDatasetRecords',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'generate_dataset_records',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_dataset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'GetDataset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'GetDataset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='GetDataset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_dataset(
                dataset_id=request.pop(util.camelize('datasetId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'GetDataset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_import_pre_annotated_data(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'ImportPreAnnotatedData'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'ImportPreAnnotatedData')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='ImportPreAnnotatedData')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.import_pre_annotated_data(
                dataset_id=request.pop(util.camelize('datasetId')),
                import_pre_annotated_data_details=request.pop(util.camelize('ImportPreAnnotatedDataDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'ImportPreAnnotatedData',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'import_pre_annotated_data',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_annotation_formats(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'ListAnnotationFormats'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'ListAnnotationFormats')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='ListAnnotationFormats')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_annotation_formats(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_annotation_formats(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_annotation_formats(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'ListAnnotationFormats',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'annotationFormatCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_datasets(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'ListDatasets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'ListDatasets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='ListDatasets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.list_datasets(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_datasets(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_datasets(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'ListDatasets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'datasetCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
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
            'data_labeling_service',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
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
            'data_labeling_service',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
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
            'data_labeling_service',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummaryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_remove_dataset_labels(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'RemoveDatasetLabels'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'RemoveDatasetLabels')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='RemoveDatasetLabels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.remove_dataset_labels(
                dataset_id=request.pop(util.camelize('datasetId')),
                remove_dataset_labels_details=request.pop(util.camelize('RemoveDatasetLabelsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'RemoveDatasetLabels',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'remove_dataset_labels',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_rename_dataset_labels(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'RenameDatasetLabels'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'RenameDatasetLabels')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='RenameDatasetLabels')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.rename_dataset_labels(
                dataset_id=request.pop(util.camelize('datasetId')),
                rename_dataset_labels_details=request.pop(util.camelize('RenameDatasetLabelsDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'RenameDatasetLabels',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'rename_dataset_labels',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_snapshot_dataset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'SnapshotDataset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'SnapshotDataset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='SnapshotDataset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.snapshot_dataset(
                dataset_id=request.pop(util.camelize('datasetId')),
                snapshot_dataset_details=request.pop(util.camelize('SnapshotDatasetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'SnapshotDataset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'snapshot_dataset',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="oci-dls_us_grp@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_dataset(testing_service_client):
    if not testing_service_client.is_api_enabled('data_labeling_service', 'UpdateDataset'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('data_labeling_service', util.camelize('data_labeling_management'), 'UpdateDataset')
    )

    request_containers = testing_service_client.get_requests(service_name='data_labeling_service', api_name='UpdateDataset')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.data_labeling_service.DataLabelingManagementClient(config, service_endpoint=service_endpoint)
            response = client.update_dataset(
                dataset_id=request.pop(util.camelize('datasetId')),
                update_dataset_details=request.pop(util.camelize('UpdateDatasetDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'data_labeling_service',
            'UpdateDataset',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'dataset',
            False,
            False
        )
