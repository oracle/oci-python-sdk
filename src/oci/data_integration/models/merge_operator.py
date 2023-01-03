# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .operator import Operator
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MergeOperator(Operator):
    """
    Represents the start of a pipeline.
    """

    #: A constant which can be used with the trigger_rule property of a MergeOperator.
    #: This constant has a value of "ALL_SUCCESS"
    TRIGGER_RULE_ALL_SUCCESS = "ALL_SUCCESS"

    #: A constant which can be used with the trigger_rule property of a MergeOperator.
    #: This constant has a value of "ALL_FAILED"
    TRIGGER_RULE_ALL_FAILED = "ALL_FAILED"

    #: A constant which can be used with the trigger_rule property of a MergeOperator.
    #: This constant has a value of "ALL_COMPLETE"
    TRIGGER_RULE_ALL_COMPLETE = "ALL_COMPLETE"

    #: A constant which can be used with the trigger_rule property of a MergeOperator.
    #: This constant has a value of "ONE_SUCCESS"
    TRIGGER_RULE_ONE_SUCCESS = "ONE_SUCCESS"

    #: A constant which can be used with the trigger_rule property of a MergeOperator.
    #: This constant has a value of "ONE_FAILED"
    TRIGGER_RULE_ONE_FAILED = "ONE_FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new MergeOperator object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.MergeOperator.model_type` attribute
        of this class is ``MERGE_OPERATOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this MergeOperator.
            Allowed values for this property are: "SOURCE_OPERATOR", "FILTER_OPERATOR", "JOINER_OPERATOR", "AGGREGATOR_OPERATOR", "PROJECTION_OPERATOR", "TARGET_OPERATOR", "FLATTEN_OPERATOR", "DISTINCT_OPERATOR", "SORT_OPERATOR", "UNION_OPERATOR", "INTERSECT_OPERATOR", "MINUS_OPERATOR", "MERGE_OPERATOR", "FUNCTION_OPERATOR", "SPLIT_OPERATOR", "START_OPERATOR", "END_OPERATOR", "PIPELINE_OPERATOR", "DECISION_OPERATOR", "TASK_OPERATOR", "EXPRESSION_OPERATOR", "LOOKUP_OPERATOR", "PIVOT_OPERATOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this MergeOperator.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this MergeOperator.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this MergeOperator.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this MergeOperator.
        :type name: str

        :param description:
            The value to assign to the description property of this MergeOperator.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this MergeOperator.
        :type object_version: int

        :param input_ports:
            The value to assign to the input_ports property of this MergeOperator.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this MergeOperator.
        :type output_ports: list[oci.data_integration.models.TypedObject]

        :param object_status:
            The value to assign to the object_status property of this MergeOperator.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this MergeOperator.
        :type identifier: str

        :param parameters:
            The value to assign to the parameters property of this MergeOperator.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this MergeOperator.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param trigger_rule:
            The value to assign to the trigger_rule property of this MergeOperator.
            Allowed values for this property are: "ALL_SUCCESS", "ALL_FAILED", "ALL_COMPLETE", "ONE_SUCCESS", "ONE_FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type trigger_rule: str

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
            'trigger_rule': 'str'
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
            'trigger_rule': 'triggerRule'
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
        self._trigger_rule = None
        self._model_type = 'MERGE_OPERATOR'

    @property
    def trigger_rule(self):
        """
        Gets the trigger_rule of this MergeOperator.
        The merge condition. The conditions are
        ALL_SUCCESS - All the preceeding operators need to be successful.
        ALL_FAILED - All the preceeding operators should have failed.
        ALL_COMPLETE - All the preceeding operators should have completed. It could have executed successfully or failed.
        ONE_SUCCESS - Atleast one of the preceeding operators should have succeeded.
        ONE_FAILED - Atleast one of the preceeding operators should have failed.

        Allowed values for this property are: "ALL_SUCCESS", "ALL_FAILED", "ALL_COMPLETE", "ONE_SUCCESS", "ONE_FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The trigger_rule of this MergeOperator.
        :rtype: str
        """
        return self._trigger_rule

    @trigger_rule.setter
    def trigger_rule(self, trigger_rule):
        """
        Sets the trigger_rule of this MergeOperator.
        The merge condition. The conditions are
        ALL_SUCCESS - All the preceeding operators need to be successful.
        ALL_FAILED - All the preceeding operators should have failed.
        ALL_COMPLETE - All the preceeding operators should have completed. It could have executed successfully or failed.
        ONE_SUCCESS - Atleast one of the preceeding operators should have succeeded.
        ONE_FAILED - Atleast one of the preceeding operators should have failed.


        :param trigger_rule: The trigger_rule of this MergeOperator.
        :type: str
        """
        allowed_values = ["ALL_SUCCESS", "ALL_FAILED", "ALL_COMPLETE", "ONE_SUCCESS", "ONE_FAILED"]
        if not value_allowed_none_or_none_sentinel(trigger_rule, allowed_values):
            trigger_rule = 'UNKNOWN_ENUM_VALUE'
        self._trigger_rule = trigger_rule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
