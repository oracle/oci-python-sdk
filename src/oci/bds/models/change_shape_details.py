# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ChangeShapeDetails(object):
    """
    Resize details specified for individual nodes.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ChangeShapeDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this ChangeShapeDetails.
        :type cluster_admin_password: str

        :param nodes:
            The value to assign to the nodes property of this ChangeShapeDetails.
        :type nodes: oci.bds.models.ChangeShapeNodes

        """
        self.swagger_types = {
            'cluster_admin_password': 'str',
            'nodes': 'ChangeShapeNodes'
        }

        self.attribute_map = {
            'cluster_admin_password': 'clusterAdminPassword',
            'nodes': 'nodes'
        }

        self._cluster_admin_password = None
        self._nodes = None

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this ChangeShapeDetails.
        Base-64 encoded password for Cloudera Manager admin user


        :return: The cluster_admin_password of this ChangeShapeDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this ChangeShapeDetails.
        Base-64 encoded password for Cloudera Manager admin user


        :param cluster_admin_password: The cluster_admin_password of this ChangeShapeDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def nodes(self):
        """
        **[Required]** Gets the nodes of this ChangeShapeDetails.

        :return: The nodes of this ChangeShapeDetails.
        :rtype: oci.bds.models.ChangeShapeNodes
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this ChangeShapeDetails.

        :param nodes: The nodes of this ChangeShapeDetails.
        :type: oci.bds.models.ChangeShapeNodes
        """
        self._nodes = nodes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
