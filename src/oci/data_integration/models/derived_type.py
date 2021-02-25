# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .base_type import BaseType
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DerivedType(BaseType):
    """
    A `DerivedType` object represents a more complex type that is derived from a set of simple types, for example an `Address` or `SSN` data type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DerivedType object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.DerivedType.model_type` attribute
        of this class is ``DERIVED_TYPE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DerivedType.
            Allowed values for this property are: "DYNAMIC_TYPE", "STRUCTURED_TYPE", "DATA_TYPE", "JAVA_TYPE", "CONFIGURED_TYPE", "COMPOSITE_TYPE", "DERIVED_TYPE"
        :type model_type: str

        :param key:
            The value to assign to the key property of this DerivedType.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DerivedType.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this DerivedType.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this DerivedType.
        :type name: str

        :param object_status:
            The value to assign to the object_status property of this DerivedType.
        :type object_status: int

        :param description:
            The value to assign to the description property of this DerivedType.
        :type description: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'object_status': 'int',
            'description': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'object_status': 'objectStatus',
            'description': 'description'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._object_status = None
        self._description = None
        self._model_type = 'DERIVED_TYPE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
