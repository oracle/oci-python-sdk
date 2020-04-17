# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousExadataInfrastructureShapeSummary(object):
    """
    The shape of the Autonomous Exadata Infrastructure. The shape determines resources to allocate to the Autonomous Exadata Infrastructure (CPU cores, memory and storage).

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator.
    If you're an administrator who needs to write policies to give users access,
    see `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousExadataInfrastructureShapeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AutonomousExadataInfrastructureShapeSummary.
        :type name: str

        :param available_core_count:
            The value to assign to the available_core_count property of this AutonomousExadataInfrastructureShapeSummary.
        :type available_core_count: int

        :param minimum_core_count:
            The value to assign to the minimum_core_count property of this AutonomousExadataInfrastructureShapeSummary.
        :type minimum_core_count: int

        :param core_count_increment:
            The value to assign to the core_count_increment property of this AutonomousExadataInfrastructureShapeSummary.
        :type core_count_increment: int

        :param minimum_node_count:
            The value to assign to the minimum_node_count property of this AutonomousExadataInfrastructureShapeSummary.
        :type minimum_node_count: int

        :param maximum_node_count:
            The value to assign to the maximum_node_count property of this AutonomousExadataInfrastructureShapeSummary.
        :type maximum_node_count: int

        """
        self.swagger_types = {
            'name': 'str',
            'available_core_count': 'int',
            'minimum_core_count': 'int',
            'core_count_increment': 'int',
            'minimum_node_count': 'int',
            'maximum_node_count': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'available_core_count': 'availableCoreCount',
            'minimum_core_count': 'minimumCoreCount',
            'core_count_increment': 'coreCountIncrement',
            'minimum_node_count': 'minimumNodeCount',
            'maximum_node_count': 'maximumNodeCount'
        }

        self._name = None
        self._available_core_count = None
        self._minimum_core_count = None
        self._core_count_increment = None
        self._minimum_node_count = None
        self._maximum_node_count = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AutonomousExadataInfrastructureShapeSummary.
        The name of the shape used for the Autonomous Exadata Infrastructure.


        :return: The name of this AutonomousExadataInfrastructureShapeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AutonomousExadataInfrastructureShapeSummary.
        The name of the shape used for the Autonomous Exadata Infrastructure.


        :param name: The name of this AutonomousExadataInfrastructureShapeSummary.
        :type: str
        """
        self._name = name

    @property
    def available_core_count(self):
        """
        **[Required]** Gets the available_core_count of this AutonomousExadataInfrastructureShapeSummary.
        The maximum number of CPU cores that can be enabled on the Autonomous Exadata Infrastructure.


        :return: The available_core_count of this AutonomousExadataInfrastructureShapeSummary.
        :rtype: int
        """
        return self._available_core_count

    @available_core_count.setter
    def available_core_count(self, available_core_count):
        """
        Sets the available_core_count of this AutonomousExadataInfrastructureShapeSummary.
        The maximum number of CPU cores that can be enabled on the Autonomous Exadata Infrastructure.


        :param available_core_count: The available_core_count of this AutonomousExadataInfrastructureShapeSummary.
        :type: int
        """
        self._available_core_count = available_core_count

    @property
    def minimum_core_count(self):
        """
        Gets the minimum_core_count of this AutonomousExadataInfrastructureShapeSummary.
        The minimum number of CPU cores that can be enabled on the Autonomous Exadata Infrastructure.


        :return: The minimum_core_count of this AutonomousExadataInfrastructureShapeSummary.
        :rtype: int
        """
        return self._minimum_core_count

    @minimum_core_count.setter
    def minimum_core_count(self, minimum_core_count):
        """
        Sets the minimum_core_count of this AutonomousExadataInfrastructureShapeSummary.
        The minimum number of CPU cores that can be enabled on the Autonomous Exadata Infrastructure.


        :param minimum_core_count: The minimum_core_count of this AutonomousExadataInfrastructureShapeSummary.
        :type: int
        """
        self._minimum_core_count = minimum_core_count

    @property
    def core_count_increment(self):
        """
        Gets the core_count_increment of this AutonomousExadataInfrastructureShapeSummary.
        The increment in which core count can be increased or decreased.


        :return: The core_count_increment of this AutonomousExadataInfrastructureShapeSummary.
        :rtype: int
        """
        return self._core_count_increment

    @core_count_increment.setter
    def core_count_increment(self, core_count_increment):
        """
        Sets the core_count_increment of this AutonomousExadataInfrastructureShapeSummary.
        The increment in which core count can be increased or decreased.


        :param core_count_increment: The core_count_increment of this AutonomousExadataInfrastructureShapeSummary.
        :type: int
        """
        self._core_count_increment = core_count_increment

    @property
    def minimum_node_count(self):
        """
        Gets the minimum_node_count of this AutonomousExadataInfrastructureShapeSummary.
        The minimum number of nodes available for the shape.


        :return: The minimum_node_count of this AutonomousExadataInfrastructureShapeSummary.
        :rtype: int
        """
        return self._minimum_node_count

    @minimum_node_count.setter
    def minimum_node_count(self, minimum_node_count):
        """
        Sets the minimum_node_count of this AutonomousExadataInfrastructureShapeSummary.
        The minimum number of nodes available for the shape.


        :param minimum_node_count: The minimum_node_count of this AutonomousExadataInfrastructureShapeSummary.
        :type: int
        """
        self._minimum_node_count = minimum_node_count

    @property
    def maximum_node_count(self):
        """
        Gets the maximum_node_count of this AutonomousExadataInfrastructureShapeSummary.
        The maximum number of nodes available for the shape.


        :return: The maximum_node_count of this AutonomousExadataInfrastructureShapeSummary.
        :rtype: int
        """
        return self._maximum_node_count

    @maximum_node_count.setter
    def maximum_node_count(self, maximum_node_count):
        """
        Sets the maximum_node_count of this AutonomousExadataInfrastructureShapeSummary.
        The maximum number of nodes available for the shape.


        :param maximum_node_count: The maximum_node_count of this AutonomousExadataInfrastructureShapeSummary.
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
