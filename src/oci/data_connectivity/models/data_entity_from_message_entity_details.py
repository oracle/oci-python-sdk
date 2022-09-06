# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_entity_details import DataEntityDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataEntityFromMessageEntityDetails(DataEntityDetails):
    """
    The message data entity details.
    """

    #: A constant which can be used with the entity_type property of a DataEntityFromMessageEntityDetails.
    #: This constant has a value of "TABLE"
    ENTITY_TYPE_TABLE = "TABLE"

    #: A constant which can be used with the entity_type property of a DataEntityFromMessageEntityDetails.
    #: This constant has a value of "VIEW"
    ENTITY_TYPE_VIEW = "VIEW"

    #: A constant which can be used with the entity_type property of a DataEntityFromMessageEntityDetails.
    #: This constant has a value of "FILE"
    ENTITY_TYPE_FILE = "FILE"

    #: A constant which can be used with the entity_type property of a DataEntityFromMessageEntityDetails.
    #: This constant has a value of "SQL"
    ENTITY_TYPE_SQL = "SQL"

    #: A constant which can be used with the entity_type property of a DataEntityFromMessageEntityDetails.
    #: This constant has a value of "DATA_STORE"
    ENTITY_TYPE_DATA_STORE = "DATA_STORE"

    #: A constant which can be used with the entity_type property of a DataEntityFromMessageEntityDetails.
    #: This constant has a value of "MESSAGE"
    ENTITY_TYPE_MESSAGE = "MESSAGE"

    def __init__(self, **kwargs):
        """
        Initializes a new DataEntityFromMessageEntityDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_connectivity.models.DataEntityFromMessageEntityDetails.model_type` attribute
        of this class is ``MESSAGE_ENTITY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataEntityFromMessageEntityDetails.
            Allowed values for this property are: "VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "DATA_STORE_ENTITY", "SQL_ENTITY", "DERIVED_ENTITY", "MESSAGE_ENTITY"
        :type model_type: str

        :param key:
            The value to assign to the key property of this DataEntityFromMessageEntityDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DataEntityFromMessageEntityDetails.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this DataEntityFromMessageEntityDetails.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this DataEntityFromMessageEntityDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this DataEntityFromMessageEntityDetails.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this DataEntityFromMessageEntityDetails.
        :type object_version: int

        :param external_key:
            The value to assign to the external_key property of this DataEntityFromMessageEntityDetails.
        :type external_key: str

        :param shape:
            The value to assign to the shape property of this DataEntityFromMessageEntityDetails.
        :type shape: oci.data_connectivity.models.Shape

        :param shape_id:
            The value to assign to the shape_id property of this DataEntityFromMessageEntityDetails.
        :type shape_id: str

        :param entity_type:
            The value to assign to the entity_type property of this DataEntityFromMessageEntityDetails.
            Allowed values for this property are: "TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"
        :type entity_type: str

        :param other_type_label:
            The value to assign to the other_type_label property of this DataEntityFromMessageEntityDetails.
        :type other_type_label: str

        :param unique_keys:
            The value to assign to the unique_keys property of this DataEntityFromMessageEntityDetails.
        :type unique_keys: list[oci.data_connectivity.models.UniqueKey]

        :param foreign_keys:
            The value to assign to the foreign_keys property of this DataEntityFromMessageEntityDetails.
        :type foreign_keys: list[oci.data_connectivity.models.ForeignKey]

        :param resource_name:
            The value to assign to the resource_name property of this DataEntityFromMessageEntityDetails.
        :type resource_name: str

        :param data_format:
            The value to assign to the data_format property of this DataEntityFromMessageEntityDetails.
        :type data_format: oci.data_connectivity.models.DataFormat

        :param object_status:
            The value to assign to the object_status property of this DataEntityFromMessageEntityDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this DataEntityFromMessageEntityDetails.
        :type identifier: str

        """
        self.swagger_types = {
            'model_type': 'str',
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
            'data_format': 'DataFormat',
            'object_status': 'int',
            'identifier': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
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
            'data_format': 'dataFormat',
            'object_status': 'objectStatus',
            'identifier': 'identifier'
        }

        self._model_type = None
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
        self._data_format = None
        self._object_status = None
        self._identifier = None
        self._model_type = 'MESSAGE_ENTITY'

    @property
    def key(self):
        """
        Gets the key of this DataEntityFromMessageEntityDetails.
        The object key.


        :return: The key of this DataEntityFromMessageEntityDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DataEntityFromMessageEntityDetails.
        The object key.


        :param key: The key of this DataEntityFromMessageEntityDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this DataEntityFromMessageEntityDetails.
        The model version of the object.


        :return: The model_version of this DataEntityFromMessageEntityDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this DataEntityFromMessageEntityDetails.
        The model version of the object.


        :param model_version: The model_version of this DataEntityFromMessageEntityDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this DataEntityFromMessageEntityDetails.

        :return: The parent_ref of this DataEntityFromMessageEntityDetails.
        :rtype: oci.data_connectivity.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this DataEntityFromMessageEntityDetails.

        :param parent_ref: The parent_ref of this DataEntityFromMessageEntityDetails.
        :type: oci.data_connectivity.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DataEntityFromMessageEntityDetails.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is unique, editable and is restricted to 1000 characters.


        :return: The name of this DataEntityFromMessageEntityDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DataEntityFromMessageEntityDetails.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is unique, editable and is restricted to 1000 characters.


        :param name: The name of this DataEntityFromMessageEntityDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DataEntityFromMessageEntityDetails.
        Detailed description of the object.


        :return: The description of this DataEntityFromMessageEntityDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataEntityFromMessageEntityDetails.
        Detailed description of the object.


        :param description: The description of this DataEntityFromMessageEntityDetails.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this DataEntityFromMessageEntityDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this DataEntityFromMessageEntityDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this DataEntityFromMessageEntityDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this DataEntityFromMessageEntityDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def external_key(self):
        """
        Gets the external_key of this DataEntityFromMessageEntityDetails.
        The external key of the object.


        :return: The external_key of this DataEntityFromMessageEntityDetails.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this DataEntityFromMessageEntityDetails.
        The external key of the object.


        :param external_key: The external_key of this DataEntityFromMessageEntityDetails.
        :type: str
        """
        self._external_key = external_key

    @property
    def shape(self):
        """
        Gets the shape of this DataEntityFromMessageEntityDetails.

        :return: The shape of this DataEntityFromMessageEntityDetails.
        :rtype: oci.data_connectivity.models.Shape
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this DataEntityFromMessageEntityDetails.

        :param shape: The shape of this DataEntityFromMessageEntityDetails.
        :type: oci.data_connectivity.models.Shape
        """
        self._shape = shape

    @property
    def shape_id(self):
        """
        Gets the shape_id of this DataEntityFromMessageEntityDetails.
        The shape ID.


        :return: The shape_id of this DataEntityFromMessageEntityDetails.
        :rtype: str
        """
        return self._shape_id

    @shape_id.setter
    def shape_id(self, shape_id):
        """
        Sets the shape_id of this DataEntityFromMessageEntityDetails.
        The shape ID.


        :param shape_id: The shape_id of this DataEntityFromMessageEntityDetails.
        :type: str
        """
        self._shape_id = shape_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this DataEntityFromMessageEntityDetails.
        The entity type.

        Allowed values for this property are: "TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"


        :return: The entity_type of this DataEntityFromMessageEntityDetails.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this DataEntityFromMessageEntityDetails.
        The entity type.


        :param entity_type: The entity_type of this DataEntityFromMessageEntityDetails.
        :type: str
        """
        allowed_values = ["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE", "MESSAGE"]
        if not value_allowed_none_or_none_sentinel(entity_type, allowed_values):
            raise ValueError(
                "Invalid value for `entity_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._entity_type = entity_type

    @property
    def other_type_label(self):
        """
        Gets the other_type_label of this DataEntityFromMessageEntityDetails.
        Specifies other type label.


        :return: The other_type_label of this DataEntityFromMessageEntityDetails.
        :rtype: str
        """
        return self._other_type_label

    @other_type_label.setter
    def other_type_label(self, other_type_label):
        """
        Sets the other_type_label of this DataEntityFromMessageEntityDetails.
        Specifies other type label.


        :param other_type_label: The other_type_label of this DataEntityFromMessageEntityDetails.
        :type: str
        """
        self._other_type_label = other_type_label

    @property
    def unique_keys(self):
        """
        Gets the unique_keys of this DataEntityFromMessageEntityDetails.
        An array of unique keys.


        :return: The unique_keys of this DataEntityFromMessageEntityDetails.
        :rtype: list[oci.data_connectivity.models.UniqueKey]
        """
        return self._unique_keys

    @unique_keys.setter
    def unique_keys(self, unique_keys):
        """
        Sets the unique_keys of this DataEntityFromMessageEntityDetails.
        An array of unique keys.


        :param unique_keys: The unique_keys of this DataEntityFromMessageEntityDetails.
        :type: list[oci.data_connectivity.models.UniqueKey]
        """
        self._unique_keys = unique_keys

    @property
    def foreign_keys(self):
        """
        Gets the foreign_keys of this DataEntityFromMessageEntityDetails.
        An array of foreign keys.


        :return: The foreign_keys of this DataEntityFromMessageEntityDetails.
        :rtype: list[oci.data_connectivity.models.ForeignKey]
        """
        return self._foreign_keys

    @foreign_keys.setter
    def foreign_keys(self, foreign_keys):
        """
        Sets the foreign_keys of this DataEntityFromMessageEntityDetails.
        An array of foreign keys.


        :param foreign_keys: The foreign_keys of this DataEntityFromMessageEntityDetails.
        :type: list[oci.data_connectivity.models.ForeignKey]
        """
        self._foreign_keys = foreign_keys

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this DataEntityFromMessageEntityDetails.
        The resource name.


        :return: The resource_name of this DataEntityFromMessageEntityDetails.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this DataEntityFromMessageEntityDetails.
        The resource name.


        :param resource_name: The resource_name of this DataEntityFromMessageEntityDetails.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def data_format(self):
        """
        Gets the data_format of this DataEntityFromMessageEntityDetails.

        :return: The data_format of this DataEntityFromMessageEntityDetails.
        :rtype: oci.data_connectivity.models.DataFormat
        """
        return self._data_format

    @data_format.setter
    def data_format(self, data_format):
        """
        Sets the data_format of this DataEntityFromMessageEntityDetails.

        :param data_format: The data_format of this DataEntityFromMessageEntityDetails.
        :type: oci.data_connectivity.models.DataFormat
        """
        self._data_format = data_format

    @property
    def object_status(self):
        """
        Gets the object_status of this DataEntityFromMessageEntityDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this DataEntityFromMessageEntityDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this DataEntityFromMessageEntityDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this DataEntityFromMessageEntityDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this DataEntityFromMessageEntityDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.


        :return: The identifier of this DataEntityFromMessageEntityDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this DataEntityFromMessageEntityDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this DataEntityFromMessageEntityDetails.
        :type: str
        """
        self._identifier = identifier

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
