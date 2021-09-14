# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .launch_instance_platform_config import LaunchInstancePlatformConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AmdMilanBmLaunchInstancePlatformConfig(LaunchInstancePlatformConfig):
    """
    The platform configuration used when launching a bare metal instance with an E4 shape
    (the AMD Milan platform).
    """

    #: A constant which can be used with the numa_nodes_per_socket property of a AmdMilanBmLaunchInstancePlatformConfig.
    #: This constant has a value of "NPS0"
    NUMA_NODES_PER_SOCKET_NPS0 = "NPS0"

    #: A constant which can be used with the numa_nodes_per_socket property of a AmdMilanBmLaunchInstancePlatformConfig.
    #: This constant has a value of "NPS1"
    NUMA_NODES_PER_SOCKET_NPS1 = "NPS1"

    #: A constant which can be used with the numa_nodes_per_socket property of a AmdMilanBmLaunchInstancePlatformConfig.
    #: This constant has a value of "NPS2"
    NUMA_NODES_PER_SOCKET_NPS2 = "NPS2"

    #: A constant which can be used with the numa_nodes_per_socket property of a AmdMilanBmLaunchInstancePlatformConfig.
    #: This constant has a value of "NPS4"
    NUMA_NODES_PER_SOCKET_NPS4 = "NPS4"

    def __init__(self, **kwargs):
        """
        Initializes a new AmdMilanBmLaunchInstancePlatformConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.AmdMilanBmLaunchInstancePlatformConfig.type` attribute
        of this class is ``AMD_MILAN_BM`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AmdMilanBmLaunchInstancePlatformConfig.
            Allowed values for this property are: "AMD_MILAN_BM", "AMD_ROME_BM", "INTEL_SKYLAKE_BM", "AMD_VM", "INTEL_VM"
        :type type: str

        :param is_secure_boot_enabled:
            The value to assign to the is_secure_boot_enabled property of this AmdMilanBmLaunchInstancePlatformConfig.
        :type is_secure_boot_enabled: bool

        :param is_trusted_platform_module_enabled:
            The value to assign to the is_trusted_platform_module_enabled property of this AmdMilanBmLaunchInstancePlatformConfig.
        :type is_trusted_platform_module_enabled: bool

        :param is_measured_boot_enabled:
            The value to assign to the is_measured_boot_enabled property of this AmdMilanBmLaunchInstancePlatformConfig.
        :type is_measured_boot_enabled: bool

        :param numa_nodes_per_socket:
            The value to assign to the numa_nodes_per_socket property of this AmdMilanBmLaunchInstancePlatformConfig.
            Allowed values for this property are: "NPS0", "NPS1", "NPS2", "NPS4"
        :type numa_nodes_per_socket: str

        """
        self.swagger_types = {
            'type': 'str',
            'is_secure_boot_enabled': 'bool',
            'is_trusted_platform_module_enabled': 'bool',
            'is_measured_boot_enabled': 'bool',
            'numa_nodes_per_socket': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'is_secure_boot_enabled': 'isSecureBootEnabled',
            'is_trusted_platform_module_enabled': 'isTrustedPlatformModuleEnabled',
            'is_measured_boot_enabled': 'isMeasuredBootEnabled',
            'numa_nodes_per_socket': 'numaNodesPerSocket'
        }

        self._type = None
        self._is_secure_boot_enabled = None
        self._is_trusted_platform_module_enabled = None
        self._is_measured_boot_enabled = None
        self._numa_nodes_per_socket = None
        self._type = 'AMD_MILAN_BM'

    @property
    def numa_nodes_per_socket(self):
        """
        Gets the numa_nodes_per_socket of this AmdMilanBmLaunchInstancePlatformConfig.
        The number of NUMA nodes per socket (NPS).

        Allowed values for this property are: "NPS0", "NPS1", "NPS2", "NPS4"


        :return: The numa_nodes_per_socket of this AmdMilanBmLaunchInstancePlatformConfig.
        :rtype: str
        """
        return self._numa_nodes_per_socket

    @numa_nodes_per_socket.setter
    def numa_nodes_per_socket(self, numa_nodes_per_socket):
        """
        Sets the numa_nodes_per_socket of this AmdMilanBmLaunchInstancePlatformConfig.
        The number of NUMA nodes per socket (NPS).


        :param numa_nodes_per_socket: The numa_nodes_per_socket of this AmdMilanBmLaunchInstancePlatformConfig.
        :type: str
        """
        allowed_values = ["NPS0", "NPS1", "NPS2", "NPS4"]
        if not value_allowed_none_or_none_sentinel(numa_nodes_per_socket, allowed_values):
            raise ValueError(
                "Invalid value for `numa_nodes_per_socket`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._numa_nodes_per_socket = numa_nodes_per_socket

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
