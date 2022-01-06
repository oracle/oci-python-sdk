# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_configuration_metric_group import DatabaseConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DBOSConfigInstance(DatabaseConfigurationMetricGroup):
    """
    Configuration parameters defined for external databases instance level.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DBOSConfigInstance object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.DBOSConfigInstance.metric_name` attribute
        of this class is ``DB_OS_CONFIG_INSTANCE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this DBOSConfigInstance.
            Allowed values for this property are: "DB_EXTERNAL_PROPERTIES", "DB_EXTERNAL_INSTANCE", "DB_OS_CONFIG_INSTANCE"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this DBOSConfigInstance.
        :type time_collected: datetime

        :param instance_name:
            The value to assign to the instance_name property of this DBOSConfigInstance.
        :type instance_name: str

        :param host_name:
            The value to assign to the host_name property of this DBOSConfigInstance.
        :type host_name: str

        :param num_cp_us:
            The value to assign to the num_cp_us property of this DBOSConfigInstance.
        :type num_cp_us: int

        :param num_cpu_cores:
            The value to assign to the num_cpu_cores property of this DBOSConfigInstance.
        :type num_cpu_cores: int

        :param num_cpu_sockets:
            The value to assign to the num_cpu_sockets property of this DBOSConfigInstance.
        :type num_cpu_sockets: int

        :param physical_memory_bytes:
            The value to assign to the physical_memory_bytes property of this DBOSConfigInstance.
        :type physical_memory_bytes: float

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'instance_name': 'str',
            'host_name': 'str',
            'num_cp_us': 'int',
            'num_cpu_cores': 'int',
            'num_cpu_sockets': 'int',
            'physical_memory_bytes': 'float'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'instance_name': 'instanceName',
            'host_name': 'hostName',
            'num_cp_us': 'numCPUs',
            'num_cpu_cores': 'numCPUCores',
            'num_cpu_sockets': 'numCPUSockets',
            'physical_memory_bytes': 'physicalMemoryBytes'
        }

        self._metric_name = None
        self._time_collected = None
        self._instance_name = None
        self._host_name = None
        self._num_cp_us = None
        self._num_cpu_cores = None
        self._num_cpu_sockets = None
        self._physical_memory_bytes = None
        self._metric_name = 'DB_OS_CONFIG_INSTANCE'

    @property
    def instance_name(self):
        """
        **[Required]** Gets the instance_name of this DBOSConfigInstance.
        Name of the database instance.


        :return: The instance_name of this DBOSConfigInstance.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """
        Sets the instance_name of this DBOSConfigInstance.
        Name of the database instance.


        :param instance_name: The instance_name of this DBOSConfigInstance.
        :type: str
        """
        self._instance_name = instance_name

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this DBOSConfigInstance.
        Host name of the database instance.


        :return: The host_name of this DBOSConfigInstance.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this DBOSConfigInstance.
        Host name of the database instance.


        :param host_name: The host_name of this DBOSConfigInstance.
        :type: str
        """
        self._host_name = host_name

    @property
    def num_cp_us(self):
        """
        Gets the num_cp_us of this DBOSConfigInstance.
        Total number of CPUs available.


        :return: The num_cp_us of this DBOSConfigInstance.
        :rtype: int
        """
        return self._num_cp_us

    @num_cp_us.setter
    def num_cp_us(self, num_cp_us):
        """
        Sets the num_cp_us of this DBOSConfigInstance.
        Total number of CPUs available.


        :param num_cp_us: The num_cp_us of this DBOSConfigInstance.
        :type: int
        """
        self._num_cp_us = num_cp_us

    @property
    def num_cpu_cores(self):
        """
        Gets the num_cpu_cores of this DBOSConfigInstance.
        Number of CPU cores available (includes subcores of multicore CPUs as well as single-core CPUs).


        :return: The num_cpu_cores of this DBOSConfigInstance.
        :rtype: int
        """
        return self._num_cpu_cores

    @num_cpu_cores.setter
    def num_cpu_cores(self, num_cpu_cores):
        """
        Sets the num_cpu_cores of this DBOSConfigInstance.
        Number of CPU cores available (includes subcores of multicore CPUs as well as single-core CPUs).


        :param num_cpu_cores: The num_cpu_cores of this DBOSConfigInstance.
        :type: int
        """
        self._num_cpu_cores = num_cpu_cores

    @property
    def num_cpu_sockets(self):
        """
        Gets the num_cpu_sockets of this DBOSConfigInstance.
        Number of CPU Sockets available.


        :return: The num_cpu_sockets of this DBOSConfigInstance.
        :rtype: int
        """
        return self._num_cpu_sockets

    @num_cpu_sockets.setter
    def num_cpu_sockets(self, num_cpu_sockets):
        """
        Sets the num_cpu_sockets of this DBOSConfigInstance.
        Number of CPU Sockets available.


        :param num_cpu_sockets: The num_cpu_sockets of this DBOSConfigInstance.
        :type: int
        """
        self._num_cpu_sockets = num_cpu_sockets

    @property
    def physical_memory_bytes(self):
        """
        Gets the physical_memory_bytes of this DBOSConfigInstance.
        Total number of bytes of physical memory.


        :return: The physical_memory_bytes of this DBOSConfigInstance.
        :rtype: float
        """
        return self._physical_memory_bytes

    @physical_memory_bytes.setter
    def physical_memory_bytes(self, physical_memory_bytes):
        """
        Sets the physical_memory_bytes of this DBOSConfigInstance.
        Total number of bytes of physical memory.


        :param physical_memory_bytes: The physical_memory_bytes of this DBOSConfigInstance.
        :type: float
        """
        self._physical_memory_bytes = physical_memory_bytes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
