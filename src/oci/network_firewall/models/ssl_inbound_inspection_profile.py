# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .decryption_profile import DecryptionProfile
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SslInboundInspectionProfile(DecryptionProfile):
    """
    SSLInboundInspection used on the firewall policy rules.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SslInboundInspectionProfile object with values from keyword arguments. The default value of the :py:attr:`~oci.network_firewall.models.SslInboundInspectionProfile.type` attribute
        of this class is ``SSL_INBOUND_INSPECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this SslInboundInspectionProfile.
            Allowed values for this property are: "SSL_INBOUND_INSPECTION", "SSL_FORWARD_PROXY"
        :type type: str

        :param is_unsupported_version_blocked:
            The value to assign to the is_unsupported_version_blocked property of this SslInboundInspectionProfile.
        :type is_unsupported_version_blocked: bool

        :param is_unsupported_cipher_blocked:
            The value to assign to the is_unsupported_cipher_blocked property of this SslInboundInspectionProfile.
        :type is_unsupported_cipher_blocked: bool

        :param is_out_of_capacity_blocked:
            The value to assign to the is_out_of_capacity_blocked property of this SslInboundInspectionProfile.
        :type is_out_of_capacity_blocked: bool

        """
        self.swagger_types = {
            'type': 'str',
            'is_unsupported_version_blocked': 'bool',
            'is_unsupported_cipher_blocked': 'bool',
            'is_out_of_capacity_blocked': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'is_unsupported_version_blocked': 'isUnsupportedVersionBlocked',
            'is_unsupported_cipher_blocked': 'isUnsupportedCipherBlocked',
            'is_out_of_capacity_blocked': 'isOutOfCapacityBlocked'
        }

        self._type = None
        self._is_unsupported_version_blocked = None
        self._is_unsupported_cipher_blocked = None
        self._is_out_of_capacity_blocked = None
        self._type = 'SSL_INBOUND_INSPECTION'

    @property
    def is_unsupported_version_blocked(self):
        """
        **[Required]** Gets the is_unsupported_version_blocked of this SslInboundInspectionProfile.
        Whether to block sessions if SSL version is not supported.


        :return: The is_unsupported_version_blocked of this SslInboundInspectionProfile.
        :rtype: bool
        """
        return self._is_unsupported_version_blocked

    @is_unsupported_version_blocked.setter
    def is_unsupported_version_blocked(self, is_unsupported_version_blocked):
        """
        Sets the is_unsupported_version_blocked of this SslInboundInspectionProfile.
        Whether to block sessions if SSL version is not supported.


        :param is_unsupported_version_blocked: The is_unsupported_version_blocked of this SslInboundInspectionProfile.
        :type: bool
        """
        self._is_unsupported_version_blocked = is_unsupported_version_blocked

    @property
    def is_unsupported_cipher_blocked(self):
        """
        **[Required]** Gets the is_unsupported_cipher_blocked of this SslInboundInspectionProfile.
        Whether to block sessions if SSL cipher suite is not supported.


        :return: The is_unsupported_cipher_blocked of this SslInboundInspectionProfile.
        :rtype: bool
        """
        return self._is_unsupported_cipher_blocked

    @is_unsupported_cipher_blocked.setter
    def is_unsupported_cipher_blocked(self, is_unsupported_cipher_blocked):
        """
        Sets the is_unsupported_cipher_blocked of this SslInboundInspectionProfile.
        Whether to block sessions if SSL cipher suite is not supported.


        :param is_unsupported_cipher_blocked: The is_unsupported_cipher_blocked of this SslInboundInspectionProfile.
        :type: bool
        """
        self._is_unsupported_cipher_blocked = is_unsupported_cipher_blocked

    @property
    def is_out_of_capacity_blocked(self):
        """
        **[Required]** Gets the is_out_of_capacity_blocked of this SslInboundInspectionProfile.
        Whether to block sessions if the firewall is temporarily unable to decrypt their traffic.


        :return: The is_out_of_capacity_blocked of this SslInboundInspectionProfile.
        :rtype: bool
        """
        return self._is_out_of_capacity_blocked

    @is_out_of_capacity_blocked.setter
    def is_out_of_capacity_blocked(self, is_out_of_capacity_blocked):
        """
        Sets the is_out_of_capacity_blocked of this SslInboundInspectionProfile.
        Whether to block sessions if the firewall is temporarily unable to decrypt their traffic.


        :param is_out_of_capacity_blocked: The is_out_of_capacity_blocked of this SslInboundInspectionProfile.
        :type: bool
        """
        self._is_out_of_capacity_blocked = is_out_of_capacity_blocked

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
