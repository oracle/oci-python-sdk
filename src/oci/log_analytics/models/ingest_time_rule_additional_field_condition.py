# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngestTimeRuleAdditionalFieldCondition(object):
    """
    The additional field condition(s) to evaluate for an ingest time rule.
    """

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "CONTAINS"
    CONDITION_OPERATOR_CONTAINS = "CONTAINS"

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "CONTAINS_IGNORE_CASE"
    CONDITION_OPERATOR_CONTAINS_IGNORE_CASE = "CONTAINS_IGNORE_CASE"

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "CONTAINS_REGEX"
    CONDITION_OPERATOR_CONTAINS_REGEX = "CONTAINS_REGEX"

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "CONTAINS_ONEOF_REGEXES"
    CONDITION_OPERATOR_CONTAINS_ONEOF_REGEXES = "CONTAINS_ONEOF_REGEXES"

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "ENDS_WITH"
    CONDITION_OPERATOR_ENDS_WITH = "ENDS_WITH"

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "EQUAL"
    CONDITION_OPERATOR_EQUAL = "EQUAL"

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "EQUAL_IGNORE_CASE"
    CONDITION_OPERATOR_EQUAL_IGNORE_CASE = "EQUAL_IGNORE_CASE"

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "IN"
    CONDITION_OPERATOR_IN = "IN"

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "IN_IGNORE_CASE"
    CONDITION_OPERATOR_IN_IGNORE_CASE = "IN_IGNORE_CASE"

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "NOT_CONTAINS"
    CONDITION_OPERATOR_NOT_CONTAINS = "NOT_CONTAINS"

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "NOT_EQUAL"
    CONDITION_OPERATOR_NOT_EQUAL = "NOT_EQUAL"

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "NOT_IN"
    CONDITION_OPERATOR_NOT_IN = "NOT_IN"

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "NOT_NULL"
    CONDITION_OPERATOR_NOT_NULL = "NOT_NULL"

    #: A constant which can be used with the condition_operator property of a IngestTimeRuleAdditionalFieldCondition.
    #: This constant has a value of "STARTS_WITH"
    CONDITION_OPERATOR_STARTS_WITH = "STARTS_WITH"

    def __init__(self, **kwargs):
        """
        Initializes a new IngestTimeRuleAdditionalFieldCondition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param condition_field:
            The value to assign to the condition_field property of this IngestTimeRuleAdditionalFieldCondition.
        :type condition_field: str

        :param condition_operator:
            The value to assign to the condition_operator property of this IngestTimeRuleAdditionalFieldCondition.
            Allowed values for this property are: "CONTAINS", "CONTAINS_IGNORE_CASE", "CONTAINS_REGEX", "CONTAINS_ONEOF_REGEXES", "ENDS_WITH", "EQUAL", "EQUAL_IGNORE_CASE", "IN", "IN_IGNORE_CASE", "NOT_CONTAINS", "NOT_EQUAL", "NOT_IN", "NOT_NULL", "STARTS_WITH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type condition_operator: str

        :param condition_value:
            The value to assign to the condition_value property of this IngestTimeRuleAdditionalFieldCondition.
        :type condition_value: str

        """
        self.swagger_types = {
            'condition_field': 'str',
            'condition_operator': 'str',
            'condition_value': 'str'
        }

        self.attribute_map = {
            'condition_field': 'conditionField',
            'condition_operator': 'conditionOperator',
            'condition_value': 'conditionValue'
        }

        self._condition_field = None
        self._condition_operator = None
        self._condition_value = None

    @property
    def condition_field(self):
        """
        **[Required]** Gets the condition_field of this IngestTimeRuleAdditionalFieldCondition.
        The additional field name to be evaluated.


        :return: The condition_field of this IngestTimeRuleAdditionalFieldCondition.
        :rtype: str
        """
        return self._condition_field

    @condition_field.setter
    def condition_field(self, condition_field):
        """
        Sets the condition_field of this IngestTimeRuleAdditionalFieldCondition.
        The additional field name to be evaluated.


        :param condition_field: The condition_field of this IngestTimeRuleAdditionalFieldCondition.
        :type: str
        """
        self._condition_field = condition_field

    @property
    def condition_operator(self):
        """
        **[Required]** Gets the condition_operator of this IngestTimeRuleAdditionalFieldCondition.
        The operator to be used for evaluating the additional field.

        Allowed values for this property are: "CONTAINS", "CONTAINS_IGNORE_CASE", "CONTAINS_REGEX", "CONTAINS_ONEOF_REGEXES", "ENDS_WITH", "EQUAL", "EQUAL_IGNORE_CASE", "IN", "IN_IGNORE_CASE", "NOT_CONTAINS", "NOT_EQUAL", "NOT_IN", "NOT_NULL", "STARTS_WITH", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The condition_operator of this IngestTimeRuleAdditionalFieldCondition.
        :rtype: str
        """
        return self._condition_operator

    @condition_operator.setter
    def condition_operator(self, condition_operator):
        """
        Sets the condition_operator of this IngestTimeRuleAdditionalFieldCondition.
        The operator to be used for evaluating the additional field.


        :param condition_operator: The condition_operator of this IngestTimeRuleAdditionalFieldCondition.
        :type: str
        """
        allowed_values = ["CONTAINS", "CONTAINS_IGNORE_CASE", "CONTAINS_REGEX", "CONTAINS_ONEOF_REGEXES", "ENDS_WITH", "EQUAL", "EQUAL_IGNORE_CASE", "IN", "IN_IGNORE_CASE", "NOT_CONTAINS", "NOT_EQUAL", "NOT_IN", "NOT_NULL", "STARTS_WITH"]
        if not value_allowed_none_or_none_sentinel(condition_operator, allowed_values):
            condition_operator = 'UNKNOWN_ENUM_VALUE'
        self._condition_operator = condition_operator

    @property
    def condition_value(self):
        """
        **[Required]** Gets the condition_value of this IngestTimeRuleAdditionalFieldCondition.
        The additional field value to be evaluated.


        :return: The condition_value of this IngestTimeRuleAdditionalFieldCondition.
        :rtype: str
        """
        return self._condition_value

    @condition_value.setter
    def condition_value(self, condition_value):
        """
        Sets the condition_value of this IngestTimeRuleAdditionalFieldCondition.
        The additional field value to be evaluated.


        :param condition_value: The condition_value of this IngestTimeRuleAdditionalFieldCondition.
        :type: str
        """
        self._condition_value = condition_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
