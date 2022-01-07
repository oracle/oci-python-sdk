# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .base_type import BaseType
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfiguredType(BaseType):
    """
    A `ConfiguredType` represents a type that has built-in configuration to the type itself. An example is a `SSN` type whose basic type is `VARCHAR`, but the type itself also has a built-in configuration like length=10.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfiguredType object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.ConfiguredType.model_type` attribute
        of this class is ``CONFIGURED_TYPE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ConfiguredType.
            Allowed values for this property are: "DYNAMIC_TYPE", "STRUCTURED_TYPE", "DATA_TYPE", "JAVA_TYPE", "CONFIGURED_TYPE", "COMPOSITE_TYPE", "DERIVED_TYPE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this ConfiguredType.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this ConfiguredType.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ConfiguredType.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this ConfiguredType.
        :type name: str

        :param object_status:
            The value to assign to the object_status property of this ConfiguredType.
        :type object_status: int

        :param description:
            The value to assign to the description property of this ConfiguredType.
        :type description: str

        :param wrapped_type:
            The value to assign to the wrapped_type property of this ConfiguredType.
        :type wrapped_type: object

        :param config_values:
            The value to assign to the config_values property of this ConfiguredType.
        :type config_values: oci.data_integration.models.ConfigValues

        :param config_definition:
            The value to assign to the config_definition property of this ConfiguredType.
        :type config_definition: oci.data_integration.models.ConfigDefinition

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'object_status': 'int',
            'description': 'str',
            'wrapped_type': 'object',
            'config_values': 'ConfigValues',
            'config_definition': 'ConfigDefinition'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'object_status': 'objectStatus',
            'description': 'description',
            'wrapped_type': 'wrappedType',
            'config_values': 'configValues',
            'config_definition': 'configDefinition'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._object_status = None
        self._description = None
        self._wrapped_type = None
        self._config_values = None
        self._config_definition = None
        self._model_type = 'CONFIGURED_TYPE'

    @property
    def wrapped_type(self):
        """
        Gets the wrapped_type of this ConfiguredType.
        A wrapped type, may be a string or a BaseType.


        :return: The wrapped_type of this ConfiguredType.
        :rtype: object
        """
        return self._wrapped_type

    @wrapped_type.setter
    def wrapped_type(self, wrapped_type):
        """
        Sets the wrapped_type of this ConfiguredType.
        A wrapped type, may be a string or a BaseType.


        :param wrapped_type: The wrapped_type of this ConfiguredType.
        :type: object
        """
        self._wrapped_type = wrapped_type

    @property
    def config_values(self):
        """
        Gets the config_values of this ConfiguredType.

        :return: The config_values of this ConfiguredType.
        :rtype: oci.data_integration.models.ConfigValues
        """
        return self._config_values

    @config_values.setter
    def config_values(self, config_values):
        """
        Sets the config_values of this ConfiguredType.

        :param config_values: The config_values of this ConfiguredType.
        :type: oci.data_integration.models.ConfigValues
        """
        self._config_values = config_values

    @property
    def config_definition(self):
        """
        Gets the config_definition of this ConfiguredType.

        :return: The config_definition of this ConfiguredType.
        :rtype: oci.data_integration.models.ConfigDefinition
        """
        return self._config_definition

    @config_definition.setter
    def config_definition(self, config_definition):
        """
        Sets the config_definition of this ConfiguredType.

        :param config_definition: The config_definition of this ConfiguredType.
        :type: oci.data_integration.models.ConfigDefinition
        """
        self._config_definition = config_definition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
