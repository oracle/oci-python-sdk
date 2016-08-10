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

# python 2 and python 3 compatibility library
from six import iteritems
from io import IOBase

class VcnServiceApi(object):

    def __init__(self, api_client):
        self.api_client = api_client


    def create_cpe(self, create_cpe_request, **kwargs):
        """
        CreateCpe
        Creates a new virtual Customer-Premise Equipment (CPE) object in the specified compartment. You can\nthink of a CPE object as a virtual representation of the actual router that is on-premise at your site,\nat your end of the VPN connection to your VCN. You need to create this object as part of the process of\nsetting up the VPN. For more information, see\n[Typical Virtual Cloud Network Scenarios](../../../#Network/Concepts/overview.htm#Typical_Cloud_Network_Scenarios)\n and [Managing Customer-Premise Equipment (CPE)](../../../#Network/Tasks/managingCPEs.htm).\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want\nthe CPE to reside. Notice that the CPE doesn't have to be in the same compartment as the IPsec\nconnection or other Virtual Network Service components. If you're not sure which compartment to\nuse, put the CPE in the same compartment as the IPsec connection. For more information about\ncompartments and access control, see [Overview of the Identity Service](../../../#Identity/Concepts/overview.htm).\nFor information about OCIDs, see [Resource Identifiers](../../../#General/Concepts/identifiers.htm).\n\nYou must provide the public IP address of your on-premise router. See\n[Configuring Your On-Premise Router](../../../#Network/Tasks/configuringCPE.htm).\n\nYou may optionally specify a *display name* for the CPE, which is simply a friendly name or description.\nIt does not have to be unique, and it's unchangeable.\n

        :param CreateCpeRequest create_cpe_request: Request object for creating a CPE. (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :return: A Response object with data of type Cpe
        """

        all_params = ['create_cpe_request', 'opc_idempotency_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_cpe" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_cpe_request' is set
        if ('create_cpe_request' not in params) or (params['create_cpe_request'] is None):
            raise ValueError("Missing the required parameter `create_cpe_request` when calling `create_cpe`")

        resource_path = '/cpes'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']

        body_params = None
        if 'create_cpe_request' in params:
            body_params = params['create_cpe_request']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Cpe')
        return response

    def create_drg(self, create_drg_request, **kwargs):
        """
        CreateDrg
        Creates a new Dynamic Routing Gateway (DRG) in the specified compartment. You can think of a DRG\nas a virtual router that provides a path for private traffic between your VCN and your on-premise\nnetwork. You use it with other Virtual Network Service components and an on-premise router to create\na site-to-site VPN. For more information, see\n[Typical Virtual Cloud Network Scenarios](../../../#Network/Concepts/overview.htm#Typical_Cloud_Network_Scenarios)\nand [Managing Dynamic Routing Gateways (DRGs)](../../../#Network/Tasks/managingDRGs.htm).\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want\nthe DRG to reside. Notice that the DRG doesn't have to be in the same compartment as the VCN,\nthe DRG attachment, or other Virtual Network Service components. If you're not sure which compartment\nto use, put the DRG in the same compartment as the VCN. For more information about compartments\nand access control, see [Overview of the Identity Service](../../../#Identity/Concepts/overview.htm).\nFor information about OCIDs, see [Resource Identifiers](../../../#General/Concepts/identifiers.htm).\n\nYou may optionally specify a *display name* for the DRG, which is simply a friendly name or\ndescription. It does not have to be unique, and it's unchangeable.\n

        :param CreateDrgRequest create_drg_request: Request object for creating a DRG. (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :return: A Response object with data of type Drg
        """

        all_params = ['create_drg_request', 'opc_idempotency_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_drg" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_drg_request' is set
        if ('create_drg_request' not in params) or (params['create_drg_request'] is None):
            raise ValueError("Missing the required parameter `create_drg_request` when calling `create_drg`")

        resource_path = '/drgs'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']

        body_params = None
        if 'create_drg_request' in params:
            body_params = params['create_drg_request']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Drg')
        return response

    def create_drg_attachment(self, create_drg_attachment_request, **kwargs):
        """
        CreateDrgAttachment
        Attaches the specified DRG to the specified VCN. A VCN can be attached to only one DRG at a time.\nThe response includes a `DrgAttachment` object with its own OCID. For more information about DRGs, see\n[Managing Dynamic Routing Gateways (DRGs)](../../../#Network/Tasks/managingDRGs.htm).\n\nYou may optionally specify a *display name* for the attachment, which is simply a friendly name or\ndescription. It does not have to be unique, and it's unchangeable.\n\nFor the purposes of access control, the DRG attachment is automatically placed into the same compartment\nas the VCN. For more information about compartments and access control, see\n[Overview of the Identity Service](../../../#Identity/Concepts/overview.htm).\n

        :param CreateDrgAttachmentRequest create_drg_attachment_request: Request object for creating a `DrgAttachment`. (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :return: A Response object with data of type DrgAttachment
        """

        all_params = ['create_drg_attachment_request', 'opc_idempotency_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_drg_attachment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_drg_attachment_request' is set
        if ('create_drg_attachment_request' not in params) or (params['create_drg_attachment_request'] is None):
            raise ValueError("Missing the required parameter `create_drg_attachment_request` when calling `create_drg_attachment`")

        resource_path = '/drgAttachments'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']

        body_params = None
        if 'create_drg_attachment_request' in params:
            body_params = params['create_drg_attachment_request']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='DrgAttachment')
        return response

    def create_internet_gateway(self, create_internet_gateway_request, **kwargs):
        """
        CreateInternetGateway
        Creates a new Internet Gateway for the specified VCN. You can think of an Internet Gateway as a router\nthat connects the edge of the VCN with the Internet. For an example scenario that uses an Internet Gateway,\nsee [Typical Virtual Cloud Network Scenarios](../../../#Network/Concepts/overview.htm#Typical_Cloud_Network_Scenarios)\nand [Managing Internet Gateways](../../../#Network/Tasks/managingIGs.htm).\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want the Internet\nGateway to reside. Notice that the Internet Gateway doesn't have to be in the same compartment as the VCN or\nother Virtual Network Service components. If you're not sure which compartment to use, put the Internet\nGateway in the same compartment with the VCN. For more information about compartments and access control, see\n[Overview of the Identity Service](../../../#Identity/Concepts/overview.htm). For information about OCIDs, see\n[Resource Identifiers](../../../#General/Concepts/identifiers.htm).\n\nYou may optionally specify a *display name* for the Internet Gateway, which is simply a friendly name or\ndescription. It does not have to be unique, and it's unchangeable.\n\nFor traffic to flow between a subnet and an Internet Gateway, you must create a route rule accordingly in\nthe subnet's route table (e.g., 0.0.0.0/0 > Internet Gateway). See [UpdateRouteTable](#updateRouteTable).\n\nYou must specify whether the Internet Gateway is enabled when you create it. If it's disabled, that means no\ntraffic will flow to/from the Internet even if there's a route rule that enables that traffic. You can later\nuse [UpdateInternetGateway](#updateInternetGateway) to easily disable/enable the gateway without changing the\nroute rule.\n

        :param CreateInternetGatewayRequest create_internet_gateway_request: Request object for creating a new Internet Gateway. (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :return: A Response object with data of type InternetGateway
        """

        all_params = ['create_internet_gateway_request', 'opc_idempotency_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_internet_gateway" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_internet_gateway_request' is set
        if ('create_internet_gateway_request' not in params) or (params['create_internet_gateway_request'] is None):
            raise ValueError("Missing the required parameter `create_internet_gateway_request` when calling `create_internet_gateway`")

        resource_path = '/internetGateways'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']

        body_params = None
        if 'create_internet_gateway_request' in params:
            body_params = params['create_internet_gateway_request']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='InternetGateway')
        return response

    def create_ip_sec_connection(self, create_ip_sec_connection_request, **kwargs):
        """
        CreateIPSecConnection
        Creates a new IPSec connection between the specified DRG and CPE. This connection consists of two IPsec\ntunnels. Creating this connection is one of the steps required when setting up a VPN. For more\ninformation, see\n[Typical Virtual Cloud Network Scenarios](../../../#Network/Concepts/overview.htm#Typical_Cloud_Network_Scenarios)\nand [Managing IPsec Connections](../../../#Network/Tasks/managingIPsec.htm).\n\nIn the request, you must include at least one static route to the CPE object (you're allowed a maximum\nof 10). For example: 10.0.8.0/16.\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want the\nIPsec connection to reside. Notice that the IPsec connection doesn't have to be in the same compartment\nas the DRG, CPE, or other Virtual Network Service components. If you're not sure which compartment to\nuse, put the IPSec connection in the same compartment as the CPE. For more information about\ncompartments and access control, see\n[Overview of the Identity Service](../../../#Identity/Concepts/overview.htm).\nFor information about OCIDs, see [Resource Identifiers](../../../#General/Concepts/identifiers.htm).\n\nYou may optionally specify a *display name* for the IPSec connection, which is simply a friendly\nname or description. It does not have to be unique, and it is unchangeable.\n\nAfter creating the IPsec connection, you need to configure your on-premise router\nwith tunnel-specific information returned by\n[GetIPSecConnectionDeviceConfig](#getIPSecConnectionDeviceConfig). For each tunnel, that operation gives\nyou the IP address of Oracle's VPN headend and the shared secret (i.e., the pre-shared key). For more\ninformation, see [Configuring Your On-Premise Router](../../../#Network/Tasks/configuringCPE.htm).\n\nTo get the status of the tunnels (whether they're up or down), use\n[GetIPSecConnectionDeviceStatus](#getIPSecConnectionDeviceStatus).\n

        :param CreateIPSecConnectionRequest create_ip_sec_connection_request: Request object for creating an `IPSecConnection`. (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :return: A Response object with data of type IPSecConnection
        """

        all_params = ['create_ip_sec_connection_request', 'opc_idempotency_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ip_sec_connection" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_ip_sec_connection_request' is set
        if ('create_ip_sec_connection_request' not in params) or (params['create_ip_sec_connection_request'] is None):
            raise ValueError("Missing the required parameter `create_ip_sec_connection_request` when calling `create_ip_sec_connection`")

        resource_path = '/ipsecConnections'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']

        body_params = None
        if 'create_ip_sec_connection_request' in params:
            body_params = params['create_ip_sec_connection_request']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='IPSecConnection')
        return response

    def create_route_table(self, create_route_table_request, **kwargs):
        """
        CreateRouteTable
        Creates a new route table for the specified VCN. In the request you must also include at least one route\nrule for the new route table (10 route rules maximum per table). For general information about route\ntables in your VCN, see [Managing Route Tables](../../../#Network/Tasks/managingroutetables.htm).\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want the route\ntable to reside. Notice that the route table doesn't have to be in the same compartment as the VCN, subnets,\nor other Virtual Network Service components. If you're not sure which compartment to use, put the route\ntable in the same compartment as the VCN. For more information about compartments and access control, see\n[Overview of the Identity Service](../../../#Identity/Concepts/overview.htm). For information about OCIDs, see\n[Resource Identifiers](../../../#General/Concepts/identifiers.htm).\n\nYou may optionally specify a *display name* for the route table, which is simply a friendly name or description.\nIt does not have to be unique, and it's unchangeable.\n

        :param CreateRouteTableRequest create_route_table_request: Request object for creating a new route table. (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :return: A Response object with data of type RouteTable
        """

        all_params = ['create_route_table_request', 'opc_idempotency_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_route_table" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_route_table_request' is set
        if ('create_route_table_request' not in params) or (params['create_route_table_request'] is None):
            raise ValueError("Missing the required parameter `create_route_table_request` when calling `create_route_table`")

        resource_path = '/routeTables'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']

        body_params = None
        if 'create_route_table_request' in params:
            body_params = params['create_route_table_request']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='RouteTable')
        return response

    def create_subnet(self, create_subnet_request, **kwargs):
        """
        CreateSubnet
        Creates a new subnet in the specified VCN. A subnet is a logical subdivision of a VCN. Each subnet exists\nin a single Availability Domain and consists of a contiguous range of IP addresses that do not overlap with\nother subnets in the VCN. Example: 172.16.1.0/24. You can't change the size of the subnet after creation,\nso it's important to think about the size of subnets you need before creating them.\nYou can have up to 10 subnets in your VCN. For conceptual information about VCNs, subnets, and other\nVirtual Network Service components, see [Overview of your Cloud Network](../../../#Network/Concepts/overview.htm)\nand [Managing Subnets](../../../#Network/Tasks/managingsubnets.htm).\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want the subnet\nto reside. Notice that the subnet doesn't have to be in the same compartment as the VCN, route tables, or\nother Virtual Network Service components. If you're not sure which compartment to use, put the subnet in\nthe same compartment as the VCN. For more information about compartments and access control, see\n[Overview of the Identity Service](../../../#Identity/Concepts/overview.htm). For information about OCIDs,\nsee [Resource Identifiers](../../../#General/Concepts/identifiers.htm).\n\nYou may optionally specify a route table for the subnet to use. If you don't, the subnet will use the\nVCN's default route table. For more information about route tables, see\n[Managing Route Tables](../../../#Network/Tasks/managingroutetables.htm).\n\nYou may optionally specify a *display name* for the subnet, which is simply a friendly name or description.\nIt does not have to be unique, and it's unchangeable.\n

        :param CreateSubnetRequest create_subnet_request: Request object for creating a subnet. (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :return: A Response object with data of type Subnet
        """

        all_params = ['create_subnet_request', 'opc_idempotency_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_subnet" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_subnet_request' is set
        if ('create_subnet_request' not in params) or (params['create_subnet_request'] is None):
            raise ValueError("Missing the required parameter `create_subnet_request` when calling `create_subnet`")

        resource_path = '/subnets'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']

        body_params = None
        if 'create_subnet_request' in params:
            body_params = params['create_subnet_request']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Subnet')
        return response

    def create_vcn(self, create_vcn_request, **kwargs):
        """
        CreateVcn
        Creates a new Virtual Cloud Network (VCN). For conceptual information about VCNs and other Virtual Network Service\ncomponents, see [Overview of your Cloud Network](../../../#Network/Concepts/overview.htm) and\n[Managing Virtual Cloud Networks (VCNs)](../../../#Network/Tasks/managingVCNs.htm).\n\nFor the VCN you must specify a single, contiguous IPv4 CIDR block in the private IP address ranges specified in\n[RFC 1918](https://tools.ietf.org/html/rfc1918) (10.0.0.0/8, 172.16/12, and 192.168/16). Example: 172.16.0.0/16.\nThe CIDR block can range from /16 to /30, and it must not overlap with your on-premise network. You can't\nchange the size of the VCN after creation.\n\nFor the purposes of access control, you must provide the OCID of the compartment where you want the VCN to reside.\nConsult an Oracle Bare Metal IaaS Administrator in your organization if you're not sure which compartment to use.\nNotice that the VCN doesn't have to be in the same compartment as the subnets or other Virtual Network Service\ncomponents. For more information about compartments and access control, see\n[Overview of the Identity Service](../../../#Identity/Concepts/overview.htm). For information about OCIDs, see\n[Resource Identifiers](../../../#General/Concepts/identifiers.htm).\n\nYou may optionally specify a *display name* for the VCN, which is simply a friendly name or description.\nIt does not have to be unique, and it is unchangeable.\n\nThe VCN automatically comes with a default route table; its OCID is returned in the response.\n\nThe VCN and subnets you create are not accessible until you attach an Internet Gateway or set up a VPN.\nFor more information, see\n[Typical Virtual Cloud Network Scenarios](../../../#Network/Concepts/overview.htm#Typical_Cloud_Network_Scenarios).\n\nFor information about endpoints and signing API requests, see\n[Making API Requests](../../../#API/Concepts/usingapi.htm).\n

        :param CreateVcnRequest create_vcn_request: Request object for creating a new VCN. (required)
        :param str opc_idempotency_token: A token you supply to uniquely identify the request and provide idempotency if\nthe request is retried. Idempotency tokens expire after 30 minutes.\n
        :return: A Response object with data of type Vcn
        """

        all_params = ['create_vcn_request', 'opc_idempotency_token']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_vcn" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'create_vcn_request' is set
        if ('create_vcn_request' not in params) or (params['create_vcn_request'] is None):
            raise ValueError("Missing the required parameter `create_vcn_request` when calling `create_vcn`")

        resource_path = '/vcns'
        path_params = {}

        query_params = {}

        header_params = {}
        if 'opc_idempotency_token' in params:
            header_params['opc-idempotency-token'] = params['opc_idempotency_token']

        body_params = None
        if 'create_vcn_request' in params:
            body_params = params['create_vcn_request']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Vcn')
        return response

    def delete_cpe(self, cpe_id, **kwargs):
        """
        DeleteCpe
        Deletes the specified CPE object. The CPE must not be connected to a DRG. This is an asynchronous\noperation; the CPE's state will switch to TERMINATING temporarily until the CPE is completely removed.\n

        :param str cpe_id: The CPE's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['cpe_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_cpe" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'cpe_id' is set
        if ('cpe_id' not in params) or (params['cpe_id'] is None):
            raise ValueError("Missing the required parameter `cpe_id` when calling `delete_cpe`")

        resource_path = '/cpes/{cpeId}'
        path_params = {}
        if 'cpe_id' in params:
            path_params['cpeId'] = params['cpe_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def delete_drg(self, drg_id, **kwargs):
        """
        DeleteDrg
        Deletes the specified DRG. The DRG must not be attached to a VCN or be connected to your on-premise\nnetwork. Also, there must not be a route table that lists the DRG as a target. This is an asynchronous\noperation; the DRG's state will switch to TERMINATING temporarily until the DRG is completely removed.\n

        :param str drg_id: The DRG's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['drg_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_drg" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'drg_id' is set
        if ('drg_id' not in params) or (params['drg_id'] is None):
            raise ValueError("Missing the required parameter `drg_id` when calling `delete_drg`")

        resource_path = '/drgs/{drgId}'
        path_params = {}
        if 'drg_id' in params:
            path_params['drgId'] = params['drg_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def delete_drg_attachment(self, drg_attachment_id, **kwargs):
        """
        DeleteDrgAttachment
        Detaches a DRG from a VCN by deleting the corresponding `DrgAttachment`. This is an asynchronous\noperation; the attachment's state will switch to TERMINATING temporarily until the attachment\nis completely removed.\n

        :param str drg_attachment_id: The DRG attachment's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['drg_attachment_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_drg_attachment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'drg_attachment_id' is set
        if ('drg_attachment_id' not in params) or (params['drg_attachment_id'] is None):
            raise ValueError("Missing the required parameter `drg_attachment_id` when calling `delete_drg_attachment`")

        resource_path = '/drgAttachments/{drgAttachmentId}'
        path_params = {}
        if 'drg_attachment_id' in params:
            path_params['drgAttachmentId'] = params['drg_attachment_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def delete_internet_gateway(self, ig_id, **kwargs):
        """
        DeleteInternetGateway
        Deletes the specified Internet Gateway. The Internet Gateway does not have to be disabled, but\nthere must not be a route table that lists it as a target.\n\nThis is an asynchronous operation; the gateway's state will switch to TERMINATING temporarily\nuntil the gateway is completely removed.\n

        :param str ig_id: The Internet Gateway's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['ig_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_internet_gateway" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'ig_id' is set
        if ('ig_id' not in params) or (params['ig_id'] is None):
            raise ValueError("Missing the required parameter `ig_id` when calling `delete_internet_gateway`")

        resource_path = '/internetGateways/{igId}'
        path_params = {}
        if 'ig_id' in params:
            path_params['igId'] = params['ig_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def delete_ip_sec_connection(self, ipsc_id, **kwargs):
        """
        DeleteIPSecConnection
        Deletes the specified IPsec connection. If your goal is to disable the VPN between your VCN and\non-premise network, it's easiest to simply detach the DRG but keep all the VPN components intact.\nIf you were to delete all the components and then later need to create a VPN again, you would\nneed to configure your on-premise router again with the new information returned from\n[CreateIPSecConnection](#createIPSecConnection).\n\nThis is an asynchronous operation; the connection's state will switch to TERMINATING temporarily\nuntil the connection is completely removed.\n

        :param str ipsc_id: The IPsec connection's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['ipsc_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_ip_sec_connection" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'ipsc_id' is set
        if ('ipsc_id' not in params) or (params['ipsc_id'] is None):
            raise ValueError("Missing the required parameter `ipsc_id` when calling `delete_ip_sec_connection`")

        resource_path = '/ipsecConnections/{ipscId}'
        path_params = {}
        if 'ipsc_id' in params:
            path_params['ipscId'] = params['ipsc_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def delete_route_table(self, rt_id, **kwargs):
        """
        DeleteRouteTable
        Deletes the specified route table, but only if it's not in use by a subnet. You can't delete a\nVCN's default route table.\n\nThis is an asynchronous operation; the route table's state will switch to TERMINATING temporarily\nuntil the route table is completely removed.\n

        :param str rt_id: The route table's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['rt_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_route_table" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'rt_id' is set
        if ('rt_id' not in params) or (params['rt_id'] is None):
            raise ValueError("Missing the required parameter `rt_id` when calling `delete_route_table`")

        resource_path = '/routeTables/{rtId}'
        path_params = {}
        if 'rt_id' in params:
            path_params['rtId'] = params['rt_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def delete_subnet(self, subnet_id, **kwargs):
        """
        DeleteSubnet
        Deletes the specified subnet, but only if there are no instances in the subnet. This is an asynchronous\noperation; the subnet's state will switch to TERMINATING temporarily. When the subnet is deleted,\nits state will switch to TERMINATED. If there are any instances in the subnet, the subnet's state\nwill instead switch back to AVAILABLE.\n

        :param str subnet_id: The subnet's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['subnet_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_subnet" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'subnet_id' is set
        if ('subnet_id' not in params) or (params['subnet_id'] is None):
            raise ValueError("Missing the required parameter `subnet_id` when calling `delete_subnet`")

        resource_path = '/subnets/{subnetId}'
        path_params = {}
        if 'subnet_id' in params:
            path_params['subnetId'] = params['subnet_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def delete_vcn(self, vcn_id, **kwargs):
        """
        DeleteVcn
        Deletes the specified VCN. The VCN must be empty and have no attached gateways. This is an asynchronous\noperation; the VCN's state will switch to TERMINATING temporarily until the VCN is completely removed.\n

        :param str vcn_id: The VCN's OCID. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type None
        """

        all_params = ['vcn_id', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_vcn" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'vcn_id' is set
        if ('vcn_id' not in params) or (params['vcn_id'] is None):
            raise ValueError("Missing the required parameter `vcn_id` when calling `delete_vcn`")

        resource_path = '/vcns/{vcnId}'
        path_params = {}
        if 'vcn_id' in params:
            path_params['vcnId'] = params['vcn_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type=None)
        return response

    def get_cpe(self, cpe_id, **kwargs):
        """
        GetCpe
        Gets the specified CPE's information.

        :param str cpe_id: The CPE's OCID. (required)
        :return: A Response object with data of type Cpe
        """

        all_params = ['cpe_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cpe" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'cpe_id' is set
        if ('cpe_id' not in params) or (params['cpe_id'] is None):
            raise ValueError("Missing the required parameter `cpe_id` when calling `get_cpe`")

        resource_path = '/cpes/{cpeId}'
        path_params = {}
        if 'cpe_id' in params:
            path_params['cpeId'] = params['cpe_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Cpe')
        return response

    def get_drg(self, drg_id, **kwargs):
        """
        GetDrg
        Gets the specified DRG's information.

        :param str drg_id: The DRG's OCID. (required)
        :return: A Response object with data of type Drg
        """

        all_params = ['drg_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_drg" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'drg_id' is set
        if ('drg_id' not in params) or (params['drg_id'] is None):
            raise ValueError("Missing the required parameter `drg_id` when calling `get_drg`")

        resource_path = '/drgs/{drgId}'
        path_params = {}
        if 'drg_id' in params:
            path_params['drgId'] = params['drg_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Drg')
        return response

    def get_drg_attachment(self, drg_attachment_id, **kwargs):
        """
        GetDrgAttachment
        Gets the information for the specified `DrgAttachment`.

        :param str drg_attachment_id: The DRG attachment's OCID. (required)
        :return: A Response object with data of type DrgAttachment
        """

        all_params = ['drg_attachment_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_drg_attachment" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'drg_attachment_id' is set
        if ('drg_attachment_id' not in params) or (params['drg_attachment_id'] is None):
            raise ValueError("Missing the required parameter `drg_attachment_id` when calling `get_drg_attachment`")

        resource_path = '/drgAttachments/{drgAttachmentId}'
        path_params = {}
        if 'drg_attachment_id' in params:
            path_params['drgAttachmentId'] = params['drg_attachment_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='DrgAttachment')
        return response

    def get_internet_gateway(self, ig_id, **kwargs):
        """
        GetInternetGateway
        Gets the specified Internet Gateway's information.

        :param str ig_id: The Internet Gateway's OCID. (required)
        :return: A Response object with data of type InternetGateway
        """

        all_params = ['ig_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_internet_gateway" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'ig_id' is set
        if ('ig_id' not in params) or (params['ig_id'] is None):
            raise ValueError("Missing the required parameter `ig_id` when calling `get_internet_gateway`")

        resource_path = '/internetGateways/{igId}'
        path_params = {}
        if 'ig_id' in params:
            path_params['igId'] = params['ig_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='InternetGateway')
        return response

    def get_ip_sec_connection(self, ipsc_id, **kwargs):
        """
        GetIPSecConnection
        Gets the specified IPsec connection's basic information, including the static routes for the\non-premise router. If you want the status of the connection (whether it's up or down), use\n[GetIPSecConnectionDeviceStatus](#getIPSecConnectionDeviceStatus).\n

        :param str ipsc_id: The IPsec connection's OCID. (required)
        :return: A Response object with data of type IPSecConnection
        """

        all_params = ['ipsc_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ip_sec_connection" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'ipsc_id' is set
        if ('ipsc_id' not in params) or (params['ipsc_id'] is None):
            raise ValueError("Missing the required parameter `ipsc_id` when calling `get_ip_sec_connection`")

        resource_path = '/ipsecConnections/{ipscId}'
        path_params = {}
        if 'ipsc_id' in params:
            path_params['ipscId'] = params['ipsc_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='IPSecConnection')
        return response

    def get_ip_sec_connection_device_config(self, ipsc_id, **kwargs):
        """
        GetIPSecConnectionDeviceConfig
        Gets the configuration information for the specified IPsec connection. For each tunnel, the\nresponse includes the IP address of Oracle's VPN headend and the shared secret.\n

        :param str ipsc_id: The IPsec connection's OCID. (required)
        :return: A Response object with data of type IPSecConnectionDeviceConfig
        """

        all_params = ['ipsc_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ip_sec_connection_device_config" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'ipsc_id' is set
        if ('ipsc_id' not in params) or (params['ipsc_id'] is None):
            raise ValueError("Missing the required parameter `ipsc_id` when calling `get_ip_sec_connection_device_config`")

        resource_path = '/ipsecConnections/{ipscId}/deviceConfig'
        path_params = {}
        if 'ipsc_id' in params:
            path_params['ipscId'] = params['ipsc_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='IPSecConnectionDeviceConfig')
        return response

    def get_ip_sec_connection_device_status(self, ipsc_id, **kwargs):
        """
        GetIPSecConnectionDeviceStatus
        Gets the status of the specified IPsec connection (whether it's up or down).

        :param str ipsc_id: The IPsec connection's OCID. (required)
        :return: A Response object with data of type IPSecConnectionDeviceStatus
        """

        all_params = ['ipsc_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ip_sec_connection_device_status" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'ipsc_id' is set
        if ('ipsc_id' not in params) or (params['ipsc_id'] is None):
            raise ValueError("Missing the required parameter `ipsc_id` when calling `get_ip_sec_connection_device_status`")

        resource_path = '/ipsecConnections/{ipscId}/deviceStatus'
        path_params = {}
        if 'ipsc_id' in params:
            path_params['ipscId'] = params['ipsc_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='IPSecConnectionDeviceStatus')
        return response

    def get_route_table(self, rt_id, **kwargs):
        """
        GetRouteTable
        Gets the specified route table's information.

        :param str rt_id: The route table's OCID. (required)
        :return: A Response object with data of type RouteTable
        """

        all_params = ['rt_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_route_table" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'rt_id' is set
        if ('rt_id' not in params) or (params['rt_id'] is None):
            raise ValueError("Missing the required parameter `rt_id` when calling `get_route_table`")

        resource_path = '/routeTables/{rtId}'
        path_params = {}
        if 'rt_id' in params:
            path_params['rtId'] = params['rt_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='RouteTable')
        return response

    def get_subnet(self, subnet_id, **kwargs):
        """
        GetSubnet
        Gets the specified subnet's information.

        :param str subnet_id: The subnet's OCID. (required)
        :return: A Response object with data of type Subnet
        """

        all_params = ['subnet_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subnet" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'subnet_id' is set
        if ('subnet_id' not in params) or (params['subnet_id'] is None):
            raise ValueError("Missing the required parameter `subnet_id` when calling `get_subnet`")

        resource_path = '/subnets/{subnetId}'
        path_params = {}
        if 'subnet_id' in params:
            path_params['subnetId'] = params['subnet_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Subnet')
        return response

    def get_vcn(self, vcn_id, **kwargs):
        """
        GetVcn
        Gets the specified VCN's information.

        :param str vcn_id: The VCN's OCID. (required)
        :return: A Response object with data of type Vcn
        """

        all_params = ['vcn_id']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_vcn" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'vcn_id' is set
        if ('vcn_id' not in params) or (params['vcn_id'] is None):
            raise ValueError("Missing the required parameter `vcn_id` when calling `get_vcn`")

        resource_path = '/vcns/{vcnId}'
        path_params = {}
        if 'vcn_id' in params:
            path_params['vcnId'] = params['vcn_id']

        query_params = {}

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='Vcn')
        return response

    def list_cpes(self, compartment_id, **kwargs):
        """
        ListCpes
        Gets a list of the Customer-Premise Equipment objects (CPEs) in the specified compartment.\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :return: A Response object with data of type list[Cpe]
        """

        all_params = ['compartment_id', 'limit', 'page']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_cpes" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_cpes`")

        resource_path = '/cpes'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[Cpe]')
        return response

    def list_drg_attachments(self, compartment_id, **kwargs):
        """
        ListDrgAttachments
        Gets a list of the `DrgAttachment`s for the specified compartment. You can optionally filter the\nresults by VCN or DRG.\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str vcn_id: The VCN's OCID.
        :param str drg_id: The DRG's OCID.
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :return: A Response object with data of type list[DrgAttachment]
        """

        all_params = ['compartment_id', 'vcn_id', 'drg_id', 'limit', 'page']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_drg_attachments" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_drg_attachments`")

        resource_path = '/drgAttachments'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'vcn_id' in params:
            query_params['vcnId'] = params['vcn_id']
        if 'drg_id' in params:
            query_params['drgId'] = params['drg_id']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[DrgAttachment]')
        return response

    def list_drgs(self, compartment_id, **kwargs):
        """
        ListDrgs
        Gets a list of the DRGs in the specified compartment.

        :param str compartment_id: The OCID of the compartment. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :return: A Response object with data of type list[Drg]
        """

        all_params = ['compartment_id', 'limit', 'page']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_drgs" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_drgs`")

        resource_path = '/drgs'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[Drg]')
        return response

    def list_internet_gateways(self, compartment_id, vcn, **kwargs):
        """
        ListInternetGateways
        Gets a list of the Internet Gateways in the specified VCN and the specified compartment.\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str vcn: The VCN's OCID. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :return: A Response object with data of type list[InternetGateway]
        """

        all_params = ['compartment_id', 'vcn', 'limit', 'page']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_internet_gateways" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_internet_gateways`")
        # verify the required parameter 'vcn' is set
        if ('vcn' not in params) or (params['vcn'] is None):
            raise ValueError("Missing the required parameter `vcn` when calling `list_internet_gateways`")

        resource_path = '/internetGateways'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'vcn' in params:
            query_params['vcn'] = params['vcn']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[InternetGateway]')
        return response

    def list_ip_sec_connections(self, compartment_id, **kwargs):
        """
        ListIPSecConnections
        Gets a list of the IPsec connections for the specified compartment. You can optionally filter the\nresults by DRG or CPE.\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str drg_id: The DRG's OCID.
        :param str cpe_id: The CPE's OCID.
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :return: A Response object with data of type list[IPSecConnection]
        """

        all_params = ['compartment_id', 'drg_id', 'cpe_id', 'limit', 'page']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_ip_sec_connections" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_ip_sec_connections`")

        resource_path = '/ipsecConnections'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'drg_id' in params:
            query_params['drgId'] = params['drg_id']
        if 'cpe_id' in params:
            query_params['cpeId'] = params['cpe_id']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[IPSecConnection]')
        return response

    def list_route_tables(self, compartment_id, vcn, **kwargs):
        """
        ListRouteTables
        Gets a list of the route tables in the specified VCN and specified compartment. The response\nincludes the default route table that automatically comes with each VCN, plus any route tables\nyou've created.\n

        :param str compartment_id: The OCID of the compartment. (required)
        :param str vcn: The VCN's OCID. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :return: A Response object with data of type list[RouteTable]
        """

        all_params = ['compartment_id', 'vcn', 'limit', 'page']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_route_tables" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_route_tables`")
        # verify the required parameter 'vcn' is set
        if ('vcn' not in params) or (params['vcn'] is None):
            raise ValueError("Missing the required parameter `vcn` when calling `list_route_tables`")

        resource_path = '/routeTables'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'vcn' in params:
            query_params['vcn'] = params['vcn']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[RouteTable]')
        return response

    def list_subnets(self, compartment_id, vcn, **kwargs):
        """
        ListSubnets
        Gets a list of the subnets in the specified VCN and the specified compartment.

        :param str compartment_id: The OCID of the compartment. (required)
        :param str vcn: The VCN's OCID. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :return: A Response object with data of type list[Subnet]
        """

        all_params = ['compartment_id', 'vcn', 'limit', 'page']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_subnets" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_subnets`")
        # verify the required parameter 'vcn' is set
        if ('vcn' not in params) or (params['vcn'] is None):
            raise ValueError("Missing the required parameter `vcn` when calling `list_subnets`")

        resource_path = '/subnets'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'vcn' in params:
            query_params['vcn'] = params['vcn']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[Subnet]')
        return response

    def list_vcns(self, compartment_id, **kwargs):
        """
        ListVcns
        Gets a list of the Virtual Cloud Networks (VCNs) in the specified compartment.

        :param str compartment_id: The OCID of the compartment. (required)
        :param int limit: The maximum number of items to return in a paginated \"List\" call. For information about pagination, see\n[List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :param str page: The value of the `opc-next-page` response header from the previous \"List\" call. For information about\npagination, see [List Pagination](../../../#API/Concepts/usingapi.htm#List_Pagination).\n
        :return: A Response object with data of type list[Vcn]
        """

        all_params = ['compartment_id', 'limit', 'page']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_vcns" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'compartment_id' is set
        if ('compartment_id' not in params) or (params['compartment_id'] is None):
            raise ValueError("Missing the required parameter `compartment_id` when calling `list_vcns`")

        resource_path = '/vcns'
        path_params = {}

        query_params = {}
        if 'compartment_id' in params:
            query_params['compartmentId'] = params['compartment_id']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        body_params = None

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='list[Vcn]')
        return response

    def update_internet_gateway(self, ig_id, update_internet_gateway_request, **kwargs):
        """
        UpdateInternetGateway
        Disables/enables the Internet Gateway.\n\nIf the gateway is disabled, that means no traffic will flow to/from the Internet even if there's\na route rule that enables that traffic.\n

        :param str ig_id: The Internet Gateway's OCID. (required)
        :param UpdateInternetGatewayRequest update_internet_gateway_request: Request object for updating the Internet Gateway. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type InternetGateway
        """

        all_params = ['ig_id', 'update_internet_gateway_request', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_internet_gateway" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'ig_id' is set
        if ('ig_id' not in params) or (params['ig_id'] is None):
            raise ValueError("Missing the required parameter `ig_id` when calling `update_internet_gateway`")
        # verify the required parameter 'update_internet_gateway_request' is set
        if ('update_internet_gateway_request' not in params) or (params['update_internet_gateway_request'] is None):
            raise ValueError("Missing the required parameter `update_internet_gateway_request` when calling `update_internet_gateway`")

        resource_path = '/internetGateways/{igId}'
        path_params = {}
        if 'ig_id' in params:
            path_params['igId'] = params['ig_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_internet_gateway_request' in params:
            body_params = params['update_internet_gateway_request']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='InternetGateway')
        return response

    def update_route_table(self, rt_id, update_route_table_request, **kwargs):
        """
        UpdateRouteTable
        Updates the specified route table's rules.\n\nWhen updating the route table, the new `RouteRules` object you provide replaces the entire\nexisting set of rules.\n

        :param str rt_id: The route table's OCID. (required)
        :param UpdateRouteTableRequest update_route_table_request: Request object for updating a route table. (required)
        :param str if_match: For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`\nparameter to the value of the etag from a previous GET or POST response for that resource.  The resource\nwill be updated or deleted only if the etag you provide matches the resource's current etag value.\n
        :return: A Response object with data of type RouteTable
        """

        all_params = ['rt_id', 'update_route_table_request', 'if_match']

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_route_table" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'rt_id' is set
        if ('rt_id' not in params) or (params['rt_id'] is None):
            raise ValueError("Missing the required parameter `rt_id` when calling `update_route_table`")
        # verify the required parameter 'update_route_table_request' is set
        if ('update_route_table_request' not in params) or (params['update_route_table_request'] is None):
            raise ValueError("Missing the required parameter `update_route_table_request` when calling `update_route_table`")

        resource_path = '/routeTables/{rtId}'
        path_params = {}
        if 'rt_id' in params:
            path_params['rtId'] = params['rt_id']

        query_params = {}

        header_params = {}
        if 'if_match' in params:
            header_params['if-match'] = params['if_match']

        body_params = None
        if 'update_route_table_request' in params:
            body_params = params['update_route_table_request']

        header_params['accept'] = 'application/json'
        header_params['content-type'] = 'application/json'

        response = self.api_client.call_api(self.api_client.config.endpoint_vcn_service_api,
                                            resource_path,
                                            'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            response_type='RouteTable')
        return response
