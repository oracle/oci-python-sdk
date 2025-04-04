# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220615

from .ingress_gateway_traffic_route_rule import IngressGatewayTrafficRouteRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HttpIngressGatewayTrafficRouteRule(IngressGatewayTrafficRouteRule):
    """
    Rule for routing incoming ingress gateway traffic with HTTP protocol
    """

    #: A constant which can be used with the path_type property of a HttpIngressGatewayTrafficRouteRule.
    #: This constant has a value of "PREFIX"
    PATH_TYPE_PREFIX = "PREFIX"

    def __init__(self, **kwargs):
        """
        Initializes a new HttpIngressGatewayTrafficRouteRule object with values from keyword arguments. The default value of the :py:attr:`~oci.service_mesh.models.HttpIngressGatewayTrafficRouteRule.type` attribute
        of this class is ``HTTP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this HttpIngressGatewayTrafficRouteRule.
            Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param ingress_gateway_host:
            The value to assign to the ingress_gateway_host property of this HttpIngressGatewayTrafficRouteRule.
        :type ingress_gateway_host: oci.service_mesh.models.IngressGatewayHostRef

        :param destinations:
            The value to assign to the destinations property of this HttpIngressGatewayTrafficRouteRule.
        :type destinations: list[oci.service_mesh.models.VirtualServiceTrafficRuleTarget]

        :param path:
            The value to assign to the path property of this HttpIngressGatewayTrafficRouteRule.
        :type path: str

        :param path_type:
            The value to assign to the path_type property of this HttpIngressGatewayTrafficRouteRule.
            Allowed values for this property are: "PREFIX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type path_type: str

        :param is_grpc:
            The value to assign to the is_grpc property of this HttpIngressGatewayTrafficRouteRule.
        :type is_grpc: bool

        :param is_host_rewrite_enabled:
            The value to assign to the is_host_rewrite_enabled property of this HttpIngressGatewayTrafficRouteRule.
        :type is_host_rewrite_enabled: bool

        :param is_path_rewrite_enabled:
            The value to assign to the is_path_rewrite_enabled property of this HttpIngressGatewayTrafficRouteRule.
        :type is_path_rewrite_enabled: bool

        :param request_timeout_in_ms:
            The value to assign to the request_timeout_in_ms property of this HttpIngressGatewayTrafficRouteRule.
        :type request_timeout_in_ms: int

        """
        self.swagger_types = {
            'type': 'str',
            'ingress_gateway_host': 'IngressGatewayHostRef',
            'destinations': 'list[VirtualServiceTrafficRuleTarget]',
            'path': 'str',
            'path_type': 'str',
            'is_grpc': 'bool',
            'is_host_rewrite_enabled': 'bool',
            'is_path_rewrite_enabled': 'bool',
            'request_timeout_in_ms': 'int'
        }
        self.attribute_map = {
            'type': 'type',
            'ingress_gateway_host': 'ingressGatewayHost',
            'destinations': 'destinations',
            'path': 'path',
            'path_type': 'pathType',
            'is_grpc': 'isGrpc',
            'is_host_rewrite_enabled': 'isHostRewriteEnabled',
            'is_path_rewrite_enabled': 'isPathRewriteEnabled',
            'request_timeout_in_ms': 'requestTimeoutInMs'
        }
        self._type = None
        self._ingress_gateway_host = None
        self._destinations = None
        self._path = None
        self._path_type = None
        self._is_grpc = None
        self._is_host_rewrite_enabled = None
        self._is_path_rewrite_enabled = None
        self._request_timeout_in_ms = None
        self._type = 'HTTP'

    @property
    def path(self):
        """
        Gets the path of this HttpIngressGatewayTrafficRouteRule.
        Route to match


        :return: The path of this HttpIngressGatewayTrafficRouteRule.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this HttpIngressGatewayTrafficRouteRule.
        Route to match


        :param path: The path of this HttpIngressGatewayTrafficRouteRule.
        :type: str
        """
        self._path = path

    @property
    def path_type(self):
        """
        Gets the path_type of this HttpIngressGatewayTrafficRouteRule.
        Match type for the route

        Allowed values for this property are: "PREFIX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The path_type of this HttpIngressGatewayTrafficRouteRule.
        :rtype: str
        """
        return self._path_type

    @path_type.setter
    def path_type(self, path_type):
        """
        Sets the path_type of this HttpIngressGatewayTrafficRouteRule.
        Match type for the route


        :param path_type: The path_type of this HttpIngressGatewayTrafficRouteRule.
        :type: str
        """
        allowed_values = ["PREFIX"]
        if not value_allowed_none_or_none_sentinel(path_type, allowed_values):
            path_type = 'UNKNOWN_ENUM_VALUE'
        self._path_type = path_type

    @property
    def is_grpc(self):
        """
        Gets the is_grpc of this HttpIngressGatewayTrafficRouteRule.
        If true, the rule will check that the content-type header has a application/grpc
        or one of the various application/grpc+ values.


        :return: The is_grpc of this HttpIngressGatewayTrafficRouteRule.
        :rtype: bool
        """
        return self._is_grpc

    @is_grpc.setter
    def is_grpc(self, is_grpc):
        """
        Sets the is_grpc of this HttpIngressGatewayTrafficRouteRule.
        If true, the rule will check that the content-type header has a application/grpc
        or one of the various application/grpc+ values.


        :param is_grpc: The is_grpc of this HttpIngressGatewayTrafficRouteRule.
        :type: bool
        """
        self._is_grpc = is_grpc

    @property
    def is_host_rewrite_enabled(self):
        """
        Gets the is_host_rewrite_enabled of this HttpIngressGatewayTrafficRouteRule.
        If true, the hostname will be rewritten to the target virtual deployment's DNS hostname.


        :return: The is_host_rewrite_enabled of this HttpIngressGatewayTrafficRouteRule.
        :rtype: bool
        """
        return self._is_host_rewrite_enabled

    @is_host_rewrite_enabled.setter
    def is_host_rewrite_enabled(self, is_host_rewrite_enabled):
        """
        Sets the is_host_rewrite_enabled of this HttpIngressGatewayTrafficRouteRule.
        If true, the hostname will be rewritten to the target virtual deployment's DNS hostname.


        :param is_host_rewrite_enabled: The is_host_rewrite_enabled of this HttpIngressGatewayTrafficRouteRule.
        :type: bool
        """
        self._is_host_rewrite_enabled = is_host_rewrite_enabled

    @property
    def is_path_rewrite_enabled(self):
        """
        Gets the is_path_rewrite_enabled of this HttpIngressGatewayTrafficRouteRule.
        If true, the matched path prefix will be rewritten to '/' before being directed to the target virtual deployment.


        :return: The is_path_rewrite_enabled of this HttpIngressGatewayTrafficRouteRule.
        :rtype: bool
        """
        return self._is_path_rewrite_enabled

    @is_path_rewrite_enabled.setter
    def is_path_rewrite_enabled(self, is_path_rewrite_enabled):
        """
        Sets the is_path_rewrite_enabled of this HttpIngressGatewayTrafficRouteRule.
        If true, the matched path prefix will be rewritten to '/' before being directed to the target virtual deployment.


        :param is_path_rewrite_enabled: The is_path_rewrite_enabled of this HttpIngressGatewayTrafficRouteRule.
        :type: bool
        """
        self._is_path_rewrite_enabled = is_path_rewrite_enabled

    @property
    def request_timeout_in_ms(self):
        """
        Gets the request_timeout_in_ms of this HttpIngressGatewayTrafficRouteRule.
        The maximum duration in milliseconds for the upstream service to respond to a request.
        If provided, the timeout value overrides the default timeout of 15 seconds for the HTTP based route rules, and disabled (no timeout) when 'isGrpc' is true.
        The value 0 (zero) indicates that the timeout is disabled.
        For streaming responses from the upstream service, consider either keeping the timeout disabled or set a sufficiently high value.


        :return: The request_timeout_in_ms of this HttpIngressGatewayTrafficRouteRule.
        :rtype: int
        """
        return self._request_timeout_in_ms

    @request_timeout_in_ms.setter
    def request_timeout_in_ms(self, request_timeout_in_ms):
        """
        Sets the request_timeout_in_ms of this HttpIngressGatewayTrafficRouteRule.
        The maximum duration in milliseconds for the upstream service to respond to a request.
        If provided, the timeout value overrides the default timeout of 15 seconds for the HTTP based route rules, and disabled (no timeout) when 'isGrpc' is true.
        The value 0 (zero) indicates that the timeout is disabled.
        For streaming responses from the upstream service, consider either keeping the timeout disabled or set a sufficiently high value.


        :param request_timeout_in_ms: The request_timeout_in_ms of this HttpIngressGatewayTrafficRouteRule.
        :type: int
        """
        self._request_timeout_in_ms = request_timeout_in_ms

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
