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

    cassette_location = os.path.join('generated', 'core_{name}.yml'.format(name=request.function.__name__))
    with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
        yield


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_copy_volume_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CopyVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'CopyVolumeBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CopyVolumeBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.copy_volume_backup(
                volume_backup_id=request.pop(util.camelize('volume_backup_id')),
                copy_volume_backup_details=request.pop(util.camelize('copy_volume_backup_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CopyVolumeBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeBackup',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_create_boot_volume(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateBootVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'CreateBootVolume')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateBootVolume')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_boot_volume(
                create_boot_volume_details=request.pop(util.camelize('create_boot_volume_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateBootVolume',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolume',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_create_boot_volume_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateBootVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'CreateBootVolumeBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateBootVolumeBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_boot_volume_backup(
                create_boot_volume_backup_details=request.pop(util.camelize('create_boot_volume_backup_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateBootVolumeBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolumeBackup',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_create_volume(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'CreateVolume')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateVolume')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_volume(
                create_volume_details=request.pop(util.camelize('create_volume_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateVolume',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volume',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_create_volume_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'CreateVolumeBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateVolumeBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_volume_backup(
                create_volume_backup_details=request.pop(util.camelize('create_volume_backup_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateVolumeBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeBackup',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_create_volume_backup_policy_assignment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateVolumeBackupPolicyAssignment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'CreateVolumeBackupPolicyAssignment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateVolumeBackupPolicyAssignment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_volume_backup_policy_assignment(
                create_volume_backup_policy_assignment_details=request.pop(util.camelize('create_volume_backup_policy_assignment_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateVolumeBackupPolicyAssignment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeBackupPolicyAssignment',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_create_volume_group(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateVolumeGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'CreateVolumeGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateVolumeGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_volume_group(
                create_volume_group_details=request.pop(util.camelize('create_volume_group_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateVolumeGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeGroup',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_create_volume_group_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateVolumeGroupBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'CreateVolumeGroupBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateVolumeGroupBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_volume_group_backup(
                create_volume_group_backup_details=request.pop(util.camelize('create_volume_group_backup_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateVolumeGroupBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeGroupBackup',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_delete_boot_volume(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteBootVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'DeleteBootVolume')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteBootVolume')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_boot_volume(
                boot_volume_id=request.pop(util.camelize('boot_volume_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteBootVolume',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_boot_volume',
            True,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_delete_boot_volume_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteBootVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'DeleteBootVolumeBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteBootVolumeBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_boot_volume_backup(
                boot_volume_backup_id=request.pop(util.camelize('boot_volume_backup_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteBootVolumeBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_boot_volume_backup',
            True,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_delete_boot_volume_kms_key(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteBootVolumeKmsKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'DeleteBootVolumeKmsKey')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteBootVolumeKmsKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_boot_volume_kms_key(
                boot_volume_id=request.pop(util.camelize('boot_volume_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteBootVolumeKmsKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_boot_volume_kms_key',
            True,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_delete_volume(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'DeleteVolume')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteVolume')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_volume(
                volume_id=request.pop(util.camelize('volume_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteVolume',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_volume',
            True,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_delete_volume_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'DeleteVolumeBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_volume_backup(
                volume_backup_id=request.pop(util.camelize('volume_backup_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteVolumeBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_volume_backup',
            True,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_delete_volume_backup_policy_assignment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteVolumeBackupPolicyAssignment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'DeleteVolumeBackupPolicyAssignment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeBackupPolicyAssignment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_volume_backup_policy_assignment(
                policy_assignment_id=request.pop(util.camelize('policy_assignment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteVolumeBackupPolicyAssignment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_volume_backup_policy_assignment',
            True,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_delete_volume_group(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteVolumeGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'DeleteVolumeGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_volume_group(
                volume_group_id=request.pop(util.camelize('volume_group_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteVolumeGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_volume_group',
            True,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_delete_volume_group_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteVolumeGroupBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'DeleteVolumeGroupBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeGroupBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_volume_group_backup(
                volume_group_backup_id=request.pop(util.camelize('volume_group_backup_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteVolumeGroupBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_volume_group_backup',
            True,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_delete_volume_kms_key(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteVolumeKmsKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'DeleteVolumeKmsKey')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeKmsKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_volume_kms_key(
                volume_id=request.pop(util.camelize('volume_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteVolumeKmsKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_volume_kms_key',
            True,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_get_boot_volume(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetBootVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'GetBootVolume')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetBootVolume')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_boot_volume(
                boot_volume_id=request.pop(util.camelize('boot_volume_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetBootVolume',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolume',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_get_boot_volume_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetBootVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'GetBootVolumeBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetBootVolumeBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_boot_volume_backup(
                boot_volume_backup_id=request.pop(util.camelize('boot_volume_backup_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetBootVolumeBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolumeBackup',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_get_boot_volume_kms_key(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetBootVolumeKmsKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'GetBootVolumeKmsKey')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetBootVolumeKmsKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_boot_volume_kms_key(
                boot_volume_id=request.pop(util.camelize('boot_volume_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetBootVolumeKmsKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolumeKmsKey',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_get_volume(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'GetVolume')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVolume')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume(
                volume_id=request.pop(util.camelize('volume_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetVolume',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volume',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_get_volume_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'GetVolumeBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVolumeBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_backup(
                volume_backup_id=request.pop(util.camelize('volume_backup_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetVolumeBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeBackup',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_get_volume_backup_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetVolumeBackupPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'GetVolumeBackupPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVolumeBackupPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_backup_policy(
                policy_id=request.pop(util.camelize('policy_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetVolumeBackupPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeBackupPolicy',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_get_volume_backup_policy_asset_assignment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetVolumeBackupPolicyAssetAssignment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'GetVolumeBackupPolicyAssetAssignment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVolumeBackupPolicyAssetAssignment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_backup_policy_asset_assignment(
                asset_id=request.pop(util.camelize('asset_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.get_volume_backup_policy_asset_assignment(
                    asset_id=request.pop(util.camelize('asset_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.get_volume_backup_policy_asset_assignment(
                        asset_id=request.pop(util.camelize('asset_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetVolumeBackupPolicyAssetAssignment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeBackupPolicyAssignment',
            False,
            True
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_get_volume_backup_policy_assignment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetVolumeBackupPolicyAssignment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'GetVolumeBackupPolicyAssignment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVolumeBackupPolicyAssignment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_backup_policy_assignment(
                policy_assignment_id=request.pop(util.camelize('policy_assignment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetVolumeBackupPolicyAssignment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeBackupPolicyAssignment',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_get_volume_group(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetVolumeGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'GetVolumeGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVolumeGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_group(
                volume_group_id=request.pop(util.camelize('volume_group_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetVolumeGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeGroup',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_get_volume_group_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetVolumeGroupBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'GetVolumeGroupBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVolumeGroupBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_group_backup(
                volume_group_backup_id=request.pop(util.camelize('volume_group_backup_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetVolumeGroupBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeGroupBackup',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_get_volume_kms_key(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'GetVolumeKmsKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'GetVolumeKmsKey')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVolumeKmsKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_kms_key(
                volume_id=request.pop(util.camelize('volume_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'GetVolumeKmsKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeKmsKey',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_list_boot_volume_backups(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListBootVolumeBackups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'ListBootVolumeBackups')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListBootVolumeBackups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_boot_volume_backups(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_boot_volume_backups(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_boot_volume_backups(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListBootVolumeBackups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolumeBackup',
            False,
            True
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_list_boot_volumes(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListBootVolumes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'ListBootVolumes')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListBootVolumes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_boot_volumes(
                availability_domain=request.pop(util.camelize('availability_domain')),
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_boot_volumes(
                    availability_domain=request.pop(util.camelize('availability_domain')),
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_boot_volumes(
                        availability_domain=request.pop(util.camelize('availability_domain')),
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListBootVolumes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolume',
            False,
            True
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_list_volume_backup_policies(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListVolumeBackupPolicies'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'ListVolumeBackupPolicies')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVolumeBackupPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_volume_backup_policies(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_volume_backup_policies(
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_volume_backup_policies(
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListVolumeBackupPolicies',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeBackupPolicy',
            False,
            True
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_list_volume_backups(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListVolumeBackups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'ListVolumeBackups')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVolumeBackups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_volume_backups(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_volume_backups(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_volume_backups(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListVolumeBackups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeBackup',
            False,
            True
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_list_volume_group_backups(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListVolumeGroupBackups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'ListVolumeGroupBackups')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVolumeGroupBackups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_volume_group_backups(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_volume_group_backups(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_volume_group_backups(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListVolumeGroupBackups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeGroupBackup',
            False,
            True
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_list_volume_groups(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListVolumeGroups'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'ListVolumeGroups')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVolumeGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_volume_groups(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_volume_groups(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_volume_groups(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListVolumeGroups',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeGroup',
            False,
            True
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_list_volumes(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ListVolumes'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'ListVolumes')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVolumes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_volumes(
                compartment_id=request.pop(util.camelize('compartment_id')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_volumes(
                    compartment_id=request.pop(util.camelize('compartment_id')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_volumes(
                        compartment_id=request.pop(util.camelize('compartment_id')),
                        page=next_response.headers[prev_page],
                        **(util.camel_to_snake_keys(request))
                    )
                    result.append(prev_response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ListVolumes',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volume',
            False,
            True
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_update_boot_volume(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateBootVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'UpdateBootVolume')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateBootVolume')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_boot_volume(
                boot_volume_id=request.pop(util.camelize('boot_volume_id')),
                update_boot_volume_details=request.pop(util.camelize('update_boot_volume_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateBootVolume',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolume',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_update_boot_volume_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateBootVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'UpdateBootVolumeBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateBootVolumeBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_boot_volume_backup(
                boot_volume_backup_id=request.pop(util.camelize('boot_volume_backup_id')),
                update_boot_volume_backup_details=request.pop(util.camelize('update_boot_volume_backup_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateBootVolumeBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolumeBackup',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_update_boot_volume_kms_key(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateBootVolumeKmsKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'UpdateBootVolumeKmsKey')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateBootVolumeKmsKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_boot_volume_kms_key(
                boot_volume_id=request.pop(util.camelize('boot_volume_id')),
                update_boot_volume_kms_key_details=request.pop(util.camelize('update_boot_volume_kms_key_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateBootVolumeKmsKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolumeKmsKey',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_update_volume(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateVolume'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'UpdateVolume')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateVolume')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_volume(
                volume_id=request.pop(util.camelize('volume_id')),
                update_volume_details=request.pop(util.camelize('update_volume_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateVolume',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volume',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_update_volume_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'UpdateVolumeBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_volume_backup(
                volume_backup_id=request.pop(util.camelize('volume_backup_id')),
                update_volume_backup_details=request.pop(util.camelize('update_volume_backup_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateVolumeBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeBackup',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_update_volume_group(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateVolumeGroup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'UpdateVolumeGroup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeGroup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_volume_group(
                volume_group_id=request.pop(util.camelize('volume_group_id')),
                update_volume_group_details=request.pop(util.camelize('update_volume_group_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateVolumeGroup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeGroup',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_update_volume_group_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateVolumeGroupBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'UpdateVolumeGroupBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeGroupBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_volume_group_backup(
                volume_group_backup_id=request.pop(util.camelize('volume_group_backup_id')),
                update_volume_group_backup_details=request.pop(util.camelize('update_volume_group_backup_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateVolumeGroupBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeGroupBackup',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_update_volume_kms_key(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateVolumeKmsKey'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'UpdateVolumeKmsKey')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeKmsKey')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['service_endpoint'] if 'service_endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_volume_kms_key(
                volume_id=request.pop(util.camelize('volume_id')),
                update_volume_kms_key_details=request.pop(util.camelize('update_volume_kms_key_details')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateVolumeKmsKey',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeKmsKey',
            False,
            False
        )
