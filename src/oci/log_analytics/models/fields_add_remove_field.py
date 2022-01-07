# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .abstract_field import AbstractField
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FieldsAddRemoveField(AbstractField):
    """
    Field denoting a field specified in querylanguage FIELDS command.
    """

    #: A constant which can be used with the operation property of a FieldsAddRemoveField.
    #: This constant has a value of "ADD"
    OPERATION_ADD = "ADD"

    #: A constant which can be used with the operation property of a FieldsAddRemoveField.
    #: This constant has a value of "REMOVE"
    OPERATION_REMOVE = "REMOVE"

    def __init__(self, **kwargs):
        """
        Initializes a new FieldsAddRemoveField object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.FieldsAddRemoveField.name` attribute
        of this class is ``FIELDS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this FieldsAddRemoveField.
            Allowed values for this property are: "FIELD", "FIELDS", "FUNCTION", "SORT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this FieldsAddRemoveField.
        :type display_name: str

        :param is_declared:
            The value to assign to the is_declared property of this FieldsAddRemoveField.
        :type is_declared: bool

        :param original_display_names:
            The value to assign to the original_display_names property of this FieldsAddRemoveField.
        :type original_display_names: list[str]

        :param internal_name:
            The value to assign to the internal_name property of this FieldsAddRemoveField.
        :type internal_name: str

        :param value_type:
            The value to assign to the value_type property of this FieldsAddRemoveField.
            Allowed values for this property are: "BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type value_type: str

        :param is_groupable:
            The value to assign to the is_groupable property of this FieldsAddRemoveField.
        :type is_groupable: bool

        :param is_duration:
            The value to assign to the is_duration property of this FieldsAddRemoveField.
        :type is_duration: bool

        :param alias:
            The value to assign to the alias property of this FieldsAddRemoveField.
        :type alias: str

        :param filter_query_string:
            The value to assign to the filter_query_string property of this FieldsAddRemoveField.
        :type filter_query_string: str

        :param unit_type:
            The value to assign to the unit_type property of this FieldsAddRemoveField.
        :type unit_type: str

        :param operation:
            The value to assign to the operation property of this FieldsAddRemoveField.
            Allowed values for this property are: "ADD", "REMOVE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operation: str

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
            'operation': 'str'
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
            'operation': 'operation'
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
        self._operation = None
        self._name = 'FIELDS'

    @property
    def operation(self):
        """
        Gets the operation of this FieldsAddRemoveField.
        Denotes if field entry in FIELDS command is to show / hide field in results.

        Allowed values for this property are: "ADD", "REMOVE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operation of this FieldsAddRemoveField.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this FieldsAddRemoveField.
        Denotes if field entry in FIELDS command is to show / hide field in results.


        :param operation: The operation of this FieldsAddRemoveField.
        :type: str
        """
        allowed_values = ["ADD", "REMOVE"]
        if not value_allowed_none_or_none_sentinel(operation, allowed_values):
            operation = 'UNKNOWN_ENUM_VALUE'
        self._operation = operation

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
