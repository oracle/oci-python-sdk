# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .monitor_configuration import MonitorConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScriptedRestMonitorConfiguration(MonitorConfiguration):
    """
    Configuration details for the SCRIPTED_REST monitor type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScriptedRestMonitorConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.apm_synthetics.models.ScriptedRestMonitorConfiguration.config_type` attribute
        of this class is ``SCRIPTED_REST_CONFIG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param config_type:
            The value to assign to the config_type property of this ScriptedRestMonitorConfiguration.
            Allowed values for this property are: "BROWSER_CONFIG", "SCRIPTED_BROWSER_CONFIG", "REST_CONFIG", "SCRIPTED_REST_CONFIG"
        :type config_type: str

        :param is_failure_retried:
            The value to assign to the is_failure_retried property of this ScriptedRestMonitorConfiguration.
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
        self._config_type = 'SCRIPTED_REST_CONFIG'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
