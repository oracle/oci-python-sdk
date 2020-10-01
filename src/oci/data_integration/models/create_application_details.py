# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateApplicationDetails(object):
    """
    Properties used in application create operations.
    """

    #: A constant which can be used with the model_type property of a CreateApplicationDetails.
    #: This constant has a value of "INTEGRATION_APPLICATION"
    MODEL_TYPE_INTEGRATION_APPLICATION = "INTEGRATION_APPLICATION"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateApplicationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this CreateApplicationDetails.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateApplicationDetails.
        :type model_version: str

        :param model_type:
            The value to assign to the model_type property of this CreateApplicationDetails.
            Allowed values for this property are: "INTEGRATION_APPLICATION"
        :type model_type: str

        :param name:
            The value to assign to the name property of this CreateApplicationDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateApplicationDetails.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateApplicationDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateApplicationDetails.
        :type identifier: str

        :param source_application_info:
            The value to assign to the source_application_info property of this CreateApplicationDetails.
        :type source_application_info: CreateSourceApplicationInfo

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateApplicationDetails.
        :type registry_metadata: RegistryMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_version': 'str',
            'model_type': 'str',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'source_application_info': 'CreateSourceApplicationInfo',
            'registry_metadata': 'RegistryMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_version': 'modelVersion',
            'model_type': 'modelType',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'source_application_info': 'sourceApplicationInfo',
            'registry_metadata': 'registryMetadata'
        }

        self._key = None
        self._model_version = None
        self._model_type = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._source_application_info = None
        self._registry_metadata = None

    @property
    def key(self):
        """
        Gets the key of this CreateApplicationDetails.
        Currently not used on application creation. Reserved for future.


        :return: The key of this CreateApplicationDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CreateApplicationDetails.
        Currently not used on application creation. Reserved for future.


        :param key: The key of this CreateApplicationDetails.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this CreateApplicationDetails.
        The object's model version.


        :return: The model_version of this CreateApplicationDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this CreateApplicationDetails.
        The object's model version.


        :param model_version: The model_version of this CreateApplicationDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def model_type(self):
        """
        Gets the model_type of this CreateApplicationDetails.
        The type of the application.

        Allowed values for this property are: "INTEGRATION_APPLICATION"


        :return: The model_type of this CreateApplicationDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this CreateApplicationDetails.
        The type of the application.


        :param model_type: The model_type of this CreateApplicationDetails.
        :type: str
        """
        allowed_values = ["INTEGRATION_APPLICATION"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            raise ValueError(
                "Invalid value for `model_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._model_type = model_type

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateApplicationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this CreateApplicationDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateApplicationDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this CreateApplicationDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateApplicationDetails.
        Detailed description for the object.


        :return: The description of this CreateApplicationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateApplicationDetails.
        Detailed description for the object.


        :param description: The description of this CreateApplicationDetails.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this CreateApplicationDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this CreateApplicationDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this CreateApplicationDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this CreateApplicationDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        **[Required]** Gets the identifier of this CreateApplicationDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this CreateApplicationDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this CreateApplicationDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this CreateApplicationDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def source_application_info(self):
        """
        Gets the source_application_info of this CreateApplicationDetails.

        :return: The source_application_info of this CreateApplicationDetails.
        :rtype: CreateSourceApplicationInfo
        """
        return self._source_application_info

    @source_application_info.setter
    def source_application_info(self, source_application_info):
        """
        Sets the source_application_info of this CreateApplicationDetails.

        :param source_application_info: The source_application_info of this CreateApplicationDetails.
        :type: CreateSourceApplicationInfo
        """
        self._source_application_info = source_application_info

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this CreateApplicationDetails.

        :return: The registry_metadata of this CreateApplicationDetails.
        :rtype: RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this CreateApplicationDetails.

        :param registry_metadata: The registry_metadata of this CreateApplicationDetails.
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
