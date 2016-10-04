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

from .dhcp_option import DhcpOption
from ..util import formatted_flat_dict


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
        If you set `serverType` to `CustomDnsServer`, specify the IP address\nof at least one DNS server of your choice (three maximum).\n

        :return: The custom_dns_servers of this DhcpDnsOption.
        :rtype: list[str]
        """
        return self._custom_dns_servers

    @custom_dns_servers.setter
    def custom_dns_servers(self, custom_dns_servers):
        """
        Sets the custom_dns_servers of this DhcpDnsOption.
        If you set `serverType` to `CustomDnsServer`, specify the IP address\nof at least one DNS server of your choice (three maximum).\n

        :param custom_dns_servers: The custom_dns_servers of this DhcpDnsOption.
        :type: list[str]
        """
        self._custom_dns_servers = custom_dns_servers

    @property
    def server_type(self):
        """
        Gets the server_type of this DhcpDnsOption.
        - *VcnLocal:* Reserved for future use.\n- *VcnLocalPlusInternet:* Instances can resolve only internet host\nnames (no Internet Gateway is required). The instances still need to use\ntheir IP addresses to communicate with each other. This is the default\nvalue in the default set of DHCP options in the VCN.\n- *CustomDnsServer:* Instances use a DNS server of your choice (three maximum).\n

        :return: The server_type of this DhcpDnsOption.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """
        Sets the server_type of this DhcpDnsOption.
        - *VcnLocal:* Reserved for future use.\n- *VcnLocalPlusInternet:* Instances can resolve only internet host\nnames (no Internet Gateway is required). The instances still need to use\ntheir IP addresses to communicate with each other. This is the default\nvalue in the default set of DHCP options in the VCN.\n- *CustomDnsServer:* Instances use a DNS server of your choice (three maximum).\n

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

