# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddWorkerNodesDetails(object):
    """
    The information about added nodes.
    """

    #: A constant which can be used with the node_type property of a AddWorkerNodesDetails.
    #: This constant has a value of "WORKER"
    NODE_TYPE_WORKER = "WORKER"

    #: A constant which can be used with the node_type property of a AddWorkerNodesDetails.
    #: This constant has a value of "COMPUTE_ONLY_WORKER"
    NODE_TYPE_COMPUTE_ONLY_WORKER = "COMPUTE_ONLY_WORKER"

    def __init__(self, **kwargs):
        """
        Initializes a new AddWorkerNodesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this AddWorkerNodesDetails.
        :type cluster_admin_password: str

        :param number_of_worker_nodes:
            The value to assign to the number_of_worker_nodes property of this AddWorkerNodesDetails.
        :type number_of_worker_nodes: int

        :param node_type:
            The value to assign to the node_type property of this AddWorkerNodesDetails.
            Allowed values for this property are: "WORKER", "COMPUTE_ONLY_WORKER"
        :type node_type: str

        :param shape:
            The value to assign to the shape property of this AddWorkerNodesDetails.
        :type shape: str

        :param block_volume_size_in_gbs:
            The value to assign to the block_volume_size_in_gbs property of this AddWorkerNodesDetails.
        :type block_volume_size_in_gbs: int

        :param shape_config:
            The value to assign to the shape_config property of this AddWorkerNodesDetails.
        :type shape_config: oci.bds.models.ShapeConfigDetails

        """
        self.swagger_types = {
            'cluster_admin_password': 'str',
            'number_of_worker_nodes': 'int',
            'node_type': 'str',
            'shape': 'str',
            'block_volume_size_in_gbs': 'int',
            'shape_config': 'ShapeConfigDetails'
        }

        self.attribute_map = {
            'cluster_admin_password': 'clusterAdminPassword',
            'number_of_worker_nodes': 'numberOfWorkerNodes',
            'node_type': 'nodeType',
            'shape': 'shape',
            'block_volume_size_in_gbs': 'blockVolumeSizeInGBs',
            'shape_config': 'shapeConfig'
        }

        self._cluster_admin_password = None
        self._number_of_worker_nodes = None
        self._node_type = None
        self._shape = None
        self._block_volume_size_in_gbs = None
        self._shape_config = None

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this AddWorkerNodesDetails.
        Base-64 encoded password for the cluster (and Cloudera Manager) admin user.


        :return: The cluster_admin_password of this AddWorkerNodesDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this AddWorkerNodesDetails.
        Base-64 encoded password for the cluster (and Cloudera Manager) admin user.


        :param cluster_admin_password: The cluster_admin_password of this AddWorkerNodesDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def number_of_worker_nodes(self):
        """
        **[Required]** Gets the number_of_worker_nodes of this AddWorkerNodesDetails.
        Number of additional worker nodes for the cluster.


        :return: The number_of_worker_nodes of this AddWorkerNodesDetails.
        :rtype: int
        """
        return self._number_of_worker_nodes

    @number_of_worker_nodes.setter
    def number_of_worker_nodes(self, number_of_worker_nodes):
        """
        Sets the number_of_worker_nodes of this AddWorkerNodesDetails.
        Number of additional worker nodes for the cluster.


        :param number_of_worker_nodes: The number_of_worker_nodes of this AddWorkerNodesDetails.
        :type: int
        """
        self._number_of_worker_nodes = number_of_worker_nodes

    @property
    def node_type(self):
        """
        **[Required]** Gets the node_type of this AddWorkerNodesDetails.
        Worker node types, can either be Worker Data node or Compute only worker node.

        Allowed values for this property are: "WORKER", "COMPUTE_ONLY_WORKER"


        :return: The node_type of this AddWorkerNodesDetails.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """
        Sets the node_type of this AddWorkerNodesDetails.
        Worker node types, can either be Worker Data node or Compute only worker node.


        :param node_type: The node_type of this AddWorkerNodesDetails.
        :type: str
        """
        allowed_values = ["WORKER", "COMPUTE_ONLY_WORKER"]
        if not value_allowed_none_or_none_sentinel(node_type, allowed_values):
            raise ValueError(
                "Invalid value for `node_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._node_type = node_type

    @property
    def shape(self):
        """
        Gets the shape of this AddWorkerNodesDetails.
        Shape of the node. This has to be specified when adding compute only worker node at the first time. Otherwise, it's a read-only property.


        :return: The shape of this AddWorkerNodesDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this AddWorkerNodesDetails.
        Shape of the node. This has to be specified when adding compute only worker node at the first time. Otherwise, it's a read-only property.


        :param shape: The shape of this AddWorkerNodesDetails.
        :type: str
        """
        self._shape = shape

    @property
    def block_volume_size_in_gbs(self):
        """
        Gets the block_volume_size_in_gbs of this AddWorkerNodesDetails.
        The size of block volume in GB to be attached to the given node. This has to be specified when adding compute only worker node at the first time. Otherwise, it's a read-only property.


        :return: The block_volume_size_in_gbs of this AddWorkerNodesDetails.
        :rtype: int
        """
        return self._block_volume_size_in_gbs

    @block_volume_size_in_gbs.setter
    def block_volume_size_in_gbs(self, block_volume_size_in_gbs):
        """
        Sets the block_volume_size_in_gbs of this AddWorkerNodesDetails.
        The size of block volume in GB to be attached to the given node. This has to be specified when adding compute only worker node at the first time. Otherwise, it's a read-only property.


        :param block_volume_size_in_gbs: The block_volume_size_in_gbs of this AddWorkerNodesDetails.
        :type: int
        """
        self._block_volume_size_in_gbs = block_volume_size_in_gbs

    @property
    def shape_config(self):
        """
        Gets the shape_config of this AddWorkerNodesDetails.

        :return: The shape_config of this AddWorkerNodesDetails.
        :rtype: oci.bds.models.ShapeConfigDetails
        """
        return self._shape_config

    @shape_config.setter
    def shape_config(self, shape_config):
        """
        Sets the shape_config of this AddWorkerNodesDetails.

        :param shape_config: The shape_config of this AddWorkerNodesDetails.
        :type: oci.bds.models.ShapeConfigDetails
        """
        self._shape_config = shape_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
