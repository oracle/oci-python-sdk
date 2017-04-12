# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from . import util
import oraclebmc


IPXE_SCRIPT_FILE = 'tests/resources/ipxe_script_example.txt'


class TestLaunchInstanceOptions:

    @util.slow
    def test_main(self, compute, virtual_network):
        try:
            self.subtest_setup(virtual_network)
            self.subtest_launch_instance_ipxe_script_file(compute, virtual_network)
        finally:
            self.subtest_delete(compute, virtual_network)

    @util.log_test
    def subtest_setup(self, virtual_network):
        # Create a VCN
        vcn_name = util.random_name('python_sdk_test_compute_vcn')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        create_vcn_details = oraclebmc.core.models.CreateVcnDetails()
        create_vcn_details.compartment_id = util.COMPARTMENT_ID
        create_vcn_details.display_name = vcn_name
        create_vcn_details.cidr_block = cidr_block
        create_vcn_details.dns_label = vcn_dns_label

        result = virtual_network.create_vcn(create_vcn_details)
        self.vcn_ocid = result.data.id
        util.validate_response(result, expect_etag=True)
        oraclebmc.wait_until(virtual_network, virtual_network.get_vcn(self.vcn_ocid), 'lifecycle_state', 'AVAILABLE',
                             max_wait_seconds=300)

        # Create a subnet
        subnet_name = util.random_name('python_sdk_test_compute_subnet')
        subnet_dns_label = util.random_name('subnet', insert_underscore=False)

        create_subnet_details = oraclebmc.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = util.COMPARTMENT_ID
        create_subnet_details.availability_domain = util.AVAILABILITY_DOMAIN
        create_subnet_details.display_name = subnet_name
        create_subnet_details.vcn_id = self.vcn_ocid
        create_subnet_details.dns_label = subnet_dns_label
        create_subnet_details.cidr_block = cidr_block

        result = virtual_network.create_subnet(create_subnet_details)
        self.subnet_ocid = result.data.id
        util.validate_response(result, expect_etag=True)
        oraclebmc.wait_until(virtual_network, virtual_network.get_subnet(self.subnet_ocid), 'lifecycle_state',
                             'AVAILABLE', max_wait_seconds=300)

    @util.log_test
    def subtest_launch_instance_ipxe_script_file(self, compute, virtual_network):
        instance_name = util.random_name('python_sdk_test_instance_options')
        image_id = 'ocid1.image.oc1.phx.aaaaaaaamv5wg7ffvaxaba3orhpuya7x7opz24hd6m7epmwfqbeudi6meepq'  # ol6.8-base-0.0.2
        shape = 'VM.Standard1.2'
        hostname_label = util.random_name('bminstance', insert_underscore=False)

        with open(IPXE_SCRIPT_FILE, mode='r') as file:
            ipxe_script_content = file.read()

        launch_instance_details = oraclebmc.core.models.LaunchInstanceDetails()
        launch_instance_details.compartment_id = util.COMPARTMENT_ID
        launch_instance_details.availability_domain = util.AVAILABILITY_DOMAIN
        launch_instance_details.display_name = instance_name
        launch_instance_details.subnet_id = self.subnet_ocid
        launch_instance_details.image_id = image_id
        launch_instance_details.shape = shape
        launch_instance_details.ipxe_script = ipxe_script_content
        launch_instance_details.hostname_label = hostname_label

        launch_instance_result = compute.launch_instance(launch_instance_details)
        self.instance_ocid = launch_instance_result.data.id

        util.validate_response(launch_instance_result, expect_etag=True)

        util.wait_until(lambda: compute.list_vnic_attachments(util.COMPARTMENT_ID, instance_id=self.instance_ocid),
                        'ATTACHED', max_wait_seconds=20, item_index_in_list_response=0)

        # get vnic attachments for given instance
        result = compute.list_vnic_attachments(util.COMPARTMENT_ID, instance_id=self.instance_ocid)
        vnic_id = result.data[0].vnic_id

        # get full data for vnic attached to new instance (which includes hostname-label)
        get_vnic_result = virtual_network.get_vnic(vnic_id)

        # validate that hostname label matches what was supplied in --dns-label
        assert get_vnic_result.data.hostname_label == hostname_label

        assert launch_instance_result.data.ipxe_script
        # Just look at the first few characters. Once we hit a line break the formatting will differ.
        assert ipxe_script_content[:5] in launch_instance_result.data.ipxe_script

    @util.log_test
    def subtest_delete(self, compute, virtual_network):
        error_count = 0

        if hasattr(self, 'instance_ocid'):
            try:
                print("Deleting instance")
                compute.terminate_instance(self.instance_ocid)
                oraclebmc.wait_until(compute, compute.get_instance(self.instance_ocid), 'lifecycle_state', 'TERMINATED',
                                     max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'subnet_ocid'):
            try:
                print("Deleting subnet")
                virtual_network.delete_subnet(self.subnet_ocid)
                oraclebmc.wait_until(virtual_network, virtual_network.get_subnet(self.subnet_ocid), 'lifecycle_state',
                                     'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'vcn_ocid'):
            try:
                print("Deleting vcn")
                virtual_network.delete_vcn(self.vcn_ocid)
                oraclebmc.wait_until(virtual_network, virtual_network.get_vcn(self.vcn_ocid), 'lifecycle_state',
                                     'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        assert error_count == 0
