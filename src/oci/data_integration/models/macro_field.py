# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .typed_object import TypedObject
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MacroField(TypedObject):
    """
    The type representing the macro field concept. Macro fields have an expression to define a macro.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MacroField object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.MacroField.model_type` attribute
        of this class is ``MACRO_FIELD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this MacroField.
            Allowed values for this property are: "SHAPE", "INPUT_PORT", "SHAPE_FIELD", "INPUT_FIELD", "DERIVED_FIELD", "MACRO_FIELD", "OUTPUT_FIELD", "DYNAMIC_PROXY_FIELD", "OUTPUT_PORT", "DYNAMIC_INPUT_FIELD", "PROXY_FIELD", "PARAMETER", "PIVOT_FIELD", "MACRO_PIVOT_FIELD", "CONDITIONAL_OUTPUT_PORT"
        :type model_type: str

        :param key:
            The value to assign to the key property of this MacroField.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this MacroField.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this MacroField.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param config_values:
            The value to assign to the config_values property of this MacroField.
        :type config_values: oci.data_integration.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this MacroField.
        :type object_status: int

        :param name:
            The value to assign to the name property of this MacroField.
        :type name: str

        :param description:
            The value to assign to the description property of this MacroField.
        :type description: str

        :param expr:
            The value to assign to the expr property of this MacroField.
        :type expr: oci.data_integration.models.Expression

        :param type:
            The value to assign to the type property of this MacroField.
        :type type: oci.data_integration.models.BaseType

        :param is_use_source_type:
            The value to assign to the is_use_source_type property of this MacroField.
        :type is_use_source_type: bool

        :param use_type:
            The value to assign to the use_type property of this MacroField.
        :type use_type: oci.data_integration.models.ConfiguredType

        :param labels:
            The value to assign to the labels property of this MacroField.
        :type labels: list[str]

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
            'type': 'BaseType',
            'is_use_source_type': 'bool',
            'use_type': 'ConfiguredType',
            'labels': 'list[str]'
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
            'type': 'type',
            'is_use_source_type': 'isUseSourceType',
            'use_type': 'useType',
            'labels': 'labels'
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
        self._type = None
        self._is_use_source_type = None
        self._use_type = None
        self._labels = None
        self._model_type = 'MACRO_FIELD'

    @property
    def expr(self):
        """
        Gets the expr of this MacroField.

        :return: The expr of this MacroField.
        :rtype: oci.data_integration.models.Expression
        """
        return self._expr

    @expr.setter
    def expr(self, expr):
        """
        Sets the expr of this MacroField.

        :param expr: The expr of this MacroField.
        :type: oci.data_integration.models.Expression
        """
        self._expr = expr

    @property
    def type(self):
        """
        Gets the type of this MacroField.

        :return: The type of this MacroField.
        :rtype: oci.data_integration.models.BaseType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MacroField.

        :param type: The type of this MacroField.
        :type: oci.data_integration.models.BaseType
        """
        self._type = type

    @property
    def is_use_source_type(self):
        """
        Gets the is_use_source_type of this MacroField.
        Specifies whether the type of macro fields is inferred from an expression or useType (false) or the source field (true).


        :return: The is_use_source_type of this MacroField.
        :rtype: bool
        """
        return self._is_use_source_type

    @is_use_source_type.setter
    def is_use_source_type(self, is_use_source_type):
        """
        Sets the is_use_source_type of this MacroField.
        Specifies whether the type of macro fields is inferred from an expression or useType (false) or the source field (true).


        :param is_use_source_type: The is_use_source_type of this MacroField.
        :type: bool
        """
        self._is_use_source_type = is_use_source_type

    @property
    def use_type(self):
        """
        Gets the use_type of this MacroField.

        :return: The use_type of this MacroField.
        :rtype: oci.data_integration.models.ConfiguredType
        """
        return self._use_type

    @use_type.setter
    def use_type(self, use_type):
        """
        Sets the use_type of this MacroField.

        :param use_type: The use_type of this MacroField.
        :type: oci.data_integration.models.ConfiguredType
        """
        self._use_type = use_type

    @property
    def labels(self):
        """
        Gets the labels of this MacroField.
        Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them to categorize content.


        :return: The labels of this MacroField.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this MacroField.
        Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them to categorize content.


        :param labels: The labels of this MacroField.
        :type: list[str]
        """
        self._labels = labels

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
