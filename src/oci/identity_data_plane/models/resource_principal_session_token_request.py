# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourcePrincipalSessionTokenRequest(object):
    """
    ResourcePrincipalSessionTokenRequest model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourcePrincipalSessionTokenRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_principal_token:
            The value to assign to the resource_principal_token property of this ResourcePrincipalSessionTokenRequest.
        :type resource_principal_token: str

        :param service_principal_session_token:
            The value to assign to the service_principal_session_token property of this ResourcePrincipalSessionTokenRequest.
        :type service_principal_session_token: str

        :param session_public_key:
            The value to assign to the session_public_key property of this ResourcePrincipalSessionTokenRequest.
        :type session_public_key: str

        """
        self.swagger_types = {
            'resource_principal_token': 'str',
            'service_principal_session_token': 'str',
            'session_public_key': 'str'
        }

        self.attribute_map = {
            'resource_principal_token': 'resourcePrincipalToken',
            'service_principal_session_token': 'servicePrincipalSessionToken',
            'session_public_key': 'sessionPublicKey'
        }

        self._resource_principal_token = None
        self._service_principal_session_token = None
        self._session_public_key = None

    @property
    def resource_principal_token(self):
        """
        **[Required]** Gets the resource_principal_token of this ResourcePrincipalSessionTokenRequest.
        The resource principal token.


        :return: The resource_principal_token of this ResourcePrincipalSessionTokenRequest.
        :rtype: str
        """
        return self._resource_principal_token

    @resource_principal_token.setter
    def resource_principal_token(self, resource_principal_token):
        """
        Sets the resource_principal_token of this ResourcePrincipalSessionTokenRequest.
        The resource principal token.


        :param resource_principal_token: The resource_principal_token of this ResourcePrincipalSessionTokenRequest.
        :type: str
        """
        self._resource_principal_token = resource_principal_token

    @property
    def service_principal_session_token(self):
        """
        **[Required]** Gets the service_principal_session_token of this ResourcePrincipalSessionTokenRequest.
        The service principal session token.


        :return: The service_principal_session_token of this ResourcePrincipalSessionTokenRequest.
        :rtype: str
        """
        return self._service_principal_session_token

    @service_principal_session_token.setter
    def service_principal_session_token(self, service_principal_session_token):
        """
        Sets the service_principal_session_token of this ResourcePrincipalSessionTokenRequest.
        The service principal session token.


        :param service_principal_session_token: The service_principal_session_token of this ResourcePrincipalSessionTokenRequest.
        :type: str
        """
        self._service_principal_session_token = service_principal_session_token

    @property
    def session_public_key(self):
        """
        **[Required]** Gets the session_public_key of this ResourcePrincipalSessionTokenRequest.
        The session public key.


        :return: The session_public_key of this ResourcePrincipalSessionTokenRequest.
        :rtype: str
        """
        return self._session_public_key

    @session_public_key.setter
    def session_public_key(self, session_public_key):
        """
        Sets the session_public_key of this ResourcePrincipalSessionTokenRequest.
        The session public key.


        :param session_public_key: The session_public_key of this ResourcePrincipalSessionTokenRequest.
        :type: str
        """
        self._session_public_key = session_public_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
