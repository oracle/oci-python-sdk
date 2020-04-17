# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .dhcp_option import DhcpOption
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DhcpDnsOption(DhcpOption):
    """
    DHCP option for specifying how DNS (hostname resolution) is handled in the subnets in the VCN.
    For more information, see
    `DNS in Your Virtual Cloud Network`__.

    __ https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm
    """

    #: A constant which can be used with the server_type property of a DhcpDnsOption.
    #: This constant has a value of "VcnLocal"
    SERVER_TYPE_VCN_LOCAL = "VcnLocal"

    #: A constant which can be used with the server_type property of a DhcpDnsOption.
    #: This constant has a value of "VcnLocalPlusInternet"
    SERVER_TYPE_VCN_LOCAL_PLUS_INTERNET = "VcnLocalPlusInternet"

    #: A constant which can be used with the server_type property of a DhcpDnsOption.
    #: This constant has a value of "CustomDnsServer"
    SERVER_TYPE_CUSTOM_DNS_SERVER = "CustomDnsServer"

    def __init__(self, **kwargs):
        """
        Initializes a new DhcpDnsOption object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.DhcpDnsOption.type` attribute
        of this class is ``DomainNameServer`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DhcpDnsOption.
        :type type: str

        :param custom_dns_servers:
            The value to assign to the custom_dns_servers property of this DhcpDnsOption.
        :type custom_dns_servers: list[str]

        :param server_type:
            The value to assign to the server_type property of this DhcpDnsOption.
            Allowed values for this property are: "VcnLocal", "VcnLocalPlusInternet", "CustomDnsServer", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type server_type: str

        """
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
        If you set `serverType` to `CustomDnsServer`, specify the
        IP address of at least one DNS server of your choice (three maximum).


        :return: The custom_dns_servers of this DhcpDnsOption.
        :rtype: list[str]
        """
        return self._custom_dns_servers

    @custom_dns_servers.setter
    def custom_dns_servers(self, custom_dns_servers):
        """
        Sets the custom_dns_servers of this DhcpDnsOption.
        If you set `serverType` to `CustomDnsServer`, specify the
        IP address of at least one DNS server of your choice (three maximum).


        :param custom_dns_servers: The custom_dns_servers of this DhcpDnsOption.
        :type: list[str]
        """
        self._custom_dns_servers = custom_dns_servers

    @property
    def server_type(self):
        """
        **[Required]** Gets the server_type of this DhcpDnsOption.
        * **VcnLocal:** Reserved for future use.

        * **VcnLocalPlusInternet:** Also referred to as \"Internet and VCN Resolver\".
        Instances can resolve internet hostnames (no internet gateway is required),
        and can resolve hostnames of instances in the VCN. This is the default
        value in the default set of DHCP options in the VCN. For the Internet and
        VCN Resolver to work across the VCN, there must also be a DNS label set for
        the VCN, a DNS label set for each subnet, and a hostname for each instance.
        The Internet and VCN Resolver also enables reverse DNS lookup, which lets
        you determine the hostname corresponding to the private IP address. For more
        information, see
        `DNS in Your Virtual Cloud Network`__.

        * **CustomDnsServer:** Instances use a DNS server of your choice (three
        maximum).

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm

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
        * **VcnLocal:** Reserved for future use.

        * **VcnLocalPlusInternet:** Also referred to as \"Internet and VCN Resolver\".
        Instances can resolve internet hostnames (no internet gateway is required),
        and can resolve hostnames of instances in the VCN. This is the default
        value in the default set of DHCP options in the VCN. For the Internet and
        VCN Resolver to work across the VCN, there must also be a DNS label set for
        the VCN, a DNS label set for each subnet, and a hostname for each instance.
        The Internet and VCN Resolver also enables reverse DNS lookup, which lets
        you determine the hostname corresponding to the private IP address. For more
        information, see
        `DNS in Your Virtual Cloud Network`__.

        * **CustomDnsServer:** Instances use a DNS server of your choice (three
        maximum).

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/dns.htm


        :param server_type: The server_type of this DhcpDnsOption.
        :type: str
        """
        allowed_values = ["VcnLocal", "VcnLocalPlusInternet", "CustomDnsServer"]
        if not value_allowed_none_or_none_sentinel(server_type, allowed_values):
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
