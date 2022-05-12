# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputePerformanceSummary(object):
    """
    Parameters detailing the compute performance for a specified DB system shape.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputePerformanceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this ComputePerformanceSummary.
        :type cpu_core_count: int

        :param memory_in_gbs:
            The value to assign to the memory_in_gbs property of this ComputePerformanceSummary.
        :type memory_in_gbs: float

        :param network_bandwidth_in_gbps:
            The value to assign to the network_bandwidth_in_gbps property of this ComputePerformanceSummary.
        :type network_bandwidth_in_gbps: float

        :param network_iops:
            The value to assign to the network_iops property of this ComputePerformanceSummary.
        :type network_iops: float

        :param network_throughput_in_mbps:
            The value to assign to the network_throughput_in_mbps property of this ComputePerformanceSummary.
        :type network_throughput_in_mbps: float

        """
        self.swagger_types = {
            'cpu_core_count': 'int',
            'memory_in_gbs': 'float',
            'network_bandwidth_in_gbps': 'float',
            'network_iops': 'float',
            'network_throughput_in_mbps': 'float'
        }

        self.attribute_map = {
            'cpu_core_count': 'cpuCoreCount',
            'memory_in_gbs': 'memoryInGBs',
            'network_bandwidth_in_gbps': 'networkBandwidthInGbps',
            'network_iops': 'networkIops',
            'network_throughput_in_mbps': 'networkThroughputInMbps'
        }

        self._cpu_core_count = None
        self._memory_in_gbs = None
        self._network_bandwidth_in_gbps = None
        self._network_iops = None
        self._network_throughput_in_mbps = None

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this ComputePerformanceSummary.
        The number of OCPU cores available.


        :return: The cpu_core_count of this ComputePerformanceSummary.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this ComputePerformanceSummary.
        The number of OCPU cores available.


        :param cpu_core_count: The cpu_core_count of this ComputePerformanceSummary.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def memory_in_gbs(self):
        """
        **[Required]** Gets the memory_in_gbs of this ComputePerformanceSummary.
        The amount of memory allocated for the VMDB System.


        :return: The memory_in_gbs of this ComputePerformanceSummary.
        :rtype: float
        """
        return self._memory_in_gbs

    @memory_in_gbs.setter
    def memory_in_gbs(self, memory_in_gbs):
        """
        Sets the memory_in_gbs of this ComputePerformanceSummary.
        The amount of memory allocated for the VMDB System.


        :param memory_in_gbs: The memory_in_gbs of this ComputePerformanceSummary.
        :type: float
        """
        self._memory_in_gbs = memory_in_gbs

    @property
    def network_bandwidth_in_gbps(self):
        """
        **[Required]** Gets the network_bandwidth_in_gbps of this ComputePerformanceSummary.
        The network bandwidth of the VMDB system in gbps.


        :return: The network_bandwidth_in_gbps of this ComputePerformanceSummary.
        :rtype: float
        """
        return self._network_bandwidth_in_gbps

    @network_bandwidth_in_gbps.setter
    def network_bandwidth_in_gbps(self, network_bandwidth_in_gbps):
        """
        Sets the network_bandwidth_in_gbps of this ComputePerformanceSummary.
        The network bandwidth of the VMDB system in gbps.


        :param network_bandwidth_in_gbps: The network_bandwidth_in_gbps of this ComputePerformanceSummary.
        :type: float
        """
        self._network_bandwidth_in_gbps = network_bandwidth_in_gbps

    @property
    def network_iops(self):
        """
        **[Required]** Gets the network_iops of this ComputePerformanceSummary.
        IOPS for the VMDB System.


        :return: The network_iops of this ComputePerformanceSummary.
        :rtype: float
        """
        return self._network_iops

    @network_iops.setter
    def network_iops(self, network_iops):
        """
        Sets the network_iops of this ComputePerformanceSummary.
        IOPS for the VMDB System.


        :param network_iops: The network_iops of this ComputePerformanceSummary.
        :type: float
        """
        self._network_iops = network_iops

    @property
    def network_throughput_in_mbps(self):
        """
        **[Required]** Gets the network_throughput_in_mbps of this ComputePerformanceSummary.
        Network throughput for the VMDB System.


        :return: The network_throughput_in_mbps of this ComputePerformanceSummary.
        :rtype: float
        """
        return self._network_throughput_in_mbps

    @network_throughput_in_mbps.setter
    def network_throughput_in_mbps(self, network_throughput_in_mbps):
        """
        Sets the network_throughput_in_mbps of this ComputePerformanceSummary.
        Network throughput for the VMDB System.


        :param network_throughput_in_mbps: The network_throughput_in_mbps of this ComputePerformanceSummary.
        :type: float
        """
        self._network_throughput_in_mbps = network_throughput_in_mbps

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
