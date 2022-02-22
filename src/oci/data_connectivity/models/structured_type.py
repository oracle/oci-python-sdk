# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .base_type import BaseType
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StructuredType(BaseType):
    """
    A `StructuredType` object represents a data type that exists in a physical data asset object such as a table column, but is more complex. For example, an Oracle database `OBJECT` type. It can be composed of multiple `DataType` objects.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StructuredType object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.StructuredType.model_type` attribute
        of this class is ``STRUCTURED_TYPE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this StructuredType.
            Allowed values for this property are: "STRUCTURED_TYPE", "DATA_TYPE", "CONFIGURED_TYPE", "COMPOSITE_TYPE", "DERIVED_TYPE"
        :type model_type: str

        :param key:
            The value to assign to the key property of this StructuredType.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this StructuredType.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this StructuredType.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this StructuredType.
        :type name: str

        :param object_status:
            The value to assign to the object_status property of this StructuredType.
        :type object_status: int

        :param description:
            The value to assign to the description property of this StructuredType.
        :type description: str

        :param schema:
            The value to assign to the schema property of this StructuredType.
        :type schema: oci.data_connectivity.models.BaseType

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'object_status': 'int',
            'description': 'str',
            'schema': 'BaseType'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'object_status': 'objectStatus',
            'description': 'description',
            'schema': 'schema'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._object_status = None
        self._description = None
        self._schema = None
        self._model_type = 'STRUCTURED_TYPE'

    @property
    def schema(self):
        """
        Gets the schema of this StructuredType.

        :return: The schema of this StructuredType.
        :rtype: oci.data_connectivity.models.BaseType
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this StructuredType.

        :param schema: The schema of this StructuredType.
        :type: oci.data_connectivity.models.BaseType
        """
        self._schema = schema

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
