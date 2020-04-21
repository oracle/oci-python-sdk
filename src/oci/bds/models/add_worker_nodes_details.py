# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddWorkerNodesDetails(object):
    """
    The information about additionaly added nodes
    """

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

        """
        self.swagger_types = {
            'cluster_admin_password': 'str',
            'number_of_worker_nodes': 'int'
        }

        self.attribute_map = {
            'cluster_admin_password': 'clusterAdminPassword',
            'number_of_worker_nodes': 'numberOfWorkerNodes'
        }

        self._cluster_admin_password = None
        self._number_of_worker_nodes = None

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this AddWorkerNodesDetails.
        Base-64 encoded password for Cloudera Manager admin user


        :return: The cluster_admin_password of this AddWorkerNodesDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this AddWorkerNodesDetails.
        Base-64 encoded password for Cloudera Manager admin user


        :param cluster_admin_password: The cluster_admin_password of this AddWorkerNodesDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def number_of_worker_nodes(self):
        """
        **[Required]** Gets the number_of_worker_nodes of this AddWorkerNodesDetails.
        Number of additional worker nodes for the BDS instance


        :return: The number_of_worker_nodes of this AddWorkerNodesDetails.
        :rtype: int
        """
        return self._number_of_worker_nodes

    @number_of_worker_nodes.setter
    def number_of_worker_nodes(self, number_of_worker_nodes):
        """
        Sets the number_of_worker_nodes of this AddWorkerNodesDetails.
        Number of additional worker nodes for the BDS instance


        :param number_of_worker_nodes: The number_of_worker_nodes of this AddWorkerNodesDetails.
        :type: int
        """
        self._number_of_worker_nodes = number_of_worker_nodes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
