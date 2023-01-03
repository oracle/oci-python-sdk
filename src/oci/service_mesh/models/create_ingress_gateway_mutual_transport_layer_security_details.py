# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateIngressGatewayMutualTransportLayerSecurityDetails(object):
    """
    Mutual TLS settings used when sending requests to virtual services within the mesh.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateIngressGatewayMutualTransportLayerSecurityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param maximum_validity:
            The value to assign to the maximum_validity property of this CreateIngressGatewayMutualTransportLayerSecurityDetails.
        :type maximum_validity: int

        """
        self.swagger_types = {
            'maximum_validity': 'int'
        }

        self.attribute_map = {
            'maximum_validity': 'maximumValidity'
        }

        self._maximum_validity = None

    @property
    def maximum_validity(self):
        """
        Gets the maximum_validity of this CreateIngressGatewayMutualTransportLayerSecurityDetails.
        The number of days the mTLS certificate is valid.  This value should be less than the Maximum Validity Duration
        for Certificates (Days) setting on the Certificate Authority associated with this Mesh.  The certificate will
        be automatically renewed after 2/3 of the validity period, so a certificate with a maximum validity of 45 days
        will be renewed every 30 days.


        :return: The maximum_validity of this CreateIngressGatewayMutualTransportLayerSecurityDetails.
        :rtype: int
        """
        return self._maximum_validity

    @maximum_validity.setter
    def maximum_validity(self, maximum_validity):
        """
        Sets the maximum_validity of this CreateIngressGatewayMutualTransportLayerSecurityDetails.
        The number of days the mTLS certificate is valid.  This value should be less than the Maximum Validity Duration
        for Certificates (Days) setting on the Certificate Authority associated with this Mesh.  The certificate will
        be automatically renewed after 2/3 of the validity period, so a certificate with a maximum validity of 45 days
        will be renewed every 30 days.


        :param maximum_validity: The maximum_validity of this CreateIngressGatewayMutualTransportLayerSecurityDetails.
        :type: int
        """
        self._maximum_validity = maximum_validity

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
