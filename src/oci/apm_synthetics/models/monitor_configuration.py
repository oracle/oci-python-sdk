# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitorConfiguration(object):
    """
    Details of monitor configuration.
    """

    #: A constant which can be used with the config_type property of a MonitorConfiguration.
    #: This constant has a value of "BROWSER_CONFIG"
    CONFIG_TYPE_BROWSER_CONFIG = "BROWSER_CONFIG"

    #: A constant which can be used with the config_type property of a MonitorConfiguration.
    #: This constant has a value of "SCRIPTED_BROWSER_CONFIG"
    CONFIG_TYPE_SCRIPTED_BROWSER_CONFIG = "SCRIPTED_BROWSER_CONFIG"

    #: A constant which can be used with the config_type property of a MonitorConfiguration.
    #: This constant has a value of "REST_CONFIG"
    CONFIG_TYPE_REST_CONFIG = "REST_CONFIG"

    #: A constant which can be used with the config_type property of a MonitorConfiguration.
    #: This constant has a value of "SCRIPTED_REST_CONFIG"
    CONFIG_TYPE_SCRIPTED_REST_CONFIG = "SCRIPTED_REST_CONFIG"

    def __init__(self, **kwargs):
        """
        Initializes a new MonitorConfiguration object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.apm_synthetics.models.ScriptedRestMonitorConfiguration`
        * :class:`~oci.apm_synthetics.models.ScriptedBrowserMonitorConfiguration`
        * :class:`~oci.apm_synthetics.models.RestMonitorConfiguration`
        * :class:`~oci.apm_synthetics.models.BrowserMonitorConfiguration`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this MonitorConfiguration.
            Allowed values for this property are: "BROWSER_CONFIG", "SCRIPTED_BROWSER_CONFIG", "REST_CONFIG", "SCRIPTED_REST_CONFIG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type config_type: str

        :param is_failure_retried:
            The value to assign to the is_failure_retried property of this MonitorConfiguration.
        :type is_failure_retried: bool

        """
        self.swagger_types = {
            'config_type': 'str',
            'is_failure_retried': 'bool'
        }

        self.attribute_map = {
            'config_type': 'configType',
            'is_failure_retried': 'isFailureRetried'
        }

        self._config_type = None
        self._is_failure_retried = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['configType']

        if type == 'SCRIPTED_REST_CONFIG':
            return 'ScriptedRestMonitorConfiguration'

        if type == 'SCRIPTED_BROWSER_CONFIG':
            return 'ScriptedBrowserMonitorConfiguration'

        if type == 'REST_CONFIG':
            return 'RestMonitorConfiguration'

        if type == 'BROWSER_CONFIG':
            return 'BrowserMonitorConfiguration'
        else:
            return 'MonitorConfiguration'

    @property
    def config_type(self):
        """
        Gets the config_type of this MonitorConfiguration.
        Type of configuration.

        Allowed values for this property are: "BROWSER_CONFIG", "SCRIPTED_BROWSER_CONFIG", "REST_CONFIG", "SCRIPTED_REST_CONFIG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The config_type of this MonitorConfiguration.
        :rtype: str
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        """
        Sets the config_type of this MonitorConfiguration.
        Type of configuration.


        :param config_type: The config_type of this MonitorConfiguration.
        :type: str
        """
        allowed_values = ["BROWSER_CONFIG", "SCRIPTED_BROWSER_CONFIG", "REST_CONFIG", "SCRIPTED_REST_CONFIG"]
        if not value_allowed_none_or_none_sentinel(config_type, allowed_values):
            config_type = 'UNKNOWN_ENUM_VALUE'
        self._config_type = config_type

    @property
    def is_failure_retried(self):
        """
        Gets the is_failure_retried of this MonitorConfiguration.
        If isFailureRetried is enabled, then a failed call will be retried.


        :return: The is_failure_retried of this MonitorConfiguration.
        :rtype: bool
        """
        return self._is_failure_retried

    @is_failure_retried.setter
    def is_failure_retried(self, is_failure_retried):
        """
        Sets the is_failure_retried of this MonitorConfiguration.
        If isFailureRetried is enabled, then a failed call will be retried.


        :param is_failure_retried: The is_failure_retried of this MonitorConfiguration.
        :type: bool
        """
        self._is_failure_retried = is_failure_retried

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
