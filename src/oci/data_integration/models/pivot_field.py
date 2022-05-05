# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .typed_object import TypedObject
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PivotField(TypedObject):
    """
    The type representing the pivot field. Pivot fields have an expression to define a macro and a pattern to generate the column name
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PivotField object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.PivotField.model_type` attribute
        of this class is ``PIVOT_FIELD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this PivotField.
            Allowed values for this property are: "SHAPE", "INPUT_PORT", "SHAPE_FIELD", "INPUT_FIELD", "DERIVED_FIELD", "MACRO_FIELD", "OUTPUT_FIELD", "DYNAMIC_PROXY_FIELD", "OUTPUT_PORT", "DYNAMIC_INPUT_FIELD", "PROXY_FIELD", "PARAMETER", "PIVOT_FIELD", "MACRO_PIVOT_FIELD", "CONDITIONAL_OUTPUT_PORT"
        :type model_type: str

        :param key:
            The value to assign to the key property of this PivotField.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this PivotField.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this PivotField.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param config_values:
            The value to assign to the config_values property of this PivotField.
        :type config_values: oci.data_integration.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this PivotField.
        :type object_status: int

        :param name:
            The value to assign to the name property of this PivotField.
        :type name: str

        :param description:
            The value to assign to the description property of this PivotField.
        :type description: str

        :param expr:
            The value to assign to the expr property of this PivotField.
        :type expr: oci.data_integration.models.Expression

        :param use_type:
            The value to assign to the use_type property of this PivotField.
        :type use_type: oci.data_integration.models.ConfiguredType

        :param type:
            The value to assign to the type property of this PivotField.
        :type type: oci.data_integration.models.BaseType

        :param column_name_pattern:
            The value to assign to the column_name_pattern property of this PivotField.
        :type column_name_pattern: str

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
            'expr': 'Expression',
            'use_type': 'ConfiguredType',
            'type': 'BaseType',
            'column_name_pattern': 'str'
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
            'expr': 'expr',
            'use_type': 'useType',
            'type': 'type',
            'column_name_pattern': 'columnNamePattern'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._config_values = None
        self._object_status = None
        self._name = None
        self._description = None
        self._expr = None
        self._use_type = None
        self._type = None
        self._column_name_pattern = None
        self._model_type = 'PIVOT_FIELD'

    @property
    def expr(self):
        """
        Gets the expr of this PivotField.

        :return: The expr of this PivotField.
        :rtype: oci.data_integration.models.Expression
        """
        return self._expr

    @expr.setter
    def expr(self, expr):
        """
        Sets the expr of this PivotField.

        :param expr: The expr of this PivotField.
        :type: oci.data_integration.models.Expression
        """
        self._expr = expr

    @property
    def use_type(self):
        """
        Gets the use_type of this PivotField.

        :return: The use_type of this PivotField.
        :rtype: oci.data_integration.models.ConfiguredType
        """
        return self._use_type

    @use_type.setter
    def use_type(self, use_type):
        """
        Sets the use_type of this PivotField.

        :param use_type: The use_type of this PivotField.
        :type: oci.data_integration.models.ConfiguredType
        """
        self._use_type = use_type

    @property
    def type(self):
        """
        Gets the type of this PivotField.

        :return: The type of this PivotField.
        :rtype: oci.data_integration.models.BaseType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PivotField.

        :param type: The type of this PivotField.
        :type: oci.data_integration.models.BaseType
        """
        self._type = type

    @property
    def column_name_pattern(self):
        """
        Gets the column_name_pattern of this PivotField.
        column name pattern can be used to generate the name structure of the generated columns. By default column names are of %PIVOT_KEY_VALUE% or %MACRO_INPUT%_%PIVOT_KEY_VALUE%, but we can change it something by passing something like MY_PREFIX%PIVOT_KEY_VALUE%MY_SUFFIX or MY_PREFIX%MACRO_INPUT%_%PIVOT_KEY_VALUE%MY_SUFFIX which will add custom prefix and suffix to the column name.


        :return: The column_name_pattern of this PivotField.
        :rtype: str
        """
        return self._column_name_pattern

    @column_name_pattern.setter
    def column_name_pattern(self, column_name_pattern):
        """
        Sets the column_name_pattern of this PivotField.
        column name pattern can be used to generate the name structure of the generated columns. By default column names are of %PIVOT_KEY_VALUE% or %MACRO_INPUT%_%PIVOT_KEY_VALUE%, but we can change it something by passing something like MY_PREFIX%PIVOT_KEY_VALUE%MY_SUFFIX or MY_PREFIX%MACRO_INPUT%_%PIVOT_KEY_VALUE%MY_SUFFIX which will add custom prefix and suffix to the column name.


        :param column_name_pattern: The column_name_pattern of this PivotField.
        :type: str
        """
        self._column_name_pattern = column_name_pattern

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
