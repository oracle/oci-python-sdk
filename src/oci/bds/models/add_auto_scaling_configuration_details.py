# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AddAutoScalingConfigurationDetails(object):
    """
    The information about auto scale configuration capability
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AddAutoScalingConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this AddAutoScalingConfigurationDetails.
        :type display_name: str

        :param node_type:
            The value to assign to the node_type property of this AddAutoScalingConfigurationDetails.
        :type node_type: str

        :param is_enabled:
            The value to assign to the is_enabled property of this AddAutoScalingConfigurationDetails.
        :type is_enabled: bool

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this AddAutoScalingConfigurationDetails.
        :type cluster_admin_password: str

        :param policy:
            The value to assign to the policy property of this AddAutoScalingConfigurationDetails.
        :type policy: oci.bds.models.AutoScalePolicy

        """
        self.swagger_types = {
            'display_name': 'str',
            'node_type': 'str',
            'is_enabled': 'bool',
            'cluster_admin_password': 'str',
            'policy': 'AutoScalePolicy'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'node_type': 'nodeType',
            'is_enabled': 'isEnabled',
            'cluster_admin_password': 'clusterAdminPassword',
            'policy': 'policy'
        }

        self._display_name = None
        self._node_type = None
        self._is_enabled = None
        self._cluster_admin_password = None
        self._policy = None

    @property
    def display_name(self):
        """
        Gets the display_name of this AddAutoScalingConfigurationDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this AddAutoScalingConfigurationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AddAutoScalingConfigurationDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this AddAutoScalingConfigurationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def node_type(self):
        """
        **[Required]** Gets the node_type of this AddAutoScalingConfigurationDetails.
        A node type that is managed by an autoscaling configuration. The only supported type is WORKER.


        :return: The node_type of this AddAutoScalingConfigurationDetails.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """
        Sets the node_type of this AddAutoScalingConfigurationDetails.
        A node type that is managed by an autoscaling configuration. The only supported type is WORKER.


        :param node_type: The node_type of this AddAutoScalingConfigurationDetails.
        :type: str
        """
        self._node_type = node_type

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this AddAutoScalingConfigurationDetails.
        Whether the autoscaling configuration is enabled.


        :return: The is_enabled of this AddAutoScalingConfigurationDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this AddAutoScalingConfigurationDetails.
        Whether the autoscaling configuration is enabled.


        :param is_enabled: The is_enabled of this AddAutoScalingConfigurationDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this AddAutoScalingConfigurationDetails.
        Base-64 encoded password for Cloudera Manager admin user


        :return: The cluster_admin_password of this AddAutoScalingConfigurationDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this AddAutoScalingConfigurationDetails.
        Base-64 encoded password for Cloudera Manager admin user


        :param cluster_admin_password: The cluster_admin_password of this AddAutoScalingConfigurationDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def policy(self):
        """
        **[Required]** Gets the policy of this AddAutoScalingConfigurationDetails.

        :return: The policy of this AddAutoScalingConfigurationDetails.
        :rtype: oci.bds.models.AutoScalePolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this AddAutoScalingConfigurationDetails.

        :param policy: The policy of this AddAutoScalingConfigurationDetails.
        :type: oci.bds.models.AutoScalePolicy
        """
        self._policy = policy

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
