# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsSourceDataFilter(object):
    """
    LogAnalyticsSourceDataFilter
    """

    #: A constant which can be used with the filter_type property of a LogAnalyticsSourceDataFilter.
    #: This constant has a value of "MASK"
    FILTER_TYPE_MASK = "MASK"

    #: A constant which can be used with the filter_type property of a LogAnalyticsSourceDataFilter.
    #: This constant has a value of "HASH_MASK"
    FILTER_TYPE_HASH_MASK = "HASH_MASK"

    #: A constant which can be used with the filter_type property of a LogAnalyticsSourceDataFilter.
    #: This constant has a value of "DROP_LOG_ENTRY"
    FILTER_TYPE_DROP_LOG_ENTRY = "DROP_LOG_ENTRY"

    #: A constant which can be used with the filter_type property of a LogAnalyticsSourceDataFilter.
    #: This constant has a value of "DROP_STRING"
    FILTER_TYPE_DROP_STRING = "DROP_STRING"

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsSourceDataFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param description:
            The value to assign to the description property of this LogAnalyticsSourceDataFilter.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this LogAnalyticsSourceDataFilter.
        :type display_name: str

        :param edit_version:
            The value to assign to the edit_version property of this LogAnalyticsSourceDataFilter.
        :type edit_version: int

        :param is_enabled:
            The value to assign to the is_enabled property of this LogAnalyticsSourceDataFilter.
        :type is_enabled: bool

        :param field_name:
            The value to assign to the field_name property of this LogAnalyticsSourceDataFilter.
        :type field_name: str

        :param hash_type:
            The value to assign to the hash_type property of this LogAnalyticsSourceDataFilter.
        :type hash_type: int

        :param data_filter_id:
            The value to assign to the data_filter_id property of this LogAnalyticsSourceDataFilter.
        :type data_filter_id: int

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsSourceDataFilter.
        :type is_system: bool

        :param match_regular_expression:
            The value to assign to the match_regular_expression property of this LogAnalyticsSourceDataFilter.
        :type match_regular_expression: str

        :param order:
            The value to assign to the order property of this LogAnalyticsSourceDataFilter.
        :type order: int

        :param path:
            The value to assign to the path property of this LogAnalyticsSourceDataFilter.
        :type path: str

        :param replacement_string:
            The value to assign to the replacement_string property of this LogAnalyticsSourceDataFilter.
        :type replacement_string: str

        :param source_id:
            The value to assign to the source_id property of this LogAnalyticsSourceDataFilter.
        :type source_id: int

        :param filter_type:
            The value to assign to the filter_type property of this LogAnalyticsSourceDataFilter.
            Allowed values for this property are: "MASK", "HASH_MASK", "DROP_LOG_ENTRY", "DROP_STRING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type filter_type: str

        """
        self.swagger_types = {
            'description': 'str',
            'display_name': 'str',
            'edit_version': 'int',
            'is_enabled': 'bool',
            'field_name': 'str',
            'hash_type': 'int',
            'data_filter_id': 'int',
            'is_system': 'bool',
            'match_regular_expression': 'str',
            'order': 'int',
            'path': 'str',
            'replacement_string': 'str',
            'source_id': 'int',
            'filter_type': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'display_name': 'displayName',
            'edit_version': 'editVersion',
            'is_enabled': 'isEnabled',
            'field_name': 'fieldName',
            'hash_type': 'hashType',
            'data_filter_id': 'dataFilterId',
            'is_system': 'isSystem',
            'match_regular_expression': 'matchRegularExpression',
            'order': 'order',
            'path': 'path',
            'replacement_string': 'replacementString',
            'source_id': 'sourceId',
            'filter_type': 'filterType'
        }

        self._description = None
        self._display_name = None
        self._edit_version = None
        self._is_enabled = None
        self._field_name = None
        self._hash_type = None
        self._data_filter_id = None
        self._is_system = None
        self._match_regular_expression = None
        self._order = None
        self._path = None
        self._replacement_string = None
        self._source_id = None
        self._filter_type = None

    @property
    def description(self):
        """
        Gets the description of this LogAnalyticsSourceDataFilter.
        The filter description.


        :return: The description of this LogAnalyticsSourceDataFilter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LogAnalyticsSourceDataFilter.
        The filter description.


        :param description: The description of this LogAnalyticsSourceDataFilter.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        Gets the display_name of this LogAnalyticsSourceDataFilter.
        The filter display name.


        :return: The display_name of this LogAnalyticsSourceDataFilter.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this LogAnalyticsSourceDataFilter.
        The filter display name.


        :param display_name: The display_name of this LogAnalyticsSourceDataFilter.
        :type: str
        """
        self._display_name = display_name

    @property
    def edit_version(self):
        """
        Gets the edit_version of this LogAnalyticsSourceDataFilter.
        The filter edit version.


        :return: The edit_version of this LogAnalyticsSourceDataFilter.
        :rtype: int
        """
        return self._edit_version

    @edit_version.setter
    def edit_version(self, edit_version):
        """
        Sets the edit_version of this LogAnalyticsSourceDataFilter.
        The filter edit version.


        :param edit_version: The edit_version of this LogAnalyticsSourceDataFilter.
        :type: int
        """
        self._edit_version = edit_version

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this LogAnalyticsSourceDataFilter.
        A flag inidcating whether or not the filter is enabled.


        :return: The is_enabled of this LogAnalyticsSourceDataFilter.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this LogAnalyticsSourceDataFilter.
        A flag inidcating whether or not the filter is enabled.


        :param is_enabled: The is_enabled of this LogAnalyticsSourceDataFilter.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def field_name(self):
        """
        Gets the field_name of this LogAnalyticsSourceDataFilter.
        The field internal name.


        :return: The field_name of this LogAnalyticsSourceDataFilter.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this LogAnalyticsSourceDataFilter.
        The field internal name.


        :param field_name: The field_name of this LogAnalyticsSourceDataFilter.
        :type: str
        """
        self._field_name = field_name

    @property
    def hash_type(self):
        """
        Gets the hash_type of this LogAnalyticsSourceDataFilter.
        The hash type.


        :return: The hash_type of this LogAnalyticsSourceDataFilter.
        :rtype: int
        """
        return self._hash_type

    @hash_type.setter
    def hash_type(self, hash_type):
        """
        Sets the hash_type of this LogAnalyticsSourceDataFilter.
        The hash type.


        :param hash_type: The hash_type of this LogAnalyticsSourceDataFilter.
        :type: int
        """
        self._hash_type = hash_type

    @property
    def data_filter_id(self):
        """
        Gets the data_filter_id of this LogAnalyticsSourceDataFilter.
        The filter unique identifier.


        :return: The data_filter_id of this LogAnalyticsSourceDataFilter.
        :rtype: int
        """
        return self._data_filter_id

    @data_filter_id.setter
    def data_filter_id(self, data_filter_id):
        """
        Sets the data_filter_id of this LogAnalyticsSourceDataFilter.
        The filter unique identifier.


        :param data_filter_id: The data_filter_id of this LogAnalyticsSourceDataFilter.
        :type: int
        """
        self._data_filter_id = data_filter_id

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsSourceDataFilter.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :return: The is_system of this LogAnalyticsSourceDataFilter.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsSourceDataFilter.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :param is_system: The is_system of this LogAnalyticsSourceDataFilter.
        :type: bool
        """
        self._is_system = is_system

    @property
    def match_regular_expression(self):
        """
        Gets the match_regular_expression of this LogAnalyticsSourceDataFilter.
        The regular expression for matching.


        :return: The match_regular_expression of this LogAnalyticsSourceDataFilter.
        :rtype: str
        """
        return self._match_regular_expression

    @match_regular_expression.setter
    def match_regular_expression(self, match_regular_expression):
        """
        Sets the match_regular_expression of this LogAnalyticsSourceDataFilter.
        The regular expression for matching.


        :param match_regular_expression: The match_regular_expression of this LogAnalyticsSourceDataFilter.
        :type: str
        """
        self._match_regular_expression = match_regular_expression

    @property
    def order(self):
        """
        Gets the order of this LogAnalyticsSourceDataFilter.
        The filter order.


        :return: The order of this LogAnalyticsSourceDataFilter.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this LogAnalyticsSourceDataFilter.
        The filter order.


        :param order: The order of this LogAnalyticsSourceDataFilter.
        :type: int
        """
        self._order = order

    @property
    def path(self):
        """
        Gets the path of this LogAnalyticsSourceDataFilter.
        The filter path.


        :return: The path of this LogAnalyticsSourceDataFilter.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this LogAnalyticsSourceDataFilter.
        The filter path.


        :param path: The path of this LogAnalyticsSourceDataFilter.
        :type: str
        """
        self._path = path

    @property
    def replacement_string(self):
        """
        Gets the replacement_string of this LogAnalyticsSourceDataFilter.
        The replacement string.


        :return: The replacement_string of this LogAnalyticsSourceDataFilter.
        :rtype: str
        """
        return self._replacement_string

    @replacement_string.setter
    def replacement_string(self, replacement_string):
        """
        Sets the replacement_string of this LogAnalyticsSourceDataFilter.
        The replacement string.


        :param replacement_string: The replacement_string of this LogAnalyticsSourceDataFilter.
        :type: str
        """
        self._replacement_string = replacement_string

    @property
    def source_id(self):
        """
        Gets the source_id of this LogAnalyticsSourceDataFilter.
        The source unique identifier.


        :return: The source_id of this LogAnalyticsSourceDataFilter.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LogAnalyticsSourceDataFilter.
        The source unique identifier.


        :param source_id: The source_id of this LogAnalyticsSourceDataFilter.
        :type: int
        """
        self._source_id = source_id

    @property
    def filter_type(self):
        """
        Gets the filter_type of this LogAnalyticsSourceDataFilter.
        The filter type.

        Allowed values for this property are: "MASK", "HASH_MASK", "DROP_LOG_ENTRY", "DROP_STRING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The filter_type of this LogAnalyticsSourceDataFilter.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """
        Sets the filter_type of this LogAnalyticsSourceDataFilter.
        The filter type.


        :param filter_type: The filter_type of this LogAnalyticsSourceDataFilter.
        :type: str
        """
        allowed_values = ["MASK", "HASH_MASK", "DROP_LOG_ENTRY", "DROP_STRING"]
        if not value_allowed_none_or_none_sentinel(filter_type, allowed_values):
            filter_type = 'UNKNOWN_ENUM_VALUE'
        self._filter_type = filter_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
