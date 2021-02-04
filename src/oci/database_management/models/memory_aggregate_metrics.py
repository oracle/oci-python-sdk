# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MemoryAggregateMetrics(object):
    """
    The memory aggregate metric details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MemoryAggregateMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param memory_usage:
            The value to assign to the memory_usage property of this MemoryAggregateMetrics.
        :type memory_usage: list[oci.database_management.models.MetricDataPoint]

        """
        self.swagger_types = {
            'memory_usage': 'list[MetricDataPoint]'
        }

        self.attribute_map = {
            'memory_usage': 'memoryUsage'
        }

        self._memory_usage = None

    @property
    def memory_usage(self):
        """
        Gets the memory_usage of this MemoryAggregateMetrics.
        A list of the memory usage metrics grouped by memorypool for a specific database.


        :return: The memory_usage of this MemoryAggregateMetrics.
        :rtype: list[oci.database_management.models.MetricDataPoint]
        """
        return self._memory_usage

    @memory_usage.setter
    def memory_usage(self, memory_usage):
        """
        Sets the memory_usage of this MemoryAggregateMetrics.
        A list of the memory usage metrics grouped by memorypool for a specific database.


        :param memory_usage: The memory_usage of this MemoryAggregateMetrics.
        :type: list[oci.database_management.models.MetricDataPoint]
        """
        self._memory_usage = memory_usage

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
