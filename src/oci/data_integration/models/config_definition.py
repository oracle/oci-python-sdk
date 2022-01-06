# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigDefinition(object):
    """
    The configuration details of a configurable object. This contains one or more config param definitions.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ConfigDefinition.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this ConfigDefinition.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this ConfigDefinition.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ConfigDefinition.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this ConfigDefinition.
        :type name: str

        :param is_contained:
            The value to assign to the is_contained property of this ConfigDefinition.
        :type is_contained: bool

        :param object_status:
            The value to assign to the object_status property of this ConfigDefinition.
        :type object_status: int

        :param config_parameter_definitions:
            The value to assign to the config_parameter_definitions property of this ConfigDefinition.
        :type config_parameter_definitions: dict(str, ConfigParameterDefinition)

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'is_contained': 'bool',
            'object_status': 'int',
            'config_parameter_definitions': 'dict(str, ConfigParameterDefinition)'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'is_contained': 'isContained',
            'object_status': 'objectStatus',
            'config_parameter_definitions': 'configParameterDefinitions'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._is_contained = None
        self._object_status = None
        self._config_parameter_definitions = None

    @property
    def key(self):
        """
        Gets the key of this ConfigDefinition.
        The key of the object.


        :return: The key of this ConfigDefinition.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ConfigDefinition.
        The key of the object.


        :param key: The key of this ConfigDefinition.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this ConfigDefinition.
        The type of the object.


        :return: The model_type of this ConfigDefinition.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this ConfigDefinition.
        The type of the object.


        :param model_type: The model_type of this ConfigDefinition.
        :type: str
        """
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this ConfigDefinition.
        The model version of an object.


        :return: The model_version of this ConfigDefinition.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this ConfigDefinition.
        The model version of an object.


        :param model_version: The model_version of this ConfigDefinition.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this ConfigDefinition.

        :return: The parent_ref of this ConfigDefinition.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this ConfigDefinition.

        :param parent_ref: The parent_ref of this ConfigDefinition.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this ConfigDefinition.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this ConfigDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConfigDefinition.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this ConfigDefinition.
        :type: str
        """
        self._name = name

    @property
    def is_contained(self):
        """
        Gets the is_contained of this ConfigDefinition.
        Specifies whether the configuration is contained or not.


        :return: The is_contained of this ConfigDefinition.
        :rtype: bool
        """
        return self._is_contained

    @is_contained.setter
    def is_contained(self, is_contained):
        """
        Sets the is_contained of this ConfigDefinition.
        Specifies whether the configuration is contained or not.


        :param is_contained: The is_contained of this ConfigDefinition.
        :type: bool
        """
        self._is_contained = is_contained

    @property
    def object_status(self):
        """
        Gets the object_status of this ConfigDefinition.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this ConfigDefinition.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this ConfigDefinition.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this ConfigDefinition.
        :type: int
        """
        self._object_status = object_status

    @property
    def config_parameter_definitions(self):
        """
        Gets the config_parameter_definitions of this ConfigDefinition.
        The parameter configuration details.


        :return: The config_parameter_definitions of this ConfigDefinition.
        :rtype: dict(str, ConfigParameterDefinition)
        """
        return self._config_parameter_definitions

    @config_parameter_definitions.setter
    def config_parameter_definitions(self, config_parameter_definitions):
        """
        Sets the config_parameter_definitions of this ConfigDefinition.
        The parameter configuration details.


        :param config_parameter_definitions: The config_parameter_definitions of this ConfigDefinition.
        :type: dict(str, ConfigParameterDefinition)
        """
        self._config_parameter_definitions = config_parameter_definitions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
