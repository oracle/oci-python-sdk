# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .decryption_profile import DecryptionProfile
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SslForwardProxyProfile(DecryptionProfile):
    """
    SSLForwardProxy used on the firewall policy rules.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SslForwardProxyProfile object with values from keyword arguments. The default value of the :py:attr:`~oci.network_firewall.models.SslForwardProxyProfile.type` attribute
        of this class is ``SSL_FORWARD_PROXY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this SslForwardProxyProfile.
            Allowed values for this property are: "SSL_INBOUND_INSPECTION", "SSL_FORWARD_PROXY"
        :type type: str

        :param is_expired_certificate_blocked:
            The value to assign to the is_expired_certificate_blocked property of this SslForwardProxyProfile.
        :type is_expired_certificate_blocked: bool

        :param is_untrusted_issuer_blocked:
            The value to assign to the is_untrusted_issuer_blocked property of this SslForwardProxyProfile.
        :type is_untrusted_issuer_blocked: bool

        :param is_revocation_status_timeout_blocked:
            The value to assign to the is_revocation_status_timeout_blocked property of this SslForwardProxyProfile.
        :type is_revocation_status_timeout_blocked: bool

        :param is_unsupported_version_blocked:
            The value to assign to the is_unsupported_version_blocked property of this SslForwardProxyProfile.
        :type is_unsupported_version_blocked: bool

        :param is_unsupported_cipher_blocked:
            The value to assign to the is_unsupported_cipher_blocked property of this SslForwardProxyProfile.
        :type is_unsupported_cipher_blocked: bool

        :param is_unknown_revocation_status_blocked:
            The value to assign to the is_unknown_revocation_status_blocked property of this SslForwardProxyProfile.
        :type is_unknown_revocation_status_blocked: bool

        :param are_certificate_extensions_restricted:
            The value to assign to the are_certificate_extensions_restricted property of this SslForwardProxyProfile.
        :type are_certificate_extensions_restricted: bool

        :param is_auto_include_alt_name:
            The value to assign to the is_auto_include_alt_name property of this SslForwardProxyProfile.
        :type is_auto_include_alt_name: bool

        :param is_out_of_capacity_blocked:
            The value to assign to the is_out_of_capacity_blocked property of this SslForwardProxyProfile.
        :type is_out_of_capacity_blocked: bool

        """
        self.swagger_types = {
            'type': 'str',
            'is_expired_certificate_blocked': 'bool',
            'is_untrusted_issuer_blocked': 'bool',
            'is_revocation_status_timeout_blocked': 'bool',
            'is_unsupported_version_blocked': 'bool',
            'is_unsupported_cipher_blocked': 'bool',
            'is_unknown_revocation_status_blocked': 'bool',
            'are_certificate_extensions_restricted': 'bool',
            'is_auto_include_alt_name': 'bool',
            'is_out_of_capacity_blocked': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'is_expired_certificate_blocked': 'isExpiredCertificateBlocked',
            'is_untrusted_issuer_blocked': 'isUntrustedIssuerBlocked',
            'is_revocation_status_timeout_blocked': 'isRevocationStatusTimeoutBlocked',
            'is_unsupported_version_blocked': 'isUnsupportedVersionBlocked',
            'is_unsupported_cipher_blocked': 'isUnsupportedCipherBlocked',
            'is_unknown_revocation_status_blocked': 'isUnknownRevocationStatusBlocked',
            'are_certificate_extensions_restricted': 'areCertificateExtensionsRestricted',
            'is_auto_include_alt_name': 'isAutoIncludeAltName',
            'is_out_of_capacity_blocked': 'isOutOfCapacityBlocked'
        }

        self._type = None
        self._is_expired_certificate_blocked = None
        self._is_untrusted_issuer_blocked = None
        self._is_revocation_status_timeout_blocked = None
        self._is_unsupported_version_blocked = None
        self._is_unsupported_cipher_blocked = None
        self._is_unknown_revocation_status_blocked = None
        self._are_certificate_extensions_restricted = None
        self._is_auto_include_alt_name = None
        self._is_out_of_capacity_blocked = None
        self._type = 'SSL_FORWARD_PROXY'

    @property
    def is_expired_certificate_blocked(self):
        """
        **[Required]** Gets the is_expired_certificate_blocked of this SslForwardProxyProfile.
        Whether to block sessions if server's certificate is expired.


        :return: The is_expired_certificate_blocked of this SslForwardProxyProfile.
        :rtype: bool
        """
        return self._is_expired_certificate_blocked

    @is_expired_certificate_blocked.setter
    def is_expired_certificate_blocked(self, is_expired_certificate_blocked):
        """
        Sets the is_expired_certificate_blocked of this SslForwardProxyProfile.
        Whether to block sessions if server's certificate is expired.


        :param is_expired_certificate_blocked: The is_expired_certificate_blocked of this SslForwardProxyProfile.
        :type: bool
        """
        self._is_expired_certificate_blocked = is_expired_certificate_blocked

    @property
    def is_untrusted_issuer_blocked(self):
        """
        **[Required]** Gets the is_untrusted_issuer_blocked of this SslForwardProxyProfile.
        Whether to block sessions if server's certificate is issued by an untrusted certificate authority (CA).


        :return: The is_untrusted_issuer_blocked of this SslForwardProxyProfile.
        :rtype: bool
        """
        return self._is_untrusted_issuer_blocked

    @is_untrusted_issuer_blocked.setter
    def is_untrusted_issuer_blocked(self, is_untrusted_issuer_blocked):
        """
        Sets the is_untrusted_issuer_blocked of this SslForwardProxyProfile.
        Whether to block sessions if server's certificate is issued by an untrusted certificate authority (CA).


        :param is_untrusted_issuer_blocked: The is_untrusted_issuer_blocked of this SslForwardProxyProfile.
        :type: bool
        """
        self._is_untrusted_issuer_blocked = is_untrusted_issuer_blocked

    @property
    def is_revocation_status_timeout_blocked(self):
        """
        **[Required]** Gets the is_revocation_status_timeout_blocked of this SslForwardProxyProfile.
        Whether to block sessions if the revocation status check for server's certificate
        does not succeed within the maximum allowed time (defaulting to 5 seconds).


        :return: The is_revocation_status_timeout_blocked of this SslForwardProxyProfile.
        :rtype: bool
        """
        return self._is_revocation_status_timeout_blocked

    @is_revocation_status_timeout_blocked.setter
    def is_revocation_status_timeout_blocked(self, is_revocation_status_timeout_blocked):
        """
        Sets the is_revocation_status_timeout_blocked of this SslForwardProxyProfile.
        Whether to block sessions if the revocation status check for server's certificate
        does not succeed within the maximum allowed time (defaulting to 5 seconds).


        :param is_revocation_status_timeout_blocked: The is_revocation_status_timeout_blocked of this SslForwardProxyProfile.
        :type: bool
        """
        self._is_revocation_status_timeout_blocked = is_revocation_status_timeout_blocked

    @property
    def is_unsupported_version_blocked(self):
        """
        **[Required]** Gets the is_unsupported_version_blocked of this SslForwardProxyProfile.
        Whether to block sessions if SSL version is not supported.


        :return: The is_unsupported_version_blocked of this SslForwardProxyProfile.
        :rtype: bool
        """
        return self._is_unsupported_version_blocked

    @is_unsupported_version_blocked.setter
    def is_unsupported_version_blocked(self, is_unsupported_version_blocked):
        """
        Sets the is_unsupported_version_blocked of this SslForwardProxyProfile.
        Whether to block sessions if SSL version is not supported.


        :param is_unsupported_version_blocked: The is_unsupported_version_blocked of this SslForwardProxyProfile.
        :type: bool
        """
        self._is_unsupported_version_blocked = is_unsupported_version_blocked

    @property
    def is_unsupported_cipher_blocked(self):
        """
        **[Required]** Gets the is_unsupported_cipher_blocked of this SslForwardProxyProfile.
        Whether to block sessions if SSL cipher suite is not supported.


        :return: The is_unsupported_cipher_blocked of this SslForwardProxyProfile.
        :rtype: bool
        """
        return self._is_unsupported_cipher_blocked

    @is_unsupported_cipher_blocked.setter
    def is_unsupported_cipher_blocked(self, is_unsupported_cipher_blocked):
        """
        Sets the is_unsupported_cipher_blocked of this SslForwardProxyProfile.
        Whether to block sessions if SSL cipher suite is not supported.


        :param is_unsupported_cipher_blocked: The is_unsupported_cipher_blocked of this SslForwardProxyProfile.
        :type: bool
        """
        self._is_unsupported_cipher_blocked = is_unsupported_cipher_blocked

    @property
    def is_unknown_revocation_status_blocked(self):
        """
        **[Required]** Gets the is_unknown_revocation_status_blocked of this SslForwardProxyProfile.
        Whether to block sessions if the revocation status check for server's certificate results in \"unknown\".


        :return: The is_unknown_revocation_status_blocked of this SslForwardProxyProfile.
        :rtype: bool
        """
        return self._is_unknown_revocation_status_blocked

    @is_unknown_revocation_status_blocked.setter
    def is_unknown_revocation_status_blocked(self, is_unknown_revocation_status_blocked):
        """
        Sets the is_unknown_revocation_status_blocked of this SslForwardProxyProfile.
        Whether to block sessions if the revocation status check for server's certificate results in \"unknown\".


        :param is_unknown_revocation_status_blocked: The is_unknown_revocation_status_blocked of this SslForwardProxyProfile.
        :type: bool
        """
        self._is_unknown_revocation_status_blocked = is_unknown_revocation_status_blocked

    @property
    def are_certificate_extensions_restricted(self):
        """
        **[Required]** Gets the are_certificate_extensions_restricted of this SslForwardProxyProfile.
        Whether to block sessions if the server's certificate uses extensions other than key usage and/or extended key usage.


        :return: The are_certificate_extensions_restricted of this SslForwardProxyProfile.
        :rtype: bool
        """
        return self._are_certificate_extensions_restricted

    @are_certificate_extensions_restricted.setter
    def are_certificate_extensions_restricted(self, are_certificate_extensions_restricted):
        """
        Sets the are_certificate_extensions_restricted of this SslForwardProxyProfile.
        Whether to block sessions if the server's certificate uses extensions other than key usage and/or extended key usage.


        :param are_certificate_extensions_restricted: The are_certificate_extensions_restricted of this SslForwardProxyProfile.
        :type: bool
        """
        self._are_certificate_extensions_restricted = are_certificate_extensions_restricted

    @property
    def is_auto_include_alt_name(self):
        """
        **[Required]** Gets the is_auto_include_alt_name of this SslForwardProxyProfile.
        Whether to automatically append SAN to impersonating certificate if server certificate is missing SAN.


        :return: The is_auto_include_alt_name of this SslForwardProxyProfile.
        :rtype: bool
        """
        return self._is_auto_include_alt_name

    @is_auto_include_alt_name.setter
    def is_auto_include_alt_name(self, is_auto_include_alt_name):
        """
        Sets the is_auto_include_alt_name of this SslForwardProxyProfile.
        Whether to automatically append SAN to impersonating certificate if server certificate is missing SAN.


        :param is_auto_include_alt_name: The is_auto_include_alt_name of this SslForwardProxyProfile.
        :type: bool
        """
        self._is_auto_include_alt_name = is_auto_include_alt_name

    @property
    def is_out_of_capacity_blocked(self):
        """
        **[Required]** Gets the is_out_of_capacity_blocked of this SslForwardProxyProfile.
        Whether to block sessions if the firewall is temporarily unable to decrypt their traffic.


        :return: The is_out_of_capacity_blocked of this SslForwardProxyProfile.
        :rtype: bool
        """
        return self._is_out_of_capacity_blocked

    @is_out_of_capacity_blocked.setter
    def is_out_of_capacity_blocked(self, is_out_of_capacity_blocked):
        """
        Sets the is_out_of_capacity_blocked of this SslForwardProxyProfile.
        Whether to block sessions if the firewall is temporarily unable to decrypt their traffic.


        :param is_out_of_capacity_blocked: The is_out_of_capacity_blocked of this SslForwardProxyProfile.
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
