# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateInstanceAgentConfigDetails(object):
    """
    Instance agent configuration options to choose for updating the instance
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateInstanceAgentConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_monitoring_disabled:
            The value to assign to the is_monitoring_disabled property of this UpdateInstanceAgentConfigDetails.
        :type is_monitoring_disabled: bool

        """
        self.swagger_types = {
            'is_monitoring_disabled': 'bool'
        }

        self.attribute_map = {
            'is_monitoring_disabled': 'isMonitoringDisabled'
        }

        self._is_monitoring_disabled = None

    @property
    def is_monitoring_disabled(self):
        """
        Gets the is_monitoring_disabled of this UpdateInstanceAgentConfigDetails.
        Whether the agent running on the instance can gather performance metrics and monitor the instance.


        :return: The is_monitoring_disabled of this UpdateInstanceAgentConfigDetails.
        :rtype: bool
        """
        return self._is_monitoring_disabled

    @is_monitoring_disabled.setter
    def is_monitoring_disabled(self, is_monitoring_disabled):
        """
        Sets the is_monitoring_disabled of this UpdateInstanceAgentConfigDetails.
        Whether the agent running on the instance can gather performance metrics and monitor the instance.


        :param is_monitoring_disabled: The is_monitoring_disabled of this UpdateInstanceAgentConfigDetails.
        :type: bool
        """
        self._is_monitoring_disabled = is_monitoring_disabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
