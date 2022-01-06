# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_configuration_metric_group import DatabaseConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DBExternalInstance(DatabaseConfigurationMetricGroup):
    """
    Configuration parameters defined for external databases instance level.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DBExternalInstance object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.DBExternalInstance.metric_name` attribute
        of this class is ``DB_EXTERNAL_INSTANCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this DBExternalInstance.
            Allowed values for this property are: "DB_EXTERNAL_PROPERTIES", "DB_EXTERNAL_INSTANCE", "DB_OS_CONFIG_INSTANCE"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this DBExternalInstance.
        :type time_collected: datetime

        :param instance_name:
            The value to assign to the instance_name property of this DBExternalInstance.
        :type instance_name: str

        :param host_name:
            The value to assign to the host_name property of this DBExternalInstance.
        :type host_name: str

        :param cpu_count:
            The value to assign to the cpu_count property of this DBExternalInstance.
        :type cpu_count: int

        :param host_memory_capacity:
            The value to assign to the host_memory_capacity property of this DBExternalInstance.
        :type host_memory_capacity: float

        :param version:
            The value to assign to the version property of this DBExternalInstance.
        :type version: str

        :param parallel:
            The value to assign to the parallel property of this DBExternalInstance.
        :type parallel: str

        :param instance_role:
            The value to assign to the instance_role property of this DBExternalInstance.
        :type instance_role: str

        :param logins:
            The value to assign to the logins property of this DBExternalInstance.
        :type logins: str

        :param database_status:
            The value to assign to the database_status property of this DBExternalInstance.
        :type database_status: str

        :param status:
            The value to assign to the status property of this DBExternalInstance.
        :type status: str

        :param edition:
            The value to assign to the edition property of this DBExternalInstance.
        :type edition: str

        :param startup_time:
            The value to assign to the startup_time property of this DBExternalInstance.
        :type startup_time: datetime

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'instance_name': 'str',
            'host_name': 'str',
            'cpu_count': 'int',
            'host_memory_capacity': 'float',
            'version': 'str',
            'parallel': 'str',
            'instance_role': 'str',
            'logins': 'str',
            'database_status': 'str',
            'status': 'str',
            'edition': 'str',
            'startup_time': 'datetime'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'instance_name': 'instanceName',
            'host_name': 'hostName',
            'cpu_count': 'cpuCount',
            'host_memory_capacity': 'hostMemoryCapacity',
            'version': 'version',
            'parallel': 'parallel',
            'instance_role': 'instanceRole',
            'logins': 'logins',
            'database_status': 'databaseStatus',
            'status': 'status',
            'edition': 'edition',
            'startup_time': 'startupTime'
        }

        self._metric_name = None
        self._time_collected = None
        self._instance_name = None
        self._host_name = None
        self._cpu_count = None
        self._host_memory_capacity = None
        self._version = None
        self._parallel = None
        self._instance_role = None
        self._logins = None
        self._database_status = None
        self._status = None
        self._edition = None
        self._startup_time = None
        self._metric_name = 'DB_EXTERNAL_INSTANCE'

    @property
    def instance_name(self):
        """
        **[Required]** Gets the instance_name of this DBExternalInstance.
        Name of the database instance.


        :return: The instance_name of this DBExternalInstance.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """
        Sets the instance_name of this DBExternalInstance.
        Name of the database instance.


        :param instance_name: The instance_name of this DBExternalInstance.
        :type: str
        """
        self._instance_name = instance_name

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this DBExternalInstance.
        Host name of the database instance.


        :return: The host_name of this DBExternalInstance.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this DBExternalInstance.
        Host name of the database instance.


        :param host_name: The host_name of this DBExternalInstance.
        :type: str
        """
        self._host_name = host_name

    @property
    def cpu_count(self):
        """
        Gets the cpu_count of this DBExternalInstance.
        Total number of CPUs allocated for the host.


        :return: The cpu_count of this DBExternalInstance.
        :rtype: int
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, cpu_count):
        """
        Sets the cpu_count of this DBExternalInstance.
        Total number of CPUs allocated for the host.


        :param cpu_count: The cpu_count of this DBExternalInstance.
        :type: int
        """
        self._cpu_count = cpu_count

    @property
    def host_memory_capacity(self):
        """
        Gets the host_memory_capacity of this DBExternalInstance.
        Total amount of usable Physical RAM Memory available in gigabytes.


        :return: The host_memory_capacity of this DBExternalInstance.
        :rtype: float
        """
        return self._host_memory_capacity

    @host_memory_capacity.setter
    def host_memory_capacity(self, host_memory_capacity):
        """
        Sets the host_memory_capacity of this DBExternalInstance.
        Total amount of usable Physical RAM Memory available in gigabytes.


        :param host_memory_capacity: The host_memory_capacity of this DBExternalInstance.
        :type: float
        """
        self._host_memory_capacity = host_memory_capacity

    @property
    def version(self):
        """
        Gets the version of this DBExternalInstance.
        Database version.


        :return: The version of this DBExternalInstance.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this DBExternalInstance.
        Database version.


        :param version: The version of this DBExternalInstance.
        :type: str
        """
        self._version = version

    @property
    def parallel(self):
        """
        Gets the parallel of this DBExternalInstance.
        Indicates whether the instance is mounted in cluster database mode (YES) or not (NO).


        :return: The parallel of this DBExternalInstance.
        :rtype: str
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        """
        Sets the parallel of this DBExternalInstance.
        Indicates whether the instance is mounted in cluster database mode (YES) or not (NO).


        :param parallel: The parallel of this DBExternalInstance.
        :type: str
        """
        self._parallel = parallel

    @property
    def instance_role(self):
        """
        Gets the instance_role of this DBExternalInstance.
        Role (permissions) of the database instance.


        :return: The instance_role of this DBExternalInstance.
        :rtype: str
        """
        return self._instance_role

    @instance_role.setter
    def instance_role(self, instance_role):
        """
        Sets the instance_role of this DBExternalInstance.
        Role (permissions) of the database instance.


        :param instance_role: The instance_role of this DBExternalInstance.
        :type: str
        """
        self._instance_role = instance_role

    @property
    def logins(self):
        """
        Gets the logins of this DBExternalInstance.
        Indicates if logins are allowed or restricted.


        :return: The logins of this DBExternalInstance.
        :rtype: str
        """
        return self._logins

    @logins.setter
    def logins(self, logins):
        """
        Sets the logins of this DBExternalInstance.
        Indicates if logins are allowed or restricted.


        :param logins: The logins of this DBExternalInstance.
        :type: str
        """
        self._logins = logins

    @property
    def database_status(self):
        """
        Gets the database_status of this DBExternalInstance.
        Status of the database.


        :return: The database_status of this DBExternalInstance.
        :rtype: str
        """
        return self._database_status

    @database_status.setter
    def database_status(self, database_status):
        """
        Sets the database_status of this DBExternalInstance.
        Status of the database.


        :param database_status: The database_status of this DBExternalInstance.
        :type: str
        """
        self._database_status = database_status

    @property
    def status(self):
        """
        Gets the status of this DBExternalInstance.
        Status of the instance.


        :return: The status of this DBExternalInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this DBExternalInstance.
        Status of the instance.


        :param status: The status of this DBExternalInstance.
        :type: str
        """
        self._status = status

    @property
    def edition(self):
        """
        Gets the edition of this DBExternalInstance.
        The edition of the database.


        :return: The edition of this DBExternalInstance.
        :rtype: str
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """
        Sets the edition of this DBExternalInstance.
        The edition of the database.


        :param edition: The edition of this DBExternalInstance.
        :type: str
        """
        self._edition = edition

    @property
    def startup_time(self):
        """
        Gets the startup_time of this DBExternalInstance.
        Start up time of the database instance.


        :return: The startup_time of this DBExternalInstance.
        :rtype: datetime
        """
        return self._startup_time

    @startup_time.setter
    def startup_time(self, startup_time):
        """
        Sets the startup_time of this DBExternalInstance.
        Start up time of the database instance.


        :param startup_time: The startup_time of this DBExternalInstance.
        :type: datetime
        """
        self._startup_time = startup_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
