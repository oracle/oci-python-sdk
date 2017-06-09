# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class IngressSecurityRule(object):

    def __init__(self):

        self.swagger_types = {
            'icmp_options': 'IcmpOptions',
            'is_stateless': 'bool',
            'protocol': 'str',
            'source': 'str',
            'tcp_options': 'TcpOptions',
            'udp_options': 'UdpOptions'
        }

        self.attribute_map = {
            'icmp_options': 'icmpOptions',
            'is_stateless': 'isStateless',
            'protocol': 'protocol',
            'source': 'source',
            'tcp_options': 'tcpOptions',
            'udp_options': 'udpOptions'
        }

        self._icmp_options = None
        self._is_stateless = None
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
        `ICMP Parameters`__.
        If you specify ICMP as the protocol but omit this object, then all ICMP types and
        codes are allowed. If you do provide this object, the type is required and the code is optional.
        To enable MTU negotiation for ingress internet traffic, make sure to allow type 3 (\"Destination
        Unreachable\") code 4 (\"Fragmentation Needed and Don't Fragment was Set\"). If you need to specify
        multiple codes for a single type, create a separate security list rule for each.

        __ http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml


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
        `ICMP Parameters`__.
        If you specify ICMP as the protocol but omit this object, then all ICMP types and
        codes are allowed. If you do provide this object, the type is required and the code is optional.
        To enable MTU negotiation for ingress internet traffic, make sure to allow type 3 (\"Destination
        Unreachable\") code 4 (\"Fragmentation Needed and Don't Fragment was Set\"). If you need to specify
        multiple codes for a single type, create a separate security list rule for each.

        __ http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml


        :param icmp_options: The icmp_options of this IngressSecurityRule.
        :type: IcmpOptions
        """
        self._icmp_options = icmp_options

    @property
    def is_stateless(self):
        """
        Gets the is_stateless of this IngressSecurityRule.
        A stateless rule allows traffic in one direction. Remember to add a corresponding
        stateless rule in the other direction if you need to support bidirectional traffic. For
        example, if ingress traffic allows TCP destination port 80, there should be an egress
        rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
        and a corresponding rule is not necessary for bidirectional traffic.


        :return: The is_stateless of this IngressSecurityRule.
        :rtype: bool
        """
        return self._is_stateless

    @is_stateless.setter
    def is_stateless(self, is_stateless):
        """
        Sets the is_stateless of this IngressSecurityRule.
        A stateless rule allows traffic in one direction. Remember to add a corresponding
        stateless rule in the other direction if you need to support bidirectional traffic. For
        example, if ingress traffic allows TCP destination port 80, there should be an egress
        rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
        and a corresponding rule is not necessary for bidirectional traffic.


        :param is_stateless: The is_stateless of this IngressSecurityRule.
        :type: bool
        """
        self._is_stateless = is_stateless

    @property
    def protocol(self):
        """
        Gets the protocol of this IngressSecurityRule.
        The transport protocol. Specify either `all` or an IPv4 protocol number as
        defined in
        `Protocol Numbers`__.
        Options are supported only for ICMP (\"1\"), TCP (\"6\"), and UDP (\"17\").

        __ http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml


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
        `Protocol Numbers`__.
        Options are supported only for ICMP (\"1\"), TCP (\"6\"), and UDP (\"17\").

        __ http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml


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
