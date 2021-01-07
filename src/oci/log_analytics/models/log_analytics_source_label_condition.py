# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsSourceLabelCondition(object):
    """
    LogAnalyticsSourceLabelCondition
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsSourceLabelCondition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message:
            The value to assign to the message property of this LogAnalyticsSourceLabelCondition.
        :type message: str

        :param is_visible:
            The value to assign to the is_visible property of this LogAnalyticsSourceLabelCondition.
        :type is_visible: bool

        :param block_condition_field:
            The value to assign to the block_condition_field property of this LogAnalyticsSourceLabelCondition.
        :type block_condition_field: str

        :param block_condition_operator:
            The value to assign to the block_condition_operator property of this LogAnalyticsSourceLabelCondition.
        :type block_condition_operator: str

        :param block_condition_value:
            The value to assign to the block_condition_value property of this LogAnalyticsSourceLabelCondition.
        :type block_condition_value: str

        :param label_condition_value:
            The value to assign to the label_condition_value property of this LogAnalyticsSourceLabelCondition.
        :type label_condition_value: str

        :param label_condition_values:
            The value to assign to the label_condition_values property of this LogAnalyticsSourceLabelCondition.
        :type label_condition_values: list[str]

        :param content_example:
            The value to assign to the content_example property of this LogAnalyticsSourceLabelCondition.
        :type content_example: str

        :param is_enabled:
            The value to assign to the is_enabled property of this LogAnalyticsSourceLabelCondition.
        :type is_enabled: bool

        :param field_name:
            The value to assign to the field_name property of this LogAnalyticsSourceLabelCondition.
        :type field_name: str

        :param label_condition_id:
            The value to assign to the label_condition_id property of this LogAnalyticsSourceLabelCondition.
        :type label_condition_id: int

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsSourceLabelCondition.
        :type is_system: bool

        :param label_condition_operator:
            The value to assign to the label_condition_operator property of this LogAnalyticsSourceLabelCondition.
        :type label_condition_operator: str

        :param source_id:
            The value to assign to the source_id property of this LogAnalyticsSourceLabelCondition.
        :type source_id: int

        :param label_display_name:
            The value to assign to the label_display_name property of this LogAnalyticsSourceLabelCondition.
        :type label_display_name: str

        :param storage_field:
            The value to assign to the storage_field property of this LogAnalyticsSourceLabelCondition.
        :type storage_field: str

        :param label_name:
            The value to assign to the label_name property of this LogAnalyticsSourceLabelCondition.
        :type label_name: str

        :param is_inline_label_existing_in_database:
            The value to assign to the is_inline_label_existing_in_database property of this LogAnalyticsSourceLabelCondition.
        :type is_inline_label_existing_in_database: bool

        """
        self.swagger_types = {
            'message': 'str',
            'is_visible': 'bool',
            'block_condition_field': 'str',
            'block_condition_operator': 'str',
            'block_condition_value': 'str',
            'label_condition_value': 'str',
            'label_condition_values': 'list[str]',
            'content_example': 'str',
            'is_enabled': 'bool',
            'field_name': 'str',
            'label_condition_id': 'int',
            'is_system': 'bool',
            'label_condition_operator': 'str',
            'source_id': 'int',
            'label_display_name': 'str',
            'storage_field': 'str',
            'label_name': 'str',
            'is_inline_label_existing_in_database': 'bool'
        }

        self.attribute_map = {
            'message': 'message',
            'is_visible': 'isVisible',
            'block_condition_field': 'blockConditionField',
            'block_condition_operator': 'blockConditionOperator',
            'block_condition_value': 'blockConditionValue',
            'label_condition_value': 'labelConditionValue',
            'label_condition_values': 'labelConditionValues',
            'content_example': 'contentExample',
            'is_enabled': 'isEnabled',
            'field_name': 'fieldName',
            'label_condition_id': 'labelConditionId',
            'is_system': 'isSystem',
            'label_condition_operator': 'labelConditionOperator',
            'source_id': 'sourceId',
            'label_display_name': 'labelDisplayName',
            'storage_field': 'storageField',
            'label_name': 'labelName',
            'is_inline_label_existing_in_database': 'isInlineLabelExistingInDatabase'
        }

        self._message = None
        self._is_visible = None
        self._block_condition_field = None
        self._block_condition_operator = None
        self._block_condition_value = None
        self._label_condition_value = None
        self._label_condition_values = None
        self._content_example = None
        self._is_enabled = None
        self._field_name = None
        self._label_condition_id = None
        self._is_system = None
        self._label_condition_operator = None
        self._source_id = None
        self._label_display_name = None
        self._storage_field = None
        self._label_name = None
        self._is_inline_label_existing_in_database = None

    @property
    def message(self):
        """
        Gets the message of this LogAnalyticsSourceLabelCondition.
        message


        :return: The message of this LogAnalyticsSourceLabelCondition.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this LogAnalyticsSourceLabelCondition.
        message


        :param message: The message of this LogAnalyticsSourceLabelCondition.
        :type: str
        """
        self._message = message

    @property
    def is_visible(self):
        """
        Gets the is_visible of this LogAnalyticsSourceLabelCondition.
        visible flag


        :return: The is_visible of this LogAnalyticsSourceLabelCondition.
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """
        Sets the is_visible of this LogAnalyticsSourceLabelCondition.
        visible flag


        :param is_visible: The is_visible of this LogAnalyticsSourceLabelCondition.
        :type: bool
        """
        self._is_visible = is_visible

    @property
    def block_condition_field(self):
        """
        Gets the block_condition_field of this LogAnalyticsSourceLabelCondition.
        block condition field


        :return: The block_condition_field of this LogAnalyticsSourceLabelCondition.
        :rtype: str
        """
        return self._block_condition_field

    @block_condition_field.setter
    def block_condition_field(self, block_condition_field):
        """
        Sets the block_condition_field of this LogAnalyticsSourceLabelCondition.
        block condition field


        :param block_condition_field: The block_condition_field of this LogAnalyticsSourceLabelCondition.
        :type: str
        """
        self._block_condition_field = block_condition_field

    @property
    def block_condition_operator(self):
        """
        Gets the block_condition_operator of this LogAnalyticsSourceLabelCondition.
        block condition operator


        :return: The block_condition_operator of this LogAnalyticsSourceLabelCondition.
        :rtype: str
        """
        return self._block_condition_operator

    @block_condition_operator.setter
    def block_condition_operator(self, block_condition_operator):
        """
        Sets the block_condition_operator of this LogAnalyticsSourceLabelCondition.
        block condition operator


        :param block_condition_operator: The block_condition_operator of this LogAnalyticsSourceLabelCondition.
        :type: str
        """
        self._block_condition_operator = block_condition_operator

    @property
    def block_condition_value(self):
        """
        Gets the block_condition_value of this LogAnalyticsSourceLabelCondition.
        block condition value


        :return: The block_condition_value of this LogAnalyticsSourceLabelCondition.
        :rtype: str
        """
        return self._block_condition_value

    @block_condition_value.setter
    def block_condition_value(self, block_condition_value):
        """
        Sets the block_condition_value of this LogAnalyticsSourceLabelCondition.
        block condition value


        :param block_condition_value: The block_condition_value of this LogAnalyticsSourceLabelCondition.
        :type: str
        """
        self._block_condition_value = block_condition_value

    @property
    def label_condition_value(self):
        """
        Gets the label_condition_value of this LogAnalyticsSourceLabelCondition.
        condition value


        :return: The label_condition_value of this LogAnalyticsSourceLabelCondition.
        :rtype: str
        """
        return self._label_condition_value

    @label_condition_value.setter
    def label_condition_value(self, label_condition_value):
        """
        Sets the label_condition_value of this LogAnalyticsSourceLabelCondition.
        condition value


        :param label_condition_value: The label_condition_value of this LogAnalyticsSourceLabelCondition.
        :type: str
        """
        self._label_condition_value = label_condition_value

    @property
    def label_condition_values(self):
        """
        Gets the label_condition_values of this LogAnalyticsSourceLabelCondition.
        list of condition values


        :return: The label_condition_values of this LogAnalyticsSourceLabelCondition.
        :rtype: list[str]
        """
        return self._label_condition_values

    @label_condition_values.setter
    def label_condition_values(self, label_condition_values):
        """
        Sets the label_condition_values of this LogAnalyticsSourceLabelCondition.
        list of condition values


        :param label_condition_values: The label_condition_values of this LogAnalyticsSourceLabelCondition.
        :type: list[str]
        """
        self._label_condition_values = label_condition_values

    @property
    def content_example(self):
        """
        Gets the content_example of this LogAnalyticsSourceLabelCondition.
        content example


        :return: The content_example of this LogAnalyticsSourceLabelCondition.
        :rtype: str
        """
        return self._content_example

    @content_example.setter
    def content_example(self, content_example):
        """
        Sets the content_example of this LogAnalyticsSourceLabelCondition.
        content example


        :param content_example: The content_example of this LogAnalyticsSourceLabelCondition.
        :type: str
        """
        self._content_example = content_example

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this LogAnalyticsSourceLabelCondition.
        enabled


        :return: The is_enabled of this LogAnalyticsSourceLabelCondition.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this LogAnalyticsSourceLabelCondition.
        enabled


        :param is_enabled: The is_enabled of this LogAnalyticsSourceLabelCondition.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def field_name(self):
        """
        Gets the field_name of this LogAnalyticsSourceLabelCondition.
        field internal name


        :return: The field_name of this LogAnalyticsSourceLabelCondition.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this LogAnalyticsSourceLabelCondition.
        field internal name


        :param field_name: The field_name of this LogAnalyticsSourceLabelCondition.
        :type: str
        """
        self._field_name = field_name

    @property
    def label_condition_id(self):
        """
        Gets the label_condition_id of this LogAnalyticsSourceLabelCondition.
        Id


        :return: The label_condition_id of this LogAnalyticsSourceLabelCondition.
        :rtype: int
        """
        return self._label_condition_id

    @label_condition_id.setter
    def label_condition_id(self, label_condition_id):
        """
        Sets the label_condition_id of this LogAnalyticsSourceLabelCondition.
        Id


        :param label_condition_id: The label_condition_id of this LogAnalyticsSourceLabelCondition.
        :type: int
        """
        self._label_condition_id = label_condition_id

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsSourceLabelCondition.
        is system flag


        :return: The is_system of this LogAnalyticsSourceLabelCondition.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsSourceLabelCondition.
        is system flag


        :param is_system: The is_system of this LogAnalyticsSourceLabelCondition.
        :type: bool
        """
        self._is_system = is_system

    @property
    def label_condition_operator(self):
        """
        Gets the label_condition_operator of this LogAnalyticsSourceLabelCondition.
        operator


        :return: The label_condition_operator of this LogAnalyticsSourceLabelCondition.
        :rtype: str
        """
        return self._label_condition_operator

    @label_condition_operator.setter
    def label_condition_operator(self, label_condition_operator):
        """
        Sets the label_condition_operator of this LogAnalyticsSourceLabelCondition.
        operator


        :param label_condition_operator: The label_condition_operator of this LogAnalyticsSourceLabelCondition.
        :type: str
        """
        self._label_condition_operator = label_condition_operator

    @property
    def source_id(self):
        """
        Gets the source_id of this LogAnalyticsSourceLabelCondition.
        source Id


        :return: The source_id of this LogAnalyticsSourceLabelCondition.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this LogAnalyticsSourceLabelCondition.
        source Id


        :param source_id: The source_id of this LogAnalyticsSourceLabelCondition.
        :type: int
        """
        self._source_id = source_id

    @property
    def label_display_name(self):
        """
        Gets the label_display_name of this LogAnalyticsSourceLabelCondition.
        label display name


        :return: The label_display_name of this LogAnalyticsSourceLabelCondition.
        :rtype: str
        """
        return self._label_display_name

    @label_display_name.setter
    def label_display_name(self, label_display_name):
        """
        Sets the label_display_name of this LogAnalyticsSourceLabelCondition.
        label display name


        :param label_display_name: The label_display_name of this LogAnalyticsSourceLabelCondition.
        :type: str
        """
        self._label_display_name = label_display_name

    @property
    def storage_field(self):
        """
        Gets the storage_field of this LogAnalyticsSourceLabelCondition.
        label storage field


        :return: The storage_field of this LogAnalyticsSourceLabelCondition.
        :rtype: str
        """
        return self._storage_field

    @storage_field.setter
    def storage_field(self, storage_field):
        """
        Sets the storage_field of this LogAnalyticsSourceLabelCondition.
        label storage field


        :param storage_field: The storage_field of this LogAnalyticsSourceLabelCondition.
        :type: str
        """
        self._storage_field = storage_field

    @property
    def label_name(self):
        """
        Gets the label_name of this LogAnalyticsSourceLabelCondition.
        label name


        :return: The label_name of this LogAnalyticsSourceLabelCondition.
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        """
        Sets the label_name of this LogAnalyticsSourceLabelCondition.
        label name


        :param label_name: The label_name of this LogAnalyticsSourceLabelCondition.
        :type: str
        """
        self._label_name = label_name

    @property
    def is_inline_label_existing_in_database(self):
        """
        Gets the is_inline_label_existing_in_database of this LogAnalyticsSourceLabelCondition.
        inline label exists in DB flag


        :return: The is_inline_label_existing_in_database of this LogAnalyticsSourceLabelCondition.
        :rtype: bool
        """
        return self._is_inline_label_existing_in_database

    @is_inline_label_existing_in_database.setter
    def is_inline_label_existing_in_database(self, is_inline_label_existing_in_database):
        """
        Sets the is_inline_label_existing_in_database of this LogAnalyticsSourceLabelCondition.
        inline label exists in DB flag


        :param is_inline_label_existing_in_database: The is_inline_label_existing_in_database of this LogAnalyticsSourceLabelCondition.
        :type: bool
        """
        self._is_inline_label_existing_in_database = is_inline_label_existing_in_database

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
