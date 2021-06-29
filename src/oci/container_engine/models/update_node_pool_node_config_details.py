# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNodePoolNodeConfigDetails(object):
    """
    The size and placement configuration of nodes in the node pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNodePoolNodeConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param size:
            The value to assign to the size property of this UpdateNodePoolNodeConfigDetails.
        :type size: int

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateNodePoolNodeConfigDetails.
        :type nsg_ids: list[str]

        :param placement_configs:
            The value to assign to the placement_configs property of this UpdateNodePoolNodeConfigDetails.
        :type placement_configs: list[oci.container_engine.models.NodePoolPlacementConfigDetails]

        """
        self.swagger_types = {
            'size': 'int',
            'nsg_ids': 'list[str]',
            'placement_configs': 'list[NodePoolPlacementConfigDetails]'
        }

        self.attribute_map = {
            'size': 'size',
            'nsg_ids': 'nsgIds',
            'placement_configs': 'placementConfigs'
        }

        self._size = None
        self._nsg_ids = None
        self._placement_configs = None

    @property
    def size(self):
        """
        Gets the size of this UpdateNodePoolNodeConfigDetails.
        The number of nodes in the node pool.


        :return: The size of this UpdateNodePoolNodeConfigDetails.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this UpdateNodePoolNodeConfigDetails.
        The number of nodes in the node pool.


        :param size: The size of this UpdateNodePoolNodeConfigDetails.
        :type: int
        """
        self._size = size

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateNodePoolNodeConfigDetails.
        The OCIDs of the Network Security Group(s) to associate nodes for this node pool with. For more information about NSGs, see :class:`NetworkSecurityGroup`.


        :return: The nsg_ids of this UpdateNodePoolNodeConfigDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateNodePoolNodeConfigDetails.
        The OCIDs of the Network Security Group(s) to associate nodes for this node pool with. For more information about NSGs, see :class:`NetworkSecurityGroup`.


        :param nsg_ids: The nsg_ids of this UpdateNodePoolNodeConfigDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def placement_configs(self):
        """
        Gets the placement_configs of this UpdateNodePoolNodeConfigDetails.
        The placement configurations for the node pool. Provide one placement
        configuration for each availability domain in which you intend to launch a node.

        To use the node pool with a regional subnet, provide a placement configuration for
        each availability domain, and include the regional subnet in each placement
        configuration.


        :return: The placement_configs of this UpdateNodePoolNodeConfigDetails.
        :rtype: list[oci.container_engine.models.NodePoolPlacementConfigDetails]
        """
        return self._placement_configs

    @placement_configs.setter
    def placement_configs(self, placement_configs):
        """
        Sets the placement_configs of this UpdateNodePoolNodeConfigDetails.
        The placement configurations for the node pool. Provide one placement
        configuration for each availability domain in which you intend to launch a node.

        To use the node pool with a regional subnet, provide a placement configuration for
        each availability domain, and include the regional subnet in each placement
        configuration.


        :param placement_configs: The placement_configs of this UpdateNodePoolNodeConfigDetails.
        :type: list[oci.container_engine.models.NodePoolPlacementConfigDetails]
        """
        self._placement_configs = placement_configs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
