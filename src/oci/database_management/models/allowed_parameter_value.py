# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AllowedParameterValue(object):
    """
    A valid value for a database parameter.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AllowedParameterValue object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ordinal:
            The value to assign to the ordinal property of this AllowedParameterValue.
        :type ordinal: float

        :param value:
            The value to assign to the value property of this AllowedParameterValue.
        :type value: str

        :param is_default:
            The value to assign to the is_default property of this AllowedParameterValue.
        :type is_default: bool

        """
        self.swagger_types = {
            'ordinal': 'float',
            'value': 'str',
            'is_default': 'bool'
        }
        self.attribute_map = {
            'ordinal': 'ordinal',
            'value': 'value',
            'is_default': 'isDefault'
        }
        self._ordinal = None
        self._value = None
        self._is_default = None

    @property
    def ordinal(self):
        """
        Gets the ordinal of this AllowedParameterValue.
        The ordinal number in the list (1-based).


        :return: The ordinal of this AllowedParameterValue.
        :rtype: float
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """
        Sets the ordinal of this AllowedParameterValue.
        The ordinal number in the list (1-based).


        :param ordinal: The ordinal of this AllowedParameterValue.
        :type: float
        """
        self._ordinal = ordinal

    @property
    def value(self):
        """
        Gets the value of this AllowedParameterValue.
        The parameter value at ordinal.


        :return: The value of this AllowedParameterValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AllowedParameterValue.
        The parameter value at ordinal.


        :param value: The value of this AllowedParameterValue.
        :type: str
        """
        self._value = value

    @property
    def is_default(self):
        """
        Gets the is_default of this AllowedParameterValue.
        Indicates whether the given ordinal value is the default value for the parameter.


        :return: The is_default of this AllowedParameterValue.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this AllowedParameterValue.
        Indicates whether the given ordinal value is the default value for the parameter.


        :param is_default: The is_default of this AllowedParameterValue.
        :type: bool
        """
        self._is_default = is_default

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
