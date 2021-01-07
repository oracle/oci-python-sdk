# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .condition import Condition
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SimpleCondition(Condition):
    """
    Simple Condition object.
    """

    #: A constant which can be used with the operator property of a SimpleCondition.
    #: This constant has a value of "IN"
    OPERATOR_IN = "IN"

    #: A constant which can be used with the operator property of a SimpleCondition.
    #: This constant has a value of "NOT_IN"
    OPERATOR_NOT_IN = "NOT_IN"

    #: A constant which can be used with the operator property of a SimpleCondition.
    #: This constant has a value of "EQUALS"
    OPERATOR_EQUALS = "EQUALS"

    #: A constant which can be used with the operator property of a SimpleCondition.
    #: This constant has a value of "NOT_EQUALS"
    OPERATOR_NOT_EQUALS = "NOT_EQUALS"

    #: A constant which can be used with the value_type property of a SimpleCondition.
    #: This constant has a value of "MANAGED"
    VALUE_TYPE_MANAGED = "MANAGED"

    #: A constant which can be used with the value_type property of a SimpleCondition.
    #: This constant has a value of "CUSTOM"
    VALUE_TYPE_CUSTOM = "CUSTOM"

    def __init__(self, **kwargs):
        """
        Initializes a new SimpleCondition object with values from keyword arguments. The default value of the :py:attr:`~oci.cloud_guard.models.SimpleCondition.kind` attribute
        of this class is ``SIMPLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this SimpleCondition.
            Allowed values for this property are: "COMPOSITE", "SIMPLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type kind: str

        :param parameter:
            The value to assign to the parameter property of this SimpleCondition.
        :type parameter: str

        :param operator:
            The value to assign to the operator property of this SimpleCondition.
            Allowed values for this property are: "IN", "NOT_IN", "EQUALS", "NOT_EQUALS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operator: str

        :param value:
            The value to assign to the value property of this SimpleCondition.
        :type value: str

        :param value_type:
            The value to assign to the value_type property of this SimpleCondition.
            Allowed values for this property are: "MANAGED", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type value_type: str

        """
        self.swagger_types = {
            'kind': 'str',
            'parameter': 'str',
            'operator': 'str',
            'value': 'str',
            'value_type': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'parameter': 'parameter',
            'operator': 'operator',
            'value': 'value',
            'value_type': 'valueType'
        }

        self._kind = None
        self._parameter = None
        self._operator = None
        self._value = None
        self._value_type = None
        self._kind = 'SIMPLE'

    @property
    def parameter(self):
        """
        Gets the parameter of this SimpleCondition.
        parameter Key


        :return: The parameter of this SimpleCondition.
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """
        Sets the parameter of this SimpleCondition.
        parameter Key


        :param parameter: The parameter of this SimpleCondition.
        :type: str
        """
        self._parameter = parameter

    @property
    def operator(self):
        """
        Gets the operator of this SimpleCondition.
        type of operator

        Allowed values for this property are: "IN", "NOT_IN", "EQUALS", "NOT_EQUALS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operator of this SimpleCondition.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this SimpleCondition.
        type of operator


        :param operator: The operator of this SimpleCondition.
        :type: str
        """
        allowed_values = ["IN", "NOT_IN", "EQUALS", "NOT_EQUALS"]
        if not value_allowed_none_or_none_sentinel(operator, allowed_values):
            operator = 'UNKNOWN_ENUM_VALUE'
        self._operator = operator

    @property
    def value(self):
        """
        Gets the value of this SimpleCondition.
        type of operator


        :return: The value of this SimpleCondition.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SimpleCondition.
        type of operator


        :param value: The value of this SimpleCondition.
        :type: str
        """
        self._value = value

    @property
    def value_type(self):
        """
        Gets the value_type of this SimpleCondition.
        type of value

        Allowed values for this property are: "MANAGED", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The value_type of this SimpleCondition.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """
        Sets the value_type of this SimpleCondition.
        type of value


        :param value_type: The value_type of this SimpleCondition.
        :type: str
        """
        allowed_values = ["MANAGED", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(value_type, allowed_values):
            value_type = 'UNKNOWN_ENUM_VALUE'
        self._value_type = value_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
