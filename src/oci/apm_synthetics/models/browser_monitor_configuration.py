# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .monitor_configuration import MonitorConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BrowserMonitorConfiguration(MonitorConfiguration):
    """
    Configuration details for the BROWSER monitor type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BrowserMonitorConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.apm_synthetics.models.BrowserMonitorConfiguration.config_type` attribute
        of this class is ``BROWSER_CONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this BrowserMonitorConfiguration.
            Allowed values for this property are: "BROWSER_CONFIG", "SCRIPTED_BROWSER_CONFIG", "REST_CONFIG", "SCRIPTED_REST_CONFIG"
        :type config_type: str

        :param is_failure_retried:
            The value to assign to the is_failure_retried property of this BrowserMonitorConfiguration.
        :type is_failure_retried: bool

        :param is_certificate_validation_enabled:
            The value to assign to the is_certificate_validation_enabled property of this BrowserMonitorConfiguration.
        :type is_certificate_validation_enabled: bool

        :param verify_texts:
            The value to assign to the verify_texts property of this BrowserMonitorConfiguration.
        :type verify_texts: list[oci.apm_synthetics.models.VerifyText]

        :param network_configuration:
            The value to assign to the network_configuration property of this BrowserMonitorConfiguration.
        :type network_configuration: oci.apm_synthetics.models.NetworkConfiguration

        """
        self.swagger_types = {
            'config_type': 'str',
            'is_failure_retried': 'bool',
            'is_certificate_validation_enabled': 'bool',
            'verify_texts': 'list[VerifyText]',
            'network_configuration': 'NetworkConfiguration'
        }

        self.attribute_map = {
            'config_type': 'configType',
            'is_failure_retried': 'isFailureRetried',
            'is_certificate_validation_enabled': 'isCertificateValidationEnabled',
            'verify_texts': 'verifyTexts',
            'network_configuration': 'networkConfiguration'
        }

        self._config_type = None
        self._is_failure_retried = None
        self._is_certificate_validation_enabled = None
        self._verify_texts = None
        self._network_configuration = None
        self._config_type = 'BROWSER_CONFIG'

    @property
    def is_certificate_validation_enabled(self):
        """
        Gets the is_certificate_validation_enabled of this BrowserMonitorConfiguration.
        If certificate validation is enabled, then the call will fail in case of certification errors.


        :return: The is_certificate_validation_enabled of this BrowserMonitorConfiguration.
        :rtype: bool
        """
        return self._is_certificate_validation_enabled

    @is_certificate_validation_enabled.setter
    def is_certificate_validation_enabled(self, is_certificate_validation_enabled):
        """
        Sets the is_certificate_validation_enabled of this BrowserMonitorConfiguration.
        If certificate validation is enabled, then the call will fail in case of certification errors.


        :param is_certificate_validation_enabled: The is_certificate_validation_enabled of this BrowserMonitorConfiguration.
        :type: bool
        """
        self._is_certificate_validation_enabled = is_certificate_validation_enabled

    @property
    def verify_texts(self):
        """
        Gets the verify_texts of this BrowserMonitorConfiguration.
        Verifies all the search strings present in the response.
        If any search string is not present in the response, then it will be considered as a failure.


        :return: The verify_texts of this BrowserMonitorConfiguration.
        :rtype: list[oci.apm_synthetics.models.VerifyText]
        """
        return self._verify_texts

    @verify_texts.setter
    def verify_texts(self, verify_texts):
        """
        Sets the verify_texts of this BrowserMonitorConfiguration.
        Verifies all the search strings present in the response.
        If any search string is not present in the response, then it will be considered as a failure.


        :param verify_texts: The verify_texts of this BrowserMonitorConfiguration.
        :type: list[oci.apm_synthetics.models.VerifyText]
        """
        self._verify_texts = verify_texts

    @property
    def network_configuration(self):
        """
        Gets the network_configuration of this BrowserMonitorConfiguration.

        :return: The network_configuration of this BrowserMonitorConfiguration.
        :rtype: oci.apm_synthetics.models.NetworkConfiguration
        """
        return self._network_configuration

    @network_configuration.setter
    def network_configuration(self, network_configuration):
        """
        Sets the network_configuration of this BrowserMonitorConfiguration.

        :param network_configuration: The network_configuration of this BrowserMonitorConfiguration.
        :type: oci.apm_synthetics.models.NetworkConfiguration
        """
        self._network_configuration = network_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
