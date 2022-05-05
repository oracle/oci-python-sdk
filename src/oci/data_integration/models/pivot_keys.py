# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PivotKeys(object):
    """
    The type representing the pivot key and pivot value details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PivotKeys object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param pivot_axis:
            The value to assign to the pivot_axis property of this PivotKeys.
        :type pivot_axis: list[str]

        :param pivot_key_value_map:
            The value to assign to the pivot_key_value_map property of this PivotKeys.
        :type pivot_key_value_map: dict(str, list[str])

        :param key:
            The value to assign to the key property of this PivotKeys.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this PivotKeys.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this PivotKeys.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this PivotKeys.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param object_status:
            The value to assign to the object_status property of this PivotKeys.
        :type object_status: int

        """
        self.swagger_types = {
            'pivot_axis': 'list[str]',
            'pivot_key_value_map': 'dict(str, list[str])',
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'object_status': 'int'
        }

        self.attribute_map = {
            'pivot_axis': 'pivotAxis',
            'pivot_key_value_map': 'pivotKeyValueMap',
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'object_status': 'objectStatus'
        }

        self._pivot_axis = None
        self._pivot_key_value_map = None
        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._object_status = None

    @property
    def pivot_axis(self):
        """
        Gets the pivot_axis of this PivotKeys.
        The pivot axis is the point around which the table will be rotated, and the pivot values will be transposed into columns in the output table.


        :return: The pivot_axis of this PivotKeys.
        :rtype: list[str]
        """
        return self._pivot_axis

    @pivot_axis.setter
    def pivot_axis(self, pivot_axis):
        """
        Sets the pivot_axis of this PivotKeys.
        The pivot axis is the point around which the table will be rotated, and the pivot values will be transposed into columns in the output table.


        :param pivot_axis: The pivot_axis of this PivotKeys.
        :type: list[str]
        """
        self._pivot_axis = pivot_axis

    @property
    def pivot_key_value_map(self):
        """
        Gets the pivot_key_value_map of this PivotKeys.
        Map of alias to pivot key values.


        :return: The pivot_key_value_map of this PivotKeys.
        :rtype: dict(str, list[str])
        """
        return self._pivot_key_value_map

    @pivot_key_value_map.setter
    def pivot_key_value_map(self, pivot_key_value_map):
        """
        Sets the pivot_key_value_map of this PivotKeys.
        Map of alias to pivot key values.


        :param pivot_key_value_map: The pivot_key_value_map of this PivotKeys.
        :type: dict(str, list[str])
        """
        self._pivot_key_value_map = pivot_key_value_map

    @property
    def key(self):
        """
        Gets the key of this PivotKeys.
        The key of the object.


        :return: The key of this PivotKeys.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this PivotKeys.
        The key of the object.


        :param key: The key of this PivotKeys.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this PivotKeys.
        The type of the object.


        :return: The model_type of this PivotKeys.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this PivotKeys.
        The type of the object.


        :param model_type: The model_type of this PivotKeys.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this PivotKeys.
        The model version of an object.


        :return: The model_version of this PivotKeys.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this PivotKeys.
        The model version of an object.


        :param model_version: The model_version of this PivotKeys.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this PivotKeys.

        :return: The parent_ref of this PivotKeys.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this PivotKeys.

        :param parent_ref: The parent_ref of this PivotKeys.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def object_status(self):
        """
        Gets the object_status of this PivotKeys.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this PivotKeys.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this PivotKeys.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this PivotKeys.
        :type: int
        """
        self._object_status = object_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
