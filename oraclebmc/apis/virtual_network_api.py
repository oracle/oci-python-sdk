# coding: utf-8

# This is a modified version of the same template from swagger-codegen.
# The original can be found at https://github.com/swagger-api/swagger-codegen.
# The original license is below.
#
#     Copyright 2016 SmartBear Software
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#     Ref: https://github.com/swagger-api/swagger-codegen

from __future__ import absolute_import

import six

from ..api_client import ApiClient
from ..signer import Signer
missing_param = object()


class VirtualNetworkApi(object):

    def __init__(self, config):
        signer = Signer(config.tenancy, config.user, config.fingerprint, config.key_file)
        self.api_client = ApiClient(config, signer)

    def create_cpe(self, create_cpe_details, **kwargs):
        """
        CreateCpe
        Creates a new virtual Customer-Premise Equipment (CPE) object in the specified compartment. You can\nthink of a CPE object as a virtual representation of the actual router that is on-premise at your site,\nat your end of the VPN connection to your VCN. You need to create this object as part of the process of\nsetting up the VPN. For more information, see\n[Typical Virtual Cloud Network Scenarios](/Content/Network/Concepts/overview.htm#Typical_Cloud_Network_Scenarios)\nand [Managing Customer-Premise Equipment (CPE)](/Content/Network/Tasks/managingCPEs.htm).\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want\nthe CPE to reside. Notice that the CPE doesn't have to be in the same compartment as the IPSec\nconnection or other Virtual Network Service components. If you're not sure which compartment to\nuse, put the CPE in the same compartment as the IPSec connection. For more information about\ncompartments and access control, see [Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm).\nFor information about OCIDs, see [Resource Identifiers](/Content/General/Concepts/identifiers.htm).\n\nYou must provide the public IP address of your on-premise router. See\n[Configuring Your On-Premise Router](/Content/Network/Tasks/configuringCPE.htm).\n\nYou may optionally specify a *display name* for the CPE, which is simply a friendly name or description.\nIt does not have to be unique, and it's not changeable.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateCpeDetails create_cpe_details: Details for creating a CPE. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type Cpe
        """
        resource_path = "/cpes"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_cpe_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_cpe got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_cpe_details,
            response_type="Cpe")

    def create_dhcp_options(self, create_dhcp_details, **kwargs):
        """
        CreateDhcpOptions
        Creates a new set of DHCP options for the specified VCN. The only option available to use is\n[DhcpDnsOption](#/en/iaas/20160918/DhcpDnsOption/), which lets you specify how DNS (host name resolution) is\nhandled in the subnets in your VCN. For more information, see\n[Managing DHCP Options](/Content/Network/Tasks/managingDHCP.htm).\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want the set of\nDHCP options to reside. Notice that the set of options doesn't have to be in the same compartment as the VCN,\nsubnets, or other Virtual Network Service components. If you're not sure which compartment to use, put the set\nof DHCP options in the same compartment as the VCN. For more information about compartments and access control, see\n[Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm). For information about OCIDs, see\n[Resource Identifiers](/Content/General/Concepts/identifiers.htm).\n\nYou may optionally specify a *display name* for the set of DHCP options, which is simply a friendly name or description.\nIt does not have to be unique, and it's unchangeable.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateDhcpDetails create_dhcp_details: Request object for creating a new set of DHCP options. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type DhcpOptions
        """
        resource_path = "/dhcps"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_dhcp_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_dhcp_details,
            response_type="DhcpOptions")

    def create_drg(self, create_drg_details, **kwargs):
        """
        CreateDrg
        Creates a new Dynamic Routing Gateway (DRG) in the specified compartment. You can think of a DRG\nas a virtual router that provides a path for private traffic between your VCN and your on-premise\nnetwork. You use it with other Virtual Network Service components and an on-premise router to create\na site-to-site VPN. For more information, see\n[Typical Virtual Cloud Network Scenarios](/Content/Network/Concepts/overview.htm#Typical_Cloud_Network_Scenarios)\nand [Managing Dynamic Routing Gateways (DRGs)](/Content/Network/Tasks/managingDRGs.htm).\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want\nthe DRG to reside. Notice that the DRG doesn't have to be in the same compartment as the VCN,\nthe DRG attachment, or other Virtual Network Service components. If you're not sure which compartment\nto use, put the DRG in the same compartment as the VCN. For more information about compartments\nand access control, see [Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm).\nFor information about OCIDs, see [Resource Identifiers](/Content/General/Concepts/identifiers.htm).\n\nYou may optionally specify a *display name* for the DRG, which is simply a friendly name or\ndescription. It does not have to be unique, and it's not changeable.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateDrgDetails create_drg_details: Details for creating a DRG. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type Drg
        """
        resource_path = "/drgs"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_drg_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_drg got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_drg_details,
            response_type="Drg")

    def create_drg_attachment(self, create_drg_attachment_details, **kwargs):
        """
        CreateDrgAttachment
        Attaches the specified DRG to the specified VCN. A VCN can be attached to only one DRG at a time.\nThe response includes a `DrgAttachment` object with its own OCID. For more information about DRGs, see\n[Managing Dynamic Routing Gateways (DRGs)](/Content/Network/Tasks/managingDRGs.htm).\n\nYou may optionally specify a *display name* for the attachment, which is simply a friendly name or\ndescription. It does not have to be unique, and it's not changeable.\n\nFor the purposes of access control, the DRG attachment is automatically placed into the same compartment\nas the VCN. For more information about compartments and access control, see\n[Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm).\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateDrgAttachmentDetails create_drg_attachment_details: Details for creating a `DrgAttachment`. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type DrgAttachment
        """
        resource_path = "/drgAttachments"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_drg_attachment_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_drg_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_drg_attachment_details,
            response_type="DrgAttachment")

    def create_internet_gateway(self, create_internet_gateway_details, **kwargs):
        """
        CreateInternetGateway
        Creates a new Internet Gateway for the specified VCN. You can think of an Internet Gateway as a router\nthat connects the edge of the VCN with the Internet. For an example scenario that uses an Internet Gateway,\nsee [Typical Virtual Cloud Network Scenarios](/Content/Network/Concepts/overview.htm#Typical_Cloud_Network_Scenarios)\nand [Managing Internet Gateways](/Content/Network/Tasks/managingIGs.htm).\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want the Internet\nGateway to reside. Notice that the Internet Gateway doesn't have to be in the same compartment as the VCN or\nother Virtual Network Service components. If you're not sure which compartment to use, put the Internet\nGateway in the same compartment with the VCN. For more information about compartments and access control, see\n[Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm). For information about OCIDs, see\n[Resource Identifiers](/Content/General/Concepts/identifiers.htm).\n\nYou may optionally specify a *display name* for the Internet Gateway, which is simply a friendly name or\ndescription. It does not have to be unique, and it's not changeable.\n\nFor traffic to flow between a subnet and an Internet Gateway, you must create a route rule accordingly in\nthe subnet's route table (e.g., 0.0.0.0/0 > Internet Gateway). See [UpdateRouteTable](#/en/iaas/20160918/RouteTable/UpdateRouteTable).\n\nYou must specify whether the Internet Gateway is enabled when you create it. If it's disabled, that means no\ntraffic will flow to/from the Internet even if there's a route rule that enables that traffic. You can later\nuse [UpdateInternetGateway](#/en/iaas/20160918/InternetGateway/UpdateInternetGateway) to easily disable/enable the gateway without changing the\nroute rule.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateInternetGatewayDetails create_internet_gateway_details: Details for creating a new Internet Gateway. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type InternetGateway
        """
        resource_path = "/internetGateways"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_internet_gateway_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_internet_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_internet_gateway_details,
            response_type="InternetGateway")

    def create_ip_sec_connection(self, create_ip_sec_connection_details, **kwargs):
        """
        CreateIPSecConnection
        Creates a new IPSec connection between the specified DRG and CPE. This connection consists of two IPSec\ntunnels. Creating this connection is one of the steps required when setting up a VPN. For more\ninformation, see\n[Typical Virtual Cloud Network Scenarios](/Content/Network/Concepts/overview.htm#Typical_Cloud_Network_Scenarios)\nand [Managing IPSec Connections](/Content/Network/Tasks/managingIPsec.htm).\n\nIn the request, you must include at least one static route to the CPE object (you're allowed a maximum\nof 10). For example: 10.0.8.0/16.\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want the\nIPSec connection to reside. Notice that the IPSec connection doesn't have to be in the same compartment\nas the DRG, CPE, or other Virtual Network Service components. If you're not sure which compartment to\nuse, put the IPSec connection in the same compartment as the CPE. For more information about\ncompartments and access control, see\n[Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm).\nFor information about OCIDs, see [Resource Identifiers](/Content/General/Concepts/identifiers.htm).\n\nYou may optionally specify a *display name* for the IPSec connection, which is simply a friendly\nname or description. It does not have to be unique, and it is not changeable.\n\nAfter creating the IPSec connection, you need to configure your on-premise router\nwith tunnel-specific information returned by\n[GetIPSecConnectionDeviceConfig](#/en/iaas/20160918/IPSecConnectionDeviceConfig/GetIPSecConnectionDeviceConfig). For each tunnel, that operation gives\nyou the IP address of Oracle's VPN headend and the shared secret (i.e., the pre-shared key). For more\ninformation, see [Configuring Your On-Premise Router](/Content/Network/Tasks/configuringCPE.htm).\n\nTo get the status of the tunnels (whether they're up or down), use\n[GetIPSecConnectionDeviceStatus](#/en/iaas/20160918/IPSecConnectionDeviceStatus/GetIPSecConnectionDeviceStatus).\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateIPSecConnectionDetails create_ip_sec_connection_details: Details for creating an `IPSecConnection`. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type IPSecConnection
        """
        resource_path = "/ipsecConnections"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_ip_sec_connection_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_ip_sec_connection got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_ip_sec_connection_details,
            response_type="IPSecConnection")

    def create_route_table(self, create_route_table_details, **kwargs):
        """
        CreateRouteTable
        Creates a new route table for the specified VCN. In the request you must also include at least one route\nrule for the new route table (10 route rules maximum per table). For general information about route\ntables in your VCN, see [Managing Route Tables](/Content/Network/Tasks/managingroutetables.htm).\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want the route\ntable to reside. Notice that the route table doesn't have to be in the same compartment as the VCN, subnets,\nor other Virtual Network Service components. If you're not sure which compartment to use, put the route\ntable in the same compartment as the VCN. For more information about compartments and access control, see\n[Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm). For information about OCIDs, see\n[Resource Identifiers](/Content/General/Concepts/identifiers.htm).\n\nYou may optionally specify a *display name* for the route table, which is simply a friendly name or description.\nIt does not have to be unique, and it's not changeable.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateRouteTableDetails create_route_table_details: Details for creating a new route table. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type RouteTable
        """
        resource_path = "/routeTables"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_route_table_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_route_table got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_route_table_details,
            response_type="RouteTable")

    def create_security_list(self, details, **kwargs):
        """
        CreateSecurityList
        Creates a new security list for the specified VCN. A security list provides a stateful firewall\nfor the instance. Security lists are configured at the subnet level, but the rules are applied\nto the ingress and egress traffic for the individual instances in the subnet. For more information\nabout security lists, see [Security Lists](/Content/Network/Concepts/permissions.htm#Security_Lists).\n\n**Important:** Oracle Bare Metal Cloud images that run Oracle Linux automatically include iptables rules.\nIf there are issues with some type of access to an instance, make sure both the security lists associated\nwith the instance's subnet and the instance's iptables rules are set correctly. For more information,\nsee [Ways to Secure Your Network](/Content/Network/Concepts/permissions.htm#Ways_to_Secure_Your_Network).\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want the security\nlist to reside. Notice that the security list doesn't have to be in the same compartment as the VCN, subnets,\nor other Virtual Network Service components. If you're not sure which compartment to use, put the security\nlist in the same compartment as the VCN. For more information about compartments and access control, see\n[Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm). For information about OCIDs, see\n[Resource Identifiers](/Content/General/Concepts/identifiers.htm).\n\nYou may optionally specify a *display name* for the security list, which is simply a friendly name or\ndescription. It does not have to be unique, and it's not changeable.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateSecurityListDetails details: Details regarding the security list to create. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type SecurityList
        """
        resource_path = "/securityLists"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_security_list got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=details,
            response_type="SecurityList")

    def create_subnet(self, create_subnet_details, **kwargs):
        """
        CreateSubnet
        Creates a new subnet in the specified VCN. A subnet is a logical subdivision of a VCN. Each subnet exists\nin a single Availability Domain and consists of a contiguous range of IP addresses that do not overlap with\nother subnets in the VCN. Example: 172.16.1.0/24. You can't change the size of the subnet after creation,\nso it's important to think about the size of subnets you need before creating them.\nYou can have up to 300 subnets in your VCN. For conceptual information about VCNs, subnets, and other\nVirtual Network Service components, see [Overview of your Cloud Network](/Content/Network/Concepts/overview.htm)\nand [Managing Subnets](/Content/Network/Tasks/managingsubnets.htm).\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want the subnet\nto reside. Notice that the subnet doesn't have to be in the same compartment as the VCN, route tables, or\nother Virtual Network Service components. If you're not sure which compartment to use, put the subnet in\nthe same compartment as the VCN. For more information about compartments and access control, see\n[Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm). For information about OCIDs,\nsee [Resource Identifiers](/Content/General/Concepts/identifiers.htm).\n\nYou may optionally specify a route table for the subnet to use. If you don't, the subnet will use the\nVCN's default route table. For more information about route tables, see\n[Managing Route Tables](/Content/Network/Tasks/managingroutetables.htm).\n\nYou may optionally specify a security list for the subnet to use. If you don't, the subnet will use the\nVCN's default security list. For more information about security lists, see\n[Security Lists](/Content/Network/Concepts/permissions.htm#Security_Lists).\n\nYou may optionally specify a set of DHCP options for the subnet to use. If you don't, the subnet will use the\nVCN's default set. For more information about DHCP options, see\n[Managing DHCP Options](/Content/Network/Tasks/managingDHCP.htm).\n\nYou may optionally specify a *display name* for the subnet, which is simply a friendly name or description.\nIt does not have to be unique, and it's not changeable.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param CreateSubnetDetails create_subnet_details: Details for creating a subnet. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type Subnet
        """
        resource_path = "/subnets"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_subnet_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_subnet got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_subnet_details,
            response_type="Subnet")

    def create_vcn(self, create_vcn_details, **kwargs):
        """
        CreateVcn
        Creates a new Virtual Cloud Network (VCN). For conceptual information about VCNs and other Virtual Network\nService components, see [Overview of your Cloud Network](/Content/Network/Concepts/overview.htm) and\n[Managing Virtual Cloud Networks (VCNs)](/Content/Network/Tasks/managingVCNs.htm).\n\nFor the VCN you must specify a single, contiguous IPv4 CIDR block in the private IP address ranges specified in\n[RFC 1918](https://tools.ietf.org/html/rfc1918) (10.0.0.0/8, 172.16/12, and 192.168/16). Example: 172.16.0.0/16.\nThe CIDR block can range from /16 to /30, and it must not overlap with your on-premise network. You can't\nchange the size of the VCN after creation.\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want the VCN to\nreside. Consult an Oracle Bare Metal IaaS Administrator in your organization if you're not sure which\ncompartment to use. Notice that the VCN doesn't have to be in the same compartment as the subnets or other\nVirtual Network Service components. For more information about compartments and access control, see\n[Overview of the Identity and Access Management Service](/Content/Identity/Concepts/overview.htm). For information about OCIDs, see\n[Resource Identifiers](/Content/General/Concepts/identifiers.htm).\n\nYou may optionally specify a *display name* for the VCN, which is simply a friendly name or description.\nIt does not have to be unique, and it is not changeable.\n\nThe VCN automatically comes with a default route table, default security list, and default set of DHCP options.\nThe OCID for each is returned in the response. You can't delete these default objects, but you can change their\ncontents (i.e., route rules, etc.)\n\nThe VCN and subnets you create are not accessible until you attach an Internet Gateway or set up a VPN.\nFor more information, see\n[Typical Virtual Cloud Network Scenarios](/Content/Network/Concepts/overview.htm#Typical_Cloud_Network_Scenarios).\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n\nFor information about endpoints and signing API requests, see\n[Making API Requests](/Content/API/Concepts/usingapi.htm).\n

        :param CreateVcnDetails create_vcn_details: Details for creating a new VCN. (required)
        :param str opc_retry_token: A token that uniquely identifies a request so it can be retried in case of a timeout or\nserver error without risk of executing that same action again. Retry tokens expire after 24\nhours, but can be invalidated before then due to conflicting operations (e.g., if a resource\nhas been deleted and purged from the system, then a retry of the original creation request\nmay be rejected).\n
        :return: A Response object with data of type Vcn
        """
        resource_path = "/vcns"
        method = "POST"

        # Don't accept unknown kwargs
        expected_params = [
            "create_vcn_details",
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "create_vcn got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_vcn_details,
            response_type="Vcn")

    def delete_cpe(self, cpe_id, **kwargs):
        """
        DeleteCpe
        Deletes the specified CPE object. The CPE must not be connected to a DRG. This is an asynchronous\noperation; the CPE's `lifecycleState` will change to TERMINATING temporarily until the CPE is completely\nremoved.\n

        :param str cpe_id: The CPE's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/cpes/{cpeId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "cpe_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_cpe got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "cpeId": cpe_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_dhcp_options(self, dhcp_id, **kwargs):
        """
        DeleteDhcpOptions
        Deletes the specified set of DHCP options, but only if it's not in use by a subnet. You can't delete a\nVCN's default set of DHCP options.\n\nThis is an asynchronous operation; the state of the set of options will switch to TERMINATING temporarily\nuntil the set is completely removed.\n

        :param str dhcp_id: The OCID for the set of DHCP options. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/dhcps/{dhcpId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "dhcp_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dhcpId": dhcp_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_drg(self, drg_id, **kwargs):
        """
        DeleteDrg
        Deletes the specified DRG. The DRG must not be attached to a VCN or be connected to your on-premise\nnetwork. Also, there must not be a route table that lists the DRG as a target. This is an asynchronous\noperation; the DRG's `lifecycleState` will change to TERMINATING temporarily until the DRG is completely\nremoved.\n

        :param str drg_id: The DRG's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/drgs/{drgId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "drg_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_drg got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgId": drg_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_drg_attachment(self, drg_attachment_id, **kwargs):
        """
        DeleteDrgAttachment
        Detaches a DRG from a VCN by deleting the corresponding `DrgAttachment`. This is an asynchronous\noperation; the attachment's `lifecycleState` will change to TERMINATING temporarily until the attachment\nis completely removed.\n

        :param str drg_attachment_id: The DRG attachment's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/drgAttachments/{drgAttachmentId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "drg_attachment_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_drg_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgAttachmentId": drg_attachment_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_internet_gateway(self, ig_id, **kwargs):
        """
        DeleteInternetGateway
        Deletes the specified Internet Gateway. The Internet Gateway does not have to be disabled, but\nthere must not be a route table that lists it as a target.\n\nThis is an asynchronous operation; the gateway's `lifecycleState` will change to TERMINATING temporarily\nuntil the gateway is completely removed.\n

        :param str ig_id: The Internet Gateway's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/internetGateways/{igId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "ig_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_internet_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "igId": ig_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_ip_sec_connection(self, ipsc_id, **kwargs):
        """
        DeleteIPSecConnection
        Deletes the specified IPSec connection. If your goal is to disable the VPN between your VCN and\non-premise network, it's easiest to simply detach the DRG but keep all the VPN components intact.\nIf you were to delete all the components and then later need to create a VPN again, you would\nneed to configure your on-premise router again with the new information returned from\n[CreateIPSecConnection](#/en/iaas/20160918/IPSecConnection/CreateIPSecConnection).\n\nThis is an asynchronous operation; the connection's `lifecycleState` will change to TERMINATING temporarily\nuntil the connection is completely removed.\n

        :param str ipsc_id: The IPSec connection's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/ipsecConnections/{ipscId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "ipsc_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_ip_sec_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_route_table(self, rt_id, **kwargs):
        """
        DeleteRouteTable
        Deletes the specified route table, but only if it's not in use by a subnet. You can't delete a\nVCN's default route table.\n\nThis is an asynchronous operation; the route table's `lifecycleState` will change to TERMINATING temporarily\nuntil the route table is completely removed.\n

        :param str rt_id: The route table's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/routeTables/{rtId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "rt_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_route_table got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "rtId": rt_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_security_list(self, security_list_id, **kwargs):
        """
        DeleteSecurityList
        Deletes the specified security list, but only if it's not in use.\n\nThis is an asynchronous operation; the security list's `lifecycleState` will change to TERMINATING temporarily\nuntil the security list is completely removed.\n

        :param str security_list_id: The security list's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/securityLists/{securityListId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "security_list_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_security_list got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "securityListId": security_list_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_subnet(self, subnet_id, **kwargs):
        """
        DeleteSubnet
        Deletes the specified subnet, but only if there are no instances in the subnet. This is an asynchronous\noperation; the subnet's `lifecycleState` will change to TERMINATING temporarily. If there are any\ninstances in the subnet, the state will instead change back to AVAILABLE.\n

        :param str subnet_id: The subnet's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/subnets/{subnetId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "subnet_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_subnet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subnetId": subnet_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_vcn(self, vcn_id, **kwargs):
        """
        DeleteVcn
        Deletes the specified VCN. The VCN must be empty and have no attached gateways. This is an asynchronous\noperation; the VCN's `lifecycleState` will change to TERMINATING temporarily until the VCN is completely\nremoved.\n

        :param str vcn_id: The VCN's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """
        resource_path = "/vcns/{vcnId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_params = [
            "vcn_id",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "delete_vcn got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vcnId": vcn_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def get_cpe(self, cpe_id, **kwargs):
        """
        GetCpe
        Gets the specified CPE's information.

        :param str cpe_id: The CPE's OCID. (required)
        :return: A Response object with data of type Cpe
        """
        resource_path = "/cpes/{cpeId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "cpe_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_cpe got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "cpeId": cpe_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Cpe")

    def get_dhcp_options(self, dhcp_id, **kwargs):
        """
        GetDhcpOptions
        Gets the specified set of DHCP options.

        :param str dhcp_id: The OCID for the set of DHCP options. (required)
        :return: A Response object with data of type DhcpOptions
        """
        resource_path = "/dhcps/{dhcpId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "dhcp_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dhcpId": dhcp_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="DhcpOptions")

    def get_drg(self, drg_id, **kwargs):
        """
        GetDrg
        Gets the specified DRG's information.

        :param str drg_id: The DRG's OCID. (required)
        :return: A Response object with data of type Drg
        """
        resource_path = "/drgs/{drgId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "drg_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_drg got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgId": drg_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Drg")

    def get_drg_attachment(self, drg_attachment_id, **kwargs):
        """
        GetDrgAttachment
        Gets the information for the specified `DrgAttachment`.

        :param str drg_attachment_id: The DRG attachment's OCID. (required)
        :return: A Response object with data of type DrgAttachment
        """
        resource_path = "/drgAttachments/{drgAttachmentId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "drg_attachment_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_drg_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgAttachmentId": drg_attachment_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="DrgAttachment")

    def get_internet_gateway(self, ig_id, **kwargs):
        """
        GetInternetGateway
        Gets the specified Internet Gateway's information.

        :param str ig_id: The Internet Gateway's OCID. (required)
        :return: A Response object with data of type InternetGateway
        """
        resource_path = "/internetGateways/{igId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "ig_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_internet_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "igId": ig_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="InternetGateway")

    def get_ip_sec_connection(self, ipsc_id, **kwargs):
        """
        GetIPSecConnection
        Gets the specified IPSec connection's basic information, including the static routes for the\non-premise router. If you want the status of the connection (whether it's up or down), use\n[GetIPSecConnectionDeviceStatus](#/en/iaas/20160918/IPSecConnectionDeviceStatus/GetIPSecConnectionDeviceStatus).\n

        :param str ipsc_id: The IPSec connection's OCID. (required)
        :return: A Response object with data of type IPSecConnection
        """
        resource_path = "/ipsecConnections/{ipscId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "ipsc_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_ip_sec_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="IPSecConnection")

    def get_ip_sec_connection_device_config(self, ipsc_id, **kwargs):
        """
        GetIPSecConnectionDeviceConfig
        Gets the configuration information for the specified IPSec connection. For each tunnel, the\nresponse includes the IP address of Oracle's VPN headend and the shared secret.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str ipsc_id: The IPSec connection's OCID. (required)
        :return: A Response object with data of type IPSecConnectionDeviceConfig
        """
        resource_path = "/ipsecConnections/{ipscId}/deviceConfig"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "ipsc_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_ip_sec_connection_device_config got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="IPSecConnectionDeviceConfig")

    def get_ip_sec_connection_device_status(self, ipsc_id, **kwargs):
        """
        GetIPSecConnectionDeviceStatus
        Gets the status of the specified IPSec connection (whether it's up or down).

        :param str ipsc_id: The IPSec connection's OCID. (required)
        :return: A Response object with data of type IPSecConnectionDeviceStatus
        """
        resource_path = "/ipsecConnections/{ipscId}/deviceStatus"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "ipsc_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_ip_sec_connection_device_status got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="IPSecConnectionDeviceStatus")

    def get_route_table(self, rt_id, **kwargs):
        """
        GetRouteTable
        Gets the specified route table's information.

        :param str rt_id: The route table's OCID. (required)
        :return: A Response object with data of type RouteTable
        """
        resource_path = "/routeTables/{rtId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "rt_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_route_table got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "rtId": rt_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="RouteTable")

    def get_security_list(self, security_list_id, **kwargs):
        """
        GetSecurityList
        Gets the specified security list's information.

        :param str security_list_id: The security list's OCID. (required)
        :return: A Response object with data of type SecurityList
        """
        resource_path = "/securityLists/{securityListId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "security_list_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_security_list got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "securityListId": security_list_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="SecurityList")

    def get_subnet(self, subnet_id, **kwargs):
        """
        GetSubnet
        Gets the specified subnet's information.

        :param str subnet_id: The subnet's OCID. (required)
        :return: A Response object with data of type Subnet
        """
        resource_path = "/subnets/{subnetId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "subnet_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_subnet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subnetId": subnet_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Subnet")

    def get_vcn(self, vcn_id, **kwargs):
        """
        GetVcn
        Gets the specified VCN's information.

        :param str vcn_id: The VCN's OCID. (required)
        :return: A Response object with data of type Vcn
        """
        resource_path = "/vcns/{vcnId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "vcn_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_vcn got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vcnId": vcn_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Vcn")

    def get_vnic(self, vnic_id, **kwargs):
        """
        GetVnic
        Gets the information for the specified Virtual Network Interface Card (VNIC), including the attached\ninstance's public and private IP addresses. Each instance automatically has a VNIC attached to it,\nand the VNIC connects the instance to the subnet. You can get the instance's VNIC OCID from the\nCloud Compute Service's [ListVnicAttachments](#/en/iaas/20160918/VnicAttachment/ListVnicAttachments) operation.\n

        :param str vnic_id: The VNIC's OCID. (required)
        :return: A Response object with data of type Vnic
        """
        resource_path = "/vnics/{vnicId}"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "vnic_id"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "get_vnic got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vnicId": vnic_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Vnic")

    def list_cpes(self, compartment_id, **kwargs):
        """
        ListCpes
        Gets a list of the Customer-Premise Equipment objects (CPEs) in the specified compartment.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[Cpe]
        """
        resource_path = "/cpes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_cpes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing_param),
            "page": kwargs.get("page", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Cpe]")

    def list_dhcp_options(self, compartment_id, vcn_id, **kwargs):
        """
        ListDhcpOptions
        Gets a list of the sets of DHCP options in the specified VCN and specified compartment.\nThe response includes the default set of options that automatically comes with each VCN,\nplus any other sets you've created.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str vcn_id: The VCN's OCID. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[DhcpOptions]
        """
        resource_path = "/dhcps"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "vcn_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "vcnId": vcn_id,
            "limit": kwargs.get("limit", missing_param),
            "page": kwargs.get("page", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[DhcpOptions]")

    def list_drg_attachments(self, compartment_id, **kwargs):
        """
        ListDrgAttachments
        Gets a list of the `DrgAttachment`s for the specified compartment. You can optionally filter the\nresults by VCN or DRG.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str vcn_id: The VCN's OCID.
        :param str drg_id: The DRG's OCID.
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[DrgAttachment]
        """
        resource_path = "/drgAttachments"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "vcn_id",
            "drg_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_drg_attachments got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "vcnId": kwargs.get("vcn_id", missing_param),
            "drgId": kwargs.get("drg_id", missing_param),
            "limit": kwargs.get("limit", missing_param),
            "page": kwargs.get("page", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[DrgAttachment]")

    def list_drgs(self, compartment_id, **kwargs):
        """
        ListDrgs
        Gets a list of the DRGs in the specified compartment.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[Drg]
        """
        resource_path = "/drgs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_drgs got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing_param),
            "page": kwargs.get("page", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Drg]")

    def list_internet_gateways(self, compartment_id, vcn_id, **kwargs):
        """
        ListInternetGateways
        Gets a list of the Internet Gateways in the specified VCN and the specified compartment.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str vcn_id: The VCN's OCID. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[InternetGateway]
        """
        resource_path = "/internetGateways"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "vcn_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_internet_gateways got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "vcnId": vcn_id,
            "limit": kwargs.get("limit", missing_param),
            "page": kwargs.get("page", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[InternetGateway]")

    def list_ip_sec_connections(self, compartment_id, **kwargs):
        """
        ListIPSecConnections
        Gets a list of the IPSec connections for the specified compartment. You can optionally filter the\nresults by DRG or CPE.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str drg_id: The DRG's OCID.
        :param str cpe_id: The CPE's OCID.
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[IPSecConnection]
        """
        resource_path = "/ipsecConnections"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "drg_id",
            "cpe_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_ip_sec_connections got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "drgId": kwargs.get("drg_id", missing_param),
            "cpeId": kwargs.get("cpe_id", missing_param),
            "limit": kwargs.get("limit", missing_param),
            "page": kwargs.get("page", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[IPSecConnection]")

    def list_route_tables(self, compartment_id, vcn_id, **kwargs):
        """
        ListRouteTables
        Gets a list of the route tables in the specified VCN and specified compartment. The response\nincludes the default route table that automatically comes with each VCN, plus any route tables\nyou've created.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str vcn_id: The VCN's OCID. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[RouteTable]
        """
        resource_path = "/routeTables"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "vcn_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_route_tables got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing_param),
            "page": kwargs.get("page", missing_param),
            "vcnId": vcn_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[RouteTable]")

    def list_security_lists(self, compartment_id, vcn_id, **kwargs):
        """
        ListSecurityLists
        Gets a list of the security lists in the specified VCN and compartment.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str vcn_id: The VCN's OCID. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[SecurityList]
        """
        resource_path = "/securityLists"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "vcn_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_security_lists got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing_param),
            "page": kwargs.get("page", missing_param),
            "vcnId": vcn_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[SecurityList]")

    def list_subnets(self, compartment_id, vcn_id, **kwargs):
        """
        ListSubnets
        Gets a list of the subnets in the specified VCN and the specified compartment.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str vcn_id: The VCN's OCID. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[Subnet]
        """
        resource_path = "/subnets"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "vcn_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_subnets got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing_param),
            "page": kwargs.get("page", missing_param),
            "vcnId": vcn_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Subnet]")

    def list_vcns(self, compartment_id, **kwargs):
        """
        ListVcns
        Gets a list of the Virtual Cloud Networks (VCNs) in the specified compartment.\n\nTo use this and other API operations, you must be authorized in an IAM policy. If you're not authorized,\ntalk to an administrator. If you're an administrator who needs to write policies to give users access, see\n[Getting Started with Policies](/Content/Identity/Concepts/policygetstarted.htm).\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call.\n\nExample: `500`\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call.\n
        :return: A Response object with data of type list[Vcn]
        """
        resource_path = "/vcns"
        method = "GET"

        # Don't accept unknown kwargs
        expected_params = [
            "compartment_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "list_vcns got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing_param),
            "page": kwargs.get("page", missing_param)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Vcn]")

    def update_dhcp_options(self, dhcp_id, update_dhcp_details, **kwargs):
        """
        UpdateDhcpOptions
        Updates the specified set of DHCP options. When updating the set, the new `DhcpOptions` object\nyou provide replaces the entire existing set of options.\n

        :param str dhcp_id: The OCID for the set of DHCP options. (required)
        :param UpdateDhcpDetails update_dhcp_details: Request object for updating a set of DHCP options. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type DhcpOptions
        """
        resource_path = "/dhcps/{dhcpId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_params = [
            "dhcp_id",
            "update_dhcp_details",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "update_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dhcpId": dhcp_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_dhcp_details,
            response_type="DhcpOptions")

    def update_internet_gateway(self, ig_id, update_internet_gateway_details, **kwargs):
        """
        UpdateInternetGateway
        Disables/enables the Internet Gateway.\n\nIf the gateway is disabled, that means no traffic will flow to/from the Internet even if there's\na route rule that enables that traffic.\n

        :param str ig_id: The Internet Gateway's OCID. (required)
        :param UpdateInternetGatewayDetails update_internet_gateway_details: Details for updating the Internet Gateway. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type InternetGateway
        """
        resource_path = "/internetGateways/{igId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_params = [
            "ig_id",
            "update_internet_gateway_details",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "update_internet_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "igId": ig_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_internet_gateway_details,
            response_type="InternetGateway")

    def update_route_table(self, rt_id, update_route_table_details, **kwargs):
        """
        UpdateRouteTable
        Updates the specified route table's rules.\n\nWhen updating the route table, the new `RouteRules` object you provide replaces the entire\nexisting set of rules.\n

        :param str rt_id: The route table's OCID. (required)
        :param UpdateRouteTableDetails update_route_table_details: Details object for updating a route table. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type RouteTable
        """
        resource_path = "/routeTables/{rtId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_params = [
            "rt_id",
            "update_route_table_details",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "update_route_table got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "rtId": rt_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_route_table_details,
            response_type="RouteTable")

    def update_security_list(self, security_list_id, details, **kwargs):
        """
        UpdateSecurityList
        Updates the specified security list's rules. The entire set of existing rules is replaced by\nthe new set of rules.\n

        :param str security_list_id: The security list's OCID. (required)
        :param UpdateSecurityListDetails details: Updated details for the security list. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type SecurityList
        """
        resource_path = "/securityLists/{securityListId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_params = [
            "security_list_id",
            "details",
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_params]
        if extra_kwargs:
            raise ValueError(
                "update_security_list got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "securityListId": security_list_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing_param}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing_param)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing_param}

        return self.api_client.call_api(
            endpoint=self.api_client.config.endpoint_virtual_network_api,
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=details,
            response_type="SecurityList")
