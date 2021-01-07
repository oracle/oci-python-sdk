# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobDefinitionSummary(object):
    """
    A list of job definition resources. Job definitions define the harvest scope and includes the list of objects
    to be harvested along with a schedule. The list of objects is usually specified through a combination of object
    type, regular expressions, or specific names of objects and a sample size for the data harvested.
    """

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "HARVEST"
    JOB_TYPE_HARVEST = "HARVEST"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "PROFILING"
    JOB_TYPE_PROFILING = "PROFILING"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "SAMPLING"
    JOB_TYPE_SAMPLING = "SAMPLING"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "PREVIEW"
    JOB_TYPE_PREVIEW = "PREVIEW"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "IMPORT"
    JOB_TYPE_IMPORT = "IMPORT"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "EXPORT"
    JOB_TYPE_EXPORT = "EXPORT"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "IMPORT_GLOSSARY"
    JOB_TYPE_IMPORT_GLOSSARY = "IMPORT_GLOSSARY"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "EXPORT_GLOSSARY"
    JOB_TYPE_EXPORT_GLOSSARY = "EXPORT_GLOSSARY"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "INTERNAL"
    JOB_TYPE_INTERNAL = "INTERNAL"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "PURGE"
    JOB_TYPE_PURGE = "PURGE"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "IMMEDIATE"
    JOB_TYPE_IMMEDIATE = "IMMEDIATE"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "SCHEDULED"
    JOB_TYPE_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "IMMEDIATE_EXECUTION"
    JOB_TYPE_IMMEDIATE_EXECUTION = "IMMEDIATE_EXECUTION"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "SCHEDULED_EXECUTION"
    JOB_TYPE_SCHEDULED_EXECUTION = "SCHEDULED_EXECUTION"

    #: A constant which can be used with the job_type property of a JobDefinitionSummary.
    #: This constant has a value of "SCHEDULED_EXECUTION_INSTANCE"
    JOB_TYPE_SCHEDULED_EXECUTION_INSTANCE = "SCHEDULED_EXECUTION_INSTANCE"

    #: A constant which can be used with the lifecycle_state property of a JobDefinitionSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a JobDefinitionSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a JobDefinitionSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a JobDefinitionSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a JobDefinitionSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a JobDefinitionSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a JobDefinitionSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a JobDefinitionSummary.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    #: A constant which can be used with the job_execution_state property of a JobDefinitionSummary.
    #: This constant has a value of "CREATED"
    JOB_EXECUTION_STATE_CREATED = "CREATED"

    #: A constant which can be used with the job_execution_state property of a JobDefinitionSummary.
    #: This constant has a value of "IN_PROGRESS"
    JOB_EXECUTION_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the job_execution_state property of a JobDefinitionSummary.
    #: This constant has a value of "INACTIVE"
    JOB_EXECUTION_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the job_execution_state property of a JobDefinitionSummary.
    #: This constant has a value of "FAILED"
    JOB_EXECUTION_STATE_FAILED = "FAILED"

    #: A constant which can be used with the job_execution_state property of a JobDefinitionSummary.
    #: This constant has a value of "SUCCEEDED"
    JOB_EXECUTION_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the job_execution_state property of a JobDefinitionSummary.
    #: This constant has a value of "CANCELED"
    JOB_EXECUTION_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the schedule_type property of a JobDefinitionSummary.
    #: This constant has a value of "SCHEDULED"
    SCHEDULE_TYPE_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the schedule_type property of a JobDefinitionSummary.
    #: This constant has a value of "IMMEDIATE"
    SCHEDULE_TYPE_IMMEDIATE = "IMMEDIATE"

    def __init__(self, **kwargs):
        """
        Initializes a new JobDefinitionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this JobDefinitionSummary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this JobDefinitionSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this JobDefinitionSummary.
        :type description: str

        :param catalog_id:
            The value to assign to the catalog_id property of this JobDefinitionSummary.
        :type catalog_id: str

        :param uri:
            The value to assign to the uri property of this JobDefinitionSummary.
        :type uri: str

        :param job_type:
            The value to assign to the job_type property of this JobDefinitionSummary.
            Allowed values for this property are: "HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type job_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this JobDefinitionSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param is_sample_data_extracted:
            The value to assign to the is_sample_data_extracted property of this JobDefinitionSummary.
        :type is_sample_data_extracted: bool

        :param time_created:
            The value to assign to the time_created property of this JobDefinitionSummary.
        :type time_created: datetime

        :param connection_key:
            The value to assign to the connection_key property of this JobDefinitionSummary.
        :type connection_key: str

        :param time_latest_execution_started:
            The value to assign to the time_latest_execution_started property of this JobDefinitionSummary.
        :type time_latest_execution_started: datetime

        :param time_latest_execution_ended:
            The value to assign to the time_latest_execution_ended property of this JobDefinitionSummary.
        :type time_latest_execution_ended: datetime

        :param job_execution_state:
            The value to assign to the job_execution_state property of this JobDefinitionSummary.
            Allowed values for this property are: "CREATED", "IN_PROGRESS", "INACTIVE", "FAILED", "SUCCEEDED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type job_execution_state: str

        :param schedule_type:
            The value to assign to the schedule_type property of this JobDefinitionSummary.
            Allowed values for this property are: "SCHEDULED", "IMMEDIATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type schedule_type: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'catalog_id': 'str',
            'uri': 'str',
            'job_type': 'str',
            'lifecycle_state': 'str',
            'is_sample_data_extracted': 'bool',
            'time_created': 'datetime',
            'connection_key': 'str',
            'time_latest_execution_started': 'datetime',
            'time_latest_execution_ended': 'datetime',
            'job_execution_state': 'str',
            'schedule_type': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'catalog_id': 'catalogId',
            'uri': 'uri',
            'job_type': 'jobType',
            'lifecycle_state': 'lifecycleState',
            'is_sample_data_extracted': 'isSampleDataExtracted',
            'time_created': 'timeCreated',
            'connection_key': 'connectionKey',
            'time_latest_execution_started': 'timeLatestExecutionStarted',
            'time_latest_execution_ended': 'timeLatestExecutionEnded',
            'job_execution_state': 'jobExecutionState',
            'schedule_type': 'scheduleType'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._catalog_id = None
        self._uri = None
        self._job_type = None
        self._lifecycle_state = None
        self._is_sample_data_extracted = None
        self._time_created = None
        self._connection_key = None
        self._time_latest_execution_started = None
        self._time_latest_execution_ended = None
        self._job_execution_state = None
        self._schedule_type = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this JobDefinitionSummary.
        Unique key of the job definition resource that is immutable.


        :return: The key of this JobDefinitionSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this JobDefinitionSummary.
        Unique key of the job definition resource that is immutable.


        :param key: The key of this JobDefinitionSummary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this JobDefinitionSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this JobDefinitionSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this JobDefinitionSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this JobDefinitionSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this JobDefinitionSummary.
        Detailed description of the job definition.


        :return: The description of this JobDefinitionSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this JobDefinitionSummary.
        Detailed description of the job definition.


        :param description: The description of this JobDefinitionSummary.
        :type: str
        """
        self._description = description

    @property
    def catalog_id(self):
        """
        Gets the catalog_id of this JobDefinitionSummary.
        The data catalog's OCID.


        :return: The catalog_id of this JobDefinitionSummary.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """
        Sets the catalog_id of this JobDefinitionSummary.
        The data catalog's OCID.


        :param catalog_id: The catalog_id of this JobDefinitionSummary.
        :type: str
        """
        self._catalog_id = catalog_id

    @property
    def uri(self):
        """
        Gets the uri of this JobDefinitionSummary.
        URI to the job definition instance in the API.


        :return: The uri of this JobDefinitionSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this JobDefinitionSummary.
        URI to the job definition instance in the API.


        :param uri: The uri of this JobDefinitionSummary.
        :type: str
        """
        self._uri = uri

    @property
    def job_type(self):
        """
        Gets the job_type of this JobDefinitionSummary.
        Type of the job definition.

        Allowed values for this property are: "HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The job_type of this JobDefinitionSummary.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """
        Sets the job_type of this JobDefinitionSummary.
        Type of the job definition.


        :param job_type: The job_type of this JobDefinitionSummary.
        :type: str
        """
        allowed_values = ["HARVEST", "PROFILING", "SAMPLING", "PREVIEW", "IMPORT", "EXPORT", "IMPORT_GLOSSARY", "EXPORT_GLOSSARY", "INTERNAL", "PURGE", "IMMEDIATE", "SCHEDULED", "IMMEDIATE_EXECUTION", "SCHEDULED_EXECUTION", "SCHEDULED_EXECUTION_INSTANCE"]
        if not value_allowed_none_or_none_sentinel(job_type, allowed_values):
            job_type = 'UNKNOWN_ENUM_VALUE'
        self._job_type = job_type

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this JobDefinitionSummary.
        Lifecycle state of the job definition.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this JobDefinitionSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this JobDefinitionSummary.
        Lifecycle state of the job definition.


        :param lifecycle_state: The lifecycle_state of this JobDefinitionSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def is_sample_data_extracted(self):
        """
        Gets the is_sample_data_extracted of this JobDefinitionSummary.
        Specify if sample data to be extracted as part of this harvest.


        :return: The is_sample_data_extracted of this JobDefinitionSummary.
        :rtype: bool
        """
        return self._is_sample_data_extracted

    @is_sample_data_extracted.setter
    def is_sample_data_extracted(self, is_sample_data_extracted):
        """
        Sets the is_sample_data_extracted of this JobDefinitionSummary.
        Specify if sample data to be extracted as part of this harvest.


        :param is_sample_data_extracted: The is_sample_data_extracted of this JobDefinitionSummary.
        :type: bool
        """
        self._is_sample_data_extracted = is_sample_data_extracted

    @property
    def time_created(self):
        """
        Gets the time_created of this JobDefinitionSummary.
        The date and time the job definition was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this JobDefinitionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JobDefinitionSummary.
        The date and time the job definition was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this JobDefinitionSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def connection_key(self):
        """
        Gets the connection_key of this JobDefinitionSummary.
        The key of the connection resource used in harvest, sampling, profiling jobs.


        :return: The connection_key of this JobDefinitionSummary.
        :rtype: str
        """
        return self._connection_key

    @connection_key.setter
    def connection_key(self, connection_key):
        """
        Sets the connection_key of this JobDefinitionSummary.
        The key of the connection resource used in harvest, sampling, profiling jobs.


        :param connection_key: The connection_key of this JobDefinitionSummary.
        :type: str
        """
        self._connection_key = connection_key

    @property
    def time_latest_execution_started(self):
        """
        Gets the time_latest_execution_started of this JobDefinitionSummary.
        Time that the latest job execution started. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_latest_execution_started of this JobDefinitionSummary.
        :rtype: datetime
        """
        return self._time_latest_execution_started

    @time_latest_execution_started.setter
    def time_latest_execution_started(self, time_latest_execution_started):
        """
        Sets the time_latest_execution_started of this JobDefinitionSummary.
        Time that the latest job execution started. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_latest_execution_started: The time_latest_execution_started of this JobDefinitionSummary.
        :type: datetime
        """
        self._time_latest_execution_started = time_latest_execution_started

    @property
    def time_latest_execution_ended(self):
        """
        Gets the time_latest_execution_ended of this JobDefinitionSummary.
        Time that the latest job execution ended or null if it hasn't yet completed.
        An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_latest_execution_ended of this JobDefinitionSummary.
        :rtype: datetime
        """
        return self._time_latest_execution_ended

    @time_latest_execution_ended.setter
    def time_latest_execution_ended(self, time_latest_execution_ended):
        """
        Sets the time_latest_execution_ended of this JobDefinitionSummary.
        Time that the latest job execution ended or null if it hasn't yet completed.
        An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_latest_execution_ended: The time_latest_execution_ended of this JobDefinitionSummary.
        :type: datetime
        """
        self._time_latest_execution_ended = time_latest_execution_ended

    @property
    def job_execution_state(self):
        """
        Gets the job_execution_state of this JobDefinitionSummary.
        Status of the latest job execution, such as running, paused, or completed.

        Allowed values for this property are: "CREATED", "IN_PROGRESS", "INACTIVE", "FAILED", "SUCCEEDED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The job_execution_state of this JobDefinitionSummary.
        :rtype: str
        """
        return self._job_execution_state

    @job_execution_state.setter
    def job_execution_state(self, job_execution_state):
        """
        Sets the job_execution_state of this JobDefinitionSummary.
        Status of the latest job execution, such as running, paused, or completed.


        :param job_execution_state: The job_execution_state of this JobDefinitionSummary.
        :type: str
        """
        allowed_values = ["CREATED", "IN_PROGRESS", "INACTIVE", "FAILED", "SUCCEEDED", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(job_execution_state, allowed_values):
            job_execution_state = 'UNKNOWN_ENUM_VALUE'
        self._job_execution_state = job_execution_state

    @property
    def schedule_type(self):
        """
        Gets the schedule_type of this JobDefinitionSummary.
        Type of job schedule for the latest job executed.

        Allowed values for this property are: "SCHEDULED", "IMMEDIATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The schedule_type of this JobDefinitionSummary.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this JobDefinitionSummary.
        Type of job schedule for the latest job executed.


        :param schedule_type: The schedule_type of this JobDefinitionSummary.
        :type: str
        """
        allowed_values = ["SCHEDULED", "IMMEDIATE"]
        if not value_allowed_none_or_none_sentinel(schedule_type, allowed_values):
            schedule_type = 'UNKNOWN_ENUM_VALUE'
        self._schedule_type = schedule_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
