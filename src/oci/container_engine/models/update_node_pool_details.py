# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateNodePoolDetails(object):
    """
    The properties that define a request to update a node pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateNodePoolDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this UpdateNodePoolDetails.
        :type name: str

        :param kubernetes_version:
            The value to assign to the kubernetes_version property of this UpdateNodePoolDetails.
        :type kubernetes_version: str

        :param initial_node_labels:
            The value to assign to the initial_node_labels property of this UpdateNodePoolDetails.
        :type initial_node_labels: list[KeyValue]

        :param quantity_per_subnet:
            The value to assign to the quantity_per_subnet property of this UpdateNodePoolDetails.
        :type quantity_per_subnet: int

        :param subnet_ids:
            The value to assign to the subnet_ids property of this UpdateNodePoolDetails.
        :type subnet_ids: list[str]

        :param node_config_details:
            The value to assign to the node_config_details property of this UpdateNodePoolDetails.
        :type node_config_details: UpdateNodePoolNodeConfigDetails

        :param node_metadata:
            The value to assign to the node_metadata property of this UpdateNodePoolDetails.
        :type node_metadata: dict(str, str)

        :param node_source_details:
            The value to assign to the node_source_details property of this UpdateNodePoolDetails.
        :type node_source_details: NodeSourceDetails

        :param ssh_public_key:
            The value to assign to the ssh_public_key property of this UpdateNodePoolDetails.
        :type ssh_public_key: str

        :param node_shape:
            The value to assign to the node_shape property of this UpdateNodePoolDetails.
        :type node_shape: str

        :param node_shape_config:
            The value to assign to the node_shape_config property of this UpdateNodePoolDetails.
        :type node_shape_config: UpdateNodeShapeConfigDetails

        """
        self.swagger_types = {
            'name': 'str',
            'kubernetes_version': 'str',
            'initial_node_labels': 'list[KeyValue]',
            'quantity_per_subnet': 'int',
            'subnet_ids': 'list[str]',
            'node_config_details': 'UpdateNodePoolNodeConfigDetails',
            'node_metadata': 'dict(str, str)',
            'node_source_details': 'NodeSourceDetails',
            'ssh_public_key': 'str',
            'node_shape': 'str',
            'node_shape_config': 'UpdateNodeShapeConfigDetails'
        }

        self.attribute_map = {
            'name': 'name',
            'kubernetes_version': 'kubernetesVersion',
            'initial_node_labels': 'initialNodeLabels',
            'quantity_per_subnet': 'quantityPerSubnet',
            'subnet_ids': 'subnetIds',
            'node_config_details': 'nodeConfigDetails',
            'node_metadata': 'nodeMetadata',
            'node_source_details': 'nodeSourceDetails',
            'ssh_public_key': 'sshPublicKey',
            'node_shape': 'nodeShape',
            'node_shape_config': 'nodeShapeConfig'
        }

        self._name = None
        self._kubernetes_version = None
        self._initial_node_labels = None
        self._quantity_per_subnet = None
        self._subnet_ids = None
        self._node_config_details = None
        self._node_metadata = None
        self._node_source_details = None
        self._ssh_public_key = None
        self._node_shape = None
        self._node_shape_config = None

    @property
    def name(self):
        """
        Gets the name of this UpdateNodePoolDetails.
        The new name for the cluster. Avoid entering confidential information.


        :return: The name of this UpdateNodePoolDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateNodePoolDetails.
        The new name for the cluster. Avoid entering confidential information.


        :param name: The name of this UpdateNodePoolDetails.
        :type: str
        """
        self._name = name

    @property
    def kubernetes_version(self):
        """
        Gets the kubernetes_version of this UpdateNodePoolDetails.
        The version of Kubernetes to which the nodes in the node pool should be upgraded.


        :return: The kubernetes_version of this UpdateNodePoolDetails.
        :rtype: str
        """
        return self._kubernetes_version

    @kubernetes_version.setter
    def kubernetes_version(self, kubernetes_version):
        """
        Sets the kubernetes_version of this UpdateNodePoolDetails.
        The version of Kubernetes to which the nodes in the node pool should be upgraded.


        :param kubernetes_version: The kubernetes_version of this UpdateNodePoolDetails.
        :type: str
        """
        self._kubernetes_version = kubernetes_version

    @property
    def initial_node_labels(self):
        """
        Gets the initial_node_labels of this UpdateNodePoolDetails.
        A list of key/value pairs to add to nodes after they join the Kubernetes cluster.


        :return: The initial_node_labels of this UpdateNodePoolDetails.
        :rtype: list[KeyValue]
        """
        return self._initial_node_labels

    @initial_node_labels.setter
    def initial_node_labels(self, initial_node_labels):
        """
        Sets the initial_node_labels of this UpdateNodePoolDetails.
        A list of key/value pairs to add to nodes after they join the Kubernetes cluster.


        :param initial_node_labels: The initial_node_labels of this UpdateNodePoolDetails.
        :type: list[KeyValue]
        """
        self._initial_node_labels = initial_node_labels

    @property
    def quantity_per_subnet(self):
        """
        Gets the quantity_per_subnet of this UpdateNodePoolDetails.
        The number of nodes to have in each subnet specified in the subnetIds property. This property is deprecated,
        use nodeConfigDetails instead. If the current value of quantityPerSubnet is greater than 0, you can only
        use quantityPerSubnet to scale the node pool. If the current value of quantityPerSubnet is equal to 0 and
        the current value of size in nodeConfigDetails is greater than 0, before you can use quantityPerSubnet,
        you must first scale the node pool to 0 nodes using nodeConfigDetails.


        :return: The quantity_per_subnet of this UpdateNodePoolDetails.
        :rtype: int
        """
        return self._quantity_per_subnet

    @quantity_per_subnet.setter
    def quantity_per_subnet(self, quantity_per_subnet):
        """
        Sets the quantity_per_subnet of this UpdateNodePoolDetails.
        The number of nodes to have in each subnet specified in the subnetIds property. This property is deprecated,
        use nodeConfigDetails instead. If the current value of quantityPerSubnet is greater than 0, you can only
        use quantityPerSubnet to scale the node pool. If the current value of quantityPerSubnet is equal to 0 and
        the current value of size in nodeConfigDetails is greater than 0, before you can use quantityPerSubnet,
        you must first scale the node pool to 0 nodes using nodeConfigDetails.


        :param quantity_per_subnet: The quantity_per_subnet of this UpdateNodePoolDetails.
        :type: int
        """
        self._quantity_per_subnet = quantity_per_subnet

    @property
    def subnet_ids(self):
        """
        Gets the subnet_ids of this UpdateNodePoolDetails.
        The OCIDs of the subnets in which to place nodes for this node pool. This property is deprecated,
        use nodeConfigDetails instead. Only one of the subnetIds or nodeConfigDetails
        properties can be specified.


        :return: The subnet_ids of this UpdateNodePoolDetails.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """
        Sets the subnet_ids of this UpdateNodePoolDetails.
        The OCIDs of the subnets in which to place nodes for this node pool. This property is deprecated,
        use nodeConfigDetails instead. Only one of the subnetIds or nodeConfigDetails
        properties can be specified.


        :param subnet_ids: The subnet_ids of this UpdateNodePoolDetails.
        :type: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def node_config_details(self):
        """
        Gets the node_config_details of this UpdateNodePoolDetails.
        The configuration of nodes in the node pool. Only one of the subnetIds or nodeConfigDetails
        properties should be specified. If the current value of quantityPerSubnet is greater than 0, the node
        pool may still be scaled using quantityPerSubnet. Before you can use nodeConfigDetails,
        you must first scale the node pool to 0 nodes using quantityPerSubnet.


        :return: The node_config_details of this UpdateNodePoolDetails.
        :rtype: UpdateNodePoolNodeConfigDetails
        """
        return self._node_config_details

    @node_config_details.setter
    def node_config_details(self, node_config_details):
        """
        Sets the node_config_details of this UpdateNodePoolDetails.
        The configuration of nodes in the node pool. Only one of the subnetIds or nodeConfigDetails
        properties should be specified. If the current value of quantityPerSubnet is greater than 0, the node
        pool may still be scaled using quantityPerSubnet. Before you can use nodeConfigDetails,
        you must first scale the node pool to 0 nodes using quantityPerSubnet.


        :param node_config_details: The node_config_details of this UpdateNodePoolDetails.
        :type: UpdateNodePoolNodeConfigDetails
        """
        self._node_config_details = node_config_details

    @property
    def node_metadata(self):
        """
        Gets the node_metadata of this UpdateNodePoolDetails.
        A list of key/value pairs to add to each underlying OCI instance in the node pool on launch.


        :return: The node_metadata of this UpdateNodePoolDetails.
        :rtype: dict(str, str)
        """
        return self._node_metadata

    @node_metadata.setter
    def node_metadata(self, node_metadata):
        """
        Sets the node_metadata of this UpdateNodePoolDetails.
        A list of key/value pairs to add to each underlying OCI instance in the node pool on launch.


        :param node_metadata: The node_metadata of this UpdateNodePoolDetails.
        :type: dict(str, str)
        """
        self._node_metadata = node_metadata

    @property
    def node_source_details(self):
        """
        Gets the node_source_details of this UpdateNodePoolDetails.
        Specify the source to use to launch nodes in the node pool. Currently, image is the only supported source.


        :return: The node_source_details of this UpdateNodePoolDetails.
        :rtype: NodeSourceDetails
        """
        return self._node_source_details

    @node_source_details.setter
    def node_source_details(self, node_source_details):
        """
        Sets the node_source_details of this UpdateNodePoolDetails.
        Specify the source to use to launch nodes in the node pool. Currently, image is the only supported source.


        :param node_source_details: The node_source_details of this UpdateNodePoolDetails.
        :type: NodeSourceDetails
        """
        self._node_source_details = node_source_details

    @property
    def ssh_public_key(self):
        """
        Gets the ssh_public_key of this UpdateNodePoolDetails.
        The SSH public key to add to each node in the node pool on launch.


        :return: The ssh_public_key of this UpdateNodePoolDetails.
        :rtype: str
        """
        return self._ssh_public_key

    @ssh_public_key.setter
    def ssh_public_key(self, ssh_public_key):
        """
        Sets the ssh_public_key of this UpdateNodePoolDetails.
        The SSH public key to add to each node in the node pool on launch.


        :param ssh_public_key: The ssh_public_key of this UpdateNodePoolDetails.
        :type: str
        """
        self._ssh_public_key = ssh_public_key

    @property
    def node_shape(self):
        """
        Gets the node_shape of this UpdateNodePoolDetails.
        The name of the node shape of the nodes in the node pool used on launch.


        :return: The node_shape of this UpdateNodePoolDetails.
        :rtype: str
        """
        return self._node_shape

    @node_shape.setter
    def node_shape(self, node_shape):
        """
        Sets the node_shape of this UpdateNodePoolDetails.
        The name of the node shape of the nodes in the node pool used on launch.


        :param node_shape: The node_shape of this UpdateNodePoolDetails.
        :type: str
        """
        self._node_shape = node_shape

    @property
    def node_shape_config(self):
        """
        Gets the node_shape_config of this UpdateNodePoolDetails.
        Specify the configuration of the shape to launch nodes in the node pool.


        :return: The node_shape_config of this UpdateNodePoolDetails.
        :rtype: UpdateNodeShapeConfigDetails
        """
        return self._node_shape_config

    @node_shape_config.setter
    def node_shape_config(self, node_shape_config):
        """
        Sets the node_shape_config of this UpdateNodePoolDetails.
        Specify the configuration of the shape to launch nodes in the node pool.


        :param node_shape_config: The node_shape_config of this UpdateNodePoolDetails.
        :type: UpdateNodeShapeConfigDetails
        """
        self._node_shape_config = node_shape_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
