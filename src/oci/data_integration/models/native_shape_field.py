# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NativeShapeField(object):
    """
    The native shape field object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NativeShapeField object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this NativeShapeField.
        :type name: str

        :param model_type:
            The value to assign to the model_type property of this NativeShapeField.
        :type model_type: str

        :param type:
            The value to assign to the type property of this NativeShapeField.
        :type type: object

        :param config_values:
            The value to assign to the config_values property of this NativeShapeField.
        :type config_values: oci.data_integration.models.ConfigValues

        :param position:
            The value to assign to the position property of this NativeShapeField.
        :type position: int

        :param default_value_string:
            The value to assign to the default_value_string property of this NativeShapeField.
        :type default_value_string: str

        :param is_mandatory:
            The value to assign to the is_mandatory property of this NativeShapeField.
        :type is_mandatory: bool

        """
        self.swagger_types = {
            'name': 'str',
            'model_type': 'str',
            'type': 'object',
            'config_values': 'ConfigValues',
            'position': 'int',
            'default_value_string': 'str',
            'is_mandatory': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'model_type': 'modelType',
            'type': 'type',
            'config_values': 'configValues',
            'position': 'position',
            'default_value_string': 'defaultValueString',
            'is_mandatory': 'isMandatory'
        }

        self._name = None
        self._model_type = None
        self._type = None
        self._config_values = None
        self._position = None
        self._default_value_string = None
        self._is_mandatory = None

    @property
    def name(self):
        """
        Gets the name of this NativeShapeField.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this NativeShapeField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NativeShapeField.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this NativeShapeField.
        :type: str
        """
        self._name = name

    @property
    def model_type(self):
        """
        Gets the model_type of this NativeShapeField.
        The model type reference.


        :return: The model_type of this NativeShapeField.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this NativeShapeField.
        The model type reference.


        :param model_type: The model_type of this NativeShapeField.
        :type: str
        """
        self._model_type = model_type

    @property
    def type(self):
        """
        Gets the type of this NativeShapeField.
        The type reference.


        :return: The type of this NativeShapeField.
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this NativeShapeField.
        The type reference.


        :param type: The type of this NativeShapeField.
        :type: object
        """
        self._type = type

    @property
    def config_values(self):
        """
        Gets the config_values of this NativeShapeField.

        :return: The config_values of this NativeShapeField.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this NativeShapeField.

        :param config_values: The config_values of this NativeShapeField.
        :type: oci.data_integration.models.ConfigValues
        """
        self._config_values = config_values

    @property
    def position(self):
        """
        Gets the position of this NativeShapeField.
        The position of the attribute.


        :return: The position of this NativeShapeField.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this NativeShapeField.
        The position of the attribute.


        :param position: The position of this NativeShapeField.
        :type: int
        """
        self._position = position

    @property
    def default_value_string(self):
        """
        Gets the default_value_string of this NativeShapeField.
        The default value.


        :return: The default_value_string of this NativeShapeField.
        :rtype: str
        """
        return self._default_value_string

    @default_value_string.setter
    def default_value_string(self, default_value_string):
        """
        Sets the default_value_string of this NativeShapeField.
        The default value.


        :param default_value_string: The default_value_string of this NativeShapeField.
        :type: str
        """
        self._default_value_string = default_value_string

    @property
    def is_mandatory(self):
        """
        Gets the is_mandatory of this NativeShapeField.
        Specifies whether the field is mandatory.


        :return: The is_mandatory of this NativeShapeField.
        :rtype: bool
        """
        return self._is_mandatory

    @is_mandatory.setter
    def is_mandatory(self, is_mandatory):
        """
        Sets the is_mandatory of this NativeShapeField.
        Specifies whether the field is mandatory.


        :param is_mandatory: The is_mandatory of this NativeShapeField.
        :type: bool
        """
        self._is_mandatory = is_mandatory

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
