# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .operator import Operator
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExpressionOperator(Operator):
    """
    An operator for expressions
    """

    #: A constant which can be used with the trigger_rule property of a ExpressionOperator.
    #: This constant has a value of "ALL_SUCCESS"
    TRIGGER_RULE_ALL_SUCCESS = "ALL_SUCCESS"

    #: A constant which can be used with the trigger_rule property of a ExpressionOperator.
    #: This constant has a value of "ALL_FAILED"
    TRIGGER_RULE_ALL_FAILED = "ALL_FAILED"

    #: A constant which can be used with the trigger_rule property of a ExpressionOperator.
    #: This constant has a value of "ALL_COMPLETE"
    TRIGGER_RULE_ALL_COMPLETE = "ALL_COMPLETE"

    def __init__(self, **kwargs):
        """
        Initializes a new ExpressionOperator object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.ExpressionOperator.model_type` attribute
        of this class is ``EXPRESSION_OPERATOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this ExpressionOperator.
            Allowed values for this property are: "SOURCE_OPERATOR", "FILTER_OPERATOR", "JOINER_OPERATOR", "AGGREGATOR_OPERATOR", "PROJECTION_OPERATOR", "TARGET_OPERATOR", "DISTINCT_OPERATOR", "SORT_OPERATOR", "UNION_OPERATOR", "INTERSECT_OPERATOR", "MINUS_OPERATOR", "MERGE_OPERATOR", "START_OPERATOR", "END_OPERATOR", "PIPELINE_OPERATOR", "TASK_OPERATOR", "EXPRESSION_OPERATOR", "LOOKUP_OPERATOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this ExpressionOperator.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this ExpressionOperator.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this ExpressionOperator.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this ExpressionOperator.
        :type name: str

        :param description:
            The value to assign to the description property of this ExpressionOperator.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this ExpressionOperator.
        :type object_version: int

        :param input_ports:
            The value to assign to the input_ports property of this ExpressionOperator.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this ExpressionOperator.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param object_status:
            The value to assign to the object_status property of this ExpressionOperator.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this ExpressionOperator.
        :type identifier: str

        :param parameters:
            The value to assign to the parameters property of this ExpressionOperator.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this ExpressionOperator.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param trigger_rule:
            The value to assign to the trigger_rule property of this ExpressionOperator.
            Allowed values for this property are: "ALL_SUCCESS", "ALL_FAILED", "ALL_COMPLETE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type trigger_rule: str

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this ExpressionOperator.
        :type config_provider_delegate: oci.data_integration.models.ConfigProvider

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
            'output_ports': 'list[OutputPort]',
            'object_status': 'int',
            'identifier': 'str',
            'parameters': 'list[Parameter]',
            'op_config_values': 'ConfigValues',
            'trigger_rule': 'str',
            'config_provider_delegate': 'ConfigProvider'
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
            'trigger_rule': 'triggerRule',
            'config_provider_delegate': 'configProviderDelegate'
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
        self._config_provider_delegate = None
        self._model_type = 'EXPRESSION_OPERATOR'

    @property
    def trigger_rule(self):
        """
        Gets the trigger_rule of this ExpressionOperator.
        The merge condition. The conditions are
        ALL_SUCCESS - All the preceeding operators need to be successful.
        ALL_FAILED - All the preceeding operators should have failed.
        ALL_COMPLETE - All the preceeding operators should have completed. It could have executed successfully or failed.

        Allowed values for this property are: "ALL_SUCCESS", "ALL_FAILED", "ALL_COMPLETE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The trigger_rule of this ExpressionOperator.
        :rtype: str
        """
        return self._trigger_rule

    @trigger_rule.setter
    def trigger_rule(self, trigger_rule):
        """
        Sets the trigger_rule of this ExpressionOperator.
        The merge condition. The conditions are
        ALL_SUCCESS - All the preceeding operators need to be successful.
        ALL_FAILED - All the preceeding operators should have failed.
        ALL_COMPLETE - All the preceeding operators should have completed. It could have executed successfully or failed.


        :param trigger_rule: The trigger_rule of this ExpressionOperator.
        :type: str
        """
        allowed_values = ["ALL_SUCCESS", "ALL_FAILED", "ALL_COMPLETE"]
        if not value_allowed_none_or_none_sentinel(trigger_rule, allowed_values):
            trigger_rule = 'UNKNOWN_ENUM_VALUE'
        self._trigger_rule = trigger_rule

    @property
    def config_provider_delegate(self):
        """
        Gets the config_provider_delegate of this ExpressionOperator.

        :return: The config_provider_delegate of this ExpressionOperator.
        :rtype: oci.data_integration.models.ConfigProvider
        """
        return self._config_provider_delegate

    @config_provider_delegate.setter
    def config_provider_delegate(self, config_provider_delegate):
        """
        Sets the config_provider_delegate of this ExpressionOperator.

        :param config_provider_delegate: The config_provider_delegate of this ExpressionOperator.
        :type: oci.data_integration.models.ConfigProvider
        """
        self._config_provider_delegate = config_provider_delegate

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other