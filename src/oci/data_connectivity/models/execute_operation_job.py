# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExecuteOperationJob(object):
    """
    Response of executeOperationJob.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExecuteOperationJob object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation_status:
            The value to assign to the operation_status property of this ExecuteOperationJob.
        :type operation_status: str

        :param error_message:
            The value to assign to the error_message property of this ExecuteOperationJob.
        :type error_message: str

        :param operation_name:
            The value to assign to the operation_name property of this ExecuteOperationJob.
        :type operation_name: str

        :param out_params:
            The value to assign to the out_params property of this ExecuteOperationJob.
        :type out_params: list[str]

        :param operation_result:
            The value to assign to the operation_result property of this ExecuteOperationJob.
        :type operation_result: list[oci.data_connectivity.models.OperationExecResult]

        """
        self.swagger_types = {
            'operation_status': 'str',
            'error_message': 'str',
            'operation_name': 'str',
            'out_params': 'list[str]',
            'operation_result': 'list[OperationExecResult]'
        }

        self.attribute_map = {
            'operation_status': 'operationStatus',
            'error_message': 'errorMessage',
            'operation_name': 'operationName',
            'out_params': 'outParams',
            'operation_result': 'operationResult'
        }

        self._operation_status = None
        self._error_message = None
        self._operation_name = None
        self._out_params = None
        self._operation_result = None

    @property
    def operation_status(self):
        """
        **[Required]** Gets the operation_status of this ExecuteOperationJob.
        Status of the operation job for all sets of input.


        :return: The operation_status of this ExecuteOperationJob.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        """
        Sets the operation_status of this ExecuteOperationJob.
        Status of the operation job for all sets of input.


        :param operation_status: The operation_status of this ExecuteOperationJob.
        :type: str
        """
        self._operation_status = operation_status

    @property
    def error_message(self):
        """
        Gets the error_message of this ExecuteOperationJob.
        Error message, if whole operation is failed.


        :return: The error_message of this ExecuteOperationJob.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ExecuteOperationJob.
        Error message, if whole operation is failed.


        :param error_message: The error_message of this ExecuteOperationJob.
        :type: str
        """
        self._error_message = error_message

    @property
    def operation_name(self):
        """
        Gets the operation_name of this ExecuteOperationJob.
        Name of the operation.


        :return: The operation_name of this ExecuteOperationJob.
        :rtype: str
        """
        return self._operation_name

    @operation_name.setter
    def operation_name(self, operation_name):
        """
        Sets the operation_name of this ExecuteOperationJob.
        Name of the operation.


        :param operation_name: The operation_name of this ExecuteOperationJob.
        :type: str
        """
        self._operation_name = operation_name

    @property
    def out_params(self):
        """
        Gets the out_params of this ExecuteOperationJob.
        List of names of OUT/INOUT params.


        :return: The out_params of this ExecuteOperationJob.
        :rtype: list[str]
        """
        return self._out_params

    @out_params.setter
    def out_params(self, out_params):
        """
        Sets the out_params of this ExecuteOperationJob.
        List of names of OUT/INOUT params.


        :param out_params: The out_params of this ExecuteOperationJob.
        :type: list[str]
        """
        self._out_params = out_params

    @property
    def operation_result(self):
        """
        **[Required]** Gets the operation_result of this ExecuteOperationJob.
        List of operation execution result for each input set.


        :return: The operation_result of this ExecuteOperationJob.
        :rtype: list[oci.data_connectivity.models.OperationExecResult]
        """
        return self._operation_result

    @operation_result.setter
    def operation_result(self, operation_result):
        """
        Sets the operation_result of this ExecuteOperationJob.
        List of operation execution result for each input set.


        :param operation_result: The operation_result of this ExecuteOperationJob.
        :type: list[oci.data_connectivity.models.OperationExecResult]
        """
        self._operation_result = operation_result

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
