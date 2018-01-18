# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import time
from . import util
from .. import test_config_container
import oci


class TestVnicSourceDestCheck:

    def test_vnic_source_dest(self, compute, virtual_network):
        with test_config_container.create_vcr().use_cassette('test_vnic_source_dest.yml'):
            try:
                self.create_resources(compute, virtual_network)
                self.subtest_vnic_source_dest(compute, virtual_network)
            finally:
                self.clean_up_resources(compute, virtual_network)

    @util.log_test
    def subtest_vnic_source_dest(self, compute, virtual_network):
        result = compute.list_vnic_attachments(util.COMPARTMENT_ID, instance_id=self.instance_ocid)
        util.validate_response(result)
        assert len(result.data) == 1

        # We do an initial create with skip on the VNIC set to True, so grab the VNIC and check that
        vnic_id = result.data[0].vnic_id
        get_vnic_response = virtual_network.get_vnic(vnic_id)
        assert get_vnic_response.data.skip_source_dest_check

        # Update the VNIC so that skip is set to False. Ensure that this is echoed in the response to
        # update_vnic, as well as when we get the VNIC again
        update_vnic_details = oci.core.models.UpdateVnicDetails()
        update_vnic_details.skip_source_dest_check = False
        update_vnic_response = virtual_network.update_vnic(vnic_id, update_vnic_details)
        assert not update_vnic_response.data.skip_source_dest_check

        get_vnic_response = virtual_network.get_vnic(vnic_id)
        assert not get_vnic_response.data.skip_source_dest_check

        # Update the VNIC so that skip is set back to True. Ensure that this is echoed in the response to
        # update_vnic, as well as when we get the VNIC again
        update_vnic_details.skip_source_dest_check = True
        update_vnic_response = virtual_network.update_vnic(vnic_id, update_vnic_details)
        assert update_vnic_response.data.skip_source_dest_check

        get_vnic_response = virtual_network.get_vnic(vnic_id)
        assert get_vnic_response.data.skip_source_dest_check

        # Attach without specifying whether to skip the source/dest check (defaults to False)
        self.attach_update_then_detach_vnic(compute, virtual_network, None)

        # Attach with skip source/dest check explicitly False
        self.attach_update_then_detach_vnic(compute, virtual_network, False)

        # Attach with skip source/dest check explicitly True
        self.attach_update_then_detach_vnic(compute, virtual_network, False)

    def attach_update_then_detach_vnic(self, compute, virtual_network, skip_source_dest_check):
        create_vnic_details = oci.core.models.CreateVnicDetails()
        create_vnic_details.subnet_id = self.subnet_ocid

        if skip_source_dest_check is None:
            expected_skip_source_dest_check = False
        else:
            expected_skip_source_dest_check = skip_source_dest_check

        attach_vnic_details = oci.core.models.AttachVnicDetails()
        attach_vnic_details.instance_id = self.instance_ocid
        attach_vnic_details.create_vnic_details = create_vnic_details

        attach_vnic_response = compute.attach_vnic(attach_vnic_details)
        self.second_vnic_attachment_id = attach_vnic_response.data.id

        test_config_container.do_wait(compute, compute.get_vnic_attachment(self.second_vnic_attachment_id), 'lifecycle_state', 'ATTACHED', max_wait_seconds=300)

        vnic_attachment = compute.get_vnic_attachment(self.second_vnic_attachment_id).data
        get_vnic_response = virtual_network.get_vnic(vnic_attachment.vnic_id)

        if expected_skip_source_dest_check:
            # TODO: In LA/preview we cannot attach a VNIC and specify True for the skip source/dest check value. We have to update
            # it post-creation
            assert True
            # assert get_vnic_response.data.skip_source_dest_check
        else:
            assert not get_vnic_response.data.skip_source_dest_check

        # Update to be True
        update_vnic_details = oci.core.models.UpdateVnicDetails()
        update_vnic_details.skip_source_dest_check = True
        update_vnic_response = virtual_network.update_vnic(vnic_attachment.vnic_id, update_vnic_details)
        assert update_vnic_response.data.skip_source_dest_check

        get_vnic_response = virtual_network.get_vnic(vnic_attachment.vnic_id)
        assert get_vnic_response.data.skip_source_dest_check

        # Update to be False
        update_vnic_details.skip_source_dest_check = False
        update_vnic_response = virtual_network.update_vnic(vnic_attachment.vnic_id, update_vnic_details)
        assert not update_vnic_response.data.skip_source_dest_check

        get_vnic_response = virtual_network.get_vnic(vnic_attachment.vnic_id)
        assert not get_vnic_response.data.skip_source_dest_check

        time.sleep(10)
        compute.detach_vnic(self.second_vnic_attachment_id)
        test_config_container.do_wait(compute, compute.get_vnic_attachment(self.second_vnic_attachment_id), 'lifecycle_state', 'DETACHED', max_wait_seconds=300)
        time.sleep(10)

    @util.log_test
    def create_resources(self, compute, virtual_network):
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
        test_config_container.do_wait(virtual_network, virtual_network.get_vcn(self.vcn_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

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
        test_config_container.do_wait(virtual_network, virtual_network.get_subnet(self.subnet_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        instance_name = util.random_name('python_sdk_test_instance')
        image_id = 'ocid1.image.oc1.phx.aaaaaaaamv5wg7ffvaxaba3orhpuya7x7opz24hd6m7epmwfqbeudi6meepq'  # ol6.8-base-0.0.2
        shape = 'VM.Standard1.1'

        create_vnic_details = oci.core.models.CreateVnicDetails()
        create_vnic_details.subnet_id = self.subnet_ocid
        create_vnic_details.skip_source_dest_check = True

        create_instance_details = oci.core.models.LaunchInstanceDetails()
        create_instance_details.compartment_id = util.COMPARTMENT_ID
        create_instance_details.availability_domain = util.availability_domain()
        create_instance_details.display_name = instance_name
        create_instance_details.subnet_id = self.subnet_ocid
        create_instance_details.image_id = image_id
        create_instance_details.shape = shape
        create_instance_details.create_vnic_details = create_vnic_details

        result = compute.launch_instance(create_instance_details)
        self.instance_ocid = result.data.id

        test_config_container.do_wait(compute, compute.get_instance(self.instance_ocid), 'lifecycle_state', 'RUNNING', max_wait_seconds=600)

    @util.log_test
    def clean_up_resources(self, compute, virtual_network):
        error_count = 0

        if (hasattr(self, 'second_vnic_attachment_id')):
            try:
                time.sleep(10)
                print("Detaching second VNIC")
                compute.detach_vnic(self.second_vnic_attachment_id)
                test_config_container.do_wait(compute, compute.get_vnic_attachment(self.second_vnic_attachment_id), 'lifecycle_state', 'DETACHED', max_wait_seconds=300)
            except Exception as error:
                # succeed if resource is deleted already
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'instance_ocid'):
            try:
                print("Deleting instance")
                compute.terminate_instance(self.instance_ocid)
                test_config_container.do_wait(compute, compute.get_instance(self.instance_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                # succeed if resource is deleted already
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'subnet_ocid'):
            try:
                print("Deleting subnet")
                virtual_network.delete_subnet(self.subnet_ocid)
                test_config_container.do_wait(virtual_network, virtual_network.get_subnet(self.subnet_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                # succeed if resource is deleted already
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'vcn_ocid'):
            try:
                print("Deleting vcn")
                virtual_network.delete_vcn(self.vcn_ocid)
                test_config_container.do_wait(virtual_network, virtual_network.get_vcn(self.vcn_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                # succeed if resource is deleted already
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        assert error_count == 0
