# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystemShapeSummary(object):
    """
    The shape of the DB system. The shape determines resources to allocate to the DB system - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator.
    If you're an administrator who needs to write policies to give users access,
    see `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystemShapeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DbSystemShapeSummary.
        :type name: str

        :param shape_family:
            The value to assign to the shape_family property of this DbSystemShapeSummary.
        :type shape_family: str

        :param shape:
            The value to assign to the shape property of this DbSystemShapeSummary.
        :type shape: str

        :param available_core_count:
            The value to assign to the available_core_count property of this DbSystemShapeSummary.
        :type available_core_count: int

        :param minimum_core_count:
            The value to assign to the minimum_core_count property of this DbSystemShapeSummary.
        :type minimum_core_count: int

        :param core_count_increment:
            The value to assign to the core_count_increment property of this DbSystemShapeSummary.
        :type core_count_increment: int

        :param min_core_count_per_node:
            The value to assign to the min_core_count_per_node property of this DbSystemShapeSummary.
        :type min_core_count_per_node: int

        :param available_memory_in_gbs:
            The value to assign to the available_memory_in_gbs property of this DbSystemShapeSummary.
        :type available_memory_in_gbs: int

        :param min_memory_per_node_in_g_bs:
            The value to assign to the min_memory_per_node_in_g_bs property of this DbSystemShapeSummary.
        :type min_memory_per_node_in_g_bs: int

        :param available_db_node_storage_in_g_bs:
            The value to assign to the available_db_node_storage_in_g_bs property of this DbSystemShapeSummary.
        :type available_db_node_storage_in_g_bs: int

        :param min_db_node_storage_per_node_in_g_bs:
            The value to assign to the min_db_node_storage_per_node_in_g_bs property of this DbSystemShapeSummary.
        :type min_db_node_storage_per_node_in_g_bs: int

        :param available_data_storage_in_t_bs:
            The value to assign to the available_data_storage_in_t_bs property of this DbSystemShapeSummary.
        :type available_data_storage_in_t_bs: int

        :param min_data_storage_in_t_bs:
            The value to assign to the min_data_storage_in_t_bs property of this DbSystemShapeSummary.
        :type min_data_storage_in_t_bs: int

        :param minimum_node_count:
            The value to assign to the minimum_node_count property of this DbSystemShapeSummary.
        :type minimum_node_count: int

        :param maximum_node_count:
            The value to assign to the maximum_node_count property of this DbSystemShapeSummary.
        :type maximum_node_count: int

        """
        self.swagger_types = {
            'name': 'str',
            'shape_family': 'str',
            'shape': 'str',
            'available_core_count': 'int',
            'minimum_core_count': 'int',
            'core_count_increment': 'int',
            'min_core_count_per_node': 'int',
            'available_memory_in_gbs': 'int',
            'min_memory_per_node_in_g_bs': 'int',
            'available_db_node_storage_in_g_bs': 'int',
            'min_db_node_storage_per_node_in_g_bs': 'int',
            'available_data_storage_in_t_bs': 'int',
            'min_data_storage_in_t_bs': 'int',
            'minimum_node_count': 'int',
            'maximum_node_count': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'shape_family': 'shapeFamily',
            'shape': 'shape',
            'available_core_count': 'availableCoreCount',
            'minimum_core_count': 'minimumCoreCount',
            'core_count_increment': 'coreCountIncrement',
            'min_core_count_per_node': 'minCoreCountPerNode',
            'available_memory_in_gbs': 'availableMemoryInGBs',
            'min_memory_per_node_in_g_bs': 'minMemoryPerNodeInGBs',
            'available_db_node_storage_in_g_bs': 'availableDbNodeStorageInGBs',
            'min_db_node_storage_per_node_in_g_bs': 'minDbNodeStoragePerNodeInGBs',
            'available_data_storage_in_t_bs': 'availableDataStorageInTBs',
            'min_data_storage_in_t_bs': 'minDataStorageInTBs',
            'minimum_node_count': 'minimumNodeCount',
            'maximum_node_count': 'maximumNodeCount'
        }

        self._name = None
        self._shape_family = None
        self._shape = None
        self._available_core_count = None
        self._minimum_core_count = None
        self._core_count_increment = None
        self._min_core_count_per_node = None
        self._available_memory_in_gbs = None
        self._min_memory_per_node_in_g_bs = None
        self._available_db_node_storage_in_g_bs = None
        self._min_db_node_storage_per_node_in_g_bs = None
        self._available_data_storage_in_t_bs = None
        self._min_data_storage_in_t_bs = None
        self._minimum_node_count = None
        self._maximum_node_count = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DbSystemShapeSummary.
        The name of the shape used for the DB system.


        :return: The name of this DbSystemShapeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DbSystemShapeSummary.
        The name of the shape used for the DB system.


        :param name: The name of this DbSystemShapeSummary.
        :type: str
        """
        self._name = name

    @property
    def shape_family(self):
        """
        Gets the shape_family of this DbSystemShapeSummary.
        The family of the shape used for the DB system.


        :return: The shape_family of this DbSystemShapeSummary.
        :rtype: str
        """
        return self._shape_family

    @shape_family.setter
    def shape_family(self, shape_family):
        """
        Sets the shape_family of this DbSystemShapeSummary.
        The family of the shape used for the DB system.


        :param shape_family: The shape_family of this DbSystemShapeSummary.
        :type: str
        """
        self._shape_family = shape_family

    @property
    def shape(self):
        """
        Gets the shape of this DbSystemShapeSummary.
        Deprecated. Use `name` instead of `shape`.


        :return: The shape of this DbSystemShapeSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this DbSystemShapeSummary.
        Deprecated. Use `name` instead of `shape`.


        :param shape: The shape of this DbSystemShapeSummary.
        :type: str
        """
        self._shape = shape

    @property
    def available_core_count(self):
        """
        **[Required]** Gets the available_core_count of this DbSystemShapeSummary.
        The maximum number of CPU cores that can be enabled on the DB system for this shape.


        :return: The available_core_count of this DbSystemShapeSummary.
        :rtype: int
        """
        return self._available_core_count

    @available_core_count.setter
    def available_core_count(self, available_core_count):
        """
        Sets the available_core_count of this DbSystemShapeSummary.
        The maximum number of CPU cores that can be enabled on the DB system for this shape.


        :param available_core_count: The available_core_count of this DbSystemShapeSummary.
        :type: int
        """
        self._available_core_count = available_core_count

    @property
    def minimum_core_count(self):
        """
        Gets the minimum_core_count of this DbSystemShapeSummary.
        The minimum number of CPU cores that can be enabled on the DB system for this shape.


        :return: The minimum_core_count of this DbSystemShapeSummary.
        :rtype: int
        """
        return self._minimum_core_count

    @minimum_core_count.setter
    def minimum_core_count(self, minimum_core_count):
        """
        Sets the minimum_core_count of this DbSystemShapeSummary.
        The minimum number of CPU cores that can be enabled on the DB system for this shape.


        :param minimum_core_count: The minimum_core_count of this DbSystemShapeSummary.
        :type: int
        """
        self._minimum_core_count = minimum_core_count

    @property
    def core_count_increment(self):
        """
        Gets the core_count_increment of this DbSystemShapeSummary.
        The discrete number by which the CPU core count for this shape can be increased or decreased.


        :return: The core_count_increment of this DbSystemShapeSummary.
        :rtype: int
        """
        return self._core_count_increment

    @core_count_increment.setter
    def core_count_increment(self, core_count_increment):
        """
        Sets the core_count_increment of this DbSystemShapeSummary.
        The discrete number by which the CPU core count for this shape can be increased or decreased.


        :param core_count_increment: The core_count_increment of this DbSystemShapeSummary.
        :type: int
        """
        self._core_count_increment = core_count_increment

    @property
    def min_core_count_per_node(self):
        """
        Gets the min_core_count_per_node of this DbSystemShapeSummary.
        The minimum number of CPU cores that can be enabled per node for this shape.


        :return: The min_core_count_per_node of this DbSystemShapeSummary.
        :rtype: int
        """
        return self._min_core_count_per_node

    @min_core_count_per_node.setter
    def min_core_count_per_node(self, min_core_count_per_node):
        """
        Sets the min_core_count_per_node of this DbSystemShapeSummary.
        The minimum number of CPU cores that can be enabled per node for this shape.


        :param min_core_count_per_node: The min_core_count_per_node of this DbSystemShapeSummary.
        :type: int
        """
        self._min_core_count_per_node = min_core_count_per_node

    @property
    def available_memory_in_gbs(self):
        """
        Gets the available_memory_in_gbs of this DbSystemShapeSummary.
        The maximum memory that can be enabled for this shape.


        :return: The available_memory_in_gbs of this DbSystemShapeSummary.
        :rtype: int
        """
        return self._available_memory_in_gbs

    @available_memory_in_gbs.setter
    def available_memory_in_gbs(self, available_memory_in_gbs):
        """
        Sets the available_memory_in_gbs of this DbSystemShapeSummary.
        The maximum memory that can be enabled for this shape.


        :param available_memory_in_gbs: The available_memory_in_gbs of this DbSystemShapeSummary.
        :type: int
        """
        self._available_memory_in_gbs = available_memory_in_gbs

    @property
    def min_memory_per_node_in_g_bs(self):
        """
        Gets the min_memory_per_node_in_g_bs of this DbSystemShapeSummary.
        The minimum memory that need be allocated per node for this shape.


        :return: The min_memory_per_node_in_g_bs of this DbSystemShapeSummary.
        :rtype: int
        """
        return self._min_memory_per_node_in_g_bs

    @min_memory_per_node_in_g_bs.setter
    def min_memory_per_node_in_g_bs(self, min_memory_per_node_in_g_bs):
        """
        Sets the min_memory_per_node_in_g_bs of this DbSystemShapeSummary.
        The minimum memory that need be allocated per node for this shape.


        :param min_memory_per_node_in_g_bs: The min_memory_per_node_in_g_bs of this DbSystemShapeSummary.
        :type: int
        """
        self._min_memory_per_node_in_g_bs = min_memory_per_node_in_g_bs

    @property
    def available_db_node_storage_in_g_bs(self):
        """
        Gets the available_db_node_storage_in_g_bs of this DbSystemShapeSummary.
        The maximum Db Node storage that can be enabled for this shape.


        :return: The available_db_node_storage_in_g_bs of this DbSystemShapeSummary.
        :rtype: int
        """
        return self._available_db_node_storage_in_g_bs

    @available_db_node_storage_in_g_bs.setter
    def available_db_node_storage_in_g_bs(self, available_db_node_storage_in_g_bs):
        """
        Sets the available_db_node_storage_in_g_bs of this DbSystemShapeSummary.
        The maximum Db Node storage that can be enabled for this shape.


        :param available_db_node_storage_in_g_bs: The available_db_node_storage_in_g_bs of this DbSystemShapeSummary.
        :type: int
        """
        self._available_db_node_storage_in_g_bs = available_db_node_storage_in_g_bs

    @property
    def min_db_node_storage_per_node_in_g_bs(self):
        """
        Gets the min_db_node_storage_per_node_in_g_bs of this DbSystemShapeSummary.
        The minimum Db Node storage that need be allocated per node for this shape.


        :return: The min_db_node_storage_per_node_in_g_bs of this DbSystemShapeSummary.
        :rtype: int
        """
        return self._min_db_node_storage_per_node_in_g_bs

    @min_db_node_storage_per_node_in_g_bs.setter
    def min_db_node_storage_per_node_in_g_bs(self, min_db_node_storage_per_node_in_g_bs):
        """
        Sets the min_db_node_storage_per_node_in_g_bs of this DbSystemShapeSummary.
        The minimum Db Node storage that need be allocated per node for this shape.


        :param min_db_node_storage_per_node_in_g_bs: The min_db_node_storage_per_node_in_g_bs of this DbSystemShapeSummary.
        :type: int
        """
        self._min_db_node_storage_per_node_in_g_bs = min_db_node_storage_per_node_in_g_bs

    @property
    def available_data_storage_in_t_bs(self):
        """
        Gets the available_data_storage_in_t_bs of this DbSystemShapeSummary.
        The maximum DATA storage that can be enabled for this shape.


        :return: The available_data_storage_in_t_bs of this DbSystemShapeSummary.
        :rtype: int
        """
        return self._available_data_storage_in_t_bs

    @available_data_storage_in_t_bs.setter
    def available_data_storage_in_t_bs(self, available_data_storage_in_t_bs):
        """
        Sets the available_data_storage_in_t_bs of this DbSystemShapeSummary.
        The maximum DATA storage that can be enabled for this shape.


        :param available_data_storage_in_t_bs: The available_data_storage_in_t_bs of this DbSystemShapeSummary.
        :type: int
        """
        self._available_data_storage_in_t_bs = available_data_storage_in_t_bs

    @property
    def min_data_storage_in_t_bs(self):
        """
        Gets the min_data_storage_in_t_bs of this DbSystemShapeSummary.
        The minimum data storage that need be allocated for this shape.


        :return: The min_data_storage_in_t_bs of this DbSystemShapeSummary.
        :rtype: int
        """
        return self._min_data_storage_in_t_bs

    @min_data_storage_in_t_bs.setter
    def min_data_storage_in_t_bs(self, min_data_storage_in_t_bs):
        """
        Sets the min_data_storage_in_t_bs of this DbSystemShapeSummary.
        The minimum data storage that need be allocated for this shape.


        :param min_data_storage_in_t_bs: The min_data_storage_in_t_bs of this DbSystemShapeSummary.
        :type: int
        """
        self._min_data_storage_in_t_bs = min_data_storage_in_t_bs

    @property
    def minimum_node_count(self):
        """
        Gets the minimum_node_count of this DbSystemShapeSummary.
        The minimum number of database nodes available for this shape.


        :return: The minimum_node_count of this DbSystemShapeSummary.
        :rtype: int
        """
        return self._minimum_node_count

    @minimum_node_count.setter
    def minimum_node_count(self, minimum_node_count):
        """
        Sets the minimum_node_count of this DbSystemShapeSummary.
        The minimum number of database nodes available for this shape.


        :param minimum_node_count: The minimum_node_count of this DbSystemShapeSummary.
        :type: int
        """
        self._minimum_node_count = minimum_node_count

    @property
    def maximum_node_count(self):
        """
        Gets the maximum_node_count of this DbSystemShapeSummary.
        The maximum number of database nodes available for this shape.


        :return: The maximum_node_count of this DbSystemShapeSummary.
        :rtype: int
        """
        return self._maximum_node_count

    @maximum_node_count.setter
    def maximum_node_count(self, maximum_node_count):
        """
        Sets the maximum_node_count of this DbSystemShapeSummary.
        The maximum number of database nodes available for this shape.


        :param maximum_node_count: The maximum_node_count of this DbSystemShapeSummary.
        :type: int
        """
        self._maximum_node_count = maximum_node_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
