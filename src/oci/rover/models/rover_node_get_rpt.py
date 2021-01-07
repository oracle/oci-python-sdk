# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverNodeGetRpt(object):
    """
    The resource principal token response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RoverNodeGetRpt object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param resource_principal_token:
            The value to assign to the resource_principal_token property of this RoverNodeGetRpt.
        :type resource_principal_token: str

        :param service_principal_session_token:
            The value to assign to the service_principal_session_token property of this RoverNodeGetRpt.
        :type service_principal_session_token: str

        """
        self.swagger_types = {
            'resource_principal_token': 'str',
            'service_principal_session_token': 'str'
        }

        self.attribute_map = {
            'resource_principal_token': 'resourcePrincipalToken',
            'service_principal_session_token': 'servicePrincipalSessionToken'
        }

        self._resource_principal_token = None
        self._service_principal_session_token = None

    @property
    def resource_principal_token(self):
        """
        **[Required]** Gets the resource_principal_token of this RoverNodeGetRpt.
        The resource principal token blob that contains claims about the resource.


        :return: The resource_principal_token of this RoverNodeGetRpt.
        :rtype: str
        """
        return self._resource_principal_token

    @resource_principal_token.setter
    def resource_principal_token(self, resource_principal_token):
        """
        Sets the resource_principal_token of this RoverNodeGetRpt.
        The resource principal token blob that contains claims about the resource.


        :param resource_principal_token: The resource_principal_token of this RoverNodeGetRpt.
        :type: str
        """
        self._resource_principal_token = resource_principal_token

    @property
    def service_principal_session_token(self):
        """
        Gets the service_principal_session_token of this RoverNodeGetRpt.
        The service principal session token


        :return: The service_principal_session_token of this RoverNodeGetRpt.
        :rtype: str
        """
        return self._service_principal_session_token

    @service_principal_session_token.setter
    def service_principal_session_token(self, service_principal_session_token):
        """
        Sets the service_principal_session_token of this RoverNodeGetRpt.
        The service principal session token


        :param service_principal_session_token: The service_principal_session_token of this RoverNodeGetRpt.
        :type: str
        """
        self._service_principal_session_token = service_principal_session_token

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
