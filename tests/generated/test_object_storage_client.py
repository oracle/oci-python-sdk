# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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
    # use the default matching logic (link below) with the exception of 'session_agnostic_query_matcher'
    # instead of 'query' matcher (which ignores sessionId in the url)
    # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
    custom_vcr = test_config_container.create_vcr()
    custom_vcr.register_matcher('session_agnostic_query_matcher', session_agnostic_query_matcher)

    cassette_location = os.path.join('generated', 'object_storage_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_abort_multipart_upload(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'AbortMultipartUpload'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'AbortMultipartUpload')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='AbortMultipartUpload')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.abort_multipart_upload(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                object_name=request.pop(util.camelize('object_name')),
                upload_id=request.pop(util.camelize('upload_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'AbortMultipartUpload',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'abort_multipart_upload',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_cancel_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'CancelWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'CancelWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='CancelWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.cancel_work_request(
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'CancelWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'cancel_work_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_commit_multipart_upload(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'CommitMultipartUpload'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'CommitMultipartUpload')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='CommitMultipartUpload')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.commit_multipart_upload(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                object_name=request.pop(util.camelize('object_name')),
                upload_id=request.pop(util.camelize('upload_id')),
                commit_multipart_upload_details=request.pop(util.camelize('commit_multipart_upload_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'CommitMultipartUpload',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'commit_multipart_upload',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_copy_object(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'CopyObject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'CopyObject')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='CopyObject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.copy_object(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                copy_object_details=request.pop(util.camelize('copy_object_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'CopyObject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'copy_object',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_create_bucket(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'CreateBucket'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'CreateBucket')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='CreateBucket')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.create_bucket(
                namespace_name=request.pop(util.camelize('namespace_name')),
                create_bucket_details=request.pop(util.camelize('create_bucket_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'CreateBucket',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bucket',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_create_multipart_upload(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'CreateMultipartUpload'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'CreateMultipartUpload')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='CreateMultipartUpload')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.create_multipart_upload(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                create_multipart_upload_details=request.pop(util.camelize('create_multipart_upload_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'CreateMultipartUpload',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'multipartUpload',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_create_preauthenticated_request(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'CreatePreauthenticatedRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'CreatePreauthenticatedRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='CreatePreauthenticatedRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.create_preauthenticated_request(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                create_preauthenticated_request_details=request.pop(util.camelize('create_preauthenticated_request_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'CreatePreauthenticatedRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'preauthenticatedRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_delete_bucket(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'DeleteBucket'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'DeleteBucket')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='DeleteBucket')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.delete_bucket(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'DeleteBucket',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_bucket',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_delete_object(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'DeleteObject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'DeleteObject')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='DeleteObject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.delete_object(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                object_name=request.pop(util.camelize('object_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'DeleteObject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_object',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_delete_object_lifecycle_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'DeleteObjectLifecyclePolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'DeleteObjectLifecyclePolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='DeleteObjectLifecyclePolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.delete_object_lifecycle_policy(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'DeleteObjectLifecyclePolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_object_lifecycle_policy',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_delete_preauthenticated_request(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'DeletePreauthenticatedRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'DeletePreauthenticatedRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='DeletePreauthenticatedRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.delete_preauthenticated_request(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                par_id=request.pop(util.camelize('par_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'DeletePreauthenticatedRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_preauthenticated_request',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_get_bucket(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'GetBucket'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'GetBucket')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='GetBucket')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.get_bucket(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'GetBucket',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bucket',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_get_namespace(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'GetNamespace'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'GetNamespace')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='GetNamespace')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.get_namespace(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'GetNamespace',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'str',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_get_namespace_metadata(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'GetNamespaceMetadata'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'GetNamespaceMetadata')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='GetNamespaceMetadata')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.get_namespace_metadata(
                namespace_name=request.pop(util.camelize('namespace_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'GetNamespaceMetadata',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'namespaceMetadata',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_get_object(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'GetObject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'GetObject')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='GetObject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.get_object(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                object_name=request.pop(util.camelize('object_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'GetObject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'stream',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_get_object_lifecycle_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'GetObjectLifecyclePolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'GetObjectLifecyclePolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='GetObjectLifecyclePolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.get_object_lifecycle_policy(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'GetObjectLifecyclePolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'objectLifecyclePolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_get_preauthenticated_request(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'GetPreauthenticatedRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'GetPreauthenticatedRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='GetPreauthenticatedRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.get_preauthenticated_request(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                par_id=request.pop(util.camelize('par_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'GetPreauthenticatedRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'preauthenticatedRequestSummary',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_get_work_request(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'GetWorkRequest'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'GetWorkRequest')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='GetWorkRequest')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.get_work_request(
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'GetWorkRequest',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequest',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_head_bucket(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'HeadBucket'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'HeadBucket')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='HeadBucket')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.head_bucket(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'HeadBucket',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'head_bucket',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_head_object(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'HeadObject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'HeadObject')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='HeadObject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.head_object(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                object_name=request.pop(util.camelize('object_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'HeadObject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'head_object',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_list_buckets(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'ListBuckets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'ListBuckets')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='ListBuckets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.list_buckets(
                namespace_name=request.pop(util.camelize('namespace_name')),
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_buckets(
                    namespace_name=request.pop(util.camelize('namespace_name')),
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_buckets(
                        namespace_name=request.pop(util.camelize('namespace_name')),
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'ListBuckets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bucketSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_list_multipart_upload_parts(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'ListMultipartUploadParts'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'ListMultipartUploadParts')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='ListMultipartUploadParts')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.list_multipart_upload_parts(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                object_name=request.pop(util.camelize('object_name')),
                upload_id=request.pop(util.camelize('upload_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_multipart_upload_parts(
                    namespace_name=request.pop(util.camelize('namespace_name')),
                    bucket_name=request.pop(util.camelize('bucket_name')),
                    object_name=request.pop(util.camelize('object_name')),
                    upload_id=request.pop(util.camelize('upload_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_multipart_upload_parts(
                        namespace_name=request.pop(util.camelize('namespace_name')),
                        bucket_name=request.pop(util.camelize('bucket_name')),
                        object_name=request.pop(util.camelize('object_name')),
                        upload_id=request.pop(util.camelize('upload_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'ListMultipartUploadParts',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'multipartUploadPartSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_list_multipart_uploads(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'ListMultipartUploads'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'ListMultipartUploads')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='ListMultipartUploads')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.list_multipart_uploads(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_multipart_uploads(
                    namespace_name=request.pop(util.camelize('namespace_name')),
                    bucket_name=request.pop(util.camelize('bucket_name')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_multipart_uploads(
                        namespace_name=request.pop(util.camelize('namespace_name')),
                        bucket_name=request.pop(util.camelize('bucket_name')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'ListMultipartUploads',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'multipartUpload',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_list_objects(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'ListObjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'ListObjects')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='ListObjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.list_objects(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'ListObjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'listObjects',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_list_preauthenticated_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'ListPreauthenticatedRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'ListPreauthenticatedRequests')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='ListPreauthenticatedRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.list_preauthenticated_requests(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_preauthenticated_requests(
                    namespace_name=request.pop(util.camelize('namespace_name')),
                    bucket_name=request.pop(util.camelize('bucket_name')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_preauthenticated_requests(
                        namespace_name=request.pop(util.camelize('namespace_name')),
                        bucket_name=request.pop(util.camelize('bucket_name')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'ListPreauthenticatedRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'preauthenticatedRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_list_work_request_errors(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'ListWorkRequestErrors'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'ListWorkRequestErrors')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='ListWorkRequestErrors')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.list_work_request_errors(
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_errors(
                    work_request_id=request.pop(util.camelize('work_request_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_errors(
                        work_request_id=request.pop(util.camelize('work_request_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'ListWorkRequestErrors',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestError',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_list_work_request_logs(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'ListWorkRequestLogs'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'ListWorkRequestLogs')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='ListWorkRequestLogs')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.list_work_request_logs(
                work_request_id=request.pop(util.camelize('work_request_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_request_logs(
                    work_request_id=request.pop(util.camelize('work_request_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_request_logs(
                        work_request_id=request.pop(util.camelize('work_request_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'ListWorkRequestLogs',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestLogEntry',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_list_work_requests(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'ListWorkRequests'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'ListWorkRequests')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='ListWorkRequests')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.list_work_requests(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_work_requests(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_work_requests(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'ListWorkRequests',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'workRequestSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_put_object(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'PutObject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'PutObject')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='PutObject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.put_object(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                object_name=request.pop(util.camelize('object_name')),
                put_object_body=request.pop(util.camelize('put_object_body')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'PutObject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'put_object',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_put_object_lifecycle_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'PutObjectLifecyclePolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'PutObjectLifecyclePolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='PutObjectLifecyclePolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.put_object_lifecycle_policy(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                put_object_lifecycle_policy_details=request.pop(util.camelize('put_object_lifecycle_policy_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'PutObjectLifecyclePolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'objectLifecyclePolicy',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_rename_object(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'RenameObject'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'RenameObject')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='RenameObject')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.rename_object(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                rename_object_details=request.pop(util.camelize('rename_object_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'RenameObject',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'rename_object',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_restore_objects(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'RestoreObjects'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'RestoreObjects')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='RestoreObjects')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.restore_objects(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                restore_objects_details=request.pop(util.camelize('restore_objects_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'RestoreObjects',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'restore_objects',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_update_bucket(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'UpdateBucket'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'UpdateBucket')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='UpdateBucket')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.update_bucket(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                update_bucket_details=request.pop(util.camelize('update_bucket_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'UpdateBucket',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bucket',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_update_namespace_metadata(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'UpdateNamespaceMetadata'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'UpdateNamespaceMetadata')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='UpdateNamespaceMetadata')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.update_namespace_metadata(
                namespace_name=request.pop(util.camelize('namespace_name')),
                update_namespace_metadata_details=request.pop(util.camelize('update_namespace_metadata_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'UpdateNamespaceMetadata',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'namespaceMetadata',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="opc_casper_us_grp@oracle.com" jiraProject="CASPER" opsJiraProject="IOS"
def test_upload_part(testing_service_client):
    if not testing_service_client.is_api_enabled('object_storage', 'UploadPart'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('object_storage', util.camelize('object_storage'), 'UploadPart')
    )

    request_containers = testing_service_client.get_requests(service_name='object_storage', api_name='UploadPart')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            client = oci.object_storage.ObjectStorageClient(config)
            response = client.upload_part(
                namespace_name=request.pop(util.camelize('namespace_name')),
                bucket_name=request.pop(util.camelize('bucket_name')),
                object_name=request.pop(util.camelize('object_name')),
                upload_id=request.pop(util.camelize('upload_id')),
                upload_part_num=request.pop(util.camelize('upload_part_num')),
                upload_part_body=request.pop(util.camelize('upload_part_body')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'object_storage',
            'UploadPart',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'upload_part',
            False,
            False
        )
