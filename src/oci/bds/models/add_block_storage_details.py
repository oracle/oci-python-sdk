# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddBlockStorageDetails(object):
    """
    The information about additionally added block volumes
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddBlockStorageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this AddBlockStorageDetails.
        :type cluster_admin_password: str

        :param block_volume_size_in_gbs:
            The value to assign to the block_volume_size_in_gbs property of this AddBlockStorageDetails.
        :type block_volume_size_in_gbs: int

        """
        self.swagger_types = {
            'cluster_admin_password': 'str',
            'block_volume_size_in_gbs': 'int'
        }

        self.attribute_map = {
            'cluster_admin_password': 'clusterAdminPassword',
            'block_volume_size_in_gbs': 'blockVolumeSizeInGBs'
        }

        self._cluster_admin_password = None
        self._block_volume_size_in_gbs = None

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this AddBlockStorageDetails.
        Base-64 encoded password for Cloudera Manager admin user


        :return: The cluster_admin_password of this AddBlockStorageDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this AddBlockStorageDetails.
        Base-64 encoded password for Cloudera Manager admin user


        :param cluster_admin_password: The cluster_admin_password of this AddBlockStorageDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def block_volume_size_in_gbs(self):
        """
        **[Required]** Gets the block_volume_size_in_gbs of this AddBlockStorageDetails.
        The size of block volume in GB that needs to be added to each worker node.
        All the necessary details needed for attachment are managed by service itself.


        :return: The block_volume_size_in_gbs of this AddBlockStorageDetails.
        :rtype: int
        """
        return self._block_volume_size_in_gbs

    @block_volume_size_in_gbs.setter
    def block_volume_size_in_gbs(self, block_volume_size_in_gbs):
        """
        Sets the block_volume_size_in_gbs of this AddBlockStorageDetails.
        The size of block volume in GB that needs to be added to each worker node.
        All the necessary details needed for attachment are managed by service itself.


        :param block_volume_size_in_gbs: The block_volume_size_in_gbs of this AddBlockStorageDetails.
        :type: int
        """
        self._block_volume_size_in_gbs = block_volume_size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
