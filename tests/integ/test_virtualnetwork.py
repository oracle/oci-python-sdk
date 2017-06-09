# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

import time
from . import util
import oraclebmc


class TestVirtualNetwork:

    def test_all_operations(self, virtual_network):
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
            time.sleep(20)
            self.subtest_delete(virtual_network)

    @util.log_test
    def subtest_vcn_operations(self, virtual_network):
        vcn_name = util.random_name('python_sdk_test_vcn')
        cidr_block = "10.0.0.0/16"
        vcn_dns_label = util.random_name('vcn', insert_underscore=False)

        create_vcn_details = oraclebmc.core.models.CreateVcnDetails()
        create_vcn_details.cidr_block = cidr_block
        create_vcn_details.display_name = vcn_name
        create_vcn_details.compartment_id = util.COMPARTMENT_ID
        create_vcn_details.dns_label = vcn_dns_label

        result = virtual_network.create_vcn(create_vcn_details)
        self.vcn_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        oraclebmc.wait_until(virtual_network, virtual_network.get_vcn(self.vcn_ocid), 'lifecycle_state',
                             'AVAILABLE', max_wait_seconds=300)

        result = virtual_network.list_vcns(util.COMPARTMENT_ID)
        util.validate_response(result)

        vcn_name = vcn_name + "_updated"
        update_vcn_details = oraclebmc.core.models.UpdateVcnDetails()
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

        create_security_list_details = oraclebmc.core.models.CreateSecurityListDetails()
        create_security_list_details.display_name = sl_name
        create_security_list_details.compartment_id = util.COMPARTMENT_ID
        create_security_list_details.vcn_id = self.vcn_ocid

        create_security_list_details.egress_security_rules = [self.create_default_egress_security_rule()]
        create_security_list_details.ingress_security_rules = [self.create_default_ingress_security_rule()]

        result = virtual_network.create_security_list(create_security_list_details)
        self.sl_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        oraclebmc.wait_until(virtual_network, virtual_network.get_security_list(self.sl_ocid), 'lifecycle_state',
                             'AVAILABLE', max_wait_seconds=300)

        result = virtual_network.list_security_lists(util.COMPARTMENT_ID, self.vcn_ocid)
        util.validate_response(result)

        result = virtual_network.get_security_list(self.sl_ocid)
        util.validate_response(result, expect_etag=True)

        sl_name = sl_name + "_updated"
        egress_rule = self.create_default_egress_security_rule()
        egress_rule.destination = '10.0.4.0/24'

        ingress_rule = self.create_default_ingress_security_rule()
        ingress_rule.destination = '10.0.4.0/24'

        # Force update on all fields
        update_security_list_details = oraclebmc.core.models.UpdateSecurityListDetails()
        update_security_list_details.name = sl_name
        update_security_list_details.egress_security_rules = [egress_rule]
        update_security_list_details.ingress_security_rules = [ingress_rule]
        result = virtual_network.update_security_list(self.sl_ocid, update_security_list_details)
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_security_list_stateless_rules(self, virtual_network):
        stateless_egress_rule = self.create_default_egress_security_rule()
        stateless_egress_rule.is_stateless = True

        update_security_list_details = oraclebmc.core.models.UpdateSecurityListDetails()
        update_security_list_details.egress_security_rules = [stateless_egress_rule]
        result = virtual_network.update_security_list(self.sl_ocid, update_security_list_details)

        util.validate_response(result, expect_etag=True)
        assert result.data.egress_security_rules[0].is_stateless

        time.sleep(20)

        explicit_stateful_egress_rule = self.create_default_egress_security_rule()
        explicit_stateful_egress_rule.is_stateless = False
        update_security_list_details.egress_security_rules = [explicit_stateful_egress_rule]
        result = virtual_network.update_security_list(self.sl_ocid, update_security_list_details)
        util.validate_response(result, expect_etag=True)
        assert not result.data.egress_security_rules[0].is_stateless

        time.sleep(20)

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

        create_subnet_details = oraclebmc.core.models.CreateSubnetDetails()
        create_subnet_details.compartment_id = util.COMPARTMENT_ID
        create_subnet_details.availability_domain = util.AVAILABILITY_DOMAIN
        create_subnet_details.display_name = subnet_name
        create_subnet_details.vcn_id = self.vcn_ocid
        create_subnet_details.cidr_block = cidr_block
        create_subnet_details.security_list_ids = [self.sl_ocid]
        create_subnet_details.dns_label = subnet_dns_label

        result = virtual_network.create_subnet(create_subnet_details)
        self.subnet_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        oraclebmc.wait_until(virtual_network, virtual_network.get_subnet(self.subnet_ocid), 'lifecycle_state',
                             'AVAILABLE', max_wait_seconds=300)

        result = virtual_network.list_subnets(util.COMPARTMENT_ID, self.vcn_ocid)
        util.validate_response(result)

        subnet_name = subnet_name + "_updated"
        update_subnet_details = oraclebmc.core.models.UpdateSubnetDetails()
        update_subnet_details.display_name = subnet_name
        result = virtual_network.update_subnet(self.subnet_ocid, update_subnet_details)
        util.validate_response(result, expect_etag=True)

        result = virtual_network.get_subnet(self.subnet_ocid)
        util.validate_response(result, expect_etag=True)

        assert result.data.dns_label == subnet_dns_label

    @util.log_test
    def subtest_internet_gateway_operations(self, virtual_network):
        ig_name = util.random_name('python_sdk_test_ig')

        create_internet_gateway_details = oraclebmc.core.models.CreateInternetGatewayDetails()
        create_internet_gateway_details.compartment_id = util.COMPARTMENT_ID
        create_internet_gateway_details.is_enabled = False
        create_internet_gateway_details.display_name = ig_name
        create_internet_gateway_details.vcn_id = self.vcn_ocid
        result = virtual_network.create_internet_gateway(create_internet_gateway_details)
        self.ig_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        oraclebmc.wait_until(virtual_network, virtual_network.get_internet_gateway(self.ig_ocid), 'lifecycle_state',
                             'AVAILABLE', max_wait_seconds=300)

        result = virtual_network.list_internet_gateways(util.COMPARTMENT_ID, self.vcn_ocid)
        util.validate_response(result)

        ig_name = ig_name + "_updated"
        update_internet_gateway_details = oraclebmc.core.models.UpdateInternetGatewayDetails()
        update_internet_gateway_details.display_name = ig_name
        result = virtual_network.update_internet_gateway(self.ig_ocid, update_internet_gateway_details)
        util.validate_response(result, expect_etag=True)

        result = virtual_network.get_internet_gateway(self.ig_ocid)
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_cpe_operations(self, virtual_network):
        cpe_name = util.random_name('python_sdk_test_cpe')
        ip_address = "137.254.4.11"

        create_cpe_details = oraclebmc.core.models.CreateCpeDetails()
        create_cpe_details.compartment_id = util.COMPARTMENT_ID
        create_cpe_details.display_name = cpe_name
        create_cpe_details.ip_address = ip_address
        result = virtual_network.create_cpe(create_cpe_details)
        self.cpe_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        result = virtual_network.list_cpes(util.COMPARTMENT_ID)
        util.validate_response(result)

        cpe_name = cpe_name + "_updated"
        update_cpe_details = oraclebmc.core.models.UpdateCpeDetails()
        update_cpe_details.display_name = cpe_name
        result = virtual_network.update_cpe(self.cpe_ocid, update_cpe_details)
        util.validate_response(result, expect_etag=True)

        result = virtual_network.get_cpe(self.cpe_ocid)
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_dhcp_option_operations(self, virtual_network):
        dhcp_options_name = util.random_name('python_sdk_test_dhcp_options')

        create_dhcp_details = oraclebmc.core.models.CreateDhcpDetails()
        create_dhcp_details.compartment_id = util.COMPARTMENT_ID
        create_dhcp_details.vcn_id = self.vcn_ocid
        create_dhcp_details.display_name = dhcp_options_name

        dhcp_dns_option = oraclebmc.core.models.DhcpDnsOption()
        dhcp_dns_option.custom_dns_servers = ["202.44.61.9"]
        dhcp_dns_option.server_type = 'CustomDnsServer'

        dhcp_search_domain_option = oraclebmc.core.models.DhcpSearchDomainOption()
        dhcp_search_domain_option.search_domain_names = ["testvcn.oraclevcn.com"]

        create_dhcp_details.options = [dhcp_dns_option, dhcp_search_domain_option]

        result = virtual_network.create_dhcp_options(create_dhcp_details)
        util.validate_response(result, expect_etag=True)
        self.dhcp_options_ocid = result.data.id
        oraclebmc.wait_until(virtual_network, virtual_network.get_dhcp_options(self.dhcp_options_ocid),
                             'lifecycle_state', 'AVAILABLE')

        result = virtual_network.list_dhcp_options(util.COMPARTMENT_ID, self.vcn_ocid)
        util.validate_response(result)

        result = virtual_network.get_dhcp_options(self.dhcp_options_ocid)
        util.validate_response(result, expect_etag=True)

        dhcp_options_name = dhcp_options_name + "_updated"

        update_dhcp_details = oraclebmc.core.models.UpdateDhcpDetails()
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

        create_drg_details = oraclebmc.core.models.CreateDrgDetails()
        create_drg_details.compartment_id = util.COMPARTMENT_ID
        create_drg_details.display_name = drg_name
        result = virtual_network.create_drg(create_drg_details)
        self.drg_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        oraclebmc.wait_until(virtual_network, virtual_network.get_drg(self.drg_ocid), 'lifecycle_state',
                             'AVAILABLE', max_wait_seconds=600)

        result = virtual_network.list_drgs(util.COMPARTMENT_ID)
        util.validate_response(result)

        drg_name = drg_name + "_updated"
        update_drg_details = oraclebmc.core.models.UpdateDrgDetails()
        update_drg_details.display_name = drg_name
        result = virtual_network.update_drg(self.drg_ocid, update_drg_details)
        util.validate_response(result, expect_etag=True)

        result = virtual_network.get_drg(self.drg_ocid)
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_drg_attachment_operations(self, virtual_network):
        drg_attachment_name = util.random_name('python_sdk_test_drg_attachment')

        create_drg_attachment_details = oraclebmc.core.models.CreateDrgAttachmentDetails()
        create_drg_attachment_details.drg_id = self.drg_ocid
        create_drg_attachment_details.vcn_id = self.vcn_ocid
        create_drg_attachment_details.display_name = drg_attachment_name
        result = virtual_network.create_drg_attachment(create_drg_attachment_details)
        self.drg_attachment_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        oraclebmc.wait_until(virtual_network, virtual_network.get_drg_attachment(self.drg_attachment_ocid),
                             'lifecycle_state', 'ATTACHED')

        result = virtual_network.list_drg_attachments(util.COMPARTMENT_ID)
        util.validate_response(result)

        drg_attachment_name = drg_attachment_name + "_updated"
        update_drg_attachment_details = oraclebmc.core.models.UpdateDrgAttachmentDetails()
        update_drg_attachment_details.display_name = drg_attachment_name
        result = virtual_network.update_drg_attachment(self.drg_attachment_ocid, update_drg_attachment_details)
        util.validate_response(result, expect_etag=True)

        result = virtual_network.get_drg_attachment(self.drg_attachment_ocid)
        util.validate_response(result, expect_etag=True)

    @util.log_test
    def subtest_ip_sec_connection_operations(self, virtual_network):
        ipsc_name = util.random_name('python_sdk_test_ipsc')

        create_ip_sec_details = oraclebmc.core.models.CreateIPSecConnectionDetails()
        create_ip_sec_details.compartment_id = util.COMPARTMENT_ID
        create_ip_sec_details.display_name = ipsc_name
        create_ip_sec_details.cpe_id = self.cpe_ocid
        create_ip_sec_details.drg_id = self.drg_ocid
        create_ip_sec_details.static_routes = ['10.0.0.0/16']
        result = virtual_network.create_ip_sec_connection(create_ip_sec_details)
        self.ipsc_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        oraclebmc.wait_until(virtual_network, virtual_network.get_ip_sec_connection(self.ipsc_ocid), 'lifecycle_state',
                             'AVAILABLE', max_wait_seconds=600)

        result = virtual_network.list_route_tables(util.COMPARTMENT_ID, self.vcn_ocid)
        util.validate_response(result)

        ipsc_name = ipsc_name + "_updated"
        update_ip_sec_connection_details = oraclebmc.core.models.UpdateIPSecConnectionDetails()
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

        create_route_table_details = oraclebmc.core.models.CreateRouteTableDetails()
        create_route_table_details.compartment_id = util.COMPARTMENT_ID
        create_route_table_details.display_name = rt_name
        create_route_table_details.vcn_id = self.vcn_ocid

        route_rule = oraclebmc.core.models.RouteRule()
        route_rule.cidr_block = '0.0.0.0/0'
        route_rule.network_entity_id = self.ig_ocid

        create_route_table_details.route_rules = [route_rule]
        result = virtual_network.create_route_table(create_route_table_details)
        self.rt_ocid = result.data.id
        util.validate_response(result, expect_etag=True)

        oraclebmc.wait_until(virtual_network, virtual_network.get_route_table(self.rt_ocid), 'lifecycle_state',
                             'AVAILABLE', max_wait_seconds=300)

        result = virtual_network.list_route_tables(util.COMPARTMENT_ID, self.vcn_ocid)
        util.validate_response(result)

        result = virtual_network.get_route_table(self.rt_ocid)
        util.validate_response(result, expect_etag=True)

        rt_name = rt_name + "_updated"
        update_route_table_details = oraclebmc.core.models.UpdateRouteTableDetails()
        update_route_table_details.display_name = rt_name

        updated_route_rule = oraclebmc.core.models.RouteRule()
        updated_route_rule.cidr_block = '0.0.0.0/1'
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
                oraclebmc.wait_until(virtual_network, virtual_network.get_route_table(self.rt_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=300)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'ipsc_ocid'):
            try:
                virtual_network.delete_ip_sec_connection(self.ipsc_ocid)
                oraclebmc.wait_until(virtual_network, virtual_network.get_ip_sec_connection(self.ipsc_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=300)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'drg_attachment_ocid'):
            try:
                virtual_network.delete_drg_attachment(self.drg_attachment_ocid)
                oraclebmc.wait_until(virtual_network, virtual_network.get_drg_attachment(self.drg_attachment_ocid), 'lifecycle_state', 'DETACHED', max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'drg_ocid'):
            try:
                virtual_network.delete_drg(self.drg_ocid)
                oraclebmc.wait_until(virtual_network, virtual_network.get_drg(self.drg_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'dhcp_options_ocid'):
            try:
                virtual_network.delete_dhcp_options(self.dhcp_options_ocid)
                oraclebmc.wait_until(virtual_network, virtual_network.get_dhcp_options(self.dhcp_options_ocid), 'lifecycle_state', 'TERMINATED', max_wait_seconds=600)
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
                oraclebmc.wait_until(virtual_network,
                                     virtual_network.get_internet_gateway(self.ig_ocid),
                                     'lifecycle_state',
                                     'TERMINATED',
                                     max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'subnet_ocid'):
            try:
                virtual_network.delete_subnet(self.subnet_ocid)
                oraclebmc.wait_until(virtual_network,
                                     virtual_network.get_subnet(self.subnet_ocid),
                                     'lifecycle_state',
                                     'TERMINATED',
                                     max_wait_seconds=600)
            except Exception as error:
                if not hasattr(error, 'status') or error.status != 404:
                    util.print_latest_exception(error)
                    error_count = error_count + 1

        if hasattr(self, 'sl_ocid'):
            try:
                virtual_network.delete_security_list(self.sl_ocid)
                oraclebmc.wait_until(virtual_network, virtual_network.get_security_list(self.sl_ocid),
                                     'lifecycle_state', 'TERMINATED', max_wait_seconds=300)
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

    def create_default_egress_security_rule(self):
        port_range = oraclebmc.core.models.PortRange()
        port_range.min = 1522
        port_range.max = 1522

        tcp_options = oraclebmc.core.models.TcpOptions()
        tcp_options.destination_port_range = port_range

        egress_rule = oraclebmc.core.models.EgressSecurityRule()
        egress_rule.destination = '10.0.2.0/24'
        egress_rule.source = '10.0.2.0/24'
        egress_rule.protocol = '6'
        egress_rule.tcp_options = tcp_options

        return egress_rule

    def create_default_ingress_security_rule(self):
        port_range = oraclebmc.core.models.PortRange()
        port_range.min = 1522
        port_range.max = 1522

        tcp_options = oraclebmc.core.models.TcpOptions()
        tcp_options.destination_port_range = port_range

        ingress_rule = oraclebmc.core.models.IngressSecurityRule()
        ingress_rule.destination = '10.0.2.0/24'
        ingress_rule.source = '10.0.2.0/24'
        ingress_rule.protocol = '6'
        ingress_rule.tcp_options = tcp_options

        return ingress_rule
