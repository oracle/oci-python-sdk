# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Column(object):
    """
    A column of a table.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Column object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Column.
        :type name: str

        :param type:
            The value to assign to the type property of this Column.
        :type type: str

        :param is_nullable:
            The value to assign to the is_nullable property of this Column.
        :type is_nullable: bool

        :param default_value:
            The value to assign to the default_value property of this Column.
        :type default_value: str

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'is_nullable': 'bool',
            'default_value': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'is_nullable': 'isNullable',
            'default_value': 'defaultValue'
        }

        self._name = None
        self._type = None
        self._is_nullable = None
        self._default_value = None

    @property
    def name(self):
        """
        Gets the name of this Column.
        The column name.


        :return: The name of this Column.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Column.
        The column name.


        :param name: The name of this Column.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Column.
        The column type.


        :return: The type of this Column.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Column.
        The column type.


        :param type: The type of this Column.
        :type: str
        """
        self._type = type

    @property
    def is_nullable(self):
        """
        Gets the is_nullable of this Column.
        The column nullable flag.


        :return: The is_nullable of this Column.
        :rtype: bool
        """
        return self._is_nullable

    @is_nullable.setter
    def is_nullable(self, is_nullable):
        """
        Sets the is_nullable of this Column.
        The column nullable flag.


        :param is_nullable: The is_nullable of this Column.
        :type: bool
        """
        self._is_nullable = is_nullable

    @property
    def default_value(self):
        """
        Gets the default_value of this Column.
        The column default value.


        :return: The default_value of this Column.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this Column.
        The column default value.


        :param default_value: The default_value of this Column.
        :type: str
        """
        self._default_value = default_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
