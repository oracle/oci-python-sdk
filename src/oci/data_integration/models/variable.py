# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Variable(object):
    """
    Variable definitions in the pipeline.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Variable object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Variable.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this Variable.
        :type model_version: str

        :param model_type:
            The value to assign to the model_type property of this Variable.
        :type model_type: str

        :param parent_ref:
            The value to assign to the parent_ref property of this Variable.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this Variable.
        :type name: str

        :param description:
            The value to assign to the description property of this Variable.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this Variable.
        :type object_version: int

        :param object_status:
            The value to assign to the object_status property of this Variable.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this Variable.
        :type identifier: str

        :param type:
            The value to assign to the type property of this Variable.
        :type type: oci.data_integration.models.BaseType

        :param config_values:
            The value to assign to the config_values property of this Variable.
        :type config_values: oci.data_integration.models.ConfigValues

        :param default_value:
            The value to assign to the default_value property of this Variable.
        :type default_value: object

        :param root_object_default_value:
            The value to assign to the root_object_default_value property of this Variable.
        :type root_object_default_value: oci.data_integration.models.RootObject

        """
        self.swagger_types = {
            'key': 'str',
            'model_version': 'str',
            'model_type': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'object_status': 'int',
            'identifier': 'str',
            'type': 'BaseType',
            'config_values': 'ConfigValues',
            'default_value': 'object',
            'root_object_default_value': 'RootObject'
        }

        self.attribute_map = {
            'key': 'key',
            'model_version': 'modelVersion',
            'model_type': 'modelType',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'type': 'type',
            'config_values': 'configValues',
            'default_value': 'defaultValue',
            'root_object_default_value': 'rootObjectDefaultValue'
        }

        self._key = None
        self._model_version = None
        self._model_type = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._object_status = None
        self._identifier = None
        self._type = None
        self._config_values = None
        self._default_value = None
        self._root_object_default_value = None

    @property
    def key(self):
        """
        Gets the key of this Variable.
        Generated key that can be used in API calls to identify variable. On scenarios where reference to the variable is needed, a value can be passed in create.


        :return: The key of this Variable.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Variable.
        Generated key that can be used in API calls to identify variable. On scenarios where reference to the variable is needed, a value can be passed in create.


        :param key: The key of this Variable.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this Variable.
        This is a version number that is used by the service to upgrade objects if needed through releases of the service.


        :return: The model_version of this Variable.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this Variable.
        This is a version number that is used by the service to upgrade objects if needed through releases of the service.


        :param model_version: The model_version of this Variable.
        :type: str
        """
        self._model_version = model_version

    @property
    def model_type(self):
        """
        Gets the model_type of this Variable.
        The type of the object.


        :return: The model_type of this Variable.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this Variable.
        The type of the object.


        :param model_type: The model_type of this Variable.
        :type: str
        """
        self._model_type = model_type

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this Variable.

        :return: The parent_ref of this Variable.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this Variable.

        :param parent_ref: The parent_ref of this Variable.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this Variable.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this Variable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Variable.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this Variable.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Variable.
        Detailed description for the object.


        :return: The description of this Variable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Variable.
        Detailed description for the object.


        :param description: The description of this Variable.
        :type: str
        """
        self._description = description

    @property
    def object_version(self):
        """
        Gets the object_version of this Variable.
        This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.


        :return: The object_version of this Variable.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this Variable.
        This is used by the service for optimistic locking of the object, to prevent multiple users from simultaneously updating the object.


        :param object_version: The object_version of this Variable.
        :type: int
        """
        self._object_version = object_version

    @property
    def object_status(self):
        """
        Gets the object_status of this Variable.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this Variable.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this Variable.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this Variable.
        :type: int
        """
        self._object_status = object_status

    @property
    def identifier(self):
        """
        Gets the identifier of this Variable.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this Variable.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this Variable.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this Variable.
        :type: str
        """
        self._identifier = identifier

    @property
    def type(self):
        """
        Gets the type of this Variable.

        :return: The type of this Variable.
        :rtype: oci.data_integration.models.BaseType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Variable.

        :param type: The type of this Variable.
        :type: oci.data_integration.models.BaseType
        """
        self._type = type

    @property
    def config_values(self):
        """
        Gets the config_values of this Variable.

        :return: The config_values of this Variable.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this Variable.

        :param config_values: The config_values of this Variable.
        :type: oci.data_integration.models.ConfigValues
        """
        self._config_values = config_values

    @property
    def default_value(self):
        """
        Gets the default_value of this Variable.
        A default value for the vairable.


        :return: The default_value of this Variable.
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this Variable.
        A default value for the vairable.


        :param default_value: The default_value of this Variable.
        :type: object
        """
        self._default_value = default_value

    @property
    def root_object_default_value(self):
        """
        Gets the root_object_default_value of this Variable.

        :return: The root_object_default_value of this Variable.
        :rtype: oci.data_integration.models.RootObject
        """
        return self._root_object_default_value

    @root_object_default_value.setter
    def root_object_default_value(self, root_object_default_value):
        """
        Sets the root_object_default_value of this Variable.

        :param root_object_default_value: The root_object_default_value of this Variable.
        :type: oci.data_integration.models.RootObject
        """
        self._root_object_default_value = root_object_default_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
