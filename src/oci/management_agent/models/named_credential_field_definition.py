# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200202


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NamedCredentialFieldDefinition(object):
    """
    A named credential field metadata definition
    """

    #: A constant which can be used with the value_category property of a NamedCredentialFieldDefinition.
    #: This constant has a value of "CLEAR_TEXT"
    VALUE_CATEGORY_CLEAR_TEXT = "CLEAR_TEXT"

    #: A constant which can be used with the value_category property of a NamedCredentialFieldDefinition.
    #: This constant has a value of "SECRET_IDENTIFIER"
    VALUE_CATEGORY_SECRET_IDENTIFIER = "SECRET_IDENTIFIER"

    #: A constant which can be used with the value_category property of a NamedCredentialFieldDefinition.
    #: This constant has a value of "ADB_IDENTIFIER"
    VALUE_CATEGORY_ADB_IDENTIFIER = "ADB_IDENTIFIER"

    #: A constant which can be used with the value_category property of a NamedCredentialFieldDefinition.
    #: This constant has a value of "ALLOWED_VALUE"
    VALUE_CATEGORY_ALLOWED_VALUE = "ALLOWED_VALUE"

    def __init__(self, **kwargs):
        """
        Initializes a new NamedCredentialFieldDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this NamedCredentialFieldDefinition.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this NamedCredentialFieldDefinition.
        :type display_name: str

        :param default_value:
            The value to assign to the default_value property of this NamedCredentialFieldDefinition.
        :type default_value: str

        :param regex:
            The value to assign to the regex property of this NamedCredentialFieldDefinition.
        :type regex: str

        :param allowed_values:
            The value to assign to the allowed_values property of this NamedCredentialFieldDefinition.
        :type allowed_values: list[str]

        :param value_category:
            The value to assign to the value_category property of this NamedCredentialFieldDefinition.
            Allowed values for items in this list are: "CLEAR_TEXT", "SECRET_IDENTIFIER", "ADB_IDENTIFIER", "ALLOWED_VALUE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type value_category: list[str]

        :param is_required:
            The value to assign to the is_required property of this NamedCredentialFieldDefinition.
        :type is_required: bool

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'default_value': 'str',
            'regex': 'str',
            'allowed_values': 'list[str]',
            'value_category': 'list[str]',
            'is_required': 'bool'
        }
        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'default_value': 'defaultValue',
            'regex': 'regex',
            'allowed_values': 'allowedValues',
            'value_category': 'valueCategory',
            'is_required': 'isRequired'
        }
        self._name = None
        self._display_name = None
        self._default_value = None
        self._regex = None
        self._allowed_values = None
        self._value_category = None
        self._is_required = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this NamedCredentialFieldDefinition.
        The field name


        :return: The name of this NamedCredentialFieldDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NamedCredentialFieldDefinition.
        The field name


        :param name: The name of this NamedCredentialFieldDefinition.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this NamedCredentialFieldDefinition.
        The field display name


        :return: The display_name of this NamedCredentialFieldDefinition.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this NamedCredentialFieldDefinition.
        The field display name


        :param display_name: The display_name of this NamedCredentialFieldDefinition.
        :type: str
        """
        self._display_name = display_name

    @property
    def default_value(self):
        """
        Gets the default_value of this NamedCredentialFieldDefinition.
        The default value which will be used if no value is set.  If defaultValue is empty, then no default will be set.


        :return: The default_value of this NamedCredentialFieldDefinition.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this NamedCredentialFieldDefinition.
        The default value which will be used if no value is set.  If defaultValue is empty, then no default will be set.


        :param default_value: The default_value of this NamedCredentialFieldDefinition.
        :type: str
        """
        self._default_value = default_value

    @property
    def regex(self):
        """
        Gets the regex of this NamedCredentialFieldDefinition.
        Optional regular expression definition which will be applied to the value when valueCategory is CLEAR_TEXT


        :return: The regex of this NamedCredentialFieldDefinition.
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """
        Sets the regex of this NamedCredentialFieldDefinition.
        Optional regular expression definition which will be applied to the value when valueCategory is CLEAR_TEXT


        :param regex: The regex of this NamedCredentialFieldDefinition.
        :type: str
        """
        self._regex = regex

    @property
    def allowed_values(self):
        """
        Gets the allowed_values of this NamedCredentialFieldDefinition.
        List of values which can be applied to the value when valueCategory is ALLOWED_VALUES


        :return: The allowed_values of this NamedCredentialFieldDefinition.
        :rtype: list[str]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """
        Sets the allowed_values of this NamedCredentialFieldDefinition.
        List of values which can be applied to the value when valueCategory is ALLOWED_VALUES


        :param allowed_values: The allowed_values of this NamedCredentialFieldDefinition.
        :type: list[str]
        """
        self._allowed_values = allowed_values

    @property
    def value_category(self):
        """
        **[Required]** Gets the value_category of this NamedCredentialFieldDefinition.
        List of value categories of field allowed for this property

        Allowed values for items in this list are: "CLEAR_TEXT", "SECRET_IDENTIFIER", "ADB_IDENTIFIER", "ALLOWED_VALUE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The value_category of this NamedCredentialFieldDefinition.
        :rtype: list[str]
        """
        return self._value_category

    @value_category.setter
    def value_category(self, value_category):
        """
        Sets the value_category of this NamedCredentialFieldDefinition.
        List of value categories of field allowed for this property


        :param value_category: The value_category of this NamedCredentialFieldDefinition.
        :type: list[str]
        """
        allowed_values = ["CLEAR_TEXT", "SECRET_IDENTIFIER", "ADB_IDENTIFIER", "ALLOWED_VALUE"]
        if value_category:
            value_category[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in value_category]
        self._value_category = value_category

    @property
    def is_required(self):
        """
        Gets the is_required of this NamedCredentialFieldDefinition.
        Set to true if the field must be defined


        :return: The is_required of this NamedCredentialFieldDefinition.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """
        Sets the is_required of this NamedCredentialFieldDefinition.
        Set to true if the field must be defined


        :param is_required: The is_required of this NamedCredentialFieldDefinition.
        :type: bool
        """
        self._is_required = is_required

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
