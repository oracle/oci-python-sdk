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


from ..util import formatted_flat_dict


class IngressSecurityRule(object):

    def __init__(self):

        self.swagger_types = {
            'icmp_options': 'IcmpOptions',
            'protocol': 'str',
            'source': 'str',
            'tcp_options': 'TcpOptions',
            'udp_options': 'UdpOptions'
        }

        self.attribute_map = {
            'icmp_options': 'icmpOptions',
            'protocol': 'protocol',
            'source': 'source',
            'tcp_options': 'tcpOptions',
            'udp_options': 'udpOptions'
        }

        self._icmp_options = None
        self._protocol = None
        self._source = None
        self._tcp_options = None
        self._udp_options = None

    @property
    def icmp_options(self):
        """
        Gets the icmp_options of this IngressSecurityRule.
        Optional and valid only for ICMP. Use to specify a particular ICMP type and code
        as defined in
        [ICMP Parameters](http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml).
        If you specify ICMP as the protocol but omit this object, then all ICMP types and
        codes are allowed. If you do provide this object, the type is required and the code is optional.
        To enable MTU negotiation for ingress internet traffic, make sure to allow type 3 (\"Destination
        Unreachable\") code 4 (\"Fragmentation Needed and Don't Fragment was Set\"). If you need to specify
        multiple codes for a single type, create a separate security list rule for each.

        :return: The icmp_options of this IngressSecurityRule.
        :rtype: IcmpOptions
        """
        return self._icmp_options

    @icmp_options.setter
    def icmp_options(self, icmp_options):
        """
        Sets the icmp_options of this IngressSecurityRule.
        Optional and valid only for ICMP. Use to specify a particular ICMP type and code
        as defined in
        [ICMP Parameters](http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml).
        If you specify ICMP as the protocol but omit this object, then all ICMP types and
        codes are allowed. If you do provide this object, the type is required and the code is optional.
        To enable MTU negotiation for ingress internet traffic, make sure to allow type 3 (\"Destination
        Unreachable\") code 4 (\"Fragmentation Needed and Don't Fragment was Set\"). If you need to specify
        multiple codes for a single type, create a separate security list rule for each.

        :param icmp_options: The icmp_options of this IngressSecurityRule.
        :type: IcmpOptions
        """
        self._icmp_options = icmp_options

    @property
    def protocol(self):
        """
        Gets the protocol of this IngressSecurityRule.
        The transport protocol. Specify either `all` or an IPv4 protocol number as
        defined in
        [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
        Options are supported only for ICMP (\"1\"), TCP (\"6\"), and UDP (\"17\").

        :return: The protocol of this IngressSecurityRule.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this IngressSecurityRule.
        The transport protocol. Specify either `all` or an IPv4 protocol number as
        defined in
        [Protocol Numbers](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
        Options are supported only for ICMP (\"1\"), TCP (\"6\"), and UDP (\"17\").

        :param protocol: The protocol of this IngressSecurityRule.
        :type: str
        """
        self._protocol = protocol

    @property
    def source(self):
        """
        Gets the source of this IngressSecurityRule.
        The source CIDR block for the ingress rule. This is the range of IP addresses that a
        packet coming into the instance can come from.

        :return: The source of this IngressSecurityRule.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this IngressSecurityRule.
        The source CIDR block for the ingress rule. This is the range of IP addresses that a
        packet coming into the instance can come from.

        :param source: The source of this IngressSecurityRule.
        :type: str
        """
        self._source = source

    @property
    def tcp_options(self):
        """
        Gets the tcp_options of this IngressSecurityRule.
        Optional and valid only for TCP. Use to specify particular destination ports for TCP rules.
        If you specify TCP as the protocol but omit this object, then all destination ports are allowed.

        :return: The tcp_options of this IngressSecurityRule.
        :rtype: TcpOptions
        """
        return self._tcp_options

    @tcp_options.setter
    def tcp_options(self, tcp_options):
        """
        Sets the tcp_options of this IngressSecurityRule.
        Optional and valid only for TCP. Use to specify particular destination ports for TCP rules.
        If you specify TCP as the protocol but omit this object, then all destination ports are allowed.

        :param tcp_options: The tcp_options of this IngressSecurityRule.
        :type: TcpOptions
        """
        self._tcp_options = tcp_options

    @property
    def udp_options(self):
        """
        Gets the udp_options of this IngressSecurityRule.
        Optional and valid only for UDP. Use to specify particular destination ports for UDP rules.
        If you specify UDP as the protocol but omit this object, then all destination ports are allowed.

        :return: The udp_options of this IngressSecurityRule.
        :rtype: UdpOptions
        """
        return self._udp_options

    @udp_options.setter
    def udp_options(self, udp_options):
        """
        Sets the udp_options of this IngressSecurityRule.
        Optional and valid only for UDP. Use to specify particular destination ports for UDP rules.
        If you specify UDP as the protocol but omit this object, then all destination ports are allowed.

        :param udp_options: The udp_options of this IngressSecurityRule.
        :type: UdpOptions
        """
        self._udp_options = udp_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
