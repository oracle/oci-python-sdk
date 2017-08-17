# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from . import util
import oci


class TestBlockStorage:

    def test_all_operations(self, block_storage):
        try:
            self.subtest_volume_operations(block_storage)
            self.subtest_volume_backup_operations(block_storage)
        finally:
            self.subtest_delete(block_storage)

    @util.log_test
    def subtest_volume_operations(self, block_storage):
        volume_name = util.random_name('python_sdk_test_volume')
        create_volume_details = oci.core.models.CreateVolumeDetails()
        create_volume_details.availability_domain = util.availability_domain()
        create_volume_details.compartment_id = util.COMPARTMENT_ID
        create_volume_details.display_name = volume_name

        result = block_storage.create_volume(create_volume_details)
        util.validate_response(result)
        self.volume_id = result.data.id
        oci.wait_until(block_storage, block_storage.get_volume(self.volume_id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=180)

        result = block_storage.get_volume(self.volume_id)
        util.validate_response(result)

        result = block_storage.list_volumes(util.COMPARTMENT_ID)
        util.validate_response(result)

        volume_name = volume_name + "_UPDATED"
        update_volume_details = oci.core.models.UpdateVolumeDetails()
        update_volume_details.display_name = volume_name
        result = block_storage.update_volume(self.volume_id, update_volume_details)
        util.validate_response(result)
        oci.wait_until(block_storage, block_storage.get_volume(self.volume_id), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=180)

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

        assert error_count == 0
