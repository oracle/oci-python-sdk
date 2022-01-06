# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .route_authorization_policy import RouteAuthorizationPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnyOfRouteAuthorizationPolicy(RouteAuthorizationPolicy):
    """
    If authentication has been performed, validate whether the request scope (if any) applies to this route.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnyOfRouteAuthorizationPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.AnyOfRouteAuthorizationPolicy.type` attribute
        of this class is ``ANY_OF`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AnyOfRouteAuthorizationPolicy.
            Allowed values for this property are: "ANONYMOUS", "ANY_OF", "AUTHENTICATION_ONLY"
        :type type: str

        :param allowed_scope:
            The value to assign to the allowed_scope property of this AnyOfRouteAuthorizationPolicy.
        :type allowed_scope: list[str]

        """
        self.swagger_types = {
            'type': 'str',
            'allowed_scope': 'list[str]'
        }

        self.attribute_map = {
            'type': 'type',
            'allowed_scope': 'allowedScope'
        }

        self._type = None
        self._allowed_scope = None
        self._type = 'ANY_OF'

    @property
    def allowed_scope(self):
        """
        **[Required]** Gets the allowed_scope of this AnyOfRouteAuthorizationPolicy.
        A user whose scope includes any of these access ranges is allowed on
        this route. Access ranges are case-sensitive.


        :return: The allowed_scope of this AnyOfRouteAuthorizationPolicy.
        :rtype: list[str]
        """
        return self._allowed_scope

    @allowed_scope.setter
    def allowed_scope(self, allowed_scope):
        """
        Sets the allowed_scope of this AnyOfRouteAuthorizationPolicy.
        A user whose scope includes any of these access ranges is allowed on
        this route. Access ranges are case-sensitive.


        :param allowed_scope: The allowed_scope of this AnyOfRouteAuthorizationPolicy.
        :type: list[str]
        """
        self._allowed_scope = allowed_scope

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
