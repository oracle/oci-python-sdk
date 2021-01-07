# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AbstractColumn(object):
    """
    Generic column defining all attributes common to all querylanguage columns.
    """

    #: A constant which can be used with the type property of a AbstractColumn.
    #: This constant has a value of "COLUMN"
    TYPE_COLUMN = "COLUMN"

    #: A constant which can be used with the type property of a AbstractColumn.
    #: This constant has a value of "CHART_COLUMN"
    TYPE_CHART_COLUMN = "CHART_COLUMN"

    #: A constant which can be used with the type property of a AbstractColumn.
    #: This constant has a value of "CHART_DATA_COLUMN"
    TYPE_CHART_DATA_COLUMN = "CHART_DATA_COLUMN"

    #: A constant which can be used with the type property of a AbstractColumn.
    #: This constant has a value of "TIME_COLUMN"
    TYPE_TIME_COLUMN = "TIME_COLUMN"

    #: A constant which can be used with the type property of a AbstractColumn.
    #: This constant has a value of "TREND_COLUMN"
    TYPE_TREND_COLUMN = "TREND_COLUMN"

    #: A constant which can be used with the type property of a AbstractColumn.
    #: This constant has a value of "CLASSIFY_COLUMN"
    TYPE_CLASSIFY_COLUMN = "CLASSIFY_COLUMN"

    #: A constant which can be used with the sub_system property of a AbstractColumn.
    #: This constant has a value of "LOG"
    SUB_SYSTEM_LOG = "LOG"

    #: A constant which can be used with the value_type property of a AbstractColumn.
    #: This constant has a value of "BOOLEAN"
    VALUE_TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the value_type property of a AbstractColumn.
    #: This constant has a value of "STRING"
    VALUE_TYPE_STRING = "STRING"

    #: A constant which can be used with the value_type property of a AbstractColumn.
    #: This constant has a value of "DOUBLE"
    VALUE_TYPE_DOUBLE = "DOUBLE"

    #: A constant which can be used with the value_type property of a AbstractColumn.
    #: This constant has a value of "FLOAT"
    VALUE_TYPE_FLOAT = "FLOAT"

    #: A constant which can be used with the value_type property of a AbstractColumn.
    #: This constant has a value of "LONG"
    VALUE_TYPE_LONG = "LONG"

    #: A constant which can be used with the value_type property of a AbstractColumn.
    #: This constant has a value of "INTEGER"
    VALUE_TYPE_INTEGER = "INTEGER"

    #: A constant which can be used with the value_type property of a AbstractColumn.
    #: This constant has a value of "TIMESTAMP"
    VALUE_TYPE_TIMESTAMP = "TIMESTAMP"

    #: A constant which can be used with the value_type property of a AbstractColumn.
    #: This constant has a value of "FACET"
    VALUE_TYPE_FACET = "FACET"

    def __init__(self, **kwargs):
        """
        Initializes a new AbstractColumn object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.log_analytics.models.TimeColumn`
        * :class:`~oci.log_analytics.models.ClassifyColumn`
        * :class:`~oci.log_analytics.models.TrendColumn`
        * :class:`~oci.log_analytics.models.Column`
        * :class:`~oci.log_analytics.models.ChartColumn`
        * :class:`~oci.log_analytics.models.ChartDataColumn`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AbstractColumn.
            Allowed values for this property are: "COLUMN", "CHART_COLUMN", "CHART_DATA_COLUMN", "TIME_COLUMN", "TREND_COLUMN", "CLASSIFY_COLUMN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param display_name:
            The value to assign to the display_name property of this AbstractColumn.
        :type display_name: str

        :param sub_system:
            The value to assign to the sub_system property of this AbstractColumn.
            Allowed values for this property are: "LOG", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type sub_system: str

        :param values:
            The value to assign to the values property of this AbstractColumn.
        :type values: list[oci.log_analytics.models.FieldValue]

        :param is_list_of_values:
            The value to assign to the is_list_of_values property of this AbstractColumn.
        :type is_list_of_values: bool

        :param is_multi_valued:
            The value to assign to the is_multi_valued property of this AbstractColumn.
        :type is_multi_valued: bool

        :param is_groupable:
            The value to assign to the is_groupable property of this AbstractColumn.
        :type is_groupable: bool

        :param is_evaluable:
            The value to assign to the is_evaluable property of this AbstractColumn.
        :type is_evaluable: bool

        :param value_type:
            The value to assign to the value_type property of this AbstractColumn.
            Allowed values for this property are: "BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type value_type: str

        :param original_display_name:
            The value to assign to the original_display_name property of this AbstractColumn.
        :type original_display_name: str

        :param internal_name:
            The value to assign to the internal_name property of this AbstractColumn.
        :type internal_name: str

        """
        self.swagger_types = {
            'type': 'str',
            'display_name': 'str',
            'sub_system': 'str',
            'values': 'list[FieldValue]',
            'is_list_of_values': 'bool',
            'is_multi_valued': 'bool',
            'is_groupable': 'bool',
            'is_evaluable': 'bool',
            'value_type': 'str',
            'original_display_name': 'str',
            'internal_name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'display_name': 'displayName',
            'sub_system': 'subSystem',
            'values': 'values',
            'is_list_of_values': 'isListOfValues',
            'is_multi_valued': 'isMultiValued',
            'is_groupable': 'isGroupable',
            'is_evaluable': 'isEvaluable',
            'value_type': 'valueType',
            'original_display_name': 'originalDisplayName',
            'internal_name': 'internalName'
        }

        self._type = None
        self._display_name = None
        self._sub_system = None
        self._values = None
        self._is_list_of_values = None
        self._is_multi_valued = None
        self._is_groupable = None
        self._is_evaluable = None
        self._value_type = None
        self._original_display_name = None
        self._internal_name = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'TIME_COLUMN':
            return 'TimeColumn'

        if type == 'CLASSIFY_COLUMN':
            return 'ClassifyColumn'

        if type == 'TREND_COLUMN':
            return 'TrendColumn'

        if type == 'COLUMN':
            return 'Column'

        if type == 'CHART_COLUMN':
            return 'ChartColumn'

        if type == 'CHART_DATA_COLUMN':
            return 'ChartDataColumn'
        else:
            return 'AbstractColumn'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AbstractColumn.
        Column classification when column requires special designation.

        Allowed values for this property are: "COLUMN", "CHART_COLUMN", "CHART_DATA_COLUMN", "TIME_COLUMN", "TREND_COLUMN", "CLASSIFY_COLUMN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AbstractColumn.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AbstractColumn.
        Column classification when column requires special designation.


        :param type: The type of this AbstractColumn.
        :type: str
        """
        allowed_values = ["COLUMN", "CHART_COLUMN", "CHART_DATA_COLUMN", "TIME_COLUMN", "TREND_COLUMN", "CLASSIFY_COLUMN"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def display_name(self):
        """
        Gets the display_name of this AbstractColumn.
        Column display name - will be alias if column is renamed by queryStrng.


        :return: The display_name of this AbstractColumn.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AbstractColumn.
        Column display name - will be alias if column is renamed by queryStrng.


        :param display_name: The display_name of this AbstractColumn.
        :type: str
        """
        self._display_name = display_name

    @property
    def sub_system(self):
        """
        Gets the sub_system of this AbstractColumn.
        Subsystem column belongs to.

        Allowed values for this property are: "LOG", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The sub_system of this AbstractColumn.
        :rtype: str
        """
        return self._sub_system

    @sub_system.setter
    def sub_system(self, sub_system):
        """
        Sets the sub_system of this AbstractColumn.
        Subsystem column belongs to.


        :param sub_system: The sub_system of this AbstractColumn.
        :type: str
        """
        allowed_values = ["LOG"]
        if not value_allowed_none_or_none_sentinel(sub_system, allowed_values):
            sub_system = 'UNKNOWN_ENUM_VALUE'
        self._sub_system = sub_system

    @property
    def values(self):
        """
        Gets the values of this AbstractColumn.
        If the column is a 'List of Values' column, this array contains the field values that are applicable to query results or all if no filters applied.


        :return: The values of this AbstractColumn.
        :rtype: list[oci.log_analytics.models.FieldValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this AbstractColumn.
        If the column is a 'List of Values' column, this array contains the field values that are applicable to query results or all if no filters applied.


        :param values: The values of this AbstractColumn.
        :type: list[oci.log_analytics.models.FieldValue]
        """
        self._values = values

    @property
    def is_list_of_values(self):
        """
        Gets the is_list_of_values of this AbstractColumn.
        Identifies if all values in this column come from a pre-defined list of values.


        :return: The is_list_of_values of this AbstractColumn.
        :rtype: bool
        """
        return self._is_list_of_values

    @is_list_of_values.setter
    def is_list_of_values(self, is_list_of_values):
        """
        Sets the is_list_of_values of this AbstractColumn.
        Identifies if all values in this column come from a pre-defined list of values.


        :param is_list_of_values: The is_list_of_values of this AbstractColumn.
        :type: bool
        """
        self._is_list_of_values = is_list_of_values

    @property
    def is_multi_valued(self):
        """
        Gets the is_multi_valued of this AbstractColumn.
        Identifies if this column allows multiple values to exist in a single row.


        :return: The is_multi_valued of this AbstractColumn.
        :rtype: bool
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued):
        """
        Sets the is_multi_valued of this AbstractColumn.
        Identifies if this column allows multiple values to exist in a single row.


        :param is_multi_valued: The is_multi_valued of this AbstractColumn.
        :type: bool
        """
        self._is_multi_valued = is_multi_valued

    @property
    def is_groupable(self):
        """
        Gets the is_groupable of this AbstractColumn.
        Identifies if this column can be used as a grouping field in any grouping command.


        :return: The is_groupable of this AbstractColumn.
        :rtype: bool
        """
        return self._is_groupable

    @is_groupable.setter
    def is_groupable(self, is_groupable):
        """
        Sets the is_groupable of this AbstractColumn.
        Identifies if this column can be used as a grouping field in any grouping command.


        :param is_groupable: The is_groupable of this AbstractColumn.
        :type: bool
        """
        self._is_groupable = is_groupable

    @property
    def is_evaluable(self):
        """
        Gets the is_evaluable of this AbstractColumn.
        Identifies if this column can be used as an expression parameter in any command that accepts querylanguage expressions.


        :return: The is_evaluable of this AbstractColumn.
        :rtype: bool
        """
        return self._is_evaluable

    @is_evaluable.setter
    def is_evaluable(self, is_evaluable):
        """
        Sets the is_evaluable of this AbstractColumn.
        Identifies if this column can be used as an expression parameter in any command that accepts querylanguage expressions.


        :param is_evaluable: The is_evaluable of this AbstractColumn.
        :type: bool
        """
        self._is_evaluable = is_evaluable

    @property
    def value_type(self):
        """
        Gets the value_type of this AbstractColumn.
        Field denoting column data type.

        Allowed values for this property are: "BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The value_type of this AbstractColumn.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """
        Sets the value_type of this AbstractColumn.
        Field denoting column data type.


        :param value_type: The value_type of this AbstractColumn.
        :type: str
        """
        allowed_values = ["BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET"]
        if not value_allowed_none_or_none_sentinel(value_type, allowed_values):
            value_type = 'UNKNOWN_ENUM_VALUE'
        self._value_type = value_type

    @property
    def original_display_name(self):
        """
        Gets the original_display_name of this AbstractColumn.
        Same as displayName unless column renamed in which case this will hold the original display name for the column.


        :return: The original_display_name of this AbstractColumn.
        :rtype: str
        """
        return self._original_display_name

    @original_display_name.setter
    def original_display_name(self, original_display_name):
        """
        Sets the original_display_name of this AbstractColumn.
        Same as displayName unless column renamed in which case this will hold the original display name for the column.


        :param original_display_name: The original_display_name of this AbstractColumn.
        :type: str
        """
        self._original_display_name = original_display_name

    @property
    def internal_name(self):
        """
        Gets the internal_name of this AbstractColumn.
        Internal identifier for the column.


        :return: The internal_name of this AbstractColumn.
        :rtype: str
        """
        return self._internal_name

    @internal_name.setter
    def internal_name(self, internal_name):
        """
        Sets the internal_name of this AbstractColumn.
        Internal identifier for the column.


        :param internal_name: The internal_name of this AbstractColumn.
        :type: str
        """
        self._internal_name = internal_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
