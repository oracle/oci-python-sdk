# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScriptParameterInfo(object):
    """
    Information about script parameters.
    isOverwritten specifies that the default parameter present in the script content is overwritten.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScriptParameterInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param script_parameter:
            The value to assign to the script_parameter property of this ScriptParameterInfo.
        :type script_parameter: oci.apm_synthetics.models.ScriptParameter

        :param is_overwritten:
            The value to assign to the is_overwritten property of this ScriptParameterInfo.
        :type is_overwritten: bool

        """
        self.swagger_types = {
            'script_parameter': 'ScriptParameter',
            'is_overwritten': 'bool'
        }

        self.attribute_map = {
            'script_parameter': 'scriptParameter',
            'is_overwritten': 'isOverwritten'
        }

        self._script_parameter = None
        self._is_overwritten = None

    @property
    def script_parameter(self):
        """
        **[Required]** Gets the script_parameter of this ScriptParameterInfo.

        :return: The script_parameter of this ScriptParameterInfo.
        :rtype: oci.apm_synthetics.models.ScriptParameter
        """
        return self._script_parameter

    @script_parameter.setter
    def script_parameter(self, script_parameter):
        """
        Sets the script_parameter of this ScriptParameterInfo.

        :param script_parameter: The script_parameter of this ScriptParameterInfo.
        :type: oci.apm_synthetics.models.ScriptParameter
        """
        self._script_parameter = script_parameter

    @property
    def is_overwritten(self):
        """
        **[Required]** Gets the is_overwritten of this ScriptParameterInfo.
        If parameter value is default or overwritten.


        :return: The is_overwritten of this ScriptParameterInfo.
        :rtype: bool
        """
        return self._is_overwritten

    @is_overwritten.setter
    def is_overwritten(self, is_overwritten):
        """
        Sets the is_overwritten of this ScriptParameterInfo.
        If parameter value is default or overwritten.


        :param is_overwritten: The is_overwritten of this ScriptParameterInfo.
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
