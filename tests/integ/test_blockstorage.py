# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from . import util
from .. import test_config_container
import oci
import pytest


class TestBlockStorage:

    def test_all_operations(self, block_storage):
        with test_config_container.create_vcr().use_cassette('test_blockstorage_all_operations.yml'):
            try:
                self.subtest_volume_operations(block_storage)
                self.subtest_create_volume_both_mb_and_gb_given(block_storage)
                self.subtest_volume_backup_operations(block_storage)
                self.subtest_volume_backup_policies(block_storage)
            finally:
                self.subtest_delete(block_storage)

    @util.log_test
    def subtest_volume_operations(self, block_storage):
        volume_name_mbs = util.random_name('python_sdk_test_volume_mb')
        create_volume_details_mbs = oci.core.models.CreateVolumeDetails()
        create_volume_details_mbs.availability_domain = util.availability_domain()
        create_volume_details_mbs.compartment_id = util.COMPARTMENT_ID
        create_volume_details_mbs.display_name = volume_name_mbs
        create_volume_details_mbs.size_in_mbs = 50 * 1024
        self.volume_id = self.volume_operations_internal(block_storage, create_volume_details_mbs)

        volume_name_gbs = util.random_name('python_sdk_test_volume_gb')
        create_volume_details_gbs = oci.core.models.CreateVolumeDetails()
        create_volume_details_gbs.availability_domain = util.availability_domain()
        create_volume_details_gbs.compartment_id = util.COMPARTMENT_ID
        create_volume_details_gbs.display_name = volume_name_gbs
        create_volume_details_gbs.size_in_gbs = 50
        self.volume_id_two = self.volume_operations_internal(block_storage, create_volume_details_mbs)

    def volume_operations_internal(self, block_storage, create_volume_details):
        result = block_storage.create_volume(create_volume_details)
        util.validate_response(result)
        volume_id = result.data.id
        test_config_container.do_wait(block_storage, block_storage.get_volume(volume_id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=180)

        if create_volume_details.size_in_mbs is not None:
            assert result.data.size_in_mbs == create_volume_details.size_in_mbs
        elif create_volume_details.size_in_gbs is not None:
            assert result.data.size_in_gbs == create_volume_details.size_in_gbs

        result = block_storage.get_volume(volume_id)
        util.validate_response(result)

        result = block_storage.list_volumes(util.COMPARTMENT_ID)
        util.validate_response(result)

        volume_name = create_volume_details.display_name + "_UPDATED"
        update_volume_details = oci.core.models.UpdateVolumeDetails()
        update_volume_details.display_name = volume_name
        result = block_storage.update_volume(volume_id, update_volume_details)
        util.validate_response(result)
        test_config_container.do_wait(block_storage, block_storage.get_volume(volume_id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=180)

        return volume_id

    @util.log_test
    def subtest_create_volume_both_mb_and_gb_given(self, block_storage):
        volume_name = util.random_name('python_sdk_test_volume')
        create_volume_details = oci.core.models.CreateVolumeDetails()
        create_volume_details.availability_domain = util.availability_domain()
        create_volume_details.compartment_id = util.COMPARTMENT_ID
        create_volume_details.display_name = volume_name
        create_volume_details.size_in_gbs = 50
        create_volume_details.size_in_mbs = create_volume_details.size_in_gbs * 1024

        with pytest.raises(oci.exceptions.ServiceError):
            block_storage.create_volume(create_volume_details)

    @util.log_test
    def subtest_volume_backup_operations(self, block_storage):
        backup_name = util.random_name('python_sdk_test_backup')
        create_volume_backup_details = oci.core.models.CreateVolumeBackupDetails()
        create_volume_backup_details.display_name = backup_name
        create_volume_backup_details.volume_id = self.volume_id
        result = block_storage.create_volume_backup(create_volume_backup_details)
        util.validate_response(result)
        self.backup_id = result.data.id

        test_config_container.do_wait(block_storage, block_storage.get_volume_backup(self.backup_id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=600)

        result = block_storage.get_volume_backup(self.backup_id)
        util.validate_response(result)
        assert result.data.size_in_gbs is not None
        assert result.data.size_in_mbs is not None
        assert result.data.unique_size_in_gbs is not None
        assert result.data.unique_size_in_mbs is not None

        result = block_storage.list_volume_backups(util.COMPARTMENT_ID)
        util.validate_response(result)

        result = block_storage.list_volume_backups(util.COMPARTMENT_ID, volume_id=self.volume_id)
        util.validate_response(result)
        assert 1 == len(result.data)

        backup_name = backup_name + "_UPDATED"
        update_volume_backup_details = oci.core.models.UpdateVolumeBackupDetails()
        update_volume_backup_details.display_name = backup_name

        result = block_storage.update_volume_backup(self.backup_id, update_volume_backup_details)
        util.validate_response(result)

        # Make sure we're still in a good state before deleting.
        test_config_container.do_wait(block_storage, block_storage.get_volume_backup(self.backup_id), 'lifecycle_state', 'AVAILABLE', max_interval_seconds=180)

    @util.log_test
    def subtest_volume_backup_policies(self, block_storage):
        volume_backup_policies = oci.pagination.list_call_get_all_results(block_storage.list_volume_backup_policies)
        assert len(volume_backup_policies.data) > 0
        for policy in volume_backup_policies.data:
            assert policy.display_name
            assert policy.id
            assert policy.time_created
            assert len(policy.schedules) > 0
            for schedule in policy.schedules:
                assert schedule.backup_type
                assert schedule.period
                assert schedule.retention_seconds
                assert schedule.offset_seconds is not None

        policy_from_list = volume_backup_policies.data[0]
        volume_backup_policy = block_storage.get_volume_backup_policy(policy_from_list.id).data
        assert policy_from_list.display_name == volume_backup_policy.display_name
        assert policy_from_list.id == volume_backup_policy.id
        assert policy_from_list.time_created == volume_backup_policy.time_created
        assert len(volume_backup_policy.schedules) > 0
        for schedule in volume_backup_policy.schedules:
            assert schedule.backup_type
            assert schedule.period
            assert schedule.retention_seconds
            assert schedule.offset_seconds is not None

        create_response = block_storage.create_volume_backup_policy_assignment(
            oci.core.models.CreateVolumeBackupPolicyAssignmentDetails(
                asset_id=self.volume_id,
                policy_id=volume_backup_policy.id
            )
        )
        assert create_response.request_id
        assert create_response.headers.get('etag')
        assert create_response.data.asset_id == self.volume_id
        assert create_response.data.policy_id == volume_backup_policy.id
        assert create_response.data.time_created
        assert create_response.data.id

        get_policy_assignment = block_storage.get_volume_backup_policy_assignment(create_response.data.id)
        assert get_policy_assignment.data.asset_id == self.volume_id
        assert get_policy_assignment.data.policy_id == volume_backup_policy.id
        assert get_policy_assignment.data.time_created == create_response.data.time_created

        get_policy_asset_assignment = block_storage.get_volume_backup_policy_asset_assignment(self.volume_id)
        assert len(get_policy_asset_assignment.data) == 1
        assert get_policy_asset_assignment.data[0].id == get_policy_assignment.data.id
        assert get_policy_asset_assignment.data[0].asset_id == get_policy_assignment.data.asset_id
        assert get_policy_asset_assignment.data[0].policy_id == get_policy_assignment.data.policy_id
        assert get_policy_asset_assignment.data[0].time_created == get_policy_assignment.data.time_created

        block_storage.delete_volume_backup_policy_assignment(get_policy_assignment.data.id)
        get_policy_asset_assignment = block_storage.get_volume_backup_policy_asset_assignment(self.volume_id)
        assert len(get_policy_asset_assignment.data) == 0

        # Create a volume and assign a policy at create time
        result = block_storage.create_volume(
            oci.core.models.CreateVolumeDetails(
                display_name=util.random_name('python_sdk_pol_at_create'),
                size_in_gbs=50,
                availability_domain=util.availability_domain(),
                compartment_id=util.COMPARTMENT_ID,
                backup_policy_id=volume_backup_policy.id
            )
        )
        volume_id = result.data.id
        test_config_container.do_wait(block_storage, block_storage.get_volume(volume_id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=180)
        get_policy_asset_assignment = block_storage.get_volume_backup_policy_asset_assignment(volume_id)
        assert len(get_policy_asset_assignment.data) == 1
        assert get_policy_asset_assignment.data[0].id
        assert get_policy_asset_assignment.data[0].asset_id == volume_id
        assert get_policy_asset_assignment.data[0].policy_id == volume_backup_policy.id
        assert get_policy_asset_assignment.data[0].time_created

        block_storage.delete_volume_backup_policy_assignment(get_policy_asset_assignment.data[0].id)

        block_storage.delete_volume(volume_id)
        test_config_container.do_wait(block_storage, block_storage.get_volume(volume_id), 'lifecycle_state', 'TERMINATED', max_interval_seconds=180, succeed_on_not_found=True)

    @util.log_test
    def subtest_delete(self, block_storage):
        error_count = 0

        if hasattr(self, 'backup_id'):
            try:
                block_storage.delete_volume_backup(self.backup_id)
                test_config_container.do_wait(block_storage, block_storage.get_volume_backup(self.backup_id), 'lifecycle_state', 'TERMINATED', max_interval_seconds=180)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'volume_id'):
            try:
                block_storage.delete_volume(self.volume_id)
                test_config_container.do_wait(block_storage, block_storage.get_volume(self.volume_id), 'lifecycle_state', 'TERMINATED', max_interval_seconds=180)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'volume_id_two'):
            try:
                block_storage.delete_volume(self.volume_id_two)
                test_config_container.do_wait(block_storage, block_storage.get_volume(self.volume_id_two), 'lifecycle_state', 'TERMINATED', max_interval_seconds=180)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        assert error_count == 0
