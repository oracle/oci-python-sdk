# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from . import util
from .. import test_config_container
import oci
import os
import pytest
import time


@pytest.fixture(scope="module")
def file_storage_client(request):
    config = oci.config.from_file(
        file_location=request.config.getoption("--config-file"),
        profile_name=request.config.getoption("--config-profile")
    )
    pass_phrase = os.environ.get('PYTHON_TESTS_ADMIN_PASS_PHRASE')
    if pass_phrase:
        config['pass_phrase'] = pass_phrase

    identity_client = oci.identity.IdentityClient(config)
    util.init_availability_domain_variables(identity_client, config['tenancy'])

    client = oci.file_storage.FileStorageClient(config)

    return client


@pytest.fixture(scope="module")
def file_system(file_storage_client):
    with test_config_container.create_vcr().use_cassette('test_file_storage_file_system_fixture.yml'):
        file_system_name = util.random_name('pysdk_test_fs')

        create_response = file_storage_client.create_file_system(
            oci.file_storage.models.CreateFileSystemDetails(
                display_name=file_system_name,
                compartment_id=util.COMPARTMENT_ID,
                availability_domain=util.availability_domain()
            ),
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
        )
        assert create_response.request_id
        assert create_response.headers.get('ETag')

        file_system = test_config_container.do_wait(
            file_storage_client,
            file_storage_client.get_file_system(create_response.data.id),
            'lifecycle_state',
            'ACTIVE'
        ).data
        assert file_system.id
        assert file_system.time_created
        assert file_system.lifecycle_state == 'ACTIVE'
        assert file_system.compartment_id == util.COMPARTMENT_ID
        assert file_system.availability_domain == util.availability_domain()
        assert file_system_name == file_system.display_name
        assert file_system.metered_bytes == 0

    yield file_system

    with test_config_container.create_vcr().use_cassette('test_file_storage_file_system_fixture_delete.yml'):
        file_storage_client.delete_file_system(file_system.id)
        test_config_container.do_wait(
            file_storage_client,
            file_storage_client.get_file_system(file_system.id),
            'lifecycle_state',
            'DELETED',
            succeed_on_not_found=True
        )


@pytest.fixture
def vcn_and_subnet(virtual_network):
    with test_config_container.create_vcr().use_cassette('test_file_storage_vcn_subnet_fixture.yml'):
        vcn_name = util.random_name('python_sdk_test_vcn')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        result = virtual_network.create_vcn(
            oci.core.models.CreateVcnDetails(
                cidr_block=cidr_block,
                display_name=vcn_name,
                compartment_id=util.COMPARTMENT_ID,
                dns_label=vcn_dns_label
            )
        )
        vcn = test_config_container.do_wait(
            virtual_network,
            virtual_network.get_vcn(result.data.id),
            'lifecycle_state',
            'AVAILABLE',
            max_wait_seconds=300
        ).data

        subnet_name = util.random_name('python_sdk_test_subnet')
        subnet_dns_label = util.random_name('pyfssub', insert_underscore=False)
        result = virtual_network.create_subnet(
            oci.core.models.CreateSubnetDetails(
                compartment_id=util.COMPARTMENT_ID,
                availability_domain=util.availability_domain(),
                display_name=subnet_name,
                vcn_id=vcn.id,
                cidr_block=cidr_block,
                dns_label=subnet_dns_label
            )
        )
        subnet = test_config_container.do_wait(
            virtual_network,
            virtual_network.get_subnet(result.data.id),
            'lifecycle_state',
            'AVAILABLE',
            max_wait_seconds=300
        ).data

    yield {'vcn': vcn, 'subnet': subnet}

    with test_config_container.create_vcr().use_cassette('test_file_storage_vcn_subnet_fixture_delete.yml'):
        # Sometimes we can't delete the subnet straight after the mount target because some VNIC is still
        # hanging around. If we get a conflict, try a few times before bailing out
        attempts = 0
        while attempts < 5:
            try:
                virtual_network.delete_subnet(subnet.id)
                test_config_container.do_wait(
                    virtual_network,
                    virtual_network.get_subnet(subnet.id),
                    'lifecycle_state',
                    'TERMINATED',
                    max_wait_seconds=600,
                    succeed_on_not_found=True
                )
                break
            except oci.exceptions.ServiceError as e:
                attempts += 1
                if e.status == 409 and attempts < 5:
                    time.sleep(5)
                elif e.status == 404:
                    # print('subnet already been deleted')
                    break
                else:
                    raise

        try:
            virtual_network.delete_vcn(vcn.id)
            test_config_container.do_wait(
                virtual_network,
                virtual_network.get_vcn(vcn.id),
                'lifecycle_state',
                'TERMINATED',
                max_wait_seconds=600,
                succeed_on_not_found=True
            )
        except oci.exceptions.ServiceError as e:
            if e.status == 404:
                # print('vcn already been deleted')
                pass
            else:
                raise


@pytest.fixture
def mount_target(file_storage_client, vcn_and_subnet):
    with test_config_container.create_vcr().use_cassette('test_file_storage_mount_target_fixture.yml'):
        mount_target_name = util.random_name('pysdk_test_mt')
        subnet = vcn_and_subnet['subnet']

        create_response = file_storage_client.create_mount_target(
            oci.file_storage.models.CreateMountTargetDetails(
                availability_domain=subnet.availability_domain,
                subnet_id=subnet.id,
                compartment_id=util.COMPARTMENT_ID,
                display_name=mount_target_name
            ),
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
        )
        assert create_response.request_id
        assert create_response.headers.get('ETag')

        get_mount_target_response = test_config_container.do_wait(
            file_storage_client,
            file_storage_client.get_mount_target(create_response.data.id),
            'lifecycle_state',
            'ACTIVE'
        )

        mount_target = get_mount_target_response.data
        assert mount_target.id
        assert mount_target.export_set_id
        assert mount_target.time_created
        assert mount_target.lifecycle_state == 'ACTIVE'
        assert mount_target.compartment_id == util.COMPARTMENT_ID
        assert mount_target.availability_domain == subnet.availability_domain
        assert mount_target.subnet_id == subnet.id

    yield mount_target

    with test_config_container.create_vcr().use_cassette('test_file_storage_mount_target_fixture_delete.yml'):
        file_storage_client.delete_mount_target(mount_target.id)
        test_config_container.do_wait(
            file_storage_client,
            get_mount_target_response,
            'lifecycle_state',
            'DELETED',
            succeed_on_not_found=True
        )


def test_crud_file_system(file_storage_client, file_system):
    with test_config_container.create_vcr().use_cassette('test_file_storage_crud_file_system.yml'):
        all_file_systems = oci.pagination.list_call_get_all_results(
            file_storage_client.list_file_systems,
            util.COMPARTMENT_ID,
            util.availability_domain()
        )

        found_fs = False
        for fs in all_file_systems.data:
            if fs.id == file_system.id:
                found_fs = True
                assert fs.time_created == file_system.time_created
                assert fs.compartment_id == file_system.compartment_id
                assert fs.metered_bytes == file_system.metered_bytes
                assert fs.lifecycle_state == file_system.lifecycle_state
                assert fs.availability_domain == file_system.availability_domain
                assert fs.display_name == file_system.display_name
        assert found_fs

        new_display_name = util.random_name('updated_pysdk_test_fs')
        update_response = file_storage_client.update_file_system(
            file_system.id,
            oci.file_storage.models.UpdateFileSystemDetails(display_name=new_display_name)
        )
        assert update_response.request_id
        assert update_response.headers.get('ETag')
        assert update_response.data.display_name == new_display_name


def test_crud_mount_target_and_export_set(file_storage_client, mount_target):
    with test_config_container.create_vcr().use_cassette('test_file_storage_crud_mount_target.yml'):
        all_mount_targets = oci.pagination.list_call_get_all_results(
            file_storage_client.list_mount_targets,
            util.COMPARTMENT_ID,
            util.availability_domain()
        )

        found_mount_target = False
        for mt in all_mount_targets.data:
            if mt.id == mount_target.id:
                found_mount_target = True
                assert mt.time_created == mount_target.time_created
                assert mt.compartment_id == mount_target.compartment_id
                assert mt.export_set_id == mount_target.export_set_id
                assert mt.display_name == mount_target.display_name
                assert mt.availability_domain == mount_target.availability_domain
                assert mt.subnet_id == mount_target.subnet_id
                assert mt.lifecycle_state == mount_target.lifecycle_state
                assert set(mt.private_ip_ids) == set(mount_target.private_ip_ids)
        assert found_mount_target

        new_display_name = util.random_name('up_pysdk_test_mt')
        update_response = file_storage_client.update_mount_target(
            mount_target.id,
            oci.file_storage.models.UpdateMountTargetDetails(display_name=new_display_name)
        )
        assert update_response.request_id
        assert update_response.headers.get('ETag')
        assert update_response.data.display_name == new_display_name

        all_export_sets = oci.pagination.list_call_get_all_results(
            file_storage_client.list_export_sets,
            util.COMPARTMENT_ID,
            util.availability_domain()
        )
        found_export_set = False
        for es in all_export_sets.data:
            if es.id == mount_target.export_set_id:
                found_export_set = True
                break
        assert found_export_set

        updated_export_set_name = util.random_name('up_pysdk_test_es')
        update_response = file_storage_client.update_export_set(
            mount_target.export_set_id,
            oci.file_storage.models.UpdateExportSetDetails(display_name=updated_export_set_name)
        )
        assert update_response.request_id
        assert update_response.headers.get('ETag')
        assert update_response.data.display_name == updated_export_set_name


def test_crud_export(file_storage_client, file_system, mount_target):
    with test_config_container.create_vcr().use_cassette('test_file_storage_crud_export.yml'):
        all_exports = oci.pagination.list_call_get_all_results(
            file_storage_client.list_exports,
            compartment_id=util.COMPARTMENT_ID,
            file_system_id=file_system.id
        )
        assert len(all_exports.data) == 0

        file_storage_client.create_export(
            oci.file_storage.models.CreateExportDetails(
                export_set_id=mount_target.export_set_id,
                file_system_id=file_system.id,
                path='/files'
            ),
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
        )

        all_exports = oci.pagination.list_call_get_all_results(
            file_storage_client.list_exports,
            compartment_id=util.COMPARTMENT_ID,
            file_system_id=file_system.id
        )
        assert len(all_exports.data) == 1
        assert all_exports.data[0].export_set_id == mount_target.export_set_id
        assert all_exports.data[0].file_system_id == file_system.id
        assert all_exports.data[0].id
        assert all_exports.data[0].time_created
        assert all_exports.data[0].path == '/files'

        all_exports_by_export_set = oci.pagination.list_call_get_all_results(
            file_storage_client.list_exports,
            compartment_id=util.COMPARTMENT_ID,
            export_set_id=mount_target.export_set_id
        )
        assert len(all_exports_by_export_set.data) == 1
        assert all_exports.data[0] == all_exports_by_export_set.data[0]

        get_export_response = test_config_container.do_wait(
            file_storage_client,
            file_storage_client.get_export(all_exports.data[0].id),
            'lifecycle_state',
            'ACTIVE'
        )
        export = get_export_response.data

        file_storage_client.delete_export(export.id)
        test_config_container.do_wait(
            file_storage_client,
            get_export_response,
            'lifecycle_state',
            'DELETED',
            succeed_on_not_found=True
        )

        all_exports = oci.pagination.list_call_get_all_results(
            file_storage_client.list_exports,
            compartment_id=util.COMPARTMENT_ID,
            file_system_id=file_system.id
        )
        _validate_export_deleted_or_not_present(all_exports.data, export.id)

        all_exports_by_export_set = oci.pagination.list_call_get_all_results(
            file_storage_client.list_exports,
            compartment_id=util.COMPARTMENT_ID,
            export_set_id=mount_target.export_set_id
        )
        _validate_export_deleted_or_not_present(all_exports_by_export_set.data, export.id)


def test_crud_snapshot(file_storage_client, file_system):
    with test_config_container.create_vcr().use_cassette('test_file_storage_crud_snapshot.yml'):
        all_snapshots = oci.pagination.list_call_get_all_results(
            file_storage_client.list_snapshots,
            file_system.id
        )
        assert len(all_snapshots.data) == 0

        create_response = file_storage_client.create_snapshot(
            oci.file_storage.models.CreateSnapshotDetails(
                file_system_id=file_system.id,
                name='my_snapshot_1'
            ),
            retry_strategy=oci.retry.DEFAULT_RETRY_STRATEGY
        )
        assert create_response.request_id
        assert create_response.headers.get('ETag')

        get_snapshot_response = test_config_container.do_wait(
            file_storage_client,
            file_storage_client.get_snapshot(create_response.data.id),
            'lifecycle_state',
            'ACTIVE'
        )
        snapshot = get_snapshot_response.data
        assert snapshot.id
        assert snapshot.file_system_id == file_system.id
        assert snapshot.name == 'my_snapshot_1'
        assert snapshot.lifecycle_state == 'ACTIVE'
        assert snapshot.time_created

        all_snapshots = oci.pagination.list_call_get_all_results(
            file_storage_client.list_snapshots,
            file_system.id
        )
        assert len(all_snapshots.data) == 1
        assert all_snapshots.data[0].id == snapshot.id

        file_storage_client.delete_snapshot(snapshot.id)
        test_config_container.do_wait(
            file_storage_client,
            get_snapshot_response,  # There's a chance the snapshot is already gone, so calling GET again 404s
            'lifecycle_state',
            'DELETED',
            succeed_on_not_found=True
        )
        all_snapshots = oci.pagination.list_call_get_all_results(
            file_storage_client.list_snapshots,
            file_system.id
        )
        if len(all_snapshots.data) != 0:
            for s in all_snapshots.data:
                assert s.lifecycle_state == 'DELETED'


def _validate_export_deleted_or_not_present(exports, export_id):
    if len(exports) == 0:
        return

    for e in exports:
        if e.id == export_id:
            assert e.lifecycle_state == 'DELETED'
