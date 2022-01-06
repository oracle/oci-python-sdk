# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlStatistics(object):
    """
    Performance statistics for the SQL.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlStatistics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param database_time_in_sec:
            The value to assign to the database_time_in_sec property of this SqlStatistics.
        :type database_time_in_sec: float

        :param executions_per_hour:
            The value to assign to the executions_per_hour property of this SqlStatistics.
        :type executions_per_hour: float

        :param executions_count:
            The value to assign to the executions_count property of this SqlStatistics.
        :type executions_count: int

        :param cpu_time_in_sec:
            The value to assign to the cpu_time_in_sec property of this SqlStatistics.
        :type cpu_time_in_sec: float

        :param io_time_in_sec:
            The value to assign to the io_time_in_sec property of this SqlStatistics.
        :type io_time_in_sec: float

        :param inefficient_wait_time_in_sec:
            The value to assign to the inefficient_wait_time_in_sec property of this SqlStatistics.
        :type inefficient_wait_time_in_sec: float

        :param response_time_in_sec:
            The value to assign to the response_time_in_sec property of this SqlStatistics.
        :type response_time_in_sec: float

        :param plan_count:
            The value to assign to the plan_count property of this SqlStatistics.
        :type plan_count: int

        :param variability:
            The value to assign to the variability property of this SqlStatistics.
        :type variability: float

        :param average_active_sessions:
            The value to assign to the average_active_sessions property of this SqlStatistics.
        :type average_active_sessions: float

        :param database_time_pct:
            The value to assign to the database_time_pct property of this SqlStatistics.
        :type database_time_pct: float

        :param inefficiency_in_pct:
            The value to assign to the inefficiency_in_pct property of this SqlStatistics.
        :type inefficiency_in_pct: float

        :param change_in_cpu_time_in_pct:
            The value to assign to the change_in_cpu_time_in_pct property of this SqlStatistics.
        :type change_in_cpu_time_in_pct: float

        :param change_in_io_time_in_pct:
            The value to assign to the change_in_io_time_in_pct property of this SqlStatistics.
        :type change_in_io_time_in_pct: float

        :param change_in_inefficient_wait_time_in_pct:
            The value to assign to the change_in_inefficient_wait_time_in_pct property of this SqlStatistics.
        :type change_in_inefficient_wait_time_in_pct: float

        :param change_in_response_time_in_pct:
            The value to assign to the change_in_response_time_in_pct property of this SqlStatistics.
        :type change_in_response_time_in_pct: float

        :param change_in_average_active_sessions_in_pct:
            The value to assign to the change_in_average_active_sessions_in_pct property of this SqlStatistics.
        :type change_in_average_active_sessions_in_pct: float

        :param change_in_executions_per_hour_in_pct:
            The value to assign to the change_in_executions_per_hour_in_pct property of this SqlStatistics.
        :type change_in_executions_per_hour_in_pct: float

        :param change_in_inefficiency_in_pct:
            The value to assign to the change_in_inefficiency_in_pct property of this SqlStatistics.
        :type change_in_inefficiency_in_pct: float

        """
        self.swagger_types = {
            'database_time_in_sec': 'float',
            'executions_per_hour': 'float',
            'executions_count': 'int',
            'cpu_time_in_sec': 'float',
            'io_time_in_sec': 'float',
            'inefficient_wait_time_in_sec': 'float',
            'response_time_in_sec': 'float',
            'plan_count': 'int',
            'variability': 'float',
            'average_active_sessions': 'float',
            'database_time_pct': 'float',
            'inefficiency_in_pct': 'float',
            'change_in_cpu_time_in_pct': 'float',
            'change_in_io_time_in_pct': 'float',
            'change_in_inefficient_wait_time_in_pct': 'float',
            'change_in_response_time_in_pct': 'float',
            'change_in_average_active_sessions_in_pct': 'float',
            'change_in_executions_per_hour_in_pct': 'float',
            'change_in_inefficiency_in_pct': 'float'
        }

        self.attribute_map = {
            'database_time_in_sec': 'databaseTimeInSec',
            'executions_per_hour': 'executionsPerHour',
            'executions_count': 'executionsCount',
            'cpu_time_in_sec': 'cpuTimeInSec',
            'io_time_in_sec': 'ioTimeInSec',
            'inefficient_wait_time_in_sec': 'inefficientWaitTimeInSec',
            'response_time_in_sec': 'responseTimeInSec',
            'plan_count': 'planCount',
            'variability': 'variability',
            'average_active_sessions': 'averageActiveSessions',
            'database_time_pct': 'databaseTimePct',
            'inefficiency_in_pct': 'inefficiencyInPct',
            'change_in_cpu_time_in_pct': 'changeInCpuTimeInPct',
            'change_in_io_time_in_pct': 'changeInIoTimeInPct',
            'change_in_inefficient_wait_time_in_pct': 'changeInInefficientWaitTimeInPct',
            'change_in_response_time_in_pct': 'changeInResponseTimeInPct',
            'change_in_average_active_sessions_in_pct': 'changeInAverageActiveSessionsInPct',
            'change_in_executions_per_hour_in_pct': 'changeInExecutionsPerHourInPct',
            'change_in_inefficiency_in_pct': 'changeInInefficiencyInPct'
        }

        self._database_time_in_sec = None
        self._executions_per_hour = None
        self._executions_count = None
        self._cpu_time_in_sec = None
        self._io_time_in_sec = None
        self._inefficient_wait_time_in_sec = None
        self._response_time_in_sec = None
        self._plan_count = None
        self._variability = None
        self._average_active_sessions = None
        self._database_time_pct = None
        self._inefficiency_in_pct = None
        self._change_in_cpu_time_in_pct = None
        self._change_in_io_time_in_pct = None
        self._change_in_inefficient_wait_time_in_pct = None
        self._change_in_response_time_in_pct = None
        self._change_in_average_active_sessions_in_pct = None
        self._change_in_executions_per_hour_in_pct = None
        self._change_in_inefficiency_in_pct = None

    @property
    def database_time_in_sec(self):
        """
        **[Required]** Gets the database_time_in_sec of this SqlStatistics.
        Database Time in seconds


        :return: The database_time_in_sec of this SqlStatistics.
        :rtype: float
        """
        return self._database_time_in_sec

    @database_time_in_sec.setter
    def database_time_in_sec(self, database_time_in_sec):
        """
        Sets the database_time_in_sec of this SqlStatistics.
        Database Time in seconds


        :param database_time_in_sec: The database_time_in_sec of this SqlStatistics.
        :type: float
        """
        self._database_time_in_sec = database_time_in_sec

    @property
    def executions_per_hour(self):
        """
        **[Required]** Gets the executions_per_hour of this SqlStatistics.
        Number of executions per hour


        :return: The executions_per_hour of this SqlStatistics.
        :rtype: float
        """
        return self._executions_per_hour

    @executions_per_hour.setter
    def executions_per_hour(self, executions_per_hour):
        """
        Sets the executions_per_hour of this SqlStatistics.
        Number of executions per hour


        :param executions_per_hour: The executions_per_hour of this SqlStatistics.
        :type: float
        """
        self._executions_per_hour = executions_per_hour

    @property
    def executions_count(self):
        """
        **[Required]** Gets the executions_count of this SqlStatistics.
        Total number of executions


        :return: The executions_count of this SqlStatistics.
        :rtype: int
        """
        return self._executions_count

    @executions_count.setter
    def executions_count(self, executions_count):
        """
        Sets the executions_count of this SqlStatistics.
        Total number of executions


        :param executions_count: The executions_count of this SqlStatistics.
        :type: int
        """
        self._executions_count = executions_count

    @property
    def cpu_time_in_sec(self):
        """
        **[Required]** Gets the cpu_time_in_sec of this SqlStatistics.
        CPU Time in seconds


        :return: The cpu_time_in_sec of this SqlStatistics.
        :rtype: float
        """
        return self._cpu_time_in_sec

    @cpu_time_in_sec.setter
    def cpu_time_in_sec(self, cpu_time_in_sec):
        """
        Sets the cpu_time_in_sec of this SqlStatistics.
        CPU Time in seconds


        :param cpu_time_in_sec: The cpu_time_in_sec of this SqlStatistics.
        :type: float
        """
        self._cpu_time_in_sec = cpu_time_in_sec

    @property
    def io_time_in_sec(self):
        """
        **[Required]** Gets the io_time_in_sec of this SqlStatistics.
        I/O Time in seconds


        :return: The io_time_in_sec of this SqlStatistics.
        :rtype: float
        """
        return self._io_time_in_sec

    @io_time_in_sec.setter
    def io_time_in_sec(self, io_time_in_sec):
        """
        Sets the io_time_in_sec of this SqlStatistics.
        I/O Time in seconds


        :param io_time_in_sec: The io_time_in_sec of this SqlStatistics.
        :type: float
        """
        self._io_time_in_sec = io_time_in_sec

    @property
    def inefficient_wait_time_in_sec(self):
        """
        **[Required]** Gets the inefficient_wait_time_in_sec of this SqlStatistics.
        Inefficient Wait Time in seconds


        :return: The inefficient_wait_time_in_sec of this SqlStatistics.
        :rtype: float
        """
        return self._inefficient_wait_time_in_sec

    @inefficient_wait_time_in_sec.setter
    def inefficient_wait_time_in_sec(self, inefficient_wait_time_in_sec):
        """
        Sets the inefficient_wait_time_in_sec of this SqlStatistics.
        Inefficient Wait Time in seconds


        :param inefficient_wait_time_in_sec: The inefficient_wait_time_in_sec of this SqlStatistics.
        :type: float
        """
        self._inefficient_wait_time_in_sec = inefficient_wait_time_in_sec

    @property
    def response_time_in_sec(self):
        """
        **[Required]** Gets the response_time_in_sec of this SqlStatistics.
        Response time is the average elaspsed time per execution. It is the ratio of Total Database Time to the number of executions


        :return: The response_time_in_sec of this SqlStatistics.
        :rtype: float
        """
        return self._response_time_in_sec

    @response_time_in_sec.setter
    def response_time_in_sec(self, response_time_in_sec):
        """
        Sets the response_time_in_sec of this SqlStatistics.
        Response time is the average elaspsed time per execution. It is the ratio of Total Database Time to the number of executions


        :param response_time_in_sec: The response_time_in_sec of this SqlStatistics.
        :type: float
        """
        self._response_time_in_sec = response_time_in_sec

    @property
    def plan_count(self):
        """
        **[Required]** Gets the plan_count of this SqlStatistics.
        Number of SQL execution plans used by the SQL


        :return: The plan_count of this SqlStatistics.
        :rtype: int
        """
        return self._plan_count

    @plan_count.setter
    def plan_count(self, plan_count):
        """
        Sets the plan_count of this SqlStatistics.
        Number of SQL execution plans used by the SQL


        :param plan_count: The plan_count of this SqlStatistics.
        :type: int
        """
        self._plan_count = plan_count

    @property
    def variability(self):
        """
        **[Required]** Gets the variability of this SqlStatistics.
        Variability is the ratio of the standard deviation in response time to the mean of response time of the SQL


        :return: The variability of this SqlStatistics.
        :rtype: float
        """
        return self._variability

    @variability.setter
    def variability(self, variability):
        """
        Sets the variability of this SqlStatistics.
        Variability is the ratio of the standard deviation in response time to the mean of response time of the SQL


        :param variability: The variability of this SqlStatistics.
        :type: float
        """
        self._variability = variability

    @property
    def average_active_sessions(self):
        """
        **[Required]** Gets the average_active_sessions of this SqlStatistics.
        Average Active Sessions represent the average active sessions at a point in time. It is the number of sessions that are either working or waiting.


        :return: The average_active_sessions of this SqlStatistics.
        :rtype: float
        """
        return self._average_active_sessions

    @average_active_sessions.setter
    def average_active_sessions(self, average_active_sessions):
        """
        Sets the average_active_sessions of this SqlStatistics.
        Average Active Sessions represent the average active sessions at a point in time. It is the number of sessions that are either working or waiting.


        :param average_active_sessions: The average_active_sessions of this SqlStatistics.
        :type: float
        """
        self._average_active_sessions = average_active_sessions

    @property
    def database_time_pct(self):
        """
        **[Required]** Gets the database_time_pct of this SqlStatistics.
        Percentage of Database Time


        :return: The database_time_pct of this SqlStatistics.
        :rtype: float
        """
        return self._database_time_pct

    @database_time_pct.setter
    def database_time_pct(self, database_time_pct):
        """
        Sets the database_time_pct of this SqlStatistics.
        Percentage of Database Time


        :param database_time_pct: The database_time_pct of this SqlStatistics.
        :type: float
        """
        self._database_time_pct = database_time_pct

    @property
    def inefficiency_in_pct(self):
        """
        **[Required]** Gets the inefficiency_in_pct of this SqlStatistics.
        Percentage of Inefficiency. It is calculated by Total Database Time divided by Total Wait Time


        :return: The inefficiency_in_pct of this SqlStatistics.
        :rtype: float
        """
        return self._inefficiency_in_pct

    @inefficiency_in_pct.setter
    def inefficiency_in_pct(self, inefficiency_in_pct):
        """
        Sets the inefficiency_in_pct of this SqlStatistics.
        Percentage of Inefficiency. It is calculated by Total Database Time divided by Total Wait Time


        :param inefficiency_in_pct: The inefficiency_in_pct of this SqlStatistics.
        :type: float
        """
        self._inefficiency_in_pct = inefficiency_in_pct

    @property
    def change_in_cpu_time_in_pct(self):
        """
        **[Required]** Gets the change_in_cpu_time_in_pct of this SqlStatistics.
        Percent change in CPU Time based on linear regression


        :return: The change_in_cpu_time_in_pct of this SqlStatistics.
        :rtype: float
        """
        return self._change_in_cpu_time_in_pct

    @change_in_cpu_time_in_pct.setter
    def change_in_cpu_time_in_pct(self, change_in_cpu_time_in_pct):
        """
        Sets the change_in_cpu_time_in_pct of this SqlStatistics.
        Percent change in CPU Time based on linear regression


        :param change_in_cpu_time_in_pct: The change_in_cpu_time_in_pct of this SqlStatistics.
        :type: float
        """
        self._change_in_cpu_time_in_pct = change_in_cpu_time_in_pct

    @property
    def change_in_io_time_in_pct(self):
        """
        **[Required]** Gets the change_in_io_time_in_pct of this SqlStatistics.
        Percent change in IO Time based on linear regression


        :return: The change_in_io_time_in_pct of this SqlStatistics.
        :rtype: float
        """
        return self._change_in_io_time_in_pct

    @change_in_io_time_in_pct.setter
    def change_in_io_time_in_pct(self, change_in_io_time_in_pct):
        """
        Sets the change_in_io_time_in_pct of this SqlStatistics.
        Percent change in IO Time based on linear regression


        :param change_in_io_time_in_pct: The change_in_io_time_in_pct of this SqlStatistics.
        :type: float
        """
        self._change_in_io_time_in_pct = change_in_io_time_in_pct

    @property
    def change_in_inefficient_wait_time_in_pct(self):
        """
        **[Required]** Gets the change_in_inefficient_wait_time_in_pct of this SqlStatistics.
        Percent change in Inefficient Wait Time based on linear regression


        :return: The change_in_inefficient_wait_time_in_pct of this SqlStatistics.
        :rtype: float
        """
        return self._change_in_inefficient_wait_time_in_pct

    @change_in_inefficient_wait_time_in_pct.setter
    def change_in_inefficient_wait_time_in_pct(self, change_in_inefficient_wait_time_in_pct):
        """
        Sets the change_in_inefficient_wait_time_in_pct of this SqlStatistics.
        Percent change in Inefficient Wait Time based on linear regression


        :param change_in_inefficient_wait_time_in_pct: The change_in_inefficient_wait_time_in_pct of this SqlStatistics.
        :type: float
        """
        self._change_in_inefficient_wait_time_in_pct = change_in_inefficient_wait_time_in_pct

    @property
    def change_in_response_time_in_pct(self):
        """
        **[Required]** Gets the change_in_response_time_in_pct of this SqlStatistics.
        Percent change in Response Time based on linear regression


        :return: The change_in_response_time_in_pct of this SqlStatistics.
        :rtype: float
        """
        return self._change_in_response_time_in_pct

    @change_in_response_time_in_pct.setter
    def change_in_response_time_in_pct(self, change_in_response_time_in_pct):
        """
        Sets the change_in_response_time_in_pct of this SqlStatistics.
        Percent change in Response Time based on linear regression


        :param change_in_response_time_in_pct: The change_in_response_time_in_pct of this SqlStatistics.
        :type: float
        """
        self._change_in_response_time_in_pct = change_in_response_time_in_pct

    @property
    def change_in_average_active_sessions_in_pct(self):
        """
        **[Required]** Gets the change_in_average_active_sessions_in_pct of this SqlStatistics.
        Percent change in Average Active Sessions based on linear regression


        :return: The change_in_average_active_sessions_in_pct of this SqlStatistics.
        :rtype: float
        """
        return self._change_in_average_active_sessions_in_pct

    @change_in_average_active_sessions_in_pct.setter
    def change_in_average_active_sessions_in_pct(self, change_in_average_active_sessions_in_pct):
        """
        Sets the change_in_average_active_sessions_in_pct of this SqlStatistics.
        Percent change in Average Active Sessions based on linear regression


        :param change_in_average_active_sessions_in_pct: The change_in_average_active_sessions_in_pct of this SqlStatistics.
        :type: float
        """
        self._change_in_average_active_sessions_in_pct = change_in_average_active_sessions_in_pct

    @property
    def change_in_executions_per_hour_in_pct(self):
        """
        **[Required]** Gets the change_in_executions_per_hour_in_pct of this SqlStatistics.
        Percent change in Executions per hour based on linear regression


        :return: The change_in_executions_per_hour_in_pct of this SqlStatistics.
        :rtype: float
        """
        return self._change_in_executions_per_hour_in_pct

    @change_in_executions_per_hour_in_pct.setter
    def change_in_executions_per_hour_in_pct(self, change_in_executions_per_hour_in_pct):
        """
        Sets the change_in_executions_per_hour_in_pct of this SqlStatistics.
        Percent change in Executions per hour based on linear regression


        :param change_in_executions_per_hour_in_pct: The change_in_executions_per_hour_in_pct of this SqlStatistics.
        :type: float
        """
        self._change_in_executions_per_hour_in_pct = change_in_executions_per_hour_in_pct

    @property
    def change_in_inefficiency_in_pct(self):
        """
        **[Required]** Gets the change_in_inefficiency_in_pct of this SqlStatistics.
        Percent change in Inefficiency based on linear regression


        :return: The change_in_inefficiency_in_pct of this SqlStatistics.
        :rtype: float
        """
        return self._change_in_inefficiency_in_pct

    @change_in_inefficiency_in_pct.setter
    def change_in_inefficiency_in_pct(self, change_in_inefficiency_in_pct):
        """
        Sets the change_in_inefficiency_in_pct of this SqlStatistics.
        Percent change in Inefficiency based on linear regression


        :param change_in_inefficiency_in_pct: The change_in_inefficiency_in_pct of this SqlStatistics.
        :type: float
        """
        self._change_in_inefficiency_in_pct = change_in_inefficiency_in_pct

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
