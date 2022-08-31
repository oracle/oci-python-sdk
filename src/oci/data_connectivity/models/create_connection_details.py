# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateConnectionDetails(object):
    """
    Properties used in the create connection operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateConnectionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CreateConnectionDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateConnectionDetails.
        :type model_version: str

        :param model_type:
            The value to assign to the model_type property of this CreateConnectionDetails.
        :type model_type: str

        :param name:
            The value to assign to the name property of this CreateConnectionDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateConnectionDetails.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this CreateConnectionDetails.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this CreateConnectionDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateConnectionDetails.
        :type identifier: str

        :param primary_schema:
            The value to assign to the primary_schema property of this CreateConnectionDetails.
        :type primary_schema: oci.data_connectivity.models.Schema

        :param connection_properties:
            The value to assign to the connection_properties property of this CreateConnectionDetails.
        :type connection_properties: list[oci.data_connectivity.models.ConnectionProperty]

        :param properties:
            The value to assign to the properties property of this CreateConnectionDetails.
        :type properties: dict(str, object)

        :param type:
            The value to assign to the type property of this CreateConnectionDetails.
        :type type: str

        :param is_default:
            The value to assign to the is_default property of this CreateConnectionDetails.
        :type is_default: bool

        :param metadata:
            The value to assign to the metadata property of this CreateConnectionDetails.
        :type metadata: oci.data_connectivity.models.ObjectMetadata

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateConnectionDetails.
        :type registry_metadata: oci.data_connectivity.models.RegistryMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_version': 'str',
            'model_type': 'str',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'primary_schema': 'Schema',
            'connection_properties': 'list[ConnectionProperty]',
            'properties': 'dict(str, object)',
            'type': 'str',
            'is_default': 'bool',
            'metadata': 'ObjectMetadata',
            'registry_metadata': 'RegistryMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_version': 'modelVersion',
            'model_type': 'modelType',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'primary_schema': 'primarySchema',
            'connection_properties': 'connectionProperties',
            'properties': 'properties',
            'type': 'type',
            'is_default': 'isDefault',
            'metadata': 'metadata',
            'registry_metadata': 'registryMetadata'
        }

        self._key = None
        self._model_version = None
        self._model_type = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._primary_schema = None
        self._connection_properties = None
        self._properties = None
        self._type = None
        self._is_default = None
        self._metadata = None
        self._registry_metadata = None

    @property
    def key(self):
        """
        Gets the key of this CreateConnectionDetails.
        Generated key that can be used in API calls to identify the connection. In scenarios where reference to the connection is required, a value can be passed in create.


        :return: The key of this CreateConnectionDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateConnectionDetails.
        Generated key that can be used in API calls to identify the connection. In scenarios where reference to the connection is required, a value can be passed in create.


        :param key: The key of this CreateConnectionDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateConnectionDetails.
        The model version of an object.


        :return: The model_version of this CreateConnectionDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateConnectionDetails.
        The model version of an object.


        :param model_version: The model_version of this CreateConnectionDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def model_type(self):
        """
        Gets the model_type of this CreateConnectionDetails.
        The type of the object.


        :return: The model_type of this CreateConnectionDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateConnectionDetails.
        The type of the object.


        :param model_type: The model_type of this CreateConnectionDetails.
        :type: str
        """
        self._model_type = model_type

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateConnectionDetails.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this CreateConnectionDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateConnectionDetails.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this CreateConnectionDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateConnectionDetails.
        User-defined description of the connection.


        :return: The description of this CreateConnectionDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateConnectionDetails.
        User-defined description of the connection.


        :param description: The description of this CreateConnectionDetails.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this CreateConnectionDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this CreateConnectionDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this CreateConnectionDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this CreateConnectionDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this CreateConnectionDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CreateConnectionDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CreateConnectionDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CreateConnectionDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this CreateConnectionDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.


        :return: The identifier of this CreateConnectionDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreateConnectionDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this CreateConnectionDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def primary_schema(self):
        """
        Gets the primary_schema of this CreateConnectionDetails.

        :return: The primary_schema of this CreateConnectionDetails.
        :rtype: oci.data_connectivity.models.Schema
        """
        return self._primary_schema

    @primary_schema.setter
    def primary_schema(self, primary_schema):
        """
        Sets the primary_schema of this CreateConnectionDetails.

        :param primary_schema: The primary_schema of this CreateConnectionDetails.
        :type: oci.data_connectivity.models.Schema
        """
        self._primary_schema = primary_schema

    @property
    def connection_properties(self):
        """
        Gets the connection_properties of this CreateConnectionDetails.
        The properties of the connection.


        :return: The connection_properties of this CreateConnectionDetails.
        :rtype: list[oci.data_connectivity.models.ConnectionProperty]
        """
        return self._connection_properties

    @connection_properties.setter
    def connection_properties(self, connection_properties):
        """
        Sets the connection_properties of this CreateConnectionDetails.
        The properties of the connection.


        :param connection_properties: The connection_properties of this CreateConnectionDetails.
        :type: list[oci.data_connectivity.models.ConnectionProperty]
        """
        self._connection_properties = connection_properties

    @property
    def properties(self):
        """
        **[Required]** Gets the properties of this CreateConnectionDetails.
        All the properties of the connection in a key-value map format.


        :return: The properties of this CreateConnectionDetails.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CreateConnectionDetails.
        All the properties of the connection in a key-value map format.


        :param properties: The properties of this CreateConnectionDetails.
        :type: dict(str, object)
        """
        self._properties = properties

    @property
    def type(self):
        """
        **[Required]** Gets the type of this CreateConnectionDetails.
        Specific Connection Type


        :return: The type of this CreateConnectionDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateConnectionDetails.
        Specific Connection Type


        :param type: The type of this CreateConnectionDetails.
        :type: str
        """
        self._type = type

    @property
    def is_default(self):
        """
        Gets the is_default of this CreateConnectionDetails.
        The default property of the connection.


        :return: The is_default of this CreateConnectionDetails.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this CreateConnectionDetails.
        The default property of the connection.


        :param is_default: The is_default of this CreateConnectionDetails.
        :type: bool
        """
        self._is_default = is_default

    @property
    def metadata(self):
        """
        Gets the metadata of this CreateConnectionDetails.

        :return: The metadata of this CreateConnectionDetails.
        :rtype: oci.data_connectivity.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this CreateConnectionDetails.

        :param metadata: The metadata of this CreateConnectionDetails.
        :type: oci.data_connectivity.models.ObjectMetadata
        """
        self._metadata = metadata

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this CreateConnectionDetails.

        :return: The registry_metadata of this CreateConnectionDetails.
        :rtype: oci.data_connectivity.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this CreateConnectionDetails.

        :param registry_metadata: The registry_metadata of this CreateConnectionDetails.
        :type: oci.data_connectivity.models.RegistryMetadata
        """
        self._registry_metadata = registry_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
