# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExecuteOperationJobDetails(object):
    """
    Contains details of executeOperationJob.
    """

    #: A constant which can be used with the status property of a ExecuteOperationJobDetails.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a ExecuteOperationJobDetails.
    #: This constant has a value of "SUCCESS"
    STATUS_SUCCESS = "SUCCESS"

    def __init__(self, **kwargs):
        """
        Initializes a new ExecuteOperationJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param execute_operation_job_id:
            The value to assign to the execute_operation_job_id property of this ExecuteOperationJobDetails.
        :type execute_operation_job_id: str

        :param status:
            The value to assign to the status property of this ExecuteOperationJobDetails.
            Allowed values for this property are: "FAILED", "SUCCESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param error_message:
            The value to assign to the error_message property of this ExecuteOperationJobDetails.
        :type error_message: str

        """
        self.swagger_types = {
            'execute_operation_job_id': 'str',
            'status': 'str',
            'error_message': 'str'
        }

        self.attribute_map = {
            'execute_operation_job_id': 'executeOperationJobId',
            'status': 'status',
            'error_message': 'errorMessage'
        }

        self._execute_operation_job_id = None
        self._status = None
        self._error_message = None

    @property
    def execute_operation_job_id(self):
        """
        **[Required]** Gets the execute_operation_job_id of this ExecuteOperationJobDetails.
        Job ID to track the job status.


        :return: The execute_operation_job_id of this ExecuteOperationJobDetails.
        :rtype: str
        """
        return self._execute_operation_job_id

    @execute_operation_job_id.setter
    def execute_operation_job_id(self, execute_operation_job_id):
        """
        Sets the execute_operation_job_id of this ExecuteOperationJobDetails.
        Job ID to track the job status.


        :param execute_operation_job_id: The execute_operation_job_id of this ExecuteOperationJobDetails.
        :type: str
        """
        self._execute_operation_job_id = execute_operation_job_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this ExecuteOperationJobDetails.
        The status of the job.

        Allowed values for this property are: "FAILED", "SUCCESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this ExecuteOperationJobDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ExecuteOperationJobDetails.
        The status of the job.


        :param status: The status of this ExecuteOperationJobDetails.
        :type: str
        """
        allowed_values = ["FAILED", "SUCCESS"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def error_message(self):
        """
        Gets the error_message of this ExecuteOperationJobDetails.
        Error message when the job creation fails.


        :return: The error_message of this ExecuteOperationJobDetails.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ExecuteOperationJobDetails.
        Error message when the job creation fails.


        :param error_message: The error_message of this ExecuteOperationJobDetails.
        :type: str
        """
        self._error_message = error_message

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
