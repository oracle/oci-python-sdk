# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperationExecResult(object):
    """
    Operation execution result for a single input set.
    """

    #: A constant which can be used with the execution_status property of a OperationExecResult.
    #: This constant has a value of "FAILED"
    EXECUTION_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the execution_status property of a OperationExecResult.
    #: This constant has a value of "SUCCESS"
    EXECUTION_STATUS_SUCCESS = "SUCCESS"

    #: A constant which can be used with the execution_status property of a OperationExecResult.
    #: This constant has a value of "QUEUED"
    EXECUTION_STATUS_QUEUED = "QUEUED"

    #: A constant which can be used with the execution_status property of a OperationExecResult.
    #: This constant has a value of "RUNNING"
    EXECUTION_STATUS_RUNNING = "RUNNING"

    def __init__(self, **kwargs):
        """
        Initializes a new OperationExecResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param execution_status:
            The value to assign to the execution_status property of this OperationExecResult.
            Allowed values for this property are: "FAILED", "SUCCESS", "QUEUED", "RUNNING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type execution_status: str

        :param error_message:
            The value to assign to the error_message property of this OperationExecResult.
        :type error_message: str

        :param metrics:
            The value to assign to the metrics property of this OperationExecResult.
        :type metrics: object

        :param output_values:
            The value to assign to the output_values property of this OperationExecResult.
        :type output_values: list[list[object]]

        :param is_whitelisted_error_message:
            The value to assign to the is_whitelisted_error_message property of this OperationExecResult.
        :type is_whitelisted_error_message: bool

        """
        self.swagger_types = {
            'execution_status': 'str',
            'error_message': 'str',
            'metrics': 'object',
            'output_values': 'list[list[object]]',
            'is_whitelisted_error_message': 'bool'
        }

        self.attribute_map = {
            'execution_status': 'executionStatus',
            'error_message': 'errorMessage',
            'metrics': 'metrics',
            'output_values': 'outputValues',
            'is_whitelisted_error_message': 'isWhitelistedErrorMessage'
        }

        self._execution_status = None
        self._error_message = None
        self._metrics = None
        self._output_values = None
        self._is_whitelisted_error_message = None

    @property
    def execution_status(self):
        """
        Gets the execution_status of this OperationExecResult.
        Status of the operation job for particular set of input.

        Allowed values for this property are: "FAILED", "SUCCESS", "QUEUED", "RUNNING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The execution_status of this OperationExecResult.
        :rtype: str
        """
        return self._execution_status

    @execution_status.setter
    def execution_status(self, execution_status):
        """
        Sets the execution_status of this OperationExecResult.
        Status of the operation job for particular set of input.


        :param execution_status: The execution_status of this OperationExecResult.
        :type: str
        """
        allowed_values = ["FAILED", "SUCCESS", "QUEUED", "RUNNING"]
        if not value_allowed_none_or_none_sentinel(execution_status, allowed_values):
            execution_status = 'UNKNOWN_ENUM_VALUE'
        self._execution_status = execution_status

    @property
    def error_message(self):
        """
        Gets the error_message of this OperationExecResult.
        Error message if execution of operation is failed.


        :return: The error_message of this OperationExecResult.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this OperationExecResult.
        Error message if execution of operation is failed.


        :param error_message: The error_message of this OperationExecResult.
        :type: str
        """
        self._error_message = error_message

    @property
    def metrics(self):
        """
        Gets the metrics of this OperationExecResult.
        Metrics of operation execution job.


        :return: The metrics of this OperationExecResult.
        :rtype: object
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this OperationExecResult.
        Metrics of operation execution job.


        :param metrics: The metrics of this OperationExecResult.
        :type: object
        """
        self._metrics = metrics

    @property
    def output_values(self):
        """
        Gets the output_values of this OperationExecResult.
        List of emitted rows for each OUT/INOUT param.


        :return: The output_values of this OperationExecResult.
        :rtype: list[list[object]]
        """
        return self._output_values

    @output_values.setter
    def output_values(self, output_values):
        """
        Sets the output_values of this OperationExecResult.
        List of emitted rows for each OUT/INOUT param.


        :param output_values: The output_values of this OperationExecResult.
        :type: list[list[object]]
        """
        self._output_values = output_values

    @property
    def is_whitelisted_error_message(self):
        """
        Gets the is_whitelisted_error_message of this OperationExecResult.
        True, if error message should be displayed on UI.


        :return: The is_whitelisted_error_message of this OperationExecResult.
        :rtype: bool
        """
        return self._is_whitelisted_error_message

    @is_whitelisted_error_message.setter
    def is_whitelisted_error_message(self, is_whitelisted_error_message):
        """
        Sets the is_whitelisted_error_message of this OperationExecResult.
        True, if error message should be displayed on UI.


        :param is_whitelisted_error_message: The is_whitelisted_error_message of this OperationExecResult.
        :type: bool
        """
        self._is_whitelisted_error_message = is_whitelisted_error_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
