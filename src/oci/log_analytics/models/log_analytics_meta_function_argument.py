# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsMetaFunctionArgument(object):
    """
    LogAnalyticsMetaFunctionArgument
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsMetaFunctionArgument object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_override_output_fields:
            The value to assign to the is_override_output_fields property of this LogAnalyticsMetaFunctionArgument.
        :type is_override_output_fields: bool

        :param argument_display_name:
            The value to assign to the argument_display_name property of this LogAnalyticsMetaFunctionArgument.
        :type argument_display_name: str

        :param argument_example:
            The value to assign to the argument_example property of this LogAnalyticsMetaFunctionArgument.
        :type argument_example: str

        :param argument_service:
            The value to assign to the argument_service property of this LogAnalyticsMetaFunctionArgument.
        :type argument_service: str

        :param argument_data_type:
            The value to assign to the argument_data_type property of this LogAnalyticsMetaFunctionArgument.
        :type argument_data_type: str

        :param argument_description:
            The value to assign to the argument_description property of this LogAnalyticsMetaFunctionArgument.
        :type argument_description: str

        :param argument_name:
            The value to assign to the argument_name property of this LogAnalyticsMetaFunctionArgument.
        :type argument_name: str

        :param argument_order:
            The value to assign to the argument_order property of this LogAnalyticsMetaFunctionArgument.
        :type argument_order: int

        :param argument_type:
            The value to assign to the argument_type property of this LogAnalyticsMetaFunctionArgument.
        :type argument_type: int

        :param argument_id:
            The value to assign to the argument_id property of this LogAnalyticsMetaFunctionArgument.
        :type argument_id: int

        :param argument_lookup_column:
            The value to assign to the argument_lookup_column property of this LogAnalyticsMetaFunctionArgument.
        :type argument_lookup_column: str

        :param argument_lookup_column_position:
            The value to assign to the argument_lookup_column_position property of this LogAnalyticsMetaFunctionArgument.
        :type argument_lookup_column_position: int

        :param argument_value:
            The value to assign to the argument_value property of this LogAnalyticsMetaFunctionArgument.
        :type argument_value: str

        :param argument_reference:
            The value to assign to the argument_reference property of this LogAnalyticsMetaFunctionArgument.
        :type argument_reference: str

        """
        self.swagger_types = {
            'is_override_output_fields': 'bool',
            'argument_display_name': 'str',
            'argument_example': 'str',
            'argument_service': 'str',
            'argument_data_type': 'str',
            'argument_description': 'str',
            'argument_name': 'str',
            'argument_order': 'int',
            'argument_type': 'int',
            'argument_id': 'int',
            'argument_lookup_column': 'str',
            'argument_lookup_column_position': 'int',
            'argument_value': 'str',
            'argument_reference': 'str'
        }

        self.attribute_map = {
            'is_override_output_fields': 'isOverrideOutputFields',
            'argument_display_name': 'argumentDisplayName',
            'argument_example': 'argumentExample',
            'argument_service': 'argumentService',
            'argument_data_type': 'argumentDataType',
            'argument_description': 'argumentDescription',
            'argument_name': 'argumentName',
            'argument_order': 'argumentOrder',
            'argument_type': 'argumentType',
            'argument_id': 'argumentId',
            'argument_lookup_column': 'argumentLookupColumn',
            'argument_lookup_column_position': 'argumentLookupColumnPosition',
            'argument_value': 'argumentValue',
            'argument_reference': 'argumentReference'
        }

        self._is_override_output_fields = None
        self._argument_display_name = None
        self._argument_example = None
        self._argument_service = None
        self._argument_data_type = None
        self._argument_description = None
        self._argument_name = None
        self._argument_order = None
        self._argument_type = None
        self._argument_id = None
        self._argument_lookup_column = None
        self._argument_lookup_column_position = None
        self._argument_value = None
        self._argument_reference = None

    @property
    def is_override_output_fields(self):
        """
        Gets the is_override_output_fields of this LogAnalyticsMetaFunctionArgument.
        The override output fields.


        :return: The is_override_output_fields of this LogAnalyticsMetaFunctionArgument.
        :rtype: bool
        """
        return self._is_override_output_fields

    @is_override_output_fields.setter
    def is_override_output_fields(self, is_override_output_fields):
        """
        Sets the is_override_output_fields of this LogAnalyticsMetaFunctionArgument.
        The override output fields.


        :param is_override_output_fields: The is_override_output_fields of this LogAnalyticsMetaFunctionArgument.
        :type: bool
        """
        self._is_override_output_fields = is_override_output_fields

    @property
    def argument_display_name(self):
        """
        Gets the argument_display_name of this LogAnalyticsMetaFunctionArgument.
        The argument display name.


        :return: The argument_display_name of this LogAnalyticsMetaFunctionArgument.
        :rtype: str
        """
        return self._argument_display_name

    @argument_display_name.setter
    def argument_display_name(self, argument_display_name):
        """
        Sets the argument_display_name of this LogAnalyticsMetaFunctionArgument.
        The argument display name.


        :param argument_display_name: The argument_display_name of this LogAnalyticsMetaFunctionArgument.
        :type: str
        """
        self._argument_display_name = argument_display_name

    @property
    def argument_example(self):
        """
        Gets the argument_example of this LogAnalyticsMetaFunctionArgument.
        The argument example.


        :return: The argument_example of this LogAnalyticsMetaFunctionArgument.
        :rtype: str
        """
        return self._argument_example

    @argument_example.setter
    def argument_example(self, argument_example):
        """
        Sets the argument_example of this LogAnalyticsMetaFunctionArgument.
        The argument example.


        :param argument_example: The argument_example of this LogAnalyticsMetaFunctionArgument.
        :type: str
        """
        self._argument_example = argument_example

    @property
    def argument_service(self):
        """
        Gets the argument_service of this LogAnalyticsMetaFunctionArgument.
        The argument service.


        :return: The argument_service of this LogAnalyticsMetaFunctionArgument.
        :rtype: str
        """
        return self._argument_service

    @argument_service.setter
    def argument_service(self, argument_service):
        """
        Sets the argument_service of this LogAnalyticsMetaFunctionArgument.
        The argument service.


        :param argument_service: The argument_service of this LogAnalyticsMetaFunctionArgument.
        :type: str
        """
        self._argument_service = argument_service

    @property
    def argument_data_type(self):
        """
        Gets the argument_data_type of this LogAnalyticsMetaFunctionArgument.
        The argument data type.


        :return: The argument_data_type of this LogAnalyticsMetaFunctionArgument.
        :rtype: str
        """
        return self._argument_data_type

    @argument_data_type.setter
    def argument_data_type(self, argument_data_type):
        """
        Sets the argument_data_type of this LogAnalyticsMetaFunctionArgument.
        The argument data type.


        :param argument_data_type: The argument_data_type of this LogAnalyticsMetaFunctionArgument.
        :type: str
        """
        self._argument_data_type = argument_data_type

    @property
    def argument_description(self):
        """
        Gets the argument_description of this LogAnalyticsMetaFunctionArgument.
        The argument description.


        :return: The argument_description of this LogAnalyticsMetaFunctionArgument.
        :rtype: str
        """
        return self._argument_description

    @argument_description.setter
    def argument_description(self, argument_description):
        """
        Sets the argument_description of this LogAnalyticsMetaFunctionArgument.
        The argument description.


        :param argument_description: The argument_description of this LogAnalyticsMetaFunctionArgument.
        :type: str
        """
        self._argument_description = argument_description

    @property
    def argument_name(self):
        """
        Gets the argument_name of this LogAnalyticsMetaFunctionArgument.
        The argument name.


        :return: The argument_name of this LogAnalyticsMetaFunctionArgument.
        :rtype: str
        """
        return self._argument_name

    @argument_name.setter
    def argument_name(self, argument_name):
        """
        Sets the argument_name of this LogAnalyticsMetaFunctionArgument.
        The argument name.


        :param argument_name: The argument_name of this LogAnalyticsMetaFunctionArgument.
        :type: str
        """
        self._argument_name = argument_name

    @property
    def argument_order(self):
        """
        Gets the argument_order of this LogAnalyticsMetaFunctionArgument.
        The argument order.


        :return: The argument_order of this LogAnalyticsMetaFunctionArgument.
        :rtype: int
        """
        return self._argument_order

    @argument_order.setter
    def argument_order(self, argument_order):
        """
        Sets the argument_order of this LogAnalyticsMetaFunctionArgument.
        The argument order.


        :param argument_order: The argument_order of this LogAnalyticsMetaFunctionArgument.
        :type: int
        """
        self._argument_order = argument_order

    @property
    def argument_type(self):
        """
        Gets the argument_type of this LogAnalyticsMetaFunctionArgument.
        The argument type.


        :return: The argument_type of this LogAnalyticsMetaFunctionArgument.
        :rtype: int
        """
        return self._argument_type

    @argument_type.setter
    def argument_type(self, argument_type):
        """
        Sets the argument_type of this LogAnalyticsMetaFunctionArgument.
        The argument type.


        :param argument_type: The argument_type of this LogAnalyticsMetaFunctionArgument.
        :type: int
        """
        self._argument_type = argument_type

    @property
    def argument_id(self):
        """
        Gets the argument_id of this LogAnalyticsMetaFunctionArgument.
        The argument unique identifier.


        :return: The argument_id of this LogAnalyticsMetaFunctionArgument.
        :rtype: int
        """
        return self._argument_id

    @argument_id.setter
    def argument_id(self, argument_id):
        """
        Sets the argument_id of this LogAnalyticsMetaFunctionArgument.
        The argument unique identifier.


        :param argument_id: The argument_id of this LogAnalyticsMetaFunctionArgument.
        :type: int
        """
        self._argument_id = argument_id

    @property
    def argument_lookup_column(self):
        """
        Gets the argument_lookup_column of this LogAnalyticsMetaFunctionArgument.
        The lookup column.


        :return: The argument_lookup_column of this LogAnalyticsMetaFunctionArgument.
        :rtype: str
        """
        return self._argument_lookup_column

    @argument_lookup_column.setter
    def argument_lookup_column(self, argument_lookup_column):
        """
        Sets the argument_lookup_column of this LogAnalyticsMetaFunctionArgument.
        The lookup column.


        :param argument_lookup_column: The argument_lookup_column of this LogAnalyticsMetaFunctionArgument.
        :type: str
        """
        self._argument_lookup_column = argument_lookup_column

    @property
    def argument_lookup_column_position(self):
        """
        Gets the argument_lookup_column_position of this LogAnalyticsMetaFunctionArgument.
        The lookup column position.


        :return: The argument_lookup_column_position of this LogAnalyticsMetaFunctionArgument.
        :rtype: int
        """
        return self._argument_lookup_column_position

    @argument_lookup_column_position.setter
    def argument_lookup_column_position(self, argument_lookup_column_position):
        """
        Sets the argument_lookup_column_position of this LogAnalyticsMetaFunctionArgument.
        The lookup column position.


        :param argument_lookup_column_position: The argument_lookup_column_position of this LogAnalyticsMetaFunctionArgument.
        :type: int
        """
        self._argument_lookup_column_position = argument_lookup_column_position

    @property
    def argument_value(self):
        """
        Gets the argument_value of this LogAnalyticsMetaFunctionArgument.
        The argument value.


        :return: The argument_value of this LogAnalyticsMetaFunctionArgument.
        :rtype: str
        """
        return self._argument_value

    @argument_value.setter
    def argument_value(self, argument_value):
        """
        Sets the argument_value of this LogAnalyticsMetaFunctionArgument.
        The argument value.


        :param argument_value: The argument_value of this LogAnalyticsMetaFunctionArgument.
        :type: str
        """
        self._argument_value = argument_value

    @property
    def argument_reference(self):
        """
        Gets the argument_reference of this LogAnalyticsMetaFunctionArgument.
        The argument unique identifier as a string.


        :return: The argument_reference of this LogAnalyticsMetaFunctionArgument.
        :rtype: str
        """
        return self._argument_reference

    @argument_reference.setter
    def argument_reference(self, argument_reference):
        """
        Sets the argument_reference of this LogAnalyticsMetaFunctionArgument.
        The argument unique identifier as a string.


        :param argument_reference: The argument_reference of this LogAnalyticsMetaFunctionArgument.
        :type: str
        """
        self._argument_reference = argument_reference

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
