# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceStatistics(object):
    """
    Contains resource statistics with usage unit
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceStatistics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param usage:
            The value to assign to the usage property of this ResourceStatistics.
        :type usage: float

        :param capacity:
            The value to assign to the capacity property of this ResourceStatistics.
        :type capacity: float

        :param base_capacity:
            The value to assign to the base_capacity property of this ResourceStatistics.
        :type base_capacity: float

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this ResourceStatistics.
        :type is_auto_scaling_enabled: bool

        :param utilization_percent:
            The value to assign to the utilization_percent property of this ResourceStatistics.
        :type utilization_percent: float

        :param usage_change_percent:
            The value to assign to the usage_change_percent property of this ResourceStatistics.
        :type usage_change_percent: float

        :param instance_metrics:
            The value to assign to the instance_metrics property of this ResourceStatistics.
        :type instance_metrics: list[oci.opsi.models.InstanceMetrics]

        """
        self.swagger_types = {
            'usage': 'float',
            'capacity': 'float',
            'base_capacity': 'float',
            'is_auto_scaling_enabled': 'bool',
            'utilization_percent': 'float',
            'usage_change_percent': 'float',
            'instance_metrics': 'list[InstanceMetrics]'
        }

        self.attribute_map = {
            'usage': 'usage',
            'capacity': 'capacity',
            'base_capacity': 'baseCapacity',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'utilization_percent': 'utilizationPercent',
            'usage_change_percent': 'usageChangePercent',
            'instance_metrics': 'instanceMetrics'
        }

        self._usage = None
        self._capacity = None
        self._base_capacity = None
        self._is_auto_scaling_enabled = None
        self._utilization_percent = None
        self._usage_change_percent = None
        self._instance_metrics = None

    @property
    def usage(self):
        """
        **[Required]** Gets the usage of this ResourceStatistics.
        Total amount used of the resource metric type (CPU, STORAGE).


        :return: The usage of this ResourceStatistics.
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this ResourceStatistics.
        Total amount used of the resource metric type (CPU, STORAGE).


        :param usage: The usage of this ResourceStatistics.
        :type: float
        """
        self._usage = usage

    @property
    def capacity(self):
        """
        **[Required]** Gets the capacity of this ResourceStatistics.
        The maximum allocated amount of the resource metric type  (CPU, STORAGE).


        :return: The capacity of this ResourceStatistics.
        :rtype: float
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this ResourceStatistics.
        The maximum allocated amount of the resource metric type  (CPU, STORAGE).


        :param capacity: The capacity of this ResourceStatistics.
        :type: float
        """
        self._capacity = capacity

    @property
    def base_capacity(self):
        """
        Gets the base_capacity of this ResourceStatistics.
        The base allocated amount of the resource metric type  (CPU, STORAGE).


        :return: The base_capacity of this ResourceStatistics.
        :rtype: float
        """
        return self._base_capacity

    @base_capacity.setter
    def base_capacity(self, base_capacity):
        """
        Sets the base_capacity of this ResourceStatistics.
        The base allocated amount of the resource metric type  (CPU, STORAGE).


        :param base_capacity: The base_capacity of this ResourceStatistics.
        :type: float
        """
        self._base_capacity = base_capacity

    @property
    def is_auto_scaling_enabled(self):
        """
        Gets the is_auto_scaling_enabled of this ResourceStatistics.
        Indicates if auto scaling feature is enabled or disabled on a database. It will be false for all metrics other than CPU.


        :return: The is_auto_scaling_enabled of this ResourceStatistics.
        :rtype: bool
        """
        return self._is_auto_scaling_enabled

    @is_auto_scaling_enabled.setter
    def is_auto_scaling_enabled(self, is_auto_scaling_enabled):
        """
        Sets the is_auto_scaling_enabled of this ResourceStatistics.
        Indicates if auto scaling feature is enabled or disabled on a database. It will be false for all metrics other than CPU.


        :param is_auto_scaling_enabled: The is_auto_scaling_enabled of this ResourceStatistics.
        :type: bool
        """
        self._is_auto_scaling_enabled = is_auto_scaling_enabled

    @property
    def utilization_percent(self):
        """
        **[Required]** Gets the utilization_percent of this ResourceStatistics.
        Resource utilization in percentage


        :return: The utilization_percent of this ResourceStatistics.
        :rtype: float
        """
        return self._utilization_percent

    @utilization_percent.setter
    def utilization_percent(self, utilization_percent):
        """
        Sets the utilization_percent of this ResourceStatistics.
        Resource utilization in percentage


        :param utilization_percent: The utilization_percent of this ResourceStatistics.
        :type: float
        """
        self._utilization_percent = utilization_percent

    @property
    def usage_change_percent(self):
        """
        **[Required]** Gets the usage_change_percent of this ResourceStatistics.
        Change in resource utilization in percentage


        :return: The usage_change_percent of this ResourceStatistics.
        :rtype: float
        """
        return self._usage_change_percent

    @usage_change_percent.setter
    def usage_change_percent(self, usage_change_percent):
        """
        Sets the usage_change_percent of this ResourceStatistics.
        Change in resource utilization in percentage


        :param usage_change_percent: The usage_change_percent of this ResourceStatistics.
        :type: float
        """
        self._usage_change_percent = usage_change_percent

    @property
    def instance_metrics(self):
        """
        Gets the instance_metrics of this ResourceStatistics.
        Array of instance metrics


        :return: The instance_metrics of this ResourceStatistics.
        :rtype: list[oci.opsi.models.InstanceMetrics]
        """
        return self._instance_metrics

    @instance_metrics.setter
    def instance_metrics(self, instance_metrics):
        """
        Sets the instance_metrics of this ResourceStatistics.
        Array of instance metrics


        :param instance_metrics: The instance_metrics of this ResourceStatistics.
        :type: list[oci.opsi.models.InstanceMetrics]
        """
        self._instance_metrics = instance_metrics

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
