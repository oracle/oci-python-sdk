# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigurationField(object):
    """
    Information required to migrate an application. Populated by the service as the source application is introspected
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigurationField object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ConfigurationField.
        :type name: str

        :param group:
            The value to assign to the group property of this ConfigurationField.
        :type group: str

        :param type:
            The value to assign to the type property of this ConfigurationField.
        :type type: str

        :param value:
            The value to assign to the value property of this ConfigurationField.
        :type value: str

        :param description:
            The value to assign to the description property of this ConfigurationField.
        :type description: str

        :param is_required:
            The value to assign to the is_required property of this ConfigurationField.
        :type is_required: bool

        :param is_mutable:
            The value to assign to the is_mutable property of this ConfigurationField.
        :type is_mutable: bool

        """
        self.swagger_types = {
            'name': 'str',
            'group': 'str',
            'type': 'str',
            'value': 'str',
            'description': 'str',
            'is_required': 'bool',
            'is_mutable': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'group': 'group',
            'type': 'type',
            'value': 'value',
            'description': 'description',
            'is_required': 'isRequired',
            'is_mutable': 'isMutable'
        }

        self._name = None
        self._group = None
        self._type = None
        self._value = None
        self._description = None
        self._is_required = None
        self._is_mutable = None

    @property
    def name(self):
        """
        Gets the name of this ConfigurationField.
        The name of the configuration field


        :return: The name of this ConfigurationField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConfigurationField.
        The name of the configuration field


        :param name: The name of this ConfigurationField.
        :type: str
        """
        self._name = name

    @property
    def group(self):
        """
        Gets the group of this ConfigurationField.
        The name of the group to which this field belongs, if any.


        :return: The group of this ConfigurationField.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this ConfigurationField.
        The name of the group to which this field belongs, if any.


        :param group: The group of this ConfigurationField.
        :type: str
        """
        self._group = group

    @property
    def type(self):
        """
        Gets the type of this ConfigurationField.
        The configuration field type


        :return: The type of this ConfigurationField.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ConfigurationField.
        The configuration field type


        :param type: The type of this ConfigurationField.
        :type: str
        """
        self._type = type

    @property
    def value(self):
        """
        Gets the value of this ConfigurationField.
        The value of the field


        :return: The value of this ConfigurationField.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ConfigurationField.
        The value of the field


        :param value: The value of this ConfigurationField.
        :type: str
        """
        self._value = value

    @property
    def description(self):
        """
        Gets the description of this ConfigurationField.
        Help text to guide the customer in setting the configuration value


        :return: The description of this ConfigurationField.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ConfigurationField.
        Help text to guide the customer in setting the configuration value


        :param description: The description of this ConfigurationField.
        :type: str
        """
        self._description = description

    @property
    def is_required(self):
        """
        Gets the is_required of this ConfigurationField.
        Indicates whether or not the field is required (defaults to true)


        :return: The is_required of this ConfigurationField.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """
        Sets the is_required of this ConfigurationField.
        Indicates whether or not the field is required (defaults to true)


        :param is_required: The is_required of this ConfigurationField.
        :type: bool
        """
        self._is_required = is_required

    @property
    def is_mutable(self):
        """
        Gets the is_mutable of this ConfigurationField.
        Indicates whether or not the field may be modified (defaults to true)


        :return: The is_mutable of this ConfigurationField.
        :rtype: bool
        """
        return self._is_mutable

    @is_mutable.setter
    def is_mutable(self, is_mutable):
        """
        Sets the is_mutable of this ConfigurationField.
        Indicates whether or not the field may be modified (defaults to true)


        :param is_mutable: The is_mutable of this ConfigurationField.
        :type: bool
        """
        self._is_mutable = is_mutable

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
