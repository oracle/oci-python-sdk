# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMutualTransportLayerSecurityDetails(object):
    """
    The mTLS authentication mode to use when receiving requests from other virtual services or ingress gateways within the mesh.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMutualTransportLayerSecurityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param maximum_validity:
            The value to assign to the maximum_validity property of this CreateMutualTransportLayerSecurityDetails.
        :type maximum_validity: int

        :param mode:
            The value to assign to the mode property of this CreateMutualTransportLayerSecurityDetails.
        :type mode: str

        """
        self.swagger_types = {
            'maximum_validity': 'int',
            'mode': 'str'
        }

        self.attribute_map = {
            'maximum_validity': 'maximumValidity',
            'mode': 'mode'
        }

        self._maximum_validity = None
        self._mode = None

    @property
    def maximum_validity(self):
        """
        Gets the maximum_validity of this CreateMutualTransportLayerSecurityDetails.
        The number of days the mTLS certificate is valid.  This value should be less than the Maximum Validity Duration
        for Certificates (Days) setting on the Certificate Authority associated with this Mesh.  The certificate will
        be automatically renewed after 2/3 of the validity period, so a certificate with a maximum validity of 45 days
        will be renewed every 30 days.


        :return: The maximum_validity of this CreateMutualTransportLayerSecurityDetails.
        :rtype: int
        """
        return self._maximum_validity

    @maximum_validity.setter
    def maximum_validity(self, maximum_validity):
        """
        Sets the maximum_validity of this CreateMutualTransportLayerSecurityDetails.
        The number of days the mTLS certificate is valid.  This value should be less than the Maximum Validity Duration
        for Certificates (Days) setting on the Certificate Authority associated with this Mesh.  The certificate will
        be automatically renewed after 2/3 of the validity period, so a certificate with a maximum validity of 45 days
        will be renewed every 30 days.


        :param maximum_validity: The maximum_validity of this CreateMutualTransportLayerSecurityDetails.
        :type: int
        """
        self._maximum_validity = maximum_validity

    @property
    def mode(self):
        """
        **[Required]** Gets the mode of this CreateMutualTransportLayerSecurityDetails.
        DISABLED: Connection is not tunneled.
        PERMISSIVE: Connection can be either plaintext or an mTLS tunnel.
        STRICT: Connection is an mTLS tunnel.  Clients without a valid certificate will be rejected.


        :return: The mode of this CreateMutualTransportLayerSecurityDetails.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this CreateMutualTransportLayerSecurityDetails.
        DISABLED: Connection is not tunneled.
        PERMISSIVE: Connection can be either plaintext or an mTLS tunnel.
        STRICT: Connection is an mTLS tunnel.  Clients without a valid certificate will be rejected.


        :param mode: The mode of this CreateMutualTransportLayerSecurityDetails.
        :type: str
        """
        self._mode = mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
