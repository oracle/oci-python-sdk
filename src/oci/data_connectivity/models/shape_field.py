# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .typed_object import TypedObject
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapeField(TypedObject):
    """
    The shape field object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ShapeField object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.ShapeField.model_type` attribute
        of this class is ``SHAPE_FIELD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ShapeField.
            Allowed values for this property are: "SHAPE", "SHAPE_FIELD", "NATIVE_SHAPE_FIELD"
        :type model_type: str

        :param key:
            The value to assign to the key property of this ShapeField.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this ShapeField.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ShapeField.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param config_values:
            The value to assign to the config_values property of this ShapeField.
        :type config_values: oci.data_connectivity.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this ShapeField.
        :type object_status: int

        :param name:
            The value to assign to the name property of this ShapeField.
        :type name: str

        :param description:
            The value to assign to the description property of this ShapeField.
        :type description: str

        :param type:
            The value to assign to the type property of this ShapeField.
        :type type: object

        :param labels:
            The value to assign to the labels property of this ShapeField.
        :type labels: list[str]

        :param native_shape_field:
            The value to assign to the native_shape_field property of this ShapeField.
        :type native_shape_field: oci.data_connectivity.models.NativeShapeField

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
            'labels': 'list[str]',
            'native_shape_field': 'NativeShapeField'
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
            'labels': 'labels',
            'native_shape_field': 'nativeShapeField'
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
        self._labels = None
        self._native_shape_field = None
        self._model_type = 'SHAPE_FIELD'

    @property
    def type(self):
        """
        Gets the type of this ShapeField.
        The type reference.


        :return: The type of this ShapeField.
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ShapeField.
        The type reference.


        :param type: The type of this ShapeField.
        :type: object
        """
        self._type = type

    @property
    def labels(self):
        """
        Gets the labels of this ShapeField.
        Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them to categorize content.


        :return: The labels of this ShapeField.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this ShapeField.
        Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them to categorize content.


        :param labels: The labels of this ShapeField.
        :type: list[str]
        """
        self._labels = labels

    @property
    def native_shape_field(self):
        """
        Gets the native_shape_field of this ShapeField.

        :return: The native_shape_field of this ShapeField.
        :rtype: oci.data_connectivity.models.NativeShapeField
        """
        return self._native_shape_field

    @native_shape_field.setter
    def native_shape_field(self, native_shape_field):
        """
        Sets the native_shape_field of this ShapeField.

        :param native_shape_field: The native_shape_field of this ShapeField.
        :type: oci.data_connectivity.models.NativeShapeField
        """
        self._native_shape_field = native_shape_field

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
