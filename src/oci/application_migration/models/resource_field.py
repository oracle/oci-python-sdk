# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceField(object):
    """
    Resource object that can be used to pass details about any list of resources associated with Migrations. The List of resources are added to ConfigurationField to add the capability to pass lists of resources of any type and group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceField object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ResourceField.
        :type name: str

        :param group:
            The value to assign to the group property of this ResourceField.
        :type group: str

        :param type:
            The value to assign to the type property of this ResourceField.
        :type type: str

        :param value:
            The value to assign to the value property of this ResourceField.
        :type value: str

        """
        self.swagger_types = {
            'name': 'str',
            'group': 'str',
            'type': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'group': 'group',
            'type': 'type',
            'value': 'value'
        }

        self._name = None
        self._group = None
        self._type = None
        self._value = None

    @property
    def name(self):
        """
        Gets the name of this ResourceField.
        The display name of the resource field.


        :return: The name of this ResourceField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ResourceField.
        The display name of the resource field.


        :param name: The name of this ResourceField.
        :type: str
        """
        self._name = name

    @property
    def group(self):
        """
        Gets the group of this ResourceField.
        The name of the group to which this field belongs to.


        :return: The group of this ResourceField.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this ResourceField.
        The name of the group to which this field belongs to.


        :param group: The group of this ResourceField.
        :type: str
        """
        self._group = group

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ResourceField.
        The type of the resource field.


        :return: The type of this ResourceField.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ResourceField.
        The type of the resource field.


        :param type: The type of this ResourceField.
        :type: str
        """
        self._type = type

    @property
    def value(self):
        """
        **[Required]** Gets the value of this ResourceField.
        The value of the field.


        :return: The value of this ResourceField.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ResourceField.
        The value of the field.


        :param value: The value of this ResourceField.
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
