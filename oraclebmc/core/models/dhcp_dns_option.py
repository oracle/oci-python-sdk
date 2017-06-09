# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .dhcp_option import DhcpOption
from ...util import formatted_flat_dict


class DhcpDnsOption(DhcpOption):

    def __init__(self):

        self.swagger_types = {
            'type': 'str',
            'custom_dns_servers': 'list[str]',
            'server_type': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'custom_dns_servers': 'customDnsServers',
            'server_type': 'serverType'
        }

        self._type = None
        self._custom_dns_servers = None
        self._server_type = None
        self._type = 'DomainNameServer'

    @property
    def custom_dns_servers(self):
        """
        Gets the custom_dns_servers of this DhcpDnsOption.
        If you set `serverType` to `CustomDnsServer`, specify the IP address
        of at least one DNS server of your choice (three maximum).


        :return: The custom_dns_servers of this DhcpDnsOption.
        :rtype: list[str]
        """
        return self._custom_dns_servers

    @custom_dns_servers.setter
    def custom_dns_servers(self, custom_dns_servers):
        """
        Sets the custom_dns_servers of this DhcpDnsOption.
        If you set `serverType` to `CustomDnsServer`, specify the IP address
        of at least one DNS server of your choice (three maximum).


        :param custom_dns_servers: The custom_dns_servers of this DhcpDnsOption.
        :type: list[str]
        """
        self._custom_dns_servers = custom_dns_servers

    @property
    def server_type(self):
        """
        Gets the server_type of this DhcpDnsOption.
        - **VcnLocal:** Reserved for future use.

        - **VcnLocalPlusInternet:** Also referred to as \"Internet and VCN Resolver\".
        Instances can resolve internet hostnames (no Internet Gateway is required),
        and can resolve hostnames of instances in the VCN. This is the default
        value in the default set of DHCP options in the VCN. For the Internet and
        VCN Resolver to work across the VCN, there must also be a DNS label set for
        the VCN, a DNS label set for each subnet, and a hostname for each instance.
        The Internet and VCN Resolver also enables reverse DNS lookup, which lets
        you determine the hostname corresponding to the private IP address. For more
        information, see
        `DNS in Your Virtual Cloud Network`__.

        - **CustomDnsServer:** Instances use a DNS server of your choice (three maximum).

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm

        Allowed values for this property are: "VcnLocal", "VcnLocalPlusInternet", "CustomDnsServer", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The server_type of this DhcpDnsOption.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """
        Sets the server_type of this DhcpDnsOption.
        - **VcnLocal:** Reserved for future use.

        - **VcnLocalPlusInternet:** Also referred to as \"Internet and VCN Resolver\".
        Instances can resolve internet hostnames (no Internet Gateway is required),
        and can resolve hostnames of instances in the VCN. This is the default
        value in the default set of DHCP options in the VCN. For the Internet and
        VCN Resolver to work across the VCN, there must also be a DNS label set for
        the VCN, a DNS label set for each subnet, and a hostname for each instance.
        The Internet and VCN Resolver also enables reverse DNS lookup, which lets
        you determine the hostname corresponding to the private IP address. For more
        information, see
        `DNS in Your Virtual Cloud Network`__.

        - **CustomDnsServer:** Instances use a DNS server of your choice (three maximum).

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm


        :param server_type: The server_type of this DhcpDnsOption.
        :type: str
        """
        allowed_values = ["VcnLocal", "VcnLocalPlusInternet", "CustomDnsServer"]
        if server_type not in allowed_values:
            server_type = 'UNKNOWN_ENUM_VALUE'
        self._server_type = server_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
