# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProjectDetails(object):
    """
    The details including name and description for the project, which is a container of folders, tasks, and dataflows.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProjectDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ProjectDetails.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this ProjectDetails.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this ProjectDetails.
        :type model_version: str

        :param name:
            The value to assign to the name property of this ProjectDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this ProjectDetails.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this ProjectDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this ProjectDetails.
        :type identifier: str

        :param object_version:
            The value to assign to the object_version property of this ProjectDetails.
        :type object_version: int

        :param parent_ref:
            The value to assign to the parent_ref property of this ProjectDetails.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param registry_metadata:
            The value to assign to the registry_metadata property of this ProjectDetails.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'object_version': 'int',
            'parent_ref': 'ParentReference',
            'registry_metadata': 'RegistryMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'object_version': 'objectVersion',
            'parent_ref': 'parentRef',
            'registry_metadata': 'registryMetadata'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._object_version = None
        self._parent_ref = None
        self._registry_metadata = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this ProjectDetails.
        Generated key that can be used in API calls to identify project.


        :return: The key of this ProjectDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ProjectDetails.
        Generated key that can be used in API calls to identify project.


        :param key: The key of this ProjectDetails.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this ProjectDetails.
        The type of the object.


        :return: The model_type of this ProjectDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this ProjectDetails.
        The type of the object.


        :param model_type: The model_type of this ProjectDetails.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this ProjectDetails.
        The model version of an object.


        :return: The model_version of this ProjectDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this ProjectDetails.
        The model version of an object.


        :param model_version: The model_version of this ProjectDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        Gets the name of this ProjectDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this ProjectDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProjectDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this ProjectDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ProjectDetails.
        A user defined description for the project.


        :return: The description of this ProjectDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProjectDetails.
        A user defined description for the project.


        :param description: The description of this ProjectDetails.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this ProjectDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this ProjectDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this ProjectDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this ProjectDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this ProjectDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this ProjectDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this ProjectDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this ProjectDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def object_version(self):
        """
        **[Required]** Gets the object_version of this ProjectDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this ProjectDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this ProjectDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this ProjectDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this ProjectDetails.

        :return: The parent_ref of this ProjectDetails.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this ProjectDetails.

        :param parent_ref: The parent_ref of this ProjectDetails.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this ProjectDetails.

        :return: The registry_metadata of this ProjectDetails.
        :rtype: oci.data_integration.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this ProjectDetails.

        :param registry_metadata: The registry_metadata of this ProjectDetails.
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
