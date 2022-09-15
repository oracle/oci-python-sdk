# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .base_type import BaseType
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ArrayType(BaseType):
    """
    Array type object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ArrayType object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.ArrayType.model_type` attribute
        of this class is ``ARRAY_TYPE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ArrayType.
            Allowed values for this property are: "DYNAMIC_TYPE", "STRUCTURED_TYPE", "DATA_TYPE", "JAVA_TYPE", "CONFIGURED_TYPE", "COMPOSITE_TYPE", "DERIVED_TYPE", "ARRAY_TYPE", "MAP_TYPE", "MATERIALIZED_COMPOSITE_TYPE"
        :type model_type: str

        :param key:
            The value to assign to the key property of this ArrayType.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this ArrayType.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ArrayType.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this ArrayType.
        :type name: str

        :param object_status:
            The value to assign to the object_status property of this ArrayType.
        :type object_status: int

        :param description:
            The value to assign to the description property of this ArrayType.
        :type description: str

        :param element_type:
            The value to assign to the element_type property of this ArrayType.
        :type element_type: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'object_status': 'int',
            'description': 'str',
            'element_type': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'object_status': 'objectStatus',
            'description': 'description',
            'element_type': 'elementType'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._object_status = None
        self._description = None
        self._element_type = None
        self._model_type = 'ARRAY_TYPE'

    @property
    def element_type(self):
        """
        Gets the element_type of this ArrayType.
        Seeded type


        :return: The element_type of this ArrayType.
        :rtype: str
        """
        return self._element_type

    @element_type.setter
    def element_type(self, element_type):
        """
        Sets the element_type of this ArrayType.
        Seeded type


        :param element_type: The element_type of this ArrayType.
        :type: str
        """
        self._element_type = element_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
