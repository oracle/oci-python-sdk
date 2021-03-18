# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .instance_configuration_launch_instance_platform_config import InstanceConfigurationLaunchInstancePlatformConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationAmdMilanBmLaunchInstancePlatformConfig(InstanceConfigurationLaunchInstancePlatformConfig):
    """
    The platform configuration used when launching a bare metal instance with an E4 shape
    (the AMD Milan platform).
    """

    #: A constant which can be used with the numa_nodes_per_socket property of a InstanceConfigurationAmdMilanBmLaunchInstancePlatformConfig.
    #: This constant has a value of "NPS0"
    NUMA_NODES_PER_SOCKET_NPS0 = "NPS0"

    #: A constant which can be used with the numa_nodes_per_socket property of a InstanceConfigurationAmdMilanBmLaunchInstancePlatformConfig.
    #: This constant has a value of "NPS1"
    NUMA_NODES_PER_SOCKET_NPS1 = "NPS1"

    #: A constant which can be used with the numa_nodes_per_socket property of a InstanceConfigurationAmdMilanBmLaunchInstancePlatformConfig.
    #: This constant has a value of "NPS2"
    NUMA_NODES_PER_SOCKET_NPS2 = "NPS2"

    #: A constant which can be used with the numa_nodes_per_socket property of a InstanceConfigurationAmdMilanBmLaunchInstancePlatformConfig.
    #: This constant has a value of "NPS4"
    NUMA_NODES_PER_SOCKET_NPS4 = "NPS4"

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationAmdMilanBmLaunchInstancePlatformConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.InstanceConfigurationAmdMilanBmLaunchInstancePlatformConfig.type` attribute
        of this class is ``AMD_MILAN_BM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this InstanceConfigurationAmdMilanBmLaunchInstancePlatformConfig.
            Allowed values for this property are: "AMD_MILAN_BM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param numa_nodes_per_socket:
            The value to assign to the numa_nodes_per_socket property of this InstanceConfigurationAmdMilanBmLaunchInstancePlatformConfig.
            Allowed values for this property are: "NPS0", "NPS1", "NPS2", "NPS4", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type numa_nodes_per_socket: str

        """
        self.swagger_types = {
            'type': 'str',
            'numa_nodes_per_socket': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'numa_nodes_per_socket': 'numaNodesPerSocket'
        }

        self._type = None
        self._numa_nodes_per_socket = None
        self._type = 'AMD_MILAN_BM'

    @property
    def numa_nodes_per_socket(self):
        """
        Gets the numa_nodes_per_socket of this InstanceConfigurationAmdMilanBmLaunchInstancePlatformConfig.
        The number of NUMA nodes per socket.

        Allowed values for this property are: "NPS0", "NPS1", "NPS2", "NPS4", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The numa_nodes_per_socket of this InstanceConfigurationAmdMilanBmLaunchInstancePlatformConfig.
        :rtype: str
        """
        return self._numa_nodes_per_socket

    @numa_nodes_per_socket.setter
    def numa_nodes_per_socket(self, numa_nodes_per_socket):
        """
        Sets the numa_nodes_per_socket of this InstanceConfigurationAmdMilanBmLaunchInstancePlatformConfig.
        The number of NUMA nodes per socket.


        :param numa_nodes_per_socket: The numa_nodes_per_socket of this InstanceConfigurationAmdMilanBmLaunchInstancePlatformConfig.
        :type: str
        """
        allowed_values = ["NPS0", "NPS1", "NPS2", "NPS4"]
        if not value_allowed_none_or_none_sentinel(numa_nodes_per_socket, allowed_values):
            numa_nodes_per_socket = 'UNKNOWN_ENUM_VALUE'
        self._numa_nodes_per_socket = numa_nodes_per_socket

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
