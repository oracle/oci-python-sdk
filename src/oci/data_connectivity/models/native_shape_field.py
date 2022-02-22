# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .typed_object import TypedObject
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NativeShapeField(TypedObject):
    """
    The native shape field object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NativeShapeField object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.NativeShapeField.model_type` attribute
        of this class is ``NATIVE_SHAPE_FIELD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this NativeShapeField.
            Allowed values for this property are: "SHAPE", "SHAPE_FIELD", "NATIVE_SHAPE_FIELD"
        :type model_type: str

        :param key:
            The value to assign to the key property of this NativeShapeField.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this NativeShapeField.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this NativeShapeField.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param config_values:
            The value to assign to the config_values property of this NativeShapeField.
        :type config_values: oci.data_connectivity.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this NativeShapeField.
        :type object_status: int

        :param name:
            The value to assign to the name property of this NativeShapeField.
        :type name: str

        :param description:
            The value to assign to the description property of this NativeShapeField.
        :type description: str

        :param type:
            The value to assign to the type property of this NativeShapeField.
        :type type: object

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
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'config_values': 'ConfigValues',
            'object_status': 'int',
            'name': 'str',
            'description': 'str',
            'type': 'object',
            'position': 'int',
            'default_value_string': 'str',
            'is_mandatory': 'bool'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'config_values': 'configValues',
            'object_status': 'objectStatus',
            'name': 'name',
            'description': 'description',
            'type': 'type',
            'position': 'position',
            'default_value_string': 'defaultValueString',
            'is_mandatory': 'isMandatory'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._config_values = None
        self._object_status = None
        self._name = None
        self._description = None
        self._type = None
        self._position = None
        self._default_value_string = None
        self._is_mandatory = None
        self._model_type = 'NATIVE_SHAPE_FIELD'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this NativeShapeField.
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
