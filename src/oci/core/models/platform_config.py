# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PlatformConfig(object):
    """
    The platform configuration for the instance.
    """

    #: A constant which can be used with the type property of a PlatformConfig.
    #: This constant has a value of "AMD_MILAN_BM"
    TYPE_AMD_MILAN_BM = "AMD_MILAN_BM"

    #: A constant which can be used with the type property of a PlatformConfig.
    #: This constant has a value of "AMD_ROME_BM"
    TYPE_AMD_ROME_BM = "AMD_ROME_BM"

    #: A constant which can be used with the type property of a PlatformConfig.
    #: This constant has a value of "AMD_ROME_BM_GPU"
    TYPE_AMD_ROME_BM_GPU = "AMD_ROME_BM_GPU"

    #: A constant which can be used with the type property of a PlatformConfig.
    #: This constant has a value of "INTEL_ICELAKE_BM"
    TYPE_INTEL_ICELAKE_BM = "INTEL_ICELAKE_BM"

    #: A constant which can be used with the type property of a PlatformConfig.
    #: This constant has a value of "INTEL_SKYLAKE_BM"
    TYPE_INTEL_SKYLAKE_BM = "INTEL_SKYLAKE_BM"

    #: A constant which can be used with the type property of a PlatformConfig.
    #: This constant has a value of "AMD_VM"
    TYPE_AMD_VM = "AMD_VM"

    #: A constant which can be used with the type property of a PlatformConfig.
    #: This constant has a value of "INTEL_VM"
    TYPE_INTEL_VM = "INTEL_VM"

    def __init__(self, **kwargs):
        """
        Initializes a new PlatformConfig object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.core.models.AmdMilanBmPlatformConfig`
        * :class:`~oci.core.models.AmdRomeBmPlatformConfig`
        * :class:`~oci.core.models.IntelSkylakeBmPlatformConfig`
        * :class:`~oci.core.models.AmdRomeBmGpuPlatformConfig`
        * :class:`~oci.core.models.IntelIcelakeBmPlatformConfig`
        * :class:`~oci.core.models.AmdVmPlatformConfig`
        * :class:`~oci.core.models.IntelVmPlatformConfig`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this PlatformConfig.
            Allowed values for this property are: "AMD_MILAN_BM", "AMD_ROME_BM", "AMD_ROME_BM_GPU", "INTEL_ICELAKE_BM", "INTEL_SKYLAKE_BM", "AMD_VM", "INTEL_VM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param is_secure_boot_enabled:
            The value to assign to the is_secure_boot_enabled property of this PlatformConfig.
        :type is_secure_boot_enabled: bool

        :param is_trusted_platform_module_enabled:
            The value to assign to the is_trusted_platform_module_enabled property of this PlatformConfig.
        :type is_trusted_platform_module_enabled: bool

        :param is_measured_boot_enabled:
            The value to assign to the is_measured_boot_enabled property of this PlatformConfig.
        :type is_measured_boot_enabled: bool

        """
        self.swagger_types = {
            'type': 'str',
            'is_secure_boot_enabled': 'bool',
            'is_trusted_platform_module_enabled': 'bool',
            'is_measured_boot_enabled': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'is_secure_boot_enabled': 'isSecureBootEnabled',
            'is_trusted_platform_module_enabled': 'isTrustedPlatformModuleEnabled',
            'is_measured_boot_enabled': 'isMeasuredBootEnabled'
        }

        self._type = None
        self._is_secure_boot_enabled = None
        self._is_trusted_platform_module_enabled = None
        self._is_measured_boot_enabled = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['type']

        if type == 'AMD_MILAN_BM':
            return 'AmdMilanBmPlatformConfig'

        if type == 'AMD_ROME_BM':
            return 'AmdRomeBmPlatformConfig'

        if type == 'INTEL_SKYLAKE_BM':
            return 'IntelSkylakeBmPlatformConfig'

        if type == 'AMD_ROME_BM_GPU':
            return 'AmdRomeBmGpuPlatformConfig'

        if type == 'INTEL_ICELAKE_BM':
            return 'IntelIcelakeBmPlatformConfig'

        if type == 'AMD_VM':
            return 'AmdVmPlatformConfig'

        if type == 'INTEL_VM':
            return 'IntelVmPlatformConfig'
        else:
            return 'PlatformConfig'

    @property
    def type(self):
        """
        **[Required]** Gets the type of this PlatformConfig.
        The type of platform being configured.

        Allowed values for this property are: "AMD_MILAN_BM", "AMD_ROME_BM", "AMD_ROME_BM_GPU", "INTEL_ICELAKE_BM", "INTEL_SKYLAKE_BM", "AMD_VM", "INTEL_VM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this PlatformConfig.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PlatformConfig.
        The type of platform being configured.


        :param type: The type of this PlatformConfig.
        :type: str
        """
        allowed_values = ["AMD_MILAN_BM", "AMD_ROME_BM", "AMD_ROME_BM_GPU", "INTEL_ICELAKE_BM", "INTEL_SKYLAKE_BM", "AMD_VM", "INTEL_VM"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def is_secure_boot_enabled(self):
        """
        Gets the is_secure_boot_enabled of this PlatformConfig.
        Whether Secure Boot is enabled on the instance.


        :return: The is_secure_boot_enabled of this PlatformConfig.
        :rtype: bool
        """
        return self._is_secure_boot_enabled

    @is_secure_boot_enabled.setter
    def is_secure_boot_enabled(self, is_secure_boot_enabled):
        """
        Sets the is_secure_boot_enabled of this PlatformConfig.
        Whether Secure Boot is enabled on the instance.


        :param is_secure_boot_enabled: The is_secure_boot_enabled of this PlatformConfig.
        :type: bool
        """
        self._is_secure_boot_enabled = is_secure_boot_enabled

    @property
    def is_trusted_platform_module_enabled(self):
        """
        Gets the is_trusted_platform_module_enabled of this PlatformConfig.
        Whether the Trusted Platform Module (TPM) is enabled on the instance.


        :return: The is_trusted_platform_module_enabled of this PlatformConfig.
        :rtype: bool
        """
        return self._is_trusted_platform_module_enabled

    @is_trusted_platform_module_enabled.setter
    def is_trusted_platform_module_enabled(self, is_trusted_platform_module_enabled):
        """
        Sets the is_trusted_platform_module_enabled of this PlatformConfig.
        Whether the Trusted Platform Module (TPM) is enabled on the instance.


        :param is_trusted_platform_module_enabled: The is_trusted_platform_module_enabled of this PlatformConfig.
        :type: bool
        """
        self._is_trusted_platform_module_enabled = is_trusted_platform_module_enabled

    @property
    def is_measured_boot_enabled(self):
        """
        Gets the is_measured_boot_enabled of this PlatformConfig.
        Whether the Measured Boot feature is enabled on the instance.


        :return: The is_measured_boot_enabled of this PlatformConfig.
        :rtype: bool
        """
        return self._is_measured_boot_enabled

    @is_measured_boot_enabled.setter
    def is_measured_boot_enabled(self, is_measured_boot_enabled):
        """
        Sets the is_measured_boot_enabled of this PlatformConfig.
        Whether the Measured Boot feature is enabled on the instance.


        :param is_measured_boot_enabled: The is_measured_boot_enabled of this PlatformConfig.
        :type: bool
        """
        self._is_measured_boot_enabled = is_measured_boot_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
