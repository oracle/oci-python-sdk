# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .network_endpoint_details import NetworkEndpointDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateEndpointDetails(NetworkEndpointDetails):
    """
    Private endpoint configuration details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateEndpointDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.analytics.models.PrivateEndpointDetails.network_endpoint_type` attribute
        of this class is ``PRIVATE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param network_endpoint_type:
            The value to assign to the network_endpoint_type property of this PrivateEndpointDetails.
            Allowed values for this property are: "PUBLIC", "PRIVATE"
        :type network_endpoint_type: str

        :param vcn_id:
            The value to assign to the vcn_id property of this PrivateEndpointDetails.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this PrivateEndpointDetails.
        :type subnet_id: str

        """
        self.swagger_types = {
            'network_endpoint_type': 'str',
            'vcn_id': 'str',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'network_endpoint_type': 'networkEndpointType',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId'
        }

        self._network_endpoint_type = None
        self._vcn_id = None
        self._subnet_id = None
        self._network_endpoint_type = 'PRIVATE'

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this PrivateEndpointDetails.
        The VCN OCID for the private endpoint.


        :return: The vcn_id of this PrivateEndpointDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this PrivateEndpointDetails.
        The VCN OCID for the private endpoint.


        :param vcn_id: The vcn_id of this PrivateEndpointDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this PrivateEndpointDetails.
        The subnet OCID for the private endpoint.


        :return: The subnet_id of this PrivateEndpointDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this PrivateEndpointDetails.
        The subnet OCID for the private endpoint.


        :param subnet_id: The subnet_id of this PrivateEndpointDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
