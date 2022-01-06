# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNodeDetails(object):
    """
    The information about the new node.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNodeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param node_type:
            The value to assign to the node_type property of this CreateNodeDetails.
        :type node_type: str

        :param shape:
            The value to assign to the shape property of this CreateNodeDetails.
        :type shape: str

        :param block_volume_size_in_gbs:
            The value to assign to the block_volume_size_in_gbs property of this CreateNodeDetails.
        :type block_volume_size_in_gbs: int

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateNodeDetails.
        :type subnet_id: str

        """
        self.swagger_types = {
            'node_type': 'str',
            'shape': 'str',
            'block_volume_size_in_gbs': 'int',
            'subnet_id': 'str'
        }

        self.attribute_map = {
            'node_type': 'nodeType',
            'shape': 'shape',
            'block_volume_size_in_gbs': 'blockVolumeSizeInGBs',
            'subnet_id': 'subnetId'
        }

        self._node_type = None
        self._shape = None
        self._block_volume_size_in_gbs = None
        self._subnet_id = None

    @property
    def node_type(self):
        """
        **[Required]** Gets the node_type of this CreateNodeDetails.
        The Big Data Service cluster node type.


        :return: The node_type of this CreateNodeDetails.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """
        Sets the node_type of this CreateNodeDetails.
        The Big Data Service cluster node type.


        :param node_type: The node_type of this CreateNodeDetails.
        :type: str
        """
        self._node_type = node_type

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this CreateNodeDetails.
        Shape of the node.


        :return: The shape of this CreateNodeDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this CreateNodeDetails.
        Shape of the node.


        :param shape: The shape of this CreateNodeDetails.
        :type: str
        """
        self._shape = shape

    @property
    def block_volume_size_in_gbs(self):
        """
        **[Required]** Gets the block_volume_size_in_gbs of this CreateNodeDetails.
        The size of block volume in GB to be attached to a given node. All the
        details needed for attaching the block volume are managed by service itself.


        :return: The block_volume_size_in_gbs of this CreateNodeDetails.
        :rtype: int
        """
        return self._block_volume_size_in_gbs

    @block_volume_size_in_gbs.setter
    def block_volume_size_in_gbs(self, block_volume_size_in_gbs):
        """
        Sets the block_volume_size_in_gbs of this CreateNodeDetails.
        The size of block volume in GB to be attached to a given node. All the
        details needed for attaching the block volume are managed by service itself.


        :param block_volume_size_in_gbs: The block_volume_size_in_gbs of this CreateNodeDetails.
        :type: int
        """
        self._block_volume_size_in_gbs = block_volume_size_in_gbs

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateNodeDetails.
        The OCID of the subnet in which the node will be created.


        :return: The subnet_id of this CreateNodeDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateNodeDetails.
        The OCID of the subnet in which the node will be created.


        :param subnet_id: The subnet_id of this CreateNodeDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
