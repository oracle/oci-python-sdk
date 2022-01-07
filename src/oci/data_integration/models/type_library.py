# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TypeLibrary(object):
    """
    The Data Integration type library container type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TypeLibrary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this TypeLibrary.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this TypeLibrary.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this TypeLibrary.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this TypeLibrary.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this TypeLibrary.
        :type name: str

        :param description:
            The value to assign to the description property of this TypeLibrary.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this TypeLibrary.
        :type object_version: int

        :param types:
            The value to assign to the types property of this TypeLibrary.
        :type types: dict(str, DerivedType)

        :param object_status:
            The value to assign to the object_status property of this TypeLibrary.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this TypeLibrary.
        :type identifier: str

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'types': 'dict(str, DerivedType)',
            'object_status': 'int',
            'identifier': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'types': 'types',
            'object_status': 'objectStatus',
            'identifier': 'identifier'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._types = None
        self._object_status = None
        self._identifier = None

    @property
    def key(self):
        """
        Gets the key of this TypeLibrary.
        The key of the object.


        :return: The key of this TypeLibrary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TypeLibrary.
        The key of the object.


        :param key: The key of this TypeLibrary.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this TypeLibrary.
        The type of the object.


        :return: The model_type of this TypeLibrary.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this TypeLibrary.
        The type of the object.


        :param model_type: The model_type of this TypeLibrary.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this TypeLibrary.
        The model version of an object.


        :return: The model_version of this TypeLibrary.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this TypeLibrary.
        The model version of an object.


        :param model_version: The model_version of this TypeLibrary.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this TypeLibrary.

        :return: The parent_ref of this TypeLibrary.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this TypeLibrary.

        :param parent_ref: The parent_ref of this TypeLibrary.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this TypeLibrary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this TypeLibrary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TypeLibrary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this TypeLibrary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TypeLibrary.
        A user defined description for the object.


        :return: The description of this TypeLibrary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TypeLibrary.
        A user defined description for the object.


        :param description: The description of this TypeLibrary.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this TypeLibrary.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this TypeLibrary.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this TypeLibrary.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this TypeLibrary.
        :type: int
        """
        self._object_version = object_version

    @property
    def types(self):
        """
        Gets the types of this TypeLibrary.
        types


        :return: The types of this TypeLibrary.
        :rtype: dict(str, DerivedType)
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this TypeLibrary.
        types


        :param types: The types of this TypeLibrary.
        :type: dict(str, DerivedType)
        """
        self._types = types

    @property
    def object_status(self):
        """
        Gets the object_status of this TypeLibrary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this TypeLibrary.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this TypeLibrary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this TypeLibrary.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this TypeLibrary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this TypeLibrary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this TypeLibrary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this TypeLibrary.
        :type: str
        """
        self._identifier = identifier

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
