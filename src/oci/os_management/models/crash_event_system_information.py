# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CrashEventSystemInformation(object):
    """
    Detailed information about system at the time of the crash.
    """

    #: A constant which can be used with the architecture property of a CrashEventSystemInformation.
    #: This constant has a value of "IA_32"
    ARCHITECTURE_IA_32 = "IA_32"

    #: A constant which can be used with the architecture property of a CrashEventSystemInformation.
    #: This constant has a value of "X86_64"
    ARCHITECTURE_X86_64 = "X86_64"

    #: A constant which can be used with the architecture property of a CrashEventSystemInformation.
    #: This constant has a value of "AARCH64"
    ARCHITECTURE_AARCH64 = "AARCH64"

    #: A constant which can be used with the architecture property of a CrashEventSystemInformation.
    #: This constant has a value of "SPARC"
    ARCHITECTURE_SPARC = "SPARC"

    #: A constant which can be used with the architecture property of a CrashEventSystemInformation.
    #: This constant has a value of "AMD64_DEBIAN"
    ARCHITECTURE_AMD64_DEBIAN = "AMD64_DEBIAN"

    #: A constant which can be used with the os_family property of a CrashEventSystemInformation.
    #: This constant has a value of "LINUX"
    OS_FAMILY_LINUX = "LINUX"

    #: A constant which can be used with the os_family property of a CrashEventSystemInformation.
    #: This constant has a value of "WINDOWS"
    OS_FAMILY_WINDOWS = "WINDOWS"

    #: A constant which can be used with the os_family property of a CrashEventSystemInformation.
    #: This constant has a value of "ALL"
    OS_FAMILY_ALL = "ALL"

    def __init__(self, **kwargs):
        """
        Initializes a new CrashEventSystemInformation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param architecture:
            The value to assign to the architecture property of this CrashEventSystemInformation.
            Allowed values for this property are: "IA_32", "X86_64", "AARCH64", "SPARC", "AMD64_DEBIAN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type architecture: str

        :param ksplice_effective_kernel_version:
            The value to assign to the ksplice_effective_kernel_version property of this CrashEventSystemInformation.
        :type ksplice_effective_kernel_version: str

        :param os_family:
            The value to assign to the os_family property of this CrashEventSystemInformation.
            Allowed values for this property are: "LINUX", "WINDOWS", "ALL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type os_family: str

        :param os_name:
            The value to assign to the os_name property of this CrashEventSystemInformation.
        :type os_name: str

        :param os_kernel_release:
            The value to assign to the os_kernel_release property of this CrashEventSystemInformation.
        :type os_kernel_release: str

        :param os_kernel_version:
            The value to assign to the os_kernel_version property of this CrashEventSystemInformation.
        :type os_kernel_version: str

        :param os_system_version:
            The value to assign to the os_system_version property of this CrashEventSystemInformation.
        :type os_system_version: str

        """
        self.swagger_types = {
            'architecture': 'str',
            'ksplice_effective_kernel_version': 'str',
            'os_family': 'str',
            'os_name': 'str',
            'os_kernel_release': 'str',
            'os_kernel_version': 'str',
            'os_system_version': 'str'
        }

        self.attribute_map = {
            'architecture': 'architecture',
            'ksplice_effective_kernel_version': 'kspliceEffectiveKernelVersion',
            'os_family': 'osFamily',
            'os_name': 'osName',
            'os_kernel_release': 'osKernelRelease',
            'os_kernel_version': 'osKernelVersion',
            'os_system_version': 'osSystemVersion'
        }

        self._architecture = None
        self._ksplice_effective_kernel_version = None
        self._os_family = None
        self._os_name = None
        self._os_kernel_release = None
        self._os_kernel_version = None
        self._os_system_version = None

    @property
    def architecture(self):
        """
        Gets the architecture of this CrashEventSystemInformation.
        system architecture

        Allowed values for this property are: "IA_32", "X86_64", "AARCH64", "SPARC", "AMD64_DEBIAN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The architecture of this CrashEventSystemInformation.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this CrashEventSystemInformation.
        system architecture


        :param architecture: The architecture of this CrashEventSystemInformation.
        :type: str
        """
        allowed_values = ["IA_32", "X86_64", "AARCH64", "SPARC", "AMD64_DEBIAN"]
        if not value_allowed_none_or_none_sentinel(architecture, allowed_values):
            architecture = 'UNKNOWN_ENUM_VALUE'
        self._architecture = architecture

    @property
    def ksplice_effective_kernel_version(self):
        """
        Gets the ksplice_effective_kernel_version of this CrashEventSystemInformation.
        Active ksplice kernel version (uptrack-uname -r)


        :return: The ksplice_effective_kernel_version of this CrashEventSystemInformation.
        :rtype: str
        """
        return self._ksplice_effective_kernel_version

    @ksplice_effective_kernel_version.setter
    def ksplice_effective_kernel_version(self, ksplice_effective_kernel_version):
        """
        Sets the ksplice_effective_kernel_version of this CrashEventSystemInformation.
        Active ksplice kernel version (uptrack-uname -r)


        :param ksplice_effective_kernel_version: The ksplice_effective_kernel_version of this CrashEventSystemInformation.
        :type: str
        """
        self._ksplice_effective_kernel_version = ksplice_effective_kernel_version

    @property
    def os_family(self):
        """
        Gets the os_family of this CrashEventSystemInformation.
        The Operating System type of the managed instance.

        Allowed values for this property are: "LINUX", "WINDOWS", "ALL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The os_family of this CrashEventSystemInformation.
        :rtype: str
        """
        return self._os_family

    @os_family.setter
    def os_family(self, os_family):
        """
        Sets the os_family of this CrashEventSystemInformation.
        The Operating System type of the managed instance.


        :param os_family: The os_family of this CrashEventSystemInformation.
        :type: str
        """
        allowed_values = ["LINUX", "WINDOWS", "ALL"]
        if not value_allowed_none_or_none_sentinel(os_family, allowed_values):
            os_family = 'UNKNOWN_ENUM_VALUE'
        self._os_family = os_family

    @property
    def os_name(self):
        """
        Gets the os_name of this CrashEventSystemInformation.
        Operating System Name (OCA value)


        :return: The os_name of this CrashEventSystemInformation.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """
        Sets the os_name of this CrashEventSystemInformation.
        Operating System Name (OCA value)


        :param os_name: The os_name of this CrashEventSystemInformation.
        :type: str
        """
        self._os_name = os_name

    @property
    def os_kernel_release(self):
        """
        Gets the os_kernel_release of this CrashEventSystemInformation.
        Operating System Kernel Release (uname -v)


        :return: The os_kernel_release of this CrashEventSystemInformation.
        :rtype: str
        """
        return self._os_kernel_release

    @os_kernel_release.setter
    def os_kernel_release(self, os_kernel_release):
        """
        Sets the os_kernel_release of this CrashEventSystemInformation.
        Operating System Kernel Release (uname -v)


        :param os_kernel_release: The os_kernel_release of this CrashEventSystemInformation.
        :type: str
        """
        self._os_kernel_release = os_kernel_release

    @property
    def os_kernel_version(self):
        """
        Gets the os_kernel_version of this CrashEventSystemInformation.
        Operating System Kernel Version (uname -r)


        :return: The os_kernel_version of this CrashEventSystemInformation.
        :rtype: str
        """
        return self._os_kernel_version

    @os_kernel_version.setter
    def os_kernel_version(self, os_kernel_version):
        """
        Sets the os_kernel_version of this CrashEventSystemInformation.
        Operating System Kernel Version (uname -r)


        :param os_kernel_version: The os_kernel_version of this CrashEventSystemInformation.
        :type: str
        """
        self._os_kernel_version = os_kernel_version

    @property
    def os_system_version(self):
        """
        Gets the os_system_version of this CrashEventSystemInformation.
        Version of the OS (VERSION from /etc/os-release)


        :return: The os_system_version of this CrashEventSystemInformation.
        :rtype: str
        """
        return self._os_system_version

    @os_system_version.setter
    def os_system_version(self, os_system_version):
        """
        Sets the os_system_version of this CrashEventSystemInformation.
        Version of the OS (VERSION from /etc/os-release)


        :param os_system_version: The os_system_version of this CrashEventSystemInformation.
        :type: str
        """
        self._os_system_version = os_system_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
