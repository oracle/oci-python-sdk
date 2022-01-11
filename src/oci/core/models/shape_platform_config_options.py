# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ShapePlatformConfigOptions(object):
    """
    The list of supported platform configuration options for this shape.
    """

    #: A constant which can be used with the type property of a ShapePlatformConfigOptions.
    #: This constant has a value of "AMD_MILAN_BM"
    TYPE_AMD_MILAN_BM = "AMD_MILAN_BM"

    #: A constant which can be used with the type property of a ShapePlatformConfigOptions.
    #: This constant has a value of "AMD_ROME_BM"
    TYPE_AMD_ROME_BM = "AMD_ROME_BM"

    #: A constant which can be used with the type property of a ShapePlatformConfigOptions.
    #: This constant has a value of "INTEL_SKYLAKE_BM"
    TYPE_INTEL_SKYLAKE_BM = "INTEL_SKYLAKE_BM"

    #: A constant which can be used with the type property of a ShapePlatformConfigOptions.
    #: This constant has a value of "AMD_VM"
    TYPE_AMD_VM = "AMD_VM"

    #: A constant which can be used with the type property of a ShapePlatformConfigOptions.
    #: This constant has a value of "INTEL_VM"
    TYPE_INTEL_VM = "INTEL_VM"

    def __init__(self, **kwargs):
        """
        Initializes a new ShapePlatformConfigOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ShapePlatformConfigOptions.
            Allowed values for this property are: "AMD_MILAN_BM", "AMD_ROME_BM", "INTEL_SKYLAKE_BM", "AMD_VM", "INTEL_VM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param secure_boot_options:
            The value to assign to the secure_boot_options property of this ShapePlatformConfigOptions.
        :type secure_boot_options: oci.core.models.ShapeSecureBootOptions

        :param measured_boot_options:
            The value to assign to the measured_boot_options property of this ShapePlatformConfigOptions.
        :type measured_boot_options: oci.core.models.ShapeMeasuredBootOptions

        :param trusted_platform_module_options:
            The value to assign to the trusted_platform_module_options property of this ShapePlatformConfigOptions.
        :type trusted_platform_module_options: oci.core.models.ShapeTrustedPlatformModuleOptions

        :param numa_nodes_per_socket_platform_options:
            The value to assign to the numa_nodes_per_socket_platform_options property of this ShapePlatformConfigOptions.
        :type numa_nodes_per_socket_platform_options: oci.core.models.ShapeNumaNodesPerSocketPlatformOptions

        """
        self.swagger_types = {
            'type': 'str',
            'secure_boot_options': 'ShapeSecureBootOptions',
            'measured_boot_options': 'ShapeMeasuredBootOptions',
            'trusted_platform_module_options': 'ShapeTrustedPlatformModuleOptions',
            'numa_nodes_per_socket_platform_options': 'ShapeNumaNodesPerSocketPlatformOptions'
        }

        self.attribute_map = {
            'type': 'type',
            'secure_boot_options': 'secureBootOptions',
            'measured_boot_options': 'measuredBootOptions',
            'trusted_platform_module_options': 'trustedPlatformModuleOptions',
            'numa_nodes_per_socket_platform_options': 'numaNodesPerSocketPlatformOptions'
        }

        self._type = None
        self._secure_boot_options = None
        self._measured_boot_options = None
        self._trusted_platform_module_options = None
        self._numa_nodes_per_socket_platform_options = None

    @property
    def type(self):
        """
        Gets the type of this ShapePlatformConfigOptions.
        The type of platform being configured.

        Allowed values for this property are: "AMD_MILAN_BM", "AMD_ROME_BM", "INTEL_SKYLAKE_BM", "AMD_VM", "INTEL_VM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ShapePlatformConfigOptions.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ShapePlatformConfigOptions.
        The type of platform being configured.


        :param type: The type of this ShapePlatformConfigOptions.
        :type: str
        """
        allowed_values = ["AMD_MILAN_BM", "AMD_ROME_BM", "INTEL_SKYLAKE_BM", "AMD_VM", "INTEL_VM"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def secure_boot_options(self):
        """
        Gets the secure_boot_options of this ShapePlatformConfigOptions.

        :return: The secure_boot_options of this ShapePlatformConfigOptions.
        :rtype: oci.core.models.ShapeSecureBootOptions
        """
        return self._secure_boot_options

    @secure_boot_options.setter
    def secure_boot_options(self, secure_boot_options):
        """
        Sets the secure_boot_options of this ShapePlatformConfigOptions.

        :param secure_boot_options: The secure_boot_options of this ShapePlatformConfigOptions.
        :type: oci.core.models.ShapeSecureBootOptions
        """
        self._secure_boot_options = secure_boot_options

    @property
    def measured_boot_options(self):
        """
        Gets the measured_boot_options of this ShapePlatformConfigOptions.

        :return: The measured_boot_options of this ShapePlatformConfigOptions.
        :rtype: oci.core.models.ShapeMeasuredBootOptions
        """
        return self._measured_boot_options

    @measured_boot_options.setter
    def measured_boot_options(self, measured_boot_options):
        """
        Sets the measured_boot_options of this ShapePlatformConfigOptions.

        :param measured_boot_options: The measured_boot_options of this ShapePlatformConfigOptions.
        :type: oci.core.models.ShapeMeasuredBootOptions
        """
        self._measured_boot_options = measured_boot_options

    @property
    def trusted_platform_module_options(self):
        """
        Gets the trusted_platform_module_options of this ShapePlatformConfigOptions.

        :return: The trusted_platform_module_options of this ShapePlatformConfigOptions.
        :rtype: oci.core.models.ShapeTrustedPlatformModuleOptions
        """
        return self._trusted_platform_module_options

    @trusted_platform_module_options.setter
    def trusted_platform_module_options(self, trusted_platform_module_options):
        """
        Sets the trusted_platform_module_options of this ShapePlatformConfigOptions.

        :param trusted_platform_module_options: The trusted_platform_module_options of this ShapePlatformConfigOptions.
        :type: oci.core.models.ShapeTrustedPlatformModuleOptions
        """
        self._trusted_platform_module_options = trusted_platform_module_options

    @property
    def numa_nodes_per_socket_platform_options(self):
        """
        Gets the numa_nodes_per_socket_platform_options of this ShapePlatformConfigOptions.

        :return: The numa_nodes_per_socket_platform_options of this ShapePlatformConfigOptions.
        :rtype: oci.core.models.ShapeNumaNodesPerSocketPlatformOptions
        """
        return self._numa_nodes_per_socket_platform_options

    @numa_nodes_per_socket_platform_options.setter
    def numa_nodes_per_socket_platform_options(self, numa_nodes_per_socket_platform_options):
        """
        Sets the numa_nodes_per_socket_platform_options of this ShapePlatformConfigOptions.

        :param numa_nodes_per_socket_platform_options: The numa_nodes_per_socket_platform_options of this ShapePlatformConfigOptions.
        :type: oci.core.models.ShapeNumaNodesPerSocketPlatformOptions
        """
        self._numa_nodes_per_socket_platform_options = numa_nodes_per_socket_platform_options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
