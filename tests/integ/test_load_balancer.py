# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import oci
import time
from . import util


class TestLoadBalancer:
    def test_operations(self, load_balancer_client, virtual_network):
        try:
            self.subtest_basic_operations(load_balancer_client, virtual_network)
        finally:
            time.sleep(20)
            self.subtest_delete(load_balancer_client, virtual_network)

    @util.log_test
    def subtest_basic_operations(self, load_balancer_client, virtual_network):
        # Create a VCN
        vcn_name = util.random_name('python_sdk_test_lb_vcn')
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
        subnet_name = util.random_name('python_sdk_test_lb_subnet')

        subnet_cidr_block1 = "10.0.0.0/24"

        create_subnet_details = oci.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = util.COMPARTMENT_ID
        create_subnet_details.availability_domain = util.availability_domain()
        create_subnet_details.display_name = subnet_name
        create_subnet_details.vcn_id = self.vcn_ocid
        create_subnet_details.cidr_block = subnet_cidr_block1

        result = virtual_network.create_subnet(create_subnet_details)
        util.validate_response(result, expect_etag=True)

        self.subnet_ocid1 = result.data.id
        oci.wait_until(virtual_network, virtual_network.get_subnet(self.subnet_ocid1), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        # Create a subnet
        subnet_name = util.random_name('python_sdk_test_lb_subnet')
        subnet_cidr_block2 = "10.0.1.0/24"

        create_subnet_details = oci.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = util.COMPARTMENT_ID
        create_subnet_details.availability_domain = util.second_availability_domain()
        create_subnet_details.display_name = subnet_name
        create_subnet_details.vcn_id = self.vcn_ocid
        create_subnet_details.cidr_block = subnet_cidr_block2

        result = virtual_network.create_subnet(create_subnet_details)
        util.validate_response(result, expect_etag=True)

        self.subnet_ocid2 = result.data.id
        oci.wait_until(virtual_network, virtual_network.get_subnet(self.subnet_ocid2), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        create_load_balancer_details = oci.load_balancer.models.CreateLoadBalancerDetails()
        create_load_balancer_details.compartment_id = util.COMPARTMENT_ID
        create_load_balancer_details.display_name = "My Load Balancer"
        create_load_balancer_details.shape_name = "100Mbps"
        create_load_balancer_details.subnet_ids = [self.subnet_ocid1, self.subnet_ocid2]

        response = load_balancer_client.create_load_balancer(create_load_balancer_details)
        util.validate_response(response)

        work_request_id = response.headers['opc-work-request-id']
        oci.wait_until(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        response = load_balancer_client.get_work_request(work_request_id)
        self.load_balancer_ocid = response.data.load_balancer_id

    @util.log_test
    def subtest_delete(self, load_balancer_client, virtual_network):
        error_count = 0

        if hasattr(self, 'load_balancer_ocid'):
            try:
                load_balancer_client.delete_load_balancer(self.load_balancer_ocid)
                oci.wait_until(load_balancer_client, load_balancer_client.get_load_balancer(self.load_balancer_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=300)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'subnet_ocid1'):
            try:
                virtual_network.delete_subnet(self.subnet_ocid1)
                oci.wait_until(virtual_network, virtual_network.get_subnet(self.subnet_ocid1), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'subnet_ocid2'):
            try:
                virtual_network.delete_subnet(self.subnet_ocid2)
                oci.wait_until(virtual_network, virtual_network.get_subnet(self.subnet_ocid2), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'vcn_ocid'):
            try:
                virtual_network.delete_vcn(self.vcn_ocid)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        assert error_count == 0
