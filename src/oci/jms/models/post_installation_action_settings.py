# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PostInstallationActionSettings(object):
    """
    List of available post actions you can execute after the successful Java installation.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PostInstallationActionSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param disabled_tls_versions:
            The value to assign to the disabled_tls_versions property of this PostInstallationActionSettings.
        :type disabled_tls_versions: list[oci.jms.models.TlsVersions]

        :param should_replace_certificates_operating_system:
            The value to assign to the should_replace_certificates_operating_system property of this PostInstallationActionSettings.
        :type should_replace_certificates_operating_system: bool

        :param minimum_key_size_settings:
            The value to assign to the minimum_key_size_settings property of this PostInstallationActionSettings.
        :type minimum_key_size_settings: oci.jms.models.MinimumKeySizeSettings

        """
        self.swagger_types = {
            'disabled_tls_versions': 'list[TlsVersions]',
            'should_replace_certificates_operating_system': 'bool',
            'minimum_key_size_settings': 'MinimumKeySizeSettings'
        }

        self.attribute_map = {
            'disabled_tls_versions': 'disabledTlsVersions',
            'should_replace_certificates_operating_system': 'shouldReplaceCertificatesOperatingSystem',
            'minimum_key_size_settings': 'minimumKeySizeSettings'
        }

        self._disabled_tls_versions = None
        self._should_replace_certificates_operating_system = None
        self._minimum_key_size_settings = None

    @property
    def disabled_tls_versions(self):
        """
        Gets the disabled_tls_versions of this PostInstallationActionSettings.
        The following post JRE installation actions are supported by the field:
        - Disable TLS 1.0 , TLS 1.1


        :return: The disabled_tls_versions of this PostInstallationActionSettings.
        :rtype: list[oci.jms.models.TlsVersions]
        """
        return self._disabled_tls_versions

    @disabled_tls_versions.setter
    def disabled_tls_versions(self, disabled_tls_versions):
        """
        Sets the disabled_tls_versions of this PostInstallationActionSettings.
        The following post JRE installation actions are supported by the field:
        - Disable TLS 1.0 , TLS 1.1


        :param disabled_tls_versions: The disabled_tls_versions of this PostInstallationActionSettings.
        :type: list[oci.jms.models.TlsVersions]
        """
        self._disabled_tls_versions = disabled_tls_versions

    @property
    def should_replace_certificates_operating_system(self):
        """
        Gets the should_replace_certificates_operating_system of this PostInstallationActionSettings.
        Restores JDK root certificates with the certificates that are available in the operating system.
        The following action is supported by the field:
        - Replace JDK root certificates with a list provided by the operating system


        :return: The should_replace_certificates_operating_system of this PostInstallationActionSettings.
        :rtype: bool
        """
        return self._should_replace_certificates_operating_system

    @should_replace_certificates_operating_system.setter
    def should_replace_certificates_operating_system(self, should_replace_certificates_operating_system):
        """
        Sets the should_replace_certificates_operating_system of this PostInstallationActionSettings.
        Restores JDK root certificates with the certificates that are available in the operating system.
        The following action is supported by the field:
        - Replace JDK root certificates with a list provided by the operating system


        :param should_replace_certificates_operating_system: The should_replace_certificates_operating_system of this PostInstallationActionSettings.
        :type: bool
        """
        self._should_replace_certificates_operating_system = should_replace_certificates_operating_system

    @property
    def minimum_key_size_settings(self):
        """
        Gets the minimum_key_size_settings of this PostInstallationActionSettings.

        :return: The minimum_key_size_settings of this PostInstallationActionSettings.
        :rtype: oci.jms.models.MinimumKeySizeSettings
        """
        return self._minimum_key_size_settings

    @minimum_key_size_settings.setter
    def minimum_key_size_settings(self, minimum_key_size_settings):
        """
        Sets the minimum_key_size_settings of this PostInstallationActionSettings.

        :param minimum_key_size_settings: The minimum_key_size_settings of this PostInstallationActionSettings.
        :type: oci.jms.models.MinimumKeySizeSettings
        """
        self._minimum_key_size_settings = minimum_key_size_settings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
