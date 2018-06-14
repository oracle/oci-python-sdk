# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNodePoolDetails(object):
    """
    The properties that define a request to create a node pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNodePoolDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateNodePoolDetails.
        :type compartment_id: str

        :param cluster_id:
            The value to assign to the cluster_id property of this CreateNodePoolDetails.
        :type cluster_id: str

        :param name:
            The value to assign to the name property of this CreateNodePoolDetails.
        :type name: str

        :param kubernetes_version:
            The value to assign to the kubernetes_version property of this CreateNodePoolDetails.
        :type kubernetes_version: str

        :param node_image_name:
            The value to assign to the node_image_name property of this CreateNodePoolDetails.
        :type node_image_name: str

        :param node_shape:
            The value to assign to the node_shape property of this CreateNodePoolDetails.
        :type node_shape: str

        :param initial_node_labels:
            The value to assign to the initial_node_labels property of this CreateNodePoolDetails.
        :type initial_node_labels: list[KeyValue]

        :param ssh_public_key:
            The value to assign to the ssh_public_key property of this CreateNodePoolDetails.
        :type ssh_public_key: str

        :param quantity_per_subnet:
            The value to assign to the quantity_per_subnet property of this CreateNodePoolDetails.
        :type quantity_per_subnet: int

        :param subnet_ids:
            The value to assign to the subnet_ids property of this CreateNodePoolDetails.
        :type subnet_ids: list[str]

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'cluster_id': 'str',
            'name': 'str',
            'kubernetes_version': 'str',
            'node_image_name': 'str',
            'node_shape': 'str',
            'initial_node_labels': 'list[KeyValue]',
            'ssh_public_key': 'str',
            'quantity_per_subnet': 'int',
            'subnet_ids': 'list[str]'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'cluster_id': 'clusterId',
            'name': 'name',
            'kubernetes_version': 'kubernetesVersion',
            'node_image_name': 'nodeImageName',
            'node_shape': 'nodeShape',
            'initial_node_labels': 'initialNodeLabels',
            'ssh_public_key': 'sshPublicKey',
            'quantity_per_subnet': 'quantityPerSubnet',
            'subnet_ids': 'subnetIds'
        }

        self._compartment_id = None
        self._cluster_id = None
        self._name = None
        self._kubernetes_version = None
        self._node_image_name = None
        self._node_shape = None
        self._initial_node_labels = None
        self._ssh_public_key = None
        self._quantity_per_subnet = None
        self._subnet_ids = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateNodePoolDetails.
        The OCID of the compartment in which the node pool exists.


        :return: The compartment_id of this CreateNodePoolDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateNodePoolDetails.
        The OCID of the compartment in which the node pool exists.


        :param compartment_id: The compartment_id of this CreateNodePoolDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cluster_id(self):
        """
        **[Required]** Gets the cluster_id of this CreateNodePoolDetails.
        The OCID of the cluster to which this node pool is attached.


        :return: The cluster_id of this CreateNodePoolDetails.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """
        Sets the cluster_id of this CreateNodePoolDetails.
        The OCID of the cluster to which this node pool is attached.


        :param cluster_id: The cluster_id of this CreateNodePoolDetails.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateNodePoolDetails.
        The name of the node pool. Avoid entering confidential information.


        :return: The name of this CreateNodePoolDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateNodePoolDetails.
        The name of the node pool. Avoid entering confidential information.


        :param name: The name of this CreateNodePoolDetails.
        :type: str
        """
        self._name = name

    @property
    def kubernetes_version(self):
        """
        **[Required]** Gets the kubernetes_version of this CreateNodePoolDetails.
        The version of Kubernetes to install on the nodes in the node pool.


        :return: The kubernetes_version of this CreateNodePoolDetails.
        :rtype: str
        """
        return self._kubernetes_version

    @kubernetes_version.setter
    def kubernetes_version(self, kubernetes_version):
        """
        Sets the kubernetes_version of this CreateNodePoolDetails.
        The version of Kubernetes to install on the nodes in the node pool.


        :param kubernetes_version: The kubernetes_version of this CreateNodePoolDetails.
        :type: str
        """
        self._kubernetes_version = kubernetes_version

    @property
    def node_image_name(self):
        """
        **[Required]** Gets the node_image_name of this CreateNodePoolDetails.
        The name of the image running on the nodes in the node pool.


        :return: The node_image_name of this CreateNodePoolDetails.
        :rtype: str
        """
        return self._node_image_name

    @node_image_name.setter
    def node_image_name(self, node_image_name):
        """
        Sets the node_image_name of this CreateNodePoolDetails.
        The name of the image running on the nodes in the node pool.


        :param node_image_name: The node_image_name of this CreateNodePoolDetails.
        :type: str
        """
        self._node_image_name = node_image_name

    @property
    def node_shape(self):
        """
        **[Required]** Gets the node_shape of this CreateNodePoolDetails.
        The name of the node shape of the nodes in the node pool.


        :return: The node_shape of this CreateNodePoolDetails.
        :rtype: str
        """
        return self._node_shape

    @node_shape.setter
    def node_shape(self, node_shape):
        """
        Sets the node_shape of this CreateNodePoolDetails.
        The name of the node shape of the nodes in the node pool.


        :param node_shape: The node_shape of this CreateNodePoolDetails.
        :type: str
        """
        self._node_shape = node_shape

    @property
    def initial_node_labels(self):
        """
        Gets the initial_node_labels of this CreateNodePoolDetails.
        A list of key/value pairs to add to nodes after they join the Kubernetes cluster.


        :return: The initial_node_labels of this CreateNodePoolDetails.
        :rtype: list[KeyValue]
        """
        return self._initial_node_labels

    @initial_node_labels.setter
    def initial_node_labels(self, initial_node_labels):
        """
        Sets the initial_node_labels of this CreateNodePoolDetails.
        A list of key/value pairs to add to nodes after they join the Kubernetes cluster.


        :param initial_node_labels: The initial_node_labels of this CreateNodePoolDetails.
        :type: list[KeyValue]
        """
        self._initial_node_labels = initial_node_labels

    @property
    def ssh_public_key(self):
        """
        Gets the ssh_public_key of this CreateNodePoolDetails.
        The SSH public key to add to each node in the node pool.


        :return: The ssh_public_key of this CreateNodePoolDetails.
        :rtype: str
        """
        return self._ssh_public_key

    @ssh_public_key.setter
    def ssh_public_key(self, ssh_public_key):
        """
        Sets the ssh_public_key of this CreateNodePoolDetails.
        The SSH public key to add to each node in the node pool.


        :param ssh_public_key: The ssh_public_key of this CreateNodePoolDetails.
        :type: str
        """
        self._ssh_public_key = ssh_public_key

    @property
    def quantity_per_subnet(self):
        """
        Gets the quantity_per_subnet of this CreateNodePoolDetails.
        The number of nodes to create in each subnet.


        :return: The quantity_per_subnet of this CreateNodePoolDetails.
        :rtype: int
        """
        return self._quantity_per_subnet

    @quantity_per_subnet.setter
    def quantity_per_subnet(self, quantity_per_subnet):
        """
        Sets the quantity_per_subnet of this CreateNodePoolDetails.
        The number of nodes to create in each subnet.


        :param quantity_per_subnet: The quantity_per_subnet of this CreateNodePoolDetails.
        :type: int
        """
        self._quantity_per_subnet = quantity_per_subnet

    @property
    def subnet_ids(self):
        """
        **[Required]** Gets the subnet_ids of this CreateNodePoolDetails.
        The OCIDs of the subnets in which to place nodes for this node pool.


        :return: The subnet_ids of this CreateNodePoolDetails.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """
        Sets the subnet_ids of this CreateNodePoolDetails.
        The OCIDs of the subnets in which to place nodes for this node pool.


        :param subnet_ids: The subnet_ids of this CreateNodePoolDetails.
        :type: list[str]
        """
        self._subnet_ids = subnet_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
