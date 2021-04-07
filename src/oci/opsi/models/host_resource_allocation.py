# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_configuration_metric_group import HostConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostResourceAllocation(HostConfigurationMetricGroup):
    """
    Resource Allocation metric for the host
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostResourceAllocation object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostResourceAllocation.metric_name` attribute
        of this class is ``HOST_RESOURCE_ALLOCATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostResourceAllocation.
            Allowed values for this property are: "HOST_PRODUCT", "HOST_RESOURCE_ALLOCATION", "HOST_MEMORY_CONFIGURATION", "HOST_HARDWARE_CONFIGURATION", "HOST_CPU_HARDWARE_CONFIGURATION", "HOST_NETWORK_CONFIGURATION", "HOST_ENTITES"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostResourceAllocation.
        :type time_collected: datetime

        :param total_cpus:
            The value to assign to the total_cpus property of this HostResourceAllocation.
        :type total_cpus: int

        :param total_memory_in_gb:
            The value to assign to the total_memory_in_gb property of this HostResourceAllocation.
        :type total_memory_in_gb: float

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'total_cpus': 'int',
            'total_memory_in_gb': 'float'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'total_cpus': 'totalCpus',
            'total_memory_in_gb': 'totalMemoryInGB'
        }

        self._metric_name = None
        self._time_collected = None
        self._total_cpus = None
        self._total_memory_in_gb = None
        self._metric_name = 'HOST_RESOURCE_ALLOCATION'

    @property
    def total_cpus(self):
        """
        Gets the total_cpus of this HostResourceAllocation.
        Total number of CPUs available


        :return: The total_cpus of this HostResourceAllocation.
        :rtype: int
        """
        return self._total_cpus

    @total_cpus.setter
    def total_cpus(self, total_cpus):
        """
        Sets the total_cpus of this HostResourceAllocation.
        Total number of CPUs available


        :param total_cpus: The total_cpus of this HostResourceAllocation.
        :type: int
        """
        self._total_cpus = total_cpus

    @property
    def total_memory_in_gb(self):
        """
        Gets the total_memory_in_gb of this HostResourceAllocation.
        Total amount of usable physical memory in gibabytes


        :return: The total_memory_in_gb of this HostResourceAllocation.
        :rtype: float
        """
        return self._total_memory_in_gb

    @total_memory_in_gb.setter
    def total_memory_in_gb(self, total_memory_in_gb):
        """
        Sets the total_memory_in_gb of this HostResourceAllocation.
        Total amount of usable physical memory in gibabytes


        :param total_memory_in_gb: The total_memory_in_gb of this HostResourceAllocation.
        :type: float
        """
        self._total_memory_in_gb = total_memory_in_gb

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
