# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateJobExecutionDetails(object):
    """
    Properties for creating a new job execution.
    """

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "HARVEST"
    JOB_TYPE_HARVEST = "HARVEST"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "PROFILING"
    JOB_TYPE_PROFILING = "PROFILING"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "SAMPLING"
    JOB_TYPE_SAMPLING = "SAMPLING"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "PREVIEW"
    JOB_TYPE_PREVIEW = "PREVIEW"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "IMPORT"
    JOB_TYPE_IMPORT = "IMPORT"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "EXPORT"
    JOB_TYPE_EXPORT = "EXPORT"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "IMPORT_GLOSSARY"
    JOB_TYPE_IMPORT_GLOSSARY = "IMPORT_GLOSSARY"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "EXPORT_GLOSSARY"
    JOB_TYPE_EXPORT_GLOSSARY = "EXPORT_GLOSSARY"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "INTERNAL"
    JOB_TYPE_INTERNAL = "INTERNAL"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "PURGE"
    JOB_TYPE_PURGE = "PURGE"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "IMMEDIATE"
    JOB_TYPE_IMMEDIATE = "IMMEDIATE"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "SCHEDULED"
    JOB_TYPE_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "IMMEDIATE_EXECUTION"
    JOB_TYPE_IMMEDIATE_EXECUTION = "IMMEDIATE_EXECUTION"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "SCHEDULED_EXECUTION"
    JOB_TYPE_SCHEDULED_EXECUTION = "SCHEDULED_EXECUTION"

    #: A constant which can be used with the job_type property of a CreateJobExecutionDetails.
    #: This constant has a value of "SCHEDULED_EXECUTION_INSTANCE"
    JOB_TYPE_SCHEDULED_EXECUTION_INSTANCE = "SCHEDULED_EXECUTION_INSTANCE"

    #: A constant which can be used with the lifecycle_state property of a CreateJobExecutionDetails.
    #: This constant has a value of "CREATED"
    LIFECYCLE_STATE_CREATED = "CREATED"

    #: A constant which can be used with the lifecycle_state property of a CreateJobExecutionDetails.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a CreateJobExecutionDetails.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CreateJobExecutionDetails.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a CreateJobExecutionDetails.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a CreateJobExecutionDetails.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateJobExecutionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sub_type:
            The value to assign to the sub_type property of this CreateJobExecutionDetails.
        :type sub_type: str

        :param job_type:
            The value to assign to the job_type property of this CreateJobExecutionDetails.
            Allowed values for this property are: "HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE"
        :type job_type: str

        :param parent_key:
            The value to assign to the parent_key property of this CreateJobExecutionDetails.
        :type parent_key: str

        :param time_started:
            The value to assign to the time_started property of this CreateJobExecutionDetails.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this CreateJobExecutionDetails.
        :type time_ended: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CreateJobExecutionDetails.
            Allowed values for this property are: "CREATED", "IN_PROGRESS", "INACTIVE", "FAILED", "SUCCEEDED", "CANCELED"
        :type lifecycle_state: str

        :param error_code:
            The value to assign to the error_code property of this CreateJobExecutionDetails.
        :type error_code: str

        :param error_message:
            The value to assign to the error_message property of this CreateJobExecutionDetails.
        :type error_message: str

        :param schedule_instance_key:
            The value to assign to the schedule_instance_key property of this CreateJobExecutionDetails.
        :type schedule_instance_key: str

        :param process_key:
            The value to assign to the process_key property of this CreateJobExecutionDetails.
        :type process_key: str

        :param external_url:
            The value to assign to the external_url property of this CreateJobExecutionDetails.
        :type external_url: str

        :param event_key:
            The value to assign to the event_key property of this CreateJobExecutionDetails.
        :type event_key: str

        :param data_entity_key:
            The value to assign to the data_entity_key property of this CreateJobExecutionDetails.
        :type data_entity_key: str

        :param properties:
            The value to assign to the properties property of this CreateJobExecutionDetails.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'sub_type': 'str',
            'job_type': 'str',
            'parent_key': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'lifecycle_state': 'str',
            'error_code': 'str',
            'error_message': 'str',
            'schedule_instance_key': 'str',
            'process_key': 'str',
            'external_url': 'str',
            'event_key': 'str',
            'data_entity_key': 'str',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'sub_type': 'subType',
            'job_type': 'jobType',
            'parent_key': 'parentKey',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'lifecycle_state': 'lifecycleState',
            'error_code': 'errorCode',
            'error_message': 'errorMessage',
            'schedule_instance_key': 'scheduleInstanceKey',
            'process_key': 'processKey',
            'external_url': 'externalUrl',
            'event_key': 'eventKey',
            'data_entity_key': 'dataEntityKey',
            'properties': 'properties'
        }

        self._sub_type = None
        self._job_type = None
        self._parent_key = None
        self._time_started = None
        self._time_ended = None
        self._lifecycle_state = None
        self._error_code = None
        self._error_message = None
        self._schedule_instance_key = None
        self._process_key = None
        self._external_url = None
        self._event_key = None
        self._data_entity_key = None
        self._properties = None

    @property
    def sub_type(self):
        """
        Gets the sub_type of this CreateJobExecutionDetails.
        Sub-type of this job execution.


        :return: The sub_type of this CreateJobExecutionDetails.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """
        Sets the sub_type of this CreateJobExecutionDetails.
        Sub-type of this job execution.


        :param sub_type: The sub_type of this CreateJobExecutionDetails.
        :type: str
        """
        self._sub_type = sub_type

    @property
    def job_type(self):
        """
        Gets the job_type of this CreateJobExecutionDetails.
        Type of the job execution.

        Allowed values for this property are: "HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE"


        :return: The job_type of this CreateJobExecutionDetails.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """
        Sets the job_type of this CreateJobExecutionDetails.
        Type of the job execution.


        :param job_type: The job_type of this CreateJobExecutionDetails.
        :type: str
        """
        allowed_values = ["HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE"]
        if not value_allowed_none_or_none_sentinel(job_type, allowed_values):
            raise ValueError(
                "Invalid value for `job_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._job_type = job_type

    @property
    def parent_key(self):
        """
        Gets the parent_key of this CreateJobExecutionDetails.
        The unique key of the parent execution or null if this job execution has no parent.


        :return: The parent_key of this CreateJobExecutionDetails.
        :rtype: str
        """
        return self._parent_key

    @parent_key.setter
    def parent_key(self, parent_key):
        """
        Sets the parent_key of this CreateJobExecutionDetails.
        The unique key of the parent execution or null if this job execution has no parent.


        :param parent_key: The parent_key of this CreateJobExecutionDetails.
        :type: str
        """
        self._parent_key = parent_key

    @property
    def time_started(self):
        """
        Gets the time_started of this CreateJobExecutionDetails.
        Time that job execution started. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_started of this CreateJobExecutionDetails.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this CreateJobExecutionDetails.
        Time that job execution started. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_started: The time_started of this CreateJobExecutionDetails.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this CreateJobExecutionDetails.
        Time that the job execution ended or null if it hasn't yet completed.
        An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_ended of this CreateJobExecutionDetails.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this CreateJobExecutionDetails.
        Time that the job execution ended or null if it hasn't yet completed.
        An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_ended: The time_ended of this CreateJobExecutionDetails.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CreateJobExecutionDetails.
        Status of the job execution, such as running, paused, or completed.

        Allowed values for this property are: "CREATED", "IN_PROGRESS", "INACTIVE", "FAILED", "SUCCEEDED", "CANCELED"


        :return: The lifecycle_state of this CreateJobExecutionDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CreateJobExecutionDetails.
        Status of the job execution, such as running, paused, or completed.


        :param lifecycle_state: The lifecycle_state of this CreateJobExecutionDetails.
        :type: str
        """
        allowed_values = ["CREATED", "IN_PROGRESS", "INACTIVE", "FAILED", "SUCCEEDED", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def error_code(self):
        """
        Gets the error_code of this CreateJobExecutionDetails.
        Error code returned from the job execution or null if job is still running or didn't return an error.


        :return: The error_code of this CreateJobExecutionDetails.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this CreateJobExecutionDetails.
        Error code returned from the job execution or null if job is still running or didn't return an error.


        :param error_code: The error_code of this CreateJobExecutionDetails.
        :type: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """
        Gets the error_message of this CreateJobExecutionDetails.
        Error message returned from the job execution or null if job is still running or didn't return an error.


        :return: The error_message of this CreateJobExecutionDetails.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this CreateJobExecutionDetails.
        Error message returned from the job execution or null if job is still running or didn't return an error.


        :param error_message: The error_message of this CreateJobExecutionDetails.
        :type: str
        """
        self._error_message = error_message

    @property
    def schedule_instance_key(self):
        """
        Gets the schedule_instance_key of this CreateJobExecutionDetails.
        The unique key of the triggering external scheduler resource or null if this job execution is not externally triggered.


        :return: The schedule_instance_key of this CreateJobExecutionDetails.
        :rtype: str
        """
        return self._schedule_instance_key

    @schedule_instance_key.setter
    def schedule_instance_key(self, schedule_instance_key):
        """
        Sets the schedule_instance_key of this CreateJobExecutionDetails.
        The unique key of the triggering external scheduler resource or null if this job execution is not externally triggered.


        :param schedule_instance_key: The schedule_instance_key of this CreateJobExecutionDetails.
        :type: str
        """
        self._schedule_instance_key = schedule_instance_key

    @property
    def process_key(self):
        """
        Gets the process_key of this CreateJobExecutionDetails.
        Process identifier related to the job execution if the job is an external job.


        :return: The process_key of this CreateJobExecutionDetails.
        :rtype: str
        """
        return self._process_key

    @process_key.setter
    def process_key(self, process_key):
        """
        Sets the process_key of this CreateJobExecutionDetails.
        Process identifier related to the job execution if the job is an external job.


        :param process_key: The process_key of this CreateJobExecutionDetails.
        :type: str
        """
        self._process_key = process_key

    @property
    def external_url(self):
        """
        Gets the external_url of this CreateJobExecutionDetails.
        If the job is an external process, then a URL of the job for accessing this resource and its status.


        :return: The external_url of this CreateJobExecutionDetails.
        :rtype: str
        """
        return self._external_url

    @external_url.setter
    def external_url(self, external_url):
        """
        Sets the external_url of this CreateJobExecutionDetails.
        If the job is an external process, then a URL of the job for accessing this resource and its status.


        :param external_url: The external_url of this CreateJobExecutionDetails.
        :type: str
        """
        self._external_url = external_url

    @property
    def event_key(self):
        """
        Gets the event_key of this CreateJobExecutionDetails.
        An identifier used for log message correlation.


        :return: The event_key of this CreateJobExecutionDetails.
        :rtype: str
        """
        return self._event_key

    @event_key.setter
    def event_key(self, event_key):
        """
        Sets the event_key of this CreateJobExecutionDetails.
        An identifier used for log message correlation.


        :param event_key: The event_key of this CreateJobExecutionDetails.
        :type: str
        """
        self._event_key = event_key

    @property
    def data_entity_key(self):
        """
        Gets the data_entity_key of this CreateJobExecutionDetails.
        The key of the associated data entity resource.


        :return: The data_entity_key of this CreateJobExecutionDetails.
        :rtype: str
        """
        return self._data_entity_key

    @data_entity_key.setter
    def data_entity_key(self, data_entity_key):
        """
        Sets the data_entity_key of this CreateJobExecutionDetails.
        The key of the associated data entity resource.


        :param data_entity_key: The data_entity_key of this CreateJobExecutionDetails.
        :type: str
        """
        self._data_entity_key = data_entity_key

    @property
    def properties(self):
        """
        Gets the properties of this CreateJobExecutionDetails.
        A map of maps that contains the execution context properties which are specific to a job execution. Each job
        execution may define it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        job executions have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :return: The properties of this CreateJobExecutionDetails.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this CreateJobExecutionDetails.
        A map of maps that contains the execution context properties which are specific to a job execution. Each job
        execution may define it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        job executions have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :param properties: The properties of this CreateJobExecutionDetails.
        :type: dict(str, dict(str, str))
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
