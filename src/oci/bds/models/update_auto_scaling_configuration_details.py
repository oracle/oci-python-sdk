# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAutoScalingConfigurationDetails(object):
    """
    The information about the autoscale configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAutoScalingConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateAutoScalingConfigurationDetails.
        :type display_name: str

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateAutoScalingConfigurationDetails.
        :type is_enabled: bool

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this UpdateAutoScalingConfigurationDetails.
        :type cluster_admin_password: str

        :param policy:
            The value to assign to the policy property of this UpdateAutoScalingConfigurationDetails.
        :type policy: oci.bds.models.AutoScalePolicy

        """
        self.swagger_types = {
            'display_name': 'str',
            'is_enabled': 'bool',
            'cluster_admin_password': 'str',
            'policy': 'AutoScalePolicy'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'is_enabled': 'isEnabled',
            'cluster_admin_password': 'clusterAdminPassword',
            'policy': 'policy'
        }

        self._display_name = None
        self._is_enabled = None
        self._cluster_admin_password = None
        self._policy = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAutoScalingConfigurationDetails.
        A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.


        :return: The display_name of this UpdateAutoScalingConfigurationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAutoScalingConfigurationDetails.
        A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateAutoScalingConfigurationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdateAutoScalingConfigurationDetails.
        Whether the autoscale configuration is enabled.


        :return: The is_enabled of this UpdateAutoScalingConfigurationDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateAutoScalingConfigurationDetails.
        Whether the autoscale configuration is enabled.


        :param is_enabled: The is_enabled of this UpdateAutoScalingConfigurationDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def cluster_admin_password(self):
        """
        Gets the cluster_admin_password of this UpdateAutoScalingConfigurationDetails.
        Base-64 encoded password for the cluster (and Cloudera Manager) admin user.


        :return: The cluster_admin_password of this UpdateAutoScalingConfigurationDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this UpdateAutoScalingConfigurationDetails.
        Base-64 encoded password for the cluster (and Cloudera Manager) admin user.


        :param cluster_admin_password: The cluster_admin_password of this UpdateAutoScalingConfigurationDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def policy(self):
        """
        Gets the policy of this UpdateAutoScalingConfigurationDetails.

        :return: The policy of this UpdateAutoScalingConfigurationDetails.
        :rtype: oci.bds.models.AutoScalePolicy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this UpdateAutoScalingConfigurationDetails.

        :param policy: The policy of this UpdateAutoScalingConfigurationDetails.
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
