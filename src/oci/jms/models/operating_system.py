# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OperatingSystem(object):
    """
    Operating System of the platform on which the Java Runtime was reported.
    """

    #: A constant which can be used with the family property of a OperatingSystem.
    #: This constant has a value of "LINUX"
    FAMILY_LINUX = "LINUX"

    #: A constant which can be used with the family property of a OperatingSystem.
    #: This constant has a value of "WINDOWS"
    FAMILY_WINDOWS = "WINDOWS"

    #: A constant which can be used with the family property of a OperatingSystem.
    #: This constant has a value of "MACOS"
    FAMILY_MACOS = "MACOS"

    #: A constant which can be used with the family property of a OperatingSystem.
    #: This constant has a value of "UNKNOWN"
    FAMILY_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new OperatingSystem object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param family:
            The value to assign to the family property of this OperatingSystem.
            Allowed values for this property are: "LINUX", "WINDOWS", "MACOS", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type family: str

        :param name:
            The value to assign to the name property of this OperatingSystem.
        :type name: str

        :param version:
            The value to assign to the version property of this OperatingSystem.
        :type version: str

        :param architecture:
            The value to assign to the architecture property of this OperatingSystem.
        :type architecture: str

        :param managed_instance_count:
            The value to assign to the managed_instance_count property of this OperatingSystem.
        :type managed_instance_count: int

        """
        self.swagger_types = {
            'family': 'str',
            'name': 'str',
            'version': 'str',
            'architecture': 'str',
            'managed_instance_count': 'int'
        }

        self.attribute_map = {
            'family': 'family',
            'name': 'name',
            'version': 'version',
            'architecture': 'architecture',
            'managed_instance_count': 'managedInstanceCount'
        }

        self._family = None
        self._name = None
        self._version = None
        self._architecture = None
        self._managed_instance_count = None

    @property
    def family(self):
        """
        **[Required]** Gets the family of this OperatingSystem.
        The operating system type, such as Windows or Linux

        Allowed values for this property are: "LINUX", "WINDOWS", "MACOS", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The family of this OperatingSystem.
        :rtype: str
        """
        return self._family

    @family.setter
    def family(self, family):
        """
        Sets the family of this OperatingSystem.
        The operating system type, such as Windows or Linux


        :param family: The family of this OperatingSystem.
        :type: str
        """
        allowed_values = ["LINUX", "WINDOWS", "MACOS", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(family, allowed_values):
            family = 'UNKNOWN_ENUM_VALUE'
        self._family = family

    @property
    def name(self):
        """
        **[Required]** Gets the name of this OperatingSystem.
        The name of the operating system as provided by the Java system property os.name.


        :return: The name of this OperatingSystem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OperatingSystem.
        The name of the operating system as provided by the Java system property os.name.


        :param name: The name of this OperatingSystem.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """
        **[Required]** Gets the version of this OperatingSystem.
        The version of the operating system as provided by the Java system property os.version.


        :return: The version of this OperatingSystem.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this OperatingSystem.
        The version of the operating system as provided by the Java system property os.version.


        :param version: The version of this OperatingSystem.
        :type: str
        """
        self._version = version

    @property
    def architecture(self):
        """
        **[Required]** Gets the architecture of this OperatingSystem.
        The architecture of the operating system as provided by the Java system property os.arch.


        :return: The architecture of this OperatingSystem.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this OperatingSystem.
        The architecture of the operating system as provided by the Java system property os.arch.


        :param architecture: The architecture of this OperatingSystem.
        :type: str
        """
        self._architecture = architecture

    @property
    def managed_instance_count(self):
        """
        Gets the managed_instance_count of this OperatingSystem.
        Number of instances running the operating system


        :return: The managed_instance_count of this OperatingSystem.
        :rtype: int
        """
        return self._managed_instance_count

    @managed_instance_count.setter
    def managed_instance_count(self, managed_instance_count):
        """
        Sets the managed_instance_count of this OperatingSystem.
        Number of instances running the operating system


        :param managed_instance_count: The managed_instance_count of this OperatingSystem.
        :type: int
        """
        self._managed_instance_count = managed_instance_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
