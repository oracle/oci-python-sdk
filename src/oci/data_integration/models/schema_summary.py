# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SchemaSummary(object):
    """
    The schema summary object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SchemaSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this SchemaSummary.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this SchemaSummary.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this SchemaSummary.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this SchemaSummary.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this SchemaSummary.
        :type name: str

        :param resource_name:
            The value to assign to the resource_name property of this SchemaSummary.
        :type resource_name: str

        :param description:
            The value to assign to the description property of this SchemaSummary.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this SchemaSummary.
        :type object_version: int

        :param external_key:
            The value to assign to the external_key property of this SchemaSummary.
        :type external_key: str

        :param is_has_containers:
            The value to assign to the is_has_containers property of this SchemaSummary.
        :type is_has_containers: bool

        :param default_connection:
            The value to assign to the default_connection property of this SchemaSummary.
        :type default_connection: str

        :param object_status:
            The value to assign to the object_status property of this SchemaSummary.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this SchemaSummary.
        :type identifier: str

        :param metadata:
            The value to assign to the metadata property of this SchemaSummary.
        :type metadata: oci.data_integration.models.ObjectMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'resource_name': 'str',
            'description': 'str',
            'object_version': 'int',
            'external_key': 'str',
            'is_has_containers': 'bool',
            'default_connection': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'metadata': 'ObjectMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'resource_name': 'resourceName',
            'description': 'description',
            'object_version': 'objectVersion',
            'external_key': 'externalKey',
            'is_has_containers': 'isHasContainers',
            'default_connection': 'defaultConnection',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'metadata': 'metadata'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._resource_name = None
        self._description = None
        self._object_version = None
        self._external_key = None
        self._is_has_containers = None
        self._default_connection = None
        self._object_status = None
        self._identifier = None
        self._metadata = None

    @property
    def key(self):
        """
        Gets the key of this SchemaSummary.
        The object key.


        :return: The key of this SchemaSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this SchemaSummary.
        The object key.


        :param key: The key of this SchemaSummary.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this SchemaSummary.
        The object's type.


        :return: The model_type of this SchemaSummary.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this SchemaSummary.
        The object's type.


        :param model_type: The model_type of this SchemaSummary.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this SchemaSummary.
        The object's model version.


        :return: The model_version of this SchemaSummary.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this SchemaSummary.
        The object's model version.


        :param model_version: The model_version of this SchemaSummary.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this SchemaSummary.

        :return: The parent_ref of this SchemaSummary.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this SchemaSummary.

        :param parent_ref: The parent_ref of this SchemaSummary.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this SchemaSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this SchemaSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SchemaSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this SchemaSummary.
        :type: str
        """
        self._name = name

    @property
    def resource_name(self):
        """
        Gets the resource_name of this SchemaSummary.
        A resource name can have letters, numbers, and special characters. The value is editable and is restricted to 4000 characters.


        :return: The resource_name of this SchemaSummary.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this SchemaSummary.
        A resource name can have letters, numbers, and special characters. The value is editable and is restricted to 4000 characters.


        :param resource_name: The resource_name of this SchemaSummary.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def description(self):
        """
        Gets the description of this SchemaSummary.
        User-defined description for the schema.


        :return: The description of this SchemaSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SchemaSummary.
        User-defined description for the schema.


        :param description: The description of this SchemaSummary.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this SchemaSummary.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this SchemaSummary.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this SchemaSummary.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this SchemaSummary.
        :type: int
        """
        self._object_version = object_version

    @property
    def external_key(self):
        """
        Gets the external_key of this SchemaSummary.
        The external key for the object.


        :return: The external_key of this SchemaSummary.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this SchemaSummary.
        The external key for the object.


        :param external_key: The external_key of this SchemaSummary.
        :type: str
        """
        self._external_key = external_key

    @property
    def is_has_containers(self):
        """
        Gets the is_has_containers of this SchemaSummary.
        Specifies whether the schema has containers.


        :return: The is_has_containers of this SchemaSummary.
        :rtype: bool
        """
        return self._is_has_containers

    @is_has_containers.setter
    def is_has_containers(self, is_has_containers):
        """
        Sets the is_has_containers of this SchemaSummary.
        Specifies whether the schema has containers.


        :param is_has_containers: The is_has_containers of this SchemaSummary.
        :type: bool
        """
        self._is_has_containers = is_has_containers

    @property
    def default_connection(self):
        """
        Gets the default_connection of this SchemaSummary.
        The default connection key.


        :return: The default_connection of this SchemaSummary.
        :rtype: str
        """
        return self._default_connection

    @default_connection.setter
    def default_connection(self, default_connection):
        """
        Sets the default_connection of this SchemaSummary.
        The default connection key.


        :param default_connection: The default_connection of this SchemaSummary.
        :type: str
        """
        self._default_connection = default_connection

    @property
    def object_status(self):
        """
        Gets the object_status of this SchemaSummary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this SchemaSummary.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this SchemaSummary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this SchemaSummary.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this SchemaSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this SchemaSummary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this SchemaSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this SchemaSummary.
        :type: str
        """
        self._identifier = identifier

    @property
    def metadata(self):
        """
        Gets the metadata of this SchemaSummary.

        :return: The metadata of this SchemaSummary.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this SchemaSummary.

        :param metadata: The metadata of this SchemaSummary.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
