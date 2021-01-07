# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RouteAuthorizationPolicy(object):
    """
    If authentication has been performed, validate whether the request scope (if any) applies to this route.
    If no RouteAuthorizationPolicy is defined for a route, a policy with a type of AUTHENTICATION_ONLY is applied.
    """

    #: A constant which can be used with the type property of a RouteAuthorizationPolicy.
    #: This constant has a value of "ANONYMOUS"
    TYPE_ANONYMOUS = "ANONYMOUS"

    #: A constant which can be used with the type property of a RouteAuthorizationPolicy.
    #: This constant has a value of "ANY_OF"
    TYPE_ANY_OF = "ANY_OF"

    #: A constant which can be used with the type property of a RouteAuthorizationPolicy.
    #: This constant has a value of "AUTHENTICATION_ONLY"
    TYPE_AUTHENTICATION_ONLY = "AUTHENTICATION_ONLY"

    def __init__(self, **kwargs):
        """
        Initializes a new RouteAuthorizationPolicy object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.apigateway.models.AnyOfRouteAuthorizationPolicy`
        * :class:`~oci.apigateway.models.AnonymousRouteAuthorizationPolicy`
        * :class:`~oci.apigateway.models.AuthenticationOnlyRouteAuthorizationPolicy`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this RouteAuthorizationPolicy.
            Allowed values for this property are: "ANONYMOUS", "ANY_OF", "AUTHENTICATION_ONLY", 'UNKNOWN_ENUM_VALUE'.
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

        if type == 'ANY_OF':
            return 'AnyOfRouteAuthorizationPolicy'

        if type == 'ANONYMOUS':
            return 'AnonymousRouteAuthorizationPolicy'

        if type == 'AUTHENTICATION_ONLY':
            return 'AuthenticationOnlyRouteAuthorizationPolicy'
        else:
            return 'RouteAuthorizationPolicy'

    @property
    def type(self):
        """
        Gets the type of this RouteAuthorizationPolicy.
        Indicates how authorization should be applied. For a type of ANY_OF, an \"allowedScope\"
        property must also be specified. Otherwise, only a type is required. For a type of ANONYMOUS, an
        authenticated API must have the \"isAnonymousAccessAllowed\" property set to \"true\" in the authentication
        policy.

        Allowed values for this property are: "ANONYMOUS", "ANY_OF", "AUTHENTICATION_ONLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this RouteAuthorizationPolicy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RouteAuthorizationPolicy.
        Indicates how authorization should be applied. For a type of ANY_OF, an \"allowedScope\"
        property must also be specified. Otherwise, only a type is required. For a type of ANONYMOUS, an
        authenticated API must have the \"isAnonymousAccessAllowed\" property set to \"true\" in the authentication
        policy.


        :param type: The type of this RouteAuthorizationPolicy.
        :type: str
        """
        allowed_values = ["ANONYMOUS", "ANY_OF", "AUTHENTICATION_ONLY"]
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
