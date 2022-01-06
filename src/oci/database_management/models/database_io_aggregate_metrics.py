# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseIOAggregateMetrics(object):
    """
    The database Input/Output metric details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseIOAggregateMetrics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param iops:
            The value to assign to the iops property of this DatabaseIOAggregateMetrics.
        :type iops: list[oci.database_management.models.MetricDataPoint]

        :param io_throughput:
            The value to assign to the io_throughput property of this DatabaseIOAggregateMetrics.
        :type io_throughput: list[oci.database_management.models.MetricDataPoint]

        """
        self.swagger_types = {
            'iops': 'list[MetricDataPoint]',
            'io_throughput': 'list[MetricDataPoint]'
        }

        self.attribute_map = {
            'iops': 'iops',
            'io_throughput': 'ioThroughput'
        }

        self._iops = None
        self._io_throughput = None

    @property
    def iops(self):
        """
        Gets the iops of this DatabaseIOAggregateMetrics.
        A list of the Input/Output Operations Per Second metrics grouped by IOType for a specific database.


        :return: The iops of this DatabaseIOAggregateMetrics.
        :rtype: list[oci.database_management.models.MetricDataPoint]
        """
        return self._iops

    @iops.setter
    def iops(self, iops):
        """
        Sets the iops of this DatabaseIOAggregateMetrics.
        A list of the Input/Output Operations Per Second metrics grouped by IOType for a specific database.


        :param iops: The iops of this DatabaseIOAggregateMetrics.
        :type: list[oci.database_management.models.MetricDataPoint]
        """
        self._iops = iops

    @property
    def io_throughput(self):
        """
        Gets the io_throughput of this DatabaseIOAggregateMetrics.
        A list of the IOThroughput metrics grouped for a specific database.


        :return: The io_throughput of this DatabaseIOAggregateMetrics.
        :rtype: list[oci.database_management.models.MetricDataPoint]
        """
        return self._io_throughput

    @io_throughput.setter
    def io_throughput(self, io_throughput):
        """
        Sets the io_throughput of this DatabaseIOAggregateMetrics.
        A list of the IOThroughput metrics grouped for a specific database.


        :param io_throughput: The io_throughput of this DatabaseIOAggregateMetrics.
        :type: list[oci.database_management.models.MetricDataPoint]
        """
        self._io_throughput = io_throughput

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
