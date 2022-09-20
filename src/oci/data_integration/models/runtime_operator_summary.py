# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RuntimeOperatorSummary(object):
    """
    The information about RuntimeOperator.
    """

    #: A constant which can be used with the status property of a RuntimeOperatorSummary.
    #: This constant has a value of "NOT_STARTED"
    STATUS_NOT_STARTED = "NOT_STARTED"

    #: A constant which can be used with the status property of a RuntimeOperatorSummary.
    #: This constant has a value of "QUEUED"
    STATUS_QUEUED = "QUEUED"

    #: A constant which can be used with the status property of a RuntimeOperatorSummary.
    #: This constant has a value of "RUNNING"
    STATUS_RUNNING = "RUNNING"

    #: A constant which can be used with the status property of a RuntimeOperatorSummary.
    #: This constant has a value of "TERMINATING"
    STATUS_TERMINATING = "TERMINATING"

    #: A constant which can be used with the status property of a RuntimeOperatorSummary.
    #: This constant has a value of "TERMINATED"
    STATUS_TERMINATED = "TERMINATED"

    #: A constant which can be used with the status property of a RuntimeOperatorSummary.
    #: This constant has a value of "SUCCESS"
    STATUS_SUCCESS = "SUCCESS"

    #: A constant which can be used with the status property of a RuntimeOperatorSummary.
    #: This constant has a value of "ERROR"
    STATUS_ERROR = "ERROR"

    #: A constant which can be used with the execution_state property of a RuntimeOperatorSummary.
    #: This constant has a value of "NOT_STARTED"
    EXECUTION_STATE_NOT_STARTED = "NOT_STARTED"

    #: A constant which can be used with the execution_state property of a RuntimeOperatorSummary.
    #: This constant has a value of "RUNNING"
    EXECUTION_STATE_RUNNING = "RUNNING"

    #: A constant which can be used with the execution_state property of a RuntimeOperatorSummary.
    #: This constant has a value of "TERMINATED"
    EXECUTION_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the execution_state property of a RuntimeOperatorSummary.
    #: This constant has a value of "SUCCESS"
    EXECUTION_STATE_SUCCESS = "SUCCESS"

    #: A constant which can be used with the execution_state property of a RuntimeOperatorSummary.
    #: This constant has a value of "ERROR"
    EXECUTION_STATE_ERROR = "ERROR"

    #: A constant which can be used with the execution_state property of a RuntimeOperatorSummary.
    #: This constant has a value of "SKIPPED"
    EXECUTION_STATE_SKIPPED = "SKIPPED"

    #: A constant which can be used with the execution_state property of a RuntimeOperatorSummary.
    #: This constant has a value of "UNKNOWN"
    EXECUTION_STATE_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new RuntimeOperatorSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param task_run_key:
            The value to assign to the task_run_key property of this RuntimeOperatorSummary.
        :type task_run_key: str

        :param start_time_in_millis:
            The value to assign to the start_time_in_millis property of this RuntimeOperatorSummary.
        :type start_time_in_millis: int

        :param end_time_in_millis:
            The value to assign to the end_time_in_millis property of this RuntimeOperatorSummary.
        :type end_time_in_millis: int

        :param status:
            The value to assign to the status property of this RuntimeOperatorSummary.
            Allowed values for this property are: "NOT_STARTED", "QUEUED", "RUNNING", "TERMINATING", "TERMINATED", "SUCCESS", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param execution_state:
            The value to assign to the execution_state property of this RuntimeOperatorSummary.
            Allowed values for this property are: "NOT_STARTED", "RUNNING", "TERMINATED", "SUCCESS", "ERROR", "SKIPPED", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type execution_state: str

        :param parameters:
            The value to assign to the parameters property of this RuntimeOperatorSummary.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param inputs:
            The value to assign to the inputs property of this RuntimeOperatorSummary.
        :type inputs: dict(str, ParameterValue)

        :param outputs:
            The value to assign to the outputs property of this RuntimeOperatorSummary.
        :type outputs: dict(str, ParameterValue)

        :param metrics:
            The value to assign to the metrics property of this RuntimeOperatorSummary.
        :type metrics: dict(str, float)

        """
        self.swagger_types = {
            'task_run_key': 'str',
            'start_time_in_millis': 'int',
            'end_time_in_millis': 'int',
            'status': 'str',
            'execution_state': 'str',
            'parameters': 'list[Parameter]',
            'inputs': 'dict(str, ParameterValue)',
            'outputs': 'dict(str, ParameterValue)',
            'metrics': 'dict(str, float)'
        }

        self.attribute_map = {
            'task_run_key': 'taskRunKey',
            'start_time_in_millis': 'startTimeInMillis',
            'end_time_in_millis': 'endTimeInMillis',
            'status': 'status',
            'execution_state': 'executionState',
            'parameters': 'parameters',
            'inputs': 'inputs',
            'outputs': 'outputs',
            'metrics': 'metrics'
        }

        self._task_run_key = None
        self._start_time_in_millis = None
        self._end_time_in_millis = None
        self._status = None
        self._execution_state = None
        self._parameters = None
        self._inputs = None
        self._outputs = None
        self._metrics = None

    @property
    def task_run_key(self):
        """
        Gets the task_run_key of this RuntimeOperatorSummary.
        The TaskRun key.


        :return: The task_run_key of this RuntimeOperatorSummary.
        :rtype: str
        """
        return self._task_run_key

    @task_run_key.setter
    def task_run_key(self, task_run_key):
        """
        Sets the task_run_key of this RuntimeOperatorSummary.
        The TaskRun key.


        :param task_run_key: The task_run_key of this RuntimeOperatorSummary.
        :type: str
        """
        self._task_run_key = task_run_key

    @property
    def start_time_in_millis(self):
        """
        Gets the start_time_in_millis of this RuntimeOperatorSummary.
        The runtime operator start time.


        :return: The start_time_in_millis of this RuntimeOperatorSummary.
        :rtype: int
        """
        return self._start_time_in_millis

    @start_time_in_millis.setter
    def start_time_in_millis(self, start_time_in_millis):
        """
        Sets the start_time_in_millis of this RuntimeOperatorSummary.
        The runtime operator start time.


        :param start_time_in_millis: The start_time_in_millis of this RuntimeOperatorSummary.
        :type: int
        """
        self._start_time_in_millis = start_time_in_millis

    @property
    def end_time_in_millis(self):
        """
        Gets the end_time_in_millis of this RuntimeOperatorSummary.
        The runtime operator end time.


        :return: The end_time_in_millis of this RuntimeOperatorSummary.
        :rtype: int
        """
        return self._end_time_in_millis

    @end_time_in_millis.setter
    def end_time_in_millis(self, end_time_in_millis):
        """
        Sets the end_time_in_millis of this RuntimeOperatorSummary.
        The runtime operator end time.


        :param end_time_in_millis: The end_time_in_millis of this RuntimeOperatorSummary.
        :type: int
        """
        self._end_time_in_millis = end_time_in_millis

    @property
    def status(self):
        """
        Gets the status of this RuntimeOperatorSummary.
        status

        Allowed values for this property are: "NOT_STARTED", "QUEUED", "RUNNING", "TERMINATING", "TERMINATED", "SUCCESS", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this RuntimeOperatorSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this RuntimeOperatorSummary.
        status


        :param status: The status of this RuntimeOperatorSummary.
        :type: str
        """
        allowed_values = ["NOT_STARTED", "QUEUED", "RUNNING", "TERMINATING", "TERMINATED", "SUCCESS", "ERROR"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def execution_state(self):
        """
        Gets the execution_state of this RuntimeOperatorSummary.
        status

        Allowed values for this property are: "NOT_STARTED", "RUNNING", "TERMINATED", "SUCCESS", "ERROR", "SKIPPED", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The execution_state of this RuntimeOperatorSummary.
        :rtype: str
        """
        return self._execution_state

    @execution_state.setter
    def execution_state(self, execution_state):
        """
        Sets the execution_state of this RuntimeOperatorSummary.
        status


        :param execution_state: The execution_state of this RuntimeOperatorSummary.
        :type: str
        """
        allowed_values = ["NOT_STARTED", "RUNNING", "TERMINATED", "SUCCESS", "ERROR", "SKIPPED", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(execution_state, allowed_values):
            execution_state = 'UNKNOWN_ENUM_VALUE'
        self._execution_state = execution_state

    @property
    def parameters(self):
        """
        Gets the parameters of this RuntimeOperatorSummary.
        A list of parameters for the pipeline, this allows certain aspects of the pipeline to be configured when the pipeline is executed.


        :return: The parameters of this RuntimeOperatorSummary.
        :rtype: list[oci.data_integration.models.Parameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this RuntimeOperatorSummary.
        A list of parameters for the pipeline, this allows certain aspects of the pipeline to be configured when the pipeline is executed.


        :param parameters: The parameters of this RuntimeOperatorSummary.
        :type: list[oci.data_integration.models.Parameter]
        """
        self._parameters = parameters

    @property
    def inputs(self):
        """
        Gets the inputs of this RuntimeOperatorSummary.
        The configuration provider bindings.


        :return: The inputs of this RuntimeOperatorSummary.
        :rtype: dict(str, ParameterValue)
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """
        Sets the inputs of this RuntimeOperatorSummary.
        The configuration provider bindings.


        :param inputs: The inputs of this RuntimeOperatorSummary.
        :type: dict(str, ParameterValue)
        """
        self._inputs = inputs

    @property
    def outputs(self):
        """
        Gets the outputs of this RuntimeOperatorSummary.
        The configuration provider bindings.


        :return: The outputs of this RuntimeOperatorSummary.
        :rtype: dict(str, ParameterValue)
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """
        Sets the outputs of this RuntimeOperatorSummary.
        The configuration provider bindings.


        :param outputs: The outputs of this RuntimeOperatorSummary.
        :type: dict(str, ParameterValue)
        """
        self._outputs = outputs

    @property
    def metrics(self):
        """
        Gets the metrics of this RuntimeOperatorSummary.
        A map metrics for the task run.


        :return: The metrics of this RuntimeOperatorSummary.
        :rtype: dict(str, float)
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this RuntimeOperatorSummary.
        A map metrics for the task run.


        :param metrics: The metrics of this RuntimeOperatorSummary.
        :type: dict(str, float)
        """
        self._metrics = metrics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
