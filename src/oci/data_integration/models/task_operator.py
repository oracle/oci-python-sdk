# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .operator import Operator
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TaskOperator(Operator):
    """
    An operator for task
    """

    #: A constant which can be used with the retry_delay_unit property of a TaskOperator.
    #: This constant has a value of "SECONDS"
    RETRY_DELAY_UNIT_SECONDS = "SECONDS"

    #: A constant which can be used with the retry_delay_unit property of a TaskOperator.
    #: This constant has a value of "MINUTES"
    RETRY_DELAY_UNIT_MINUTES = "MINUTES"

    #: A constant which can be used with the retry_delay_unit property of a TaskOperator.
    #: This constant has a value of "HOURS"
    RETRY_DELAY_UNIT_HOURS = "HOURS"

    #: A constant which can be used with the retry_delay_unit property of a TaskOperator.
    #: This constant has a value of "DAYS"
    RETRY_DELAY_UNIT_DAYS = "DAYS"

    #: A constant which can be used with the expected_duration_unit property of a TaskOperator.
    #: This constant has a value of "SECONDS"
    EXPECTED_DURATION_UNIT_SECONDS = "SECONDS"

    #: A constant which can be used with the expected_duration_unit property of a TaskOperator.
    #: This constant has a value of "MINUTES"
    EXPECTED_DURATION_UNIT_MINUTES = "MINUTES"

    #: A constant which can be used with the expected_duration_unit property of a TaskOperator.
    #: This constant has a value of "HOURS"
    EXPECTED_DURATION_UNIT_HOURS = "HOURS"

    #: A constant which can be used with the expected_duration_unit property of a TaskOperator.
    #: This constant has a value of "DAYS"
    EXPECTED_DURATION_UNIT_DAYS = "DAYS"

    #: A constant which can be used with the task_type property of a TaskOperator.
    #: This constant has a value of "PIPELINE_TASK"
    TASK_TYPE_PIPELINE_TASK = "PIPELINE_TASK"

    #: A constant which can be used with the task_type property of a TaskOperator.
    #: This constant has a value of "INTEGRATION_TASK"
    TASK_TYPE_INTEGRATION_TASK = "INTEGRATION_TASK"

    #: A constant which can be used with the task_type property of a TaskOperator.
    #: This constant has a value of "DATA_LOADER_TASK"
    TASK_TYPE_DATA_LOADER_TASK = "DATA_LOADER_TASK"

    #: A constant which can be used with the trigger_rule property of a TaskOperator.
    #: This constant has a value of "ALL_SUCCESS"
    TRIGGER_RULE_ALL_SUCCESS = "ALL_SUCCESS"

    #: A constant which can be used with the trigger_rule property of a TaskOperator.
    #: This constant has a value of "ALL_FAILED"
    TRIGGER_RULE_ALL_FAILED = "ALL_FAILED"

    #: A constant which can be used with the trigger_rule property of a TaskOperator.
    #: This constant has a value of "ALL_COMPLETE"
    TRIGGER_RULE_ALL_COMPLETE = "ALL_COMPLETE"

    def __init__(self, **kwargs):
        """
        Initializes a new TaskOperator object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.TaskOperator.model_type` attribute
        of this class is ``TASK_OPERATOR`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this TaskOperator.
            Allowed values for this property are: "SOURCE_OPERATOR", "FILTER_OPERATOR", "JOINER_OPERATOR", "AGGREGATOR_OPERATOR", "PROJECTION_OPERATOR", "TARGET_OPERATOR", "DISTINCT_OPERATOR", "SORT_OPERATOR", "UNION_OPERATOR", "INTERSECT_OPERATOR", "MINUS_OPERATOR", "MERGE_OPERATOR", "START_OPERATOR", "END_OPERATOR", "PIPELINE_OPERATOR", "REST_OPERATOR", "TASK_OPERATOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this TaskOperator.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this TaskOperator.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this TaskOperator.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this TaskOperator.
        :type name: str

        :param description:
            The value to assign to the description property of this TaskOperator.
        :type description: str

        :param object_version:
            The value to assign to the object_version property of this TaskOperator.
        :type object_version: int

        :param input_ports:
            The value to assign to the input_ports property of this TaskOperator.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this TaskOperator.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param object_status:
            The value to assign to the object_status property of this TaskOperator.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this TaskOperator.
        :type identifier: str

        :param parameters:
            The value to assign to the parameters property of this TaskOperator.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this TaskOperator.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param retry_attempts:
            The value to assign to the retry_attempts property of this TaskOperator.
        :type retry_attempts: int

        :param retry_delay_unit:
            The value to assign to the retry_delay_unit property of this TaskOperator.
            Allowed values for this property are: "SECONDS", "MINUTES", "HOURS", "DAYS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type retry_delay_unit: str

        :param retry_delay:
            The value to assign to the retry_delay property of this TaskOperator.
        :type retry_delay: float

        :param expected_duration:
            The value to assign to the expected_duration property of this TaskOperator.
        :type expected_duration: float

        :param expected_duration_unit:
            The value to assign to the expected_duration_unit property of this TaskOperator.
            Allowed values for this property are: "SECONDS", "MINUTES", "HOURS", "DAYS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type expected_duration_unit: str

        :param task_type:
            The value to assign to the task_type property of this TaskOperator.
            Allowed values for this property are: "PIPELINE_TASK", "INTEGRATION_TASK", "DATA_LOADER_TASK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type task_type: str

        :param task:
            The value to assign to the task property of this TaskOperator.
        :type task: oci.data_integration.models.Task

        :param trigger_rule:
            The value to assign to the trigger_rule property of this TaskOperator.
            Allowed values for this property are: "ALL_SUCCESS", "ALL_FAILED", "ALL_COMPLETE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type trigger_rule: str

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this TaskOperator.
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
            'retry_attempts': 'int',
            'retry_delay_unit': 'str',
            'retry_delay': 'float',
            'expected_duration': 'float',
            'expected_duration_unit': 'str',
            'task_type': 'str',
            'task': 'Task',
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
            'retry_attempts': 'retryAttempts',
            'retry_delay_unit': 'retryDelayUnit',
            'retry_delay': 'retryDelay',
            'expected_duration': 'expectedDuration',
            'expected_duration_unit': 'expectedDurationUnit',
            'task_type': 'taskType',
            'task': 'task',
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
        self._retry_attempts = None
        self._retry_delay_unit = None
        self._retry_delay = None
        self._expected_duration = None
        self._expected_duration_unit = None
        self._task_type = None
        self._task = None
        self._trigger_rule = None
        self._config_provider_delegate = None
        self._model_type = 'TASK_OPERATOR'

    @property
    def retry_attempts(self):
        """
        Gets the retry_attempts of this TaskOperator.
        The number of retry attempts.


        :return: The retry_attempts of this TaskOperator.
        :rtype: int
        """
        return self._retry_attempts

    @retry_attempts.setter
    def retry_attempts(self, retry_attempts):
        """
        Sets the retry_attempts of this TaskOperator.
        The number of retry attempts.


        :param retry_attempts: The retry_attempts of this TaskOperator.
        :type: int
        """
        self._retry_attempts = retry_attempts

    @property
    def retry_delay_unit(self):
        """
        Gets the retry_delay_unit of this TaskOperator.
        The unit for the retry delay.

        Allowed values for this property are: "SECONDS", "MINUTES", "HOURS", "DAYS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The retry_delay_unit of this TaskOperator.
        :rtype: str
        """
        return self._retry_delay_unit

    @retry_delay_unit.setter
    def retry_delay_unit(self, retry_delay_unit):
        """
        Sets the retry_delay_unit of this TaskOperator.
        The unit for the retry delay.


        :param retry_delay_unit: The retry_delay_unit of this TaskOperator.
        :type: str
        """
        allowed_values = ["SECONDS", "MINUTES", "HOURS", "DAYS"]
        if not value_allowed_none_or_none_sentinel(retry_delay_unit, allowed_values):
            retry_delay_unit = 'UNKNOWN_ENUM_VALUE'
        self._retry_delay_unit = retry_delay_unit

    @property
    def retry_delay(self):
        """
        Gets the retry_delay of this TaskOperator.
        The retry delay, the unit for measurement is in the property retry delay unit.


        :return: The retry_delay of this TaskOperator.
        :rtype: float
        """
        return self._retry_delay

    @retry_delay.setter
    def retry_delay(self, retry_delay):
        """
        Sets the retry_delay of this TaskOperator.
        The retry delay, the unit for measurement is in the property retry delay unit.


        :param retry_delay: The retry_delay of this TaskOperator.
        :type: float
        """
        self._retry_delay = retry_delay

    @property
    def expected_duration(self):
        """
        Gets the expected_duration of this TaskOperator.
        The expected duration for the task run.


        :return: The expected_duration of this TaskOperator.
        :rtype: float
        """
        return self._expected_duration

    @expected_duration.setter
    def expected_duration(self, expected_duration):
        """
        Sets the expected_duration of this TaskOperator.
        The expected duration for the task run.


        :param expected_duration: The expected_duration of this TaskOperator.
        :type: float
        """
        self._expected_duration = expected_duration

    @property
    def expected_duration_unit(self):
        """
        Gets the expected_duration_unit of this TaskOperator.
        The expected duration unit of measure.

        Allowed values for this property are: "SECONDS", "MINUTES", "HOURS", "DAYS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The expected_duration_unit of this TaskOperator.
        :rtype: str
        """
        return self._expected_duration_unit

    @expected_duration_unit.setter
    def expected_duration_unit(self, expected_duration_unit):
        """
        Sets the expected_duration_unit of this TaskOperator.
        The expected duration unit of measure.


        :param expected_duration_unit: The expected_duration_unit of this TaskOperator.
        :type: str
        """
        allowed_values = ["SECONDS", "MINUTES", "HOURS", "DAYS"]
        if not value_allowed_none_or_none_sentinel(expected_duration_unit, allowed_values):
            expected_duration_unit = 'UNKNOWN_ENUM_VALUE'
        self._expected_duration_unit = expected_duration_unit

    @property
    def task_type(self):
        """
        Gets the task_type of this TaskOperator.
        The type of the task referenced in the task property.

        Allowed values for this property are: "PIPELINE_TASK", "INTEGRATION_TASK", "DATA_LOADER_TASK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The task_type of this TaskOperator.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """
        Sets the task_type of this TaskOperator.
        The type of the task referenced in the task property.


        :param task_type: The task_type of this TaskOperator.
        :type: str
        """
        allowed_values = ["PIPELINE_TASK", "INTEGRATION_TASK", "DATA_LOADER_TASK"]
        if not value_allowed_none_or_none_sentinel(task_type, allowed_values):
            task_type = 'UNKNOWN_ENUM_VALUE'
        self._task_type = task_type

    @property
    def task(self):
        """
        Gets the task of this TaskOperator.

        :return: The task of this TaskOperator.
        :rtype: oci.data_integration.models.Task
        """
        return self._task

    @task.setter
    def task(self, task):
        """
        Sets the task of this TaskOperator.

        :param task: The task of this TaskOperator.
        :type: oci.data_integration.models.Task
        """
        self._task = task

    @property
    def trigger_rule(self):
        """
        Gets the trigger_rule of this TaskOperator.
        The merge condition. The conditions are
        ALL_SUCCESS - All the preceeding operators need to be successful.
        ALL_FAILED - All the preceeding operators should have failed.
        ALL_COMPLETE - All the preceeding operators should have completed. It could have executed successfully or failed.

        Allowed values for this property are: "ALL_SUCCESS", "ALL_FAILED", "ALL_COMPLETE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The trigger_rule of this TaskOperator.
        :rtype: str
        """
        return self._trigger_rule

    @trigger_rule.setter
    def trigger_rule(self, trigger_rule):
        """
        Sets the trigger_rule of this TaskOperator.
        The merge condition. The conditions are
        ALL_SUCCESS - All the preceeding operators need to be successful.
        ALL_FAILED - All the preceeding operators should have failed.
        ALL_COMPLETE - All the preceeding operators should have completed. It could have executed successfully or failed.


        :param trigger_rule: The trigger_rule of this TaskOperator.
        :type: str
        """
        allowed_values = ["ALL_SUCCESS", "ALL_FAILED", "ALL_COMPLETE"]
        if not value_allowed_none_or_none_sentinel(trigger_rule, allowed_values):
            trigger_rule = 'UNKNOWN_ENUM_VALUE'
        self._trigger_rule = trigger_rule

    @property
    def config_provider_delegate(self):
        """
        Gets the config_provider_delegate of this TaskOperator.

        :return: The config_provider_delegate of this TaskOperator.
        :rtype: oci.data_integration.models.ConfigProvider
        """
        return self._config_provider_delegate

    @config_provider_delegate.setter
    def config_provider_delegate(self, config_provider_delegate):
        """
        Sets the config_provider_delegate of this TaskOperator.

        :param config_provider_delegate: The config_provider_delegate of this TaskOperator.
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
