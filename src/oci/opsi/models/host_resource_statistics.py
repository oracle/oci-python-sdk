# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostResourceStatistics(object):
    """
    Contains host resource base statistics.
    """

    #: A constant which can be used with the resource_name property of a HostResourceStatistics.
    #: This constant has a value of "HOST_CPU_STATISTICS"
    RESOURCE_NAME_HOST_CPU_STATISTICS = "HOST_CPU_STATISTICS"

    #: A constant which can be used with the resource_name property of a HostResourceStatistics.
    #: This constant has a value of "HOST_MEMORY_STATISTICS"
    RESOURCE_NAME_HOST_MEMORY_STATISTICS = "HOST_MEMORY_STATISTICS"

    def __init__(self, **kwargs):
        """
        Initializes a new HostResourceStatistics object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.HostMemoryStatistics`
        * :class:`~oci.opsi.models.HostCpuStatistics`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param usage:
            The value to assign to the usage property of this HostResourceStatistics.
        :type usage: float

        :param capacity:
            The value to assign to the capacity property of this HostResourceStatistics.
        :type capacity: float

        :param utilization_percent:
            The value to assign to the utilization_percent property of this HostResourceStatistics.
        :type utilization_percent: float

        :param usage_change_percent:
            The value to assign to the usage_change_percent property of this HostResourceStatistics.
        :type usage_change_percent: float

        :param resource_name:
            The value to assign to the resource_name property of this HostResourceStatistics.
            Allowed values for this property are: "HOST_CPU_STATISTICS", "HOST_MEMORY_STATISTICS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type resource_name: str

        """
        self.swagger_types = {
            'usage': 'float',
            'capacity': 'float',
            'utilization_percent': 'float',
            'usage_change_percent': 'float',
            'resource_name': 'str'
        }

        self.attribute_map = {
            'usage': 'usage',
            'capacity': 'capacity',
            'utilization_percent': 'utilizationPercent',
            'usage_change_percent': 'usageChangePercent',
            'resource_name': 'resourceName'
        }

        self._usage = None
        self._capacity = None
        self._utilization_percent = None
        self._usage_change_percent = None
        self._resource_name = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['resourceName']

        if type == 'HOST_MEMORY_STATISTICS':
            return 'HostMemoryStatistics'

        if type == 'HOST_CPU_STATISTICS':
            return 'HostCpuStatistics'
        else:
            return 'HostResourceStatistics'

    @property
    def usage(self):
        """
        **[Required]** Gets the usage of this HostResourceStatistics.
        Total amount used of the resource metric type (CPU, STORAGE).


        :return: The usage of this HostResourceStatistics.
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this HostResourceStatistics.
        Total amount used of the resource metric type (CPU, STORAGE).


        :param usage: The usage of this HostResourceStatistics.
        :type: float
        """
        self._usage = usage

    @property
    def capacity(self):
        """
        **[Required]** Gets the capacity of this HostResourceStatistics.
        The maximum allocated amount of the resource metric type  (CPU, STORAGE).


        :return: The capacity of this HostResourceStatistics.
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this HostResourceStatistics.
        The maximum allocated amount of the resource metric type  (CPU, STORAGE).


        :param capacity: The capacity of this HostResourceStatistics.
        :type: float
        """
        self._capacity = capacity

    @property
    def utilization_percent(self):
        """
        **[Required]** Gets the utilization_percent of this HostResourceStatistics.
        Resource utilization in percentage.


        :return: The utilization_percent of this HostResourceStatistics.
        :rtype: float
        """
        return self._utilization_percent

    @utilization_percent.setter
    def utilization_percent(self, utilization_percent):
        """
        Sets the utilization_percent of this HostResourceStatistics.
        Resource utilization in percentage.


        :param utilization_percent: The utilization_percent of this HostResourceStatistics.
        :type: float
        """
        self._utilization_percent = utilization_percent

    @property
    def usage_change_percent(self):
        """
        **[Required]** Gets the usage_change_percent of this HostResourceStatistics.
        Change in resource utilization in percentage


        :return: The usage_change_percent of this HostResourceStatistics.
        :rtype: float
        """
        return self._usage_change_percent

    @usage_change_percent.setter
    def usage_change_percent(self, usage_change_percent):
        """
        Sets the usage_change_percent of this HostResourceStatistics.
        Change in resource utilization in percentage


        :param usage_change_percent: The usage_change_percent of this HostResourceStatistics.
        :type: float
        """
        self._usage_change_percent = usage_change_percent

    @property
    def resource_name(self):
        """
        **[Required]** Gets the resource_name of this HostResourceStatistics.
        Name of resource for host

        Allowed values for this property are: "HOST_CPU_STATISTICS", "HOST_MEMORY_STATISTICS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The resource_name of this HostResourceStatistics.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this HostResourceStatistics.
        Name of resource for host


        :param resource_name: The resource_name of this HostResourceStatistics.
        :type: str
        """
        allowed_values = ["HOST_CPU_STATISTICS", "HOST_MEMORY_STATISTICS"]
        if not value_allowed_none_or_none_sentinel(resource_name, allowed_values):
            resource_name = 'UNKNOWN_ENUM_VALUE'
        self._resource_name = resource_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
