# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Filter(object):
    """
    Query builder filter action to apply edit to queryString.
    """

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "CLEAR"
    OPERATOR_CLEAR = "CLEAR"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "REPLACE"
    OPERATOR_REPLACE = "REPLACE"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "EQUALS"
    OPERATOR_EQUALS = "EQUALS"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "NOT_EQUALS"
    OPERATOR_NOT_EQUALS = "NOT_EQUALS"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "STARTS_WITH"
    OPERATOR_STARTS_WITH = "STARTS_WITH"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "DOES_NOT_START_WITH"
    OPERATOR_DOES_NOT_START_WITH = "DOES_NOT_START_WITH"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "ENDS_WITH"
    OPERATOR_ENDS_WITH = "ENDS_WITH"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "DOES_NOT_END_WITH"
    OPERATOR_DOES_NOT_END_WITH = "DOES_NOT_END_WITH"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "CONTAINS"
    OPERATOR_CONTAINS = "CONTAINS"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "DOES_NOT_CONTAIN"
    OPERATOR_DOES_NOT_CONTAIN = "DOES_NOT_CONTAIN"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "IS_LESS_THAN"
    OPERATOR_IS_LESS_THAN = "IS_LESS_THAN"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "IS_LESS_THAN_OR_EQUAL_TO"
    OPERATOR_IS_LESS_THAN_OR_EQUAL_TO = "IS_LESS_THAN_OR_EQUAL_TO"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "IS_GREATER_THAN"
    OPERATOR_IS_GREATER_THAN = "IS_GREATER_THAN"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "IS_GREATER_THAN_OR_EQUAL_TO"
    OPERATOR_IS_GREATER_THAN_OR_EQUAL_TO = "IS_GREATER_THAN_OR_EQUAL_TO"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "IS_BETWEEN"
    OPERATOR_IS_BETWEEN = "IS_BETWEEN"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "IS_NOT_BETWEEN"
    OPERATOR_IS_NOT_BETWEEN = "IS_NOT_BETWEEN"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "ADD_SUBQUERY"
    OPERATOR_ADD_SUBQUERY = "ADD_SUBQUERY"

    #: A constant which can be used with the operator property of a Filter.
    #: This constant has a value of "CLEAR_SUBQUERY"
    OPERATOR_CLEAR_SUBQUERY = "CLEAR_SUBQUERY"

    def __init__(self, **kwargs):
        """
        Initializes a new Filter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field_name:
            The value to assign to the field_name property of this Filter.
        :type field_name: str

        :param values:
            The value to assign to the values property of this Filter.
        :type values: list[object]

        :param operator:
            The value to assign to the operator property of this Filter.
            Allowed values for this property are: "CLEAR", "REPLACE", "EQUALS", "NOT_EQUALS", "STARTS_WITH", "DOES_NOT_START_WITH", "ENDS_WITH", "DOES_NOT_END_WITH", "CONTAINS", "DOES_NOT_CONTAIN", "IS_LESS_THAN", "IS_LESS_THAN_OR_EQUAL_TO", "IS_GREATER_THAN", "IS_GREATER_THAN_OR_EQUAL_TO", "IS_BETWEEN", "IS_NOT_BETWEEN", "ADD_SUBQUERY", "CLEAR_SUBQUERY"
        :type operator: str

        """
        self.swagger_types = {
            'field_name': 'str',
            'values': 'list[object]',
            'operator': 'str'
        }

        self.attribute_map = {
            'field_name': 'fieldName',
            'values': 'values',
            'operator': 'operator'
        }

        self._field_name = None
        self._values = None
        self._operator = None

    @property
    def field_name(self):
        """
        Gets the field_name of this Filter.
        Field filter references when inserting filter into the query string. Field must be a valid logging analytics out-of-the-box field, virtual field calculated in the query or a user defined field.


        :return: The field_name of this Filter.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this Filter.
        Field filter references when inserting filter into the query string. Field must be a valid logging analytics out-of-the-box field, virtual field calculated in the query or a user defined field.


        :param field_name: The field_name of this Filter.
        :type: str
        """
        self._field_name = field_name

    @property
    def values(self):
        """
        Gets the values of this Filter.
        Field values that will be inserted into the query string for the specified fieldName. Please note all values should reflect the fields data type otherwise the insert is subject to fail.


        :return: The values of this Filter.
        :rtype: list[object]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this Filter.
        Field values that will be inserted into the query string for the specified fieldName. Please note all values should reflect the fields data type otherwise the insert is subject to fail.


        :param values: The values of this Filter.
        :type: list[object]
        """
        self._values = values

    @property
    def operator(self):
        """
        **[Required]** Gets the operator of this Filter.
        Operator to apply when editing the query string.

        Allowed values for this property are: "CLEAR", "REPLACE", "EQUALS", "NOT_EQUALS", "STARTS_WITH", "DOES_NOT_START_WITH", "ENDS_WITH", "DOES_NOT_END_WITH", "CONTAINS", "DOES_NOT_CONTAIN", "IS_LESS_THAN", "IS_LESS_THAN_OR_EQUAL_TO", "IS_GREATER_THAN", "IS_GREATER_THAN_OR_EQUAL_TO", "IS_BETWEEN", "IS_NOT_BETWEEN", "ADD_SUBQUERY", "CLEAR_SUBQUERY"


        :return: The operator of this Filter.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this Filter.
        Operator to apply when editing the query string.


        :param operator: The operator of this Filter.
        :type: str
        """
        allowed_values = ["CLEAR", "REPLACE", "EQUALS", "NOT_EQUALS", "STARTS_WITH", "DOES_NOT_START_WITH", "ENDS_WITH", "DOES_NOT_END_WITH", "CONTAINS", "DOES_NOT_CONTAIN", "IS_LESS_THAN", "IS_LESS_THAN_OR_EQUAL_TO", "IS_GREATER_THAN", "IS_GREATER_THAN_OR_EQUAL_TO", "IS_BETWEEN", "IS_NOT_BETWEEN", "ADD_SUBQUERY", "CLEAR_SUBQUERY"]
        if not value_allowed_none_or_none_sentinel(operator, allowed_values):
            raise ValueError(
                "Invalid value for `operator`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._operator = operator

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
