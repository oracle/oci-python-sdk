# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class JobSummary(object):
    """
    Details of a job. Jobs are scheduled instances of a job definition.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new JobSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this JobSummary.
        :type key: str

        :param uri:
            The value to assign to the uri property of this JobSummary.
        :type uri: str

        :param display_name:
            The value to assign to the display_name property of this JobSummary.
        :type display_name: str

        :param catalog_id:
            The value to assign to the catalog_id property of this JobSummary.
        :type catalog_id: str

        :param job_definition_key:
            The value to assign to the job_definition_key property of this JobSummary.
        :type job_definition_key: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this JobSummary.
        :type lifecycle_state: str

        :param job_type:
            The value to assign to the job_type property of this JobSummary.
        :type job_type: str

        :param schedule_type:
            The value to assign to the schedule_type property of this JobSummary.
        :type schedule_type: str

        :param description:
            The value to assign to the description property of this JobSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this JobSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this JobSummary.
        :type time_updated: datetime

        :param created_by_id:
            The value to assign to the created_by_id property of this JobSummary.
        :type created_by_id: str

        :param updated_by_id:
            The value to assign to the updated_by_id property of this JobSummary.
        :type updated_by_id: str

        :param schedule_cron_expression:
            The value to assign to the schedule_cron_expression property of this JobSummary.
        :type schedule_cron_expression: str

        :param time_schedule_begin:
            The value to assign to the time_schedule_begin property of this JobSummary.
        :type time_schedule_begin: datetime

        :param execution_count:
            The value to assign to the execution_count property of this JobSummary.
        :type execution_count: int

        :param time_of_latest_execution:
            The value to assign to the time_of_latest_execution property of this JobSummary.
        :type time_of_latest_execution: datetime

        :param executions:
            The value to assign to the executions property of this JobSummary.
        :type executions: list[JobExecutionSummary]

        """
        self.swagger_types = {
            'key': 'str',
            'uri': 'str',
            'display_name': 'str',
            'catalog_id': 'str',
            'job_definition_key': 'str',
            'lifecycle_state': 'str',
            'job_type': 'str',
            'schedule_type': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'created_by_id': 'str',
            'updated_by_id': 'str',
            'schedule_cron_expression': 'str',
            'time_schedule_begin': 'datetime',
            'execution_count': 'int',
            'time_of_latest_execution': 'datetime',
            'executions': 'list[JobExecutionSummary]'
        }

        self.attribute_map = {
            'key': 'key',
            'uri': 'uri',
            'display_name': 'displayName',
            'catalog_id': 'catalogId',
            'job_definition_key': 'jobDefinitionKey',
            'lifecycle_state': 'lifecycleState',
            'job_type': 'jobType',
            'schedule_type': 'scheduleType',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'created_by_id': 'createdById',
            'updated_by_id': 'updatedById',
            'schedule_cron_expression': 'scheduleCronExpression',
            'time_schedule_begin': 'timeScheduleBegin',
            'execution_count': 'executionCount',
            'time_of_latest_execution': 'timeOfLatestExecution',
            'executions': 'executions'
        }

        self._key = None
        self._uri = None
        self._display_name = None
        self._catalog_id = None
        self._job_definition_key = None
        self._lifecycle_state = None
        self._job_type = None
        self._schedule_type = None
        self._description = None
        self._time_created = None
        self._time_updated = None
        self._created_by_id = None
        self._updated_by_id = None
        self._schedule_cron_expression = None
        self._time_schedule_begin = None
        self._execution_count = None
        self._time_of_latest_execution = None
        self._executions = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this JobSummary.
        Unique key of the job.


        :return: The key of this JobSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this JobSummary.
        Unique key of the job.


        :param key: The key of this JobSummary.
        :type: str
        """
        self._key = key

    @property
    def uri(self):
        """
        Gets the uri of this JobSummary.
        URI to the job instance in the API.


        :return: The uri of this JobSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this JobSummary.
        URI to the job instance in the API.


        :param uri: The uri of this JobSummary.
        :type: str
        """
        self._uri = uri

    @property
    def display_name(self):
        """
        Gets the display_name of this JobSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this JobSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this JobSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this JobSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def catalog_id(self):
        """
        Gets the catalog_id of this JobSummary.
        The data catalog's OCID.


        :return: The catalog_id of this JobSummary.
        :rtype: str
        """
        return self._catalog_id

    @catalog_id.setter
    def catalog_id(self, catalog_id):
        """
        Sets the catalog_id of this JobSummary.
        The data catalog's OCID.


        :param catalog_id: The catalog_id of this JobSummary.
        :type: str
        """
        self._catalog_id = catalog_id

    @property
    def job_definition_key(self):
        """
        Gets the job_definition_key of this JobSummary.
        The unique key of the job definition resource that defined the scope of this job.


        :return: The job_definition_key of this JobSummary.
        :rtype: str
        """
        return self._job_definition_key

    @job_definition_key.setter
    def job_definition_key(self, job_definition_key):
        """
        Sets the job_definition_key of this JobSummary.
        The unique key of the job definition resource that defined the scope of this job.


        :param job_definition_key: The job_definition_key of this JobSummary.
        :type: str
        """
        self._job_definition_key = job_definition_key

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this JobSummary.
        Lifecycle state of the job, such as running, paused, or completed.


        :return: The lifecycle_state of this JobSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this JobSummary.
        Lifecycle state of the job, such as running, paused, or completed.


        :param lifecycle_state: The lifecycle_state of this JobSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def job_type(self):
        """
        Gets the job_type of this JobSummary.
        Type of the job.


        :return: The job_type of this JobSummary.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """
        Sets the job_type of this JobSummary.
        Type of the job.


        :param job_type: The job_type of this JobSummary.
        :type: str
        """
        self._job_type = job_type

    @property
    def schedule_type(self):
        """
        Gets the schedule_type of this JobSummary.
        Type of job schedule that is inferred from the scheduling properties.


        :return: The schedule_type of this JobSummary.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this JobSummary.
        Type of job schedule that is inferred from the scheduling properties.


        :param schedule_type: The schedule_type of this JobSummary.
        :type: str
        """
        self._schedule_type = schedule_type

    @property
    def description(self):
        """
        Gets the description of this JobSummary.
        Detailed description of the job.


        :return: The description of this JobSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this JobSummary.
        Detailed description of the job.


        :param description: The description of this JobSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this JobSummary.
        The date and time the job was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this JobSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this JobSummary.
        The date and time the job was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this JobSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this JobSummary.
        Time that this job was last updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this JobSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this JobSummary.
        Time that this job was last updated. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this JobSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def created_by_id(self):
        """
        Gets the created_by_id of this JobSummary.
        OCID of the user who created this job.


        :return: The created_by_id of this JobSummary.
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """
        Sets the created_by_id of this JobSummary.
        OCID of the user who created this job.


        :param created_by_id: The created_by_id of this JobSummary.
        :type: str
        """
        self._created_by_id = created_by_id

    @property
    def updated_by_id(self):
        """
        Gets the updated_by_id of this JobSummary.
        OCID of the user who updated this job.


        :return: The updated_by_id of this JobSummary.
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """
        Sets the updated_by_id of this JobSummary.
        OCID of the user who updated this job.


        :param updated_by_id: The updated_by_id of this JobSummary.
        :type: str
        """
        self._updated_by_id = updated_by_id

    @property
    def schedule_cron_expression(self):
        """
        Gets the schedule_cron_expression of this JobSummary.
        Schedule specified in the cron expression format that has seven fields for second, minute, hour, day-of-month, month, day-of-week, year.
        It can also include special characters like * for all and ? for any. There are also pre-defined schedules that can be specified using
        special strings. For example, @hourly will run the job every hour.


        :return: The schedule_cron_expression of this JobSummary.
        :rtype: str
        """
        return self._schedule_cron_expression

    @schedule_cron_expression.setter
    def schedule_cron_expression(self, schedule_cron_expression):
        """
        Sets the schedule_cron_expression of this JobSummary.
        Schedule specified in the cron expression format that has seven fields for second, minute, hour, day-of-month, month, day-of-week, year.
        It can also include special characters like * for all and ? for any. There are also pre-defined schedules that can be specified using
        special strings. For example, @hourly will run the job every hour.


        :param schedule_cron_expression: The schedule_cron_expression of this JobSummary.
        :type: str
        """
        self._schedule_cron_expression = schedule_cron_expression

    @property
    def time_schedule_begin(self):
        """
        Gets the time_schedule_begin of this JobSummary.
        Date that the schedule should be operational. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_schedule_begin of this JobSummary.
        :rtype: datetime
        """
        return self._time_schedule_begin

    @time_schedule_begin.setter
    def time_schedule_begin(self, time_schedule_begin):
        """
        Sets the time_schedule_begin of this JobSummary.
        Date that the schedule should be operational. An `RFC3339`__ formatted datetime string.

        __ https://tools.ietf.org/html/rfc3339


        :param time_schedule_begin: The time_schedule_begin of this JobSummary.
        :type: datetime
        """
        self._time_schedule_begin = time_schedule_begin

    @property
    def execution_count(self):
        """
        Gets the execution_count of this JobSummary.
        The total number of executions for this job schedule.


        :return: The execution_count of this JobSummary.
        :rtype: int
        """
        return self._execution_count

    @execution_count.setter
    def execution_count(self, execution_count):
        """
        Sets the execution_count of this JobSummary.
        The total number of executions for this job schedule.


        :param execution_count: The execution_count of this JobSummary.
        :type: int
        """
        self._execution_count = execution_count

    @property
    def time_of_latest_execution(self):
        """
        Gets the time_of_latest_execution of this JobSummary.
        The date and time of the most recent execution for this job, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_of_latest_execution of this JobSummary.
        :rtype: datetime
        """
        return self._time_of_latest_execution

    @time_of_latest_execution.setter
    def time_of_latest_execution(self, time_of_latest_execution):
        """
        Sets the time_of_latest_execution of this JobSummary.
        The date and time of the most recent execution for this job, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_of_latest_execution: The time_of_latest_execution of this JobSummary.
        :type: datetime
        """
        self._time_of_latest_execution = time_of_latest_execution

    @property
    def executions(self):
        """
        Gets the executions of this JobSummary.
        Array of the executions summary associated with this job.


        :return: The executions of this JobSummary.
        :rtype: list[JobExecutionSummary]
        """
        return self._executions

    @executions.setter
    def executions(self, executions):
        """
        Sets the executions of this JobSummary.
        Array of the executions summary associated with this job.


        :param executions: The executions of this JobSummary.
        :type: list[JobExecutionSummary]
        """
        self._executions = executions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
