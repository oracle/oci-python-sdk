# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigValue(object):
    """
    configuration item for multi list data type
    """

    #: A constant which can be used with the list_type property of a ConfigValue.
    #: This constant has a value of "MANAGED"
    LIST_TYPE_MANAGED = "MANAGED"

    #: A constant which can be used with the list_type property of a ConfigValue.
    #: This constant has a value of "CUSTOM"
    LIST_TYPE_CUSTOM = "CUSTOM"

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigValue object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param list_type:
            The value to assign to the list_type property of this ConfigValue.
            Allowed values for this property are: "MANAGED", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type list_type: str

        :param managed_list_type:
            The value to assign to the managed_list_type property of this ConfigValue.
        :type managed_list_type: str

        :param value:
            The value to assign to the value property of this ConfigValue.
        :type value: str

        """
        self.swagger_types = {
            'list_type': 'str',
            'managed_list_type': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'list_type': 'listType',
            'managed_list_type': 'managedListType',
            'value': 'value'
        }

        self._list_type = None
        self._managed_list_type = None
        self._value = None

    @property
    def list_type(self):
        """
        **[Required]** Gets the list_type of this ConfigValue.
        configuration list item type, either CUSTOM or MANAGED

        Allowed values for this property are: "MANAGED", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The list_type of this ConfigValue.
        :rtype: str
        """
        return self._list_type

    @list_type.setter
    def list_type(self, list_type):
        """
        Sets the list_type of this ConfigValue.
        configuration list item type, either CUSTOM or MANAGED


        :param list_type: The list_type of this ConfigValue.
        :type: str
        """
        allowed_values = ["MANAGED", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(list_type, allowed_values):
            list_type = 'UNKNOWN_ENUM_VALUE'
        self._list_type = list_type

    @property
    def managed_list_type(self):
        """
        **[Required]** Gets the managed_list_type of this ConfigValue.
        type of the managed list


        :return: The managed_list_type of this ConfigValue.
        :rtype: str
        """
        return self._managed_list_type

    @managed_list_type.setter
    def managed_list_type(self, managed_list_type):
        """
        Sets the managed_list_type of this ConfigValue.
        type of the managed list


        :param managed_list_type: The managed_list_type of this ConfigValue.
        :type: str
        """
        self._managed_list_type = managed_list_type

    @property
    def value(self):
        """
        **[Required]** Gets the value of this ConfigValue.
        configuration value


        :return: The value of this ConfigValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ConfigValue.
        configuration value


        :param value: The value of this ConfigValue.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
