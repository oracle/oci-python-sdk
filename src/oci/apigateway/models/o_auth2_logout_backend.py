# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .api_specification_route_backend import ApiSpecificationRouteBackend
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OAuth2LogoutBackend(ApiSpecificationRouteBackend):
    """
    Backend which when called triggers OAuth2 logout.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OAuth2LogoutBackend object with values from keyword arguments. The default value of the :py:attr:`~oci.apigateway.models.OAuth2LogoutBackend.type` attribute
        of this class is ``OAUTH2_LOGOUT_BACKEND`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this OAuth2LogoutBackend.
            Allowed values for this property are: "ORACLE_FUNCTIONS_BACKEND", "HTTP_BACKEND", "STOCK_RESPONSE_BACKEND", "DYNAMIC_ROUTING_BACKEND", "OAUTH2_LOGOUT_BACKEND"
        :type type: str

        :param allowed_post_logout_uris:
            The value to assign to the allowed_post_logout_uris property of this OAuth2LogoutBackend.
        :type allowed_post_logout_uris: list[str]

        :param post_logout_state:
            The value to assign to the post_logout_state property of this OAuth2LogoutBackend.
        :type post_logout_state: str

        """
        self.swagger_types = {
            'type': 'str',
            'allowed_post_logout_uris': 'list[str]',
            'post_logout_state': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'allowed_post_logout_uris': 'allowedPostLogoutUris',
            'post_logout_state': 'postLogoutState'
        }

        self._type = None
        self._allowed_post_logout_uris = None
        self._post_logout_state = None
        self._type = 'OAUTH2_LOGOUT_BACKEND'

    @property
    def allowed_post_logout_uris(self):
        """
        Gets the allowed_post_logout_uris of this OAuth2LogoutBackend.

        :return: The allowed_post_logout_uris of this OAuth2LogoutBackend.
        :rtype: list[str]
        """
        return self._allowed_post_logout_uris

    @allowed_post_logout_uris.setter
    def allowed_post_logout_uris(self, allowed_post_logout_uris):
        """
        Sets the allowed_post_logout_uris of this OAuth2LogoutBackend.

        :param allowed_post_logout_uris: The allowed_post_logout_uris of this OAuth2LogoutBackend.
        :type: list[str]
        """
        self._allowed_post_logout_uris = allowed_post_logout_uris

    @property
    def post_logout_state(self):
        """
        Gets the post_logout_state of this OAuth2LogoutBackend.
        Defines a state that should be shared on redirecting to postLogout URL.


        :return: The post_logout_state of this OAuth2LogoutBackend.
        :rtype: str
        """
        return self._post_logout_state

    @post_logout_state.setter
    def post_logout_state(self, post_logout_state):
        """
        Sets the post_logout_state of this OAuth2LogoutBackend.
        Defines a state that should be shared on redirecting to postLogout URL.


        :param post_logout_state: The post_logout_state of this OAuth2LogoutBackend.
        :type: str
        """
        self._post_logout_state = post_logout_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
