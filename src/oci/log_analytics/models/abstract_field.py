# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AbstractField(object):
    """
    Generic field defining all attributes common to all querylanguage fields.
    """

    #: A constant which can be used with the name property of a AbstractField.
    #: This constant has a value of "FIELD"
    NAME_FIELD = "FIELD"

    #: A constant which can be used with the name property of a AbstractField.
    #: This constant has a value of "FIELDS"
    NAME_FIELDS = "FIELDS"

    #: A constant which can be used with the name property of a AbstractField.
    #: This constant has a value of "FUNCTION"
    NAME_FUNCTION = "FUNCTION"

    #: A constant which can be used with the name property of a AbstractField.
    #: This constant has a value of "SORT"
    NAME_SORT = "SORT"

    #: A constant which can be used with the value_type property of a AbstractField.
    #: This constant has a value of "BOOLEAN"
    VALUE_TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the value_type property of a AbstractField.
    #: This constant has a value of "STRING"
    VALUE_TYPE_STRING = "STRING"

    #: A constant which can be used with the value_type property of a AbstractField.
    #: This constant has a value of "DOUBLE"
    VALUE_TYPE_DOUBLE = "DOUBLE"

    #: A constant which can be used with the value_type property of a AbstractField.
    #: This constant has a value of "FLOAT"
    VALUE_TYPE_FLOAT = "FLOAT"

    #: A constant which can be used with the value_type property of a AbstractField.
    #: This constant has a value of "LONG"
    VALUE_TYPE_LONG = "LONG"

    #: A constant which can be used with the value_type property of a AbstractField.
    #: This constant has a value of "INTEGER"
    VALUE_TYPE_INTEGER = "INTEGER"

    #: A constant which can be used with the value_type property of a AbstractField.
    #: This constant has a value of "TIMESTAMP"
    VALUE_TYPE_TIMESTAMP = "TIMESTAMP"

    #: A constant which can be used with the value_type property of a AbstractField.
    #: This constant has a value of "FACET"
    VALUE_TYPE_FACET = "FACET"

    def __init__(self, **kwargs):
        """
        Initializes a new AbstractField object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.log_analytics.models.FieldsAddRemoveField`
        * :class:`~oci.log_analytics.models.FunctionField`
        * :class:`~oci.log_analytics.models.Field`
        * :class:`~oci.log_analytics.models.SortField`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AbstractField.
            Allowed values for this property are: "FIELD", "FIELDS", "FUNCTION", "SORT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this AbstractField.
        :type display_name: str

        :param is_declared:
            The value to assign to the is_declared property of this AbstractField.
        :type is_declared: bool

        :param original_display_names:
            The value to assign to the original_display_names property of this AbstractField.
        :type original_display_names: list[str]

        :param internal_name:
            The value to assign to the internal_name property of this AbstractField.
        :type internal_name: str

        :param value_type:
            The value to assign to the value_type property of this AbstractField.
            Allowed values for this property are: "BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type value_type: str

        :param is_groupable:
            The value to assign to the is_groupable property of this AbstractField.
        :type is_groupable: bool

        :param is_duration:
            The value to assign to the is_duration property of this AbstractField.
        :type is_duration: bool

        :param alias:
            The value to assign to the alias property of this AbstractField.
        :type alias: str

        :param filter_query_string:
            The value to assign to the filter_query_string property of this AbstractField.
        :type filter_query_string: str

        :param unit_type:
            The value to assign to the unit_type property of this AbstractField.
        :type unit_type: str

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
            'unit_type': 'str'
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
            'unit_type': 'unitType'
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

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['name']

        if type == 'FIELDS':
            return 'FieldsAddRemoveField'

        if type == 'FUNCTION':
            return 'FunctionField'

        if type == 'FIELD':
            return 'Field'

        if type == 'SORT':
            return 'SortField'
        else:
            return 'AbstractField'

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AbstractField.
        Field type classification.

        Allowed values for this property are: "FIELD", "FIELDS", "FUNCTION", "SORT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this AbstractField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AbstractField.
        Field type classification.


        :param name: The name of this AbstractField.
        :type: str
        """
        allowed_values = ["FIELD", "FIELDS", "FUNCTION", "SORT"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this AbstractField.
        Field display name - will be alias if field is renamed by queryStrng.


        :return: The display_name of this AbstractField.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AbstractField.
        Field display name - will be alias if field is renamed by queryStrng.


        :param display_name: The display_name of this AbstractField.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_declared(self):
        """
        Gets the is_declared of this AbstractField.
        Field denoting if this is a declaration of the field in the queryString.


        :return: The is_declared of this AbstractField.
        :rtype: bool
        """
        return self._is_declared

    @is_declared.setter
    def is_declared(self, is_declared):
        """
        Sets the is_declared of this AbstractField.
        Field denoting if this is a declaration of the field in the queryString.


        :param is_declared: The is_declared of this AbstractField.
        :type: bool
        """
        self._is_declared = is_declared

    @property
    def original_display_names(self):
        """
        Gets the original_display_names of this AbstractField.
        Same as displayName unless field renamed in which case this will hold the original display names for the field
        across all renames.


        :return: The original_display_names of this AbstractField.
        :rtype: list[str]
        """
        return self._original_display_names

    @original_display_names.setter
    def original_display_names(self, original_display_names):
        """
        Sets the original_display_names of this AbstractField.
        Same as displayName unless field renamed in which case this will hold the original display names for the field
        across all renames.


        :param original_display_names: The original_display_names of this AbstractField.
        :type: list[str]
        """
        self._original_display_names = original_display_names

    @property
    def internal_name(self):
        """
        Gets the internal_name of this AbstractField.
        Internal identifier for the field.


        :return: The internal_name of this AbstractField.
        :rtype: str
        """
        return self._internal_name

    @internal_name.setter
    def internal_name(self, internal_name):
        """
        Sets the internal_name of this AbstractField.
        Internal identifier for the field.


        :param internal_name: The internal_name of this AbstractField.
        :type: str
        """
        self._internal_name = internal_name

    @property
    def value_type(self):
        """
        Gets the value_type of this AbstractField.
        Field denoting field data type.

        Allowed values for this property are: "BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The value_type of this AbstractField.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """
        Sets the value_type of this AbstractField.
        Field denoting field data type.


        :param value_type: The value_type of this AbstractField.
        :type: str
        """
        allowed_values = ["BOOLEAN", "STRING", "DOUBLE", "FLOAT", "LONG", "INTEGER", "TIMESTAMP", "FACET"]
        if not value_allowed_none_or_none_sentinel(value_type, allowed_values):
            value_type = 'UNKNOWN_ENUM_VALUE'
        self._value_type = value_type

    @property
    def is_groupable(self):
        """
        Gets the is_groupable of this AbstractField.
        Identifies if this field can be used as a grouping field in any grouping command.


        :return: The is_groupable of this AbstractField.
        :rtype: bool
        """
        return self._is_groupable

    @is_groupable.setter
    def is_groupable(self, is_groupable):
        """
        Sets the is_groupable of this AbstractField.
        Identifies if this field can be used as a grouping field in any grouping command.


        :param is_groupable: The is_groupable of this AbstractField.
        :type: bool
        """
        self._is_groupable = is_groupable

    @property
    def is_duration(self):
        """
        Gets the is_duration of this AbstractField.
        Identifies if this field format is a duration.


        :return: The is_duration of this AbstractField.
        :rtype: bool
        """
        return self._is_duration

    @is_duration.setter
    def is_duration(self, is_duration):
        """
        Sets the is_duration of this AbstractField.
        Identifies if this field format is a duration.


        :param is_duration: The is_duration of this AbstractField.
        :type: bool
        """
        self._is_duration = is_duration

    @property
    def alias(self):
        """
        Gets the alias of this AbstractField.
        Alias of field if renamed by queryStrng.


        :return: The alias of this AbstractField.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """
        Sets the alias of this AbstractField.
        Alias of field if renamed by queryStrng.


        :param alias: The alias of this AbstractField.
        :type: str
        """
        self._alias = alias

    @property
    def filter_query_string(self):
        """
        Gets the filter_query_string of this AbstractField.
        Query used to derive this field if specified.


        :return: The filter_query_string of this AbstractField.
        :rtype: str
        """
        return self._filter_query_string

    @filter_query_string.setter
    def filter_query_string(self, filter_query_string):
        """
        Sets the filter_query_string of this AbstractField.
        Query used to derive this field if specified.


        :param filter_query_string: The filter_query_string of this AbstractField.
        :type: str
        """
        self._filter_query_string = filter_query_string

    @property
    def unit_type(self):
        """
        Gets the unit_type of this AbstractField.
        Field denoting field unit type.


        :return: The unit_type of this AbstractField.
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """
        Sets the unit_type of this AbstractField.
        Field denoting field unit type.


        :param unit_type: The unit_type of this AbstractField.
        :type: str
        """
        self._unit_type = unit_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
