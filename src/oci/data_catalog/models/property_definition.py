# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PropertyDefinition(object):
    """
    Details of a single type property.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PropertyDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this PropertyDefinition.
        :type name: str

        :param type:
            The value to assign to the type property of this PropertyDefinition.
        :type type: str

        :param is_required:
            The value to assign to the is_required property of this PropertyDefinition.
        :type is_required: bool

        :param is_updatable:
            The value to assign to the is_updatable property of this PropertyDefinition.
        :type is_updatable: bool

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'is_required': 'bool',
            'is_updatable': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'is_required': 'isRequired',
            'is_updatable': 'isUpdatable'
        }

        self._name = None
        self._type = None
        self._is_required = None
        self._is_updatable = None

    @property
    def name(self):
        """
        Gets the name of this PropertyDefinition.
        Name of the property.


        :return: The name of this PropertyDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PropertyDefinition.
        Name of the property.


        :param name: The name of this PropertyDefinition.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this PropertyDefinition.
        The properties value type.


        :return: The type of this PropertyDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PropertyDefinition.
        The properties value type.


        :param type: The type of this PropertyDefinition.
        :type: str
        """
        self._type = type

    @property
    def is_required(self):
        """
        Gets the is_required of this PropertyDefinition.
        Whether instances of the type are required to set this property.


        :return: The is_required of this PropertyDefinition.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """
        Sets the is_required of this PropertyDefinition.
        Whether instances of the type are required to set this property.


        :param is_required: The is_required of this PropertyDefinition.
        :type: bool
        """
        self._is_required = is_required

    @property
    def is_updatable(self):
        """
        Gets the is_updatable of this PropertyDefinition.
        Indicates if this property value can be updated.


        :return: The is_updatable of this PropertyDefinition.
        :rtype: bool
        """
        return self._is_updatable

    @is_updatable.setter
    def is_updatable(self, is_updatable):
        """
        Sets the is_updatable of this PropertyDefinition.
        Indicates if this property value can be updated.


        :param is_updatable: The is_updatable of this PropertyDefinition.
        :type: bool
        """
        self._is_updatable = is_updatable

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
