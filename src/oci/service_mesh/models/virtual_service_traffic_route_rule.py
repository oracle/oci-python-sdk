# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VirtualServiceTrafficRouteRule(object):
    """
    Rule for routing incoming virtual service traffic to a version.
    """

    #: A constant which can be used with the type property of a VirtualServiceTrafficRouteRule.
    #: This constant has a value of "HTTP"
    TYPE_HTTP = "HTTP"

    #: A constant which can be used with the type property of a VirtualServiceTrafficRouteRule.
    #: This constant has a value of "TLS_PASSTHROUGH"
    TYPE_TLS_PASSTHROUGH = "TLS_PASSTHROUGH"

    #: A constant which can be used with the type property of a VirtualServiceTrafficRouteRule.
    #: This constant has a value of "TCP"
    TYPE_TCP = "TCP"

    def __init__(self, **kwargs):
        """
        Initializes a new VirtualServiceTrafficRouteRule object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.service_mesh.models.TcpVirtualServiceTrafficRouteRule`
        * :class:`~oci.service_mesh.models.TlsPassthroughVirtualServiceTrafficRouteRule`
        * :class:`~oci.service_mesh.models.HttpVirtualServiceTrafficRouteRule`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VirtualServiceTrafficRouteRule.
            Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param destinations:
            The value to assign to the destinations property of this VirtualServiceTrafficRouteRule.
        :type destinations: list[oci.service_mesh.models.VirtualDeploymentTrafficRuleTarget]

        """
        self.swagger_types = {
            'type': 'str',
            'destinations': 'list[VirtualDeploymentTrafficRuleTarget]'
        }

        self.attribute_map = {
            'type': 'type',
            'destinations': 'destinations'
        }

        self._type = None
        self._destinations = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'TCP':
            return 'TcpVirtualServiceTrafficRouteRule'

        if type == 'TLS_PASSTHROUGH':
            return 'TlsPassthroughVirtualServiceTrafficRouteRule'

        if type == 'HTTP':
            return 'HttpVirtualServiceTrafficRouteRule'
        else:
            return 'VirtualServiceTrafficRouteRule'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this VirtualServiceTrafficRouteRule.
        Type of protocol.

        Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this VirtualServiceTrafficRouteRule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VirtualServiceTrafficRouteRule.
        Type of protocol.


        :param type: The type of this VirtualServiceTrafficRouteRule.
        :type: str
        """
        allowed_values = ["HTTP", "TLS_PASSTHROUGH", "TCP"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def destinations(self):
        """
        **[Required]** Gets the destinations of this VirtualServiceTrafficRouteRule.
        The destination of the request.


        :return: The destinations of this VirtualServiceTrafficRouteRule.
        :rtype: list[oci.service_mesh.models.VirtualDeploymentTrafficRuleTarget]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """
        Sets the destinations of this VirtualServiceTrafficRouteRule.
        The destination of the request.


        :param destinations: The destinations of this VirtualServiceTrafficRouteRule.
        :type: list[oci.service_mesh.models.VirtualDeploymentTrafficRuleTarget]
        """
        self._destinations = destinations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
