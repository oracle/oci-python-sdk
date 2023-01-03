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

        cassette_location = os.path.join('generated', 'opensearch_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_backup_opensearch_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'BackupOpensearchCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'BackupOpensearchCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='BackupOpensearchCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
            response = client.backup_opensearch_cluster(
                opensearch_cluster_id=request.pop(util.camelize('opensearchClusterId')),
                backup_opensearch_cluster_details=request.pop(util.camelize('BackupOpensearchClusterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opensearch',
            'BackupOpensearchCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'backup_opensearch_cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_create_opensearch_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'CreateOpensearchCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'CreateOpensearchCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='CreateOpensearchCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
            response = client.create_opensearch_cluster(
                create_opensearch_cluster_details=request.pop(util.camelize('CreateOpensearchClusterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opensearch',
            'CreateOpensearchCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'create_opensearch_cluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_delete_opensearch_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'DeleteOpensearchCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'DeleteOpensearchCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='DeleteOpensearchCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
            response = client.delete_opensearch_cluster(
                opensearch_cluster_id=request.pop(util.camelize('opensearchClusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opensearch',
            'DeleteOpensearchCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_opensearch_cluster',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_opensearch_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'GetOpensearchCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'GetOpensearchCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='GetOpensearchCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
            response = client.get_opensearch_cluster(
                opensearch_cluster_id=request.pop(util.camelize('opensearchClusterId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opensearch',
            'GetOpensearchCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'opensearchCluster',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('workRequestId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opensearch',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_opensearch_clusters(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'ListOpensearchClusters'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'ListOpensearchClusters')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='ListOpensearchClusters')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
            response = client.list_opensearch_clusters(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_opensearch_clusters(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_opensearch_clusters(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opensearch',
            'ListOpensearchClusters',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'opensearchClusterCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_opensearch_versions(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'ListOpensearchVersions'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'ListOpensearchVersions')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='ListOpensearchVersions')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
            response = client.list_opensearch_versions(
                compartment_id=request.pop(util.camelize('compartmentId')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_opensearch_versions(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    retry_strategy=oci.retry.NoneRetryStrategy(),
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_opensearch_versions(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        page=next_response.headers[prev_page],
                        retry_strategy=oci.retry.NoneRetryStrategy(),
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opensearch',
            'ListOpensearchVersions',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'opensearchVersionsCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'ListWorkRequestErrors')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
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
            'opensearch',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestErrorCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'ListWorkRequestLogs')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
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
            'opensearch',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntryCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'ListWorkRequests')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
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
            'opensearch',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestCollection',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_opensearch_cluster_restore(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'OpensearchClusterRestore'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'OpensearchClusterRestore')
    )

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='OpensearchClusterRestore')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
            response = client.opensearch_cluster_restore(
                opensearch_cluster_id=request.pop(util.camelize('opensearchClusterId')),
                restore_opensearch_cluster_details=request.pop(util.camelize('RestoreOpensearchClusterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opensearch',
            'OpensearchClusterRestore',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'opensearch_cluster_restore',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_resize_opensearch_cluster_horizontal(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'ResizeOpensearchClusterHorizontal'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'ResizeOpensearchClusterHorizontal')
    )

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='ResizeOpensearchClusterHorizontal')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
            response = client.resize_opensearch_cluster_horizontal(
                opensearch_cluster_id=request.pop(util.camelize('opensearchClusterId')),
                resize_opensearch_cluster_horizontal_details=request.pop(util.camelize('ResizeOpensearchClusterHorizontalDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opensearch',
            'ResizeOpensearchClusterHorizontal',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resize_opensearch_cluster_horizontal',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_resize_opensearch_cluster_vertical(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'ResizeOpensearchClusterVertical'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'ResizeOpensearchClusterVertical')
    )

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='ResizeOpensearchClusterVertical')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
            response = client.resize_opensearch_cluster_vertical(
                opensearch_cluster_id=request.pop(util.camelize('opensearchClusterId')),
                resize_opensearch_cluster_vertical_details=request.pop(util.camelize('ResizeOpensearchClusterVerticalDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opensearch',
            'ResizeOpensearchClusterVertical',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'resize_opensearch_cluster_vertical',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="lesrober_org_ww@oracle.com" jiraProject="JIRA" opsJiraProject="JIRA-OPS"
def test_update_opensearch_cluster(testing_service_client):
    if not testing_service_client.is_api_enabled('opensearch', 'UpdateOpensearchCluster'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('opensearch', util.camelize('opensearch_cluster'), 'UpdateOpensearchCluster')
    )

    request_containers = testing_service_client.get_requests(service_name='opensearch', api_name='UpdateOpensearchCluster')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.opensearch.OpensearchClusterClient(config, service_endpoint=service_endpoint)
            response = client.update_opensearch_cluster(
                opensearch_cluster_id=request.pop(util.camelize('opensearchClusterId')),
                update_opensearch_cluster_details=request.pop(util.camelize('UpdateOpensearchClusterDetails')),
                retry_strategy=oci.retry.NoneRetryStrategy(),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'opensearch',
            'UpdateOpensearchCluster',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'update_opensearch_cluster',
            False,
            False
        )
