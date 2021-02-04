# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobExecution(object):
    """
    The details of a job execution.
    """

    #: A constant which can be used with the status property of a JobExecution.
    #: This constant has a value of "SUCCEEDED"
    STATUS_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the status property of a JobExecution.
    #: This constant has a value of "FAILED"
    STATUS_FAILED = "FAILED"

    #: A constant which can be used with the status property of a JobExecution.
    #: This constant has a value of "IN_PROGRESS"
    STATUS_IN_PROGRESS = "IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new JobExecution object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this JobExecution.
        :type id: str

        :param name:
            The value to assign to the name property of this JobExecution.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this JobExecution.
        :type compartment_id: str

        :param managed_database_group_id:
            The value to assign to the managed_database_group_id property of this JobExecution.
        :type managed_database_group_id: str

        :param managed_database_id:
            The value to assign to the managed_database_id property of this JobExecution.
        :type managed_database_id: str

        :param managed_database_name:
            The value to assign to the managed_database_name property of this JobExecution.
        :type managed_database_name: str

        :param job_id:
            The value to assign to the job_id property of this JobExecution.
        :type job_id: str

        :param job_name:
            The value to assign to the job_name property of this JobExecution.
        :type job_name: str

        :param job_run_id:
            The value to assign to the job_run_id property of this JobExecution.
        :type job_run_id: str

        :param status:
            The value to assign to the status property of this JobExecution.
            Allowed values for this property are: "SUCCEEDED", "FAILED", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param error_message:
            The value to assign to the error_message property of this JobExecution.
        :type error_message: str

        :param result_details:
            The value to assign to the result_details property of this JobExecution.
        :type result_details: oci.database_management.models.JobExecutionResultDetails

        :param time_created:
            The value to assign to the time_created property of this JobExecution.
        :type time_created: datetime

        :param time_completed:
            The value to assign to the time_completed property of this JobExecution.
        :type time_completed: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'managed_database_group_id': 'str',
            'managed_database_id': 'str',
            'managed_database_name': 'str',
            'job_id': 'str',
            'job_name': 'str',
            'job_run_id': 'str',
            'status': 'str',
            'error_message': 'str',
            'result_details': 'JobExecutionResultDetails',
            'time_created': 'datetime',
            'time_completed': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'managed_database_group_id': 'managedDatabaseGroupId',
            'managed_database_id': 'managedDatabaseId',
            'managed_database_name': 'managedDatabaseName',
            'job_id': 'jobId',
            'job_name': 'jobName',
            'job_run_id': 'jobRunId',
            'status': 'status',
            'error_message': 'errorMessage',
            'result_details': 'resultDetails',
            'time_created': 'timeCreated',
            'time_completed': 'timeCompleted'
        }

        self._id = None
        self._name = None
        self._compartment_id = None
        self._managed_database_group_id = None
        self._managed_database_id = None
        self._managed_database_name = None
        self._job_id = None
        self._job_name = None
        self._job_run_id = None
        self._status = None
        self._error_message = None
        self._result_details = None
        self._time_created = None
        self._time_completed = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this JobExecution.
        The identifier of the job execution.


        :return: The id of this JobExecution.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JobExecution.
        The identifier of the job execution.


        :param id: The id of this JobExecution.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this JobExecution.
        The name of the job execution.


        :return: The name of this JobExecution.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this JobExecution.
        The name of the job execution.


        :param name: The name of this JobExecution.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this JobExecution.
        The `OCID`__ of the compartment in which the parent job resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this JobExecution.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this JobExecution.
        The `OCID`__ of the compartment in which the parent job resides.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this JobExecution.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def managed_database_group_id(self):
        """
        Gets the managed_database_group_id of this JobExecution.
        The `OCID`__ of the Managed Database Group where the parent job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_database_group_id of this JobExecution.
        :rtype: str
        """
        return self._managed_database_group_id

    @managed_database_group_id.setter
    def managed_database_group_id(self, managed_database_group_id):
        """
        Sets the managed_database_group_id of this JobExecution.
        The `OCID`__ of the Managed Database Group where the parent job has to be executed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_database_group_id: The managed_database_group_id of this JobExecution.
        :type: str
        """
        self._managed_database_group_id = managed_database_group_id

    @property
    def managed_database_id(self):
        """
        **[Required]** Gets the managed_database_id of this JobExecution.
        The `OCID`__ of the Managed Database associated with the job execution.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_database_id of this JobExecution.
        :rtype: str
        """
        return self._managed_database_id

    @managed_database_id.setter
    def managed_database_id(self, managed_database_id):
        """
        Sets the managed_database_id of this JobExecution.
        The `OCID`__ of the Managed Database associated with the job execution.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_database_id: The managed_database_id of this JobExecution.
        :type: str
        """
        self._managed_database_id = managed_database_id

    @property
    def managed_database_name(self):
        """
        **[Required]** Gets the managed_database_name of this JobExecution.
        The name of the Managed Database associated with the job execution.


        :return: The managed_database_name of this JobExecution.
        :rtype: str
        """
        return self._managed_database_name

    @managed_database_name.setter
    def managed_database_name(self, managed_database_name):
        """
        Sets the managed_database_name of this JobExecution.
        The name of the Managed Database associated with the job execution.


        :param managed_database_name: The managed_database_name of this JobExecution.
        :type: str
        """
        self._managed_database_name = managed_database_name

    @property
    def job_id(self):
        """
        **[Required]** Gets the job_id of this JobExecution.
        The `OCID`__ of the parent job.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The job_id of this JobExecution.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this JobExecution.
        The `OCID`__ of the parent job.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param job_id: The job_id of this JobExecution.
        :type: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """
        **[Required]** Gets the job_name of this JobExecution.
        The name of the parent job.


        :return: The job_name of this JobExecution.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """
        Sets the job_name of this JobExecution.
        The name of the parent job.


        :param job_name: The job_name of this JobExecution.
        :type: str
        """
        self._job_name = job_name

    @property
    def job_run_id(self):
        """
        **[Required]** Gets the job_run_id of this JobExecution.
        The identifier of the associated job run.


        :return: The job_run_id of this JobExecution.
        :rtype: str
        """
        return self._job_run_id

    @job_run_id.setter
    def job_run_id(self, job_run_id):
        """
        Sets the job_run_id of this JobExecution.
        The identifier of the associated job run.


        :param job_run_id: The job_run_id of this JobExecution.
        :type: str
        """
        self._job_run_id = job_run_id

    @property
    def status(self):
        """
        **[Required]** Gets the status of this JobExecution.
        The status of the job execution.

        Allowed values for this property are: "SUCCEEDED", "FAILED", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this JobExecution.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this JobExecution.
        The status of the job execution.


        :param status: The status of this JobExecution.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED", "IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def error_message(self):
        """
        Gets the error_message of this JobExecution.
        The error message that is returned if the job execution fails. Null is returned if the job is
        still running or if the job execution is successful.


        :return: The error_message of this JobExecution.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this JobExecution.
        The error message that is returned if the job execution fails. Null is returned if the job is
        still running or if the job execution is successful.


        :param error_message: The error_message of this JobExecution.
        :type: str
        """
        self._error_message = error_message

    @property
    def result_details(self):
        """
        Gets the result_details of this JobExecution.

        :return: The result_details of this JobExecution.
        :rtype: oci.database_management.models.JobExecutionResultDetails
        """
        return self._result_details

    @result_details.setter
    def result_details(self, result_details):
        """
        Sets the result_details of this JobExecution.

        :param result_details: The result_details of this JobExecution.
        :type: oci.database_management.models.JobExecutionResultDetails
        """
        self._result_details = result_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this JobExecution.
        The date and time when the job execution was created.


        :return: The time_created of this JobExecution.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JobExecution.
        The date and time when the job execution was created.


        :param time_created: The time_created of this JobExecution.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_completed(self):
        """
        Gets the time_completed of this JobExecution.
        The date and time when the job execution completed.


        :return: The time_completed of this JobExecution.
        :rtype: datetime
        """
        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """
        Sets the time_completed of this JobExecution.
        The date and time when the job execution completed.


        :param time_completed: The time_completed of this JobExecution.
        :type: datetime
        """
        self._time_completed = time_completed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
