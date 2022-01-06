# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonitorScriptParameter(object):
    """
    Details of the script parameter that can be used to overwrite the parameter present in the script.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonitorScriptParameter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param param_name:
            The value to assign to the param_name property of this MonitorScriptParameter.
        :type param_name: str

        :param param_value:
            The value to assign to the param_value property of this MonitorScriptParameter.
        :type param_value: str

        """
        self.swagger_types = {
            'param_name': 'str',
            'param_value': 'str'
        }

        self.attribute_map = {
            'param_name': 'paramName',
            'param_value': 'paramValue'
        }

        self._param_name = None
        self._param_value = None

    @property
    def param_name(self):
        """
        **[Required]** Gets the param_name of this MonitorScriptParameter.
        Name of the parameter.


        :return: The param_name of this MonitorScriptParameter.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        """
        Sets the param_name of this MonitorScriptParameter.
        Name of the parameter.


        :param param_name: The param_name of this MonitorScriptParameter.
        :type: str
        """
        self._param_name = param_name

    @property
    def param_value(self):
        """
        **[Required]** Gets the param_value of this MonitorScriptParameter.
        Value of the parameter.


        :return: The param_value of this MonitorScriptParameter.
        :rtype: str
        """
        return self._param_value

    @param_value.setter
    def param_value(self, param_value):
        """
        Sets the param_value of this MonitorScriptParameter.
        Value of the parameter.


        :param param_value: The param_value of this MonitorScriptParameter.
        :type: str
        """
        self._param_value = param_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
