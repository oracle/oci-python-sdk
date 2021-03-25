# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsSourceExtendedFieldDefinition(object):
    """
    LogAnalyticsSourceExtendedFieldDefinition
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsSourceExtendedFieldDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field:
            The value to assign to the field property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type field: oci.log_analytics.models.LogAnalyticsField

        :param display_regular_expression:
            The value to assign to the display_regular_expression property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type display_regular_expression: str

        :param extended_fields:
            The value to assign to the extended_fields property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type extended_fields: list[oci.log_analytics.models.LogAnalyticsExtendedField]

        :param base_field_name:
            The value to assign to the base_field_name property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type base_field_name: str

        :param base_field_log_text:
            The value to assign to the base_field_log_text property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type base_field_log_text: str

        :param condition_data_type:
            The value to assign to the condition_data_type property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type condition_data_type: str

        :param condition_field:
            The value to assign to the condition_field property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type condition_field: str

        :param condition_operator:
            The value to assign to the condition_operator property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type condition_operator: str

        :param condition_value:
            The value to assign to the condition_value property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type condition_value: str

        :param converted_regular_expression:
            The value to assign to the converted_regular_expression property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type converted_regular_expression: str

        :param is_enabled:
            The value to assign to the is_enabled property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type is_enabled: bool

        :param extended_field_definition_id:
            The value to assign to the extended_field_definition_id property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type extended_field_definition_id: int

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type is_system: bool

        :param regular_expression:
            The value to assign to the regular_expression property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type regular_expression: str

        :param source_id:
            The value to assign to the source_id property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type source_id: int

        :param time_updated:
            The value to assign to the time_updated property of this LogAnalyticsSourceExtendedFieldDefinition.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'field': 'LogAnalyticsField',
            'display_regular_expression': 'str',
            'extended_fields': 'list[LogAnalyticsExtendedField]',
            'base_field_name': 'str',
            'base_field_log_text': 'str',
            'condition_data_type': 'str',
            'condition_field': 'str',
            'condition_operator': 'str',
            'condition_value': 'str',
            'converted_regular_expression': 'str',
            'is_enabled': 'bool',
            'extended_field_definition_id': 'int',
            'is_system': 'bool',
            'regular_expression': 'str',
            'source_id': 'int',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'field': 'field',
            'display_regular_expression': 'displayRegularExpression',
            'extended_fields': 'extendedFields',
            'base_field_name': 'baseFieldName',
            'base_field_log_text': 'baseFieldLogText',
            'condition_data_type': 'conditionDataType',
            'condition_field': 'conditionField',
            'condition_operator': 'conditionOperator',
            'condition_value': 'conditionValue',
            'converted_regular_expression': 'convertedRegularExpression',
            'is_enabled': 'isEnabled',
            'extended_field_definition_id': 'extendedFieldDefinitionId',
            'is_system': 'isSystem',
            'regular_expression': 'regularExpression',
            'source_id': 'sourceId',
            'time_updated': 'timeUpdated'
        }

        self._field = None
        self._display_regular_expression = None
        self._extended_fields = None
        self._base_field_name = None
        self._base_field_log_text = None
        self._condition_data_type = None
        self._condition_field = None
        self._condition_operator = None
        self._condition_value = None
        self._converted_regular_expression = None
        self._is_enabled = None
        self._extended_field_definition_id = None
        self._is_system = None
        self._regular_expression = None
        self._source_id = None
        self._time_updated = None

    @property
    def field(self):
        """
        Gets the field of this LogAnalyticsSourceExtendedFieldDefinition.

        :return: The field of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: oci.log_analytics.models.LogAnalyticsField
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this LogAnalyticsSourceExtendedFieldDefinition.

        :param field: The field of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: oci.log_analytics.models.LogAnalyticsField
        """
        self._field = field

    @property
    def display_regular_expression(self):
        """
        Gets the display_regular_expression of this LogAnalyticsSourceExtendedFieldDefinition.
        The regular expression.


        :return: The display_regular_expression of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: str
        """
        return self._display_regular_expression

    @display_regular_expression.setter
    def display_regular_expression(self, display_regular_expression):
        """
        Sets the display_regular_expression of this LogAnalyticsSourceExtendedFieldDefinition.
        The regular expression.


        :param display_regular_expression: The display_regular_expression of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: str
        """
        self._display_regular_expression = display_regular_expression

    @property
    def extended_fields(self):
        """
        Gets the extended_fields of this LogAnalyticsSourceExtendedFieldDefinition.
        An array of extended fields.


        :return: The extended_fields of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: list[oci.log_analytics.models.LogAnalyticsExtendedField]
        """
        return self._extended_fields

    @extended_fields.setter
    def extended_fields(self, extended_fields):
        """
        Sets the extended_fields of this LogAnalyticsSourceExtendedFieldDefinition.
        An array of extended fields.


        :param extended_fields: The extended_fields of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: list[oci.log_analytics.models.LogAnalyticsExtendedField]
        """
        self._extended_fields = extended_fields

    @property
    def base_field_name(self):
        """
        Gets the base_field_name of this LogAnalyticsSourceExtendedFieldDefinition.
        The base field internal name.


        :return: The base_field_name of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: str
        """
        return self._base_field_name

    @base_field_name.setter
    def base_field_name(self, base_field_name):
        """
        Sets the base_field_name of this LogAnalyticsSourceExtendedFieldDefinition.
        The base field internal name.


        :param base_field_name: The base_field_name of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: str
        """
        self._base_field_name = base_field_name

    @property
    def base_field_log_text(self):
        """
        Gets the base_field_log_text of this LogAnalyticsSourceExtendedFieldDefinition.
        The base field log text.


        :return: The base_field_log_text of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: str
        """
        return self._base_field_log_text

    @base_field_log_text.setter
    def base_field_log_text(self, base_field_log_text):
        """
        Sets the base_field_log_text of this LogAnalyticsSourceExtendedFieldDefinition.
        The base field log text.


        :param base_field_log_text: The base_field_log_text of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: str
        """
        self._base_field_log_text = base_field_log_text

    @property
    def condition_data_type(self):
        """
        Gets the condition_data_type of this LogAnalyticsSourceExtendedFieldDefinition.
        The conditional data type.


        :return: The condition_data_type of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: str
        """
        return self._condition_data_type

    @condition_data_type.setter
    def condition_data_type(self, condition_data_type):
        """
        Sets the condition_data_type of this LogAnalyticsSourceExtendedFieldDefinition.
        The conditional data type.


        :param condition_data_type: The condition_data_type of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: str
        """
        self._condition_data_type = condition_data_type

    @property
    def condition_field(self):
        """
        Gets the condition_field of this LogAnalyticsSourceExtendedFieldDefinition.
        The onditional field.


        :return: The condition_field of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: str
        """
        return self._condition_field

    @condition_field.setter
    def condition_field(self, condition_field):
        """
        Sets the condition_field of this LogAnalyticsSourceExtendedFieldDefinition.
        The onditional field.


        :param condition_field: The condition_field of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: str
        """
        self._condition_field = condition_field

    @property
    def condition_operator(self):
        """
        Gets the condition_operator of this LogAnalyticsSourceExtendedFieldDefinition.
        The conditional operator.


        :return: The condition_operator of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: str
        """
        return self._condition_operator

    @condition_operator.setter
    def condition_operator(self, condition_operator):
        """
        Sets the condition_operator of this LogAnalyticsSourceExtendedFieldDefinition.
        The conditional operator.


        :param condition_operator: The condition_operator of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: str
        """
        self._condition_operator = condition_operator

    @property
    def condition_value(self):
        """
        Gets the condition_value of this LogAnalyticsSourceExtendedFieldDefinition.
        The conditional value.


        :return: The condition_value of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: str
        """
        return self._condition_value

    @condition_value.setter
    def condition_value(self, condition_value):
        """
        Sets the condition_value of this LogAnalyticsSourceExtendedFieldDefinition.
        The conditional value.


        :param condition_value: The condition_value of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: str
        """
        self._condition_value = condition_value

    @property
    def converted_regular_expression(self):
        """
        Gets the converted_regular_expression of this LogAnalyticsSourceExtendedFieldDefinition.
        The converted regular expression.


        :return: The converted_regular_expression of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: str
        """
        return self._converted_regular_expression

    @converted_regular_expression.setter
    def converted_regular_expression(self, converted_regular_expression):
        """
        Sets the converted_regular_expression of this LogAnalyticsSourceExtendedFieldDefinition.
        The converted regular expression.


        :param converted_regular_expression: The converted_regular_expression of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: str
        """
        self._converted_regular_expression = converted_regular_expression

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this LogAnalyticsSourceExtendedFieldDefinition.
        A flag inidcating whether or not the extended definition is enabled.


        :return: The is_enabled of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this LogAnalyticsSourceExtendedFieldDefinition.
        A flag inidcating whether or not the extended definition is enabled.


        :param is_enabled: The is_enabled of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def extended_field_definition_id(self):
        """
        Gets the extended_field_definition_id of this LogAnalyticsSourceExtendedFieldDefinition.
        The extended field definition unique identifier.


        :return: The extended_field_definition_id of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: int
        """
        return self._extended_field_definition_id

    @extended_field_definition_id.setter
    def extended_field_definition_id(self, extended_field_definition_id):
        """
        Sets the extended_field_definition_id of this LogAnalyticsSourceExtendedFieldDefinition.
        The extended field definition unique identifier.


        :param extended_field_definition_id: The extended_field_definition_id of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: int
        """
        self._extended_field_definition_id = extended_field_definition_id

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsSourceExtendedFieldDefinition.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :return: The is_system of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsSourceExtendedFieldDefinition.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :param is_system: The is_system of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: bool
        """
        self._is_system = is_system

    @property
    def regular_expression(self):
        """
        Gets the regular_expression of this LogAnalyticsSourceExtendedFieldDefinition.
        The regular expression.


        :return: The regular_expression of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: str
        """
        return self._regular_expression

    @regular_expression.setter
    def regular_expression(self, regular_expression):
        """
        Sets the regular_expression of this LogAnalyticsSourceExtendedFieldDefinition.
        The regular expression.


        :param regular_expression: The regular_expression of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: str
        """
        self._regular_expression = regular_expression

    @property
    def source_id(self):
        """
        Gets the source_id of this LogAnalyticsSourceExtendedFieldDefinition.
        The source unique identifier.


        :return: The source_id of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LogAnalyticsSourceExtendedFieldDefinition.
        The source unique identifier.


        :param source_id: The source_id of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: int
        """
        self._source_id = source_id

    @property
    def time_updated(self):
        """
        Gets the time_updated of this LogAnalyticsSourceExtendedFieldDefinition.
        The last updated date.


        :return: The time_updated of this LogAnalyticsSourceExtendedFieldDefinition.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this LogAnalyticsSourceExtendedFieldDefinition.
        The last updated date.


        :param time_updated: The time_updated of this LogAnalyticsSourceExtendedFieldDefinition.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
