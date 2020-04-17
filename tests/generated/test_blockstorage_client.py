# Code generated. DO NOT EDIT.
# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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

        cassette_location = os.path.join('generated', 'core_{name}.yml'.format(name=request.function.__name__))
        with custom_vcr.use_cassette(cassette_location, match_on=['method', 'scheme', 'host', 'port', 'path', 'session_agnostic_query_matcher']):
            yield


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_change_boot_volume_backup_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeBootVolumeBackupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'ChangeBootVolumeBackupCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeBootVolumeBackupCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.change_boot_volume_backup_compartment(
                boot_volume_backup_id=request.pop(util.camelize('bootVolumeBackupId')),
                change_boot_volume_backup_compartment_details=request.pop(util.camelize('ChangeBootVolumeBackupCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeBootVolumeBackupCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_boot_volume_backup_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_change_boot_volume_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeBootVolumeCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'ChangeBootVolumeCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeBootVolumeCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.change_boot_volume_compartment(
                boot_volume_id=request.pop(util.camelize('bootVolumeId')),
                change_boot_volume_compartment_details=request.pop(util.camelize('ChangeBootVolumeCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeBootVolumeCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_boot_volume_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_change_volume_backup_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeVolumeBackupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'ChangeVolumeBackupCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeVolumeBackupCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.change_volume_backup_compartment(
                volume_backup_id=request.pop(util.camelize('volumeBackupId')),
                change_volume_backup_compartment_details=request.pop(util.camelize('ChangeVolumeBackupCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeVolumeBackupCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_volume_backup_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_change_volume_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeVolumeCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'ChangeVolumeCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeVolumeCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.change_volume_compartment(
                volume_id=request.pop(util.camelize('volumeId')),
                change_volume_compartment_details=request.pop(util.camelize('ChangeVolumeCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeVolumeCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_volume_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_change_volume_group_backup_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeVolumeGroupBackupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'ChangeVolumeGroupBackupCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeVolumeGroupBackupCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.change_volume_group_backup_compartment(
                volume_group_backup_id=request.pop(util.camelize('volumeGroupBackupId')),
                change_volume_group_backup_compartment_details=request.pop(util.camelize('ChangeVolumeGroupBackupCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeVolumeGroupBackupCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_volume_group_backup_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_change_volume_group_compartment(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'ChangeVolumeGroupCompartment'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'ChangeVolumeGroupCompartment')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ChangeVolumeGroupCompartment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.change_volume_group_compartment(
                volume_group_id=request.pop(util.camelize('volumeGroupId')),
                change_volume_group_compartment_details=request.pop(util.camelize('ChangeVolumeGroupCompartmentDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'ChangeVolumeGroupCompartment',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'change_volume_group_compartment',
            False,
            False
        )


# IssueRoutingInfo tag="blockStorage" email="sic_block_storage_cp_us_grp@oracle.com" jiraProject="BLOCK" opsJiraProject="BSCP"
def test_copy_boot_volume_backup(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CopyBootVolumeBackup'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'CopyBootVolumeBackup')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CopyBootVolumeBackup')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.copy_boot_volume_backup(
                boot_volume_backup_id=request.pop(util.camelize('bootVolumeBackupId')),
                copy_boot_volume_backup_details=request.pop(util.camelize('CopyBootVolumeBackupDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CopyBootVolumeBackup',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'bootVolumeBackup',
            False,
            False
        )


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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.copy_volume_backup(
                volume_backup_id=request.pop(util.camelize('volumeBackupId')),
                copy_volume_backup_details=request.pop(util.camelize('CopyVolumeBackupDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_boot_volume(
                create_boot_volume_details=request.pop(util.camelize('CreateBootVolumeDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_boot_volume_backup(
                create_boot_volume_backup_details=request.pop(util.camelize('CreateBootVolumeBackupDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_volume(
                create_volume_details=request.pop(util.camelize('CreateVolumeDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_volume_backup(
                create_volume_backup_details=request.pop(util.camelize('CreateVolumeBackupDetails')),
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
def test_create_volume_backup_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'CreateVolumeBackupPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'CreateVolumeBackupPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='CreateVolumeBackupPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_volume_backup_policy(
                create_volume_backup_policy_details=request.pop(util.camelize('CreateVolumeBackupPolicyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'CreateVolumeBackupPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeBackupPolicy',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_volume_backup_policy_assignment(
                create_volume_backup_policy_assignment_details=request.pop(util.camelize('CreateVolumeBackupPolicyAssignmentDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_volume_group(
                create_volume_group_details=request.pop(util.camelize('CreateVolumeGroupDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.create_volume_group_backup(
                create_volume_group_backup_details=request.pop(util.camelize('CreateVolumeGroupBackupDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_boot_volume(
                boot_volume_id=request.pop(util.camelize('bootVolumeId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_boot_volume_backup(
                boot_volume_backup_id=request.pop(util.camelize('bootVolumeBackupId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_boot_volume_kms_key(
                boot_volume_id=request.pop(util.camelize('bootVolumeId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_volume(
                volume_id=request.pop(util.camelize('volumeId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_volume_backup(
                volume_backup_id=request.pop(util.camelize('volumeBackupId')),
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
def test_delete_volume_backup_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'DeleteVolumeBackupPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'DeleteVolumeBackupPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='DeleteVolumeBackupPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_volume_backup_policy(
                policy_id=request.pop(util.camelize('policyId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'DeleteVolumeBackupPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'delete_volume_backup_policy',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_volume_backup_policy_assignment(
                policy_assignment_id=request.pop(util.camelize('policyAssignmentId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_volume_group(
                volume_group_id=request.pop(util.camelize('volumeGroupId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_volume_group_backup(
                volume_group_backup_id=request.pop(util.camelize('volumeGroupBackupId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.delete_volume_kms_key(
                volume_id=request.pop(util.camelize('volumeId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_boot_volume(
                boot_volume_id=request.pop(util.camelize('bootVolumeId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_boot_volume_backup(
                boot_volume_backup_id=request.pop(util.camelize('bootVolumeBackupId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_boot_volume_kms_key(
                boot_volume_id=request.pop(util.camelize('bootVolumeId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume(
                volume_id=request.pop(util.camelize('volumeId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_backup(
                volume_backup_id=request.pop(util.camelize('volumeBackupId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_backup_policy(
                policy_id=request.pop(util.camelize('policyId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='GetVolumeBackupPolicyAssetAssignment')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_backup_policy_asset_assignment(
                asset_id=request.pop(util.camelize('assetId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.get_volume_backup_policy_asset_assignment(
                    asset_id=request.pop(util.camelize('assetId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.get_volume_backup_policy_asset_assignment(
                        asset_id=request.pop(util.camelize('assetId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_backup_policy_assignment(
                policy_assignment_id=request.pop(util.camelize('policyAssignmentId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_group(
                volume_group_id=request.pop(util.camelize('volumeGroupId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_group_backup(
                volume_group_backup_id=request.pop(util.camelize('volumeGroupBackupId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.get_volume_kms_key(
                volume_id=request.pop(util.camelize('volumeId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListBootVolumeBackups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_boot_volume_backups(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_boot_volume_backups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_boot_volume_backups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListBootVolumes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_boot_volumes(
                availability_domain=request.pop(util.camelize('availabilityDomain')),
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_boot_volumes(
                    availability_domain=request.pop(util.camelize('availabilityDomain')),
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_boot_volumes(
                        availability_domain=request.pop(util.camelize('availabilityDomain')),
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVolumeBackupPolicies')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_volume_backup_policies(
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVolumeBackups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_volume_backups(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_volume_backups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_volume_backups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVolumeGroupBackups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_volume_group_backups(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_volume_group_backups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_volume_group_backups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVolumeGroups')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_volume_groups(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_volume_groups(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_volume_groups(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
    mock_mode = config['test_mode'] == 'mock' if 'test_mode' in config else False

    request_containers = testing_service_client.get_requests(service_name='core', api_name='ListVolumes')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.list_volumes(
                compartment_id=request.pop(util.camelize('compartmentId')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
            if not mock_mode and response.has_next_page:
                next_page = response.headers['opc-next-page']
                request = request_containers[i]['request'].copy()
                next_response = client.list_volumes(
                    compartment_id=request.pop(util.camelize('compartmentId')),
                    page=next_page,
                    **(util.camel_to_snake_keys(request))
                )
                result.append(next_response)

                prev_page = 'opc-prev-page'
                if prev_page in next_response.headers:
                    request = request_containers[i]['request'].copy()
                    prev_response = client.list_volumes(
                        compartment_id=request.pop(util.camelize('compartmentId')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_boot_volume(
                boot_volume_id=request.pop(util.camelize('bootVolumeId')),
                update_boot_volume_details=request.pop(util.camelize('UpdateBootVolumeDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_boot_volume_backup(
                boot_volume_backup_id=request.pop(util.camelize('bootVolumeBackupId')),
                update_boot_volume_backup_details=request.pop(util.camelize('UpdateBootVolumeBackupDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_boot_volume_kms_key(
                boot_volume_id=request.pop(util.camelize('bootVolumeId')),
                update_boot_volume_kms_key_details=request.pop(util.camelize('UpdateBootVolumeKmsKeyDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_volume(
                volume_id=request.pop(util.camelize('volumeId')),
                update_volume_details=request.pop(util.camelize('UpdateVolumeDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_volume_backup(
                volume_backup_id=request.pop(util.camelize('volumeBackupId')),
                update_volume_backup_details=request.pop(util.camelize('UpdateVolumeBackupDetails')),
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
def test_update_volume_backup_policy(testing_service_client):
    if not testing_service_client.is_api_enabled('core', 'UpdateVolumeBackupPolicy'):
        pytest.skip('OCI Testing Service has not been configured for this operation yet.')

    config = util.test_config_to_python_config(
        testing_service_client.get_test_config('core', util.camelize('blockstorage'), 'UpdateVolumeBackupPolicy')
    )

    request_containers = testing_service_client.get_requests(service_name='core', api_name='UpdateVolumeBackupPolicy')

    for i in range(len(request_containers)):
        request = request_containers[i]['request'].copy()
        result = []
        service_error = None

        try:
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_volume_backup_policy(
                policy_id=request.pop(util.camelize('policyId')),
                update_volume_backup_policy_details=request.pop(util.camelize('UpdateVolumeBackupPolicyDetails')),
                **(util.camel_to_snake_keys(request))
            )
            result.append(response)
        except oci_exception.ServiceError as service_exception:
            service_error = service_exception

        testing_service_client.validate_result(
            'core',
            'UpdateVolumeBackupPolicy',
            request_containers[i]['containerId'],
            request_containers[i]['request'],
            result,
            service_error,
            'volumeBackupPolicy',
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_volume_group(
                volume_group_id=request.pop(util.camelize('volumeGroupId')),
                update_volume_group_details=request.pop(util.camelize('UpdateVolumeGroupDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_volume_group_backup(
                volume_group_backup_id=request.pop(util.camelize('volumeGroupBackupId')),
                update_volume_group_backup_details=request.pop(util.camelize('UpdateVolumeGroupBackupDetails')),
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
            service_endpoint = config['endpoint'] if 'endpoint' in config else None
            client = oci.core.BlockstorageClient(config, service_endpoint=service_endpoint)
            response = client.update_volume_kms_key(
                volume_id=request.pop(util.camelize('volumeId')),
                update_volume_kms_key_details=request.pop(util.camelize('UpdateVolumeKmsKeyDetails')),
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
