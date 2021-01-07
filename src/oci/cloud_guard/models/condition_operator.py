# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConditionOperator(object):
    """
    Conditions related to the parameter data type
    """

    #: A constant which can be used with the name property of a ConditionOperator.
    #: This constant has a value of "AND"
    NAME_AND = "AND"

    #: A constant which can be used with the name property of a ConditionOperator.
    #: This constant has a value of "OR"
    NAME_OR = "OR"

    #: A constant which can be used with the name property of a ConditionOperator.
    #: This constant has a value of "IN"
    NAME_IN = "IN"

    #: A constant which can be used with the name property of a ConditionOperator.
    #: This constant has a value of "NOT_IN"
    NAME_NOT_IN = "NOT_IN"

    #: A constant which can be used with the name property of a ConditionOperator.
    #: This constant has a value of "EQUALS"
    NAME_EQUALS = "EQUALS"

    #: A constant which can be used with the name property of a ConditionOperator.
    #: This constant has a value of "NOT_EQUALS"
    NAME_NOT_EQUALS = "NOT_EQUALS"

    #: A constant which can be used with the name property of a ConditionOperator.
    #: This constant has a value of "LESS_THAN"
    NAME_LESS_THAN = "LESS_THAN"

    #: A constant which can be used with the name property of a ConditionOperator.
    #: This constant has a value of "GREATER_THAN"
    NAME_GREATER_THAN = "GREATER_THAN"

    #: A constant which can be used with the name property of a ConditionOperator.
    #: This constant has a value of "RANGE"
    NAME_RANGE = "RANGE"

    def __init__(self, **kwargs):
        """
        Initializes a new ConditionOperator object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ConditionOperator.
            Allowed values for this property are: "AND", "OR", "IN", "NOT_IN", "EQUALS", "NOT_EQUALS", "LESS_THAN", "GREATER_THAN", "RANGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this ConditionOperator.
        :type display_name: str

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName'
        }

        self._name = None
        self._display_name = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ConditionOperator.
        operator name

        Allowed values for this property are: "AND", "OR", "IN", "NOT_IN", "EQUALS", "NOT_EQUALS", "LESS_THAN", "GREATER_THAN", "RANGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this ConditionOperator.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConditionOperator.
        operator name


        :param name: The name of this ConditionOperator.
        :type: str
        """
        allowed_values = ["AND", "OR", "IN", "NOT_IN", "EQUALS", "NOT_EQUALS", "LESS_THAN", "GREATER_THAN", "RANGE"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ConditionOperator.
        display name of the operator


        :return: The display_name of this ConditionOperator.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ConditionOperator.
        display name of the operator


        :param display_name: The display_name of this ConditionOperator.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
