# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitorScriptParameterInfo(object):
    """
    Details of the script parameters in the monitor.
    isOverwritten specifies that the script parameters are overwritten in the monitor.
    If the user overwrites the parameter value in the monitor, then the overwritten values will be used to run the monitor.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonitorScriptParameterInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param monitor_script_parameter:
            The value to assign to the monitor_script_parameter property of this MonitorScriptParameterInfo.
        :type monitor_script_parameter: oci.apm_synthetics.models.MonitorScriptParameter

        :param is_secret:
            The value to assign to the is_secret property of this MonitorScriptParameterInfo.
        :type is_secret: bool

        :param is_overwritten:
            The value to assign to the is_overwritten property of this MonitorScriptParameterInfo.
        :type is_overwritten: bool

        """
        self.swagger_types = {
            'monitor_script_parameter': 'MonitorScriptParameter',
            'is_secret': 'bool',
            'is_overwritten': 'bool'
        }

        self.attribute_map = {
            'monitor_script_parameter': 'monitorScriptParameter',
            'is_secret': 'isSecret',
            'is_overwritten': 'isOverwritten'
        }

        self._monitor_script_parameter = None
        self._is_secret = None
        self._is_overwritten = None

    @property
    def monitor_script_parameter(self):
        """
        **[Required]** Gets the monitor_script_parameter of this MonitorScriptParameterInfo.

        :return: The monitor_script_parameter of this MonitorScriptParameterInfo.
        :rtype: oci.apm_synthetics.models.MonitorScriptParameter
        """
        return self._monitor_script_parameter

    @monitor_script_parameter.setter
    def monitor_script_parameter(self, monitor_script_parameter):
        """
        Sets the monitor_script_parameter of this MonitorScriptParameterInfo.

        :param monitor_script_parameter: The monitor_script_parameter of this MonitorScriptParameterInfo.
        :type: oci.apm_synthetics.models.MonitorScriptParameter
        """
        self._monitor_script_parameter = monitor_script_parameter

    @property
    def is_secret(self):
        """
        **[Required]** Gets the is_secret of this MonitorScriptParameterInfo.
        Describes if  the parameter value is secret and should be kept confidential.
        isSecret is specified in either CreateScript or UpdateScript API.


        :return: The is_secret of this MonitorScriptParameterInfo.
        :rtype: bool
        """
        return self._is_secret

    @is_secret.setter
    def is_secret(self, is_secret):
        """
        Sets the is_secret of this MonitorScriptParameterInfo.
        Describes if  the parameter value is secret and should be kept confidential.
        isSecret is specified in either CreateScript or UpdateScript API.


        :param is_secret: The is_secret of this MonitorScriptParameterInfo.
        :type: bool
        """
        self._is_secret = is_secret

    @property
    def is_overwritten(self):
        """
        **[Required]** Gets the is_overwritten of this MonitorScriptParameterInfo.
        If parameter value is default or overwritten.


        :return: The is_overwritten of this MonitorScriptParameterInfo.
        :rtype: bool
        """
        return self._is_overwritten

    @is_overwritten.setter
    def is_overwritten(self, is_overwritten):
        """
        Sets the is_overwritten of this MonitorScriptParameterInfo.
        If parameter value is default or overwritten.


        :param is_overwritten: The is_overwritten of this MonitorScriptParameterInfo.
        :type: bool
        """
        self._is_overwritten = is_overwritten

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
