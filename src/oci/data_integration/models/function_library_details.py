# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FunctionLibraryDetails(object):
    """
    The details including name, description for the function library, which is a container for user defined functions.
    """

    #: A constant which can be used with the model_type property of a FunctionLibraryDetails.
    #: This constant has a value of "FUNCTION_LIBRARY"
    MODEL_TYPE_FUNCTION_LIBRARY = "FUNCTION_LIBRARY"

    def __init__(self, **kwargs):
        """
        Initializes a new FunctionLibraryDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this FunctionLibraryDetails.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this FunctionLibraryDetails.
            Allowed values for this property are: "FUNCTION_LIBRARY"
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this FunctionLibraryDetails.
        :type model_version: str

        :param name:
            The value to assign to the name property of this FunctionLibraryDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this FunctionLibraryDetails.
        :type description: str

        :param category_name:
            The value to assign to the category_name property of this FunctionLibraryDetails.
        :type category_name: str

        :param object_status:
            The value to assign to the object_status property of this FunctionLibraryDetails.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this FunctionLibraryDetails.
        :type identifier: str

        :param parent_ref:
            The value to assign to the parent_ref property of this FunctionLibraryDetails.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param object_version:
            The value to assign to the object_version property of this FunctionLibraryDetails.
        :type object_version: int

        :param registry_metadata:
            The value to assign to the registry_metadata property of this FunctionLibraryDetails.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'name': 'str',
            'description': 'str',
            'category_name': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'parent_ref': 'ParentReference',
            'object_version': 'int',
            'registry_metadata': 'RegistryMetadata'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'name': 'name',
            'description': 'description',
            'category_name': 'categoryName',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'parent_ref': 'parentRef',
            'object_version': 'objectVersion',
            'registry_metadata': 'registryMetadata'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._name = None
        self._description = None
        self._category_name = None
        self._object_status = None
        self._identifier = None
        self._parent_ref = None
        self._object_version = None
        self._registry_metadata = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this FunctionLibraryDetails.
        Generated key that can be used in API calls to identify FunctionLibrary.


        :return: The key of this FunctionLibraryDetails.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this FunctionLibraryDetails.
        Generated key that can be used in API calls to identify FunctionLibrary.


        :param key: The key of this FunctionLibraryDetails.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this FunctionLibraryDetails.
        The type of the object.

        Allowed values for this property are: "FUNCTION_LIBRARY"


        :return: The model_type of this FunctionLibraryDetails.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this FunctionLibraryDetails.
        The type of the object.


        :param model_type: The model_type of this FunctionLibraryDetails.
        :type: str
        """
        allowed_values = ["FUNCTION_LIBRARY"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            raise ValueError(
                "Invalid value for `model_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this FunctionLibraryDetails.
        The model version of an object.


        :return: The model_version of this FunctionLibraryDetails.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this FunctionLibraryDetails.
        The model version of an object.


        :param model_version: The model_version of this FunctionLibraryDetails.
        :type: str
        """
        self._model_version = model_version

    @property
    def name(self):
        """
        Gets the name of this FunctionLibraryDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this FunctionLibraryDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FunctionLibraryDetails.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this FunctionLibraryDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this FunctionLibraryDetails.
        A user defined description for the FunctionLibrary.


        :return: The description of this FunctionLibraryDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FunctionLibraryDetails.
        A user defined description for the FunctionLibrary.


        :param description: The description of this FunctionLibraryDetails.
        :type: str
        """
        self._description = description

    @property
    def category_name(self):
        """
        Gets the category_name of this FunctionLibraryDetails.
        The category name.


        :return: The category_name of this FunctionLibraryDetails.
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """
        Sets the category_name of this FunctionLibraryDetails.
        The category name.


        :param category_name: The category_name of this FunctionLibraryDetails.
        :type: str
        """
        self._category_name = category_name

    @property
    def object_status(self):
        """
        Gets the object_status of this FunctionLibraryDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this FunctionLibraryDetails.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this FunctionLibraryDetails.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this FunctionLibraryDetails.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this FunctionLibraryDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this FunctionLibraryDetails.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this FunctionLibraryDetails.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this FunctionLibraryDetails.
        :type: str
        """
        self._identifier = identifier

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this FunctionLibraryDetails.

        :return: The parent_ref of this FunctionLibraryDetails.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this FunctionLibraryDetails.

        :param parent_ref: The parent_ref of this FunctionLibraryDetails.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def object_version(self):
        """
        **[Required]** Gets the object_version of this FunctionLibraryDetails.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this FunctionLibraryDetails.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this FunctionLibraryDetails.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this FunctionLibraryDetails.
        :type: int
        """
        self._object_version = object_version

    @property
    def registry_metadata(self):
        """
        Gets the registry_metadata of this FunctionLibraryDetails.

        :return: The registry_metadata of this FunctionLibraryDetails.
        :rtype: oci.data_integration.models.RegistryMetadata
        """
        return self._registry_metadata

    @registry_metadata.setter
    def registry_metadata(self, registry_metadata):
        """
        Sets the registry_metadata of this FunctionLibraryDetails.

        :param registry_metadata: The registry_metadata of this FunctionLibraryDetails.
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
