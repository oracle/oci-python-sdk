# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .base_type import BaseType
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JavaType(BaseType):
    """
    A java type object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JavaType object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.JavaType.model_type` attribute
        of this class is ``JAVA_TYPE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this JavaType.
            Allowed values for this property are: "DYNAMIC_TYPE", "STRUCTURED_TYPE", "DATA_TYPE", "JAVA_TYPE", "CONFIGURED_TYPE", "COMPOSITE_TYPE", "DERIVED_TYPE", "ARRAY_TYPE", "MAP_TYPE", "MATERIALIZED_COMPOSITE_TYPE"
        :type model_type: str

        :param key:
            The value to assign to the key property of this JavaType.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this JavaType.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this JavaType.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this JavaType.
        :type name: str

        :param object_status:
            The value to assign to the object_status property of this JavaType.
        :type object_status: int

        :param description:
            The value to assign to the description property of this JavaType.
        :type description: str

        :param java_type_name:
            The value to assign to the java_type_name property of this JavaType.
        :type java_type_name: str

        :param config_definition:
            The value to assign to the config_definition property of this JavaType.
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
            'java_type_name': 'str',
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
            'java_type_name': 'javaTypeName',
            'config_definition': 'configDefinition'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._object_status = None
        self._description = None
        self._java_type_name = None
        self._config_definition = None
        self._model_type = 'JAVA_TYPE'

    @property
    def java_type_name(self):
        """
        Gets the java_type_name of this JavaType.
        The java type name.


        :return: The java_type_name of this JavaType.
        :rtype: str
        """
        return self._java_type_name

    @java_type_name.setter
    def java_type_name(self, java_type_name):
        """
        Sets the java_type_name of this JavaType.
        The java type name.


        :param java_type_name: The java_type_name of this JavaType.
        :type: str
        """
        self._java_type_name = java_type_name

    @property
    def config_definition(self):
        """
        Gets the config_definition of this JavaType.

        :return: The config_definition of this JavaType.
        :rtype: oci.data_integration.models.ConfigDefinition
        """
        return self._config_definition

    @config_definition.setter
    def config_definition(self, config_definition):
        """
        Sets the config_definition of this JavaType.

        :param config_definition: The config_definition of this JavaType.
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
