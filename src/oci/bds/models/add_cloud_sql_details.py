# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddCloudSqlDetails(object):
    """
    The information about the added Cloud SQL.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddCloudSqlDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shape:
            The value to assign to the shape property of this AddCloudSqlDetails.
        :type shape: str

        :param block_volume_size_in_gbs:
            The value to assign to the block_volume_size_in_gbs property of this AddCloudSqlDetails.
        :type block_volume_size_in_gbs: int

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this AddCloudSqlDetails.
        :type cluster_admin_password: str

        """
        self.swagger_types = {
            'shape': 'str',
            'block_volume_size_in_gbs': 'int',
            'cluster_admin_password': 'str'
        }

        self.attribute_map = {
            'shape': 'shape',
            'block_volume_size_in_gbs': 'blockVolumeSizeInGBs',
            'cluster_admin_password': 'clusterAdminPassword'
        }

        self._shape = None
        self._block_volume_size_in_gbs = None
        self._cluster_admin_password = None

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this AddCloudSqlDetails.
        Shape of the node.


        :return: The shape of this AddCloudSqlDetails.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this AddCloudSqlDetails.
        Shape of the node.


        :param shape: The shape of this AddCloudSqlDetails.
        :type: str
        """
        self._shape = shape

    @property
    def block_volume_size_in_gbs(self):
        """
        Gets the block_volume_size_in_gbs of this AddCloudSqlDetails.
        The size of block volume in GB to be attached to the given node. All details needed for attaching the block volume are managed by the service itself.


        :return: The block_volume_size_in_gbs of this AddCloudSqlDetails.
        :rtype: int
        """
        return self._block_volume_size_in_gbs

    @block_volume_size_in_gbs.setter
    def block_volume_size_in_gbs(self, block_volume_size_in_gbs):
        """
        Sets the block_volume_size_in_gbs of this AddCloudSqlDetails.
        The size of block volume in GB to be attached to the given node. All details needed for attaching the block volume are managed by the service itself.


        :param block_volume_size_in_gbs: The block_volume_size_in_gbs of this AddCloudSqlDetails.
        :type: int
        """
        self._block_volume_size_in_gbs = block_volume_size_in_gbs

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this AddCloudSqlDetails.
        Base-64 encoded password for the cluster (and Cloudera Manager) admin user.


        :return: The cluster_admin_password of this AddCloudSqlDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this AddCloudSqlDetails.
        Base-64 encoded password for the cluster (and Cloudera Manager) admin user.


        :param cluster_admin_password: The cluster_admin_password of this AddCloudSqlDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
