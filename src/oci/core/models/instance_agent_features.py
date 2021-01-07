# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceAgentFeatures(object):
    """
    Instance agent features supported on the image
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceAgentFeatures object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_monitoring_supported:
            The value to assign to the is_monitoring_supported property of this InstanceAgentFeatures.
        :type is_monitoring_supported: bool

        :param is_management_supported:
            The value to assign to the is_management_supported property of this InstanceAgentFeatures.
        :type is_management_supported: bool

        """
        self.swagger_types = {
            'is_monitoring_supported': 'bool',
            'is_management_supported': 'bool'
        }

        self.attribute_map = {
            'is_monitoring_supported': 'isMonitoringSupported',
            'is_management_supported': 'isManagementSupported'
        }

        self._is_monitoring_supported = None
        self._is_management_supported = None

    @property
    def is_monitoring_supported(self):
        """
        Gets the is_monitoring_supported of this InstanceAgentFeatures.
        Whether the agent running on the instance can gather performance metrics and monitor the instance.


        :return: The is_monitoring_supported of this InstanceAgentFeatures.
        :rtype: bool
        """
        return self._is_monitoring_supported

    @is_monitoring_supported.setter
    def is_monitoring_supported(self, is_monitoring_supported):
        """
        Sets the is_monitoring_supported of this InstanceAgentFeatures.
        Whether the agent running on the instance can gather performance metrics and monitor the instance.


        :param is_monitoring_supported: The is_monitoring_supported of this InstanceAgentFeatures.
        :type: bool
        """
        self._is_monitoring_supported = is_monitoring_supported

    @property
    def is_management_supported(self):
        """
        Gets the is_management_supported of this InstanceAgentFeatures.
        Whether the agent running on the instance can run all the available management plugins


        :return: The is_management_supported of this InstanceAgentFeatures.
        :rtype: bool
        """
        return self._is_management_supported

    @is_management_supported.setter
    def is_management_supported(self, is_management_supported):
        """
        Sets the is_management_supported of this InstanceAgentFeatures.
        Whether the agent running on the instance can run all the available management plugins


        :param is_management_supported: The is_management_supported of this InstanceAgentFeatures.
        :type: bool
        """
        self._is_management_supported = is_management_supported

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
