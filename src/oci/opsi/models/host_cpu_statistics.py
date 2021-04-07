# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_resource_statistics import HostResourceStatistics
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostCpuStatistics(HostResourceStatistics):
    """
    Contains CPU statistics.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostCpuStatistics object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostCpuStatistics.resource_name` attribute
        of this class is ``HOST_CPU_STATISTICS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param usage:
            The value to assign to the usage property of this HostCpuStatistics.
        :type usage: float

        :param capacity:
            The value to assign to the capacity property of this HostCpuStatistics.
        :type capacity: float

        :param utilization_percent:
            The value to assign to the utilization_percent property of this HostCpuStatistics.
        :type utilization_percent: float

        :param usage_change_percent:
            The value to assign to the usage_change_percent property of this HostCpuStatistics.
        :type usage_change_percent: float

        :param resource_name:
            The value to assign to the resource_name property of this HostCpuStatistics.
            Allowed values for this property are: "HOST_CPU_STATISTICS", "HOST_MEMORY_STATISTICS"
        :type resource_name: str

        :param load:
            The value to assign to the load property of this HostCpuStatistics.
        :type load: oci.opsi.models.SummaryStatistics

        """
        self.swagger_types = {
            'usage': 'float',
            'capacity': 'float',
            'utilization_percent': 'float',
            'usage_change_percent': 'float',
            'resource_name': 'str',
            'load': 'SummaryStatistics'
        }

        self.attribute_map = {
            'usage': 'usage',
            'capacity': 'capacity',
            'utilization_percent': 'utilizationPercent',
            'usage_change_percent': 'usageChangePercent',
            'resource_name': 'resourceName',
            'load': 'load'
        }

        self._usage = None
        self._capacity = None
        self._utilization_percent = None
        self._usage_change_percent = None
        self._resource_name = None
        self._load = None
        self._resource_name = 'HOST_CPU_STATISTICS'

    @property
    def load(self):
        """
        Gets the load of this HostCpuStatistics.

        :return: The load of this HostCpuStatistics.
        :rtype: oci.opsi.models.SummaryStatistics
        """
        return self._load

    @load.setter
    def load(self, load):
        """
        Sets the load of this HostCpuStatistics.

        :param load: The load of this HostCpuStatistics.
        :type: oci.opsi.models.SummaryStatistics
        """
        self._load = load

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
