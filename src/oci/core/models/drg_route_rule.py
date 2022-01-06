# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrgRouteRule(object):
    """
    A DRG route rule is a mapping between a destination IP address range and a DRG attachment.
    The map is used to route matching packets. Traffic will be routed across the attachments using Equal-cost multi-path routing (ECMP)
    if there are multiple rules with identical destinations and none of the rules conflict.
    """

    #: A constant which can be used with the destination_type property of a DrgRouteRule.
    #: This constant has a value of "CIDR_BLOCK"
    DESTINATION_TYPE_CIDR_BLOCK = "CIDR_BLOCK"

    #: A constant which can be used with the destination_type property of a DrgRouteRule.
    #: This constant has a value of "SERVICE_CIDR_BLOCK"
    DESTINATION_TYPE_SERVICE_CIDR_BLOCK = "SERVICE_CIDR_BLOCK"

    #: A constant which can be used with the route_type property of a DrgRouteRule.
    #: This constant has a value of "STATIC"
    ROUTE_TYPE_STATIC = "STATIC"

    #: A constant which can be used with the route_type property of a DrgRouteRule.
    #: This constant has a value of "DYNAMIC"
    ROUTE_TYPE_DYNAMIC = "DYNAMIC"

    #: A constant which can be used with the route_provenance property of a DrgRouteRule.
    #: This constant has a value of "STATIC"
    ROUTE_PROVENANCE_STATIC = "STATIC"

    #: A constant which can be used with the route_provenance property of a DrgRouteRule.
    #: This constant has a value of "VCN"
    ROUTE_PROVENANCE_VCN = "VCN"

    #: A constant which can be used with the route_provenance property of a DrgRouteRule.
    #: This constant has a value of "VIRTUAL_CIRCUIT"
    ROUTE_PROVENANCE_VIRTUAL_CIRCUIT = "VIRTUAL_CIRCUIT"

    #: A constant which can be used with the route_provenance property of a DrgRouteRule.
    #: This constant has a value of "IPSEC_TUNNEL"
    ROUTE_PROVENANCE_IPSEC_TUNNEL = "IPSEC_TUNNEL"

    def __init__(self, **kwargs):
        """
        Initializes a new DrgRouteRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param destination:
            The value to assign to the destination property of this DrgRouteRule.
        :type destination: str

        :param destination_type:
            The value to assign to the destination_type property of this DrgRouteRule.
            Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type destination_type: str

        :param next_hop_drg_attachment_id:
            The value to assign to the next_hop_drg_attachment_id property of this DrgRouteRule.
        :type next_hop_drg_attachment_id: str

        :param route_type:
            The value to assign to the route_type property of this DrgRouteRule.
            Allowed values for this property are: "STATIC", "DYNAMIC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type route_type: str

        :param is_conflict:
            The value to assign to the is_conflict property of this DrgRouteRule.
        :type is_conflict: bool

        :param is_blackhole:
            The value to assign to the is_blackhole property of this DrgRouteRule.
        :type is_blackhole: bool

        :param id:
            The value to assign to the id property of this DrgRouteRule.
        :type id: str

        :param route_provenance:
            The value to assign to the route_provenance property of this DrgRouteRule.
            Allowed values for this property are: "STATIC", "VCN", "VIRTUAL_CIRCUIT", "IPSEC_TUNNEL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type route_provenance: str

        :param attributes:
            The value to assign to the attributes property of this DrgRouteRule.
        :type attributes: object

        """
        self.swagger_types = {
            'destination': 'str',
            'destination_type': 'str',
            'next_hop_drg_attachment_id': 'str',
            'route_type': 'str',
            'is_conflict': 'bool',
            'is_blackhole': 'bool',
            'id': 'str',
            'route_provenance': 'str',
            'attributes': 'object'
        }

        self.attribute_map = {
            'destination': 'destination',
            'destination_type': 'destinationType',
            'next_hop_drg_attachment_id': 'nextHopDrgAttachmentId',
            'route_type': 'routeType',
            'is_conflict': 'isConflict',
            'is_blackhole': 'isBlackhole',
            'id': 'id',
            'route_provenance': 'routeProvenance',
            'attributes': 'attributes'
        }

        self._destination = None
        self._destination_type = None
        self._next_hop_drg_attachment_id = None
        self._route_type = None
        self._is_conflict = None
        self._is_blackhole = None
        self._id = None
        self._route_provenance = None
        self._attributes = None

    @property
    def destination(self):
        """
        **[Required]** Gets the destination of this DrgRouteRule.
        Represents the range of IP addresses to match against when routing traffic.

        Potential values:
          * An IP address range (IPv4 or IPv6) in CIDR notation. For example: `192.168.1.0/24`
          or `2001:0db8:0123:45::/56`.
          * When you're setting up a security rule for traffic destined for a particular `Service` through
          a service gateway, this is the `cidrBlock` value associated with that :class:`Service`. For example: `oci-phx-objectstorage`.


        :return: The destination of this DrgRouteRule.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this DrgRouteRule.
        Represents the range of IP addresses to match against when routing traffic.

        Potential values:
          * An IP address range (IPv4 or IPv6) in CIDR notation. For example: `192.168.1.0/24`
          or `2001:0db8:0123:45::/56`.
          * When you're setting up a security rule for traffic destined for a particular `Service` through
          a service gateway, this is the `cidrBlock` value associated with that :class:`Service`. For example: `oci-phx-objectstorage`.


        :param destination: The destination of this DrgRouteRule.
        :type: str
        """
        self._destination = destination

    @property
    def destination_type(self):
        """
        **[Required]** Gets the destination_type of this DrgRouteRule.
        The type of destination for the rule. the type is required if `direction` = `EGRESS`.

        Allowed values:

          * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.
          * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic destined for a
            particular `Service` through a service gateway).

        Allowed values for this property are: "CIDR_BLOCK", "SERVICE_CIDR_BLOCK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The destination_type of this DrgRouteRule.
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """
        Sets the destination_type of this DrgRouteRule.
        The type of destination for the rule. the type is required if `direction` = `EGRESS`.

        Allowed values:

          * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.
          * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
            :class:`Service` (the rule is for traffic destined for a
            particular `Service` through a service gateway).


        :param destination_type: The destination_type of this DrgRouteRule.
        :type: str
        """
        allowed_values = ["CIDR_BLOCK", "SERVICE_CIDR_BLOCK"]
        if not value_allowed_none_or_none_sentinel(destination_type, allowed_values):
            destination_type = 'UNKNOWN_ENUM_VALUE'
        self._destination_type = destination_type

    @property
    def next_hop_drg_attachment_id(self):
        """
        **[Required]** Gets the next_hop_drg_attachment_id of this DrgRouteRule.
        The `OCID`__ of the next hop DRG attachment responsible
        for reaching the network destination.

        A value of `BLACKHOLE` means traffic for this route is discarded without notification.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The next_hop_drg_attachment_id of this DrgRouteRule.
        :rtype: str
        """
        return self._next_hop_drg_attachment_id

    @next_hop_drg_attachment_id.setter
    def next_hop_drg_attachment_id(self, next_hop_drg_attachment_id):
        """
        Sets the next_hop_drg_attachment_id of this DrgRouteRule.
        The `OCID`__ of the next hop DRG attachment responsible
        for reaching the network destination.

        A value of `BLACKHOLE` means traffic for this route is discarded without notification.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param next_hop_drg_attachment_id: The next_hop_drg_attachment_id of this DrgRouteRule.
        :type: str
        """
        self._next_hop_drg_attachment_id = next_hop_drg_attachment_id

    @property
    def route_type(self):
        """
        Gets the route_type of this DrgRouteRule.
        You can specify static routes for the DRG route table using the API.
        The DRG learns dynamic routes from the DRG attachments using various routing protocols.

        Allowed values for this property are: "STATIC", "DYNAMIC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The route_type of this DrgRouteRule.
        :rtype: str
        """
        return self._route_type

    @route_type.setter
    def route_type(self, route_type):
        """
        Sets the route_type of this DrgRouteRule.
        You can specify static routes for the DRG route table using the API.
        The DRG learns dynamic routes from the DRG attachments using various routing protocols.


        :param route_type: The route_type of this DrgRouteRule.
        :type: str
        """
        allowed_values = ["STATIC", "DYNAMIC"]
        if not value_allowed_none_or_none_sentinel(route_type, allowed_values):
            route_type = 'UNKNOWN_ENUM_VALUE'
        self._route_type = route_type

    @property
    def is_conflict(self):
        """
        Gets the is_conflict of this DrgRouteRule.
        Indicates that the route was not imported due to a conflict between route rules.


        :return: The is_conflict of this DrgRouteRule.
        :rtype: bool
        """
        return self._is_conflict

    @is_conflict.setter
    def is_conflict(self, is_conflict):
        """
        Sets the is_conflict of this DrgRouteRule.
        Indicates that the route was not imported due to a conflict between route rules.


        :param is_conflict: The is_conflict of this DrgRouteRule.
        :type: bool
        """
        self._is_conflict = is_conflict

    @property
    def is_blackhole(self):
        """
        Gets the is_blackhole of this DrgRouteRule.
        Indicates that if the next hop attachment does not exist, so traffic for this route is discarded without notification.


        :return: The is_blackhole of this DrgRouteRule.
        :rtype: bool
        """
        return self._is_blackhole

    @is_blackhole.setter
    def is_blackhole(self, is_blackhole):
        """
        Sets the is_blackhole of this DrgRouteRule.
        Indicates that if the next hop attachment does not exist, so traffic for this route is discarded without notification.


        :param is_blackhole: The is_blackhole of this DrgRouteRule.
        :type: bool
        """
        self._is_blackhole = is_blackhole

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DrgRouteRule.
        The Oracle-assigned ID of the DRG route rule.


        :return: The id of this DrgRouteRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DrgRouteRule.
        The Oracle-assigned ID of the DRG route rule.


        :param id: The id of this DrgRouteRule.
        :type: str
        """
        self._id = id

    @property
    def route_provenance(self):
        """
        **[Required]** Gets the route_provenance of this DrgRouteRule.
        The earliest origin of a route. If a route is advertised to a DRG through an IPsec tunnel attachment,
        and is propagated to peered DRGs via RPC attachments, the route's provenance in the peered DRGs remains `IPSEC_TUNNEL`,
        because that is the earliest origin.

        No routes with a provenance `IPSEC_TUNNEL` or `VIRTUAL_CIRCUIT` will be exported to IPsec tunnel or virtual circuit attachments,
        regardless of the attachment's export distribution.

        Allowed values for this property are: "STATIC", "VCN", "VIRTUAL_CIRCUIT", "IPSEC_TUNNEL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The route_provenance of this DrgRouteRule.
        :rtype: str
        """
        return self._route_provenance

    @route_provenance.setter
    def route_provenance(self, route_provenance):
        """
        Sets the route_provenance of this DrgRouteRule.
        The earliest origin of a route. If a route is advertised to a DRG through an IPsec tunnel attachment,
        and is propagated to peered DRGs via RPC attachments, the route's provenance in the peered DRGs remains `IPSEC_TUNNEL`,
        because that is the earliest origin.

        No routes with a provenance `IPSEC_TUNNEL` or `VIRTUAL_CIRCUIT` will be exported to IPsec tunnel or virtual circuit attachments,
        regardless of the attachment's export distribution.


        :param route_provenance: The route_provenance of this DrgRouteRule.
        :type: str
        """
        allowed_values = ["STATIC", "VCN", "VIRTUAL_CIRCUIT", "IPSEC_TUNNEL"]
        if not value_allowed_none_or_none_sentinel(route_provenance, allowed_values):
            route_provenance = 'UNKNOWN_ENUM_VALUE'
        self._route_provenance = route_provenance

    @property
    def attributes(self):
        """
        Gets the attributes of this DrgRouteRule.
        Additional properties for the route, computed by the service.


        :return: The attributes of this DrgRouteRule.
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this DrgRouteRule.
        Additional properties for the route, computed by the service.


        :param attributes: The attributes of this DrgRouteRule.
        :type: object
        """
        self._attributes = attributes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
