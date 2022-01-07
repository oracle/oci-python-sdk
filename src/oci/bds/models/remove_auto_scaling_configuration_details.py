# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemoveAutoScalingConfigurationDetails(object):
    """
    The information about the removed autoscale configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RemoveAutoScalingConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this RemoveAutoScalingConfigurationDetails.
        :type cluster_admin_password: str

        """
        self.swagger_types = {
            'cluster_admin_password': 'str'
        }

        self.attribute_map = {
            'cluster_admin_password': 'clusterAdminPassword'
        }

        self._cluster_admin_password = None

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this RemoveAutoScalingConfigurationDetails.
        Base-64 encoded password for the cluster (and Cloudera Manager) admin user.


        :return: The cluster_admin_password of this RemoveAutoScalingConfigurationDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this RemoveAutoScalingConfigurationDetails.
        Base-64 encoded password for the cluster (and Cloudera Manager) admin user.


        :param cluster_admin_password: The cluster_admin_password of this RemoveAutoScalingConfigurationDetails.
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
