# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataAsset(object):
    """
    Represents a data source in the Data Integration service.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DataAsset object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this DataAsset.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DataAsset.
        :type model_version: str

        :param model_type:
            The value to assign to the model_type property of this DataAsset.
        :type model_type: str

        :param name:
            The value to assign to the name property of this DataAsset.
        :type name: str

        :param description:
            The value to assign to the description property of this DataAsset.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this DataAsset.
        :type object_status: int

        :param object_version:
            The value to assign to the object_version property of this DataAsset.
        :type object_version: int

        :param identifier:
            The value to assign to the identifier property of this DataAsset.
        :type identifier: str

        :param external_key:
            The value to assign to the external_key property of this DataAsset.
        :type external_key: str

        :param asset_properties:
            The value to assign to the asset_properties property of this DataAsset.
        :type asset_properties: dict(str, str)

        :param properties:
            The value to assign to the properties property of this DataAsset.
        :type properties: dict(str, object)

        :param type:
            The value to assign to the type property of this DataAsset.
        :type type: str

        :param native_type_system:
            The value to assign to the native_type_system property of this DataAsset.
        :type native_type_system: oci.data_connectivity.models.TypeSystem

        :param registry_metadata:
            The value to assign to the registry_metadata property of this DataAsset.
        :type registry_metadata: oci.data_connectivity.models.RegistryMetadata

        :param metadata:
            The value to assign to the metadata property of this DataAsset.
        :type metadata: oci.data_connectivity.models.ObjectMetadata

        :param default_connection:
            The value to assign to the default_connection property of this DataAsset.
        :type default_connection: oci.data_connectivity.models.Connection

        :param end_points:
            The value to assign to the end_points property of this DataAsset.
        :type end_points: list[oci.data_connectivity.models.DpEndpoint]

        """
        self.swagger_types = {
            'key': 'str',
            'model_version': 'str',
            'model_type': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'object_version': 'int',
            'identifier': 'str',
            'external_key': 'str',
            'asset_properties': 'dict(str, str)',
            'properties': 'dict(str, object)',
            'type': 'str',
            'native_type_system': 'TypeSystem',
            'registry_metadata': 'RegistryMetadata',
            'metadata': 'ObjectMetadata',
            'default_connection': 'Connection',
            'end_points': 'list[DpEndpoint]'
        }

        self.attribute_map = {
            'key': 'key',
            'model_version': 'modelVersion',
            'model_type': 'modelType',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'object_version': 'objectVersion',
            'identifier': 'identifier',
            'external_key': 'externalKey',
            'asset_properties': 'assetProperties',
            'properties': 'properties',
            'type': 'type',
            'native_type_system': 'nativeTypeSystem',
            'registry_metadata': 'registryMetadata',
            'metadata': 'metadata',
            'default_connection': 'defaultConnection',
            'end_points': 'endPoints'
        }

        self._key = None
        self._model_version = None
        self._model_type = None
        self._name = None
        self._description = None
        self._object_status = None
        self._object_version = None
        self._identifier = None
        self._external_key = None
        self._asset_properties = None
        self._properties = None
        self._type = None
        self._native_type_system = None
        self._registry_metadata = None
        self._metadata = None
        self._default_connection = None
        self._end_points = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this DataAsset.
        Currently not used on data asset creation. Reserved for future.


        :return: The key of this DataAsset.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DataAsset.
        Currently not used on data asset creation. Reserved for future.


        :param key: The key of this DataAsset.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this DataAsset.
        The model version of an object.


        :return: The model_version of this DataAsset.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this DataAsset.
        The model version of an object.


        :param model_version: The model_version of this DataAsset.
        :type: str
        """
        self._model_version = model_version

    @property
    def model_type(self):
        """
        Gets the model_type of this DataAsset.
        The type of the object.


        :return: The model_type of this DataAsset.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this DataAsset.
        The type of the object.


        :param model_type: The model_type of this DataAsset.
        :type: str
        """
        self._model_type = model_type

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DataAsset.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this DataAsset.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DataAsset.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this DataAsset.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DataAsset.
        User-defined description of the data asset.


        :return: The description of this DataAsset.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DataAsset.
        User-defined description of the data asset.


        :param description: The description of this DataAsset.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this DataAsset.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this DataAsset.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this DataAsset.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this DataAsset.
        :type: int
        """
        self._object_status = object_status

    @property
    def object_version(self):
        """
        Gets the object_version of this DataAsset.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this DataAsset.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this DataAsset.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this DataAsset.
        :type: int
        """
        self._object_version = object_version

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this DataAsset.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this DataAsset.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this DataAsset.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this DataAsset.
        :type: str
        """
        self._identifier = identifier

    @property
    def external_key(self):
        """
        Gets the external_key of this DataAsset.
        The external key for the object.


        :return: The external_key of this DataAsset.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this DataAsset.
        The external key for the object.


        :param external_key: The external_key of this DataAsset.
        :type: str
        """
        self._external_key = external_key

    @property
    def asset_properties(self):
        """
        Gets the asset_properties of this DataAsset.
        Additional properties for the data asset.


        :return: The asset_properties of this DataAsset.
        :rtype: dict(str, str)
        """
        return self._asset_properties

    @asset_properties.setter
    def asset_properties(self, asset_properties):
        """
        Sets the asset_properties of this DataAsset.
        Additional properties for the data asset.


        :param asset_properties: The asset_properties of this DataAsset.
        :type: dict(str, str)
        """
        self._asset_properties = asset_properties

    @property
    def properties(self):
        """
        Gets the properties of this DataAsset.
        All the properties for the data asset in a key-value map format.


        :return: The properties of this DataAsset.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this DataAsset.
        All the properties for the data asset in a key-value map format.


        :param properties: The properties of this DataAsset.
        :type: dict(str, object)
        """
        self._properties = properties

    @property
    def type(self):
        """
        Gets the type of this DataAsset.
        Specific DataAsset Type


        :return: The type of this DataAsset.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DataAsset.
        Specific DataAsset Type


        :param type: The type of this DataAsset.
        :type: str
        """
        self._type = type

    @property
    def native_type_system(self):
        """
        Gets the native_type_system of this DataAsset.

        :return: The native_type_system of this DataAsset.
        :rtype: oci.data_connectivity.models.TypeSystem
        """
        return self._native_type_system

    @native_type_system.setter
    def native_type_system(self, native_type_system):
        """
        Sets the native_type_system of this DataAsset.

        :param native_type_system: The native_type_system of this DataAsset.
        :type: oci.data_connectivity.models.TypeSystem
        """
        self._native_type_system = native_type_system

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this DataAsset.

        :return: The registry_metadata of this DataAsset.
        :rtype: oci.data_connectivity.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this DataAsset.

        :param registry_metadata: The registry_metadata of this DataAsset.
        :type: oci.data_connectivity.models.RegistryMetadata
        """
        self._registry_metadata = registry_metadata

    @property
    def metadata(self):
        """
        Gets the metadata of this DataAsset.

        :return: The metadata of this DataAsset.
        :rtype: oci.data_connectivity.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this DataAsset.

        :param metadata: The metadata of this DataAsset.
        :type: oci.data_connectivity.models.ObjectMetadata
        """
        self._metadata = metadata

    @property
    def default_connection(self):
        """
        Gets the default_connection of this DataAsset.

        :return: The default_connection of this DataAsset.
        :rtype: oci.data_connectivity.models.Connection
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this DataAsset.

        :param default_connection: The default_connection of this DataAsset.
        :type: oci.data_connectivity.models.Connection
        """
        self._default_connection = default_connection

    @property
    def end_points(self):
        """
        Gets the end_points of this DataAsset.
        The list of endpoints with which this data asset is associated.


        :return: The end_points of this DataAsset.
        :rtype: list[oci.data_connectivity.models.DpEndpoint]
        """
        return self._end_points

    @end_points.setter
    def end_points(self, end_points):
        """
        Sets the end_points of this DataAsset.
        The list of endpoints with which this data asset is associated.


        :param end_points: The end_points of this DataAsset.
        :type: list[oci.data_connectivity.models.DpEndpoint]
        """
        self._end_points = end_points

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
