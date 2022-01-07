# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateFolderDetails(object):
    """
    The properties used in folder create operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateFolderDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CreateFolderDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateFolderDetails.
        :type model_version: str

        :param name:
            The value to assign to the name property of this CreateFolderDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateFolderDetails.
        :type description: str

        :param category_name:
            The value to assign to the category_name property of this CreateFolderDetails.
        :type category_name: str

        :param object_status:
            The value to assign to the object_status property of this CreateFolderDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateFolderDetails.
        :type identifier: str

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateFolderDetails.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'category_name': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'registry_metadata': 'RegistryMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'category_name': 'categoryName',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'registry_metadata': 'registryMetadata'
        }

        self._key = None
        self._model_version = None
        self._name = None
        self._description = None
        self._category_name = None
        self._object_status = None
        self._identifier = None
        self._registry_metadata = None

    @property
    def key(self):
        """
        Gets the key of this CreateFolderDetails.
        Currently not used on folder creation. Reserved for future.


        :return: The key of this CreateFolderDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateFolderDetails.
        Currently not used on folder creation. Reserved for future.


        :param key: The key of this CreateFolderDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateFolderDetails.
        The model version of an object.


        :return: The model_version of this CreateFolderDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateFolderDetails.
        The model version of an object.


        :param model_version: The model_version of this CreateFolderDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateFolderDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this CreateFolderDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateFolderDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this CreateFolderDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateFolderDetails.
        A user defined description for the folder.


        :return: The description of this CreateFolderDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateFolderDetails.
        A user defined description for the folder.


        :param description: The description of this CreateFolderDetails.
        :type: str
        """
        self._description = description

    @property
    def category_name(self):
        """
        Gets the category_name of this CreateFolderDetails.
        The category name.


        :return: The category_name of this CreateFolderDetails.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """
        Sets the category_name of this CreateFolderDetails.
        The category name.


        :param category_name: The category_name of this CreateFolderDetails.
        :type: str
        """
        self._category_name = category_name

    @property
    def object_status(self):
        """
        Gets the object_status of this CreateFolderDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CreateFolderDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CreateFolderDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CreateFolderDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this CreateFolderDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this CreateFolderDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreateFolderDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this CreateFolderDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def registry_metadata(self):
        """
        **[Required]** Gets the registry_metadata of this CreateFolderDetails.

        :return: The registry_metadata of this CreateFolderDetails.
        :rtype: oci.data_integration.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this CreateFolderDetails.

        :param registry_metadata: The registry_metadata of this CreateFolderDetails.
        :type: oci.data_integration.models.RegistryMetadata
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
