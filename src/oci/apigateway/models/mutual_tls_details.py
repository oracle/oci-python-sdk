# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MutualTlsDetails(object):
    """
    Properties used to configure client mTLS verification when API Consumer makes connection to the gateway.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MutualTlsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_verified_certificate_required:
            The value to assign to the is_verified_certificate_required property of this MutualTlsDetails.
        :type is_verified_certificate_required: bool

        :param allowed_sans:
            The value to assign to the allowed_sans property of this MutualTlsDetails.
        :type allowed_sans: list[str]

        """
        self.swagger_types = {
            'is_verified_certificate_required': 'bool',
            'allowed_sans': 'list[str]'
        }

        self.attribute_map = {
            'is_verified_certificate_required': 'isVerifiedCertificateRequired',
            'allowed_sans': 'allowedSans'
        }

        self._is_verified_certificate_required = None
        self._allowed_sans = None

    @property
    def is_verified_certificate_required(self):
        """
        Gets the is_verified_certificate_required of this MutualTlsDetails.
        Determines whether to enable client verification when API Consumer makes connection to the gateway.


        :return: The is_verified_certificate_required of this MutualTlsDetails.
        :rtype: bool
        """
        return self._is_verified_certificate_required

    @is_verified_certificate_required.setter
    def is_verified_certificate_required(self, is_verified_certificate_required):
        """
        Sets the is_verified_certificate_required of this MutualTlsDetails.
        Determines whether to enable client verification when API Consumer makes connection to the gateway.


        :param is_verified_certificate_required: The is_verified_certificate_required of this MutualTlsDetails.
        :type: bool
        """
        self._is_verified_certificate_required = is_verified_certificate_required

    @property
    def allowed_sans(self):
        """
        Gets the allowed_sans of this MutualTlsDetails.
        Allowed list of CN or SAN which will be used for verification of certificate.


        :return: The allowed_sans of this MutualTlsDetails.
        :rtype: list[str]
        """
        return self._allowed_sans

    @allowed_sans.setter
    def allowed_sans(self, allowed_sans):
        """
        Sets the allowed_sans of this MutualTlsDetails.
        Allowed list of CN or SAN which will be used for verification of certificate.


        :param allowed_sans: The allowed_sans of this MutualTlsDetails.
        :type: list[str]
        """
        self._allowed_sans = allowed_sans

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
