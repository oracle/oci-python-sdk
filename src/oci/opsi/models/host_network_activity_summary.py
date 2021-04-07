# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_performance_metric_group import HostPerformanceMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostNetworkActivitySummary(HostPerformanceMetricGroup):
    """
    Network Activity Summary metric for the host
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostNetworkActivitySummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostNetworkActivitySummary.metric_name` attribute
        of this class is ``HOST_NETWORK_ACTIVITY_SUMMARY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostNetworkActivitySummary.
            Allowed values for this property are: "HOST_CPU_USAGE", "HOST_MEMORY_USAGE", "HOST_NETWORK_ACTIVITY_SUMMARY"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostNetworkActivitySummary.
        :type time_collected: datetime

        :param all_network_read_in_mbps:
            The value to assign to the all_network_read_in_mbps property of this HostNetworkActivitySummary.
        :type all_network_read_in_mbps: float

        :param all_network_write_in_mbps:
            The value to assign to the all_network_write_in_mbps property of this HostNetworkActivitySummary.
        :type all_network_write_in_mbps: float

        :param all_network_io_in_mbps:
            The value to assign to the all_network_io_in_mbps property of this HostNetworkActivitySummary.
        :type all_network_io_in_mbps: float

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'all_network_read_in_mbps': 'float',
            'all_network_write_in_mbps': 'float',
            'all_network_io_in_mbps': 'float'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'all_network_read_in_mbps': 'allNetworkReadInMbps',
            'all_network_write_in_mbps': 'allNetworkWriteInMbps',
            'all_network_io_in_mbps': 'allNetworkIoInMbps'
        }

        self._metric_name = None
        self._time_collected = None
        self._all_network_read_in_mbps = None
        self._all_network_write_in_mbps = None
        self._all_network_io_in_mbps = None
        self._metric_name = 'HOST_NETWORK_ACTIVITY_SUMMARY'

    @property
    def all_network_read_in_mbps(self):
        """
        Gets the all_network_read_in_mbps of this HostNetworkActivitySummary.
        All network interfaces read rate in Mbps


        :return: The all_network_read_in_mbps of this HostNetworkActivitySummary.
        :rtype: float
        """
        return self._all_network_read_in_mbps

    @all_network_read_in_mbps.setter
    def all_network_read_in_mbps(self, all_network_read_in_mbps):
        """
        Sets the all_network_read_in_mbps of this HostNetworkActivitySummary.
        All network interfaces read rate in Mbps


        :param all_network_read_in_mbps: The all_network_read_in_mbps of this HostNetworkActivitySummary.
        :type: float
        """
        self._all_network_read_in_mbps = all_network_read_in_mbps

    @property
    def all_network_write_in_mbps(self):
        """
        Gets the all_network_write_in_mbps of this HostNetworkActivitySummary.
        All network interfaces write rate in Mbps


        :return: The all_network_write_in_mbps of this HostNetworkActivitySummary.
        :rtype: float
        """
        return self._all_network_write_in_mbps

    @all_network_write_in_mbps.setter
    def all_network_write_in_mbps(self, all_network_write_in_mbps):
        """
        Sets the all_network_write_in_mbps of this HostNetworkActivitySummary.
        All network interfaces write rate in Mbps


        :param all_network_write_in_mbps: The all_network_write_in_mbps of this HostNetworkActivitySummary.
        :type: float
        """
        self._all_network_write_in_mbps = all_network_write_in_mbps

    @property
    def all_network_io_in_mbps(self):
        """
        Gets the all_network_io_in_mbps of this HostNetworkActivitySummary.
        All network interfaces IO rate in Mbps


        :return: The all_network_io_in_mbps of this HostNetworkActivitySummary.
        :rtype: float
        """
        return self._all_network_io_in_mbps

    @all_network_io_in_mbps.setter
    def all_network_io_in_mbps(self, all_network_io_in_mbps):
        """
        Sets the all_network_io_in_mbps of this HostNetworkActivitySummary.
        All network interfaces IO rate in Mbps


        :param all_network_io_in_mbps: The all_network_io_in_mbps of this HostNetworkActivitySummary.
        :type: float
        """
        self._all_network_io_in_mbps = all_network_io_in_mbps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
