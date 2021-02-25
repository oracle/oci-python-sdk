# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .base_type import BaseType
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataType(BaseType):
    """
    A `DataType` object is a simple primitive type that describes the type of a single atomic unit of data.  For example, `INT`, `VARCHAR`, `NUMBER`, and so on.
    """

    #: A constant which can be used with the dt_type property of a DataType.
    #: This constant has a value of "PRIMITIVE"
    DT_TYPE_PRIMITIVE = "PRIMITIVE"

    #: A constant which can be used with the dt_type property of a DataType.
    #: This constant has a value of "STRUCTURED"
    DT_TYPE_STRUCTURED = "STRUCTURED"

    def __init__(self, **kwargs):
        """
        Initializes a new DataType object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.DataType.model_type` attribute
        of this class is ``DATA_TYPE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this DataType.
            Allowed values for this property are: "DYNAMIC_TYPE", "STRUCTURED_TYPE", "DATA_TYPE", "JAVA_TYPE", "CONFIGURED_TYPE", "COMPOSITE_TYPE", "DERIVED_TYPE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this DataType.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this DataType.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this DataType.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this DataType.
        :type name: str

        :param object_status:
            The value to assign to the object_status property of this DataType.
        :type object_status: int

        :param description:
            The value to assign to the description property of this DataType.
        :type description: str

        :param dt_type:
            The value to assign to the dt_type property of this DataType.
            Allowed values for this property are: "PRIMITIVE", "STRUCTURED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type dt_type: str

        :param type_system_name:
            The value to assign to the type_system_name property of this DataType.
        :type type_system_name: str

        :param config_definition:
            The value to assign to the config_definition property of this DataType.
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
            'dt_type': 'str',
            'type_system_name': 'str',
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
            'dt_type': 'dtType',
            'type_system_name': 'typeSystemName',
            'config_definition': 'configDefinition'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._object_status = None
        self._description = None
        self._dt_type = None
        self._type_system_name = None
        self._config_definition = None
        self._model_type = 'DATA_TYPE'

    @property
    def dt_type(self):
        """
        Gets the dt_type of this DataType.
        The data type.

        Allowed values for this property are: "PRIMITIVE", "STRUCTURED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The dt_type of this DataType.
        :rtype: str
        """
        return self._dt_type

    @dt_type.setter
    def dt_type(self, dt_type):
        """
        Sets the dt_type of this DataType.
        The data type.


        :param dt_type: The dt_type of this DataType.
        :type: str
        """
        allowed_values = ["PRIMITIVE", "STRUCTURED"]
        if not value_allowed_none_or_none_sentinel(dt_type, allowed_values):
            dt_type = 'UNKNOWN_ENUM_VALUE'
        self._dt_type = dt_type

    @property
    def type_system_name(self):
        """
        Gets the type_system_name of this DataType.
        The data type system name.


        :return: The type_system_name of this DataType.
        :rtype: str
        """
        return self._type_system_name

    @type_system_name.setter
    def type_system_name(self, type_system_name):
        """
        Sets the type_system_name of this DataType.
        The data type system name.


        :param type_system_name: The type_system_name of this DataType.
        :type: str
        """
        self._type_system_name = type_system_name

    @property
    def config_definition(self):
        """
        Gets the config_definition of this DataType.

        :return: The config_definition of this DataType.
        :rtype: oci.data_integration.models.ConfigDefinition
        """
        return self._config_definition

    @config_definition.setter
    def config_definition(self, config_definition):
        """
        Sets the config_definition of this DataType.

        :param config_definition: The config_definition of this DataType.
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
