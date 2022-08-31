# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_entity_shape_details import CreateEntityShapeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEntityShapeFromTable(CreateEntityShapeDetails):
    """
    The table data entity details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEntityShapeFromTable object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.CreateEntityShapeFromTable.model_type` attribute
        of this class is ``TABLE_ENTITY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateEntityShapeFromTable.
            Allowed values for this property are: "VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "DATA_STORE_ENTITY", "SQL_ENTITY", "MESSAGE_ENTITY"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateEntityShapeFromTable.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateEntityShapeFromTable.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateEntityShapeFromTable.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateEntityShapeFromTable.
        :type name: str

        :param object_version:
            The value to assign to the object_version property of this CreateEntityShapeFromTable.
        :type object_version: int

        :param external_key:
            The value to assign to the external_key property of this CreateEntityShapeFromTable.
        :type external_key: str

        :param shape:
            The value to assign to the shape property of this CreateEntityShapeFromTable.
        :type shape: oci.data_connectivity.models.Shape

        :param shape_id:
            The value to assign to the shape_id property of this CreateEntityShapeFromTable.
        :type shape_id: str

        :param entity_type:
            The value to assign to the entity_type property of this CreateEntityShapeFromTable.
            Allowed values for this property are: "TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"
        :type entity_type: str

        :param other_type_label:
            The value to assign to the other_type_label property of this CreateEntityShapeFromTable.
        :type other_type_label: str

        :param unique_keys:
            The value to assign to the unique_keys property of this CreateEntityShapeFromTable.
        :type unique_keys: list[oci.data_connectivity.models.UniqueKey]

        :param foreign_keys:
            The value to assign to the foreign_keys property of this CreateEntityShapeFromTable.
        :type foreign_keys: list[oci.data_connectivity.models.ForeignKey]

        :param resource_name:
            The value to assign to the resource_name property of this CreateEntityShapeFromTable.
        :type resource_name: str

        :param object_status:
            The value to assign to the object_status property of this CreateEntityShapeFromTable.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateEntityShapeFromTable.
        :type identifier: str

        :param types:
            The value to assign to the types property of this CreateEntityShapeFromTable.
        :type types: oci.data_connectivity.models.TypeLibrary

        :param entity_properties:
            The value to assign to the entity_properties property of this CreateEntityShapeFromTable.
        :type entity_properties: dict(str, str)

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'object_version': 'int',
            'external_key': 'str',
            'shape': 'Shape',
            'shape_id': 'str',
            'entity_type': 'str',
            'other_type_label': 'str',
            'unique_keys': 'list[UniqueKey]',
            'foreign_keys': 'list[ForeignKey]',
            'resource_name': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'types': 'TypeLibrary',
            'entity_properties': 'dict(str, str)'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'object_version': 'objectVersion',
            'external_key': 'externalKey',
            'shape': 'shape',
            'shape_id': 'shapeId',
            'entity_type': 'entityType',
            'other_type_label': 'otherTypeLabel',
            'unique_keys': 'uniqueKeys',
            'foreign_keys': 'foreignKeys',
            'resource_name': 'resourceName',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'types': 'types',
            'entity_properties': 'entityProperties'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._object_version = None
        self._external_key = None
        self._shape = None
        self._shape_id = None
        self._entity_type = None
        self._other_type_label = None
        self._unique_keys = None
        self._foreign_keys = None
        self._resource_name = None
        self._object_status = None
        self._identifier = None
        self._types = None
        self._entity_properties = None
        self._model_type = 'TABLE_ENTITY'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
