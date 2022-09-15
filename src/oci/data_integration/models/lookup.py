# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .operator import Operator
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Lookup(Operator):
    """
    The information about the lookup operator. The lookup operator has two input links, a primary input, and a lookup source input. It has an output link, fields of the lookup input are appended to the primary input and projected as the output fields.
    """

    #: A constant which can be used with the multi_match_strategy property of a Lookup.
    #: This constant has a value of "RETURN_ANY"
    MULTI_MATCH_STRATEGY_RETURN_ANY = "RETURN_ANY"

    #: A constant which can be used with the multi_match_strategy property of a Lookup.
    #: This constant has a value of "RETURN_FIRST"
    MULTI_MATCH_STRATEGY_RETURN_FIRST = "RETURN_FIRST"

    #: A constant which can be used with the multi_match_strategy property of a Lookup.
    #: This constant has a value of "RETURN_LAST"
    MULTI_MATCH_STRATEGY_RETURN_LAST = "RETURN_LAST"

    #: A constant which can be used with the multi_match_strategy property of a Lookup.
    #: This constant has a value of "RETURN_ALL"
    MULTI_MATCH_STRATEGY_RETURN_ALL = "RETURN_ALL"

    #: A constant which can be used with the multi_match_strategy property of a Lookup.
    #: This constant has a value of "RETURN_ERROR"
    MULTI_MATCH_STRATEGY_RETURN_ERROR = "RETURN_ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new Lookup object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.Lookup.model_type` attribute
        of this class is ``LOOKUP_OPERATOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this Lookup.
            Allowed values for this property are: "SOURCE_OPERATOR", "FILTER_OPERATOR", "JOINER_OPERATOR", "AGGREGATOR_OPERATOR", "PROJECTION_OPERATOR", "TARGET_OPERATOR", "FLATTEN_OPERATOR", "DISTINCT_OPERATOR", "SORT_OPERATOR", "UNION_OPERATOR", "INTERSECT_OPERATOR", "MINUS_OPERATOR", "MERGE_OPERATOR", "FUNCTION_OPERATOR", "SPLIT_OPERATOR", "START_OPERATOR", "END_OPERATOR", "PIPELINE_OPERATOR", "DECISION_OPERATOR", "TASK_OPERATOR", "EXPRESSION_OPERATOR", "LOOKUP_OPERATOR", "PIVOT_OPERATOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this Lookup.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this Lookup.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this Lookup.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this Lookup.
        :type name: str

        :param description:
            The value to assign to the description property of this Lookup.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this Lookup.
        :type object_version: int

        :param input_ports:
            The value to assign to the input_ports property of this Lookup.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this Lookup.
        :type output_ports: list[oci.data_integration.models.TypedObject]

        :param object_status:
            The value to assign to the object_status property of this Lookup.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this Lookup.
        :type identifier: str

        :param parameters:
            The value to assign to the parameters property of this Lookup.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this Lookup.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param lookup_condition:
            The value to assign to the lookup_condition property of this Lookup.
        :type lookup_condition: oci.data_integration.models.Expression

        :param is_skip_no_match:
            The value to assign to the is_skip_no_match property of this Lookup.
        :type is_skip_no_match: bool

        :param multi_match_strategy:
            The value to assign to the multi_match_strategy property of this Lookup.
            Allowed values for this property are: "RETURN_ANY", "RETURN_FIRST", "RETURN_LAST", "RETURN_ALL", "RETURN_ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type multi_match_strategy: str

        :param null_fill_values:
            The value to assign to the null_fill_values property of this Lookup.
        :type null_fill_values: dict(str, object)

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_version': 'int',
            'input_ports': 'list[InputPort]',
            'output_ports': 'list[TypedObject]',
            'object_status': 'int',
            'identifier': 'str',
            'parameters': 'list[Parameter]',
            'op_config_values': 'ConfigValues',
            'lookup_condition': 'Expression',
            'is_skip_no_match': 'bool',
            'multi_match_strategy': 'str',
            'null_fill_values': 'dict(str, object)'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_version': 'objectVersion',
            'input_ports': 'inputPorts',
            'output_ports': 'outputPorts',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'parameters': 'parameters',
            'op_config_values': 'opConfigValues',
            'lookup_condition': 'lookupCondition',
            'is_skip_no_match': 'isSkipNoMatch',
            'multi_match_strategy': 'multiMatchStrategy',
            'null_fill_values': 'nullFillValues'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_version = None
        self._input_ports = None
        self._output_ports = None
        self._object_status = None
        self._identifier = None
        self._parameters = None
        self._op_config_values = None
        self._lookup_condition = None
        self._is_skip_no_match = None
        self._multi_match_strategy = None
        self._null_fill_values = None
        self._model_type = 'LOOKUP_OPERATOR'

    @property
    def lookup_condition(self):
        """
        Gets the lookup_condition of this Lookup.

        :return: The lookup_condition of this Lookup.
        :rtype: oci.data_integration.models.Expression
        """
        return self._lookup_condition

    @lookup_condition.setter
    def lookup_condition(self, lookup_condition):
        """
        Sets the lookup_condition of this Lookup.

        :param lookup_condition: The lookup_condition of this Lookup.
        :type: oci.data_integration.models.Expression
        """
        self._lookup_condition = lookup_condition

    @property
    def is_skip_no_match(self):
        """
        Gets the is_skip_no_match of this Lookup.
        For the rows for which lookup condition does not satisfy, if set to true - do not return those rows of primary Input source and if set to false - create a row with primary input fields values and lookup field values as NULL.


        :return: The is_skip_no_match of this Lookup.
        :rtype: bool
        """
        return self._is_skip_no_match

    @is_skip_no_match.setter
    def is_skip_no_match(self, is_skip_no_match):
        """
        Sets the is_skip_no_match of this Lookup.
        For the rows for which lookup condition does not satisfy, if set to true - do not return those rows of primary Input source and if set to false - create a row with primary input fields values and lookup field values as NULL.


        :param is_skip_no_match: The is_skip_no_match of this Lookup.
        :type: bool
        """
        self._is_skip_no_match = is_skip_no_match

    @property
    def multi_match_strategy(self):
        """
        Gets the multi_match_strategy of this Lookup.
        if there are multiple records found in the lookup input what action should be performed. The default value for this field is RETURN_ANY.

        Allowed values for this property are: "RETURN_ANY", "RETURN_FIRST", "RETURN_LAST", "RETURN_ALL", "RETURN_ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The multi_match_strategy of this Lookup.
        :rtype: str
        """
        return self._multi_match_strategy

    @multi_match_strategy.setter
    def multi_match_strategy(self, multi_match_strategy):
        """
        Sets the multi_match_strategy of this Lookup.
        if there are multiple records found in the lookup input what action should be performed. The default value for this field is RETURN_ANY.


        :param multi_match_strategy: The multi_match_strategy of this Lookup.
        :type: str
        """
        allowed_values = ["RETURN_ANY", "RETURN_FIRST", "RETURN_LAST", "RETURN_ALL", "RETURN_ERROR"]
        if not value_allowed_none_or_none_sentinel(multi_match_strategy, allowed_values):
            multi_match_strategy = 'UNKNOWN_ENUM_VALUE'
        self._multi_match_strategy = multi_match_strategy

    @property
    def null_fill_values(self):
        """
        Gets the null_fill_values of this Lookup.
        this map is used for replacing NULL values in the record. Key is the column name and value is the NULL replacement.


        :return: The null_fill_values of this Lookup.
        :rtype: dict(str, object)
        """
        return self._null_fill_values

    @null_fill_values.setter
    def null_fill_values(self, null_fill_values):
        """
        Sets the null_fill_values of this Lookup.
        this map is used for replacing NULL values in the record. Key is the column name and value is the NULL replacement.


        :param null_fill_values: The null_fill_values of this Lookup.
        :type: dict(str, object)
        """
        self._null_fill_values = null_fill_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
