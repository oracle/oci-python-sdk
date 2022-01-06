# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssociationAuthorizationRequest(object):
    """
    AssociationAuthorizationRequest model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AssociationAuthorizationRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param requests:
            The value to assign to the requests property of this AssociationAuthorizationRequest.
        :type requests: list[oci.identity_data_plane.models.AuthorizationRequest]

        """
        self.swagger_types = {
            'requests': 'list[AuthorizationRequest]'
        }

        self.attribute_map = {
            'requests': 'requests'
        }

        self._requests = None

    @property
    def requests(self):
        """
        **[Required]** Gets the requests of this AssociationAuthorizationRequest.
        The list of authorization requests.


        :return: The requests of this AssociationAuthorizationRequest.
        :rtype: list[oci.identity_data_plane.models.AuthorizationRequest]
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """
        Sets the requests of this AssociationAuthorizationRequest.
        The list of authorization requests.


        :param requests: The requests of this AssociationAuthorizationRequest.
        :type: list[oci.identity_data_plane.models.AuthorizationRequest]
        """
        self._requests = requests

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
