# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngressGatewayTrafficRouteRule(object):
    """
    Rule for routing incoming ingress gateway traffic to a virtual service.
    """

    #: A constant which can be used with the type property of a IngressGatewayTrafficRouteRule.
    #: This constant has a value of "HTTP"
    TYPE_HTTP = "HTTP"

    #: A constant which can be used with the type property of a IngressGatewayTrafficRouteRule.
    #: This constant has a value of "TLS_PASSTHROUGH"
    TYPE_TLS_PASSTHROUGH = "TLS_PASSTHROUGH"

    #: A constant which can be used with the type property of a IngressGatewayTrafficRouteRule.
    #: This constant has a value of "TCP"
    TYPE_TCP = "TCP"

    def __init__(self, **kwargs):
        """
        Initializes a new IngressGatewayTrafficRouteRule object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.service_mesh.models.HttpIngressGatewayTrafficRouteRule`
        * :class:`~oci.service_mesh.models.TlsPassthroughIngressGatewayTrafficRouteRule`
        * :class:`~oci.service_mesh.models.TcpIngressGatewayTrafficRouteRule`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this IngressGatewayTrafficRouteRule.
            Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param ingress_gateway_host:
            The value to assign to the ingress_gateway_host property of this IngressGatewayTrafficRouteRule.
        :type ingress_gateway_host: oci.service_mesh.models.IngressGatewayHostRef

        :param destinations:
            The value to assign to the destinations property of this IngressGatewayTrafficRouteRule.
        :type destinations: list[oci.service_mesh.models.VirtualServiceTrafficRuleTarget]

        """
        self.swagger_types = {
            'type': 'str',
            'ingress_gateway_host': 'IngressGatewayHostRef',
            'destinations': 'list[VirtualServiceTrafficRuleTarget]'
        }

        self.attribute_map = {
            'type': 'type',
            'ingress_gateway_host': 'ingressGatewayHost',
            'destinations': 'destinations'
        }

        self._type = None
        self._ingress_gateway_host = None
        self._destinations = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'HTTP':
            return 'HttpIngressGatewayTrafficRouteRule'

        if type == 'TLS_PASSTHROUGH':
            return 'TlsPassthroughIngressGatewayTrafficRouteRule'

        if type == 'TCP':
            return 'TcpIngressGatewayTrafficRouteRule'
        else:
            return 'IngressGatewayTrafficRouteRule'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this IngressGatewayTrafficRouteRule.
        Type of protocol.

        Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this IngressGatewayTrafficRouteRule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IngressGatewayTrafficRouteRule.
        Type of protocol.


        :param type: The type of this IngressGatewayTrafficRouteRule.
        :type: str
        """
        allowed_values = ["HTTP", "TLS_PASSTHROUGH", "TCP"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def ingress_gateway_host(self):
        """
        Gets the ingress_gateway_host of this IngressGatewayTrafficRouteRule.

        :return: The ingress_gateway_host of this IngressGatewayTrafficRouteRule.
        :rtype: oci.service_mesh.models.IngressGatewayHostRef
        """
        return self._ingress_gateway_host

    @ingress_gateway_host.setter
    def ingress_gateway_host(self, ingress_gateway_host):
        """
        Sets the ingress_gateway_host of this IngressGatewayTrafficRouteRule.

        :param ingress_gateway_host: The ingress_gateway_host of this IngressGatewayTrafficRouteRule.
        :type: oci.service_mesh.models.IngressGatewayHostRef
        """
        self._ingress_gateway_host = ingress_gateway_host

    @property
    def destinations(self):
        """
        **[Required]** Gets the destinations of this IngressGatewayTrafficRouteRule.
        The destination of the request.


        :return: The destinations of this IngressGatewayTrafficRouteRule.
        :rtype: list[oci.service_mesh.models.VirtualServiceTrafficRuleTarget]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """
        Sets the destinations of this IngressGatewayTrafficRouteRule.
        The destination of the request.


        :param destinations: The destinations of this IngressGatewayTrafficRouteRule.
        :type: list[oci.service_mesh.models.VirtualServiceTrafficRuleTarget]
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
