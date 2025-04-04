# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220615

from .virtual_service_traffic_route_rule_details import VirtualServiceTrafficRouteRuleDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HttpVirtualServiceTrafficRouteRuleDetails(VirtualServiceTrafficRouteRuleDetails):
    """
    Rule for routing incoming Virtual Service traffic with HTTP protocol
    """

    #: A constant which can be used with the path_type property of a HttpVirtualServiceTrafficRouteRuleDetails.
    #: This constant has a value of "PREFIX"
    PATH_TYPE_PREFIX = "PREFIX"

    def __init__(self, **kwargs):
        """
        Initializes a new HttpVirtualServiceTrafficRouteRuleDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.service_mesh.models.HttpVirtualServiceTrafficRouteRuleDetails.type` attribute
        of this class is ``HTTP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this HttpVirtualServiceTrafficRouteRuleDetails.
            Allowed values for this property are: "HTTP", "TLS_PASSTHROUGH", "TCP"
        :type type: str

        :param destinations:
            The value to assign to the destinations property of this HttpVirtualServiceTrafficRouteRuleDetails.
        :type destinations: list[oci.service_mesh.models.VirtualDeploymentTrafficRuleTargetDetails]

        :param path:
            The value to assign to the path property of this HttpVirtualServiceTrafficRouteRuleDetails.
        :type path: str

        :param path_type:
            The value to assign to the path_type property of this HttpVirtualServiceTrafficRouteRuleDetails.
            Allowed values for this property are: "PREFIX"
        :type path_type: str

        :param is_grpc:
            The value to assign to the is_grpc property of this HttpVirtualServiceTrafficRouteRuleDetails.
        :type is_grpc: bool

        :param request_timeout_in_ms:
            The value to assign to the request_timeout_in_ms property of this HttpVirtualServiceTrafficRouteRuleDetails.
        :type request_timeout_in_ms: int

        """
        self.swagger_types = {
            'type': 'str',
            'destinations': 'list[VirtualDeploymentTrafficRuleTargetDetails]',
            'path': 'str',
            'path_type': 'str',
            'is_grpc': 'bool',
            'request_timeout_in_ms': 'int'
        }
        self.attribute_map = {
            'type': 'type',
            'destinations': 'destinations',
            'path': 'path',
            'path_type': 'pathType',
            'is_grpc': 'isGrpc',
            'request_timeout_in_ms': 'requestTimeoutInMs'
        }
        self._type = None
        self._destinations = None
        self._path = None
        self._path_type = None
        self._is_grpc = None
        self._request_timeout_in_ms = None
        self._type = 'HTTP'

    @property
    def path(self):
        """
        Gets the path of this HttpVirtualServiceTrafficRouteRuleDetails.
        Route to match


        :return: The path of this HttpVirtualServiceTrafficRouteRuleDetails.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this HttpVirtualServiceTrafficRouteRuleDetails.
        Route to match


        :param path: The path of this HttpVirtualServiceTrafficRouteRuleDetails.
        :type: str
        """
        self._path = path

    @property
    def path_type(self):
        """
        Gets the path_type of this HttpVirtualServiceTrafficRouteRuleDetails.
        Match type for the route

        Allowed values for this property are: "PREFIX"


        :return: The path_type of this HttpVirtualServiceTrafficRouteRuleDetails.
        :rtype: str
        """
        return self._path_type

    @path_type.setter
    def path_type(self, path_type):
        """
        Sets the path_type of this HttpVirtualServiceTrafficRouteRuleDetails.
        Match type for the route


        :param path_type: The path_type of this HttpVirtualServiceTrafficRouteRuleDetails.
        :type: str
        """
        allowed_values = ["PREFIX"]
        if not value_allowed_none_or_none_sentinel(path_type, allowed_values):
            raise ValueError(
                f"Invalid value for `path_type`, must be None or one of {allowed_values}"
            )
        self._path_type = path_type

    @property
    def is_grpc(self):
        """
        Gets the is_grpc of this HttpVirtualServiceTrafficRouteRuleDetails.
        If true, the rule will check that the content-type header has a application/grpc
        or one of the various application/grpc+ values.


        :return: The is_grpc of this HttpVirtualServiceTrafficRouteRuleDetails.
        :rtype: bool
        """
        return self._is_grpc

    @is_grpc.setter
    def is_grpc(self, is_grpc):
        """
        Sets the is_grpc of this HttpVirtualServiceTrafficRouteRuleDetails.
        If true, the rule will check that the content-type header has a application/grpc
        or one of the various application/grpc+ values.


        :param is_grpc: The is_grpc of this HttpVirtualServiceTrafficRouteRuleDetails.
        :type: bool
        """
        self._is_grpc = is_grpc

    @property
    def request_timeout_in_ms(self):
        """
        Gets the request_timeout_in_ms of this HttpVirtualServiceTrafficRouteRuleDetails.
        The maximum duration in milliseconds for the target service to respond to a request.
        If provided, the timeout value overrides the default timeout of 15 seconds for the HTTP based route rules, and disabled (no timeout) when 'isGrpc' is true.
        The value 0 (zero) indicates that the timeout is disabled.
        For streaming responses from the target service, consider either keeping the timeout disabled or set a sufficiently high value.


        :return: The request_timeout_in_ms of this HttpVirtualServiceTrafficRouteRuleDetails.
        :rtype: int
        """
        return self._request_timeout_in_ms

    @request_timeout_in_ms.setter
    def request_timeout_in_ms(self, request_timeout_in_ms):
        """
        Sets the request_timeout_in_ms of this HttpVirtualServiceTrafficRouteRuleDetails.
        The maximum duration in milliseconds for the target service to respond to a request.
        If provided, the timeout value overrides the default timeout of 15 seconds for the HTTP based route rules, and disabled (no timeout) when 'isGrpc' is true.
        The value 0 (zero) indicates that the timeout is disabled.
        For streaming responses from the target service, consider either keeping the timeout disabled or set a sufficiently high value.


        :param request_timeout_in_ms: The request_timeout_in_ms of this HttpVirtualServiceTrafficRouteRuleDetails.
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
