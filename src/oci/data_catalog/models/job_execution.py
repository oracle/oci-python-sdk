# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobExecution(object):
    """
    A job execution is a unit of work being executed on behalf of a job.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobExecution object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this JobExecution.
        :type key: str

        :param job_key:
            The value to assign to the job_key property of this JobExecution.
        :type job_key: str

        :param job_type:
            The value to assign to the job_type property of this JobExecution.
        :type job_type: str

        :param sub_type:
            The value to assign to the sub_type property of this JobExecution.
        :type sub_type: str

        :param parent_key:
            The value to assign to the parent_key property of this JobExecution.
        :type parent_key: str

        :param schedule_instance_key:
            The value to assign to the schedule_instance_key property of this JobExecution.
        :type schedule_instance_key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this JobExecution.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this JobExecution.
        :type time_created: datetime

        :param time_started:
            The value to assign to the time_started property of this JobExecution.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this JobExecution.
        :type time_ended: datetime

        :param error_code:
            The value to assign to the error_code property of this JobExecution.
        :type error_code: str

        :param error_message:
            The value to assign to the error_message property of this JobExecution.
        :type error_message: str

        :param process_key:
            The value to assign to the process_key property of this JobExecution.
        :type process_key: str

        :param external_url:
            The value to assign to the external_url property of this JobExecution.
        :type external_url: str

        :param event_key:
            The value to assign to the event_key property of this JobExecution.
        :type event_key: str

        :param data_entity_key:
            The value to assign to the data_entity_key property of this JobExecution.
        :type data_entity_key: str

        :param created_by_id:
            The value to assign to the created_by_id property of this JobExecution.
        :type created_by_id: str

        :param updated_by:
            The value to assign to the updated_by property of this JobExecution.
        :type updated_by: str

        :param uri:
            The value to assign to the uri property of this JobExecution.
        :type uri: str

        :param properties:
            The value to assign to the properties property of this JobExecution.
        :type properties: dict(str, dict(str, str))

        """
        self.swagger_types = {
            'key': 'str',
            'job_key': 'str',
            'job_type': 'str',
            'sub_type': 'str',
            'parent_key': 'str',
            'schedule_instance_key': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'error_code': 'str',
            'error_message': 'str',
            'process_key': 'str',
            'external_url': 'str',
            'event_key': 'str',
            'data_entity_key': 'str',
            'created_by_id': 'str',
            'updated_by': 'str',
            'uri': 'str',
            'properties': 'dict(str, dict(str, str))'
        }

        self.attribute_map = {
            'key': 'key',
            'job_key': 'jobKey',
            'job_type': 'jobType',
            'sub_type': 'subType',
            'parent_key': 'parentKey',
            'schedule_instance_key': 'scheduleInstanceKey',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'error_code': 'errorCode',
            'error_message': 'errorMessage',
            'process_key': 'processKey',
            'external_url': 'externalUrl',
            'event_key': 'eventKey',
            'data_entity_key': 'dataEntityKey',
            'created_by_id': 'createdById',
            'updated_by': 'updatedBy',
            'uri': 'uri',
            'properties': 'properties'
        }

        self._key = None
        self._job_key = None
        self._job_type = None
        self._sub_type = None
        self._parent_key = None
        self._schedule_instance_key = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_started = None
        self._time_ended = None
        self._error_code = None
        self._error_message = None
        self._process_key = None
        self._external_url = None
        self._event_key = None
        self._data_entity_key = None
        self._created_by_id = None
        self._updated_by = None
        self._uri = None
        self._properties = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this JobExecution.
        Unique key of the job execution resource.


        :return: The key of this JobExecution.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this JobExecution.
        Unique key of the job execution resource.


        :param key: The key of this JobExecution.
        :type: str
        """
        self._key = key

    @property
    def job_key(self):
        """
        Gets the job_key of this JobExecution.
        The unique key of the parent job.


        :return: The job_key of this JobExecution.
        :rtype: str
        """
        return self._job_key

    @job_key.setter
    def job_key(self, job_key):
        """
        Sets the job_key of this JobExecution.
        The unique key of the parent job.


        :param job_key: The job_key of this JobExecution.
        :type: str
        """
        self._job_key = job_key

    @property
    def job_type(self):
        """
        Gets the job_type of this JobExecution.
        Type of the job execution.


        :return: The job_type of this JobExecution.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """
        Sets the job_type of this JobExecution.
        Type of the job execution.


        :param job_type: The job_type of this JobExecution.
        :type: str
        """
        self._job_type = job_type

    @property
    def sub_type(self):
        """
        Gets the sub_type of this JobExecution.
        Sub-type of this job execution.


        :return: The sub_type of this JobExecution.
        :rtype: str
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """
        Sets the sub_type of this JobExecution.
        Sub-type of this job execution.


        :param sub_type: The sub_type of this JobExecution.
        :type: str
        """
        self._sub_type = sub_type

    @property
    def parent_key(self):
        """
        Gets the parent_key of this JobExecution.
        The unique key of the parent execution or null if this job execution has no parent.


        :return: The parent_key of this JobExecution.
        :rtype: str
        """
        return self._parent_key

    @parent_key.setter
    def parent_key(self, parent_key):
        """
        Sets the parent_key of this JobExecution.
        The unique key of the parent execution or null if this job execution has no parent.


        :param parent_key: The parent_key of this JobExecution.
        :type: str
        """
        self._parent_key = parent_key

    @property
    def schedule_instance_key(self):
        """
        Gets the schedule_instance_key of this JobExecution.
        The unique key of the triggering external scheduler resource or null if this job execution is not externally triggered.


        :return: The schedule_instance_key of this JobExecution.
        :rtype: str
        """
        return self._schedule_instance_key

    @schedule_instance_key.setter
    def schedule_instance_key(self, schedule_instance_key):
        """
        Sets the schedule_instance_key of this JobExecution.
        The unique key of the triggering external scheduler resource or null if this job execution is not externally triggered.


        :param schedule_instance_key: The schedule_instance_key of this JobExecution.
        :type: str
        """
        self._schedule_instance_key = schedule_instance_key

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this JobExecution.
        Status of the job execution, such as running, paused, or completed.


        :return: The lifecycle_state of this JobExecution.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this JobExecution.
        Status of the job execution, such as running, paused, or completed.


        :param lifecycle_state: The lifecycle_state of this JobExecution.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this JobExecution.
        The date and time the job execution was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this JobExecution.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JobExecution.
        The date and time the job execution was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this JobExecution.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_started(self):
        """
        Gets the time_started of this JobExecution.
        Time that job execution started. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_started of this JobExecution.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this JobExecution.
        Time that job execution started. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_started: The time_started of this JobExecution.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this JobExecution.
        Time that the job execution ended or null if it hasn't yet completed.
        An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_ended of this JobExecution.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this JobExecution.
        Time that the job execution ended or null if it hasn't yet completed.
        An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_ended: The time_ended of this JobExecution.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def error_code(self):
        """
        Gets the error_code of this JobExecution.
        Error code returned from the job execution or null if job is still running or didn't return an error.


        :return: The error_code of this JobExecution.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this JobExecution.
        Error code returned from the job execution or null if job is still running or didn't return an error.


        :param error_code: The error_code of this JobExecution.
        :type: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """
        Gets the error_message of this JobExecution.
        Error message returned from the job execution or null if job is still running or didn't return an error.


        :return: The error_message of this JobExecution.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this JobExecution.
        Error message returned from the job execution or null if job is still running or didn't return an error.


        :param error_message: The error_message of this JobExecution.
        :type: str
        """
        self._error_message = error_message

    @property
    def process_key(self):
        """
        Gets the process_key of this JobExecution.
        Process identifier related to the job execution if the job is an external job.


        :return: The process_key of this JobExecution.
        :rtype: str
        """
        return self._process_key

    @process_key.setter
    def process_key(self, process_key):
        """
        Sets the process_key of this JobExecution.
        Process identifier related to the job execution if the job is an external job.


        :param process_key: The process_key of this JobExecution.
        :type: str
        """
        self._process_key = process_key

    @property
    def external_url(self):
        """
        Gets the external_url of this JobExecution.
        If the job is an external process, then a URL of the job for accessing this resource and its status.


        :return: The external_url of this JobExecution.
        :rtype: str
        """
        return self._external_url

    @external_url.setter
    def external_url(self, external_url):
        """
        Sets the external_url of this JobExecution.
        If the job is an external process, then a URL of the job for accessing this resource and its status.


        :param external_url: The external_url of this JobExecution.
        :type: str
        """
        self._external_url = external_url

    @property
    def event_key(self):
        """
        Gets the event_key of this JobExecution.
        An identifier used for log message correlation.


        :return: The event_key of this JobExecution.
        :rtype: str
        """
        return self._event_key

    @event_key.setter
    def event_key(self, event_key):
        """
        Sets the event_key of this JobExecution.
        An identifier used for log message correlation.


        :param event_key: The event_key of this JobExecution.
        :type: str
        """
        self._event_key = event_key

    @property
    def data_entity_key(self):
        """
        Gets the data_entity_key of this JobExecution.
        The key of the associated data entity resource.


        :return: The data_entity_key of this JobExecution.
        :rtype: str
        """
        return self._data_entity_key

    @data_entity_key.setter
    def data_entity_key(self, data_entity_key):
        """
        Sets the data_entity_key of this JobExecution.
        The key of the associated data entity resource.


        :param data_entity_key: The data_entity_key of this JobExecution.
        :type: str
        """
        self._data_entity_key = data_entity_key

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this JobExecution.
        OCID of the user who created the job execution.


        :return: The created_by_id of this JobExecution.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this JobExecution.
        OCID of the user who created the job execution.


        :param created_by_id: The created_by_id of this JobExecution.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by(self):
        """
        Gets the updated_by of this JobExecution.
        OCID of the user who updated the job execution.


        :return: The updated_by of this JobExecution.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """
        Sets the updated_by of this JobExecution.
        OCID of the user who updated the job execution.


        :param updated_by: The updated_by of this JobExecution.
        :type: str
        """
        self._updated_by = updated_by

    @property
    def uri(self):
        """
        Gets the uri of this JobExecution.
        URI to the job execution instance in the API.


        :return: The uri of this JobExecution.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this JobExecution.
        URI to the job execution instance in the API.


        :param uri: The uri of this JobExecution.
        :type: str
        """
        self._uri = uri

    @property
    def properties(self):
        """
        Gets the properties of this JobExecution.
        A map of maps that contains the execution context properties which are specific to a job execution. Each job
        execution may define it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        job executions have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :return: The properties of this JobExecution.
        :rtype: dict(str, dict(str, str))
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this JobExecution.
        A map of maps that contains the execution context properties which are specific to a job execution. Each job
        execution may define it's set of required and optional properties. The map keys are category names and the
        values are maps of property name to property value. Every property is contained inside of a category. Most
        job executions have required properties within the \"default\" category.
        Example: `{\"properties\": { \"default\": { \"host\": \"host1\", \"port\": \"1521\", \"database\": \"orcl\"}}}`


        :param properties: The properties of this JobExecution.
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
