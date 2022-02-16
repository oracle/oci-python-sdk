# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigParameterValue(object):
    """
    Contains the parameter configuration values.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigParameterValue object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param string_value:
            The value to assign to the string_value property of this ConfigParameterValue.
        :type string_value: str

        :param int_value:
            The value to assign to the int_value property of this ConfigParameterValue.
        :type int_value: int

        :param object_value:
            The value to assign to the object_value property of this ConfigParameterValue.
        :type object_value: object

        :param ref_value:
            The value to assign to the ref_value property of this ConfigParameterValue.
        :type ref_value: object

        :param parameter_value:
            The value to assign to the parameter_value property of this ConfigParameterValue.
        :type parameter_value: str

        """
        self.swagger_types = {
            'string_value': 'str',
            'int_value': 'int',
            'object_value': 'object',
            'ref_value': 'object',
            'parameter_value': 'str'
        }

        self.attribute_map = {
            'string_value': 'stringValue',
            'int_value': 'intValue',
            'object_value': 'objectValue',
            'ref_value': 'refValue',
            'parameter_value': 'parameterValue'
        }

        self._string_value = None
        self._int_value = None
        self._object_value = None
        self._ref_value = None
        self._parameter_value = None

    @property
    def string_value(self):
        """
        Gets the string_value of this ConfigParameterValue.
        A string value of the parameter.


        :return: The string_value of this ConfigParameterValue.
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value):
        """
        Sets the string_value of this ConfigParameterValue.
        A string value of the parameter.


        :param string_value: The string_value of this ConfigParameterValue.
        :type: str
        """
        self._string_value = string_value

    @property
    def int_value(self):
        """
        Gets the int_value of this ConfigParameterValue.
        An integer value of the parameter.


        :return: The int_value of this ConfigParameterValue.
        :rtype: int
        """
        return self._int_value

    @int_value.setter
    def int_value(self, int_value):
        """
        Sets the int_value of this ConfigParameterValue.
        An integer value of the parameter.


        :param int_value: The int_value of this ConfigParameterValue.
        :type: int
        """
        self._int_value = int_value

    @property
    def object_value(self):
        """
        Gets the object_value of this ConfigParameterValue.
        An object value of the parameter.


        :return: The object_value of this ConfigParameterValue.
        :rtype: object
        """
        return self._object_value

    @object_value.setter
    def object_value(self, object_value):
        """
        Sets the object_value of this ConfigParameterValue.
        An object value of the parameter.


        :param object_value: The object_value of this ConfigParameterValue.
        :type: object
        """
        self._object_value = object_value

    @property
    def ref_value(self):
        """
        Gets the ref_value of this ConfigParameterValue.
        The root object reference value.


        :return: The ref_value of this ConfigParameterValue.
        :rtype: object
        """
        return self._ref_value

    @ref_value.setter
    def ref_value(self, ref_value):
        """
        Sets the ref_value of this ConfigParameterValue.
        The root object reference value.


        :param ref_value: The ref_value of this ConfigParameterValue.
        :type: object
        """
        self._ref_value = ref_value

    @property
    def parameter_value(self):
        """
        Gets the parameter_value of this ConfigParameterValue.
        Reference to the parameter by its key.


        :return: The parameter_value of this ConfigParameterValue.
        :rtype: str
        """
        return self._parameter_value

    @parameter_value.setter
    def parameter_value(self, parameter_value):
        """
        Sets the parameter_value of this ConfigParameterValue.
        Reference to the parameter by its key.


        :param parameter_value: The parameter_value of this ConfigParameterValue.
        :type: str
        """
        self._parameter_value = parameter_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
