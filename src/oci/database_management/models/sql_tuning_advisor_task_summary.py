# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningAdvisorTaskSummary(object):
    """
    The summary of a SQL Tuning Advisor task.
    """

    #: A constant which can be used with the task_status property of a SqlTuningAdvisorTaskSummary.
    #: This constant has a value of "COMPLETED"
    TASK_STATUS_COMPLETED = "COMPLETED"

    #: A constant which can be used with the task_status property of a SqlTuningAdvisorTaskSummary.
    #: This constant has a value of "INITIAL"
    TASK_STATUS_INITIAL = "INITIAL"

    #: A constant which can be used with the task_status property of a SqlTuningAdvisorTaskSummary.
    #: This constant has a value of "EXECUTING"
    TASK_STATUS_EXECUTING = "EXECUTING"

    #: A constant which can be used with the task_status property of a SqlTuningAdvisorTaskSummary.
    #: This constant has a value of "INTERRUPTED"
    TASK_STATUS_INTERRUPTED = "INTERRUPTED"

    #: A constant which can be used with the task_status property of a SqlTuningAdvisorTaskSummary.
    #: This constant has a value of "ERROR"
    TASK_STATUS_ERROR = "ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningAdvisorTaskSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sql_tuning_advisor_task_id:
            The value to assign to the sql_tuning_advisor_task_id property of this SqlTuningAdvisorTaskSummary.
        :type sql_tuning_advisor_task_id: int

        :param instance_id:
            The value to assign to the instance_id property of this SqlTuningAdvisorTaskSummary.
        :type instance_id: int

        :param name:
            The value to assign to the name property of this SqlTuningAdvisorTaskSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this SqlTuningAdvisorTaskSummary.
        :type description: str

        :param owner:
            The value to assign to the owner property of this SqlTuningAdvisorTaskSummary.
        :type owner: str

        :param time_created:
            The value to assign to the time_created property of this SqlTuningAdvisorTaskSummary.
        :type time_created: datetime

        :param task_status:
            The value to assign to the task_status property of this SqlTuningAdvisorTaskSummary.
            Allowed values for this property are: "COMPLETED", "INITIAL", "EXECUTING", "INTERRUPTED", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type task_status: str

        :param days_to_expire:
            The value to assign to the days_to_expire property of this SqlTuningAdvisorTaskSummary.
        :type days_to_expire: int

        :param time_execution_started:
            The value to assign to the time_execution_started property of this SqlTuningAdvisorTaskSummary.
        :type time_execution_started: datetime

        :param time_execution_ended:
            The value to assign to the time_execution_ended property of this SqlTuningAdvisorTaskSummary.
        :type time_execution_ended: datetime

        :param total_sql_statements:
            The value to assign to the total_sql_statements property of this SqlTuningAdvisorTaskSummary.
        :type total_sql_statements: int

        :param recommendation_count:
            The value to assign to the recommendation_count property of this SqlTuningAdvisorTaskSummary.
        :type recommendation_count: int

        """
        self.swagger_types = {
            'sql_tuning_advisor_task_id': 'int',
            'instance_id': 'int',
            'name': 'str',
            'description': 'str',
            'owner': 'str',
            'time_created': 'datetime',
            'task_status': 'str',
            'days_to_expire': 'int',
            'time_execution_started': 'datetime',
            'time_execution_ended': 'datetime',
            'total_sql_statements': 'int',
            'recommendation_count': 'int'
        }

        self.attribute_map = {
            'sql_tuning_advisor_task_id': 'sqlTuningAdvisorTaskId',
            'instance_id': 'instanceId',
            'name': 'name',
            'description': 'description',
            'owner': 'owner',
            'time_created': 'timeCreated',
            'task_status': 'taskStatus',
            'days_to_expire': 'daysToExpire',
            'time_execution_started': 'timeExecutionStarted',
            'time_execution_ended': 'timeExecutionEnded',
            'total_sql_statements': 'totalSqlStatements',
            'recommendation_count': 'recommendationCount'
        }

        self._sql_tuning_advisor_task_id = None
        self._instance_id = None
        self._name = None
        self._description = None
        self._owner = None
        self._time_created = None
        self._task_status = None
        self._days_to_expire = None
        self._time_execution_started = None
        self._time_execution_ended = None
        self._total_sql_statements = None
        self._recommendation_count = None

    @property
    def sql_tuning_advisor_task_id(self):
        """
        **[Required]** Gets the sql_tuning_advisor_task_id of this SqlTuningAdvisorTaskSummary.
        The unique identifier of the SQL Tuning Advisor task. This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The sql_tuning_advisor_task_id of this SqlTuningAdvisorTaskSummary.
        :rtype: int
        """
        return self._sql_tuning_advisor_task_id

    @sql_tuning_advisor_task_id.setter
    def sql_tuning_advisor_task_id(self, sql_tuning_advisor_task_id):
        """
        Sets the sql_tuning_advisor_task_id of this SqlTuningAdvisorTaskSummary.
        The unique identifier of the SQL Tuning Advisor task. This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param sql_tuning_advisor_task_id: The sql_tuning_advisor_task_id of this SqlTuningAdvisorTaskSummary.
        :type: int
        """
        self._sql_tuning_advisor_task_id = sql_tuning_advisor_task_id

    @property
    def instance_id(self):
        """
        Gets the instance_id of this SqlTuningAdvisorTaskSummary.
        The instance ID of the SQL Tuning Advisor task. This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The instance_id of this SqlTuningAdvisorTaskSummary.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """
        Sets the instance_id of this SqlTuningAdvisorTaskSummary.
        The instance ID of the SQL Tuning Advisor task. This is not the `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param instance_id: The instance_id of this SqlTuningAdvisorTaskSummary.
        :type: int
        """
        self._instance_id = instance_id

    @property
    def name(self):
        """
        Gets the name of this SqlTuningAdvisorTaskSummary.
        The name of the SQL Tuning Advisor task.


        :return: The name of this SqlTuningAdvisorTaskSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SqlTuningAdvisorTaskSummary.
        The name of the SQL Tuning Advisor task.


        :param name: The name of this SqlTuningAdvisorTaskSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this SqlTuningAdvisorTaskSummary.
        The description of the SQL Tuning Advisor task.


        :return: The description of this SqlTuningAdvisorTaskSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SqlTuningAdvisorTaskSummary.
        The description of the SQL Tuning Advisor task.


        :param description: The description of this SqlTuningAdvisorTaskSummary.
        :type: str
        """
        self._description = description

    @property
    def owner(self):
        """
        Gets the owner of this SqlTuningAdvisorTaskSummary.
        The owner of the SQL Tuning Advisor task.


        :return: The owner of this SqlTuningAdvisorTaskSummary.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this SqlTuningAdvisorTaskSummary.
        The owner of the SQL Tuning Advisor task.


        :param owner: The owner of this SqlTuningAdvisorTaskSummary.
        :type: str
        """
        self._owner = owner

    @property
    def time_created(self):
        """
        Gets the time_created of this SqlTuningAdvisorTaskSummary.
        The Creation date of the SQL Tuning Advisor task.


        :return: The time_created of this SqlTuningAdvisorTaskSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SqlTuningAdvisorTaskSummary.
        The Creation date of the SQL Tuning Advisor task.


        :param time_created: The time_created of this SqlTuningAdvisorTaskSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def task_status(self):
        """
        Gets the task_status of this SqlTuningAdvisorTaskSummary.
        The status of the SQL Tuning Advisor task.

        Allowed values for this property are: "COMPLETED", "INITIAL", "EXECUTING", "INTERRUPTED", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The task_status of this SqlTuningAdvisorTaskSummary.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """
        Sets the task_status of this SqlTuningAdvisorTaskSummary.
        The status of the SQL Tuning Advisor task.


        :param task_status: The task_status of this SqlTuningAdvisorTaskSummary.
        :type: str
        """
        allowed_values = ["COMPLETED", "INITIAL", "EXECUTING", "INTERRUPTED", "ERROR"]
        if not value_allowed_none_or_none_sentinel(task_status, allowed_values):
            task_status = 'UNKNOWN_ENUM_VALUE'
        self._task_status = task_status

    @property
    def days_to_expire(self):
        """
        Gets the days_to_expire of this SqlTuningAdvisorTaskSummary.
        The number of days left before the task expires. If the value equals -1, then the task has no expiration time (UNLIMITED).


        :return: The days_to_expire of this SqlTuningAdvisorTaskSummary.
        :rtype: int
        """
        return self._days_to_expire

    @days_to_expire.setter
    def days_to_expire(self, days_to_expire):
        """
        Sets the days_to_expire of this SqlTuningAdvisorTaskSummary.
        The number of days left before the task expires. If the value equals -1, then the task has no expiration time (UNLIMITED).


        :param days_to_expire: The days_to_expire of this SqlTuningAdvisorTaskSummary.
        :type: int
        """
        self._days_to_expire = days_to_expire

    @property
    def time_execution_started(self):
        """
        Gets the time_execution_started of this SqlTuningAdvisorTaskSummary.
        The start time of the task execution.


        :return: The time_execution_started of this SqlTuningAdvisorTaskSummary.
        :rtype: datetime
        """
        return self._time_execution_started

    @time_execution_started.setter
    def time_execution_started(self, time_execution_started):
        """
        Sets the time_execution_started of this SqlTuningAdvisorTaskSummary.
        The start time of the task execution.


        :param time_execution_started: The time_execution_started of this SqlTuningAdvisorTaskSummary.
        :type: datetime
        """
        self._time_execution_started = time_execution_started

    @property
    def time_execution_ended(self):
        """
        Gets the time_execution_ended of this SqlTuningAdvisorTaskSummary.
        The end time of the task execution.


        :return: The time_execution_ended of this SqlTuningAdvisorTaskSummary.
        :rtype: datetime
        """
        return self._time_execution_ended

    @time_execution_ended.setter
    def time_execution_ended(self, time_execution_ended):
        """
        Sets the time_execution_ended of this SqlTuningAdvisorTaskSummary.
        The end time of the task execution.


        :param time_execution_ended: The time_execution_ended of this SqlTuningAdvisorTaskSummary.
        :type: datetime
        """
        self._time_execution_ended = time_execution_ended

    @property
    def total_sql_statements(self):
        """
        Gets the total_sql_statements of this SqlTuningAdvisorTaskSummary.
        The total number of SQL statements related to the SQL Tuning Advisor task.


        :return: The total_sql_statements of this SqlTuningAdvisorTaskSummary.
        :rtype: int
        """
        return self._total_sql_statements

    @total_sql_statements.setter
    def total_sql_statements(self, total_sql_statements):
        """
        Sets the total_sql_statements of this SqlTuningAdvisorTaskSummary.
        The total number of SQL statements related to the SQL Tuning Advisor task.


        :param total_sql_statements: The total_sql_statements of this SqlTuningAdvisorTaskSummary.
        :type: int
        """
        self._total_sql_statements = total_sql_statements

    @property
    def recommendation_count(self):
        """
        Gets the recommendation_count of this SqlTuningAdvisorTaskSummary.
        The number of recommendations provided for the SQL Tuning Advisor task.


        :return: The recommendation_count of this SqlTuningAdvisorTaskSummary.
        :rtype: int
        """
        return self._recommendation_count

    @recommendation_count.setter
    def recommendation_count(self, recommendation_count):
        """
        Sets the recommendation_count of this SqlTuningAdvisorTaskSummary.
        The number of recommendations provided for the SQL Tuning Advisor task.


        :param recommendation_count: The recommendation_count of this SqlTuningAdvisorTaskSummary.
        :type: int
        """
        self._recommendation_count = recommendation_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
