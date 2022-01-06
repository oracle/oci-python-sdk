# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_resolver_endpoint_details import UpdateResolverEndpointDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateResolverVnicEndpointDetails(UpdateResolverEndpointDetails):
    """
    The body for updating an existing resolver VNIC endpoint.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateResolverVnicEndpointDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.dns.models.UpdateResolverVnicEndpointDetails.endpoint_type` attribute
        of this class is ``VNIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param endpoint_type:
            The value to assign to the endpoint_type property of this UpdateResolverVnicEndpointDetails.
            Allowed values for this property are: "VNIC"
        :type endpoint_type: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateResolverVnicEndpointDetails.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'endpoint_type': 'str',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'endpoint_type': 'endpointType',
            'nsg_ids': 'nsgIds'
        }

        self._endpoint_type = None
        self._nsg_ids = None
        self._endpoint_type = 'VNIC'

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateResolverVnicEndpointDetails.
        An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the
        resolver endpoint is a part of.


        :return: The nsg_ids of this UpdateResolverVnicEndpointDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateResolverVnicEndpointDetails.
        An array of network security group OCIDs for the resolver endpoint. These must be part of the VCN that the
        resolver endpoint is a part of.


        :param nsg_ids: The nsg_ids of this UpdateResolverVnicEndpointDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
