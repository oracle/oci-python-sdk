# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TopProcessesUsageTrend(object):
    """
    Aggregated data for top processes
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TopProcessesUsageTrend object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param end_timestamp:
            The value to assign to the end_timestamp property of this TopProcessesUsageTrend.
        :type end_timestamp: datetime

        :param cpu_usage:
            The value to assign to the cpu_usage property of this TopProcessesUsageTrend.
        :type cpu_usage: float

        :param cpu_utilization:
            The value to assign to the cpu_utilization property of this TopProcessesUsageTrend.
        :type cpu_utilization: float

        :param memory_utilization:
            The value to assign to the memory_utilization property of this TopProcessesUsageTrend.
        :type memory_utilization: float

        :param virtual_memory_in_mbs:
            The value to assign to the virtual_memory_in_mbs property of this TopProcessesUsageTrend.
        :type virtual_memory_in_mbs: float

        :param physical_memory_in_mbs:
            The value to assign to the physical_memory_in_mbs property of this TopProcessesUsageTrend.
        :type physical_memory_in_mbs: float

        :param max_process_count:
            The value to assign to the max_process_count property of this TopProcessesUsageTrend.
        :type max_process_count: int

        """
        self.swagger_types = {
            'end_timestamp': 'datetime',
            'cpu_usage': 'float',
            'cpu_utilization': 'float',
            'memory_utilization': 'float',
            'virtual_memory_in_mbs': 'float',
            'physical_memory_in_mbs': 'float',
            'max_process_count': 'int'
        }

        self.attribute_map = {
            'end_timestamp': 'endTimestamp',
            'cpu_usage': 'cpuUsage',
            'cpu_utilization': 'cpuUtilization',
            'memory_utilization': 'memoryUtilization',
            'virtual_memory_in_mbs': 'virtualMemoryInMBs',
            'physical_memory_in_mbs': 'physicalMemoryInMBs',
            'max_process_count': 'maxProcessCount'
        }

        self._end_timestamp = None
        self._cpu_usage = None
        self._cpu_utilization = None
        self._memory_utilization = None
        self._virtual_memory_in_mbs = None
        self._physical_memory_in_mbs = None
        self._max_process_count = None

    @property
    def end_timestamp(self):
        """
        **[Required]** Gets the end_timestamp of this TopProcessesUsageTrend.
        The timestamp in which the current sampling period ends in RFC 3339 format.


        :return: The end_timestamp of this TopProcessesUsageTrend.
        :rtype: datetime
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """
        Sets the end_timestamp of this TopProcessesUsageTrend.
        The timestamp in which the current sampling period ends in RFC 3339 format.


        :param end_timestamp: The end_timestamp of this TopProcessesUsageTrend.
        :type: datetime
        """
        self._end_timestamp = end_timestamp

    @property
    def cpu_usage(self):
        """
        **[Required]** Gets the cpu_usage of this TopProcessesUsageTrend.
        Process CPU usage.


        :return: The cpu_usage of this TopProcessesUsageTrend.
        :rtype: float
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        """
        Sets the cpu_usage of this TopProcessesUsageTrend.
        Process CPU usage.


        :param cpu_usage: The cpu_usage of this TopProcessesUsageTrend.
        :type: float
        """
        self._cpu_usage = cpu_usage

    @property
    def cpu_utilization(self):
        """
        **[Required]** Gets the cpu_utilization of this TopProcessesUsageTrend.
        Process CPU utilization percentage


        :return: The cpu_utilization of this TopProcessesUsageTrend.
        :rtype: float
        """
        return self._cpu_utilization

    @cpu_utilization.setter
    def cpu_utilization(self, cpu_utilization):
        """
        Sets the cpu_utilization of this TopProcessesUsageTrend.
        Process CPU utilization percentage


        :param cpu_utilization: The cpu_utilization of this TopProcessesUsageTrend.
        :type: float
        """
        self._cpu_utilization = cpu_utilization

    @property
    def memory_utilization(self):
        """
        **[Required]** Gets the memory_utilization of this TopProcessesUsageTrend.
        Process memory utilization percentage


        :return: The memory_utilization of this TopProcessesUsageTrend.
        :rtype: float
        """
        return self._memory_utilization

    @memory_utilization.setter
    def memory_utilization(self, memory_utilization):
        """
        Sets the memory_utilization of this TopProcessesUsageTrend.
        Process memory utilization percentage


        :param memory_utilization: The memory_utilization of this TopProcessesUsageTrend.
        :type: float
        """
        self._memory_utilization = memory_utilization

    @property
    def virtual_memory_in_mbs(self):
        """
        **[Required]** Gets the virtual_memory_in_mbs of this TopProcessesUsageTrend.
        Process virtual memory in Megabytes


        :return: The virtual_memory_in_mbs of this TopProcessesUsageTrend.
        :rtype: float
        """
        return self._virtual_memory_in_mbs

    @virtual_memory_in_mbs.setter
    def virtual_memory_in_mbs(self, virtual_memory_in_mbs):
        """
        Sets the virtual_memory_in_mbs of this TopProcessesUsageTrend.
        Process virtual memory in Megabytes


        :param virtual_memory_in_mbs: The virtual_memory_in_mbs of this TopProcessesUsageTrend.
        :type: float
        """
        self._virtual_memory_in_mbs = virtual_memory_in_mbs

    @property
    def physical_memory_in_mbs(self):
        """
        **[Required]** Gets the physical_memory_in_mbs of this TopProcessesUsageTrend.
        Procress physical memory in Megabytes


        :return: The physical_memory_in_mbs of this TopProcessesUsageTrend.
        :rtype: float
        """
        return self._physical_memory_in_mbs

    @physical_memory_in_mbs.setter
    def physical_memory_in_mbs(self, physical_memory_in_mbs):
        """
        Sets the physical_memory_in_mbs of this TopProcessesUsageTrend.
        Procress physical memory in Megabytes


        :param physical_memory_in_mbs: The physical_memory_in_mbs of this TopProcessesUsageTrend.
        :type: float
        """
        self._physical_memory_in_mbs = physical_memory_in_mbs

    @property
    def max_process_count(self):
        """
        **[Required]** Gets the max_process_count of this TopProcessesUsageTrend.
        Maximum number of processes running at time of collection


        :return: The max_process_count of this TopProcessesUsageTrend.
        :rtype: int
        """
        return self._max_process_count

    @max_process_count.setter
    def max_process_count(self, max_process_count):
        """
        Sets the max_process_count of this TopProcessesUsageTrend.
        Maximum number of processes running at time of collection


        :param max_process_count: The max_process_count of this TopProcessesUsageTrend.
        :type: int
        """
        self._max_process_count = max_process_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
