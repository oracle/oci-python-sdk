# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .host_configuration_metric_group import HostConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostHardwareConfiguration(HostConfigurationMetricGroup):
    """
    Hardware Configuration metric for the host
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HostHardwareConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostHardwareConfiguration.metric_name` attribute
        of this class is ``HOST_HARDWARE_CONFIGURATION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this HostHardwareConfiguration.
            Allowed values for this property are: "HOST_PRODUCT", "HOST_RESOURCE_ALLOCATION", "HOST_MEMORY_CONFIGURATION", "HOST_HARDWARE_CONFIGURATION", "HOST_CPU_HARDWARE_CONFIGURATION", "HOST_NETWORK_CONFIGURATION", "HOST_ENTITES"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this HostHardwareConfiguration.
        :type time_collected: datetime

        :param cpu_architecture:
            The value to assign to the cpu_architecture property of this HostHardwareConfiguration.
        :type cpu_architecture: str

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'cpu_architecture': 'str'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'cpu_architecture': 'cpuArchitecture'
        }

        self._metric_name = None
        self._time_collected = None
        self._cpu_architecture = None
        self._metric_name = 'HOST_HARDWARE_CONFIGURATION'

    @property
    def cpu_architecture(self):
        """
        **[Required]** Gets the cpu_architecture of this HostHardwareConfiguration.
        Processor architecture used by the platform


        :return: The cpu_architecture of this HostHardwareConfiguration.
        :rtype: str
        """
        return self._cpu_architecture

    @cpu_architecture.setter
    def cpu_architecture(self, cpu_architecture):
        """
        Sets the cpu_architecture of this HostHardwareConfiguration.
        Processor architecture used by the platform


        :param cpu_architecture: The cpu_architecture of this HostHardwareConfiguration.
        :type: str
        """
        self._cpu_architecture = cpu_architecture

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
