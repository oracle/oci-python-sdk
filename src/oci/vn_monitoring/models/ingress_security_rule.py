# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngressSecurityRule(object):
    """
    A rule for allowing inbound IP packets.
    """

    #: A constant which can be used with the source_type property of a IngressSecurityRule.
    #: This constant has a value of "CIDR_BLOCK"
    SOURCE_TYPE_CIDR_BLOCK = "CIDR_BLOCK"

    #: A constant which can be used with the source_type property of a IngressSecurityRule.
    #: This constant has a value of "SERVICE_CIDR_BLOCK"
    SOURCE_TYPE_SERVICE_CIDR_BLOCK = "SERVICE_CIDR_BLOCK"

    def __init__(self, **kwargs):
        """
        Initializes a new IngressSecurityRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param icmp_options:
            The value to assign to the icmp_options property of this IngressSecurityRule.
        :type icmp_options: oci.vn_monitoring.models.IcmpOptions

        :param is_stateless:
            The value to assign to the is_stateless property of this IngressSecurityRule.
        :type is_stateless: bool

        :param protocol:
            The value to assign to the protocol property of this IngressSecurityRule.
        :type protocol: str

        :param source:
            The value to assign to the source property of this IngressSecurityRule.
        :type source: str

        :param source_type:
            The value to assign to the source_type property of this IngressSecurityRule.
            Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source_type: str

        :param tcp_options:
            The value to assign to the tcp_options property of this IngressSecurityRule.
        :type tcp_options: oci.vn_monitoring.models.TcpOptions

        :param udp_options:
            The value to assign to the udp_options property of this IngressSecurityRule.
        :type udp_options: oci.vn_monitoring.models.UdpOptions

        """
        self.swagger_types = {
            'icmp_options': 'IcmpOptions',
            'is_stateless': 'bool',
            'protocol': 'str',
            'source': 'str',
            'source_type': 'str',
            'tcp_options': 'TcpOptions',
            'udp_options': 'UdpOptions'
        }

        self.attribute_map = {
            'icmp_options': 'icmpOptions',
            'is_stateless': 'isStateless',
            'protocol': 'protocol',
            'source': 'source',
            'source_type': 'sourceType',
            'tcp_options': 'tcpOptions',
            'udp_options': 'udpOptions'
        }

        self._icmp_options = None
        self._is_stateless = None
        self._protocol = None
        self._source = None
        self._source_type = None
        self._tcp_options = None
        self._udp_options = None

    @property
    def icmp_options(self):
        """
        Gets the icmp_options of this IngressSecurityRule.

        :return: The icmp_options of this IngressSecurityRule.
        :rtype: oci.vn_monitoring.models.IcmpOptions
        """
        return self._icmp_options

    @icmp_options.setter
    def icmp_options(self, icmp_options):
        """
        Sets the icmp_options of this IngressSecurityRule.

        :param icmp_options: The icmp_options of this IngressSecurityRule.
        :type: oci.vn_monitoring.models.IcmpOptions
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
        **[Required]** Gets the protocol of this IngressSecurityRule.
        The transport protocol. Specify either `all` or an IPv4 protocol number as
        defined in
        `Protocol Numbers`__.
        Options are supported only for ICMP (\"1\"), TCP (\"6\"), UDP (\"17\"), and ICMPv6 (\"58\").

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
        Options are supported only for ICMP (\"1\"), TCP (\"6\"), UDP (\"17\"), and ICMPv6 (\"58\").

        __ http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml


        :param protocol: The protocol of this IngressSecurityRule.
        :type: str
        """
        self._protocol = protocol

    @property
    def source(self):
        """
        **[Required]** Gets the source of this IngressSecurityRule.
        Conceptually, this is the range of IP addresses that a packet coming into the instance
        can come from.

        Allowed values:

          * IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
            IPv6 addressing is supported for all commercial and government regions. See
            `IPv6 Addresses`__.

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a security list rule for traffic coming from a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :return: The source of this IngressSecurityRule.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this IngressSecurityRule.
        Conceptually, this is the range of IP addresses that a packet coming into the instance
        can come from.

        Allowed values:

          * IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`.
            IPv6 addressing is supported for all commercial and government regions. See
            `IPv6 Addresses`__.

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a security list rule for traffic coming from a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm


        :param source: The source of this IngressSecurityRule.
        :type: str
        """
        self._source = source

    @property
    def source_type(self):
        """
        Gets the source_type of this IngressSecurityRule.
        Type of source for the rule. The default is `CIDR_BLOCK`.

          * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic coming from a
            particular `Service` through a service gateway).

        Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source_type of this IngressSecurityRule.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this IngressSecurityRule.
        Type of source for the rule. The default is `CIDR_BLOCK`.

          * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic coming from a
            particular `Service` through a service gateway).


        :param source_type: The source_type of this IngressSecurityRule.
        :type: str
        """
        allowed_values = ["CIDR_BLOCK", "SERVICE_CIDR_BLOCK"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            source_type = 'UNKNOWN_ENUM_VALUE'
        self._source_type = source_type

    @property
    def tcp_options(self):
        """
        Gets the tcp_options of this IngressSecurityRule.

        :return: The tcp_options of this IngressSecurityRule.
        :rtype: oci.vn_monitoring.models.TcpOptions
        """
        return self._tcp_options

    @tcp_options.setter
    def tcp_options(self, tcp_options):
        """
        Sets the tcp_options of this IngressSecurityRule.

        :param tcp_options: The tcp_options of this IngressSecurityRule.
        :type: oci.vn_monitoring.models.TcpOptions
        """
        self._tcp_options = tcp_options

    @property
    def udp_options(self):
        """
        Gets the udp_options of this IngressSecurityRule.

        :return: The udp_options of this IngressSecurityRule.
        :rtype: oci.vn_monitoring.models.UdpOptions
        """
        return self._udp_options

    @udp_options.setter
    def udp_options(self, udp_options):
        """
        Sets the udp_options of this IngressSecurityRule.

        :param udp_options: The udp_options of this IngressSecurityRule.
        :type: oci.vn_monitoring.models.UdpOptions
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
