# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddSecurityRuleDetails(object):
    """
    A rule for allowing inbound (INGRESS) or outbound (EGRESS) IP packets.
    """

    #: A constant which can be used with the destination_type property of a AddSecurityRuleDetails.
    #: This constant has a value of "CIDR_BLOCK"
    DESTINATION_TYPE_CIDR_BLOCK = "CIDR_BLOCK"

    #: A constant which can be used with the destination_type property of a AddSecurityRuleDetails.
    #: This constant has a value of "SERVICE_CIDR_BLOCK"
    DESTINATION_TYPE_SERVICE_CIDR_BLOCK = "SERVICE_CIDR_BLOCK"

    #: A constant which can be used with the destination_type property of a AddSecurityRuleDetails.
    #: This constant has a value of "NETWORK_SECURITY_GROUP"
    DESTINATION_TYPE_NETWORK_SECURITY_GROUP = "NETWORK_SECURITY_GROUP"

    #: A constant which can be used with the direction property of a AddSecurityRuleDetails.
    #: This constant has a value of "EGRESS"
    DIRECTION_EGRESS = "EGRESS"

    #: A constant which can be used with the direction property of a AddSecurityRuleDetails.
    #: This constant has a value of "INGRESS"
    DIRECTION_INGRESS = "INGRESS"

    #: A constant which can be used with the source_type property of a AddSecurityRuleDetails.
    #: This constant has a value of "CIDR_BLOCK"
    SOURCE_TYPE_CIDR_BLOCK = "CIDR_BLOCK"

    #: A constant which can be used with the source_type property of a AddSecurityRuleDetails.
    #: This constant has a value of "SERVICE_CIDR_BLOCK"
    SOURCE_TYPE_SERVICE_CIDR_BLOCK = "SERVICE_CIDR_BLOCK"

    #: A constant which can be used with the source_type property of a AddSecurityRuleDetails.
    #: This constant has a value of "NETWORK_SECURITY_GROUP"
    SOURCE_TYPE_NETWORK_SECURITY_GROUP = "NETWORK_SECURITY_GROUP"

    def __init__(self, **kwargs):
        """
        Initializes a new AddSecurityRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this AddSecurityRuleDetails.
        :type description: str

        :param destination:
            The value to assign to the destination property of this AddSecurityRuleDetails.
        :type destination: str

        :param destination_type:
            The value to assign to the destination_type property of this AddSecurityRuleDetails.
            Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP"
        :type destination_type: str

        :param direction:
            The value to assign to the direction property of this AddSecurityRuleDetails.
            Allowed values for this property are: "EGRESS", "INGRESS"
        :type direction: str

        :param icmp_options:
            The value to assign to the icmp_options property of this AddSecurityRuleDetails.
        :type icmp_options: IcmpOptions

        :param is_stateless:
            The value to assign to the is_stateless property of this AddSecurityRuleDetails.
        :type is_stateless: bool

        :param protocol:
            The value to assign to the protocol property of this AddSecurityRuleDetails.
        :type protocol: str

        :param source:
            The value to assign to the source property of this AddSecurityRuleDetails.
        :type source: str

        :param source_type:
            The value to assign to the source_type property of this AddSecurityRuleDetails.
            Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP"
        :type source_type: str

        :param tcp_options:
            The value to assign to the tcp_options property of this AddSecurityRuleDetails.
        :type tcp_options: TcpOptions

        :param udp_options:
            The value to assign to the udp_options property of this AddSecurityRuleDetails.
        :type udp_options: UdpOptions

        """
        self.swagger_types = {
            'description': 'str',
            'destination': 'str',
            'destination_type': 'str',
            'direction': 'str',
            'icmp_options': 'IcmpOptions',
            'is_stateless': 'bool',
            'protocol': 'str',
            'source': 'str',
            'source_type': 'str',
            'tcp_options': 'TcpOptions',
            'udp_options': 'UdpOptions'
        }

        self.attribute_map = {
            'description': 'description',
            'destination': 'destination',
            'destination_type': 'destinationType',
            'direction': 'direction',
            'icmp_options': 'icmpOptions',
            'is_stateless': 'isStateless',
            'protocol': 'protocol',
            'source': 'source',
            'source_type': 'sourceType',
            'tcp_options': 'tcpOptions',
            'udp_options': 'udpOptions'
        }

        self._description = None
        self._destination = None
        self._destination_type = None
        self._direction = None
        self._icmp_options = None
        self._is_stateless = None
        self._protocol = None
        self._source = None
        self._source_type = None
        self._tcp_options = None
        self._udp_options = None

    @property
    def description(self):
        """
        Gets the description of this AddSecurityRuleDetails.
        An optional description of your choice for the rule. Avoid entering confidential information.


        :return: The description of this AddSecurityRuleDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AddSecurityRuleDetails.
        An optional description of your choice for the rule. Avoid entering confidential information.


        :param description: The description of this AddSecurityRuleDetails.
        :type: str
        """
        self._description = description

    @property
    def destination(self):
        """
        Gets the destination of this AddSecurityRuleDetails.
        Conceptually, this is the range of IP addresses that a packet originating from the instance
        can go to.

        Allowed values:

          * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
            Note that IPv6 addressing is currently supported only in certain regions. See
            `IPv6 Addresses`__.

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a security rule for traffic destined for a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.

          * The OCID of a :class:`NetworkSecurityGroup` in the same
            VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
            traffic between VNICs in the same NSG.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/ipv6.htm


        :return: The destination of this AddSecurityRuleDetails.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this AddSecurityRuleDetails.
        Conceptually, this is the range of IP addresses that a packet originating from the instance
        can go to.

        Allowed values:

          * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
            Note that IPv6 addressing is currently supported only in certain regions. See
            `IPv6 Addresses`__.

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a security rule for traffic destined for a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.

          * The OCID of a :class:`NetworkSecurityGroup` in the same
            VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
            traffic between VNICs in the same NSG.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/ipv6.htm


        :param destination: The destination of this AddSecurityRuleDetails.
        :type: str
        """
        self._destination = destination

    @property
    def destination_type(self):
        """
        Gets the destination_type of this AddSecurityRuleDetails.
        Type of destination for the rule. Required if `direction` = `EGRESS`.

        Allowed values:

          * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic destined for a
            particular `Service` through a service gateway).

          * `NETWORK_SECURITY_GROUP`: If the rule's `destination` is the OCID of a
            :class:`NetworkSecurityGroup`.

        Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP"


        :return: The destination_type of this AddSecurityRuleDetails.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """
        Sets the destination_type of this AddSecurityRuleDetails.
        Type of destination for the rule. Required if `direction` = `EGRESS`.

        Allowed values:

          * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic destined for a
            particular `Service` through a service gateway).

          * `NETWORK_SECURITY_GROUP`: If the rule's `destination` is the OCID of a
            :class:`NetworkSecurityGroup`.


        :param destination_type: The destination_type of this AddSecurityRuleDetails.
        :type: str
        """
        allowed_values = ["CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP"]
        if not value_allowed_none_or_none_sentinel(destination_type, allowed_values):
            raise ValueError(
                "Invalid value for `destination_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._destination_type = destination_type

    @property
    def direction(self):
        """
        **[Required]** Gets the direction of this AddSecurityRuleDetails.
        Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets, or `INGRESS` for rules to allow inbound IP packets.

        Allowed values for this property are: "EGRESS", "INGRESS"


        :return: The direction of this AddSecurityRuleDetails.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this AddSecurityRuleDetails.
        Direction of the security rule. Set to `EGRESS` for rules to allow outbound IP packets, or `INGRESS` for rules to allow inbound IP packets.


        :param direction: The direction of this AddSecurityRuleDetails.
        :type: str
        """
        allowed_values = ["EGRESS", "INGRESS"]
        if not value_allowed_none_or_none_sentinel(direction, allowed_values):
            raise ValueError(
                "Invalid value for `direction`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._direction = direction

    @property
    def icmp_options(self):
        """
        Gets the icmp_options of this AddSecurityRuleDetails.
        Optional and valid only for ICMP and ICMPv6. Use to specify a particular ICMP type and code
        as defined in:
        - `ICMP Parameters`__
        - `ICMPv6 Parameters`__

        If you specify ICMP or ICMPv6 as the protocol but omit this object, then all ICMP types and
        codes are allowed. If you do provide this object, the type is required and the code is optional.
        To enable MTU negotiation for ingress internet traffic via IPv4, make sure to allow type 3 (\"Destination
        Unreachable\") code 4 (\"Fragmentation Needed and Don't Fragment was Set\"). If you need to specify
        multiple codes for a single type, create a separate security list rule for each.

        __ http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml
        __ https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml


        :return: The icmp_options of this AddSecurityRuleDetails.
        :rtype: IcmpOptions
        """
        return self._icmp_options

    @icmp_options.setter
    def icmp_options(self, icmp_options):
        """
        Sets the icmp_options of this AddSecurityRuleDetails.
        Optional and valid only for ICMP and ICMPv6. Use to specify a particular ICMP type and code
        as defined in:
        - `ICMP Parameters`__
        - `ICMPv6 Parameters`__

        If you specify ICMP or ICMPv6 as the protocol but omit this object, then all ICMP types and
        codes are allowed. If you do provide this object, the type is required and the code is optional.
        To enable MTU negotiation for ingress internet traffic via IPv4, make sure to allow type 3 (\"Destination
        Unreachable\") code 4 (\"Fragmentation Needed and Don't Fragment was Set\"). If you need to specify
        multiple codes for a single type, create a separate security list rule for each.

        __ http://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml
        __ https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml


        :param icmp_options: The icmp_options of this AddSecurityRuleDetails.
        :type: IcmpOptions
        """
        self._icmp_options = icmp_options

    @property
    def is_stateless(self):
        """
        Gets the is_stateless of this AddSecurityRuleDetails.
        A stateless rule allows traffic in one direction. Remember to add a corresponding
        stateless rule in the other direction if you need to support bidirectional traffic. For
        example, if egress traffic allows TCP destination port 80, there should be an ingress
        rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
        and a corresponding rule is not necessary for bidirectional traffic.


        :return: The is_stateless of this AddSecurityRuleDetails.
        :rtype: bool
        """
        return self._is_stateless

    @is_stateless.setter
    def is_stateless(self, is_stateless):
        """
        Sets the is_stateless of this AddSecurityRuleDetails.
        A stateless rule allows traffic in one direction. Remember to add a corresponding
        stateless rule in the other direction if you need to support bidirectional traffic. For
        example, if egress traffic allows TCP destination port 80, there should be an ingress
        rule to allow TCP source port 80. Defaults to false, which means the rule is stateful
        and a corresponding rule is not necessary for bidirectional traffic.


        :param is_stateless: The is_stateless of this AddSecurityRuleDetails.
        :type: bool
        """
        self._is_stateless = is_stateless

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this AddSecurityRuleDetails.
        The transport protocol. Specify either `all` or an IPv4 protocol number as
        defined in
        `Protocol Numbers`__.
        Options are supported only for ICMP (\"1\"), TCP (\"6\"), UDP (\"17\"), and ICMPv6 (\"58\").

        __ http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml


        :return: The protocol of this AddSecurityRuleDetails.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this AddSecurityRuleDetails.
        The transport protocol. Specify either `all` or an IPv4 protocol number as
        defined in
        `Protocol Numbers`__.
        Options are supported only for ICMP (\"1\"), TCP (\"6\"), UDP (\"17\"), and ICMPv6 (\"58\").

        __ http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml


        :param protocol: The protocol of this AddSecurityRuleDetails.
        :type: str
        """
        self._protocol = protocol

    @property
    def source(self):
        """
        Gets the source of this AddSecurityRuleDetails.
        Conceptually, this is the range of IP addresses that a packet coming into the instance
        can come from.

        Allowed values:

          * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
            Note that IPv6 addressing is currently supported only in certain regions. See
            `IPv6 Addresses`__.

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a security rule for traffic coming from a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.

          * The OCID of a :class:`NetworkSecurityGroup` in the same
            VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
            traffic between VNICs in the same NSG.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/ipv6.htm


        :return: The source of this AddSecurityRuleDetails.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this AddSecurityRuleDetails.
        Conceptually, this is the range of IP addresses that a packet coming into the instance
        can come from.

        Allowed values:

          * An IP address range in CIDR notation. For example: `192.168.1.0/24` or `2001:0db8:0123:45::/56`
            Note that IPv6 addressing is currently supported only in certain regions. See
            `IPv6 Addresses`__.

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a security rule for traffic coming from a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.

          * The OCID of a :class:`NetworkSecurityGroup` in the same
            VCN. The value can be the NSG that the rule belongs to if the rule's intent is to control
            traffic between VNICs in the same NSG.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/ipv6.htm


        :param source: The source of this AddSecurityRuleDetails.
        :type: str
        """
        self._source = source

    @property
    def source_type(self):
        """
        Gets the source_type of this AddSecurityRuleDetails.
        Type of source for the rule. Required if `direction` = `INGRESS`.

          * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic coming from a
            particular `Service` through a service gateway).

          * `NETWORK_SECURITY_GROUP`: If the rule's `source` is the OCID of a
            :class:`NetworkSecurityGroup`.

        Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP"


        :return: The source_type of this AddSecurityRuleDetails.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this AddSecurityRuleDetails.
        Type of source for the rule. Required if `direction` = `INGRESS`.

          * `CIDR_BLOCK`: If the rule's `source` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `source` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic coming from a
            particular `Service` through a service gateway).

          * `NETWORK_SECURITY_GROUP`: If the rule's `source` is the OCID of a
            :class:`NetworkSecurityGroup`.


        :param source_type: The source_type of this AddSecurityRuleDetails.
        :type: str
        """
        allowed_values = ["CIDR_BLOCK", "SERVICE_CIDR_BLOCK", "NETWORK_SECURITY_GROUP"]
        if not value_allowed_none_or_none_sentinel(source_type, allowed_values):
            raise ValueError(
                "Invalid value for `source_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._source_type = source_type

    @property
    def tcp_options(self):
        """
        Gets the tcp_options of this AddSecurityRuleDetails.
        Optional and valid only for TCP. Use to specify particular destination ports for TCP rules.
        If you specify TCP as the protocol but omit this object, then all destination ports are allowed.


        :return: The tcp_options of this AddSecurityRuleDetails.
        :rtype: TcpOptions
        """
        return self._tcp_options

    @tcp_options.setter
    def tcp_options(self, tcp_options):
        """
        Sets the tcp_options of this AddSecurityRuleDetails.
        Optional and valid only for TCP. Use to specify particular destination ports for TCP rules.
        If you specify TCP as the protocol but omit this object, then all destination ports are allowed.


        :param tcp_options: The tcp_options of this AddSecurityRuleDetails.
        :type: TcpOptions
        """
        self._tcp_options = tcp_options

    @property
    def udp_options(self):
        """
        Gets the udp_options of this AddSecurityRuleDetails.
        Optional and valid only for UDP. Use to specify particular destination ports for UDP rules.
        If you specify UDP as the protocol but omit this object, then all destination ports are allowed.


        :return: The udp_options of this AddSecurityRuleDetails.
        :rtype: UdpOptions
        """
        return self._udp_options

    @udp_options.setter
    def udp_options(self, udp_options):
        """
        Sets the udp_options of this AddSecurityRuleDetails.
        Optional and valid only for UDP. Use to specify particular destination ports for UDP rules.
        If you specify UDP as the protocol but omit this object, then all destination ports are allowed.


        :param udp_options: The udp_options of this AddSecurityRuleDetails.
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
