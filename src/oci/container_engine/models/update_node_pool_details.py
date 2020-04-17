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

        """
        self.swagger_types = {
            'name': 'str',
            'kubernetes_version': 'str',
            'initial_node_labels': 'list[KeyValue]',
            'quantity_per_subnet': 'int',
            'subnet_ids': 'list[str]',
            'node_config_details': 'UpdateNodePoolNodeConfigDetails'
        }

        self.attribute_map = {
            'name': 'name',
            'kubernetes_version': 'kubernetesVersion',
            'initial_node_labels': 'initialNodeLabels',
            'quantity_per_subnet': 'quantityPerSubnet',
            'subnet_ids': 'subnetIds',
            'node_config_details': 'nodeConfigDetails'
        }

        self._name = None
        self._kubernetes_version = None
        self._initial_node_labels = None
        self._quantity_per_subnet = None
        self._subnet_ids = None
        self._node_config_details = None

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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
