# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

import oci
import pytest
import time
from . import util


class TestLoadBalancer:
    BACKEND_IP_ADDRESS = "129.213.241.184"
    BACKEND_PORT = 80

    def test_operations(self, load_balancer_client, virtual_network):
        try:
            self.subtest_basic_operations(load_balancer_client, virtual_network)
            self.subtest_health_check_operations(load_balancer_client, virtual_network)
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

        self.backend_set_name = 'BackSet-{}'.format(int(time.time()))
        backend_set_details = oci.load_balancer.models.BackendSetDetails()
        backend_set_details.policy = 'ROUND_ROBIN'
        backend_set_details.health_checker = oci.load_balancer.models.HealthCheckerDetails()
        backend_set_details.health_checker.protocol = 'HTTP'
        backend_set_details.health_checker.url_path = '/'
        backend_set_details.health_checker.port = 80
        backend_set_details.health_checker.retries = 1
        backend_set_details.health_checker.timeout_in_millis = 100
        backend_set_details.health_checker.interval_in_millis = 1000
        backend_set_details.session_persistence_configuration = oci.load_balancer.models.SessionPersistenceConfigurationDetails()
        backend_set_details.session_persistence_configuration.cookie_name = '*'
        backend_set_details.session_persistence_configuration.disable_fallback = False

        create_load_balancer_details = oci.load_balancer.models.CreateLoadBalancerDetails()
        create_load_balancer_details.compartment_id = util.COMPARTMENT_ID
        create_load_balancer_details.display_name = "My Load Balancer"
        create_load_balancer_details.shape_name = "100Mbps"
        create_load_balancer_details.subnet_ids = [self.subnet_ocid1, self.subnet_ocid2]
        create_load_balancer_details.backend_sets = {self.backend_set_name: backend_set_details}

        try:
            response = load_balancer_client.create_load_balancer(create_load_balancer_details)
        except oci.exceptions.ServiceError as e:
            if e.code == 'LimitExceeded':
                pytest.skip('Skipping tests as load balancer limits have been exceeded')
            else:
                raise
        util.validate_response(response)

        work_request_id = response.headers['opc-work-request-id']
        oci.wait_until(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

        response = load_balancer_client.get_work_request(work_request_id)
        self.load_balancer_ocid = response.data.load_balancer_id

        create_backend_details = oci.load_balancer.models.CreateBackendDetails()
        create_backend_details.ip_address = self.BACKEND_IP_ADDRESS
        create_backend_details.port = self.BACKEND_PORT
        create_backend_details.weight = 1
        create_backend_details.backup = False
        create_backend_details.drain = False
        create_backend_details.offline = False

        response = load_balancer_client.create_backend(create_backend_details, self.load_balancer_ocid, self.backend_set_name)
        work_request_id = response.headers['opc-work-request-id']
        oci.wait_until(load_balancer_client, load_balancer_client.get_work_request(work_request_id), 'lifecycle_state', 'SUCCEEDED', max_wait_seconds=300)

    # In this test we use a fake backend so the status we get back at each level of health check
    # is UNKNOWN since we can't check something which doesn't exist
    @util.log_test
    def subtest_health_check_operations(self, load_balancer_client, virtual_network):
        kwargs = {
            'load_balancer_id': self.load_balancer_ocid,
            'backend_set_name': self.backend_set_name,
            'backend_name': '{}:{}'.format(self.BACKEND_IP_ADDRESS, self.BACKEND_PORT)
        }

        backend_health_response = self.call_with_retries_on_not_found(load_balancer_client.get_backend_health, 30, 10, **kwargs)
        assert backend_health_response.data.health_check_results == []
        assert backend_health_response.data.status == 'UNKNOWN'

        kwargs.pop('backend_name')
        backend_set_health_response = self.call_with_retries_on_not_found(load_balancer_client.get_backend_set_health, 30, 10, **kwargs)
        assert backend_set_health_response.data.critical_state_backend_names == []
        assert backend_set_health_response.data.warning_state_backend_names == []
        assert backend_set_health_response.data.unknown_state_backend_names == ['{}:{}'.format(self.BACKEND_IP_ADDRESS, self.BACKEND_PORT)]
        assert backend_set_health_response.data.total_backend_count == 1
        assert backend_set_health_response.data.status == 'UNKNOWN'

        kwargs.pop('backend_set_name')
        load_balancer_health_response = self.call_with_retries_on_not_found(load_balancer_client.get_load_balancer_health, 30, 10, **kwargs)
        assert load_balancer_health_response.data.critical_state_backend_set_names == []
        assert load_balancer_health_response.data.warning_state_backend_set_names == []
        assert load_balancer_health_response.data.unknown_state_backend_set_names == [self.backend_set_name]
        assert load_balancer_health_response.data.total_backend_set_count == 1
        assert load_balancer_health_response.data.status == 'UNKNOWN'

        list_load_balancer_healths_response = load_balancer_client.list_load_balancer_healths(util.COMPARTMENT_ID)
        assert len(list_load_balancer_healths_response.data) >= 1

        found_lb = False
        for item in list_load_balancer_healths_response.data:
            if item.load_balancer_id == self.load_balancer_ocid:
                assert item.status == 'UNKNOWN'
                found_lb = True
                break
        assert found_lb

    @util.log_test
    def subtest_delete(self, load_balancer_client, virtual_network):
        error_count = 0

        if hasattr(self, 'load_balancer_ocid'):
            if hasattr(self, 'backend_set_name'):
                try:
                    load_balancer_client.delete_backend(
                        self.load_balancer_ocid,
                        self.backend_set_name,
                        '{}:{}'.format(self.BACKEND_IP_ADDRESS, self.BACKEND_PORT)
                    )
                except Exception as error:
                    if not hasattr(error, 'status') or error.status != 404:
                        util.print_latest_exception(error)
                        error_count = error_count + 1

                try:
                    load_balancer_client.delete_backend_set(self.load_balancer_ocid, self.backend_set_name)
                except Exception as error:
                    if not hasattr(error, 'status') or error.status != 404:
                        util.print_latest_exception(error)
                        error_count = error_count + 1

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

    def call_with_retries_on_not_found(self, function_ref, wait_secs, max_retries, **kwargs):
        tries = 0
        while tries < max_retries:
            try:
                return function_ref(**kwargs)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    raise
                else:
                    tries = tries + 1
                    time.sleep(wait_secs)
