# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsExtendedField(object):
    """
    LogAnalyticsExtendedField
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsExtendedField object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field:
            The value to assign to the field property of this LogAnalyticsExtendedField.
        :type field: oci.log_analytics.models.LogAnalyticsField

        :param extended_field_definition:
            The value to assign to the extended_field_definition property of this LogAnalyticsExtendedField.
        :type extended_field_definition: oci.log_analytics.models.LogAnalyticsSourceExtendedFieldDefinition

        :param extended_field_definition_id:
            The value to assign to the extended_field_definition_id property of this LogAnalyticsExtendedField.
        :type extended_field_definition_id: int

        :param field_name:
            The value to assign to the field_name property of this LogAnalyticsExtendedField.
        :type field_name: str

        :param field_display_name:
            The value to assign to the field_display_name property of this LogAnalyticsExtendedField.
        :type field_display_name: str

        :param saved_regular_expression_name:
            The value to assign to the saved_regular_expression_name property of this LogAnalyticsExtendedField.
        :type saved_regular_expression_name: str

        :param extended_field_id:
            The value to assign to the extended_field_id property of this LogAnalyticsExtendedField.
        :type extended_field_id: int

        """
        self.swagger_types = {
            'field': 'LogAnalyticsField',
            'extended_field_definition': 'LogAnalyticsSourceExtendedFieldDefinition',
            'extended_field_definition_id': 'int',
            'field_name': 'str',
            'field_display_name': 'str',
            'saved_regular_expression_name': 'str',
            'extended_field_id': 'int'
        }

        self.attribute_map = {
            'field': 'field',
            'extended_field_definition': 'extendedFieldDefinition',
            'extended_field_definition_id': 'extendedFieldDefinitionId',
            'field_name': 'fieldName',
            'field_display_name': 'fieldDisplayName',
            'saved_regular_expression_name': 'savedRegularExpressionName',
            'extended_field_id': 'extendedFieldId'
        }

        self._field = None
        self._extended_field_definition = None
        self._extended_field_definition_id = None
        self._field_name = None
        self._field_display_name = None
        self._saved_regular_expression_name = None
        self._extended_field_id = None

    @property
    def field(self):
        """
        Gets the field of this LogAnalyticsExtendedField.

        :return: The field of this LogAnalyticsExtendedField.
        :rtype: oci.log_analytics.models.LogAnalyticsField
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this LogAnalyticsExtendedField.

        :param field: The field of this LogAnalyticsExtendedField.
        :type: oci.log_analytics.models.LogAnalyticsField
        """
        self._field = field

    @property
    def extended_field_definition(self):
        """
        Gets the extended_field_definition of this LogAnalyticsExtendedField.

        :return: The extended_field_definition of this LogAnalyticsExtendedField.
        :rtype: oci.log_analytics.models.LogAnalyticsSourceExtendedFieldDefinition
        """
        return self._extended_field_definition

    @extended_field_definition.setter
    def extended_field_definition(self, extended_field_definition):
        """
        Sets the extended_field_definition of this LogAnalyticsExtendedField.

        :param extended_field_definition: The extended_field_definition of this LogAnalyticsExtendedField.
        :type: oci.log_analytics.models.LogAnalyticsSourceExtendedFieldDefinition
        """
        self._extended_field_definition = extended_field_definition

    @property
    def extended_field_definition_id(self):
        """
        Gets the extended_field_definition_id of this LogAnalyticsExtendedField.
        The extended field unique identifier.


        :return: The extended_field_definition_id of this LogAnalyticsExtendedField.
        :rtype: int
        """
        return self._extended_field_definition_id

    @extended_field_definition_id.setter
    def extended_field_definition_id(self, extended_field_definition_id):
        """
        Sets the extended_field_definition_id of this LogAnalyticsExtendedField.
        The extended field unique identifier.


        :param extended_field_definition_id: The extended_field_definition_id of this LogAnalyticsExtendedField.
        :type: int
        """
        self._extended_field_definition_id = extended_field_definition_id

    @property
    def field_name(self):
        """
        Gets the field_name of this LogAnalyticsExtendedField.
        The field internal name


        :return: The field_name of this LogAnalyticsExtendedField.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this LogAnalyticsExtendedField.
        The field internal name


        :param field_name: The field_name of this LogAnalyticsExtendedField.
        :type: str
        """
        self._field_name = field_name

    @property
    def field_display_name(self):
        """
        Gets the field_display_name of this LogAnalyticsExtendedField.
        The field internal display name.


        :return: The field_display_name of this LogAnalyticsExtendedField.
        :rtype: str
        """
        return self._field_display_name

    @field_display_name.setter
    def field_display_name(self, field_display_name):
        """
        Sets the field_display_name of this LogAnalyticsExtendedField.
        The field internal display name.


        :param field_display_name: The field_display_name of this LogAnalyticsExtendedField.
        :type: str
        """
        self._field_display_name = field_display_name

    @property
    def saved_regular_expression_name(self):
        """
        Gets the saved_regular_expression_name of this LogAnalyticsExtendedField.
        The saved regular expression name.


        :return: The saved_regular_expression_name of this LogAnalyticsExtendedField.
        :rtype: str
        """
        return self._saved_regular_expression_name

    @saved_regular_expression_name.setter
    def saved_regular_expression_name(self, saved_regular_expression_name):
        """
        Sets the saved_regular_expression_name of this LogAnalyticsExtendedField.
        The saved regular expression name.


        :param saved_regular_expression_name: The saved_regular_expression_name of this LogAnalyticsExtendedField.
        :type: str
        """
        self._saved_regular_expression_name = saved_regular_expression_name

    @property
    def extended_field_id(self):
        """
        Gets the extended_field_id of this LogAnalyticsExtendedField.
        The extended field unique identifier.


        :return: The extended_field_id of this LogAnalyticsExtendedField.
        :rtype: int
        """
        return self._extended_field_id

    @extended_field_id.setter
    def extended_field_id(self, extended_field_id):
        """
        Sets the extended_field_id of this LogAnalyticsExtendedField.
        The extended field unique identifier.


        :param extended_field_id: The extended_field_id of this LogAnalyticsExtendedField.
        :type: int
        """
        self._extended_field_id = extended_field_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
