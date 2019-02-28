# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


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

        """
        self.swagger_types = {
            'is_monitoring_supported': 'bool'
        }

        self.attribute_map = {
            'is_monitoring_supported': 'isMonitoringSupported'
        }

        self._is_monitoring_supported = None

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

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
