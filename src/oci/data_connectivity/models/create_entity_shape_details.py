# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEntityShapeDetails(object):
    """
    The data entity shape object.
    """

    #: A constant which can be used with the model_type property of a CreateEntityShapeDetails.
    #: This constant has a value of "VIEW_ENTITY"
    MODEL_TYPE_VIEW_ENTITY = "VIEW_ENTITY"

    #: A constant which can be used with the model_type property of a CreateEntityShapeDetails.
    #: This constant has a value of "TABLE_ENTITY"
    MODEL_TYPE_TABLE_ENTITY = "TABLE_ENTITY"

    #: A constant which can be used with the model_type property of a CreateEntityShapeDetails.
    #: This constant has a value of "FILE_ENTITY"
    MODEL_TYPE_FILE_ENTITY = "FILE_ENTITY"

    #: A constant which can be used with the model_type property of a CreateEntityShapeDetails.
    #: This constant has a value of "DATA_STORE_ENTITY"
    MODEL_TYPE_DATA_STORE_ENTITY = "DATA_STORE_ENTITY"

    #: A constant which can be used with the model_type property of a CreateEntityShapeDetails.
    #: This constant has a value of "SQL_ENTITY"
    MODEL_TYPE_SQL_ENTITY = "SQL_ENTITY"

    #: A constant which can be used with the entity_type property of a CreateEntityShapeDetails.
    #: This constant has a value of "TABLE"
    ENTITY_TYPE_TABLE = "TABLE"

    #: A constant which can be used with the entity_type property of a CreateEntityShapeDetails.
    #: This constant has a value of "VIEW"
    ENTITY_TYPE_VIEW = "VIEW"

    #: A constant which can be used with the entity_type property of a CreateEntityShapeDetails.
    #: This constant has a value of "FILE"
    ENTITY_TYPE_FILE = "FILE"

    #: A constant which can be used with the entity_type property of a CreateEntityShapeDetails.
    #: This constant has a value of "SQL"
    ENTITY_TYPE_SQL = "SQL"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEntityShapeDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_connectivity.models.CreateEntityShapeFromDataStore`
        * :class:`~oci.data_connectivity.models.CreateEntityShapeFromTable`
        * :class:`~oci.data_connectivity.models.CreateEntityShapeFromSQL`
        * :class:`~oci.data_connectivity.models.CreateEntityShapeFromFile`
        * :class:`~oci.data_connectivity.models.CreateEntityShapeFromView`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateEntityShapeDetails.
            Allowed values for this property are: "VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "DATA_STORE_ENTITY", "SQL_ENTITY"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateEntityShapeDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateEntityShapeDetails.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateEntityShapeDetails.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateEntityShapeDetails.
        :type name: str

        :param object_version:
            The value to assign to the object_version property of this CreateEntityShapeDetails.
        :type object_version: int

        :param external_key:
            The value to assign to the external_key property of this CreateEntityShapeDetails.
        :type external_key: str

        :param shape:
            The value to assign to the shape property of this CreateEntityShapeDetails.
        :type shape: oci.data_connectivity.models.Shape

        :param shape_id:
            The value to assign to the shape_id property of this CreateEntityShapeDetails.
        :type shape_id: str

        :param entity_type:
            The value to assign to the entity_type property of this CreateEntityShapeDetails.
            Allowed values for this property are: "TABLE", "VIEW", "FILE", "SQL"
        :type entity_type: str

        :param other_type_label:
            The value to assign to the other_type_label property of this CreateEntityShapeDetails.
        :type other_type_label: str

        :param unique_keys:
            The value to assign to the unique_keys property of this CreateEntityShapeDetails.
        :type unique_keys: list[oci.data_connectivity.models.UniqueKey]

        :param foreign_keys:
            The value to assign to the foreign_keys property of this CreateEntityShapeDetails.
        :type foreign_keys: list[oci.data_connectivity.models.ForeignKey]

        :param resource_name:
            The value to assign to the resource_name property of this CreateEntityShapeDetails.
        :type resource_name: str

        :param object_status:
            The value to assign to the object_status property of this CreateEntityShapeDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateEntityShapeDetails.
        :type identifier: str

        :param types:
            The value to assign to the types property of this CreateEntityShapeDetails.
        :type types: oci.data_connectivity.models.TypeLibrary

        :param entity_properties:
            The value to assign to the entity_properties property of this CreateEntityShapeDetails.
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

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'DATA_STORE_ENTITY':
            return 'CreateEntityShapeFromDataStore'

        if type == 'TABLE_ENTITY':
            return 'CreateEntityShapeFromTable'

        if type == 'SQL_ENTITY':
            return 'CreateEntityShapeFromSQL'

        if type == 'FILE_ENTITY':
            return 'CreateEntityShapeFromFile'

        if type == 'VIEW_ENTITY':
            return 'CreateEntityShapeFromView'
        else:
            return 'CreateEntityShapeDetails'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this CreateEntityShapeDetails.
        The data entity type.

        Allowed values for this property are: "VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "DATA_STORE_ENTITY", "SQL_ENTITY"


        :return: The model_type of this CreateEntityShapeDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateEntityShapeDetails.
        The data entity type.


        :param model_type: The model_type of this CreateEntityShapeDetails.
        :type: str
        """
        allowed_values = ["VIEW_ENTITY", "TABLE_ENTITY", "FILE_ENTITY", "DATA_STORE_ENTITY", "SQL_ENTITY"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            raise ValueError(
                "Invalid value for `model_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this CreateEntityShapeDetails.
        The object key.


        :return: The key of this CreateEntityShapeDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateEntityShapeDetails.
        The object key.


        :param key: The key of this CreateEntityShapeDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateEntityShapeDetails.
        The object's model version.


        :return: The model_version of this CreateEntityShapeDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateEntityShapeDetails.
        The object's model version.


        :param model_version: The model_version of this CreateEntityShapeDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this CreateEntityShapeDetails.

        :return: The parent_ref of this CreateEntityShapeDetails.
        :rtype: oci.data_connectivity.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this CreateEntityShapeDetails.

        :param parent_ref: The parent_ref of this CreateEntityShapeDetails.
        :type: oci.data_connectivity.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateEntityShapeDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this CreateEntityShapeDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateEntityShapeDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this CreateEntityShapeDetails.
        :type: str
        """
        self._name = name

    @property
    def object_version(self):
        """
        Gets the object_version of this CreateEntityShapeDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this CreateEntityShapeDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this CreateEntityShapeDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this CreateEntityShapeDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def external_key(self):
        """
        Gets the external_key of this CreateEntityShapeDetails.
        The external key for the object.


        :return: The external_key of this CreateEntityShapeDetails.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this CreateEntityShapeDetails.
        The external key for the object.


        :param external_key: The external_key of this CreateEntityShapeDetails.
        :type: str
        """
        self._external_key = external_key

    @property
    def shape(self):
        """
        Gets the shape of this CreateEntityShapeDetails.

        :return: The shape of this CreateEntityShapeDetails.
        :rtype: oci.data_connectivity.models.Shape
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CreateEntityShapeDetails.

        :param shape: The shape of this CreateEntityShapeDetails.
        :type: oci.data_connectivity.models.Shape
        """
        self._shape = shape

    @property
    def shape_id(self):
        """
        Gets the shape_id of this CreateEntityShapeDetails.
        The shape ID.


        :return: The shape_id of this CreateEntityShapeDetails.
        :rtype: str
        """
        return self._shape_id

    @shape_id.setter
    def shape_id(self, shape_id):
        """
        Sets the shape_id of this CreateEntityShapeDetails.
        The shape ID.


        :param shape_id: The shape_id of this CreateEntityShapeDetails.
        :type: str
        """
        self._shape_id = shape_id

    @property
    def entity_type(self):
        """
        Gets the entity_type of this CreateEntityShapeDetails.
        The entity type.

        Allowed values for this property are: "TABLE", "VIEW", "FILE", "SQL"


        :return: The entity_type of this CreateEntityShapeDetails.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this CreateEntityShapeDetails.
        The entity type.


        :param entity_type: The entity_type of this CreateEntityShapeDetails.
        :type: str
        """
        allowed_values = ["TABLE", "VIEW", "FILE", "SQL"]
        if not value_allowed_none_or_none_sentinel(entity_type, allowed_values):
            raise ValueError(
                "Invalid value for `entity_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._entity_type = entity_type

    @property
    def other_type_label(self):
        """
        Gets the other_type_label of this CreateEntityShapeDetails.
        Specifies other type label.


        :return: The other_type_label of this CreateEntityShapeDetails.
        :rtype: str
        """
        return self._other_type_label

    @other_type_label.setter
    def other_type_label(self, other_type_label):
        """
        Sets the other_type_label of this CreateEntityShapeDetails.
        Specifies other type label.


        :param other_type_label: The other_type_label of this CreateEntityShapeDetails.
        :type: str
        """
        self._other_type_label = other_type_label

    @property
    def unique_keys(self):
        """
        Gets the unique_keys of this CreateEntityShapeDetails.
        An array of unique keys.


        :return: The unique_keys of this CreateEntityShapeDetails.
        :rtype: list[oci.data_connectivity.models.UniqueKey]
        """
        return self._unique_keys

    @unique_keys.setter
    def unique_keys(self, unique_keys):
        """
        Sets the unique_keys of this CreateEntityShapeDetails.
        An array of unique keys.


        :param unique_keys: The unique_keys of this CreateEntityShapeDetails.
        :type: list[oci.data_connectivity.models.UniqueKey]
        """
        self._unique_keys = unique_keys

    @property
    def foreign_keys(self):
        """
        Gets the foreign_keys of this CreateEntityShapeDetails.
        An array of foreign keys.


        :return: The foreign_keys of this CreateEntityShapeDetails.
        :rtype: list[oci.data_connectivity.models.ForeignKey]
        """
        return self._foreign_keys

    @foreign_keys.setter
    def foreign_keys(self, foreign_keys):
        """
        Sets the foreign_keys of this CreateEntityShapeDetails.
        An array of foreign keys.


        :param foreign_keys: The foreign_keys of this CreateEntityShapeDetails.
        :type: list[oci.data_connectivity.models.ForeignKey]
        """
        self._foreign_keys = foreign_keys

    @property
    def resource_name(self):
        """
        Gets the resource_name of this CreateEntityShapeDetails.
        The resource name.


        :return: The resource_name of this CreateEntityShapeDetails.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this CreateEntityShapeDetails.
        The resource name.


        :param resource_name: The resource_name of this CreateEntityShapeDetails.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def object_status(self):
        """
        Gets the object_status of this CreateEntityShapeDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CreateEntityShapeDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CreateEntityShapeDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CreateEntityShapeDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this CreateEntityShapeDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this CreateEntityShapeDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreateEntityShapeDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this CreateEntityShapeDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def types(self):
        """
        Gets the types of this CreateEntityShapeDetails.

        :return: The types of this CreateEntityShapeDetails.
        :rtype: oci.data_connectivity.models.TypeLibrary
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this CreateEntityShapeDetails.

        :param types: The types of this CreateEntityShapeDetails.
        :type: oci.data_connectivity.models.TypeLibrary
        """
        self._types = types

    @property
    def entity_properties(self):
        """
        Gets the entity_properties of this CreateEntityShapeDetails.
        Map<String, String> for entity properties


        :return: The entity_properties of this CreateEntityShapeDetails.
        :rtype: dict(str, str)
        """
        return self._entity_properties

    @entity_properties.setter
    def entity_properties(self, entity_properties):
        """
        Sets the entity_properties of this CreateEntityShapeDetails.
        Map<String, String> for entity properties


        :param entity_properties: The entity_properties of this CreateEntityShapeDetails.
        :type: dict(str, str)
        """
        self._entity_properties = entity_properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
