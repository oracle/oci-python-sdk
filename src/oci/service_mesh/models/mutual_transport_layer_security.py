# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MutualTransportLayerSecurity(object):
    """
    Mutual TLS settings used when communicating with other virtual services or ingress gateways within the mesh.
    """

    #: A constant which can be used with the mode property of a MutualTransportLayerSecurity.
    #: This constant has a value of "DISABLED"
    MODE_DISABLED = "DISABLED"

    #: A constant which can be used with the mode property of a MutualTransportLayerSecurity.
    #: This constant has a value of "PERMISSIVE"
    MODE_PERMISSIVE = "PERMISSIVE"

    #: A constant which can be used with the mode property of a MutualTransportLayerSecurity.
    #: This constant has a value of "STRICT"
    MODE_STRICT = "STRICT"

    def __init__(self, **kwargs):
        """
        Initializes a new MutualTransportLayerSecurity object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_id:
            The value to assign to the certificate_id property of this MutualTransportLayerSecurity.
        :type certificate_id: str

        :param maximum_validity:
            The value to assign to the maximum_validity property of this MutualTransportLayerSecurity.
        :type maximum_validity: int

        :param mode:
            The value to assign to the mode property of this MutualTransportLayerSecurity.
            Allowed values for this property are: "DISABLED", "PERMISSIVE", "STRICT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type mode: str

        """
        self.swagger_types = {
            'certificate_id': 'str',
            'maximum_validity': 'int',
            'mode': 'str'
        }

        self.attribute_map = {
            'certificate_id': 'certificateId',
            'maximum_validity': 'maximumValidity',
            'mode': 'mode'
        }

        self._certificate_id = None
        self._maximum_validity = None
        self._mode = None

    @property
    def certificate_id(self):
        """
        **[Required]** Gets the certificate_id of this MutualTransportLayerSecurity.
        The OCID of the certificate resource that will be used for mTLS authentication with other virtual services in the mesh.


        :return: The certificate_id of this MutualTransportLayerSecurity.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this MutualTransportLayerSecurity.
        The OCID of the certificate resource that will be used for mTLS authentication with other virtual services in the mesh.


        :param certificate_id: The certificate_id of this MutualTransportLayerSecurity.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def maximum_validity(self):
        """
        Gets the maximum_validity of this MutualTransportLayerSecurity.
        The number of days the mTLS certificate is valid.  This value should be less than the Maximum Validity Duration
        for Certificates (Days) setting on the Certificate Authority associated with this Mesh.  The certificate will
        be automatically renewed after 2/3 of the validity period, so a certificate with a maximum validity of 45 days
        will be renewed every 30 days.


        :return: The maximum_validity of this MutualTransportLayerSecurity.
        :rtype: int
        """
        return self._maximum_validity

    @maximum_validity.setter
    def maximum_validity(self, maximum_validity):
        """
        Sets the maximum_validity of this MutualTransportLayerSecurity.
        The number of days the mTLS certificate is valid.  This value should be less than the Maximum Validity Duration
        for Certificates (Days) setting on the Certificate Authority associated with this Mesh.  The certificate will
        be automatically renewed after 2/3 of the validity period, so a certificate with a maximum validity of 45 days
        will be renewed every 30 days.


        :param maximum_validity: The maximum_validity of this MutualTransportLayerSecurity.
        :type: int
        """
        self._maximum_validity = maximum_validity

    @property
    def mode(self):
        """
        **[Required]** Gets the mode of this MutualTransportLayerSecurity.
        DISABLED: Connection is not tunneled.
        PERMISSIVE: Connection can be either plaintext or an mTLS tunnel.
        STRICT: Connection is an mTLS tunnel.  Clients without a valid certificate will be rejected.

        Allowed values for this property are: "DISABLED", "PERMISSIVE", "STRICT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The mode of this MutualTransportLayerSecurity.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this MutualTransportLayerSecurity.
        DISABLED: Connection is not tunneled.
        PERMISSIVE: Connection can be either plaintext or an mTLS tunnel.
        STRICT: Connection is an mTLS tunnel.  Clients without a valid certificate will be rejected.


        :param mode: The mode of this MutualTransportLayerSecurity.
        :type: str
        """
        allowed_values = ["DISABLED", "PERMISSIVE", "STRICT"]
        if not value_allowed_none_or_none_sentinel(mode, allowed_values):
            mode = 'UNKNOWN_ENUM_VALUE'
        self._mode = mode

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
