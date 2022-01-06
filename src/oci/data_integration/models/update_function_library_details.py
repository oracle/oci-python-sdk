# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateFunctionLibraryDetails(object):
    """
    The properties used in FunctionLibrary update operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateFunctionLibraryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UpdateFunctionLibraryDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this UpdateFunctionLibraryDetails.
        :type description: str

        :param category_name:
            The value to assign to the category_name property of this UpdateFunctionLibraryDetails.
        :type category_name: str

        :param object_status:
            The value to assign to the object_status property of this UpdateFunctionLibraryDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this UpdateFunctionLibraryDetails.
        :type identifier: str

        :param model_version:
            The value to assign to the model_version property of this UpdateFunctionLibraryDetails.
        :type model_version: str

        :param object_version:
            The value to assign to the object_version property of this UpdateFunctionLibraryDetails.
        :type object_version: int

        :param registry_metadata:
            The value to assign to the registry_metadata property of this UpdateFunctionLibraryDetails.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        """
        self.swagger_types = {
            'name': 'str',
            'description': 'str',
            'category_name': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'model_version': 'str',
            'object_version': 'int',
            'registry_metadata': 'RegistryMetadata'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'category_name': 'categoryName',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'model_version': 'modelVersion',
            'object_version': 'objectVersion',
            'registry_metadata': 'registryMetadata'
        }

        self._name = None
        self._description = None
        self._category_name = None
        self._object_status = None
        self._identifier = None
        self._model_version = None
        self._object_version = None
        self._registry_metadata = None

    @property
    def name(self):
        """
        Gets the name of this UpdateFunctionLibraryDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to  1000 characters.


        :return: The name of this UpdateFunctionLibraryDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateFunctionLibraryDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to  1000 characters.


        :param name: The name of this UpdateFunctionLibraryDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this UpdateFunctionLibraryDetails.
        A user defined description for the FunctionLibrary.


        :return: The description of this UpdateFunctionLibraryDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateFunctionLibraryDetails.
        A user defined description for the FunctionLibrary.


        :param description: The description of this UpdateFunctionLibraryDetails.
        :type: str
        """
        self._description = description

    @property
    def category_name(self):
        """
        Gets the category_name of this UpdateFunctionLibraryDetails.
        The category name.


        :return: The category_name of this UpdateFunctionLibraryDetails.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """
        Sets the category_name of this UpdateFunctionLibraryDetails.
        The category name.


        :param category_name: The category_name of this UpdateFunctionLibraryDetails.
        :type: str
        """
        self._category_name = category_name

    @property
    def object_status(self):
        """
        Gets the object_status of this UpdateFunctionLibraryDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this UpdateFunctionLibraryDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this UpdateFunctionLibraryDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this UpdateFunctionLibraryDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this UpdateFunctionLibraryDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this UpdateFunctionLibraryDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this UpdateFunctionLibraryDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this UpdateFunctionLibraryDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def model_version(self):
        """
        Gets the model_version of this UpdateFunctionLibraryDetails.
        The model version of an object.


        :return: The model_version of this UpdateFunctionLibraryDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this UpdateFunctionLibraryDetails.
        The model version of an object.


        :param model_version: The model_version of this UpdateFunctionLibraryDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def object_version(self):
        """
        Gets the object_version of this UpdateFunctionLibraryDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this UpdateFunctionLibraryDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this UpdateFunctionLibraryDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this UpdateFunctionLibraryDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this UpdateFunctionLibraryDetails.

        :return: The registry_metadata of this UpdateFunctionLibraryDetails.
        :rtype: oci.data_integration.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this UpdateFunctionLibraryDetails.

        :param registry_metadata: The registry_metadata of this UpdateFunctionLibraryDetails.
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
