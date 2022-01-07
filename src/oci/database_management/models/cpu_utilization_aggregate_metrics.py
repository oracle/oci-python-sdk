# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CpuUtilizationAggregateMetrics(object):
    """
    The CPU utilization metrics for Autonomous Databases.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CpuUtilizationAggregateMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cpu_utilization:
            The value to assign to the cpu_utilization property of this CpuUtilizationAggregateMetrics.
        :type cpu_utilization: oci.database_management.models.MetricDataPoint

        """
        self.swagger_types = {
            'cpu_utilization': 'MetricDataPoint'
        }

        self.attribute_map = {
            'cpu_utilization': 'cpuUtilization'
        }

        self._cpu_utilization = None

    @property
    def cpu_utilization(self):
        """
        Gets the cpu_utilization of this CpuUtilizationAggregateMetrics.

        :return: The cpu_utilization of this CpuUtilizationAggregateMetrics.
        :rtype: oci.database_management.models.MetricDataPoint
        """
        return self._cpu_utilization

    @cpu_utilization.setter
    def cpu_utilization(self, cpu_utilization):
        """
        Sets the cpu_utilization of this CpuUtilizationAggregateMetrics.

        :param cpu_utilization: The cpu_utilization of this CpuUtilizationAggregateMetrics.
        :type: oci.database_management.models.MetricDataPoint
        """
        self._cpu_utilization = cpu_utilization

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
