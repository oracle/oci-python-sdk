# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomPropertyGetUsage(object):
    """
    Details of a single custom property
    """

    #: A constant which can be used with the data_type property of a CustomPropertyGetUsage.
    #: This constant has a value of "TEXT"
    DATA_TYPE_TEXT = "TEXT"

    #: A constant which can be used with the data_type property of a CustomPropertyGetUsage.
    #: This constant has a value of "RICH_TEXT"
    DATA_TYPE_RICH_TEXT = "RICH_TEXT"

    #: A constant which can be used with the data_type property of a CustomPropertyGetUsage.
    #: This constant has a value of "BOOLEAN"
    DATA_TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the data_type property of a CustomPropertyGetUsage.
    #: This constant has a value of "NUMBER"
    DATA_TYPE_NUMBER = "NUMBER"

    #: A constant which can be used with the data_type property of a CustomPropertyGetUsage.
    #: This constant has a value of "DATE"
    DATA_TYPE_DATE = "DATE"

    def __init__(self, **kwargs):
        """
        Initializes a new CustomPropertyGetUsage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CustomPropertyGetUsage.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this CustomPropertyGetUsage.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CustomPropertyGetUsage.
        :type description: str

        :param value:
            The value to assign to the value property of this CustomPropertyGetUsage.
        :type value: str

        :param data_type:
            The value to assign to the data_type property of this CustomPropertyGetUsage.
            Allowed values for this property are: "TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_type: str

        :param namespace_name:
            The value to assign to the namespace_name property of this CustomPropertyGetUsage.
        :type namespace_name: str

        :param namespace_key:
            The value to assign to the namespace_key property of this CustomPropertyGetUsage.
        :type namespace_key: str

        :param is_multi_valued:
            The value to assign to the is_multi_valued property of this CustomPropertyGetUsage.
        :type is_multi_valued: bool

        :param is_hidden:
            The value to assign to the is_hidden property of this CustomPropertyGetUsage.
        :type is_hidden: bool

        :param is_editable:
            The value to assign to the is_editable property of this CustomPropertyGetUsage.
        :type is_editable: bool

        :param is_shown_in_list:
            The value to assign to the is_shown_in_list property of this CustomPropertyGetUsage.
        :type is_shown_in_list: bool

        :param is_event_enabled:
            The value to assign to the is_event_enabled property of this CustomPropertyGetUsage.
        :type is_event_enabled: bool

        :param is_list_type:
            The value to assign to the is_list_type property of this CustomPropertyGetUsage.
        :type is_list_type: bool

        :param allowed_values:
            The value to assign to the allowed_values property of this CustomPropertyGetUsage.
        :type allowed_values: list[str]

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'value': 'str',
            'data_type': 'str',
            'namespace_name': 'str',
            'namespace_key': 'str',
            'is_multi_valued': 'bool',
            'is_hidden': 'bool',
            'is_editable': 'bool',
            'is_shown_in_list': 'bool',
            'is_event_enabled': 'bool',
            'is_list_type': 'bool',
            'allowed_values': 'list[str]'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'value': 'value',
            'data_type': 'dataType',
            'namespace_name': 'namespaceName',
            'namespace_key': 'namespaceKey',
            'is_multi_valued': 'isMultiValued',
            'is_hidden': 'isHidden',
            'is_editable': 'isEditable',
            'is_shown_in_list': 'isShownInList',
            'is_event_enabled': 'isEventEnabled',
            'is_list_type': 'isListType',
            'allowed_values': 'allowedValues'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._value = None
        self._data_type = None
        self._namespace_name = None
        self._namespace_key = None
        self._is_multi_valued = None
        self._is_hidden = None
        self._is_editable = None
        self._is_shown_in_list = None
        self._is_event_enabled = None
        self._is_list_type = None
        self._allowed_values = None

    @property
    def key(self):
        """
        Gets the key of this CustomPropertyGetUsage.
        Unique Identifier of the attribute which is ID


        :return: The key of this CustomPropertyGetUsage.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CustomPropertyGetUsage.
        Unique Identifier of the attribute which is ID


        :param key: The key of this CustomPropertyGetUsage.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this CustomPropertyGetUsage.
        Display name of the custom property


        :return: The display_name of this CustomPropertyGetUsage.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CustomPropertyGetUsage.
        Display name of the custom property


        :param display_name: The display_name of this CustomPropertyGetUsage.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CustomPropertyGetUsage.
        Description of the custom property


        :return: The description of this CustomPropertyGetUsage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CustomPropertyGetUsage.
        Description of the custom property


        :param description: The description of this CustomPropertyGetUsage.
        :type: str
        """
        self._description = description

    @property
    def value(self):
        """
        Gets the value of this CustomPropertyGetUsage.
        The custom property value


        :return: The value of this CustomPropertyGetUsage.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CustomPropertyGetUsage.
        The custom property value


        :param value: The value of this CustomPropertyGetUsage.
        :type: str
        """
        self._value = value

    @property
    def data_type(self):
        """
        Gets the data_type of this CustomPropertyGetUsage.
        The data type of the custom property

        Allowed values for this property are: "TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_type of this CustomPropertyGetUsage.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """
        Sets the data_type of this CustomPropertyGetUsage.
        The data type of the custom property


        :param data_type: The data_type of this CustomPropertyGetUsage.
        :type: str
        """
        allowed_values = ["TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE"]
        if not value_allowed_none_or_none_sentinel(data_type, allowed_values):
            data_type = 'UNKNOWN_ENUM_VALUE'
        self._data_type = data_type

    @property
    def namespace_name(self):
        """
        Gets the namespace_name of this CustomPropertyGetUsage.
        Namespace name of the custom property


        :return: The namespace_name of this CustomPropertyGetUsage.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this CustomPropertyGetUsage.
        Namespace name of the custom property


        :param namespace_name: The namespace_name of this CustomPropertyGetUsage.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def namespace_key(self):
        """
        Gets the namespace_key of this CustomPropertyGetUsage.
        Unique namespace key that is immutable


        :return: The namespace_key of this CustomPropertyGetUsage.
        :rtype: str
        """
        return self._namespace_key

    @namespace_key.setter
    def namespace_key(self, namespace_key):
        """
        Sets the namespace_key of this CustomPropertyGetUsage.
        Unique namespace key that is immutable


        :param namespace_key: The namespace_key of this CustomPropertyGetUsage.
        :type: str
        """
        self._namespace_key = namespace_key

    @property
    def is_multi_valued(self):
        """
        Gets the is_multi_valued of this CustomPropertyGetUsage.
        If this field allows multiple values to be set


        :return: The is_multi_valued of this CustomPropertyGetUsage.
        :rtype: bool
        """
        return self._is_multi_valued

    @is_multi_valued.setter
    def is_multi_valued(self, is_multi_valued):
        """
        Sets the is_multi_valued of this CustomPropertyGetUsage.
        If this field allows multiple values to be set


        :param is_multi_valued: The is_multi_valued of this CustomPropertyGetUsage.
        :type: bool
        """
        self._is_multi_valued = is_multi_valued

    @property
    def is_hidden(self):
        """
        Gets the is_hidden of this CustomPropertyGetUsage.
        If this field is a hidden field


        :return: The is_hidden of this CustomPropertyGetUsage.
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """
        Sets the is_hidden of this CustomPropertyGetUsage.
        If this field is a hidden field


        :param is_hidden: The is_hidden of this CustomPropertyGetUsage.
        :type: bool
        """
        self._is_hidden = is_hidden

    @property
    def is_editable(self):
        """
        Gets the is_editable of this CustomPropertyGetUsage.
        If this field is a editable field


        :return: The is_editable of this CustomPropertyGetUsage.
        :rtype: bool
        """
        return self._is_editable

    @is_editable.setter
    def is_editable(self, is_editable):
        """
        Sets the is_editable of this CustomPropertyGetUsage.
        If this field is a editable field


        :param is_editable: The is_editable of this CustomPropertyGetUsage.
        :type: bool
        """
        self._is_editable = is_editable

    @property
    def is_shown_in_list(self):
        """
        Gets the is_shown_in_list of this CustomPropertyGetUsage.
        If this field is displayed in a list view of applicable objects.


        :return: The is_shown_in_list of this CustomPropertyGetUsage.
        :rtype: bool
        """
        return self._is_shown_in_list

    @is_shown_in_list.setter
    def is_shown_in_list(self, is_shown_in_list):
        """
        Sets the is_shown_in_list of this CustomPropertyGetUsage.
        If this field is displayed in a list view of applicable objects.


        :param is_shown_in_list: The is_shown_in_list of this CustomPropertyGetUsage.
        :type: bool
        """
        self._is_shown_in_list = is_shown_in_list

    @property
    def is_event_enabled(self):
        """
        Gets the is_event_enabled of this CustomPropertyGetUsage.
        If an OCI Event will be emitted when the custom property is modified.


        :return: The is_event_enabled of this CustomPropertyGetUsage.
        :rtype: bool
        """
        return self._is_event_enabled

    @is_event_enabled.setter
    def is_event_enabled(self, is_event_enabled):
        """
        Sets the is_event_enabled of this CustomPropertyGetUsage.
        If an OCI Event will be emitted when the custom property is modified.


        :param is_event_enabled: The is_event_enabled of this CustomPropertyGetUsage.
        :type: bool
        """
        self._is_event_enabled = is_event_enabled

    @property
    def is_list_type(self):
        """
        Gets the is_list_type of this CustomPropertyGetUsage.
        Is this property allowed to have list of values


        :return: The is_list_type of this CustomPropertyGetUsage.
        :rtype: bool
        """
        return self._is_list_type

    @is_list_type.setter
    def is_list_type(self, is_list_type):
        """
        Sets the is_list_type of this CustomPropertyGetUsage.
        Is this property allowed to have list of values


        :param is_list_type: The is_list_type of this CustomPropertyGetUsage.
        :type: bool
        """
        self._is_list_type = is_list_type

    @property
    def allowed_values(self):
        """
        Gets the allowed_values of this CustomPropertyGetUsage.
        Allowed values for the custom property if any


        :return: The allowed_values of this CustomPropertyGetUsage.
        :rtype: list[str]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """
        Sets the allowed_values of this CustomPropertyGetUsage.
        Allowed values for the custom property if any


        :param allowed_values: The allowed_values of this CustomPropertyGetUsage.
        :type: list[str]
        """
        self._allowed_values = allowed_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
