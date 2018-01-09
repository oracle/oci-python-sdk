# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from . import util
import oci
import pytest


class TestBlockStorage:

    def test_all_operations(self, block_storage):
        try:
            self.subtest_volume_operations(block_storage)
            self.subtest_create_volume_both_mb_and_gb_given(block_storage)
            self.subtest_volume_backup_operations(block_storage)
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
        oci.wait_until(block_storage, block_storage.get_volume(volume_id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=180)

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
        oci.wait_until(block_storage, block_storage.get_volume(volume_id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=180)

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

        oci.wait_until(block_storage, block_storage.get_volume_backup(self.backup_id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=600)

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
        oci.wait_until(block_storage, block_storage.get_volume_backup(self.backup_id), 'lifecycle_state', 'AVAILABLE', max_interval_seconds=180)

    @util.log_test
    def subtest_delete(self, block_storage):
        error_count = 0

        if hasattr(self, 'backup_id'):
            try:
                block_storage.delete_volume_backup(self.backup_id)
                oci.wait_until(block_storage, block_storage.get_volume_backup(self.backup_id), 'lifecycle_state', 'TERMINATED', max_interval_seconds=180)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'volume_id'):
            try:
                block_storage.delete_volume(self.volume_id)
                oci.wait_until(block_storage, block_storage.get_volume(self.volume_id), 'lifecycle_state', 'TERMINATED', max_interval_seconds=180)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'volume_id_two'):
            try:
                block_storage.delete_volume(self.volume_id_two)
                oci.wait_until(block_storage, block_storage.get_volume(self.volume_id_two), 'lifecycle_state', 'TERMINATED', max_interval_seconds=180)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        assert error_count == 0
