# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NodePoolSummary(object):
    """
    The properties that define a node pool summary.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NodePoolSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this NodePoolSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this NodePoolSummary.
        :type compartment_id: str

        :param cluster_id:
            The value to assign to the cluster_id property of this NodePoolSummary.
        :type cluster_id: str

        :param name:
            The value to assign to the name property of this NodePoolSummary.
        :type name: str

        :param kubernetes_version:
            The value to assign to the kubernetes_version property of this NodePoolSummary.
        :type kubernetes_version: str

        :param node_image_id:
            The value to assign to the node_image_id property of this NodePoolSummary.
        :type node_image_id: str

        :param node_image_name:
            The value to assign to the node_image_name property of this NodePoolSummary.
        :type node_image_name: str

        :param node_source:
            The value to assign to the node_source property of this NodePoolSummary.
        :type node_source: NodeSourceOption

        :param node_shape:
            The value to assign to the node_shape property of this NodePoolSummary.
        :type node_shape: str

        :param initial_node_labels:
            The value to assign to the initial_node_labels property of this NodePoolSummary.
        :type initial_node_labels: list[KeyValue]

        :param ssh_public_key:
            The value to assign to the ssh_public_key property of this NodePoolSummary.
        :type ssh_public_key: str

        :param quantity_per_subnet:
            The value to assign to the quantity_per_subnet property of this NodePoolSummary.
        :type quantity_per_subnet: int

        :param subnet_ids:
            The value to assign to the subnet_ids property of this NodePoolSummary.
        :type subnet_ids: list[str]

        :param node_config_details:
            The value to assign to the node_config_details property of this NodePoolSummary.
        :type node_config_details: NodePoolNodeConfigDetails

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'cluster_id': 'str',
            'name': 'str',
            'kubernetes_version': 'str',
            'node_image_id': 'str',
            'node_image_name': 'str',
            'node_source': 'NodeSourceOption',
            'node_shape': 'str',
            'initial_node_labels': 'list[KeyValue]',
            'ssh_public_key': 'str',
            'quantity_per_subnet': 'int',
            'subnet_ids': 'list[str]',
            'node_config_details': 'NodePoolNodeConfigDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'cluster_id': 'clusterId',
            'name': 'name',
            'kubernetes_version': 'kubernetesVersion',
            'node_image_id': 'nodeImageId',
            'node_image_name': 'nodeImageName',
            'node_source': 'nodeSource',
            'node_shape': 'nodeShape',
            'initial_node_labels': 'initialNodeLabels',
            'ssh_public_key': 'sshPublicKey',
            'quantity_per_subnet': 'quantityPerSubnet',
            'subnet_ids': 'subnetIds',
            'node_config_details': 'nodeConfigDetails'
        }

        self._id = None
        self._compartment_id = None
        self._cluster_id = None
        self._name = None
        self._kubernetes_version = None
        self._node_image_id = None
        self._node_image_name = None
        self._node_source = None
        self._node_shape = None
        self._initial_node_labels = None
        self._ssh_public_key = None
        self._quantity_per_subnet = None
        self._subnet_ids = None
        self._node_config_details = None

    @property
    def id(self):
        """
        Gets the id of this NodePoolSummary.
        The OCID of the node pool.


        :return: The id of this NodePoolSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NodePoolSummary.
        The OCID of the node pool.


        :param id: The id of this NodePoolSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this NodePoolSummary.
        The OCID of the compartment in which the node pool exists.


        :return: The compartment_id of this NodePoolSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this NodePoolSummary.
        The OCID of the compartment in which the node pool exists.


        :param compartment_id: The compartment_id of this NodePoolSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cluster_id(self):
        """
        Gets the cluster_id of this NodePoolSummary.
        The OCID of the cluster to which this node pool is attached.


        :return: The cluster_id of this NodePoolSummary.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this NodePoolSummary.
        The OCID of the cluster to which this node pool is attached.


        :param cluster_id: The cluster_id of this NodePoolSummary.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def name(self):
        """
        Gets the name of this NodePoolSummary.
        The name of the node pool.


        :return: The name of this NodePoolSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NodePoolSummary.
        The name of the node pool.


        :param name: The name of this NodePoolSummary.
        :type: str
        """
        self._name = name

    @property
    def kubernetes_version(self):
        """
        Gets the kubernetes_version of this NodePoolSummary.
        The version of Kubernetes running on the nodes in the node pool.


        :return: The kubernetes_version of this NodePoolSummary.
        :rtype: str
        """
        return self._kubernetes_version

    @kubernetes_version.setter
    def kubernetes_version(self, kubernetes_version):
        """
        Sets the kubernetes_version of this NodePoolSummary.
        The version of Kubernetes running on the nodes in the node pool.


        :param kubernetes_version: The kubernetes_version of this NodePoolSummary.
        :type: str
        """
        self._kubernetes_version = kubernetes_version

    @property
    def node_image_id(self):
        """
        Gets the node_image_id of this NodePoolSummary.
        Deprecated. see `nodeSource`. The OCID of the image running on the nodes in the node pool.


        :return: The node_image_id of this NodePoolSummary.
        :rtype: str
        """
        return self._node_image_id

    @node_image_id.setter
    def node_image_id(self, node_image_id):
        """
        Sets the node_image_id of this NodePoolSummary.
        Deprecated. see `nodeSource`. The OCID of the image running on the nodes in the node pool.


        :param node_image_id: The node_image_id of this NodePoolSummary.
        :type: str
        """
        self._node_image_id = node_image_id

    @property
    def node_image_name(self):
        """
        Gets the node_image_name of this NodePoolSummary.
        Deprecated. see `nodeSource`. The name of the image running on the nodes in the node pool.


        :return: The node_image_name of this NodePoolSummary.
        :rtype: str
        """
        return self._node_image_name

    @node_image_name.setter
    def node_image_name(self, node_image_name):
        """
        Sets the node_image_name of this NodePoolSummary.
        Deprecated. see `nodeSource`. The name of the image running on the nodes in the node pool.


        :param node_image_name: The node_image_name of this NodePoolSummary.
        :type: str
        """
        self._node_image_name = node_image_name

    @property
    def node_source(self):
        """
        Gets the node_source of this NodePoolSummary.
        Source running on the nodes in the node pool.


        :return: The node_source of this NodePoolSummary.
        :rtype: NodeSourceOption
        """
        return self._node_source

    @node_source.setter
    def node_source(self, node_source):
        """
        Sets the node_source of this NodePoolSummary.
        Source running on the nodes in the node pool.


        :param node_source: The node_source of this NodePoolSummary.
        :type: NodeSourceOption
        """
        self._node_source = node_source

    @property
    def node_shape(self):
        """
        Gets the node_shape of this NodePoolSummary.
        The name of the node shape of the nodes in the node pool.


        :return: The node_shape of this NodePoolSummary.
        :rtype: str
        """
        return self._node_shape

    @node_shape.setter
    def node_shape(self, node_shape):
        """
        Sets the node_shape of this NodePoolSummary.
        The name of the node shape of the nodes in the node pool.


        :param node_shape: The node_shape of this NodePoolSummary.
        :type: str
        """
        self._node_shape = node_shape

    @property
    def initial_node_labels(self):
        """
        Gets the initial_node_labels of this NodePoolSummary.
        A list of key/value pairs to add to nodes after they join the Kubernetes cluster.


        :return: The initial_node_labels of this NodePoolSummary.
        :rtype: list[KeyValue]
        """
        return self._initial_node_labels

    @initial_node_labels.setter
    def initial_node_labels(self, initial_node_labels):
        """
        Sets the initial_node_labels of this NodePoolSummary.
        A list of key/value pairs to add to nodes after they join the Kubernetes cluster.


        :param initial_node_labels: The initial_node_labels of this NodePoolSummary.
        :type: list[KeyValue]
        """
        self._initial_node_labels = initial_node_labels

    @property
    def ssh_public_key(self):
        """
        Gets the ssh_public_key of this NodePoolSummary.
        The SSH public key on each node in the node pool.


        :return: The ssh_public_key of this NodePoolSummary.
        :rtype: str
        """
        return self._ssh_public_key

    @ssh_public_key.setter
    def ssh_public_key(self, ssh_public_key):
        """
        Sets the ssh_public_key of this NodePoolSummary.
        The SSH public key on each node in the node pool.


        :param ssh_public_key: The ssh_public_key of this NodePoolSummary.
        :type: str
        """
        self._ssh_public_key = ssh_public_key

    @property
    def quantity_per_subnet(self):
        """
        Gets the quantity_per_subnet of this NodePoolSummary.
        The number of nodes in each subnet.


        :return: The quantity_per_subnet of this NodePoolSummary.
        :rtype: int
        """
        return self._quantity_per_subnet

    @quantity_per_subnet.setter
    def quantity_per_subnet(self, quantity_per_subnet):
        """
        Sets the quantity_per_subnet of this NodePoolSummary.
        The number of nodes in each subnet.


        :param quantity_per_subnet: The quantity_per_subnet of this NodePoolSummary.
        :type: int
        """
        self._quantity_per_subnet = quantity_per_subnet

    @property
    def subnet_ids(self):
        """
        Gets the subnet_ids of this NodePoolSummary.
        The OCIDs of the subnets in which to place nodes for this node pool.


        :return: The subnet_ids of this NodePoolSummary.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """
        Sets the subnet_ids of this NodePoolSummary.
        The OCIDs of the subnets in which to place nodes for this node pool.


        :param subnet_ids: The subnet_ids of this NodePoolSummary.
        :type: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def node_config_details(self):
        """
        Gets the node_config_details of this NodePoolSummary.
        The configuration of nodes in the node pool.


        :return: The node_config_details of this NodePoolSummary.
        :rtype: NodePoolNodeConfigDetails
        """
        return self._node_config_details

    @node_config_details.setter
    def node_config_details(self, node_config_details):
        """
        Sets the node_config_details of this NodePoolSummary.
        The configuration of nodes in the node pool.


        :param node_config_details: The node_config_details of this NodePoolSummary.
        :type: NodePoolNodeConfigDetails
        """
        self._node_config_details = node_config_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
