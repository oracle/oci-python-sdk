# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .awr_query_result import AwrQueryResult
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrDatabaseCpuUsageCollection(AwrQueryResult):
    """
    The AWR CPU usage data.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwrDatabaseCpuUsageCollection object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.AwrDatabaseCpuUsageCollection.awr_result_type` attribute
        of this class is ``AWRDB_ASH_CPU_USAGE_SET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AwrDatabaseCpuUsageCollection.
        :type name: str

        :param version:
            The value to assign to the version property of this AwrDatabaseCpuUsageCollection.
        :type version: str

        :param db_query_time_in_secs:
            The value to assign to the db_query_time_in_secs property of this AwrDatabaseCpuUsageCollection.
        :type db_query_time_in_secs: float

        :param awr_result_type:
            The value to assign to the awr_result_type property of this AwrDatabaseCpuUsageCollection.
            Allowed values for this property are: "AWRDB_SET", "AWRDB_SNAPSHOT_RANGE_SET", "AWRDB_SNAPSHOT_SET", "AWRDB_METRICS_SET", "AWRDB_SYSSTAT_SET", "AWRDB_TOP_EVENT_SET", "AWRDB_EVENT_SET", "AWRDB_EVENT_HISTOGRAM", "AWRDB_DB_PARAMETER_SET", "AWRDB_DB_PARAMETER_CHANGE", "AWRDB_ASH_CPU_USAGE_SET", "AWRDB_DB_REPORT", "AWRDB_SQL_REPORT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type awr_result_type: str

        :param num_cpu_cores:
            The value to assign to the num_cpu_cores property of this AwrDatabaseCpuUsageCollection.
        :type num_cpu_cores: int

        :param database_cpu_count:
            The value to assign to the database_cpu_count property of this AwrDatabaseCpuUsageCollection.
        :type database_cpu_count: int

        :param host_cpu_count:
            The value to assign to the host_cpu_count property of this AwrDatabaseCpuUsageCollection.
        :type host_cpu_count: float

        :param items:
            The value to assign to the items property of this AwrDatabaseCpuUsageCollection.
        :type items: list[oci.opsi.models.AwrDatabaseCpuUsageSummary]

        """
        self.swagger_types = {
            'name': 'str',
            'version': 'str',
            'db_query_time_in_secs': 'float',
            'awr_result_type': 'str',
            'num_cpu_cores': 'int',
            'database_cpu_count': 'int',
            'host_cpu_count': 'float',
            'items': 'list[AwrDatabaseCpuUsageSummary]'
        }

        self.attribute_map = {
            'name': 'name',
            'version': 'version',
            'db_query_time_in_secs': 'dbQueryTimeInSecs',
            'awr_result_type': 'awrResultType',
            'num_cpu_cores': 'numCpuCores',
            'database_cpu_count': 'databaseCpuCount',
            'host_cpu_count': 'hostCpuCount',
            'items': 'items'
        }

        self._name = None
        self._version = None
        self._db_query_time_in_secs = None
        self._awr_result_type = None
        self._num_cpu_cores = None
        self._database_cpu_count = None
        self._host_cpu_count = None
        self._items = None
        self._awr_result_type = 'AWRDB_ASH_CPU_USAGE_SET'

    @property
    def num_cpu_cores(self):
        """
        Gets the num_cpu_cores of this AwrDatabaseCpuUsageCollection.
        The number of available CPU cores, which include subcores of multicore and single-core CPUs.


        :return: The num_cpu_cores of this AwrDatabaseCpuUsageCollection.
        :rtype: int
        """
        return self._num_cpu_cores

    @num_cpu_cores.setter
    def num_cpu_cores(self, num_cpu_cores):
        """
        Sets the num_cpu_cores of this AwrDatabaseCpuUsageCollection.
        The number of available CPU cores, which include subcores of multicore and single-core CPUs.


        :param num_cpu_cores: The num_cpu_cores of this AwrDatabaseCpuUsageCollection.
        :type: int
        """
        self._num_cpu_cores = num_cpu_cores

    @property
    def database_cpu_count(self):
        """
        Gets the database_cpu_count of this AwrDatabaseCpuUsageCollection.
        The number of CPUs available for the database to use.


        :return: The database_cpu_count of this AwrDatabaseCpuUsageCollection.
        :rtype: int
        """
        return self._database_cpu_count

    @database_cpu_count.setter
    def database_cpu_count(self, database_cpu_count):
        """
        Sets the database_cpu_count of this AwrDatabaseCpuUsageCollection.
        The number of CPUs available for the database to use.


        :param database_cpu_count: The database_cpu_count of this AwrDatabaseCpuUsageCollection.
        :type: int
        """
        self._database_cpu_count = database_cpu_count

    @property
    def host_cpu_count(self):
        """
        Gets the host_cpu_count of this AwrDatabaseCpuUsageCollection.
        The number of available CPUs or processors.


        :return: The host_cpu_count of this AwrDatabaseCpuUsageCollection.
        :rtype: float
        """
        return self._host_cpu_count

    @host_cpu_count.setter
    def host_cpu_count(self, host_cpu_count):
        """
        Sets the host_cpu_count of this AwrDatabaseCpuUsageCollection.
        The number of available CPUs or processors.


        :param host_cpu_count: The host_cpu_count of this AwrDatabaseCpuUsageCollection.
        :type: float
        """
        self._host_cpu_count = host_cpu_count

    @property
    def items(self):
        """
        Gets the items of this AwrDatabaseCpuUsageCollection.
        A list of AWR CPU usage summary data.


        :return: The items of this AwrDatabaseCpuUsageCollection.
        :rtype: list[oci.opsi.models.AwrDatabaseCpuUsageSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this AwrDatabaseCpuUsageCollection.
        A list of AWR CPU usage summary data.


        :param items: The items of this AwrDatabaseCpuUsageCollection.
        :type: list[oci.opsi.models.AwrDatabaseCpuUsageSummary]
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
