# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_entity import DataEntity
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataEntityFromSql(DataEntity):
    """
    The sql entity data entity details.
    """

    #: A constant which can be used with the entity_type property of a DataEntityFromSql.
    #: This constant has a value of "TABLE"
    ENTITY_TYPE_TABLE = "TABLE"

    #: A constant which can be used with the entity_type property of a DataEntityFromSql.
    #: This constant has a value of "VIEW"
    ENTITY_TYPE_VIEW = "VIEW"

    #: A constant which can be used with the entity_type property of a DataEntityFromSql.
    #: This constant has a value of "FILE"
    ENTITY_TYPE_FILE = "FILE"

    #: A constant which can be used with the entity_type property of a DataEntityFromSql.
    #: This constant has a value of "SQL"
    ENTITY_TYPE_SQL = "SQL"

    def __init__(self, **kwargs):
        """
        Initializes a new DataEntityFromSql object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.DataEntityFromSql.model_type` attribute
        of this class is ``SQL_ENTITY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataEntityFromSql.
            Allowed values for this property are: "VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "SQL_ENTITY", "DATA_STORE_ENTITY", "DERIVED_ENTITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param metadata:
            The value to assign to the metadata property of this DataEntityFromSql.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key:
            The value to assign to the key property of this DataEntityFromSql.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DataEntityFromSql.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this DataEntityFromSql.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this DataEntityFromSql.
        :type name: str

        :param description:
            The value to assign to the description property of this DataEntityFromSql.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this DataEntityFromSql.
        :type object_version: int

        :param external_key:
            The value to assign to the external_key property of this DataEntityFromSql.
        :type external_key: str

        :param shape:
            The value to assign to the shape property of this DataEntityFromSql.
        :type shape: oci.data_integration.models.Shape

        :param shape_id:
            The value to assign to the shape_id property of this DataEntityFromSql.
        :type shape_id: str

        :param entity_type:
            The value to assign to the entity_type property of this DataEntityFromSql.
            Allowed values for this property are: "TABLE", "VIEW", "FILE", "SQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_type: str

        :param other_type_label:
            The value to assign to the other_type_label property of this DataEntityFromSql.
        :type other_type_label: str

        :param unique_keys:
            The value to assign to the unique_keys property of this DataEntityFromSql.
        :type unique_keys: list[oci.data_integration.models.UniqueKey]

        :param foreign_keys:
            The value to assign to the foreign_keys property of this DataEntityFromSql.
        :type foreign_keys: list[oci.data_integration.models.ForeignKey]

        :param resource_name:
            The value to assign to the resource_name property of this DataEntityFromSql.
        :type resource_name: str

        :param object_status:
            The value to assign to the object_status property of this DataEntityFromSql.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DataEntityFromSql.
        :type identifier: str

        :param sql_query:
            The value to assign to the sql_query property of this DataEntityFromSql.
        :type sql_query: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'metadata': 'ObjectMetadata',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
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
            'sql_query': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'metadata': 'metadata',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
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
            'sql_query': 'sqlQuery'
        }

        self._model_type = None
        self._metadata = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
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
        self._sql_query = None
        self._model_type = 'SQL_ENTITY'

    @property
    def key(self):
        """
        Gets the key of this DataEntityFromSql.
        The object key.


        :return: The key of this DataEntityFromSql.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DataEntityFromSql.
        The object key.


        :param key: The key of this DataEntityFromSql.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this DataEntityFromSql.
        The object's model version.


        :return: The model_version of this DataEntityFromSql.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this DataEntityFromSql.
        The object's model version.


        :param model_version: The model_version of this DataEntityFromSql.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this DataEntityFromSql.

        :return: The parent_ref of this DataEntityFromSql.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this DataEntityFromSql.

        :param parent_ref: The parent_ref of this DataEntityFromSql.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this DataEntityFromSql.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this DataEntityFromSql.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DataEntityFromSql.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this DataEntityFromSql.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DataEntityFromSql.
        Detailed description for the object.


        :return: The description of this DataEntityFromSql.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataEntityFromSql.
        Detailed description for the object.


        :param description: The description of this DataEntityFromSql.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this DataEntityFromSql.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this DataEntityFromSql.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this DataEntityFromSql.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this DataEntityFromSql.
        :type: int
        """
        self._object_version = object_version

    @property
    def external_key(self):
        """
        Gets the external_key of this DataEntityFromSql.
        The external key for the object


        :return: The external_key of this DataEntityFromSql.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this DataEntityFromSql.
        The external key for the object


        :param external_key: The external_key of this DataEntityFromSql.
        :type: str
        """
        self._external_key = external_key

    @property
    def shape(self):
        """
        Gets the shape of this DataEntityFromSql.

        :return: The shape of this DataEntityFromSql.
        :rtype: oci.data_integration.models.Shape
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this DataEntityFromSql.

        :param shape: The shape of this DataEntityFromSql.
        :type: oci.data_integration.models.Shape
        """
        self._shape = shape

    @property
    def shape_id(self):
        """
        Gets the shape_id of this DataEntityFromSql.
        The shape ID.


        :return: The shape_id of this DataEntityFromSql.
        :rtype: str
        """
        return self._shape_id

    @shape_id.setter
    def shape_id(self, shape_id):
        """
        Sets the shape_id of this DataEntityFromSql.
        The shape ID.


        :param shape_id: The shape_id of this DataEntityFromSql.
        :type: str
        """
        self._shape_id = shape_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this DataEntityFromSql.
        The entity type.

        Allowed values for this property are: "TABLE", "VIEW", "FILE", "SQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The entity_type of this DataEntityFromSql.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this DataEntityFromSql.
        The entity type.


        :param entity_type: The entity_type of this DataEntityFromSql.
        :type: str
        """
        allowed_values = ["TABLE", "VIEW", "FILE", "SQL"]
        if not value_allowed_none_or_none_sentinel(entity_type, allowed_values):
            entity_type = 'UNKNOWN_ENUM_VALUE'
        self._entity_type = entity_type

    @property
    def other_type_label(self):
        """
        Gets the other_type_label of this DataEntityFromSql.
        Specifies other type label.


        :return: The other_type_label of this DataEntityFromSql.
        :rtype: str
        """
        return self._other_type_label

    @other_type_label.setter
    def other_type_label(self, other_type_label):
        """
        Sets the other_type_label of this DataEntityFromSql.
        Specifies other type label.


        :param other_type_label: The other_type_label of this DataEntityFromSql.
        :type: str
        """
        self._other_type_label = other_type_label

    @property
    def unique_keys(self):
        """
        Gets the unique_keys of this DataEntityFromSql.
        An array of unique keys.


        :return: The unique_keys of this DataEntityFromSql.
        :rtype: list[oci.data_integration.models.UniqueKey]
        """
        return self._unique_keys

    @unique_keys.setter
    def unique_keys(self, unique_keys):
        """
        Sets the unique_keys of this DataEntityFromSql.
        An array of unique keys.


        :param unique_keys: The unique_keys of this DataEntityFromSql.
        :type: list[oci.data_integration.models.UniqueKey]
        """
        self._unique_keys = unique_keys

    @property
    def foreign_keys(self):
        """
        Gets the foreign_keys of this DataEntityFromSql.
        An array of foreign keys.


        :return: The foreign_keys of this DataEntityFromSql.
        :rtype: list[oci.data_integration.models.ForeignKey]
        """
        return self._foreign_keys

    @foreign_keys.setter
    def foreign_keys(self, foreign_keys):
        """
        Sets the foreign_keys of this DataEntityFromSql.
        An array of foreign keys.


        :param foreign_keys: The foreign_keys of this DataEntityFromSql.
        :type: list[oci.data_integration.models.ForeignKey]
        """
        self._foreign_keys = foreign_keys

    @property
    def resource_name(self):
        """
        Gets the resource_name of this DataEntityFromSql.
        The resource name.


        :return: The resource_name of this DataEntityFromSql.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this DataEntityFromSql.
        The resource name.


        :param resource_name: The resource_name of this DataEntityFromSql.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def object_status(self):
        """
        Gets the object_status of this DataEntityFromSql.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this DataEntityFromSql.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this DataEntityFromSql.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this DataEntityFromSql.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this DataEntityFromSql.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this DataEntityFromSql.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this DataEntityFromSql.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this DataEntityFromSql.
        :type: str
        """
        self._identifier = identifier

    @property
    def sql_query(self):
        """
        Gets the sql_query of this DataEntityFromSql.
        sqlQuery


        :return: The sql_query of this DataEntityFromSql.
        :rtype: str
        """
        return self._sql_query

    @sql_query.setter
    def sql_query(self, sql_query):
        """
        Sets the sql_query of this DataEntityFromSql.
        sqlQuery


        :param sql_query: The sql_query of this DataEntityFromSql.
        :type: str
        """
        self._sql_query = sql_query

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
