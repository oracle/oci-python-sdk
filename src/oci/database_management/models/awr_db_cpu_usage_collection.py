# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .awr_query_result import AwrQueryResult
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrDbCpuUsageCollection(AwrQueryResult):
    """
    The AWR CPU usage data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwrDbCpuUsageCollection object with values from keyword arguments. The default value of the :py:attr:`~oci.database_management.models.AwrDbCpuUsageCollection.awr_result_type` attribute
        of this class is ``AWRDB_ASH_CPU_USAGE_SET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AwrDbCpuUsageCollection.
        :type name: str

        :param version:
            The value to assign to the version property of this AwrDbCpuUsageCollection.
        :type version: str

        :param query_key:
            The value to assign to the query_key property of this AwrDbCpuUsageCollection.
        :type query_key: str

        :param db_query_time_in_secs:
            The value to assign to the db_query_time_in_secs property of this AwrDbCpuUsageCollection.
        :type db_query_time_in_secs: float

        :param awr_result_type:
            The value to assign to the awr_result_type property of this AwrDbCpuUsageCollection.
            Allowed values for this property are: "AWRDB_SET", "AWRDB_SNAPSHOT_RANGE_SET", "AWRDB_SNAPSHOT_SET", "AWRDB_METRICS_SET", "AWRDB_SYSSTAT_SET", "AWRDB_TOP_EVENT_SET", "AWRDB_EVENT_SET", "AWRDB_EVENT_HISTOGRAM", "AWRDB_DB_PARAMETER_SET", "AWRDB_DB_PARAMETER_CHANGE", "AWRDB_ASH_CPU_USAGE_SET", "AWRDB_DB_REPORT", "AWRDB_SQL_REPORT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type awr_result_type: str

        :param num_cpu_cores:
            The value to assign to the num_cpu_cores property of this AwrDbCpuUsageCollection.
        :type num_cpu_cores: int

        :param cpu_count:
            The value to assign to the cpu_count property of this AwrDbCpuUsageCollection.
        :type cpu_count: int

        :param num_cpus:
            The value to assign to the num_cpus property of this AwrDbCpuUsageCollection.
        :type num_cpus: float

        :param items:
            The value to assign to the items property of this AwrDbCpuUsageCollection.
        :type items: list[oci.database_management.models.AwrDbCpuUsageSummary]

        """
        self.swagger_types = {
            'name': 'str',
            'version': 'str',
            'query_key': 'str',
            'db_query_time_in_secs': 'float',
            'awr_result_type': 'str',
            'num_cpu_cores': 'int',
            'cpu_count': 'int',
            'num_cpus': 'float',
            'items': 'list[AwrDbCpuUsageSummary]'
        }

        self.attribute_map = {
            'name': 'name',
            'version': 'version',
            'query_key': 'queryKey',
            'db_query_time_in_secs': 'dbQueryTimeInSecs',
            'awr_result_type': 'awrResultType',
            'num_cpu_cores': 'numCpuCores',
            'cpu_count': 'cpuCount',
            'num_cpus': 'numCpus',
            'items': 'items'
        }

        self._name = None
        self._version = None
        self._query_key = None
        self._db_query_time_in_secs = None
        self._awr_result_type = None
        self._num_cpu_cores = None
        self._cpu_count = None
        self._num_cpus = None
        self._items = None
        self._awr_result_type = 'AWRDB_ASH_CPU_USAGE_SET'

    @property
    def num_cpu_cores(self):
        """
        Gets the num_cpu_cores of this AwrDbCpuUsageCollection.
        The number of available CPU cores, which include subcores of multicore and single-core CPUs.


        :return: The num_cpu_cores of this AwrDbCpuUsageCollection.
        :rtype: int
        """
        return self._num_cpu_cores

    @num_cpu_cores.setter
    def num_cpu_cores(self, num_cpu_cores):
        """
        Sets the num_cpu_cores of this AwrDbCpuUsageCollection.
        The number of available CPU cores, which include subcores of multicore and single-core CPUs.


        :param num_cpu_cores: The num_cpu_cores of this AwrDbCpuUsageCollection.
        :type: int
        """
        self._num_cpu_cores = num_cpu_cores

    @property
    def cpu_count(self):
        """
        Gets the cpu_count of this AwrDbCpuUsageCollection.
        The number of CPUs available for the database to use.


        :return: The cpu_count of this AwrDbCpuUsageCollection.
        :rtype: int
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, cpu_count):
        """
        Sets the cpu_count of this AwrDbCpuUsageCollection.
        The number of CPUs available for the database to use.


        :param cpu_count: The cpu_count of this AwrDbCpuUsageCollection.
        :type: int
        """
        self._cpu_count = cpu_count

    @property
    def num_cpus(self):
        """
        Gets the num_cpus of this AwrDbCpuUsageCollection.
        The number of available CPUs or processors.


        :return: The num_cpus of this AwrDbCpuUsageCollection.
        :rtype: float
        """
        return self._num_cpus

    @num_cpus.setter
    def num_cpus(self, num_cpus):
        """
        Sets the num_cpus of this AwrDbCpuUsageCollection.
        The number of available CPUs or processors.


        :param num_cpus: The num_cpus of this AwrDbCpuUsageCollection.
        :type: float
        """
        self._num_cpus = num_cpus

    @property
    def items(self):
        """
        Gets the items of this AwrDbCpuUsageCollection.
        A list of AWR CPU usage summary data.


        :return: The items of this AwrDbCpuUsageCollection.
        :rtype: list[oci.database_management.models.AwrDbCpuUsageSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this AwrDbCpuUsageCollection.
        A list of AWR CPU usage summary data.


        :param items: The items of this AwrDbCpuUsageCollection.
        :type: list[oci.database_management.models.AwrDbCpuUsageSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
