# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiSpecificationRouteBackend(object):
    """
    The backend to forward requests to.
    """

    #: A constant which can be used with the type property of a ApiSpecificationRouteBackend.
    #: This constant has a value of "ORACLE_FUNCTIONS_BACKEND"
    TYPE_ORACLE_FUNCTIONS_BACKEND = "ORACLE_FUNCTIONS_BACKEND"

    #: A constant which can be used with the type property of a ApiSpecificationRouteBackend.
    #: This constant has a value of "HTTP_BACKEND"
    TYPE_HTTP_BACKEND = "HTTP_BACKEND"

    #: A constant which can be used with the type property of a ApiSpecificationRouteBackend.
    #: This constant has a value of "STOCK_RESPONSE_BACKEND"
    TYPE_STOCK_RESPONSE_BACKEND = "STOCK_RESPONSE_BACKEND"

    #: A constant which can be used with the type property of a ApiSpecificationRouteBackend.
    #: This constant has a value of "DYNAMIC_ROUTING_BACKEND"
    TYPE_DYNAMIC_ROUTING_BACKEND = "DYNAMIC_ROUTING_BACKEND"

    #: A constant which can be used with the type property of a ApiSpecificationRouteBackend.
    #: This constant has a value of "OAUTH2_LOGOUT_BACKEND"
    TYPE_OAUTH2_LOGOUT_BACKEND = "OAUTH2_LOGOUT_BACKEND"

    def __init__(self, **kwargs):
        """
        Initializes a new ApiSpecificationRouteBackend object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.apigateway.models.OAuth2LogoutBackend`
        * :class:`~oci.apigateway.models.HTTPBackend`
        * :class:`~oci.apigateway.models.OracleFunctionBackend`
        * :class:`~oci.apigateway.models.StockResponseBackend`
        * :class:`~oci.apigateway.models.DynamicRoutingBackend`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ApiSpecificationRouteBackend.
            Allowed values for this property are: "ORACLE_FUNCTIONS_BACKEND", "HTTP_BACKEND", "STOCK_RESPONSE_BACKEND", "DYNAMIC_ROUTING_BACKEND", "OAUTH2_LOGOUT_BACKEND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'OAUTH2_LOGOUT_BACKEND':
            return 'OAuth2LogoutBackend'

        if type == 'HTTP_BACKEND':
            return 'HTTPBackend'

        if type == 'ORACLE_FUNCTIONS_BACKEND':
            return 'OracleFunctionBackend'

        if type == 'STOCK_RESPONSE_BACKEND':
            return 'StockResponseBackend'

        if type == 'DYNAMIC_ROUTING_BACKEND':
            return 'DynamicRoutingBackend'
        else:
            return 'ApiSpecificationRouteBackend'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ApiSpecificationRouteBackend.
        Type of the API backend.

        Allowed values for this property are: "ORACLE_FUNCTIONS_BACKEND", "HTTP_BACKEND", "STOCK_RESPONSE_BACKEND", "DYNAMIC_ROUTING_BACKEND", "OAUTH2_LOGOUT_BACKEND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ApiSpecificationRouteBackend.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ApiSpecificationRouteBackend.
        Type of the API backend.


        :param type: The type of this ApiSpecificationRouteBackend.
        :type: str
        """
        allowed_values = ["ORACLE_FUNCTIONS_BACKEND", "HTTP_BACKEND", "STOCK_RESPONSE_BACKEND", "DYNAMIC_ROUTING_BACKEND", "OAUTH2_LOGOUT_BACKEND"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
