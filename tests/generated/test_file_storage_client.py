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

        cassette_location = os.path.join('generated', 'file_storage_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_change_file_system_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'ChangeFileSystemCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'ChangeFileSystemCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='ChangeFileSystemCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.change_file_system_compartment(
                file_system_id=request.pop(util.camelize('fileSystemId')),
                change_file_system_compartment_details=request.pop(util.camelize('ChangeFileSystemCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'ChangeFileSystemCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_file_system_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_change_mount_target_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'ChangeMountTargetCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'ChangeMountTargetCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='ChangeMountTargetCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.change_mount_target_compartment(
                mount_target_id=request.pop(util.camelize('mountTargetId')),
                change_mount_target_compartment_details=request.pop(util.camelize('ChangeMountTargetCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'ChangeMountTargetCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_mount_target_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_create_export(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'CreateExport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'CreateExport')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='CreateExport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.create_export(
                create_export_details=request.pop(util.camelize('CreateExportDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'CreateExport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'export',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_create_file_system(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'CreateFileSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'CreateFileSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='CreateFileSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.create_file_system(
                create_file_system_details=request.pop(util.camelize('CreateFileSystemDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'CreateFileSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fileSystem',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_create_mount_target(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'CreateMountTarget'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'CreateMountTarget')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='CreateMountTarget')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.create_mount_target(
                create_mount_target_details=request.pop(util.camelize('CreateMountTargetDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'CreateMountTarget',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mountTarget',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_create_snapshot(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'CreateSnapshot'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'CreateSnapshot')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='CreateSnapshot')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.create_snapshot(
                create_snapshot_details=request.pop(util.camelize('CreateSnapshotDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'CreateSnapshot',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'snapshot',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_delete_export(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'DeleteExport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'DeleteExport')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='DeleteExport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_export(
                export_id=request.pop(util.camelize('exportId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'DeleteExport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_export',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_delete_file_system(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'DeleteFileSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'DeleteFileSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='DeleteFileSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_file_system(
                file_system_id=request.pop(util.camelize('fileSystemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'DeleteFileSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_file_system',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_delete_mount_target(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'DeleteMountTarget'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'DeleteMountTarget')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='DeleteMountTarget')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_mount_target(
                mount_target_id=request.pop(util.camelize('mountTargetId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'DeleteMountTarget',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_mount_target',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_delete_snapshot(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'DeleteSnapshot'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'DeleteSnapshot')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='DeleteSnapshot')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_snapshot(
                snapshot_id=request.pop(util.camelize('snapshotId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'DeleteSnapshot',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_snapshot',
            True,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_get_export(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'GetExport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'GetExport')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='GetExport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.get_export(
                export_id=request.pop(util.camelize('exportId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'GetExport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'export',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_get_export_set(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'GetExportSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'GetExportSet')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='GetExportSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.get_export_set(
                export_set_id=request.pop(util.camelize('exportSetId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'GetExportSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exportSet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_get_file_system(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'GetFileSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'GetFileSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='GetFileSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.get_file_system(
                file_system_id=request.pop(util.camelize('fileSystemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'GetFileSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fileSystem',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_get_mount_target(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'GetMountTarget'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'GetMountTarget')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='GetMountTarget')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.get_mount_target(
                mount_target_id=request.pop(util.camelize('mountTargetId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'GetMountTarget',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mountTarget',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_get_snapshot(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'GetSnapshot'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'GetSnapshot')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='GetSnapshot')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.get_snapshot(
                snapshot_id=request.pop(util.camelize('snapshotId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'GetSnapshot',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'snapshot',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_list_export_sets(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'ListExportSets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'ListExportSets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='ListExportSets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.list_export_sets(
                compartment_id=request.pop(util.camelize('compartmentId')),
                availability_domain=request.pop(util.camelize('availabilityDomain')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_export_sets(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    availability_domain=request.pop(util.camelize('availabilityDomain')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_export_sets(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        availability_domain=request.pop(util.camelize('availabilityDomain')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'ListExportSets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exportSetSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_list_exports(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'ListExports'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'ListExports')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='ListExports')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.list_exports(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_exports(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_exports(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'ListExports',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exportSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_list_file_systems(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'ListFileSystems'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'ListFileSystems')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='ListFileSystems')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.list_file_systems(
                compartment_id=request.pop(util.camelize('compartmentId')),
                availability_domain=request.pop(util.camelize('availabilityDomain')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_file_systems(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    availability_domain=request.pop(util.camelize('availabilityDomain')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_file_systems(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        availability_domain=request.pop(util.camelize('availabilityDomain')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'ListFileSystems',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fileSystemSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_list_mount_targets(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'ListMountTargets'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'ListMountTargets')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='ListMountTargets')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.list_mount_targets(
                compartment_id=request.pop(util.camelize('compartmentId')),
                availability_domain=request.pop(util.camelize('availabilityDomain')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_mount_targets(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    availability_domain=request.pop(util.camelize('availabilityDomain')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_mount_targets(
                        compartment_id=request.pop(util.camelize('compartmentId')),
                        availability_domain=request.pop(util.camelize('availabilityDomain')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'ListMountTargets',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mountTargetSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_list_snapshots(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'ListSnapshots'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'ListSnapshots')
    )
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='ListSnapshots')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.list_snapshots(
                file_system_id=request.pop(util.camelize('fileSystemId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_snapshots(
                    file_system_id=request.pop(util.camelize('fileSystemId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_snapshots(
                        file_system_id=request.pop(util.camelize('fileSystemId')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'ListSnapshots',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'snapshotSummary',
            False,
            True
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_update_export(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'UpdateExport'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'UpdateExport')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='UpdateExport')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.update_export(
                export_id=request.pop(util.camelize('exportId')),
                update_export_details=request.pop(util.camelize('UpdateExportDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'UpdateExport',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'export',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_update_export_set(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'UpdateExportSet'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'UpdateExportSet')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='UpdateExportSet')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.update_export_set(
                export_set_id=request.pop(util.camelize('exportSetId')),
                update_export_set_details=request.pop(util.camelize('UpdateExportSetDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'UpdateExportSet',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'exportSet',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_update_file_system(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'UpdateFileSystem'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'UpdateFileSystem')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='UpdateFileSystem')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.update_file_system(
                file_system_id=request.pop(util.camelize('fileSystemId')),
                update_file_system_details=request.pop(util.camelize('UpdateFileSystemDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'UpdateFileSystem',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'fileSystem',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_update_mount_target(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'UpdateMountTarget'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'UpdateMountTarget')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='UpdateMountTarget')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.update_mount_target(
                mount_target_id=request.pop(util.camelize('mountTargetId')),
                update_mount_target_details=request.pop(util.camelize('UpdateMountTargetDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'UpdateMountTarget',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'mountTarget',
            False,
            False
        )


# IssueRoutingInfo tag="default" email="sic_ffsw_us_grp@oracle.com" jiraProject="FFSW" opsJiraProject="FSS"
def test_update_snapshot(testing_service_client):
    if not testing_service_client.is_api_enabled('file_storage', 'UpdateSnapshot'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('file_storage', util.camelize('file_storage'), 'UpdateSnapshot')
    )

    request_containers = testing_service_client.get_requests(service_name='file_storage', api_name='UpdateSnapshot')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.file_storage.FileStorageClient(config, service_endpoint=service_endpoint)
            response = client.update_snapshot(
                snapshot_id=request.pop(util.camelize('snapshotId')),
                update_snapshot_details=request.pop(util.camelize('UpdateSnapshotDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'file_storage',
            'UpdateSnapshot',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'snapshot',
            False,
            False
        )
