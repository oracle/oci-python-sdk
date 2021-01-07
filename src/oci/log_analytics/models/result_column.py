# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResultColumn(object):
    """
    Querylanguage result column.
    """

    #: A constant which can be used with the value_type property of a ResultColumn.
    #: This constant has a value of "BOOLEAN"
    VALUE_TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the value_type property of a ResultColumn.
    #: This constant has a value of "STRING"
    VALUE_TYPE_STRING = "STRING"

    #: A constant which can be used with the value_type property of a ResultColumn.
    #: This constant has a value of "DOUBLE"
    VALUE_TYPE_DOUBLE = "DOUBLE"

    #: A constant which can be used with the value_type property of a ResultColumn.
    #: This constant has a value of "FLOAT"
    VALUE_TYPE_FLOAT = "FLOAT"

    #: A constant which can be used with the value_type property of a ResultColumn.
    #: This constant has a value of "LONG"
    VALUE_TYPE_LONG = "LONG"

    #: A constant which can be used with the value_type property of a ResultColumn.
    #: This constant has a value of "INTEGER"
    VALUE_TYPE_INTEGER = "INTEGER"

    #: A constant which can be used with the value_type property of a ResultColumn.
    #: This constant has a value of "TIMESTAMP"
    VALUE_TYPE_TIMESTAMP = "TIMESTAMP"

    #: A constant which can be used with the value_type property of a ResultColumn.
    #: This constant has a value of "FACET"
    VALUE_TYPE_FACET = "FACET"

    def __init__(self, **kwargs):
        """
        Initializes a new ResultColumn object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param internal_name:
            The value to assign to the internal_name property of this ResultColumn.
        :type internal_name: str

        :param display_name:
            The value to assign to the display_name property of this ResultColumn.
        :type display_name: str

        :param value_type:
            The value to assign to the value_type property of this ResultColumn.
            Allowed values for this property are: "BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET"
        :type value_type: str

        """
        self.swagger_types = {
            'internal_name': 'str',
            'display_name': 'str',
            'value_type': 'str'
        }

        self.attribute_map = {
            'internal_name': 'internalName',
            'display_name': 'displayName',
            'value_type': 'valueType'
        }

        self._internal_name = None
        self._display_name = None
        self._value_type = None

    @property
    def internal_name(self):
        """
        Gets the internal_name of this ResultColumn.
        Internal identifier for the column.


        :return: The internal_name of this ResultColumn.
        :rtype: str
        """
        return self._internal_name

    @internal_name.setter
    def internal_name(self, internal_name):
        """
        Sets the internal_name of this ResultColumn.
        Internal identifier for the column.


        :param internal_name: The internal_name of this ResultColumn.
        :type: str
        """
        self._internal_name = internal_name

    @property
    def display_name(self):
        """
        Gets the display_name of this ResultColumn.
        Display name - will be alias if result column is renamed by queryString.


        :return: The display_name of this ResultColumn.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ResultColumn.
        Display name - will be alias if result column is renamed by queryString.


        :param display_name: The display_name of this ResultColumn.
        :type: str
        """
        self._display_name = display_name

    @property
    def value_type(self):
        """
        Gets the value_type of this ResultColumn.
        Field denoting column data type.

        Allowed values for this property are: "BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET"


        :return: The value_type of this ResultColumn.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """
        Sets the value_type of this ResultColumn.
        Field denoting column data type.


        :param value_type: The value_type of this ResultColumn.
        :type: str
        """
        allowed_values = ["BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET"]
        if not value_allowed_none_or_none_sentinel(value_type, allowed_values):
            raise ValueError(
                "Invalid value for `value_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._value_type = value_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
