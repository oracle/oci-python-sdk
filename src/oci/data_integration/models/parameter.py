# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .typed_object import TypedObject
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Parameter(TypedObject):
    """
    Parameters are created and assigned values that can be deferred to execution/runtime.
    """

    #: A constant which can be used with the output_aggregation_type property of a Parameter.
    #: This constant has a value of "MIN"
    OUTPUT_AGGREGATION_TYPE_MIN = "MIN"

    #: A constant which can be used with the output_aggregation_type property of a Parameter.
    #: This constant has a value of "MAX"
    OUTPUT_AGGREGATION_TYPE_MAX = "MAX"

    #: A constant which can be used with the output_aggregation_type property of a Parameter.
    #: This constant has a value of "COUNT"
    OUTPUT_AGGREGATION_TYPE_COUNT = "COUNT"

    #: A constant which can be used with the output_aggregation_type property of a Parameter.
    #: This constant has a value of "SUM"
    OUTPUT_AGGREGATION_TYPE_SUM = "SUM"

    def __init__(self, **kwargs):
        """
        Initializes a new Parameter object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.Parameter.model_type` attribute
        of this class is ``PARAMETER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this Parameter.
            Allowed values for this property are: "SHAPE", "INPUT_PORT", "SHAPE_FIELD", "INPUT_FIELD", "DERIVED_FIELD", "OUTPUT_FIELD", "DYNAMIC_PROXY_FIELD", "OUTPUT_PORT", "DYNAMIC_INPUT_FIELD", "PROXY_FIELD", "PARAMETER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this Parameter.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this Parameter.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this Parameter.
        :type parent_ref: ParentReference

        :param config_values:
            The value to assign to the config_values property of this Parameter.
        :type config_values: ConfigValues

        :param object_status:
            The value to assign to the object_status property of this Parameter.
        :type object_status: int

        :param name:
            The value to assign to the name property of this Parameter.
        :type name: str

        :param description:
            The value to assign to the description property of this Parameter.
        :type description: str

        :param type:
            The value to assign to the type property of this Parameter.
        :type type: BaseType

        :param default_value:
            The value to assign to the default_value property of this Parameter.
        :type default_value: object

        :param root_object_default_value:
            The value to assign to the root_object_default_value property of this Parameter.
        :type root_object_default_value: object

        :param is_input:
            The value to assign to the is_input property of this Parameter.
        :type is_input: bool

        :param is_output:
            The value to assign to the is_output property of this Parameter.
        :type is_output: bool

        :param output_aggregation_type:
            The value to assign to the output_aggregation_type property of this Parameter.
            Allowed values for this property are: "MIN", "MAX", "COUNT", "SUM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type output_aggregation_type: str

        :param type_name:
            The value to assign to the type_name property of this Parameter.
        :type type_name: str

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'config_values': 'ConfigValues',
            'object_status': 'int',
            'name': 'str',
            'description': 'str',
            'type': 'BaseType',
            'default_value': 'object',
            'root_object_default_value': 'object',
            'is_input': 'bool',
            'is_output': 'bool',
            'output_aggregation_type': 'str',
            'type_name': 'str'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'config_values': 'configValues',
            'object_status': 'objectStatus',
            'name': 'name',
            'description': 'description',
            'type': 'type',
            'default_value': 'defaultValue',
            'root_object_default_value': 'rootObjectDefaultValue',
            'is_input': 'isInput',
            'is_output': 'isOutput',
            'output_aggregation_type': 'outputAggregationType',
            'type_name': 'typeName'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._config_values = None
        self._object_status = None
        self._name = None
        self._description = None
        self._type = None
        self._default_value = None
        self._root_object_default_value = None
        self._is_input = None
        self._is_output = None
        self._output_aggregation_type = None
        self._type_name = None
        self._model_type = 'PARAMETER'

    @property
    def type(self):
        """
        Gets the type of this Parameter.

        :return: The type of this Parameter.
        :rtype: BaseType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Parameter.

        :param type: The type of this Parameter.
        :type: BaseType
        """
        self._type = type

    @property
    def default_value(self):
        """
        Gets the default_value of this Parameter.
        The default value of the parameter.


        :return: The default_value of this Parameter.
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this Parameter.
        The default value of the parameter.


        :param default_value: The default_value of this Parameter.
        :type: object
        """
        self._default_value = default_value

    @property
    def root_object_default_value(self):
        """
        Gets the root_object_default_value of this Parameter.
        The default value of the parameter which can be an object in DIS, such as a data entity.


        :return: The root_object_default_value of this Parameter.
        :rtype: object
        """
        return self._root_object_default_value

    @root_object_default_value.setter
    def root_object_default_value(self, root_object_default_value):
        """
        Sets the root_object_default_value of this Parameter.
        The default value of the parameter which can be an object in DIS, such as a data entity.


        :param root_object_default_value: The root_object_default_value of this Parameter.
        :type: object
        """
        self._root_object_default_value = root_object_default_value

    @property
    def is_input(self):
        """
        Gets the is_input of this Parameter.
        Whether the parameter is input value.


        :return: The is_input of this Parameter.
        :rtype: bool
        """
        return self._is_input

    @is_input.setter
    def is_input(self, is_input):
        """
        Sets the is_input of this Parameter.
        Whether the parameter is input value.


        :param is_input: The is_input of this Parameter.
        :type: bool
        """
        self._is_input = is_input

    @property
    def is_output(self):
        """
        Gets the is_output of this Parameter.
        Whether the parameter is output value.


        :return: The is_output of this Parameter.
        :rtype: bool
        """
        return self._is_output

    @is_output.setter
    def is_output(self, is_output):
        """
        Sets the is_output of this Parameter.
        Whether the parameter is output value.


        :param is_output: The is_output of this Parameter.
        :type: bool
        """
        self._is_output = is_output

    @property
    def output_aggregation_type(self):
        """
        Gets the output_aggregation_type of this Parameter.
        The output aggregation type

        Allowed values for this property are: "MIN", "MAX", "COUNT", "SUM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The output_aggregation_type of this Parameter.
        :rtype: str
        """
        return self._output_aggregation_type

    @output_aggregation_type.setter
    def output_aggregation_type(self, output_aggregation_type):
        """
        Sets the output_aggregation_type of this Parameter.
        The output aggregation type


        :param output_aggregation_type: The output_aggregation_type of this Parameter.
        :type: str
        """
        allowed_values = ["MIN", "MAX", "COUNT", "SUM"]
        if not value_allowed_none_or_none_sentinel(output_aggregation_type, allowed_values):
            output_aggregation_type = 'UNKNOWN_ENUM_VALUE'
        self._output_aggregation_type = output_aggregation_type

    @property
    def type_name(self):
        """
        Gets the type_name of this Parameter.
        The name of the object type.


        :return: The type_name of this Parameter.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """
        Sets the type_name of this Parameter.
        The name of the object type.


        :param type_name: The type_name of this Parameter.
        :type: str
        """
        self._type_name = type_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
