# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodePoolNodeConfigDetails(object):
    """
    The size and placement configuration of nodes in the node pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodePoolNodeConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param size:
            The value to assign to the size property of this NodePoolNodeConfigDetails.
        :type size: int

        :param placement_configs:
            The value to assign to the placement_configs property of this NodePoolNodeConfigDetails.
        :type placement_configs: list[NodePoolPlacementConfigDetails]

        """
        self.swagger_types = {
            'size': 'int',
            'placement_configs': 'list[NodePoolPlacementConfigDetails]'
        }

        self.attribute_map = {
            'size': 'size',
            'placement_configs': 'placementConfigs'
        }

        self._size = None
        self._placement_configs = None

    @property
    def size(self):
        """
        Gets the size of this NodePoolNodeConfigDetails.
        The number of nodes in the node pool.


        :return: The size of this NodePoolNodeConfigDetails.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this NodePoolNodeConfigDetails.
        The number of nodes in the node pool.


        :param size: The size of this NodePoolNodeConfigDetails.
        :type: int
        """
        self._size = size

    @property
    def placement_configs(self):
        """
        Gets the placement_configs of this NodePoolNodeConfigDetails.
        The placement configurations for the node pool. Provide one placement
        configuration for each availability domain in which you intend to launch a node.

        To use the node pool with a regional subnet, provide a placement configuration for
        each availability domain, and include the regional subnet in each placement
        configuration.


        :return: The placement_configs of this NodePoolNodeConfigDetails.
        :rtype: list[NodePoolPlacementConfigDetails]
        """
        return self._placement_configs

    @placement_configs.setter
    def placement_configs(self, placement_configs):
        """
        Sets the placement_configs of this NodePoolNodeConfigDetails.
        The placement configurations for the node pool. Provide one placement
        configuration for each availability domain in which you intend to launch a node.

        To use the node pool with a regional subnet, provide a placement configuration for
        each availability domain, and include the regional subnet in each placement
        configuration.


        :param placement_configs: The placement_configs of this NodePoolNodeConfigDetails.
        :type: list[NodePoolPlacementConfigDetails]
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
