# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmClusterSummary(object):
    """
    Partial information about the VM Cluster which includes name, memory allocated etc.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VmClusterSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vmcluster_name:
            The value to assign to the vmcluster_name property of this VmClusterSummary.
        :type vmcluster_name: str

        :param memory_allocated_in_gbs:
            The value to assign to the memory_allocated_in_gbs property of this VmClusterSummary.
        :type memory_allocated_in_gbs: int

        :param cpu_allocated:
            The value to assign to the cpu_allocated property of this VmClusterSummary.
        :type cpu_allocated: int

        :param db_nodes_count:
            The value to assign to the db_nodes_count property of this VmClusterSummary.
        :type db_nodes_count: int

        """
        self.swagger_types = {
            'vmcluster_name': 'str',
            'memory_allocated_in_gbs': 'int',
            'cpu_allocated': 'int',
            'db_nodes_count': 'int'
        }

        self.attribute_map = {
            'vmcluster_name': 'vmclusterName',
            'memory_allocated_in_gbs': 'memoryAllocatedInGBs',
            'cpu_allocated': 'cpuAllocated',
            'db_nodes_count': 'dbNodesCount'
        }

        self._vmcluster_name = None
        self._memory_allocated_in_gbs = None
        self._cpu_allocated = None
        self._db_nodes_count = None

    @property
    def vmcluster_name(self):
        """
        **[Required]** Gets the vmcluster_name of this VmClusterSummary.
        The name of the vm cluster.


        :return: The vmcluster_name of this VmClusterSummary.
        :rtype: str
        """
        return self._vmcluster_name

    @vmcluster_name.setter
    def vmcluster_name(self, vmcluster_name):
        """
        Sets the vmcluster_name of this VmClusterSummary.
        The name of the vm cluster.


        :param vmcluster_name: The vmcluster_name of this VmClusterSummary.
        :type: str
        """
        self._vmcluster_name = vmcluster_name

    @property
    def memory_allocated_in_gbs(self):
        """
        Gets the memory_allocated_in_gbs of this VmClusterSummary.
        The memory allocated on a vm cluster.


        :return: The memory_allocated_in_gbs of this VmClusterSummary.
        :rtype: int
        """
        return self._memory_allocated_in_gbs

    @memory_allocated_in_gbs.setter
    def memory_allocated_in_gbs(self, memory_allocated_in_gbs):
        """
        Sets the memory_allocated_in_gbs of this VmClusterSummary.
        The memory allocated on a vm cluster.


        :param memory_allocated_in_gbs: The memory_allocated_in_gbs of this VmClusterSummary.
        :type: int
        """
        self._memory_allocated_in_gbs = memory_allocated_in_gbs

    @property
    def cpu_allocated(self):
        """
        Gets the cpu_allocated of this VmClusterSummary.
        The cpu allocated on a vm cluster.


        :return: The cpu_allocated of this VmClusterSummary.
        :rtype: int
        """
        return self._cpu_allocated

    @cpu_allocated.setter
    def cpu_allocated(self, cpu_allocated):
        """
        Sets the cpu_allocated of this VmClusterSummary.
        The cpu allocated on a vm cluster.


        :param cpu_allocated: The cpu_allocated of this VmClusterSummary.
        :type: int
        """
        self._cpu_allocated = cpu_allocated

    @property
    def db_nodes_count(self):
        """
        Gets the db_nodes_count of this VmClusterSummary.
        The number of DB nodes on a vm cluster.


        :return: The db_nodes_count of this VmClusterSummary.
        :rtype: int
        """
        return self._db_nodes_count

    @db_nodes_count.setter
    def db_nodes_count(self, db_nodes_count):
        """
        Sets the db_nodes_count of this VmClusterSummary.
        The number of DB nodes on a vm cluster.


        :param db_nodes_count: The db_nodes_count of this VmClusterSummary.
        :type: int
        """
        self._db_nodes_count = db_nodes_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
