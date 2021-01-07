# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from . import util
from .. import test_config_container
import oci


class TestVirtualNetwork:

    def test_all_operations(self, virtual_network):
        with test_config_container.create_vcr().use_cassette('test_virtual_network_all_operations.yml'):
            try:
                self.subtest_vcn_operations(virtual_network)
                self.subtest_security_list_operations(virtual_network)
                self.subtest_security_list_stateless_rules(virtual_network)
                self.subtest_subnet_operations(virtual_network)
                self.subtest_internet_gateway_operations(virtual_network)
                self.subtest_cpe_operations(virtual_network)
                self.subtest_dhcp_option_operations(virtual_network)
                self.subtest_drg_operations(virtual_network)
                self.subtest_drg_attachment_operations(virtual_network)
                self.subtest_ip_sec_connection_operations(virtual_network)
                self.subtest_route_table_operations(virtual_network)
            finally:
                test_config_container.vcr_sleep(20)
                self.subtest_delete(virtual_network)

    @util.log_test
    def subtest_vcn_operations(self, virtual_network):
        vcn_name = util.random_name('python_sdk_test_vcn')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        create_vcn_details = oci.core.models.CreateVcnDetails()
        create_vcn_details.cidr_block = cidr_block
        create_vcn_details.display_name = vcn_name
        create_vcn_details.compartment_id = util.COMPARTMENT_ID
        create_vcn_details.dns_label = vcn_dns_label

        result = virtual_network.create_vcn(create_vcn_details)
        self.vcn_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        test_config_container.do_wait(virtual_network, virtual_network.get_vcn(self.vcn_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        result = virtual_network.list_vcns(util.COMPARTMENT_ID)
        util.validate_response(result)

        vcn_name = vcn_name + "_updated"
        update_vcn_details = oci.core.models.UpdateVcnDetails()
        update_vcn_details.display_name = vcn_name
        result = virtual_network.update_vcn(self.vcn_ocid, update_vcn_details)
        util.validate_response(result, expect_etag=True)

        result = virtual_network.get_vcn(self.vcn_ocid)
        util.validate_response(result, expect_etag=True)

        assert result.data.display_name == vcn_name
        assert result.data.dns_label == vcn_dns_label

    @util.log_test
    def subtest_security_list_operations(self, virtual_network):
        sl_name = util.random_name('python_sdk_test_security_list')

        create_security_list_details = oci.core.models.CreateSecurityListDetails()
        create_security_list_details.display_name = sl_name
        create_security_list_details.compartment_id = util.COMPARTMENT_ID
        create_security_list_details.vcn_id = self.vcn_ocid

        create_security_list_details.egress_security_rules = [self.create_default_egress_security_rule()]
        create_security_list_details.ingress_security_rules = [self.create_default_ingress_security_rule()]

        result = virtual_network.create_security_list(create_security_list_details)
        self.sl_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        test_config_container.do_wait(virtual_network, virtual_network.get_security_list(self.sl_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        result = virtual_network.list_security_lists(util.COMPARTMENT_ID, vcn_id=self.vcn_ocid)
        util.validate_response(result)

        result = virtual_network.get_security_list(self.sl_ocid)
        util.validate_response(result, expect_etag=True)

        sl_name = sl_name + "_updated"
        egress_rule = self.create_default_egress_security_rule()
        egress_rule.destination = '10.0.4.0/24'

        ingress_rule = self.create_default_ingress_security_rule()
        ingress_rule.destination = '10.0.4.0/24'

        # Force update on all fields
        update_security_list_details = oci.core.models.UpdateSecurityListDetails()
        update_security_list_details.name = sl_name
        update_security_list_details.egress_security_rules = [egress_rule]
        update_security_list_details.ingress_security_rules = [ingress_rule]
        result = virtual_network.update_security_list(self.sl_ocid, update_security_list_details)
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_security_list_stateless_rules(self, virtual_network):
        stateless_egress_rule = self.create_default_egress_security_rule()
        stateless_egress_rule.is_stateless = True

        update_security_list_details = oci.core.models.UpdateSecurityListDetails()
        update_security_list_details.egress_security_rules = [stateless_egress_rule]
        result = virtual_network.update_security_list(self.sl_ocid, update_security_list_details)

        util.validate_response(result, expect_etag=True)
        assert result.data.egress_security_rules[0].is_stateless

        test_config_container.vcr_sleep(20)

        explicit_stateful_egress_rule = self.create_default_egress_security_rule()
        explicit_stateful_egress_rule.is_stateless = False
        update_security_list_details.egress_security_rules = [explicit_stateful_egress_rule]
        result = virtual_network.update_security_list(self.sl_ocid, update_security_list_details)
        util.validate_response(result, expect_etag=True)
        assert not result.data.egress_security_rules[0].is_stateless

        test_config_container.vcr_sleep(20)

        implicit_stateful_egress_rule = self.create_default_egress_security_rule()
        update_security_list_details.egress_security_rules = [implicit_stateful_egress_rule]
        result = virtual_network.update_security_list(self.sl_ocid, update_security_list_details)
        util.validate_response(result, expect_etag=True)
        assert not result.data.egress_security_rules[0].is_stateless

    @util.log_test
    def subtest_subnet_operations(self, virtual_network):
        subnet_name = util.random_name('python_sdk_test_subnet')
        cidr_block = "10.0.0.0/16"
        subnet_dns_label = util.random_name('subnet', insert_underscore=False)

        create_subnet_details = oci.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = util.COMPARTMENT_ID
        create_subnet_details.availability_domain = util.availability_domain()
        create_subnet_details.display_name = subnet_name
        create_subnet_details.vcn_id = self.vcn_ocid
        create_subnet_details.cidr_block = cidr_block
        create_subnet_details.security_list_ids = [self.sl_ocid]
        create_subnet_details.dns_label = subnet_dns_label

        result = virtual_network.create_subnet(create_subnet_details)
        self.subnet_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        test_config_container.do_wait(virtual_network, virtual_network.get_subnet(self.subnet_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        result = virtual_network.list_subnets(util.COMPARTMENT_ID, vcn_id=self.vcn_ocid)
        util.validate_response(result)

        subnet_name = subnet_name + "_updated"
        update_subnet_details = oci.core.models.UpdateSubnetDetails()
        update_subnet_details.display_name = subnet_name
        result = virtual_network.update_subnet(self.subnet_ocid, update_subnet_details)
        util.validate_response(result, expect_etag=True)

        result = virtual_network.get_subnet(self.subnet_ocid)
        util.validate_response(result, expect_etag=True)

        assert result.data.dns_label == subnet_dns_label

    @util.log_test
    def subtest_internet_gateway_operations(self, virtual_network):
        ig_name = util.random_name('python_sdk_test_ig')

        create_internet_gateway_details = oci.core.models.CreateInternetGatewayDetails()
        create_internet_gateway_details.compartment_id = util.COMPARTMENT_ID
        create_internet_gateway_details.is_enabled = False
        create_internet_gateway_details.display_name = ig_name
        create_internet_gateway_details.vcn_id = self.vcn_ocid
        result = virtual_network.create_internet_gateway(create_internet_gateway_details)
        self.ig_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        test_config_container.do_wait(virtual_network, virtual_network.get_internet_gateway(self.ig_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        result = virtual_network.list_internet_gateways(util.COMPARTMENT_ID, vcn_id=self.vcn_ocid)
        util.validate_response(result)

        ig_name = ig_name + "_updated"
        update_internet_gateway_details = oci.core.models.UpdateInternetGatewayDetails()
        update_internet_gateway_details.display_name = ig_name
        result = virtual_network.update_internet_gateway(self.ig_ocid, update_internet_gateway_details)
        util.validate_response(result, expect_etag=True)

        result = virtual_network.get_internet_gateway(self.ig_ocid)
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_cpe_operations(self, virtual_network):
        cpe_name = util.random_name('python_sdk_test_cpe')
        ip_address = "137.254.4.11"

        create_cpe_details = oci.core.models.CreateCpeDetails()
        create_cpe_details.compartment_id = util.COMPARTMENT_ID
        create_cpe_details.display_name = cpe_name
        create_cpe_details.ip_address = ip_address
        result = virtual_network.create_cpe(create_cpe_details)
        self.cpe_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        result = virtual_network.list_cpes(util.COMPARTMENT_ID)
        util.validate_response(result)

        cpe_name = cpe_name + "_updated"
        update_cpe_details = oci.core.models.UpdateCpeDetails()
        update_cpe_details.display_name = cpe_name
        result = virtual_network.update_cpe(self.cpe_ocid, update_cpe_details)
        util.validate_response(result, expect_etag=True)

        result = virtual_network.get_cpe(self.cpe_ocid)
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_dhcp_option_operations(self, virtual_network):
        dhcp_options_name = util.random_name('python_sdk_test_dhcp_options')

        create_dhcp_details = oci.core.models.CreateDhcpDetails()
        create_dhcp_details.compartment_id = util.COMPARTMENT_ID
        create_dhcp_details.vcn_id = self.vcn_ocid
        create_dhcp_details.display_name = dhcp_options_name

        dhcp_dns_option = oci.core.models.DhcpDnsOption()
        dhcp_dns_option.custom_dns_servers = ["202.44.61.9"]
        dhcp_dns_option.server_type = 'CustomDnsServer'

        dhcp_search_domain_option = oci.core.models.DhcpSearchDomainOption()
        dhcp_search_domain_option.search_domain_names = ["testvcn.oraclevcn.com"]

        create_dhcp_details.options = [dhcp_dns_option, dhcp_search_domain_option]

        result = virtual_network.create_dhcp_options(create_dhcp_details)
        util.validate_response(result, expect_etag=True)
        self.dhcp_options_ocid = result.data.id
        test_config_container.do_wait(virtual_network, virtual_network.get_dhcp_options(self.dhcp_options_ocid), 'lifecycle_state', 'AVAILABLE')

        result = virtual_network.list_dhcp_options(util.COMPARTMENT_ID, vcn_id=self.vcn_ocid)
        util.validate_response(result)

        result = virtual_network.get_dhcp_options(self.dhcp_options_ocid)
        util.validate_response(result, expect_etag=True)

        dhcp_options_name = dhcp_options_name + "_updated"

        update_dhcp_details = oci.core.models.UpdateDhcpDetails()
        update_dhcp_details.display_name = dhcp_options_name
        update_dhcp_details.options = [dhcp_dns_option, dhcp_search_domain_option]

        result = virtual_network.update_dhcp_options(self.dhcp_options_ocid, update_dhcp_details)

        util.validate_response(result, expect_etag=True)

        # validate response contains SearchDomain option
        response_has_search_domain_option = False
        for option in result.data.options:
            if option.type == "SearchDomain":
                response_has_search_domain_option = True
                assert option.search_domain_names[0] == "testvcn.oraclevcn.com"

        assert response_has_search_domain_option, "Options response should contain option of type 'SearchDomain'."

    @util.log_test
    def subtest_drg_operations(self, virtual_network):
        drg_name = util.random_name('python_sdk_test_drg')

        create_drg_details = oci.core.models.CreateDrgDetails()
        create_drg_details.compartment_id = util.COMPARTMENT_ID
        create_drg_details.display_name = drg_name

        try:
            result = virtual_network.create_drg(create_drg_details)
            self.drg_ocid = result.data.id
        except oci.exceptions.ServiceError as e:
            if e.code == 'LimitExceeded':
                print('Skipping subtest_drg_operations because of LimitExceeded')
                return
            else:
                raise

        util.validate_response(result, expect_etag=True)
        test_config_container.do_wait(virtual_network, virtual_network.get_drg(self.drg_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=600)

        result = virtual_network.list_drgs(util.COMPARTMENT_ID)
        util.validate_response(result)

        drg_name = drg_name + "_updated"
        update_drg_details = oci.core.models.UpdateDrgDetails()
        update_drg_details.display_name = drg_name
        result = virtual_network.update_drg(self.drg_ocid, update_drg_details)
        util.validate_response(result, expect_etag=True)

        result = virtual_network.get_drg(self.drg_ocid)
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_drg_attachment_operations(self, virtual_network):
        if not hasattr(self, 'drg_ocid'):
            print('Skipping subtest_drg_attachment_operations because of LimitExceeded')
            return

        drg_attachment_name = util.random_name('python_sdk_test_drg_attachment')

        create_drg_attachment_details = oci.core.models.CreateDrgAttachmentDetails()
        create_drg_attachment_details.drg_id = self.drg_ocid
        create_drg_attachment_details.vcn_id = self.vcn_ocid
        create_drg_attachment_details.display_name = drg_attachment_name
        result = virtual_network.create_drg_attachment(create_drg_attachment_details)
        self.drg_attachment_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        test_config_container.do_wait(virtual_network, virtual_network.get_drg_attachment(self.drg_attachment_ocid), 'lifecycle_state', 'ATTACHED')

        result = virtual_network.list_drg_attachments(util.COMPARTMENT_ID)
        util.validate_response(result)

        drg_attachment_name = drg_attachment_name + "_updated"
        update_drg_attachment_details = oci.core.models.UpdateDrgAttachmentDetails()
        update_drg_attachment_details.display_name = drg_attachment_name
        result = virtual_network.update_drg_attachment(self.drg_attachment_ocid, update_drg_attachment_details)
        util.validate_response(result, expect_etag=True)

        result = virtual_network.get_drg_attachment(self.drg_attachment_ocid)
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_ip_sec_connection_operations(self, virtual_network):
        if not hasattr(self, 'drg_ocid'):
            print('Skipping subtest_ip_sec_connection_operations because of LimitExceeded')
            return

        ipsc_name = util.random_name('python_sdk_test_ipsc')

        create_ip_sec_details = oci.core.models.CreateIPSecConnectionDetails()
        create_ip_sec_details.compartment_id = util.COMPARTMENT_ID
        create_ip_sec_details.display_name = ipsc_name
        create_ip_sec_details.cpe_id = self.cpe_ocid
        create_ip_sec_details.drg_id = self.drg_ocid
        create_ip_sec_details.static_routes = ['10.0.0.0/16']
        result = virtual_network.create_ip_sec_connection(create_ip_sec_details)
        self.ipsc_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        test_config_container.do_wait(virtual_network, virtual_network.get_ip_sec_connection(self.ipsc_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=600)

        result = virtual_network.list_route_tables(util.COMPARTMENT_ID, vcn_id=self.vcn_ocid)
        util.validate_response(result)

        ipsc_name = ipsc_name + "_updated"
        update_ip_sec_connection_details = oci.core.models.UpdateIPSecConnectionDetails()
        update_ip_sec_connection_details.display_name = ipsc_name
        result = virtual_network.update_ip_sec_connection(self.ipsc_ocid, update_ip_sec_connection_details)
        util.validate_response(result, expect_etag=True)

        result = virtual_network.get_ip_sec_connection(self.ipsc_ocid)
        util.validate_response(result, expect_etag=True)

        result = virtual_network.get_ip_sec_connection_device_config(self.ipsc_ocid)
        util.validate_response(result)

        result = virtual_network.get_ip_sec_connection_device_status(self.ipsc_ocid)
        util.validate_response(result)

    @util.log_test
    def subtest_route_table_operations(self, virtual_network):
        rt_name = util.random_name('python_sdk_test_route_table')

        create_route_table_details = oci.core.models.CreateRouteTableDetails()
        create_route_table_details.compartment_id = util.COMPARTMENT_ID
        create_route_table_details.display_name = rt_name
        create_route_table_details.vcn_id = self.vcn_ocid

        route_rule = oci.core.models.RouteRule()
        route_rule.cidr_block = None
        route_rule.destination = '0.0.0.0/0'
        route_rule.destination_type = 'CIDR_BLOCK'
        route_rule.network_entity_id = self.ig_ocid

        create_route_table_details.route_rules = [route_rule]
        result = virtual_network.create_route_table(create_route_table_details)
        self.rt_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        test_config_container.do_wait(virtual_network, virtual_network.get_route_table(self.rt_ocid), 'lifecycle_state', 'AVAILABLE', max_wait_seconds=300)

        result = virtual_network.list_route_tables(util.COMPARTMENT_ID, vcn_id=self.vcn_ocid)
        util.validate_response(result)

        result = virtual_network.get_route_table(self.rt_ocid)
        util.validate_response(result, expect_etag=True)

        rt_name = rt_name + "_updated"
        update_route_table_details = oci.core.models.UpdateRouteTableDetails()
        update_route_table_details.display_name = rt_name

        updated_route_rule = oci.core.models.RouteRule()
        updated_route_rule.cidr_block = None
        updated_route_rule.destination = '0.0.0.0/1'
        updated_route_rule.destination_type = 'CIDR_BLOCK'
        updated_route_rule.network_entity_id = self.ig_ocid
        update_route_table_details.route_rules = [updated_route_rule]

        # update route-rules, force
        result = virtual_network.update_route_table(self.rt_ocid, update_route_table_details)
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_delete(self, virtual_network):
        error_count = 0

        if hasattr(self, 'rt_ocid'):
            try:
                virtual_network.delete_route_table(self.rt_ocid)
                test_config_container.do_wait(virtual_network, virtual_network.get_route_table(self.rt_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=300)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'ipsc_ocid'):
            try:
                virtual_network.delete_ip_sec_connection(self.ipsc_ocid)
                test_config_container.do_wait(virtual_network, virtual_network.get_ip_sec_connection(self.ipsc_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=300)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'drg_attachment_ocid'):
            try:
                virtual_network.delete_drg_attachment(self.drg_attachment_ocid)
                test_config_container.do_wait(virtual_network, virtual_network.get_drg_attachment(self.drg_attachment_ocid), 'lifecycle_state', 'DETACHED', max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'drg_ocid'):
            try:
                virtual_network.delete_drg(self.drg_ocid)
                test_config_container.do_wait(virtual_network, virtual_network.get_drg(self.drg_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'dhcp_options_ocid'):
            try:
                virtual_network.delete_dhcp_options(self.dhcp_options_ocid)
                test_config_container.do_wait(virtual_network, virtual_network.get_dhcp_options(self.dhcp_options_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'cpe_ocid'):
            try:
                result = virtual_network.delete_cpe(self.cpe_ocid)
                assert result.status == 204
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'ig_ocid'):
            try:
                virtual_network.delete_internet_gateway(self.ig_ocid)
                test_config_container.do_wait(virtual_network, virtual_network.get_internet_gateway(self.ig_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'subnet_ocid'):
            try:
                virtual_network.delete_subnet(self.subnet_ocid)
                test_config_container.do_wait(virtual_network, virtual_network.get_subnet(self.subnet_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'sl_ocid'):
            try:
                virtual_network.delete_security_list(self.sl_ocid)
                test_config_container.do_wait(virtual_network, virtual_network.get_security_list(self.sl_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=300)
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

    def test_reserved_public_ip_operations(self, virtual_network, compute):
        with test_config_container.create_vcr().use_cassette('test_virtual_network_reserved_public_ip.yml'):
            public_ip_id = None
            vcn_and_subnet = None
            instance = None
            try:
                create_public_ip_response = virtual_network.create_public_ip(
                    oci.core.models.CreatePublicIpDetails(
                        compartment_id=util.COMPARTMENT_ID,
                        display_name=util.random_name('reserved_pub_ip'),
                        lifetime='RESERVED'
                    )
                )
                assert create_public_ip_response.request_id
                assert create_public_ip_response.headers.get('etag')

                public_ip = self.get_and_list_public_ip(virtual_network, create_public_ip_response.data)
                public_ip_id = public_ip.id

                vcn_and_subnet = self.create_vcn_with_one_subnet(virtual_network)
                instance = self.launch_instance(compute, vcn_and_subnet)

                vnic_attachments = compute.list_vnic_attachments(util.COMPARTMENT_ID, instance_id=instance.id).data
                vnic_id = vnic_attachments[0].vnic_id
                private_ip_id = virtual_network.list_private_ips(vnic_id=vnic_id).data[0].id

                self.update_public_ip(virtual_network, public_ip, private_ip_id)
                self.update_public_ip(virtual_network, public_ip, '')
            finally:
                if public_ip_id:
                    try:
                        public_ip_response = virtual_network.get_public_ip(public_ip.id)
                        virtual_network.delete_public_ip(public_ip.id)
                        test_config_container.do_wait(
                            virtual_network,
                            public_ip_response,
                            'lifecycle_state',
                            'TERMINATED',
                            succeed_on_not_found=True
                        )
                    except Exception as e:
                        print('Could not delete public IP {}. Error: {}'.format(public_ip_id, e))

                if instance:
                    try:
                        compute.terminate_instance(instance.id)
                        test_config_container.do_wait(
                            compute,
                            compute.get_instance(instance.id),
                            'lifecycle_state',
                            'TERMINATED',
                            max_wait_seconds=600,
                            succeed_on_not_found=True
                        )
                    except Exception as e:
                        print('Could not delete instance {}. Error: {}'.format(instance, e))

                if vcn_and_subnet:
                    try:
                        self.delete_vcn_and_subnet(virtual_network, vcn_and_subnet)
                    except Exception as e:
                        print('Could not delete VCN and subnet {}. Error: {}'.format(vcn_and_subnet, e))

    def test_ephemeral_public_ip_operations(self, virtual_network, compute):
        with test_config_container.create_vcr().use_cassette('test_virtual_network_ephemeral_public_ip.yml'):
            public_ip_id = None
            vcn_and_subnet = None
            instance = None
            try:
                vcn_and_subnet = self.create_vcn_with_one_subnet(virtual_network)
                instance = self.launch_instance(compute, vcn_and_subnet)

                vnic_attachments = compute.list_vnic_attachments(util.COMPARTMENT_ID, instance_id=instance.id).data
                vnic_id = vnic_attachments[0].vnic_id
                private_ip_id = virtual_network.list_private_ips(vnic_id=vnic_id).data[0].id

                create_public_ip_response = virtual_network.create_public_ip(
                    oci.core.models.CreatePublicIpDetails(
                        compartment_id=util.COMPARTMENT_ID,
                        display_name=util.random_name('reserved_pub_ip'),
                        lifetime='EPHEMERAL',
                        private_ip_id=private_ip_id
                    )
                )
                assert create_public_ip_response.request_id
                assert create_public_ip_response.headers.get('etag')

                public_ip = self.get_and_list_public_ip(virtual_network, create_public_ip_response.data)
                public_ip_id = public_ip.id
                assert public_ip.private_ip_id == private_ip_id
                assert public_ip.availability_domain == util.availability_domain()

                try:
                    compute.terminate_instance(instance.id)
                    test_config_container.do_wait(
                        compute,
                        compute.get_instance(instance.id),
                        'lifecycle_state',
                        'TERMINATED',
                        max_wait_seconds=600,
                        succeed_on_not_found=True
                    )
                except Exception as e:
                    print('Could not delete instance {}. Error: {}'.format(instance, e))
            finally:
                if public_ip_id:
                    public_ip_response = None
                    try:
                        public_ip_response = virtual_network.get_public_ip(public_ip.id)
                    except Exception as e:
                        if e.status != 404:
                            raise e
                    if public_ip_response:
                        try:
                            test_config_container.do_wait(
                                virtual_network,
                                public_ip_response,
                                'lifecycle_state',
                                'TERMINATED',
                                succeed_on_not_found=True
                            )
                        except Exception as e:
                            print('Could not wait until public IP {} deleted. Error: {}'.format(public_ip_id, e))

                if vcn_and_subnet:
                    try:
                        self.delete_vcn_and_subnet(virtual_network, vcn_and_subnet)
                    except Exception as e:
                        print('Could not delete VCN and subnet {}. Error: {}'.format(vcn_and_subnet, e))

    def get_and_list_public_ip(self, virtual_network, created_public_ip):
        get_public_ip_response = test_config_container.do_wait(
            virtual_network,
            virtual_network.get_public_ip(created_public_ip.id),
            evaluate_response=lambda r: r.data.lifecycle_state in ['AVAILABLE', 'ASSIGNED']
        )
        public_ip = get_public_ip_response.data
        assert public_ip.id
        assert public_ip.display_name == created_public_ip.display_name
        assert public_ip.time_created
        assert public_ip.ip_address
        if created_public_ip.lifetime == 'RESERVED':
            assert public_ip.scope == 'REGION'
        else:
            assert public_ip.scope == 'AVAILABILITY_DOMAIN'

        all_region_scoped_public_ips = oci.pagination.list_call_get_all_results(
            virtual_network.list_public_ips,
            'REGION',
            util.COMPARTMENT_ID
        )
        if created_public_ip.lifetime == 'RESERVED':
            assert len(all_region_scoped_public_ips.data) > 0
        found_public_ip = False
        for pi in all_region_scoped_public_ips.data:
            if pi.id == public_ip.id:
                found_public_ip = True
                break
        if created_public_ip.lifetime == 'RESERVED':
            assert found_public_ip
        else:
            assert not found_public_ip

        all_ad_scoped_public_ips = oci.pagination.list_call_get_all_results(
            virtual_network.list_public_ips,
            'AVAILABILITY_DOMAIN',
            util.COMPARTMENT_ID,
            availability_domain=util.availability_domain()
        )
        if created_public_ip.lifetime == 'EPHEMERAL':
            assert len(all_ad_scoped_public_ips.data) > 0
        found_public_ip = False
        for pi in all_ad_scoped_public_ips.data:
            if pi.id == public_ip.id:
                found_public_ip = True
                break
        if created_public_ip.lifetime == 'EPHEMERAL':
            assert found_public_ip
        else:
            assert not found_public_ip

        return public_ip

    def update_public_ip(self, virtual_network, public_ip, private_ip_id):
        update_response = virtual_network.update_public_ip(
            public_ip.id,
            oci.core.models.UpdatePublicIpDetails(
                private_ip_id=private_ip_id,
                display_name='updated_pub_ip'
            )
        )
        assert update_response.request_id
        assert update_response.headers.get('etag')
        assert 'updated_pub_ip' == update_response.data.display_name

        if private_ip_id == '':
            public_ip_response = virtual_network.get_public_ip(public_ip.id)
            test_config_container.do_wait(
                virtual_network,
                public_ip_response,
                evaluate_response=lambda r: r.data.lifecycle_state in ['AVAILABLE', 'UNASSIGNED']
            )
        else:
            assert private_ip_id == update_response.data.private_ip_id
            public_ip_response = virtual_network.get_public_ip(public_ip.id)
            test_config_container.do_wait(
                virtual_network,
                public_ip_response,
                evaluate_response=lambda r: r.data.lifecycle_state in ['AVAILABLE', 'ASSIGNED']
            )

    def create_default_egress_security_rule(self):
        port_range = oci.core.models.PortRange()
        port_range.min = 1522
        port_range.max = 1522

        tcp_options = oci.core.models.TcpOptions()
        tcp_options.destination_port_range = port_range

        egress_rule = oci.core.models.EgressSecurityRule()
        egress_rule.destination = '10.0.2.0/24'
        egress_rule.source = '10.0.2.0/24'
        egress_rule.protocol = '6'
        egress_rule.tcp_options = tcp_options

        return egress_rule

    def create_default_ingress_security_rule(self):
        port_range = oci.core.models.PortRange()
        port_range.min = 1522
        port_range.max = 1522

        tcp_options = oci.core.models.TcpOptions()
        tcp_options.destination_port_range = port_range

        ingress_rule = oci.core.models.IngressSecurityRule()
        ingress_rule.destination = '10.0.2.0/24'
        ingress_rule.source = '10.0.2.0/24'
        ingress_rule.protocol = '6'
        ingress_rule.tcp_options = tcp_options

        return ingress_rule

    def create_vcn_with_one_subnet(self, virtual_network):
        vcn_name = util.random_name('python_sdk_test_vcn')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        create_vcn_details = oci.core.models.CreateVcnDetails()
        create_vcn_details.cidr_block = cidr_block
        create_vcn_details.display_name = vcn_name
        create_vcn_details.compartment_id = util.COMPARTMENT_ID
        create_vcn_details.dns_label = vcn_dns_label

        result = virtual_network.create_vcn(create_vcn_details)
        vcn_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        vcn = test_config_container.do_wait(
            virtual_network,
            virtual_network.get_vcn(vcn_ocid),
            'lifecycle_state',
            'AVAILABLE',
            max_wait_seconds=300
        ).data

        subnet_name = util.random_name('python_sdk_test_compute_subnet')

        create_subnet_details = oci.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = util.COMPARTMENT_ID
        create_subnet_details.availability_domain = util.availability_domain()
        create_subnet_details.display_name = subnet_name
        create_subnet_details.vcn_id = vcn_ocid
        create_subnet_details.cidr_block = cidr_block

        result = virtual_network.create_subnet(create_subnet_details)
        util.validate_response(result, expect_etag=True)

        subnet_ocid = result.data.id
        subnet = test_config_container.do_wait(
            virtual_network,
            virtual_network.get_subnet(subnet_ocid),
            'lifecycle_state',
            'AVAILABLE',
            max_wait_seconds=300
        ).data

        return {'vcn': vcn, 'subnet': subnet}

    def delete_vcn_and_subnet(self, virtual_network, vcn_and_subnet):
        subnet_ocid = vcn_and_subnet['subnet'].id
        subnet_response = virtual_network.get_subnet(subnet_ocid)
        virtual_network.delete_subnet(subnet_ocid)
        test_config_container.do_wait(
            virtual_network,
            subnet_response,
            'lifecycle_state',
            'TERMINATED',
            max_wait_seconds=600,
            succeed_on_not_found=True
        )

        vcn_ocid = vcn_and_subnet['vcn'].id
        vcn_response = virtual_network.get_vcn(vcn_ocid)
        virtual_network.delete_vcn(vcn_ocid)
        test_config_container.do_wait(
            virtual_network,
            vcn_response,
            'lifecycle_state',
            'TERMINATED',
            max_wait_seconds=600,
            succeed_on_not_found=True
        )

    def launch_instance(self, compute, vcn_and_subnet):
        instance_name = util.random_name('python_sdk_test_instance')
        image_id = util.oracle_linux_image()
        shape = 'VM.Standard1.1'

        create_instance_details = oci.core.models.LaunchInstanceDetails()
        create_instance_details.compartment_id = util.COMPARTMENT_ID
        create_instance_details.availability_domain = util.availability_domain()
        create_instance_details.display_name = instance_name
        create_instance_details.create_vnic_details = oci.core.models.CreateVnicDetails(
            subnet_id=vcn_and_subnet['subnet'].id,
            assign_public_ip=False
        )
        create_instance_details.image_id = image_id
        create_instance_details.shape = shape

        result = compute.launch_instance(create_instance_details)
        instance_ocid = result.data.id

        get_instance_response = test_config_container.do_wait(
            compute,
            compute.get_instance(instance_ocid),
            'lifecycle_state',
            'RUNNING',
            max_wait_seconds=600
        )

        return get_instance_response.data
