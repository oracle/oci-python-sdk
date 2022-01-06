# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessibleCompartmentRequest(object):
    """
    AccessibleCompartmentRequest model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AccessibleCompartmentRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param authorization_request:
            The value to assign to the authorization_request property of this AccessibleCompartmentRequest.
        :type authorization_request: oci.identity_data_plane.models.AuthorizationRequest

        :param compartment_ids:
            The value to assign to the compartment_ids property of this AccessibleCompartmentRequest.
        :type compartment_ids: list[str]

        """
        self.swagger_types = {
            'authorization_request': 'AuthorizationRequest',
            'compartment_ids': 'list[str]'
        }

        self.attribute_map = {
            'authorization_request': 'authorizationRequest',
            'compartment_ids': 'compartmentIds'
        }

        self._authorization_request = None
        self._compartment_ids = None

    @property
    def authorization_request(self):
        """
        **[Required]** Gets the authorization_request of this AccessibleCompartmentRequest.
        The authorization request.


        :return: The authorization_request of this AccessibleCompartmentRequest.
        :rtype: oci.identity_data_plane.models.AuthorizationRequest
        """
        return self._authorization_request

    @authorization_request.setter
    def authorization_request(self, authorization_request):
        """
        Sets the authorization_request of this AccessibleCompartmentRequest.
        The authorization request.


        :param authorization_request: The authorization_request of this AccessibleCompartmentRequest.
        :type: oci.identity_data_plane.models.AuthorizationRequest
        """
        self._authorization_request = authorization_request

    @property
    def compartment_ids(self):
        """
        **[Required]** Gets the compartment_ids of this AccessibleCompartmentRequest.
        The list of compartment ids.


        :return: The compartment_ids of this AccessibleCompartmentRequest.
        :rtype: list[str]
        """
        return self._compartment_ids

    @compartment_ids.setter
    def compartment_ids(self, compartment_ids):
        """
        Sets the compartment_ids of this AccessibleCompartmentRequest.
        The list of compartment ids.


        :param compartment_ids: The compartment_ids of this AccessibleCompartmentRequest.
        :type: list[str]
        """
        self._compartment_ids = compartment_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
