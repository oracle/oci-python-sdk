# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ColumnFilter(object):
    """
    Filters that are applied to the data at the column level.
    """

    #: A constant which can be used with the operator property of a ColumnFilter.
    #: This constant has a value of "IN"
    OPERATOR_IN = "IN"

    #: A constant which can be used with the operator property of a ColumnFilter.
    #: This constant has a value of "EQ"
    OPERATOR_EQ = "EQ"

    #: A constant which can be used with the operator property of a ColumnFilter.
    #: This constant has a value of "GT"
    OPERATOR_GT = "GT"

    #: A constant which can be used with the operator property of a ColumnFilter.
    #: This constant has a value of "GE"
    OPERATOR_GE = "GE"

    #: A constant which can be used with the operator property of a ColumnFilter.
    #: This constant has a value of "LT"
    OPERATOR_LT = "LT"

    #: A constant which can be used with the operator property of a ColumnFilter.
    #: This constant has a value of "LE"
    OPERATOR_LE = "LE"

    #: A constant which can be used with the operator property of a ColumnFilter.
    #: This constant has a value of "AND"
    OPERATOR_AND = "AND"

    #: A constant which can be used with the operator property of a ColumnFilter.
    #: This constant has a value of "OR"
    OPERATOR_OR = "OR"

    #: A constant which can be used with the operator property of a ColumnFilter.
    #: This constant has a value of "NE"
    OPERATOR_NE = "NE"

    #: A constant which can be used with the operator property of a ColumnFilter.
    #: This constant has a value of "CO"
    OPERATOR_CO = "CO"

    #: A constant which can be used with the operator property of a ColumnFilter.
    #: This constant has a value of "NOT"
    OPERATOR_NOT = "NOT"

    #: A constant which can be used with the operator property of a ColumnFilter.
    #: This constant has a value of "NOT_IN"
    OPERATOR_NOT_IN = "NOT_IN"

    def __init__(self, **kwargs):
        """
        Initializes a new ColumnFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field_name:
            The value to assign to the field_name property of this ColumnFilter.
        :type field_name: str

        :param operator:
            The value to assign to the operator property of this ColumnFilter.
            Allowed values for this property are: "IN", "EQ", "GT", "GE", "LT", "LE", "AND", "OR", "NE", "CO", "NOT", "NOT_IN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operator: str

        :param expressions:
            The value to assign to the expressions property of this ColumnFilter.
        :type expressions: list[str]

        :param is_enabled:
            The value to assign to the is_enabled property of this ColumnFilter.
        :type is_enabled: bool

        :param is_hidden:
            The value to assign to the is_hidden property of this ColumnFilter.
        :type is_hidden: bool

        """
        self.swagger_types = {
            'field_name': 'str',
            'operator': 'str',
            'expressions': 'list[str]',
            'is_enabled': 'bool',
            'is_hidden': 'bool'
        }

        self.attribute_map = {
            'field_name': 'fieldName',
            'operator': 'operator',
            'expressions': 'expressions',
            'is_enabled': 'isEnabled',
            'is_hidden': 'isHidden'
        }

        self._field_name = None
        self._operator = None
        self._expressions = None
        self._is_enabled = None
        self._is_hidden = None

    @property
    def field_name(self):
        """
        **[Required]** Gets the field_name of this ColumnFilter.
        Name of the column on which the filter must be applied.


        :return: The field_name of this ColumnFilter.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this ColumnFilter.
        Name of the column on which the filter must be applied.


        :param field_name: The field_name of this ColumnFilter.
        :type: str
        """
        self._field_name = field_name

    @property
    def operator(self):
        """
        **[Required]** Gets the operator of this ColumnFilter.
        Specifies the type of operator that must be applied for example in, eq etc.

        Allowed values for this property are: "IN", "EQ", "GT", "GE", "LT", "LE", "AND", "OR", "NE", "CO", "NOT", "NOT_IN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operator of this ColumnFilter.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this ColumnFilter.
        Specifies the type of operator that must be applied for example in, eq etc.


        :param operator: The operator of this ColumnFilter.
        :type: str
        """
        allowed_values = ["IN", "EQ", "GT", "GE", "LT", "LE", "AND", "OR", "NE", "CO", "NOT", "NOT_IN"]
        if not value_allowed_none_or_none_sentinel(operator, allowed_values):
            operator = 'UNKNOWN_ENUM_VALUE'
        self._operator = operator

    @property
    def expressions(self):
        """
        **[Required]** Gets the expressions of this ColumnFilter.
        An array of expressions based on the operator type. A filter may have one or more expressions.


        :return: The expressions of this ColumnFilter.
        :rtype: list[str]
        """
        return self._expressions

    @expressions.setter
    def expressions(self, expressions):
        """
        Sets the expressions of this ColumnFilter.
        An array of expressions based on the operator type. A filter may have one or more expressions.


        :param expressions: The expressions of this ColumnFilter.
        :type: list[str]
        """
        self._expressions = expressions

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this ColumnFilter.
        Indicates if the filter is enabled. Values can either be 'true' or 'false'.


        :return: The is_enabled of this ColumnFilter.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this ColumnFilter.
        Indicates if the filter is enabled. Values can either be 'true' or 'false'.


        :param is_enabled: The is_enabled of this ColumnFilter.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def is_hidden(self):
        """
        **[Required]** Gets the is_hidden of this ColumnFilter.
        Indicates if the filter is hidden. Values can either be 'true' or 'false'.


        :return: The is_hidden of this ColumnFilter.
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """
        Sets the is_hidden of this ColumnFilter.
        Indicates if the filter is hidden. Values can either be 'true' or 'false'.


        :param is_hidden: The is_hidden of this ColumnFilter.
        :type: bool
        """
        self._is_hidden = is_hidden

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
