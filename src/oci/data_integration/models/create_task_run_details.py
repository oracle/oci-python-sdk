# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTaskRunDetails(object):
    """
    Properties used in task run create operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTaskRunDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CreateTaskRunDetails.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this CreateTaskRunDetails.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this CreateTaskRunDetails.
        :type model_version: str

        :param name:
            The value to assign to the name property of this CreateTaskRunDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateTaskRunDetails.
        :type description: str

        :param config_provider:
            The value to assign to the config_provider property of this CreateTaskRunDetails.
        :type config_provider: CreateConfigProvider

        :param identifier:
            The value to assign to the identifier property of this CreateTaskRunDetails.
        :type identifier: str

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateTaskRunDetails.
        :type registry_metadata: RegistryMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'config_provider': 'CreateConfigProvider',
            'identifier': 'str',
            'registry_metadata': 'RegistryMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'config_provider': 'configProvider',
            'identifier': 'identifier',
            'registry_metadata': 'registryMetadata'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._name = None
        self._description = None
        self._config_provider = None
        self._identifier = None
        self._registry_metadata = None

    @property
    def key(self):
        """
        Gets the key of this CreateTaskRunDetails.
        The key of the object.


        :return: The key of this CreateTaskRunDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateTaskRunDetails.
        The key of the object.


        :param key: The key of this CreateTaskRunDetails.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this CreateTaskRunDetails.
        The type of the object.


        :return: The model_type of this CreateTaskRunDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateTaskRunDetails.
        The type of the object.


        :param model_type: The model_type of this CreateTaskRunDetails.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateTaskRunDetails.
        The model version of an object.


        :return: The model_version of this CreateTaskRunDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateTaskRunDetails.
        The model version of an object.


        :param model_version: The model_version of this CreateTaskRunDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        Gets the name of this CreateTaskRunDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :return: The name of this CreateTaskRunDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateTaskRunDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value can be edited by the user and it is restricted to 1000 characters


        :param name: The name of this CreateTaskRunDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateTaskRunDetails.
        Detailed description for the object.


        :return: The description of this CreateTaskRunDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateTaskRunDetails.
        Detailed description for the object.


        :param description: The description of this CreateTaskRunDetails.
        :type: str
        """
        self._description = description

    @property
    def config_provider(self):
        """
        Gets the config_provider of this CreateTaskRunDetails.

        :return: The config_provider of this CreateTaskRunDetails.
        :rtype: CreateConfigProvider
        """
        return self._config_provider

    @config_provider.setter
    def config_provider(self, config_provider):
        """
        Sets the config_provider of this CreateTaskRunDetails.

        :param config_provider: The config_provider of this CreateTaskRunDetails.
        :type: CreateConfigProvider
        """
        self._config_provider = config_provider

    @property
    def identifier(self):
        """
        Gets the identifier of this CreateTaskRunDetails.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.


        :return: The identifier of this CreateTaskRunDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreateTaskRunDetails.
        Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be edited by the user.


        :param identifier: The identifier of this CreateTaskRunDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this CreateTaskRunDetails.

        :return: The registry_metadata of this CreateTaskRunDetails.
        :rtype: RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this CreateTaskRunDetails.

        :param registry_metadata: The registry_metadata of this CreateTaskRunDetails.
        :type: RegistryMetadata
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
