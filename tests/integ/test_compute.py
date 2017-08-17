# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import time
from . import util
import oci


class TestCompute:

    def test_all_operations(self, block_storage, compute, virtual_network):
        try:
            self.subtest_setup(block_storage, virtual_network)
            self.subtest_instance_operations(compute)
            self.subtest_windows_instance_operations(compute)
            self.subtest_vnic_operations(compute, virtual_network)
            self.subtest_list_vnics(compute)
            self.subtest_volume_attachment_operations(compute)
            self.subtest_shape_operations(compute)
            self.subtest_console_history_operations(compute)
            self.subtest_instance_action_operations(compute)
            self.subtest_image_operations(compute)
        finally:
            self.subtest_delete(block_storage, compute, virtual_network)

    @util.log_test
    def subtest_setup(self, block_storage, virtual_network):
        # Create a VCN
        vcn_name = util.random_name('python_sdk_test_compute_vcn')
        cidr_block = "10.0.0.0/16"

        create_vcn_details = oci.core.models.CreateVcnDetails()
        create_vcn_details.cidr_block = cidr_block
        create_vcn_details.display_name = vcn_name
        create_vcn_details.compartment_id = util.COMPARTMENT_ID

        result = virtual_network.create_vcn(create_vcn_details)
        util.validate_response(result, expect_etag=True)

        self.vcn_ocid = result.data.id

        oci.wait_until(virtual_network, virtual_network.get_vcn(self.vcn_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        # Create a subnet
        subnet_name = util.random_name('python_sdk_test_compute_subnet')

        create_subnet_details = oci.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = util.COMPARTMENT_ID
        create_subnet_details.availability_domain = util.availability_domain()
        create_subnet_details.display_name = subnet_name
        create_subnet_details.vcn_id = self.vcn_ocid
        create_subnet_details.cidr_block = cidr_block

        result = virtual_network.create_subnet(create_subnet_details)
        util.validate_response(result, expect_etag=True)

        self.subnet_ocid = result.data.id
        oci.wait_until(virtual_network, virtual_network.get_subnet(self.subnet_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        # Create a volume
        volume_name = util.random_name('python_sdk_test_compute_volume')
        create_volume_details = oci.core.models.CreateVolumeDetails()
        create_volume_details.availability_domain = util.availability_domain()
        create_volume_details.compartment_id = util.COMPARTMENT_ID
        create_volume_details.display_name = volume_name

        result = block_storage.create_volume(create_volume_details)
        util.validate_response(result)

        self.volume_ocid = result.data.id
        oci.wait_until(block_storage, block_storage.get_volume(self.volume_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=180)

    @util.log_test
    def subtest_instance_operations(self, compute):
        instance_name = util.random_name('python_sdk_test_instance')
        image_id = util.oracle_linux_image()
        shape = 'VM.Standard1.2'

        create_instance_details = oci.core.models.LaunchInstanceDetails()
        create_instance_details.compartment_id = util.COMPARTMENT_ID
        create_instance_details.availability_domain = util.availability_domain()
        create_instance_details.display_name = instance_name
        create_instance_details.subnet_id = self.subnet_ocid
        create_instance_details.image_id = image_id
        create_instance_details.shape = shape

        result = compute.launch_instance(create_instance_details)

        self.instance_ocid = result.data.id

        oci.wait_until(compute, compute.get_instance(self.instance_ocid), 'lifecycle_state', 'RUNNING', max_wait_seconds=600)

        result = compute.list_instances(util.COMPARTMENT_ID)
        util.validate_response(result)

        instance_name = instance_name + "_updated"
        update_instance_details = oci.core.models.UpdateInstanceDetails()
        update_instance_details.display_name = instance_name

        result = compute.update_instance(self.instance_ocid, update_instance_details)
        util.validate_response(result, expect_etag=True)

        result = compute.get_instance(self.instance_ocid)
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_windows_instance_operations(self, compute):
        instance_name = util.random_name('python_sdk_test_instance')
        image_id = util.windows_vm_image()
        shape = 'VM.Standard1.2'

        launch_instance_details = oci.core.models.LaunchInstanceDetails()
        launch_instance_details.compartment_id = util.COMPARTMENT_ID
        launch_instance_details.availability_domain = util.availability_domain()
        launch_instance_details.display_name = instance_name
        launch_instance_details.subnet_id = self.subnet_ocid
        launch_instance_details.image_id = image_id
        launch_instance_details.shape = shape

        result = compute.launch_instance(launch_instance_details)
        util.validate_response(result, expect_etag=True)
        self.windows_instance_ocid = result.data.id

        oci.wait_until(compute, compute.get_instance(self.windows_instance_ocid), 'lifecycle_state', 'RUNNING', max_wait_seconds=600)

        result = compute.get_instance(self.windows_instance_ocid)
        util.validate_response(result, expect_etag=True)

        result = compute.get_windows_instance_initial_credentials(self.windows_instance_ocid)
        util.validate_response(result)

        assert result.data.username == 'opc'
        assert result.data.password

    @util.log_test
    def subtest_list_vnics(self, compute):
        result = compute.list_vnic_attachments(util.COMPARTMENT_ID, instance_id=self.instance_ocid)
        util.validate_response(result)
        assert len(result.data) == 1

        # Check that setting limit to 1 will give us a next page token, and listing with that token gives
        # no more results.
        result = compute.list_vnic_attachments(util.COMPARTMENT_ID, instance_id=self.instance_ocid, limit=1)
        util.validate_response(result)

        assert len(result.data) == 1
        next_page = result.headers['opc-next-page']

        result = compute.list_vnic_attachments(util.COMPARTMENT_ID, instance_id=self.instance_ocid, page=next_page)
        util.validate_response(result)
        assert len(result.data) == 0

    @util.log_test
    def subtest_vnic_operations(self, compute, virtual_network):
        result = compute.list_vnic_attachments(util.COMPARTMENT_ID, instance_id=self.instance_ocid)
        util.validate_response(result)
        assert len(result.data) > 0
        vnic_id = result.data[0].vnic_id
        assert len(vnic_id) > 0

        # Test get vnic, since this is not tested in test_virtualnetwork.py.
        result = virtual_network.get_vnic(vnic_id)
        util.validate_response(result)

    @util.log_test
    def subtest_volume_attachment_operations(self, compute):
        va_name = util.random_name('python_sdk_test_va')

        attach_volume_details = oci.core.models.AttachVolumeDetails()
        attach_volume_details.display_name = va_name
        attach_volume_details.type = 'iscsi'
        attach_volume_details.instance_id = self.instance_ocid
        attach_volume_details.volume_id = self.volume_ocid

        result = compute.attach_volume(attach_volume_details)
        self.va_ocid = result.data.id
        util.validate_response(result, expect_etag=True)
        oci.wait_until(compute, compute.get_volume_attachment(self.va_ocid), 'lifecycle_state', 'ATTACHED', max_wait_seconds=300)

        result = compute.list_volume_attachments(util.COMPARTMENT_ID, instance_id=self.instance_ocid)
        util.validate_response(result)

        result = compute.get_volume_attachment(self.va_ocid)
        util.validate_response(result, expect_etag=True)

        compute.detach_volume(self.va_ocid)
        oci.wait_until(compute, compute.get_volume_attachment(self.va_ocid), 'lifecycle_state', 'DETACHED', max_wait_seconds=300)

    @util.log_test
    def subtest_shape_operations(self, compute):
        result = compute.list_images(util.COMPARTMENT_ID)
        util.validate_response(result)

    @util.log_test
    def subtest_console_history_operations(self, compute):
        capture_console_history_details = oci.core.models.CaptureConsoleHistoryDetails()
        capture_console_history_details.instance_id = self.instance_ocid
        result = compute.capture_console_history(capture_console_history_details)
        self.ch_ocid = result.data.id
        util.validate_response(result, expect_etag=True)
        oci.wait_until(compute, compute.get_console_history(self.ch_ocid), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        result = compute.list_console_histories(util.COMPARTMENT_ID, instance_id=self.instance_ocid)
        util.validate_response(result)

        result = compute.get_console_history(self.ch_ocid)
        util.validate_response(result, expect_etag=True)

        result = compute.get_console_history_content(self.ch_ocid)
        util.validate_response(result)

        assert result.status == 200
        assert len(result.data) > 500

    @util.log_test
    def subtest_instance_action_operations(self, compute):
        result = compute.instance_action(self.instance_ocid, "RESET")
        util.validate_response(result)
        time.sleep(10)
        oci.wait_until(compute, compute.get_instance(self.instance_ocid), 'lifecycle_state', 'RUNNING', max_wait_seconds=300)
        time.sleep(5)

    @util.log_test
    def subtest_image_operations(self, compute):
        image_name = util.random_name('python_sdk_test_image')

        create_image_details = oci.core.models.CreateImageDetails()
        create_image_details.display_name = image_name
        create_image_details.instance_id = self.instance_ocid
        create_image_details.compartment_id = util.COMPARTMENT_ID

        result = compute.create_image(create_image_details)
        self.image_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        # Waiting for the image can take 20 or 30 minutes. Instead, we'll just delete the instance
        # while it's still taking the snapshot. Uncomment the wait below to wait for the image to finish.
        # oci.wait_until(compute, compute.get_image(self.image_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=2700)

        result = compute.list_images(util.COMPARTMENT_ID)
        util.validate_response(result)

        result = compute.get_image(self.image_ocid)
        util.validate_response(result, expect_etag=True)

        update_image_details = oci.core.models.UpdateImageDetails()
        update_image_details.display_name = image_name + "_updated"
        result = compute.update_image(self.image_ocid, update_image_details)
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_delete(self, block_storage, compute, virtual_network):
        error_count = 0

        if hasattr(self, 'image_ocid'):
            try:
                print("Deleting image")
                compute.delete_image(self.image_ocid)
            except Exception as error:
                if error.status != 409:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'ch_ocid'):
            try:
                print("Deleting console history")
                compute.delete_console_history(self.ch_ocid)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'instance_ocid'):
            try:
                print("Deleting instance")
                compute.terminate_instance(self.instance_ocid)
                oci.wait_until(compute, compute.get_instance(self.instance_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                # succeed if resource is deleted already
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'windows_instance_ocid'):
            try:
                print("Deleting windows instance")
                compute.terminate_instance(self.windows_instance_ocid)
                oci.wait_until(compute, compute.get_instance(self.windows_instance_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                # succeed if resource is deleted already
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'volume_ocid'):
            try:
                print("Deleting volume")
                block_storage.delete_volume(self.volume_ocid)
            except Exception as error:
                util.print_latest_exception(error)
                error_count = error_count + 1

        if hasattr(self, 'subnet_ocid'):
            try:
                print("Deleting subnet")
                virtual_network.delete_subnet(self.subnet_ocid)
                oci.wait_until(virtual_network, virtual_network.get_subnet(self.subnet_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                # succeed if resource is deleted already
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'vcn_ocid'):
            try:
                print("Deleting vcn")
                virtual_network.delete_vcn(self.vcn_ocid)
                oci.wait_until(virtual_network, virtual_network.get_vcn(self.vcn_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                # succeed if resource is deleted already
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        assert error_count == 0
