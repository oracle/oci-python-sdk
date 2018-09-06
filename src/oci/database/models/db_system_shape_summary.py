# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystemShapeSummary(object):
    """
    The shape of the DB system. The shape determines resources to allocate to the DB system - CPU cores and memory for VM shapes; CPU cores, memory and storage for non-VM (or bare metal) shapes.
    For a description of shapes, see `DB System Launch Options`__.
    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator.
    If you're an administrator who needs to write policies to give users access,
    see `Getting Started with Policies`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Database/References/launchoptions.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystemShapeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param available_core_count:
            The value to assign to the available_core_count property of this DbSystemShapeSummary.
        :type available_core_count: int

        :param core_count_increment:
            The value to assign to the core_count_increment property of this DbSystemShapeSummary.
        :type core_count_increment: int

        :param maximum_node_count:
            The value to assign to the maximum_node_count property of this DbSystemShapeSummary.
        :type maximum_node_count: int

        :param minimum_core_count:
            The value to assign to the minimum_core_count property of this DbSystemShapeSummary.
        :type minimum_core_count: int

        :param minimum_node_count:
            The value to assign to the minimum_node_count property of this DbSystemShapeSummary.
        :type minimum_node_count: int

        :param name:
            The value to assign to the name property of this DbSystemShapeSummary.
        :type name: str

        :param shape:
            The value to assign to the shape property of this DbSystemShapeSummary.
        :type shape: str

        """
        self.swagger_types = {
            'available_core_count': 'int',
            'core_count_increment': 'int',
            'maximum_node_count': 'int',
            'minimum_core_count': 'int',
            'minimum_node_count': 'int',
            'name': 'str',
            'shape': 'str'
        }

        self.attribute_map = {
            'available_core_count': 'availableCoreCount',
            'core_count_increment': 'coreCountIncrement',
            'maximum_node_count': 'maximumNodeCount',
            'minimum_core_count': 'minimumCoreCount',
            'minimum_node_count': 'minimumNodeCount',
            'name': 'name',
            'shape': 'shape'
        }

        self._available_core_count = None
        self._core_count_increment = None
        self._maximum_node_count = None
        self._minimum_core_count = None
        self._minimum_node_count = None
        self._name = None
        self._shape = None

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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
