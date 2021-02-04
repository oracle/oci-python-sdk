# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobExecutionSummary(object):
    """
    A list of job executions. A job execution is a unit of work being executed on behalf of a job.
    """

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "HARVEST"
    JOB_TYPE_HARVEST = "HARVEST"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "PROFILING"
    JOB_TYPE_PROFILING = "PROFILING"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "SAMPLING"
    JOB_TYPE_SAMPLING = "SAMPLING"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "PREVIEW"
    JOB_TYPE_PREVIEW = "PREVIEW"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "IMPORT"
    JOB_TYPE_IMPORT = "IMPORT"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "EXPORT"
    JOB_TYPE_EXPORT = "EXPORT"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "IMPORT_GLOSSARY"
    JOB_TYPE_IMPORT_GLOSSARY = "IMPORT_GLOSSARY"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "EXPORT_GLOSSARY"
    JOB_TYPE_EXPORT_GLOSSARY = "EXPORT_GLOSSARY"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "INTERNAL"
    JOB_TYPE_INTERNAL = "INTERNAL"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "PURGE"
    JOB_TYPE_PURGE = "PURGE"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "IMMEDIATE"
    JOB_TYPE_IMMEDIATE = "IMMEDIATE"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "SCHEDULED"
    JOB_TYPE_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "IMMEDIATE_EXECUTION"
    JOB_TYPE_IMMEDIATE_EXECUTION = "IMMEDIATE_EXECUTION"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "SCHEDULED_EXECUTION"
    JOB_TYPE_SCHEDULED_EXECUTION = "SCHEDULED_EXECUTION"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "SCHEDULED_EXECUTION_INSTANCE"
    JOB_TYPE_SCHEDULED_EXECUTION_INSTANCE = "SCHEDULED_EXECUTION_INSTANCE"

    #: A constant which can be used with the job_type property of a JobExecutionSummary.
    #: This constant has a value of "ASYNC_DELETE"
    JOB_TYPE_ASYNC_DELETE = "ASYNC_DELETE"

    #: A constant which can be used with the lifecycle_state property of a JobExecutionSummary.
    #: This constant has a value of "CREATED"
    LIFECYCLE_STATE_CREATED = "CREATED"

    #: A constant which can be used with the lifecycle_state property of a JobExecutionSummary.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a JobExecutionSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a JobExecutionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a JobExecutionSummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a JobExecutionSummary.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a JobExecutionSummary.
    #: This constant has a value of "SUCCEEDED_WITH_WARNINGS"
    LIFECYCLE_STATE_SUCCEEDED_WITH_WARNINGS = "SUCCEEDED_WITH_WARNINGS"

    def __init__(self, **kwargs):
        """
        Initializes a new JobExecutionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this JobExecutionSummary.
        :type key: str

        :param job_key:
            The value to assign to the job_key property of this JobExecutionSummary.
        :type job_key: str

        :param job_type:
            The value to assign to the job_type property of this JobExecutionSummary.
            Allowed values for this property are: "HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE", "ASYNC_DELETE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type job_type: str

        :param parent_key:
            The value to assign to the parent_key property of this JobExecutionSummary.
        :type parent_key: str

        :param schedule_instance_key:
            The value to assign to the schedule_instance_key property of this JobExecutionSummary.
        :type schedule_instance_key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this JobExecutionSummary.
            Allowed values for this property are: "CREATED", "IN_PROGRESS", "INACTIVE", "FAILED", "SUCCEEDED", "CANCELED", "SUCCEEDED_WITH_WARNINGS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this JobExecutionSummary.
        :type time_created: datetime

        :param time_started:
            The value to assign to the time_started property of this JobExecutionSummary.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this JobExecutionSummary.
        :type time_ended: datetime

        :param uri:
            The value to assign to the uri property of this JobExecutionSummary.
        :type uri: str

        """
        self.swagger_types = {
            'key': 'str',
            'job_key': 'str',
            'job_type': 'str',
            'parent_key': 'str',
            'schedule_instance_key': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'uri': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'job_key': 'jobKey',
            'job_type': 'jobType',
            'parent_key': 'parentKey',
            'schedule_instance_key': 'scheduleInstanceKey',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'uri': 'uri'
        }

        self._key = None
        self._job_key = None
        self._job_type = None
        self._parent_key = None
        self._schedule_instance_key = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_started = None
        self._time_ended = None
        self._uri = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this JobExecutionSummary.
        Unique key of the job execution resource.


        :return: The key of this JobExecutionSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this JobExecutionSummary.
        Unique key of the job execution resource.


        :param key: The key of this JobExecutionSummary.
        :type: str
        """
        self._key = key

    @property
    def job_key(self):
        """
        Gets the job_key of this JobExecutionSummary.
        The unique key of the parent job.


        :return: The job_key of this JobExecutionSummary.
        :rtype: str
        """
        return self._job_key

    @job_key.setter
    def job_key(self, job_key):
        """
        Sets the job_key of this JobExecutionSummary.
        The unique key of the parent job.


        :param job_key: The job_key of this JobExecutionSummary.
        :type: str
        """
        self._job_key = job_key

    @property
    def job_type(self):
        """
        Gets the job_type of this JobExecutionSummary.
        Type of the job execution.

        Allowed values for this property are: "HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE", "ASYNC_DELETE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The job_type of this JobExecutionSummary.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """
        Sets the job_type of this JobExecutionSummary.
        Type of the job execution.


        :param job_type: The job_type of this JobExecutionSummary.
        :type: str
        """
        allowed_values = ["HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE", "ASYNC_DELETE"]
        if not value_allowed_none_or_none_sentinel(job_type, allowed_values):
            job_type = 'UNKNOWN_ENUM_VALUE'
        self._job_type = job_type

    @property
    def parent_key(self):
        """
        Gets the parent_key of this JobExecutionSummary.
        The unique key of the parent execution or null if this job execution has no parent.


        :return: The parent_key of this JobExecutionSummary.
        :rtype: str
        """
        return self._parent_key

    @parent_key.setter
    def parent_key(self, parent_key):
        """
        Sets the parent_key of this JobExecutionSummary.
        The unique key of the parent execution or null if this job execution has no parent.


        :param parent_key: The parent_key of this JobExecutionSummary.
        :type: str
        """
        self._parent_key = parent_key

    @property
    def schedule_instance_key(self):
        """
        Gets the schedule_instance_key of this JobExecutionSummary.
        The unique key of the triggering external scheduler resource or null if this job execution is not externally triggered.


        :return: The schedule_instance_key of this JobExecutionSummary.
        :rtype: str
        """
        return self._schedule_instance_key

    @schedule_instance_key.setter
    def schedule_instance_key(self, schedule_instance_key):
        """
        Sets the schedule_instance_key of this JobExecutionSummary.
        The unique key of the triggering external scheduler resource or null if this job execution is not externally triggered.


        :param schedule_instance_key: The schedule_instance_key of this JobExecutionSummary.
        :type: str
        """
        self._schedule_instance_key = schedule_instance_key

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this JobExecutionSummary.
        Status of the job execution, such as running, paused, or completed.

        Allowed values for this property are: "CREATED", "IN_PROGRESS", "INACTIVE", "FAILED", "SUCCEEDED", "CANCELED", "SUCCEEDED_WITH_WARNINGS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this JobExecutionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this JobExecutionSummary.
        Status of the job execution, such as running, paused, or completed.


        :param lifecycle_state: The lifecycle_state of this JobExecutionSummary.
        :type: str
        """
        allowed_values = ["CREATED", "IN_PROGRESS", "INACTIVE", "FAILED", "SUCCEEDED", "CANCELED", "SUCCEEDED_WITH_WARNINGS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this JobExecutionSummary.
        The date and time the job execution was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this JobExecutionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JobExecutionSummary.
        The date and time the job execution was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this JobExecutionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_started(self):
        """
        Gets the time_started of this JobExecutionSummary.
        Time that job execution started. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_started of this JobExecutionSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this JobExecutionSummary.
        Time that job execution started. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_started: The time_started of this JobExecutionSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this JobExecutionSummary.
        Time that the job execution ended or null if it hasn't yet completed.
        An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_ended of this JobExecutionSummary.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this JobExecutionSummary.
        Time that the job execution ended or null if it hasn't yet completed.
        An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_ended: The time_ended of this JobExecutionSummary.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def uri(self):
        """
        Gets the uri of this JobExecutionSummary.
        URI to the job execution instance in the API.


        :return: The uri of this JobExecutionSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this JobExecutionSummary.
        URI to the job execution instance in the API.


        :param uri: The uri of this JobExecutionSummary.
        :type: str
        """
        self._uri = uri

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
