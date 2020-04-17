# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IndexKey(object):
    """
    Specifies a single key in a secondary index.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IndexKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param column_name:
            The value to assign to the column_name property of this IndexKey.
        :type column_name: str

        :param json_path:
            The value to assign to the json_path property of this IndexKey.
        :type json_path: str

        :param json_field_type:
            The value to assign to the json_field_type property of this IndexKey.
        :type json_field_type: str

        """
        self.swagger_types = {
            'column_name': 'str',
            'json_path': 'str',
            'json_field_type': 'str'
        }

        self.attribute_map = {
            'column_name': 'columnName',
            'json_path': 'jsonPath',
            'json_field_type': 'jsonFieldType'
        }

        self._column_name = None
        self._json_path = None
        self._json_field_type = None

    @property
    def column_name(self):
        """
        **[Required]** Gets the column_name of this IndexKey.
        The name of a column to be included as an index key.


        :return: The column_name of this IndexKey.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """
        Sets the column_name of this IndexKey.
        The name of a column to be included as an index key.


        :param column_name: The column_name of this IndexKey.
        :type: str
        """
        self._column_name = column_name

    @property
    def json_path(self):
        """
        Gets the json_path of this IndexKey.
        If the specified column is of type JSON, jsonPath contains
        a dotted path indicating the field within the JSON object
        that will be the index key.


        :return: The json_path of this IndexKey.
        :rtype: str
        """
        return self._json_path

    @json_path.setter
    def json_path(self, json_path):
        """
        Sets the json_path of this IndexKey.
        If the specified column is of type JSON, jsonPath contains
        a dotted path indicating the field within the JSON object
        that will be the index key.


        :param json_path: The json_path of this IndexKey.
        :type: str
        """
        self._json_path = json_path

    @property
    def json_field_type(self):
        """
        Gets the json_field_type of this IndexKey.
        If the specified column is of type JSON, jsonFieldType contains
        the type of the field indicated by jsonPath.


        :return: The json_field_type of this IndexKey.
        :rtype: str
        """
        return self._json_field_type

    @json_field_type.setter
    def json_field_type(self, json_field_type):
        """
        Sets the json_field_type of this IndexKey.
        If the specified column is of type JSON, jsonFieldType contains
        the type of the field indicated by jsonPath.


        :param json_field_type: The json_field_type of this IndexKey.
        :type: str
        """
        self._json_field_type = json_field_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
