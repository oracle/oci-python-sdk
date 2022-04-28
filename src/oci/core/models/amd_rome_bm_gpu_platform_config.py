# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .platform_config import PlatformConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AmdRomeBmGpuPlatformConfig(PlatformConfig):
    """
    The platform configuration of a bare metal GPU instance that uses the BM.GPU4.8 shape
    (the AMD Rome platform).
    """

    #: A constant which can be used with the numa_nodes_per_socket property of a AmdRomeBmGpuPlatformConfig.
    #: This constant has a value of "NPS0"
    NUMA_NODES_PER_SOCKET_NPS0 = "NPS0"

    #: A constant which can be used with the numa_nodes_per_socket property of a AmdRomeBmGpuPlatformConfig.
    #: This constant has a value of "NPS1"
    NUMA_NODES_PER_SOCKET_NPS1 = "NPS1"

    #: A constant which can be used with the numa_nodes_per_socket property of a AmdRomeBmGpuPlatformConfig.
    #: This constant has a value of "NPS2"
    NUMA_NODES_PER_SOCKET_NPS2 = "NPS2"

    #: A constant which can be used with the numa_nodes_per_socket property of a AmdRomeBmGpuPlatformConfig.
    #: This constant has a value of "NPS4"
    NUMA_NODES_PER_SOCKET_NPS4 = "NPS4"

    def __init__(self, **kwargs):
        """
        Initializes a new AmdRomeBmGpuPlatformConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.AmdRomeBmGpuPlatformConfig.type` attribute
        of this class is ``AMD_ROME_BM_GPU`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AmdRomeBmGpuPlatformConfig.
            Allowed values for this property are: "AMD_MILAN_BM", "AMD_ROME_BM", "AMD_ROME_BM_GPU", "INTEL_ICELAKE_BM", "INTEL_SKYLAKE_BM", "AMD_VM", "INTEL_VM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param is_secure_boot_enabled:
            The value to assign to the is_secure_boot_enabled property of this AmdRomeBmGpuPlatformConfig.
        :type is_secure_boot_enabled: bool

        :param is_trusted_platform_module_enabled:
            The value to assign to the is_trusted_platform_module_enabled property of this AmdRomeBmGpuPlatformConfig.
        :type is_trusted_platform_module_enabled: bool

        :param is_measured_boot_enabled:
            The value to assign to the is_measured_boot_enabled property of this AmdRomeBmGpuPlatformConfig.
        :type is_measured_boot_enabled: bool

        :param numa_nodes_per_socket:
            The value to assign to the numa_nodes_per_socket property of this AmdRomeBmGpuPlatformConfig.
            Allowed values for this property are: "NPS0", "NPS1", "NPS2", "NPS4", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type numa_nodes_per_socket: str

        :param is_symmetric_multi_threading_enabled:
            The value to assign to the is_symmetric_multi_threading_enabled property of this AmdRomeBmGpuPlatformConfig.
        :type is_symmetric_multi_threading_enabled: bool

        :param is_access_control_service_enabled:
            The value to assign to the is_access_control_service_enabled property of this AmdRomeBmGpuPlatformConfig.
        :type is_access_control_service_enabled: bool

        :param are_virtual_instructions_enabled:
            The value to assign to the are_virtual_instructions_enabled property of this AmdRomeBmGpuPlatformConfig.
        :type are_virtual_instructions_enabled: bool

        :param is_input_output_memory_management_unit_enabled:
            The value to assign to the is_input_output_memory_management_unit_enabled property of this AmdRomeBmGpuPlatformConfig.
        :type is_input_output_memory_management_unit_enabled: bool

        """
        self.swagger_types = {
            'type': 'str',
            'is_secure_boot_enabled': 'bool',
            'is_trusted_platform_module_enabled': 'bool',
            'is_measured_boot_enabled': 'bool',
            'numa_nodes_per_socket': 'str',
            'is_symmetric_multi_threading_enabled': 'bool',
            'is_access_control_service_enabled': 'bool',
            'are_virtual_instructions_enabled': 'bool',
            'is_input_output_memory_management_unit_enabled': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'is_secure_boot_enabled': 'isSecureBootEnabled',
            'is_trusted_platform_module_enabled': 'isTrustedPlatformModuleEnabled',
            'is_measured_boot_enabled': 'isMeasuredBootEnabled',
            'numa_nodes_per_socket': 'numaNodesPerSocket',
            'is_symmetric_multi_threading_enabled': 'isSymmetricMultiThreadingEnabled',
            'is_access_control_service_enabled': 'isAccessControlServiceEnabled',
            'are_virtual_instructions_enabled': 'areVirtualInstructionsEnabled',
            'is_input_output_memory_management_unit_enabled': 'isInputOutputMemoryManagementUnitEnabled'
        }

        self._type = None
        self._is_secure_boot_enabled = None
        self._is_trusted_platform_module_enabled = None
        self._is_measured_boot_enabled = None
        self._numa_nodes_per_socket = None
        self._is_symmetric_multi_threading_enabled = None
        self._is_access_control_service_enabled = None
        self._are_virtual_instructions_enabled = None
        self._is_input_output_memory_management_unit_enabled = None
        self._type = 'AMD_ROME_BM_GPU'

    @property
    def numa_nodes_per_socket(self):
        """
        Gets the numa_nodes_per_socket of this AmdRomeBmGpuPlatformConfig.
        The number of NUMA nodes per socket (NPS).

        Allowed values for this property are: "NPS0", "NPS1", "NPS2", "NPS4", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The numa_nodes_per_socket of this AmdRomeBmGpuPlatformConfig.
        :rtype: str
        """
        return self._numa_nodes_per_socket

    @numa_nodes_per_socket.setter
    def numa_nodes_per_socket(self, numa_nodes_per_socket):
        """
        Sets the numa_nodes_per_socket of this AmdRomeBmGpuPlatformConfig.
        The number of NUMA nodes per socket (NPS).


        :param numa_nodes_per_socket: The numa_nodes_per_socket of this AmdRomeBmGpuPlatformConfig.
        :type: str
        """
        allowed_values = ["NPS0", "NPS1", "NPS2", "NPS4"]
        if not value_allowed_none_or_none_sentinel(numa_nodes_per_socket, allowed_values):
            numa_nodes_per_socket = 'UNKNOWN_ENUM_VALUE'
        self._numa_nodes_per_socket = numa_nodes_per_socket

    @property
    def is_symmetric_multi_threading_enabled(self):
        """
        Gets the is_symmetric_multi_threading_enabled of this AmdRomeBmGpuPlatformConfig.
        Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also
        called simultaneous multithreading (SMT) or Intel Hyper-Threading.

        Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple
        independent threads of execution, to better use the resources and increase the efficiency
        of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which
        can provide higher or more predictable performance for some workloads.


        :return: The is_symmetric_multi_threading_enabled of this AmdRomeBmGpuPlatformConfig.
        :rtype: bool
        """
        return self._is_symmetric_multi_threading_enabled

    @is_symmetric_multi_threading_enabled.setter
    def is_symmetric_multi_threading_enabled(self, is_symmetric_multi_threading_enabled):
        """
        Sets the is_symmetric_multi_threading_enabled of this AmdRomeBmGpuPlatformConfig.
        Whether symmetric multithreading is enabled on the instance. Symmetric multithreading is also
        called simultaneous multithreading (SMT) or Intel Hyper-Threading.

        Intel and AMD processors have two hardware execution threads per core (OCPU). SMT permits multiple
        independent threads of execution, to better use the resources and increase the efficiency
        of the CPU. When multithreading is disabled, only one thread is permitted to run on each core, which
        can provide higher or more predictable performance for some workloads.


        :param is_symmetric_multi_threading_enabled: The is_symmetric_multi_threading_enabled of this AmdRomeBmGpuPlatformConfig.
        :type: bool
        """
        self._is_symmetric_multi_threading_enabled = is_symmetric_multi_threading_enabled

    @property
    def is_access_control_service_enabled(self):
        """
        Gets the is_access_control_service_enabled of this AmdRomeBmGpuPlatformConfig.
        Whether the Access Control Service is enabled on the instance. When enabled,
        the platform can enforce PCIe device isolation, required for VFIO device pass-through.


        :return: The is_access_control_service_enabled of this AmdRomeBmGpuPlatformConfig.
        :rtype: bool
        """
        return self._is_access_control_service_enabled

    @is_access_control_service_enabled.setter
    def is_access_control_service_enabled(self, is_access_control_service_enabled):
        """
        Sets the is_access_control_service_enabled of this AmdRomeBmGpuPlatformConfig.
        Whether the Access Control Service is enabled on the instance. When enabled,
        the platform can enforce PCIe device isolation, required for VFIO device pass-through.


        :param is_access_control_service_enabled: The is_access_control_service_enabled of this AmdRomeBmGpuPlatformConfig.
        :type: bool
        """
        self._is_access_control_service_enabled = is_access_control_service_enabled

    @property
    def are_virtual_instructions_enabled(self):
        """
        Gets the are_virtual_instructions_enabled of this AmdRomeBmGpuPlatformConfig.
        Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes
        or VT-x for Intel shapes.


        :return: The are_virtual_instructions_enabled of this AmdRomeBmGpuPlatformConfig.
        :rtype: bool
        """
        return self._are_virtual_instructions_enabled

    @are_virtual_instructions_enabled.setter
    def are_virtual_instructions_enabled(self, are_virtual_instructions_enabled):
        """
        Sets the are_virtual_instructions_enabled of this AmdRomeBmGpuPlatformConfig.
        Whether virtualization instructions are available. For example, Secure Virtual Machine for AMD shapes
        or VT-x for Intel shapes.


        :param are_virtual_instructions_enabled: The are_virtual_instructions_enabled of this AmdRomeBmGpuPlatformConfig.
        :type: bool
        """
        self._are_virtual_instructions_enabled = are_virtual_instructions_enabled

    @property
    def is_input_output_memory_management_unit_enabled(self):
        """
        Gets the is_input_output_memory_management_unit_enabled of this AmdRomeBmGpuPlatformConfig.
        Whether the input-output memory management unit is enabled.


        :return: The is_input_output_memory_management_unit_enabled of this AmdRomeBmGpuPlatformConfig.
        :rtype: bool
        """
        return self._is_input_output_memory_management_unit_enabled

    @is_input_output_memory_management_unit_enabled.setter
    def is_input_output_memory_management_unit_enabled(self, is_input_output_memory_management_unit_enabled):
        """
        Sets the is_input_output_memory_management_unit_enabled of this AmdRomeBmGpuPlatformConfig.
        Whether the input-output memory management unit is enabled.


        :param is_input_output_memory_management_unit_enabled: The is_input_output_memory_management_unit_enabled of this AmdRomeBmGpuPlatformConfig.
        :type: bool
        """
        self._is_input_output_memory_management_unit_enabled = is_input_output_memory_management_unit_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
