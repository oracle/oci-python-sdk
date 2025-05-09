# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190501

from .route_authorization_policy import RouteAuthorizationPolicy
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AnonymousRouteAuthorizationPolicy(RouteAuthorizationPolicy):
    """
    For a type of ANONYMOUS, an authenticated API must have the \"isAnonymousAccessAllowed\" property set to \"true\"
    in the authentication policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AnonymousRouteAuthorizationPolicy object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.AnonymousRouteAuthorizationPolicy.type` attribute
        of this class is ``ANONYMOUS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AnonymousRouteAuthorizationPolicy.
            Allowed values for this property are: "ANONYMOUS", "ANY_OF", "AUTHENTICATION_ONLY"
        :type type: str

        """
        self.swagger_types = {
            'type': 'str'
        }
        self.attribute_map = {
            'type': 'type'
        }
        self._type = None
        self._type = 'ANONYMOUS'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
