# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DynamicAuthenticationPolicy(object):
    """
    Policy on how to authenticate requests when multiple authentication options are configured for a deployment. For an incoming request, the value of selector specified under selectionSource will be matched against the keys specified for each authentication server. The authentication server whose key matches the value of selector will be used for authentication.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DynamicAuthenticationPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param selection_source:
            The value to assign to the selection_source property of this DynamicAuthenticationPolicy.
        :type selection_source: oci.apigateway.models.SelectionSourcePolicy

        :param authentication_servers:
            The value to assign to the authentication_servers property of this DynamicAuthenticationPolicy.
        :type authentication_servers: list[oci.apigateway.models.AuthenticationServerPolicy]

        """
        self.swagger_types = {
            'selection_source': 'SelectionSourcePolicy',
            'authentication_servers': 'list[AuthenticationServerPolicy]'
        }

        self.attribute_map = {
            'selection_source': 'selectionSource',
            'authentication_servers': 'authenticationServers'
        }

        self._selection_source = None
        self._authentication_servers = None

    @property
    def selection_source(self):
        """
        **[Required]** Gets the selection_source of this DynamicAuthenticationPolicy.

        :return: The selection_source of this DynamicAuthenticationPolicy.
        :rtype: oci.apigateway.models.SelectionSourcePolicy
        """
        return self._selection_source

    @selection_source.setter
    def selection_source(self, selection_source):
        """
        Sets the selection_source of this DynamicAuthenticationPolicy.

        :param selection_source: The selection_source of this DynamicAuthenticationPolicy.
        :type: oci.apigateway.models.SelectionSourcePolicy
        """
        self._selection_source = selection_source

    @property
    def authentication_servers(self):
        """
        **[Required]** Gets the authentication_servers of this DynamicAuthenticationPolicy.
        List of authentication servers to choose from during dynamic authentication.


        :return: The authentication_servers of this DynamicAuthenticationPolicy.
        :rtype: list[oci.apigateway.models.AuthenticationServerPolicy]
        """
        return self._authentication_servers

    @authentication_servers.setter
    def authentication_servers(self, authentication_servers):
        """
        Sets the authentication_servers of this DynamicAuthenticationPolicy.
        List of authentication servers to choose from during dynamic authentication.


        :param authentication_servers: The authentication_servers of this DynamicAuthenticationPolicy.
        :type: list[oci.apigateway.models.AuthenticationServerPolicy]
        """
        self._authentication_servers = authentication_servers

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
