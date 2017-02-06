# coding: utf-8
# Copyright (c) 2017 Oracle and/or its affiliates. All rights reserved.

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
        - *VcnLocal:* Reserved for future use.
        - *VcnLocalPlusInternet:* Instances can resolve only internet host
        names (no Internet Gateway is required). The instances still need to use
        their IP addresses to communicate with each other. This is the default
        value in the default set of DHCP options in the VCN.
        - *CustomDnsServer:* Instances use a DNS server of your choice (three maximum).

        :return: The server_type of this DhcpDnsOption.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """
        Sets the server_type of this DhcpDnsOption.
        - *VcnLocal:* Reserved for future use.
        - *VcnLocalPlusInternet:* Instances can resolve only internet host
        names (no Internet Gateway is required). The instances still need to use
        their IP addresses to communicate with each other. This is the default
        value in the default set of DHCP options in the VCN.
        - *CustomDnsServer:* Instances use a DNS server of your choice (three maximum).

        :param server_type: The server_type of this DhcpDnsOption.
        :type: str
        """
        allowed_values = ["VcnLocal", "VcnLocalPlusInternet", "CustomDnsServer"]
        if server_type not in allowed_values:
            raise ValueError(
                "Invalid value for `server_type`, must be one of {0}"
                .format(allowed_values)
            )
        self._server_type = server_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
