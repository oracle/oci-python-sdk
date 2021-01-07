# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


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

        :param node_metadata:
            The value to assign to the node_metadata property of this CreateNodePoolDetails.
        :type node_metadata: dict(str, str)

        :param node_image_name:
            The value to assign to the node_image_name property of this CreateNodePoolDetails.
        :type node_image_name: str

        :param node_source_details:
            The value to assign to the node_source_details property of this CreateNodePoolDetails.
        :type node_source_details: oci.container_engine.models.NodeSourceDetails

        :param node_shape:
            The value to assign to the node_shape property of this CreateNodePoolDetails.
        :type node_shape: str

        :param node_shape_config:
            The value to assign to the node_shape_config property of this CreateNodePoolDetails.
        :type node_shape_config: oci.container_engine.models.CreateNodeShapeConfigDetails

        :param initial_node_labels:
            The value to assign to the initial_node_labels property of this CreateNodePoolDetails.
        :type initial_node_labels: list[oci.container_engine.models.KeyValue]

        :param ssh_public_key:
            The value to assign to the ssh_public_key property of this CreateNodePoolDetails.
        :type ssh_public_key: str

        :param quantity_per_subnet:
            The value to assign to the quantity_per_subnet property of this CreateNodePoolDetails.
        :type quantity_per_subnet: int

        :param subnet_ids:
            The value to assign to the subnet_ids property of this CreateNodePoolDetails.
        :type subnet_ids: list[str]

        :param node_config_details:
            The value to assign to the node_config_details property of this CreateNodePoolDetails.
        :type node_config_details: oci.container_engine.models.CreateNodePoolNodeConfigDetails

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'cluster_id': 'str',
            'name': 'str',
            'kubernetes_version': 'str',
            'node_metadata': 'dict(str, str)',
            'node_image_name': 'str',
            'node_source_details': 'NodeSourceDetails',
            'node_shape': 'str',
            'node_shape_config': 'CreateNodeShapeConfigDetails',
            'initial_node_labels': 'list[KeyValue]',
            'ssh_public_key': 'str',
            'quantity_per_subnet': 'int',
            'subnet_ids': 'list[str]',
            'node_config_details': 'CreateNodePoolNodeConfigDetails'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'cluster_id': 'clusterId',
            'name': 'name',
            'kubernetes_version': 'kubernetesVersion',
            'node_metadata': 'nodeMetadata',
            'node_image_name': 'nodeImageName',
            'node_source_details': 'nodeSourceDetails',
            'node_shape': 'nodeShape',
            'node_shape_config': 'nodeShapeConfig',
            'initial_node_labels': 'initialNodeLabels',
            'ssh_public_key': 'sshPublicKey',
            'quantity_per_subnet': 'quantityPerSubnet',
            'subnet_ids': 'subnetIds',
            'node_config_details': 'nodeConfigDetails'
        }

        self._compartment_id = None
        self._cluster_id = None
        self._name = None
        self._kubernetes_version = None
        self._node_metadata = None
        self._node_image_name = None
        self._node_source_details = None
        self._node_shape = None
        self._node_shape_config = None
        self._initial_node_labels = None
        self._ssh_public_key = None
        self._quantity_per_subnet = None
        self._subnet_ids = None
        self._node_config_details = None

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
    def node_metadata(self):
        """
        Gets the node_metadata of this CreateNodePoolDetails.
        A list of key/value pairs to add to each underlying OCI instance in the node pool on launch.


        :return: The node_metadata of this CreateNodePoolDetails.
        :rtype: dict(str, str)
        """
        return self._node_metadata

    @node_metadata.setter
    def node_metadata(self, node_metadata):
        """
        Sets the node_metadata of this CreateNodePoolDetails.
        A list of key/value pairs to add to each underlying OCI instance in the node pool on launch.


        :param node_metadata: The node_metadata of this CreateNodePoolDetails.
        :type: dict(str, str)
        """
        self._node_metadata = node_metadata

    @property
    def node_image_name(self):
        """
        Gets the node_image_name of this CreateNodePoolDetails.
        Deprecated. Use `nodeSourceDetails` instead.
        If you specify values for both, this value is ignored.
        The name of the image running on the nodes in the node pool.


        :return: The node_image_name of this CreateNodePoolDetails.
        :rtype: str
        """
        return self._node_image_name

    @node_image_name.setter
    def node_image_name(self, node_image_name):
        """
        Sets the node_image_name of this CreateNodePoolDetails.
        Deprecated. Use `nodeSourceDetails` instead.
        If you specify values for both, this value is ignored.
        The name of the image running on the nodes in the node pool.


        :param node_image_name: The node_image_name of this CreateNodePoolDetails.
        :type: str
        """
        self._node_image_name = node_image_name

    @property
    def node_source_details(self):
        """
        Gets the node_source_details of this CreateNodePoolDetails.
        Specify the source to use to launch nodes in the node pool. Currently, image is the only supported source.


        :return: The node_source_details of this CreateNodePoolDetails.
        :rtype: oci.container_engine.models.NodeSourceDetails
        """
        return self._node_source_details

    @node_source_details.setter
    def node_source_details(self, node_source_details):
        """
        Sets the node_source_details of this CreateNodePoolDetails.
        Specify the source to use to launch nodes in the node pool. Currently, image is the only supported source.


        :param node_source_details: The node_source_details of this CreateNodePoolDetails.
        :type: oci.container_engine.models.NodeSourceDetails
        """
        self._node_source_details = node_source_details

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
    def node_shape_config(self):
        """
        Gets the node_shape_config of this CreateNodePoolDetails.
        Specify the configuration of the shape to launch nodes in the node pool.


        :return: The node_shape_config of this CreateNodePoolDetails.
        :rtype: oci.container_engine.models.CreateNodeShapeConfigDetails
        """
        return self._node_shape_config

    @node_shape_config.setter
    def node_shape_config(self, node_shape_config):
        """
        Sets the node_shape_config of this CreateNodePoolDetails.
        Specify the configuration of the shape to launch nodes in the node pool.


        :param node_shape_config: The node_shape_config of this CreateNodePoolDetails.
        :type: oci.container_engine.models.CreateNodeShapeConfigDetails
        """
        self._node_shape_config = node_shape_config

    @property
    def initial_node_labels(self):
        """
        Gets the initial_node_labels of this CreateNodePoolDetails.
        A list of key/value pairs to add to nodes after they join the Kubernetes cluster.


        :return: The initial_node_labels of this CreateNodePoolDetails.
        :rtype: list[oci.container_engine.models.KeyValue]
        """
        return self._initial_node_labels

    @initial_node_labels.setter
    def initial_node_labels(self, initial_node_labels):
        """
        Sets the initial_node_labels of this CreateNodePoolDetails.
        A list of key/value pairs to add to nodes after they join the Kubernetes cluster.


        :param initial_node_labels: The initial_node_labels of this CreateNodePoolDetails.
        :type: list[oci.container_engine.models.KeyValue]
        """
        self._initial_node_labels = initial_node_labels

    @property
    def ssh_public_key(self):
        """
        Gets the ssh_public_key of this CreateNodePoolDetails.
        The SSH public key on each node in the node pool on launch.


        :return: The ssh_public_key of this CreateNodePoolDetails.
        :rtype: str
        """
        return self._ssh_public_key

    @ssh_public_key.setter
    def ssh_public_key(self, ssh_public_key):
        """
        Sets the ssh_public_key of this CreateNodePoolDetails.
        The SSH public key on each node in the node pool on launch.


        :param ssh_public_key: The ssh_public_key of this CreateNodePoolDetails.
        :type: str
        """
        self._ssh_public_key = ssh_public_key

    @property
    def quantity_per_subnet(self):
        """
        Gets the quantity_per_subnet of this CreateNodePoolDetails.
        Optional, default to 1. The number of nodes to create in each subnet specified in subnetIds property.
        When used, subnetIds is required. This property is deprecated, use nodeConfigDetails instead.


        :return: The quantity_per_subnet of this CreateNodePoolDetails.
        :rtype: int
        """
        return self._quantity_per_subnet

    @quantity_per_subnet.setter
    def quantity_per_subnet(self, quantity_per_subnet):
        """
        Sets the quantity_per_subnet of this CreateNodePoolDetails.
        Optional, default to 1. The number of nodes to create in each subnet specified in subnetIds property.
        When used, subnetIds is required. This property is deprecated, use nodeConfigDetails instead.


        :param quantity_per_subnet: The quantity_per_subnet of this CreateNodePoolDetails.
        :type: int
        """
        self._quantity_per_subnet = quantity_per_subnet

    @property
    def subnet_ids(self):
        """
        Gets the subnet_ids of this CreateNodePoolDetails.
        The OCIDs of the subnets in which to place nodes for this node pool. When used, quantityPerSubnet
        can be provided. This property is deprecated, use nodeConfigDetails. Exactly one of the
        subnetIds or nodeConfigDetails properties must be specified.


        :return: The subnet_ids of this CreateNodePoolDetails.
        :rtype: list[str]
        """
        return self._subnet_ids

    @subnet_ids.setter
    def subnet_ids(self, subnet_ids):
        """
        Sets the subnet_ids of this CreateNodePoolDetails.
        The OCIDs of the subnets in which to place nodes for this node pool. When used, quantityPerSubnet
        can be provided. This property is deprecated, use nodeConfigDetails. Exactly one of the
        subnetIds or nodeConfigDetails properties must be specified.


        :param subnet_ids: The subnet_ids of this CreateNodePoolDetails.
        :type: list[str]
        """
        self._subnet_ids = subnet_ids

    @property
    def node_config_details(self):
        """
        Gets the node_config_details of this CreateNodePoolDetails.
        The configuration of nodes in the node pool. Exactly one of the
        subnetIds or nodeConfigDetails properties must be specified.


        :return: The node_config_details of this CreateNodePoolDetails.
        :rtype: oci.container_engine.models.CreateNodePoolNodeConfigDetails
        """
        return self._node_config_details

    @node_config_details.setter
    def node_config_details(self, node_config_details):
        """
        Sets the node_config_details of this CreateNodePoolDetails.
        The configuration of nodes in the node pool. Exactly one of the
        subnetIds or nodeConfigDetails properties must be specified.


        :param node_config_details: The node_config_details of this CreateNodePoolDetails.
        :type: oci.container_engine.models.CreateNodePoolNodeConfigDetails
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
