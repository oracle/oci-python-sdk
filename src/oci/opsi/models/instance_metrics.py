# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceMetrics(object):
    """
    Object containing instance metrics.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param host_name:
            The value to assign to the host_name property of this InstanceMetrics.
        :type host_name: str

        :param instance_name:
            The value to assign to the instance_name property of this InstanceMetrics.
        :type instance_name: str

        :param usage:
            The value to assign to the usage property of this InstanceMetrics.
        :type usage: float

        :param capacity:
            The value to assign to the capacity property of this InstanceMetrics.
        :type capacity: float

        :param total_host_capacity:
            The value to assign to the total_host_capacity property of this InstanceMetrics.
        :type total_host_capacity: float

        :param utilization_percent:
            The value to assign to the utilization_percent property of this InstanceMetrics.
        :type utilization_percent: float

        :param usage_change_percent:
            The value to assign to the usage_change_percent property of this InstanceMetrics.
        :type usage_change_percent: float

        """
        self.swagger_types = {
            'host_name': 'str',
            'instance_name': 'str',
            'usage': 'float',
            'capacity': 'float',
            'total_host_capacity': 'float',
            'utilization_percent': 'float',
            'usage_change_percent': 'float'
        }

        self.attribute_map = {
            'host_name': 'hostName',
            'instance_name': 'instanceName',
            'usage': 'usage',
            'capacity': 'capacity',
            'total_host_capacity': 'totalHostCapacity',
            'utilization_percent': 'utilizationPercent',
            'usage_change_percent': 'usageChangePercent'
        }

        self._host_name = None
        self._instance_name = None
        self._usage = None
        self._capacity = None
        self._total_host_capacity = None
        self._utilization_percent = None
        self._usage_change_percent = None

    @property
    def host_name(self):
        """
        Gets the host_name of this InstanceMetrics.
        The hostname of the database insight resource.


        :return: The host_name of this InstanceMetrics.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this InstanceMetrics.
        The hostname of the database insight resource.


        :param host_name: The host_name of this InstanceMetrics.
        :type: str
        """
        self._host_name = host_name

    @property
    def instance_name(self):
        """
        Gets the instance_name of this InstanceMetrics.
        The instance name of the database insight resource.


        :return: The instance_name of this InstanceMetrics.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """
        Sets the instance_name of this InstanceMetrics.
        The instance name of the database insight resource.


        :param instance_name: The instance_name of this InstanceMetrics.
        :type: str
        """
        self._instance_name = instance_name

    @property
    def usage(self):
        """
        Gets the usage of this InstanceMetrics.
        Total amount used of the resource metric type (CPU, STORAGE).


        :return: The usage of this InstanceMetrics.
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this InstanceMetrics.
        Total amount used of the resource metric type (CPU, STORAGE).


        :param usage: The usage of this InstanceMetrics.
        :type: float
        """
        self._usage = usage

    @property
    def capacity(self):
        """
        Gets the capacity of this InstanceMetrics.
        The maximum allocated amount of the resource metric type  (CPU, STORAGE) for a set of databases.


        :return: The capacity of this InstanceMetrics.
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this InstanceMetrics.
        The maximum allocated amount of the resource metric type  (CPU, STORAGE) for a set of databases.


        :param capacity: The capacity of this InstanceMetrics.
        :type: float
        """
        self._capacity = capacity

    @property
    def total_host_capacity(self):
        """
        Gets the total_host_capacity of this InstanceMetrics.
        The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous Databases.


        :return: The total_host_capacity of this InstanceMetrics.
        :rtype: float
        """
        return self._total_host_capacity

    @total_host_capacity.setter
    def total_host_capacity(self, total_host_capacity):
        """
        Sets the total_host_capacity of this InstanceMetrics.
        The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous Databases.


        :param total_host_capacity: The total_host_capacity of this InstanceMetrics.
        :type: float
        """
        self._total_host_capacity = total_host_capacity

    @property
    def utilization_percent(self):
        """
        Gets the utilization_percent of this InstanceMetrics.
        Resource utilization in percentage


        :return: The utilization_percent of this InstanceMetrics.
        :rtype: float
        """
        return self._utilization_percent

    @utilization_percent.setter
    def utilization_percent(self, utilization_percent):
        """
        Sets the utilization_percent of this InstanceMetrics.
        Resource utilization in percentage


        :param utilization_percent: The utilization_percent of this InstanceMetrics.
        :type: float
        """
        self._utilization_percent = utilization_percent

    @property
    def usage_change_percent(self):
        """
        Gets the usage_change_percent of this InstanceMetrics.
        Change in resource utilization in percentage


        :return: The usage_change_percent of this InstanceMetrics.
        :rtype: float
        """
        return self._usage_change_percent

    @usage_change_percent.setter
    def usage_change_percent(self, usage_change_percent):
        """
        Sets the usage_change_percent of this InstanceMetrics.
        Change in resource utilization in percentage


        :param usage_change_percent: The usage_change_percent of this InstanceMetrics.
        :type: float
        """
        self._usage_change_percent = usage_change_percent

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
