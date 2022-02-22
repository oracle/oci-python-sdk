# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Column(object):
    """
    Data preview column definition.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Column object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this Column.
        :type name: str

        :param data_type:
            The value to assign to the data_type property of this Column.
        :type data_type: str

        """
        self.swagger_types = {
            'name': 'str',
            'data_type': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'data_type': 'dataType'
        }

        self._name = None
        self._data_type = None

    @property
    def name(self):
        """
        Gets the name of this Column.
        Column Name.


        :return: The name of this Column.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Column.
        Column Name.


        :param name: The name of this Column.
        :type: str
        """
        self._name = name

    @property
    def data_type(self):
        """
        Gets the data_type of this Column.
        Data type of the specified column.


        :return: The data_type of this Column.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this Column.
        Data type of the specified column.


        :param data_type: The data_type of this Column.
        :type: str
        """
        self._data_type = data_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
