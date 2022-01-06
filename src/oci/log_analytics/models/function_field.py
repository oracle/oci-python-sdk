# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_field import AbstractField
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FunctionField(AbstractField):
    """
    Field outlining queryString aggregate function entries.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FunctionField object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.FunctionField.name` attribute
        of this class is ``FUNCTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this FunctionField.
            Allowed values for this property are: "FIELD", "FIELDS", "FUNCTION", "SORT"
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this FunctionField.
        :type display_name: str

        :param is_declared:
            The value to assign to the is_declared property of this FunctionField.
        :type is_declared: bool

        :param original_display_names:
            The value to assign to the original_display_names property of this FunctionField.
        :type original_display_names: list[str]

        :param internal_name:
            The value to assign to the internal_name property of this FunctionField.
        :type internal_name: str

        :param value_type:
            The value to assign to the value_type property of this FunctionField.
            Allowed values for this property are: "BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET"
        :type value_type: str

        :param is_groupable:
            The value to assign to the is_groupable property of this FunctionField.
        :type is_groupable: bool

        :param is_duration:
            The value to assign to the is_duration property of this FunctionField.
        :type is_duration: bool

        :param alias:
            The value to assign to the alias property of this FunctionField.
        :type alias: str

        :param filter_query_string:
            The value to assign to the filter_query_string property of this FunctionField.
        :type filter_query_string: str

        :param unit_type:
            The value to assign to the unit_type property of this FunctionField.
        :type unit_type: str

        :param function:
            The value to assign to the function property of this FunctionField.
        :type function: str

        :param arguments:
            The value to assign to the arguments property of this FunctionField.
        :type arguments: list[oci.log_analytics.models.Argument]

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'is_declared': 'bool',
            'original_display_names': 'list[str]',
            'internal_name': 'str',
            'value_type': 'str',
            'is_groupable': 'bool',
            'is_duration': 'bool',
            'alias': 'str',
            'filter_query_string': 'str',
            'unit_type': 'str',
            'function': 'str',
            'arguments': 'list[Argument]'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'is_declared': 'isDeclared',
            'original_display_names': 'originalDisplayNames',
            'internal_name': 'internalName',
            'value_type': 'valueType',
            'is_groupable': 'isGroupable',
            'is_duration': 'isDuration',
            'alias': 'alias',
            'filter_query_string': 'filterQueryString',
            'unit_type': 'unitType',
            'function': 'function',
            'arguments': 'arguments'
        }

        self._name = None
        self._display_name = None
        self._is_declared = None
        self._original_display_names = None
        self._internal_name = None
        self._value_type = None
        self._is_groupable = None
        self._is_duration = None
        self._alias = None
        self._filter_query_string = None
        self._unit_type = None
        self._function = None
        self._arguments = None
        self._name = 'FUNCTION'

    @property
    def function(self):
        """
        Gets the function of this FunctionField.
        Name of the aggregate function.


        :return: The function of this FunctionField.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """
        Sets the function of this FunctionField.
        Name of the aggregate function.


        :param function: The function of this FunctionField.
        :type: str
        """
        self._function = function

    @property
    def arguments(self):
        """
        Gets the arguments of this FunctionField.
        List of function arguments if specified.


        :return: The arguments of this FunctionField.
        :rtype: list[oci.log_analytics.models.Argument]
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """
        Sets the arguments of this FunctionField.
        List of function arguments if specified.


        :param arguments: The arguments of this FunctionField.
        :type: list[oci.log_analytics.models.Argument]
        """
        self._arguments = arguments

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
