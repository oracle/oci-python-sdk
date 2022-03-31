# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_performance_metric_group import HostPerformanceMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostCpuUsage(HostPerformanceMetricGroup):
    """
    CPU Usage metric for the host
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostCpuUsage object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostCpuUsage.metric_name` attribute
        of this class is ``HOST_CPU_USAGE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostCpuUsage.
            Allowed values for this property are: "HOST_CPU_USAGE", "HOST_MEMORY_USAGE", "HOST_NETWORK_ACTIVITY_SUMMARY", "HOST_TOP_PROCESSES"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostCpuUsage.
        :type time_collected: datetime

        :param cpu_user_mode_in_percent:
            The value to assign to the cpu_user_mode_in_percent property of this HostCpuUsage.
        :type cpu_user_mode_in_percent: float

        :param cpu_system_mode_in_percent:
            The value to assign to the cpu_system_mode_in_percent property of this HostCpuUsage.
        :type cpu_system_mode_in_percent: float

        :param cpu_usage_in_sec:
            The value to assign to the cpu_usage_in_sec property of this HostCpuUsage.
        :type cpu_usage_in_sec: float

        :param cpu_utilization_in_percent:
            The value to assign to the cpu_utilization_in_percent property of this HostCpuUsage.
        :type cpu_utilization_in_percent: float

        :param cpu_stolen_in_percent:
            The value to assign to the cpu_stolen_in_percent property of this HostCpuUsage.
        :type cpu_stolen_in_percent: float

        :param cpu_idle_in_percent:
            The value to assign to the cpu_idle_in_percent property of this HostCpuUsage.
        :type cpu_idle_in_percent: float

        :param cpu_load1min:
            The value to assign to the cpu_load1min property of this HostCpuUsage.
        :type cpu_load1min: float

        :param cpu_load5min:
            The value to assign to the cpu_load5min property of this HostCpuUsage.
        :type cpu_load5min: float

        :param cpu_load15min:
            The value to assign to the cpu_load15min property of this HostCpuUsage.
        :type cpu_load15min: float

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'cpu_user_mode_in_percent': 'float',
            'cpu_system_mode_in_percent': 'float',
            'cpu_usage_in_sec': 'float',
            'cpu_utilization_in_percent': 'float',
            'cpu_stolen_in_percent': 'float',
            'cpu_idle_in_percent': 'float',
            'cpu_load1min': 'float',
            'cpu_load5min': 'float',
            'cpu_load15min': 'float'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'cpu_user_mode_in_percent': 'cpuUserModeInPercent',
            'cpu_system_mode_in_percent': 'cpuSystemModeInPercent',
            'cpu_usage_in_sec': 'cpuUsageInSec',
            'cpu_utilization_in_percent': 'cpuUtilizationInPercent',
            'cpu_stolen_in_percent': 'cpuStolenInPercent',
            'cpu_idle_in_percent': 'cpuIdleInPercent',
            'cpu_load1min': 'cpuLoad1min',
            'cpu_load5min': 'cpuLoad5min',
            'cpu_load15min': 'cpuLoad15min'
        }

        self._metric_name = None
        self._time_collected = None
        self._cpu_user_mode_in_percent = None
        self._cpu_system_mode_in_percent = None
        self._cpu_usage_in_sec = None
        self._cpu_utilization_in_percent = None
        self._cpu_stolen_in_percent = None
        self._cpu_idle_in_percent = None
        self._cpu_load1min = None
        self._cpu_load5min = None
        self._cpu_load15min = None
        self._metric_name = 'HOST_CPU_USAGE'

    @property
    def cpu_user_mode_in_percent(self):
        """
        Gets the cpu_user_mode_in_percent of this HostCpuUsage.
        Percentage of CPU time spent in user mode


        :return: The cpu_user_mode_in_percent of this HostCpuUsage.
        :rtype: float
        """
        return self._cpu_user_mode_in_percent

    @cpu_user_mode_in_percent.setter
    def cpu_user_mode_in_percent(self, cpu_user_mode_in_percent):
        """
        Sets the cpu_user_mode_in_percent of this HostCpuUsage.
        Percentage of CPU time spent in user mode


        :param cpu_user_mode_in_percent: The cpu_user_mode_in_percent of this HostCpuUsage.
        :type: float
        """
        self._cpu_user_mode_in_percent = cpu_user_mode_in_percent

    @property
    def cpu_system_mode_in_percent(self):
        """
        Gets the cpu_system_mode_in_percent of this HostCpuUsage.
        Percentage of CPU time spent in system mode


        :return: The cpu_system_mode_in_percent of this HostCpuUsage.
        :rtype: float
        """
        return self._cpu_system_mode_in_percent

    @cpu_system_mode_in_percent.setter
    def cpu_system_mode_in_percent(self, cpu_system_mode_in_percent):
        """
        Sets the cpu_system_mode_in_percent of this HostCpuUsage.
        Percentage of CPU time spent in system mode


        :param cpu_system_mode_in_percent: The cpu_system_mode_in_percent of this HostCpuUsage.
        :type: float
        """
        self._cpu_system_mode_in_percent = cpu_system_mode_in_percent

    @property
    def cpu_usage_in_sec(self):
        """
        Gets the cpu_usage_in_sec of this HostCpuUsage.
        Amount of CPU Time spent in seconds


        :return: The cpu_usage_in_sec of this HostCpuUsage.
        :rtype: float
        """
        return self._cpu_usage_in_sec

    @cpu_usage_in_sec.setter
    def cpu_usage_in_sec(self, cpu_usage_in_sec):
        """
        Sets the cpu_usage_in_sec of this HostCpuUsage.
        Amount of CPU Time spent in seconds


        :param cpu_usage_in_sec: The cpu_usage_in_sec of this HostCpuUsage.
        :type: float
        """
        self._cpu_usage_in_sec = cpu_usage_in_sec

    @property
    def cpu_utilization_in_percent(self):
        """
        Gets the cpu_utilization_in_percent of this HostCpuUsage.
        Amount of CPU Time spent in percentage


        :return: The cpu_utilization_in_percent of this HostCpuUsage.
        :rtype: float
        """
        return self._cpu_utilization_in_percent

    @cpu_utilization_in_percent.setter
    def cpu_utilization_in_percent(self, cpu_utilization_in_percent):
        """
        Sets the cpu_utilization_in_percent of this HostCpuUsage.
        Amount of CPU Time spent in percentage


        :param cpu_utilization_in_percent: The cpu_utilization_in_percent of this HostCpuUsage.
        :type: float
        """
        self._cpu_utilization_in_percent = cpu_utilization_in_percent

    @property
    def cpu_stolen_in_percent(self):
        """
        Gets the cpu_stolen_in_percent of this HostCpuUsage.
        Amount of CPU time stolen in percentage


        :return: The cpu_stolen_in_percent of this HostCpuUsage.
        :rtype: float
        """
        return self._cpu_stolen_in_percent

    @cpu_stolen_in_percent.setter
    def cpu_stolen_in_percent(self, cpu_stolen_in_percent):
        """
        Sets the cpu_stolen_in_percent of this HostCpuUsage.
        Amount of CPU time stolen in percentage


        :param cpu_stolen_in_percent: The cpu_stolen_in_percent of this HostCpuUsage.
        :type: float
        """
        self._cpu_stolen_in_percent = cpu_stolen_in_percent

    @property
    def cpu_idle_in_percent(self):
        """
        Gets the cpu_idle_in_percent of this HostCpuUsage.
        Amount of CPU idle time in percentage


        :return: The cpu_idle_in_percent of this HostCpuUsage.
        :rtype: float
        """
        return self._cpu_idle_in_percent

    @cpu_idle_in_percent.setter
    def cpu_idle_in_percent(self, cpu_idle_in_percent):
        """
        Sets the cpu_idle_in_percent of this HostCpuUsage.
        Amount of CPU idle time in percentage


        :param cpu_idle_in_percent: The cpu_idle_in_percent of this HostCpuUsage.
        :type: float
        """
        self._cpu_idle_in_percent = cpu_idle_in_percent

    @property
    def cpu_load1min(self):
        """
        Gets the cpu_load1min of this HostCpuUsage.
        Load average in the last 1 minute


        :return: The cpu_load1min of this HostCpuUsage.
        :rtype: float
        """
        return self._cpu_load1min

    @cpu_load1min.setter
    def cpu_load1min(self, cpu_load1min):
        """
        Sets the cpu_load1min of this HostCpuUsage.
        Load average in the last 1 minute


        :param cpu_load1min: The cpu_load1min of this HostCpuUsage.
        :type: float
        """
        self._cpu_load1min = cpu_load1min

    @property
    def cpu_load5min(self):
        """
        Gets the cpu_load5min of this HostCpuUsage.
        Load average in the last 5 minutes


        :return: The cpu_load5min of this HostCpuUsage.
        :rtype: float
        """
        return self._cpu_load5min

    @cpu_load5min.setter
    def cpu_load5min(self, cpu_load5min):
        """
        Sets the cpu_load5min of this HostCpuUsage.
        Load average in the last 5 minutes


        :param cpu_load5min: The cpu_load5min of this HostCpuUsage.
        :type: float
        """
        self._cpu_load5min = cpu_load5min

    @property
    def cpu_load15min(self):
        """
        Gets the cpu_load15min of this HostCpuUsage.
        Load average in the last 15 minutes


        :return: The cpu_load15min of this HostCpuUsage.
        :rtype: float
        """
        return self._cpu_load15min

    @cpu_load15min.setter
    def cpu_load15min(self, cpu_load15min):
        """
        Sets the cpu_load15min of this HostCpuUsage.
        Load average in the last 15 minutes


        :param cpu_load15min: The cpu_load15min of this HostCpuUsage.
        :type: float
        """
        self._cpu_load15min = cpu_load15min

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
