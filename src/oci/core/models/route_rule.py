# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RouteRule(object):
    """
    A mapping between a destination IP address range and a virtual device to route matching
    packets to (a target).
    """

    #: A constant which can be used with the destination_type property of a RouteRule.
    #: This constant has a value of "CIDR_BLOCK"
    DESTINATION_TYPE_CIDR_BLOCK = "CIDR_BLOCK"

    #: A constant which can be used with the destination_type property of a RouteRule.
    #: This constant has a value of "SERVICE_CIDR_BLOCK"
    DESTINATION_TYPE_SERVICE_CIDR_BLOCK = "SERVICE_CIDR_BLOCK"

    def __init__(self, **kwargs):
        """
        Initializes a new RouteRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cidr_block:
            The value to assign to the cidr_block property of this RouteRule.
        :type cidr_block: str

        :param destination:
            The value to assign to the destination property of this RouteRule.
        :type destination: str

        :param destination_type:
            The value to assign to the destination_type property of this RouteRule.
            Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type destination_type: str

        :param network_entity_id:
            The value to assign to the network_entity_id property of this RouteRule.
        :type network_entity_id: str

        :param description:
            The value to assign to the description property of this RouteRule.
        :type description: str

        """
        self.swagger_types = {
            'cidr_block': 'str',
            'destination': 'str',
            'destination_type': 'str',
            'network_entity_id': 'str',
            'description': 'str'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'destination': 'destination',
            'destination_type': 'destinationType',
            'network_entity_id': 'networkEntityId',
            'description': 'description'
        }

        self._cidr_block = None
        self._destination = None
        self._destination_type = None
        self._network_entity_id = None
        self._description = None

    @property
    def cidr_block(self):
        """
        Gets the cidr_block of this RouteRule.
        Deprecated. Instead use `destination` and `destinationType`. Requests that include both
        `cidrBlock` and `destination` will be rejected.

        A destination IP address range in CIDR notation. Matching packets will
        be routed to the indicated network entity (the target).

        Cannot be an IPv6 CIDR.

        Example: `0.0.0.0/0`


        :return: The cidr_block of this RouteRule.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this RouteRule.
        Deprecated. Instead use `destination` and `destinationType`. Requests that include both
        `cidrBlock` and `destination` will be rejected.

        A destination IP address range in CIDR notation. Matching packets will
        be routed to the indicated network entity (the target).

        Cannot be an IPv6 CIDR.

        Example: `0.0.0.0/0`


        :param cidr_block: The cidr_block of this RouteRule.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def destination(self):
        """
        Gets the destination of this RouteRule.
        Conceptually, this is the range of IP addresses used for matching when routing
        traffic. Required if you provide a `destinationType`.

        Allowed values:

          * IP address range in CIDR notation. Can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24`
          or `2001:0db8:0123:45::/56`. If you set this to an IPv6 CIDR, the route rule's target
          can only be a DRG or internet gateway. Note that IPv6 addressing is currently supported
          only in certain regions. See `IPv6 Addresses`__.

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a route rule for traffic destined for a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/ipv6.htm


        :return: The destination of this RouteRule.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this RouteRule.
        Conceptually, this is the range of IP addresses used for matching when routing
        traffic. Required if you provide a `destinationType`.

        Allowed values:

          * IP address range in CIDR notation. Can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24`
          or `2001:0db8:0123:45::/56`. If you set this to an IPv6 CIDR, the route rule's target
          can only be a DRG or internet gateway. Note that IPv6 addressing is currently supported
          only in certain regions. See `IPv6 Addresses`__.

          * The `cidrBlock` value for a :class:`Service`, if you're
            setting up a route rule for traffic destined for a particular `Service` through
            a service gateway. For example: `oci-phx-objectstorage`.

        __ https://docs.cloud.oracle.com/Content/Network/Concepts/ipv6.htm


        :param destination: The destination of this RouteRule.
        :type: str
        """
        self._destination = destination

    @property
    def destination_type(self):
        """
        Gets the destination_type of this RouteRule.
        Type of destination for the rule. Required if you provide a `destination`.

          * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic destined for a
            particular `Service` through a service gateway).

        Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The destination_type of this RouteRule.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """
        Sets the destination_type of this RouteRule.
        Type of destination for the rule. Required if you provide a `destination`.

          * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.

          * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic destined for a
            particular `Service` through a service gateway).


        :param destination_type: The destination_type of this RouteRule.
        :type: str
        """
        allowed_values = ["CIDR_BLOCK", "SERVICE_CIDR_BLOCK"]
        if not value_allowed_none_or_none_sentinel(destination_type, allowed_values):
            destination_type = 'UNKNOWN_ENUM_VALUE'
        self._destination_type = destination_type

    @property
    def network_entity_id(self):
        """
        **[Required]** Gets the network_entity_id of this RouteRule.
        The OCID for the route rule's target. For information about the type of
        targets you can specify, see
        `Route Tables`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm


        :return: The network_entity_id of this RouteRule.
        :rtype: str
        """
        return self._network_entity_id

    @network_entity_id.setter
    def network_entity_id(self, network_entity_id):
        """
        Sets the network_entity_id of this RouteRule.
        The OCID for the route rule's target. For information about the type of
        targets you can specify, see
        `Route Tables`__.

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm


        :param network_entity_id: The network_entity_id of this RouteRule.
        :type: str
        """
        self._network_entity_id = network_entity_id

    @property
    def description(self):
        """
        Gets the description of this RouteRule.
        An optional description of your choice for the rule.


        :return: The description of this RouteRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RouteRule.
        An optional description of your choice for the rule.


        :param description: The description of this RouteRule.
        :type: str
        """
        self._description = description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
