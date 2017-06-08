# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from __future__ import absolute_import

import six

from ..base_client import BaseClient
from ..config import get_config_value_or_default, validate_config
from ..signer import Signer
from ..util import Sentinel
from .models import core_type_mapping
missing = Sentinel("Missing")


class VirtualNetworkClient(object):

    def __init__(self, config):
        validate_config(config)
        signer = Signer(
            tenancy=config["tenancy"],
            user=config["user"],
            fingerprint=config["fingerprint"],
            private_key_file_location=config["key_file"],
            pass_phrase=get_config_value_or_default(config, "pass_phrase")
        )
        self.base_client = BaseClient("virtual_network", config, signer, core_type_mapping)

    def create_cpe(self, create_cpe_details, **kwargs):
        """
        CreateCpe
        Creates a new virtual Customer-Premises Equipment (CPE) object in the specified compartment. For
        more information, see `Managing IPSec VPNs`__.

        For the purposes of access control, you must provide the OCID of the compartment where you want
        the CPE to reside. Notice that the CPE doesn't have to be in the same compartment as the IPSec
        connection or other Networking Service components. If you're not sure which compartment to
        use, put the CPE in the same compartment as the DRG. For more information about
        compartments and access control, see `Overview of the IAM Service`__.
        For information about OCIDs, see `Resource Identifiers`__.

        You must provide the public IP address of your on-premise router. See
        `Configuring Your On-Premise Router`__.

        You may optionally specify a *display name* for the CPE, otherwise a default is provided. It does not have to
        be unique, and you can change it.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingIPsec.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/configuringCPE.htm


        :param CreateCpeDetails create_cpe_details: (required)
            Details for creating a CPE.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type Cpe
        :rtype: Cpe
        """
        resource_path = "/cpes"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_cpe got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_cpe_details,
            response_type="Cpe")

    def create_cross_connect(self, create_cross_connect_details, **kwargs):
        """
        CreateCrossConnect
        Creates a new cross-connect. Oracle recommends you create each cross-connect in a
        :class:`CrossConnectGroup` so you can use link aggregation
        with the connection.

        After creating the `CrossConnect` object, you need to go the FastConnect location
        and request to have the physical cable installed. For more information, see
        `FastConnect Overview`__.

        For the purposes of access control, you must provide the OCID of the
        compartment where you want the cross-connect to reside. If you're
        not sure which compartment to use, put the cross-connect in the
        same compartment with your VCN. For more information about
        compartments and access control, see
        `Overview of the IAM Service`__.
        For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the cross-connect.
        It does not have to be unique, and you can change it.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/fastconnect.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param CreateCrossConnectDetails create_cross_connect_details: (required)
            Details to create a CrossConnect

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type CrossConnect
        :rtype: CrossConnect
        """
        resource_path = "/crossConnects"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_cross_connect got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_cross_connect_details,
            response_type="CrossConnect")

    def create_cross_connect_group(self, create_cross_connect_group_details, **kwargs):
        """
        CreateCrossConnectGroup
        Creates a new cross-connect group to use with Oracle Bare Metal Cloud Services
        FastConnect. For more information, see
        `FastConnect Overview`__.

        For the purposes of access control, you must provide the OCID of the
        compartment where you want the cross-connect group to reside. If you're
        not sure which compartment to use, put the cross-connect group in the
        same compartment with your VCN. For more information about
        compartments and access control, see
        `Overview of the IAM Service`__.
        For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the cross-connect group.
        It does not have to be unique, and you can change it.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/fastconnect.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param CreateCrossConnectGroupDetails create_cross_connect_group_details: (required)
            Details to create a CrossConnectGroup

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type CrossConnectGroup
        :rtype: CrossConnectGroup
        """
        resource_path = "/crossConnectGroups"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_cross_connect_group got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_cross_connect_group_details,
            response_type="CrossConnectGroup")

    def create_dhcp_options(self, create_dhcp_details, **kwargs):
        """
        CreateDhcpOptions
        Creates a new set of DHCP options for the specified VCN. For more information, see
        :class:`DhcpOptions`.

        For the purposes of access control, you must provide the OCID of the compartment where you want the set of
        DHCP options to reside. Notice that the set of options doesn't have to be in the same compartment as the VCN,
        subnets, or other Networking Service components. If you're not sure which compartment to use, put the set
        of DHCP options in the same compartment as the VCN. For more information about compartments and access control, see
        `Overview of the IAM Service`__. For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the set of DHCP options, otherwise a default is provided.
        It does not have to be unique, and you can change it.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param CreateDhcpDetails create_dhcp_details: (required)
            Request object for creating a new set of DHCP options.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type DhcpOptions
        :rtype: DhcpOptions
        """
        resource_path = "/dhcps"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_dhcp_details,
            response_type="DhcpOptions")

    def create_drg(self, create_drg_details, **kwargs):
        """
        CreateDrg
        Creates a new Dynamic Routing Gateway (DRG) in the specified compartment. For more information,
        see `Managing Dynamic Routing Gateways (DRGs)`__.

        For the purposes of access control, you must provide the OCID of the compartment where you want
        the DRG to reside. Notice that the DRG doesn't have to be in the same compartment as the VCN,
        the DRG attachment, or other Networking Service components. If you're not sure which compartment
        to use, put the DRG in the same compartment as the VCN. For more information about compartments
        and access control, see `Overview of the IAM Service`__.
        For information about OCIDs, see `Resource Identifiers`__.

        You may optionally specify a *display name* for the DRG, otherwise a default is provided.
        It does not have to be unique, and you can change it.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingDRGs.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param CreateDrgDetails create_drg_details: (required)
            Details for creating a DRG.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type Drg
        :rtype: Drg
        """
        resource_path = "/drgs"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_drg got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_drg_details,
            response_type="Drg")

    def create_drg_attachment(self, create_drg_attachment_details, **kwargs):
        """
        CreateDrgAttachment
        Attaches the specified DRG to the specified VCN. A VCN can be attached to only one DRG at a time,
        and vice versa. The response includes a `DrgAttachment` object with its own OCID. For more
        information about DRGs, see
        `Managing Dynamic Routing Gateways (DRGs)`__.

        You may optionally specify a *display name* for the attachment, otherwise a default is provided.
        It does not have to be unique, and you can change it.

        For the purposes of access control, the DRG attachment is automatically placed into the same compartment
        as the VCN. For more information about compartments and access control, see
        `Overview of the IAM Service`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingDRGs.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm


        :param CreateDrgAttachmentDetails create_drg_attachment_details: (required)
            Details for creating a `DrgAttachment`.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type DrgAttachment
        :rtype: DrgAttachment
        """
        resource_path = "/drgAttachments"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_drg_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_drg_attachment_details,
            response_type="DrgAttachment")

    def create_internet_gateway(self, create_internet_gateway_details, **kwargs):
        """
        CreateInternetGateway
        Creates a new Internet Gateway for the specified VCN. For more information, see
        `Managing Internet Gateways`__.

        For the purposes of access control, you must provide the OCID of the compartment where you want the Internet
        Gateway to reside. Notice that the Internet Gateway doesn't have to be in the same compartment as the VCN or
        other Networking Service components. If you're not sure which compartment to use, put the Internet
        Gateway in the same compartment with the VCN. For more information about compartments and access control, see
        `Overview of the IAM Service`__. For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the Internet Gateway, otherwise a default is provided. It
        does not have to be unique, and you can change it.

        For traffic to flow between a subnet and an Internet Gateway, you must create a route rule accordingly in
        the subnet's route table (e.g., 0.0.0.0/0 > Internet Gateway). See
        :func:`update_route_table`.

        You must specify whether the Internet Gateway is enabled when you create it. If it's disabled, that means no
        traffic will flow to/from the internet even if there's a route rule that enables that traffic. You can later
        use :func:`update_internet_gateway` to easily disable/enable
        the gateway without changing the route rule.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingIGs.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param CreateInternetGatewayDetails create_internet_gateway_details: (required)
            Details for creating a new Internet Gateway.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type InternetGateway
        :rtype: InternetGateway
        """
        resource_path = "/internetGateways"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_internet_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_internet_gateway_details,
            response_type="InternetGateway")

    def create_ip_sec_connection(self, create_ip_sec_connection_details, **kwargs):
        """
        CreateIPSecConnection
        Creates a new IPSec connection between the specified DRG and CPE. For more information, see
        `Managing IPSec Connections`__.

        In the request, you must include at least one static route to the CPE object (you're allowed a maximum
        of 10). For example: 10.0.8.0/16.

        For the purposes of access control, you must provide the OCID of the compartment where you want the
        IPSec connection to reside. Notice that the IPSec connection doesn't have to be in the same compartment
        as the DRG, CPE, or other Networking Service components. If you're not sure which compartment to
        use, put the IPSec connection in the same compartment as the DRG. For more information about
        compartments and access control, see
        `Overview of the IAM Service`__.
        For information about OCIDs, see `Resource Identifiers`__.

        You may optionally specify a *display name* for the IPSec connection, otherwise a default is provided.
        It does not have to be unique, and you can change it.

        After creating the IPSec connection, you need to configure your on-premise router
        with tunnel-specific information returned by
        :func:`get_ip_sec_connection_device_config`.
        For each tunnel, that operation gives you the IP address of Oracle's VPN headend and the shared secret
        (i.e., the pre-shared key). For more information, see
        `Configuring Your On-Premise Router`__.

        To get the status of the tunnels (whether they're up or down), use
        :func:`get_ip_sec_connection_device_status`.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingIPsec.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/configuringCPE.htm


        :param CreateIPSecConnectionDetails create_ip_sec_connection_details: (required)
            Details for creating an `IPSecConnection`.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type IPSecConnection
        :rtype: IPSecConnection
        """
        resource_path = "/ipsecConnections"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_ip_sec_connection got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_ip_sec_connection_details,
            response_type="IPSecConnection")

    def create_route_table(self, create_route_table_details, **kwargs):
        """
        CreateRouteTable
        Creates a new route table for the specified VCN. In the request you must also include at least one route
        rule for the new route table. For information on the number of rules you can have in a route table, see
        `Service Limits`__. For general information about route
        tables in your VCN, see `Managing Route Tables`__.

        For the purposes of access control, you must provide the OCID of the compartment where you want the route
        table to reside. Notice that the route table doesn't have to be in the same compartment as the VCN, subnets,
        or other Networking Service components. If you're not sure which compartment to use, put the route
        table in the same compartment as the VCN. For more information about compartments and access control, see
        `Overview of the IAM Service`__. For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the route table, otherwise a default is provided.
        It does not have to be unique, and you can change it.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/servicelimits.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingroutetables.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param CreateRouteTableDetails create_route_table_details: (required)
            Details for creating a new route table.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type RouteTable
        :rtype: RouteTable
        """
        resource_path = "/routeTables"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_route_table got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_route_table_details,
            response_type="RouteTable")

    def create_security_list(self, create_security_list_details, **kwargs):
        """
        CreateSecurityList
        Creates a new security list for the specified VCN. For more information
        about security lists, see `Security Lists`__.
        For information on the number of rules you can have in a security list, see
        `Service Limits`__.

        For the purposes of access control, you must provide the OCID of the compartment where you want the security
        list to reside. Notice that the security list doesn't have to be in the same compartment as the VCN, subnets,
        or other Networking Service components. If you're not sure which compartment to use, put the security
        list in the same compartment as the VCN. For more information about compartments and access control, see
        `Overview of the IAM Service`__. For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the security list, otherwise a default is provided.
        It does not have to be unique, and you can change it.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/securitylists.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/servicelimits.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param CreateSecurityListDetails create_security_list_details: (required)
            Details regarding the security list to create.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type SecurityList
        :rtype: SecurityList
        """
        resource_path = "/securityLists"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_security_list got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_security_list_details,
            response_type="SecurityList")

    def create_subnet(self, create_subnet_details, **kwargs):
        """
        CreateSubnet
        Creates a new subnet in the specified VCN. You can't change the size of the subnet after creation,
        so it's important to think about the size of subnets you need before creating them.
        For more information, see `Managing Subnets`__.
        For information on the number of subnets you can have in a VCN, see
        `Service Limits`__.

        For the purposes of access control, you must provide the OCID of the compartment where you want the subnet
        to reside. Notice that the subnet doesn't have to be in the same compartment as the VCN, route tables, or
        other Networking Service components. If you're not sure which compartment to use, put the subnet in
        the same compartment as the VCN. For more information about compartments and access control, see
        `Overview of the IAM Service`__. For information about OCIDs,
        see `Resource Identifiers`__.

        You may optionally associate a route table with the subnet. If you don't, the subnet will use the
        VCN's default route table. For more information about route tables, see
        `Managing Route Tables`__.

        You may optionally associate a security list with the subnet. If you don't, the subnet will use the
        VCN's default security list. For more information about security lists, see
        `Security Lists`__.

        You may optionally associate a set of DHCP options with the subnet. If you don't, the subnet will use the
        VCN's default set. For more information about DHCP options, see
        `Managing DHCP Options`__.

        You may optionally specify a *display name* for the subnet, otherwise a default is provided.
        It does not have to be unique, and you can change it.

        You can also add a DNS label for the subnet, which is required if you want the Internet and
        VCN Resolver to resolve hostnames for instances in the subnet. For more information, see
        `DNS in Your Virtual Cloud Network`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingsubnets.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/servicelimits.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingroutetables.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/securitylists.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingDHCP.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :param CreateSubnetDetails create_subnet_details: (required)
            Details for creating a subnet.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type Subnet
        :rtype: Subnet
        """
        resource_path = "/subnets"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_subnet got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_subnet_details,
            response_type="Subnet")

    def create_vcn(self, create_vcn_details, **kwargs):
        """
        CreateVcn
        Creates a new Virtual Cloud Network (VCN). For more information, see
        `Managing Virtual Cloud Networks (VCNs)`__.

        For the VCN you must specify a single, contiguous IPv4 CIDR block in the private IP address ranges specified in
        `RFC 1918`__ (10.0.0.0/8, 172.16/12, and 192.168/16). Example: 172.16.0.0/16.
        The CIDR block can range from /16 to /30, and it must not overlap with your on-premise network. You can't
        change the size of the VCN after creation.

        For the purposes of access control, you must provide the OCID of the compartment where you want the VCN to
        reside. Consult an Oracle Bare Metal Cloud Services administrator in your organization if you're not sure which
        compartment to use. Notice that the VCN doesn't have to be in the same compartment as the subnets or other
        Networking Service components. For more information about compartments and access control, see
        `Overview of the IAM Service`__. For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the VCN, otherwise a default is provided. It does not have to
        be unique, and you can change it.

        You can also add a DNS label for the VCN, which is required if you want the instances to use the
        Interent and VCN Resolver option for DNS in the VCN. For more information, see
        `DNS in Your Virtual Cloud Network`__.

        The VCN automatically comes with a default route table, default security list, and default set of DHCP options.
        The OCID for each is returned in the response. You can't delete these default objects, but you can change their
        contents (i.e., route rules, etc.)

        The VCN and subnets you create are not accessible until you attach an Internet Gateway or set up an IPSec VPN
        or FastConnect. For more information, see
        `Overview of the Networking Service`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingVCNs.htm
        __ https://tools.ietf.org/html/rfc1918
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/overview.htm


        :param CreateVcnDetails create_vcn_details: (required)
            Details for creating a new VCN.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type Vcn
        :rtype: Vcn
        """
        resource_path = "/vcns"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_vcn got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_vcn_details,
            response_type="Vcn")

    def create_virtual_circuit(self, create_virtual_circuit_details, **kwargs):
        """
        CreateVirtualCircuit
        Creates a new virtual circuit to use with Oracle Bare Metal Cloud
        Services FastConnect. For more information, see
        `FastConnect Overview`__.

        For the purposes of access control, you must provide the OCID of the
        compartment where you want the virtual circuit to reside. If you're
        not sure which compartment to use, put the virtual circuit in the
        same compartment with the DRG it's using. For more information about
        compartments and access control, see
        `Overview of the IAM Service`__.
        For information about OCIDs, see
        `Resource Identifiers`__.

        You may optionally specify a *display name* for the virtual circuit.
        It does not have to be unique, and you can change it.

        **Important:** When creating a virtual circuit, you specify a DRG for
        the traffic to flow through. Make sure you attach the DRG to your
        VCN and confirm the VCN's routing sends traffic to the DRG. Otherwise
        traffic will not flow. For more information, see
        `Managing Route Tables`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/fastconnect.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/overview.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm
        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Tasks/managingroutetables.htm


        :param CreateVirtualCircuitDetails create_virtual_circuit_details: (required)
            Details to create a VirtualCircuit.

        :param str opc_retry_token: (optional)
            A token that uniquely identifies a request so it can be retried in case of a timeout or
            server error without risk of executing that same action again. Retry tokens expire after 24
            hours, but can be invalidated before then due to conflicting operations (e.g., if a resource
            has been deleted and purged from the system, then a retry of the original creation request
            may be rejected).

        :return: A Response object with data of type VirtualCircuit
        :rtype: VirtualCircuit
        """
        resource_path = "/virtualCircuits"
        method = "POST"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "opc_retry_token"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "create_virtual_circuit got unknown kwargs: {!r}".format(extra_kwargs))

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "opc-retry-token": kwargs.get("opc_retry_token", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            header_params=header_params,
            body=create_virtual_circuit_details,
            response_type="VirtualCircuit")

    def delete_cpe(self, cpe_id, **kwargs):
        """
        DeleteCpe
        Deletes the specified CPE object. The CPE must not be connected to a DRG. This is an asynchronous
        operation; the CPE's `lifecycleState` will change to TERMINATING temporarily until the CPE is completely
        removed.


        :param str cpe_id: (required)
            The OCID of the CPE.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/cpes/{cpeId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_cpe got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "cpeId": cpe_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_cross_connect(self, cross_connect_id, **kwargs):
        """
        DeleteCrossConnect
        Deletes the specified cross-connect. It must not be mapped to a
        :class:`VirtualCircuit`.


        :param str cross_connect_id: (required)
            The OCID of the cross-connect.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/crossConnects/{crossConnectId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_cross_connect got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectId": cross_connect_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_cross_connect_group(self, cross_connect_group_id, **kwargs):
        """
        DeleteCrossConnectGroup
        Deletes the specified cross-connect group. It must not contain any
        cross-connects, and it cannot be mapped to a
        :class:`VirtualCircuit`.


        :param str cross_connect_group_id: (required)
            The OCID of the cross-connect group.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/crossConnectGroups/{crossConnectGroupId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_cross_connect_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectGroupId": cross_connect_group_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_dhcp_options(self, dhcp_id, **kwargs):
        """
        DeleteDhcpOptions
        Deletes the specified set of DHCP options, but only if it's not associated with a subnet. You can't delete a
        VCN's default set of DHCP options.

        This is an asynchronous operation; the state of the set of options will switch to TERMINATING temporarily
        until the set is completely removed.


        :param str dhcp_id: (required)
            The OCID for the set of DHCP options.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/dhcps/{dhcpId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dhcpId": dhcp_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_drg(self, drg_id, **kwargs):
        """
        DeleteDrg
        Deletes the specified DRG. The DRG must not be attached to a VCN or be connected to your on-premise
        network. Also, there must not be a route table that lists the DRG as a target. This is an asynchronous
        operation; the DRG's `lifecycleState` will change to TERMINATING temporarily until the DRG is completely
        removed.


        :param str drg_id: (required)
            The OCID of the DRG.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/drgs/{drgId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_drg got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgId": drg_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_drg_attachment(self, drg_attachment_id, **kwargs):
        """
        DeleteDrgAttachment
        Detaches a DRG from a VCN by deleting the corresponding `DrgAttachment`. This is an asynchronous
        operation; the attachment's `lifecycleState` will change to DETACHING temporarily until the attachment
        is completely removed.


        :param str drg_attachment_id: (required)
            The OCID of the DRG attachment.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/drgAttachments/{drgAttachmentId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_drg_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgAttachmentId": drg_attachment_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_internet_gateway(self, ig_id, **kwargs):
        """
        DeleteInternetGateway
        Deletes the specified Internet Gateway. The Internet Gateway does not have to be disabled, but
        there must not be a route table that lists it as a target.

        This is an asynchronous operation; the gateway's `lifecycleState` will change to TERMINATING temporarily
        until the gateway is completely removed.


        :param str ig_id: (required)
            The OCID of the Internet Gateway.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/internetGateways/{igId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_internet_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "igId": ig_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_ip_sec_connection(self, ipsc_id, **kwargs):
        """
        DeleteIPSecConnection
        Deletes the specified IPSec connection. If your goal is to disable the IPSec VPN between your VCN and
        on-premise network, it's easiest to simply detach the DRG but keep all the IPSec VPN components intact.
        If you were to delete all the components and then later need to create an IPSec VPN again, you would
        need to configure your on-premise router again with the new information returned from
        :func:`create_ip_sec_connection`.

        This is an asynchronous operation; the connection's `lifecycleState` will change to TERMINATING temporarily
        until the connection is completely removed.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/ipsecConnections/{ipscId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_ip_sec_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_route_table(self, rt_id, **kwargs):
        """
        DeleteRouteTable
        Deletes the specified route table, but only if it's not associated with a subnet. You can't delete a
        VCN's default route table.

        This is an asynchronous operation; the route table's `lifecycleState` will change to TERMINATING temporarily
        until the route table is completely removed.


        :param str rt_id: (required)
            The OCID of the route table.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/routeTables/{rtId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_route_table got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "rtId": rt_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_security_list(self, security_list_id, **kwargs):
        """
        DeleteSecurityList
        Deletes the specified security list, but only if it's not associated with a subnet. You can't delete
        a VCN's default security list.

        This is an asynchronous operation; the security list's `lifecycleState` will change to TERMINATING temporarily
        until the security list is completely removed.


        :param str security_list_id: (required)
            The OCID of the security list.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/securityLists/{securityListId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_security_list got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "securityListId": security_list_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_subnet(self, subnet_id, **kwargs):
        """
        DeleteSubnet
        Deletes the specified subnet, but only if there are no instances in the subnet. This is an asynchronous
        operation; the subnet's `lifecycleState` will change to TERMINATING temporarily. If there are any
        instances in the subnet, the state will instead change back to AVAILABLE.


        :param str subnet_id: (required)
            The OCID of the subnet.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/subnets/{subnetId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_subnet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subnetId": subnet_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_vcn(self, vcn_id, **kwargs):
        """
        DeleteVcn
        Deletes the specified VCN. The VCN must be empty and have no attached gateways. This is an asynchronous
        operation; the VCN's `lifecycleState` will change to TERMINATING temporarily until the VCN is completely
        removed.


        :param str vcn_id: (required)
            The OCID of the VCN.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/vcns/{vcnId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_vcn got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vcnId": vcn_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def delete_virtual_circuit(self, virtual_circuit_id, **kwargs):
        """
        DeleteVirtualCircuit
        Deletes the specified virtual circuit.

        **Important:** If you're using FastConnect via a provider,
        make sure to also terminate the connection with
        the provider, or else the provider may continue to bill you.


        :param str virtual_circuit_id: (required)
            The OCID of the virtual circuit.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type None
        :rtype: None
        """
        resource_path = "/virtualCircuits/{virtualCircuitId}"
        method = "DELETE"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "delete_virtual_circuit got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "virtualCircuitId": virtual_circuit_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params)

    def get_cpe(self, cpe_id, **kwargs):
        """
        GetCpe
        Gets the specified CPE's information.


        :param str cpe_id: (required)
            The OCID of the CPE.

        :return: A Response object with data of type Cpe
        :rtype: Cpe
        """
        resource_path = "/cpes/{cpeId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_cpe got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "cpeId": cpe_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Cpe")

    def get_cross_connect(self, cross_connect_id, **kwargs):
        """
        GetCrossConnect
        Gets the specified cross-connect's information.


        :param str cross_connect_id: (required)
            The OCID of the cross-connect.

        :return: A Response object with data of type CrossConnect
        :rtype: CrossConnect
        """
        resource_path = "/crossConnects/{crossConnectId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_cross_connect got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "crossConnectId": cross_connect_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="CrossConnect")

    def get_cross_connect_group(self, cross_connect_group_id, **kwargs):
        """
        GetCrossConnectGroups
        Gets the specified cross-connect group's information.


        :param str cross_connect_group_id: (required)
            The OCID of the cross-connect group.

        :return: A Response object with data of type CrossConnectGroup
        :rtype: CrossConnectGroup
        """
        resource_path = "/crossConnectGroups/{crossConnectGroupId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_cross_connect_group got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "crossConnectGroupId": cross_connect_group_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="CrossConnectGroup")

    def get_cross_connect_letter_of_authority(self, cross_connect_id, **kwargs):
        """
        GetCrossConnectLetterOfAuthority
        Gets the Letter of Authority for the specified cross-connect.


        :param str cross_connect_id: (required)
            The OCID of the cross-connect.

        :return: A Response object with data of type LetterOfAuthority
        :rtype: LetterOfAuthority
        """
        resource_path = "/crossConnects/{crossConnectId}/letterOfAuthority"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_cross_connect_letter_of_authority got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "crossConnectId": cross_connect_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="LetterOfAuthority")

    def get_cross_connect_status(self, cross_connect_id, **kwargs):
        """
        GetCrossConnectStatus
        Gets the status of the specified cross-connect.


        :param str cross_connect_id: (required)
            The OCID of the cross-connect.

        :return: A Response object with data of type CrossConnectStatus
        :rtype: CrossConnectStatus
        """
        resource_path = "/crossConnects/{crossConnectId}/status"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_cross_connect_status got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "crossConnectId": cross_connect_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="CrossConnectStatus")

    def get_dhcp_options(self, dhcp_id, **kwargs):
        """
        GetDhcpOptions
        Gets the specified set of DHCP options.


        :param str dhcp_id: (required)
            The OCID for the set of DHCP options.

        :return: A Response object with data of type DhcpOptions
        :rtype: DhcpOptions
        """
        resource_path = "/dhcps/{dhcpId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_dhcp_options got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "dhcpId": dhcp_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="DhcpOptions")

    def get_drg(self, drg_id, **kwargs):
        """
        GetDrg
        Gets the specified DRG's information.


        :param str drg_id: (required)
            The OCID of the DRG.

        :return: A Response object with data of type Drg
        :rtype: Drg
        """
        resource_path = "/drgs/{drgId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_drg got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "drgId": drg_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Drg")

    def get_drg_attachment(self, drg_attachment_id, **kwargs):
        """
        GetDrgAttachment
        Gets the information for the specified `DrgAttachment`.


        :param str drg_attachment_id: (required)
            The OCID of the DRG attachment.

        :return: A Response object with data of type DrgAttachment
        :rtype: DrgAttachment
        """
        resource_path = "/drgAttachments/{drgAttachmentId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_drg_attachment got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "drgAttachmentId": drg_attachment_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="DrgAttachment")

    def get_internet_gateway(self, ig_id, **kwargs):
        """
        GetInternetGateway
        Gets the specified Internet Gateway's information.


        :param str ig_id: (required)
            The OCID of the Internet Gateway.

        :return: A Response object with data of type InternetGateway
        :rtype: InternetGateway
        """
        resource_path = "/internetGateways/{igId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_internet_gateway got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "igId": ig_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="InternetGateway")

    def get_ip_sec_connection(self, ipsc_id, **kwargs):
        """
        GetIPSecConnection
        Gets the specified IPSec connection's basic information, including the static routes for the
        on-premise router. If you want the status of the connection (whether it's up or down), use
        :func:`get_ip_sec_connection_device_status`.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :return: A Response object with data of type IPSecConnection
        :rtype: IPSecConnection
        """
        resource_path = "/ipsecConnections/{ipscId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_ip_sec_connection got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "ipscId": ipsc_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="IPSecConnection")

    def get_ip_sec_connection_device_config(self, ipsc_id, **kwargs):
        """
        GetIPSecConnectionDeviceConfig
        Gets the configuration information for the specified IPSec connection. For each tunnel, the
        response includes the IP address of Oracle's VPN headend and the shared secret.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :return: A Response object with data of type IPSecConnectionDeviceConfig
        :rtype: IPSecConnectionDeviceConfig
        """
        resource_path = "/ipsecConnections/{ipscId}/deviceConfig"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_ip_sec_connection_device_config got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "ipscId": ipsc_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="IPSecConnectionDeviceConfig")

    def get_ip_sec_connection_device_status(self, ipsc_id, **kwargs):
        """
        GetIPSecConnectionDeviceStatus
        Gets the status of the specified IPSec connection (whether it's up or down).


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :return: A Response object with data of type IPSecConnectionDeviceStatus
        :rtype: IPSecConnectionDeviceStatus
        """
        resource_path = "/ipsecConnections/{ipscId}/deviceStatus"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_ip_sec_connection_device_status got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "ipscId": ipsc_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="IPSecConnectionDeviceStatus")

    def get_route_table(self, rt_id, **kwargs):
        """
        GetRouteTable
        Gets the specified route table's information.


        :param str rt_id: (required)
            The OCID of the route table.

        :return: A Response object with data of type RouteTable
        :rtype: RouteTable
        """
        resource_path = "/routeTables/{rtId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_route_table got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "rtId": rt_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="RouteTable")

    def get_security_list(self, security_list_id, **kwargs):
        """
        GetSecurityList
        Gets the specified security list's information.


        :param str security_list_id: (required)
            The OCID of the security list.

        :return: A Response object with data of type SecurityList
        :rtype: SecurityList
        """
        resource_path = "/securityLists/{securityListId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_security_list got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "securityListId": security_list_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="SecurityList")

    def get_subnet(self, subnet_id, **kwargs):
        """
        GetSubnet
        Gets the specified subnet's information.


        :param str subnet_id: (required)
            The OCID of the subnet.

        :return: A Response object with data of type Subnet
        :rtype: Subnet
        """
        resource_path = "/subnets/{subnetId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_subnet got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "subnetId": subnet_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Subnet")

    def get_vcn(self, vcn_id, **kwargs):
        """
        GetVcn
        Gets the specified VCN's information.


        :param str vcn_id: (required)
            The OCID of the VCN.

        :return: A Response object with data of type Vcn
        :rtype: Vcn
        """
        resource_path = "/vcns/{vcnId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_vcn got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "vcnId": vcn_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Vcn")

    def get_virtual_circuit(self, virtual_circuit_id, **kwargs):
        """
        GetVirtualCircuit
        Gets the specified virtual circuit's information.


        :param str virtual_circuit_id: (required)
            The OCID of the virtual circuit.

        :return: A Response object with data of type VirtualCircuit
        :rtype: VirtualCircuit
        """
        resource_path = "/virtualCircuits/{virtualCircuitId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_virtual_circuit got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "virtualCircuitId": virtual_circuit_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="VirtualCircuit")

    def get_vnic(self, vnic_id, **kwargs):
        """
        GetVnic
        Gets the information for the specified Virtual Network Interface Card (VNIC), including
        the IP addresses. You can get the instance's VNIC OCID from the
        :func:`list_vnic_attachments` operation.


        :param str vnic_id: (required)
            The OCID of the VNIC.

        :return: A Response object with data of type Vnic
        :rtype: Vnic
        """
        resource_path = "/vnics/{vnicId}"
        method = "GET"

        if kwargs:
            raise ValueError(
                "get_vnic got unknown kwargs: {!r}".format(kwargs))

        path_params = {
            "vnicId": vnic_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            response_type="Vnic")

    def list_cpes(self, compartment_id, **kwargs):
        """
        ListCpes
        Lists the Customer-Premises Equipment objects (CPEs) in the specified compartment.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[Cpe]
        :rtype: list[Cpe]
        """
        resource_path = "/cpes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_cpes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Cpe]")

    def list_cross_connect_groups(self, compartment_id, **kwargs):
        """
        ListCrossConnectGroups
        Lists the cross-connect groups in the specified compartment.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[CrossConnectGroup]
        :rtype: list[CrossConnectGroup]
        """
        resource_path = "/crossConnectGroups"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_cross_connect_groups got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[CrossConnectGroup]")

    def list_cross_connect_locations(self, compartment_id, **kwargs):
        """
        ListCrossConnectLocations
        Lists the available FastConnect locations for cross-connect installation. You need
        this information so you can specify your desired location when you create a cross-connect.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[CrossConnectLocation]
        :rtype: list[CrossConnectLocation]
        """
        resource_path = "/crossConnectLocations"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_cross_connect_locations got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[CrossConnectLocation]")

    def list_cross_connects(self, compartment_id, **kwargs):
        """
        ListCrossConnects
        Lists the cross-connects in the specified compartment. You can filter the list
        by specifying the OCID of a cross-connect group.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str cross_connect_group_id: (optional)
            The OCID of the cross-connect group.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[CrossConnect]
        :rtype: list[CrossConnect]
        """
        resource_path = "/crossConnects"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "cross_connect_group_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_cross_connects got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "crossConnectGroupId": kwargs.get("cross_connect_group_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[CrossConnect]")

    def list_crossconnect_port_speed_shapes(self, compartment_id, **kwargs):
        """
        ListCrossConnectPortSpeedShapes
        Lists the available port speeds for cross-connects. You need this information
        so you can specify your desired port speed (i.e., shape) when you create a
        cross-connect.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[CrossConnectPortSpeedShape]
        :rtype: list[CrossConnectPortSpeedShape]
        """
        resource_path = "/crossConnectPortSpeedShapes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_crossconnect_port_speed_shapes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[CrossConnectPortSpeedShape]")

    def list_dhcp_options(self, compartment_id, vcn_id, **kwargs):
        """
        ListDhcpOptions
        Lists the sets of DHCP options in the specified VCN and specified compartment.
        The response includes the default set of options that automatically comes with each VCN,
        plus any other sets you've created.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str vcn_id: (required)
            The OCID of the VCN.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[DhcpOptions]
        :rtype: list[DhcpOptions]
        """
        resource_path = "/dhcps"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "vcnId": vcn_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[DhcpOptions]")

    def list_drg_attachments(self, compartment_id, **kwargs):
        """
        ListDrgAttachments
        Lists the `DrgAttachment` objects for the specified compartment. You can filter the
        results by VCN or DRG.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str vcn_id: (optional)
            The OCID of the VCN.

        :param str drg_id: (optional)
            The OCID of the DRG.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[DrgAttachment]
        :rtype: list[DrgAttachment]
        """
        resource_path = "/drgAttachments"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "vcn_id",
            "drg_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_drg_attachments got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "vcnId": kwargs.get("vcn_id", missing),
            "drgId": kwargs.get("drg_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[DrgAttachment]")

    def list_drgs(self, compartment_id, **kwargs):
        """
        ListDrgs
        Lists the DRGs in the specified compartment.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[Drg]
        :rtype: list[Drg]
        """
        resource_path = "/drgs"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_drgs got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Drg]")

    def list_fast_connect_provider_services(self, compartment_id, **kwargs):
        """
        ListFastConnectProviderServices
        Lists the service offerings from supported providers. You need this
        information so you can specify your desired provider and service
        offering when you create a virtual circuit.

        For the compartment ID, provide the OCID of your tenancy (the root compartment).

        For more information, see `FastConnect Overview`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/fastconnect.htm


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[FastConnectProviderService]
        :rtype: list[FastConnectProviderService]
        """
        resource_path = "/fastConnectProviderServices"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_fast_connect_provider_services got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[FastConnectProviderService]")

    def list_internet_gateways(self, compartment_id, vcn_id, **kwargs):
        """
        ListInternetGateways
        Lists the Internet Gateways in the specified VCN and the specified compartment.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str vcn_id: (required)
            The OCID of the VCN.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[InternetGateway]
        :rtype: list[InternetGateway]
        """
        resource_path = "/internetGateways"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_internet_gateways got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "vcnId": vcn_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[InternetGateway]")

    def list_ip_sec_connections(self, compartment_id, **kwargs):
        """
        ListIPSecConnections
        Lists the IPSec connections for the specified compartment. You can filter the
        results by DRG or CPE.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str drg_id: (optional)
            The OCID of the DRG.

        :param str cpe_id: (optional)
            The OCID of the CPE.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[IPSecConnection]
        :rtype: list[IPSecConnection]
        """
        resource_path = "/ipsecConnections"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "drg_id",
            "cpe_id",
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_ip_sec_connections got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "drgId": kwargs.get("drg_id", missing),
            "cpeId": kwargs.get("cpe_id", missing),
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[IPSecConnection]")

    def list_route_tables(self, compartment_id, vcn_id, **kwargs):
        """
        ListRouteTables
        Lists the route tables in the specified VCN and specified compartment. The response
        includes the default route table that automatically comes with each VCN, plus any route tables
        you've created.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str vcn_id: (required)
            The OCID of the VCN.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[RouteTable]
        :rtype: list[RouteTable]
        """
        resource_path = "/routeTables"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_route_tables got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "vcnId": vcn_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[RouteTable]")

    def list_security_lists(self, compartment_id, vcn_id, **kwargs):
        """
        ListSecurityLists
        Lists the security lists in the specified VCN and compartment.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str vcn_id: (required)
            The OCID of the VCN.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[SecurityList]
        :rtype: list[SecurityList]
        """
        resource_path = "/securityLists"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_security_lists got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "vcnId": vcn_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[SecurityList]")

    def list_subnets(self, compartment_id, vcn_id, **kwargs):
        """
        ListSubnets
        Lists the subnets in the specified VCN and the specified compartment.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param str vcn_id: (required)
            The OCID of the VCN.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[Subnet]
        :rtype: list[Subnet]
        """
        resource_path = "/subnets"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_subnets got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing),
            "vcnId": vcn_id
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Subnet]")

    def list_vcns(self, compartment_id, **kwargs):
        """
        ListVcns
        Lists the Virtual Cloud Networks (VCNs) in the specified compartment.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[Vcn]
        :rtype: list[Vcn]
        """
        resource_path = "/vcns"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_vcns got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[Vcn]")

    def list_virtual_circuit_bandwidth_shapes(self, compartment_id, **kwargs):
        """
        ListVirtualCircuitBandwidthShapes
        Lists the available bandwidth levels for virtual circuits. You need this
        information so you can specify your desired bandwidth level (i.e., shape)
        when you create a virtual circuit.

        For the compartment ID, provide the OCID of your tenancy (the root compartment).

        For more information about virtual circuits, see
        `FastConnect Overview`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/fastconnect.htm


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[VirtualCircuitBandwidthShape]
        :rtype: list[VirtualCircuitBandwidthShape]
        """
        resource_path = "/virtualCircuitBandwidthShapes"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_virtual_circuit_bandwidth_shapes got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[VirtualCircuitBandwidthShape]")

    def list_virtual_circuits(self, compartment_id, **kwargs):
        """
        ListVirtualCircuits
        Lists the virtual circuits in the specified compartment.


        :param str compartment_id: (required)
            The OCID of the compartment.

        :param int limit: (optional)
            The maximum number of items to return in a paginated \"List\" call.

            Example: `500`

        :param str page: (optional)
            The value of the `opc-next-page` response header from the previous \"List\" call.

        :return: A Response object with data of type list[VirtualCircuit]
        :rtype: list[VirtualCircuit]
        """
        resource_path = "/virtualCircuits"
        method = "GET"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "limit",
            "page"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "list_virtual_circuits got unknown kwargs: {!r}".format(extra_kwargs))

        query_params = {
            "compartmentId": compartment_id,
            "limit": kwargs.get("limit", missing),
            "page": kwargs.get("page", missing)
        }
        query_params = {k: v for (k, v) in six.iteritems(query_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json"
        }

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            query_params=query_params,
            header_params=header_params,
            response_type="list[VirtualCircuit]")

    def update_cpe(self, cpe_id, update_cpe_details, **kwargs):
        """
        UpdateCpe
        Updates the specified CPE's display name.


        :param str cpe_id: (required)
            The OCID of the CPE.

        :param UpdateCpeDetails update_cpe_details: (required)
            Details object for updating a CPE.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type Cpe
        :rtype: Cpe
        """
        resource_path = "/cpes/{cpeId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_cpe got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "cpeId": cpe_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_cpe_details,
            response_type="Cpe")

    def update_cross_connect(self, cross_connect_id, update_cross_connect_details, **kwargs):
        """
        UpdateCrossConnect
        Updates the specified cross-connect.


        :param str cross_connect_id: (required)
            The OCID of the cross-connect.

        :param UpdateCrossConnectDetails update_cross_connect_details: (required)
            Update CrossConnect fields.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type CrossConnect
        :rtype: CrossConnect
        """
        resource_path = "/crossConnects/{crossConnectId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_cross_connect got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectId": cross_connect_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_cross_connect_details,
            response_type="CrossConnect")

    def update_cross_connect_group(self, cross_connect_group_id, update_cross_connect_group_details, **kwargs):
        """
        UpdateCrossConnectGroup
        Updates the specified cross-connect group's display name.


        :param str cross_connect_group_id: (required)
            The OCID of the cross-connect group.

        :param UpdateCrossConnectGroupDetails update_cross_connect_group_details: (required)
            Update CrossConnectGroup fields

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type CrossConnectGroup
        :rtype: CrossConnectGroup
        """
        resource_path = "/crossConnectGroups/{crossConnectGroupId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_cross_connect_group got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "crossConnectGroupId": cross_connect_group_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_cross_connect_group_details,
            response_type="CrossConnectGroup")

    def update_dhcp_options(self, dhcp_id, update_dhcp_details, **kwargs):
        """
        UpdateDhcpOptions
        Updates the specified set of DHCP options. You can update the display name or the options
        themselves. Note that the `options` object you provide replaces the entire existing set of options.


        :param str dhcp_id: (required)
            The OCID for the set of DHCP options.

        :param UpdateDhcpDetails update_dhcp_details: (required)
            Request object for updating a set of DHCP options.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type DhcpOptions
        :rtype: DhcpOptions
        """
        resource_path = "/dhcps/{dhcpId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_dhcp_options got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "dhcpId": dhcp_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_dhcp_details,
            response_type="DhcpOptions")

    def update_drg(self, drg_id, update_drg_details, **kwargs):
        """
        UpdateDrg
        Updates the specified DRG's display name.


        :param str drg_id: (required)
            The OCID of the DRG.

        :param UpdateDrgDetails update_drg_details: (required)
            Details object for updating a DRG.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type Drg
        :rtype: Drg
        """
        resource_path = "/drgs/{drgId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_drg got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgId": drg_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_drg_details,
            response_type="Drg")

    def update_drg_attachment(self, drg_attachment_id, update_drg_attachment_details, **kwargs):
        """
        UpdateDrgAttachment
        Updates the display name for the specified `DrgAttachment`.


        :param str drg_attachment_id: (required)
            The OCID of the DRG attachment.

        :param UpdateDrgAttachmentDetails update_drg_attachment_details: (required)
            Details object for updating a `DrgAttachment`.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type DrgAttachment
        :rtype: DrgAttachment
        """
        resource_path = "/drgAttachments/{drgAttachmentId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_drg_attachment got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "drgAttachmentId": drg_attachment_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_drg_attachment_details,
            response_type="DrgAttachment")

    def update_internet_gateway(self, ig_id, update_internet_gateway_details, **kwargs):
        """
        UpdateInternetGateway
        Updates the specified Internet Gateway. You can disable/enable it, or change its display name.

        If the gateway is disabled, that means no traffic will flow to/from the internet even if there's
        a route rule that enables that traffic.


        :param str ig_id: (required)
            The OCID of the Internet Gateway.

        :param UpdateInternetGatewayDetails update_internet_gateway_details: (required)
            Details for updating the Internet Gateway.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type InternetGateway
        :rtype: InternetGateway
        """
        resource_path = "/internetGateways/{igId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_internet_gateway got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "igId": ig_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_internet_gateway_details,
            response_type="InternetGateway")

    def update_ip_sec_connection(self, ipsc_id, update_ip_sec_connection_details, **kwargs):
        """
        UpdateIPSecConnection
        Updates the display name for the specified IPSec connection.


        :param str ipsc_id: (required)
            The OCID of the IPSec connection.

        :param UpdateIPSecConnectionDetails update_ip_sec_connection_details: (required)
            Details object for updating a IPSec connection.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type IPSecConnection
        :rtype: IPSecConnection
        """
        resource_path = "/ipsecConnections/{ipscId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_ip_sec_connection got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "ipscId": ipsc_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_ip_sec_connection_details,
            response_type="IPSecConnection")

    def update_route_table(self, rt_id, update_route_table_details, **kwargs):
        """
        UpdateRouteTable
        Updates the specified route table's display name or route rules. Note that the
        `routeRules` object you provide replaces the entire existing set of rules.


        :param str rt_id: (required)
            The OCID of the route table.

        :param UpdateRouteTableDetails update_route_table_details: (required)
            Details object for updating a route table.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type RouteTable
        :rtype: RouteTable
        """
        resource_path = "/routeTables/{rtId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_route_table got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "rtId": rt_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_route_table_details,
            response_type="RouteTable")

    def update_security_list(self, security_list_id, update_security_list_details, **kwargs):
        """
        UpdateSecurityList
        Updates the specified security list's display name or rules. Note that the
        `egressSecurityRules` or `ingressSecurityRules` objects you provide replace the entire
        existing objects.


        :param str security_list_id: (required)
            The OCID of the security list.

        :param UpdateSecurityListDetails update_security_list_details: (required)
            Updated details for the security list.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type SecurityList
        :rtype: SecurityList
        """
        resource_path = "/securityLists/{securityListId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_security_list got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "securityListId": security_list_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_security_list_details,
            response_type="SecurityList")

    def update_subnet(self, subnet_id, update_subnet_details, **kwargs):
        """
        UpdateSubnet
        Updates the specified subnet's display name.


        :param str subnet_id: (required)
            The OCID of the subnet.

        :param UpdateSubnetDetails update_subnet_details: (required)
            Details object for updating a subnet.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type Subnet
        :rtype: Subnet
        """
        resource_path = "/subnets/{subnetId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_subnet got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "subnetId": subnet_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_subnet_details,
            response_type="Subnet")

    def update_vcn(self, vcn_id, update_vcn_details, **kwargs):
        """
        UpdateVcn
        Updates the specified VCN's display name.


        :param str vcn_id: (required)
            The OCID of the VCN.

        :param UpdateVcnDetails update_vcn_details: (required)
            Details object for updating a VCN.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type Vcn
        :rtype: Vcn
        """
        resource_path = "/vcns/{vcnId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_vcn got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "vcnId": vcn_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_vcn_details,
            response_type="Vcn")

    def update_virtual_circuit(self, virtual_circuit_id, update_virtual_circuit_details, **kwargs):
        """
        UpdateVirtualCircuit
        Updates the specified virtual circuit. This can be called by
        either the customer who owns the virtual circuit, or the
        provider (when provisioning or de-provisioning the virtual
        circuit from their end). The documentation for
        :func:`update_virtual_circuit_details`
        indicates who can update each property of the virtual circuit.

        **Important:** If the virtual circuit is working and in the
        PROVISIONED state, updating any of the network-related properties
        (such as the DRG being used, the BGP ASN, etc.) will cause the virtual
        circuit's state to switch to PROVISIONING and the related BGP
        session to go down. After Oracle re-provisions the virtual circuit,
        its state will return to PROVISIONED. Make sure you confirm that
        the associated BGP session is back up. For more information
        about the various states and how to test connectivity, see
        `FastConnect Overview`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/fastconnect.htm


        :param str virtual_circuit_id: (required)
            The OCID of the virtual circuit.

        :param UpdateVirtualCircuitDetails update_virtual_circuit_details: (required)
            Update VirtualCircuit fields.

        :param str if_match: (optional)
            For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match`
            parameter to the value of the etag from a previous GET or POST response for that resource.  The resource
            will be updated or deleted only if the etag you provide matches the resource's current etag value.

        :return: A Response object with data of type VirtualCircuit
        :rtype: VirtualCircuit
        """
        resource_path = "/virtualCircuits/{virtualCircuitId}"
        method = "PUT"

        # Don't accept unknown kwargs
        expected_kwargs = [
            "if_match"
        ]
        extra_kwargs = [key for key in six.iterkeys(kwargs) if key not in expected_kwargs]
        if extra_kwargs:
            raise ValueError(
                "update_virtual_circuit got unknown kwargs: {!r}".format(extra_kwargs))

        path_params = {
            "virtualCircuitId": virtual_circuit_id
        }
        path_params = {k: v for (k, v) in six.iteritems(path_params) if v is not missing}

        header_params = {
            "accept": "application/json",
            "content-type": "application/json",
            "if-match": kwargs.get("if_match", missing)
        }
        header_params = {k: v for (k, v) in six.iteritems(header_params) if v is not missing}

        return self.base_client.call_api(
            resource_path=resource_path,
            method=method,
            path_params=path_params,
            header_params=header_params,
            body=update_virtual_circuit_details,
            response_type="VirtualCircuit")
