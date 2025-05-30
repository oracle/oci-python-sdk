# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModuleStream(object):
    """
    An object that defines a module stream provided by a software source.
    """

    #: A constant which can be used with the arch_type property of a ModuleStream.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a ModuleStream.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a ModuleStream.
    #: This constant has a value of "I686"
    ARCH_TYPE_I686 = "I686"

    #: A constant which can be used with the arch_type property of a ModuleStream.
    #: This constant has a value of "NOARCH"
    ARCH_TYPE_NOARCH = "NOARCH"

    #: A constant which can be used with the arch_type property of a ModuleStream.
    #: This constant has a value of "SRC"
    ARCH_TYPE_SRC = "SRC"

    #: A constant which can be used with the arch_type property of a ModuleStream.
    #: This constant has a value of "I386"
    ARCH_TYPE_I386 = "I386"

    def __init__(self, **kwargs):
        """
        Initializes a new ModuleStream object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param module_name:
            The value to assign to the module_name property of this ModuleStream.
        :type module_name: str

        :param name:
            The value to assign to the name property of this ModuleStream.
        :type name: str

        :param is_default:
            The value to assign to the is_default property of this ModuleStream.
        :type is_default: bool

        :param software_source_id:
            The value to assign to the software_source_id property of this ModuleStream.
        :type software_source_id: str

        :param arch_type:
            The value to assign to the arch_type property of this ModuleStream.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type arch_type: str

        :param description:
            The value to assign to the description property of this ModuleStream.
        :type description: str

        :param profiles:
            The value to assign to the profiles property of this ModuleStream.
        :type profiles: list[str]

        :param packages:
            The value to assign to the packages property of this ModuleStream.
        :type packages: list[str]

        :param is_latest:
            The value to assign to the is_latest property of this ModuleStream.
        :type is_latest: bool

        """
        self.swagger_types = {
            'module_name': 'str',
            'name': 'str',
            'is_default': 'bool',
            'software_source_id': 'str',
            'arch_type': 'str',
            'description': 'str',
            'profiles': 'list[str]',
            'packages': 'list[str]',
            'is_latest': 'bool'
        }
        self.attribute_map = {
            'module_name': 'moduleName',
            'name': 'name',
            'is_default': 'isDefault',
            'software_source_id': 'softwareSourceId',
            'arch_type': 'archType',
            'description': 'description',
            'profiles': 'profiles',
            'packages': 'packages',
            'is_latest': 'isLatest'
        }
        self._module_name = None
        self._name = None
        self._is_default = None
        self._software_source_id = None
        self._arch_type = None
        self._description = None
        self._profiles = None
        self._packages = None
        self._is_latest = None

    @property
    def module_name(self):
        """
        **[Required]** Gets the module_name of this ModuleStream.
        The name of the module that contains the stream.


        :return: The module_name of this ModuleStream.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this ModuleStream.
        The name of the module that contains the stream.


        :param module_name: The module_name of this ModuleStream.
        :type: str
        """
        self._module_name = module_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ModuleStream.
        The name of the stream.


        :return: The name of this ModuleStream.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModuleStream.
        The name of the stream.


        :param name: The name of this ModuleStream.
        :type: str
        """
        self._name = name

    @property
    def is_default(self):
        """
        Gets the is_default of this ModuleStream.
        Indicates if this stream is the default for its module.


        :return: The is_default of this ModuleStream.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this ModuleStream.
        Indicates if this stream is the default for its module.


        :param is_default: The is_default of this ModuleStream.
        :type: bool
        """
        self._is_default = is_default

    @property
    def software_source_id(self):
        """
        Gets the software_source_id of this ModuleStream.
        The `OCID`__ of the software source that provides this module stream.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The software_source_id of this ModuleStream.
        :rtype: str
        """
        return self._software_source_id

    @software_source_id.setter
    def software_source_id(self, software_source_id):
        """
        Sets the software_source_id of this ModuleStream.
        The `OCID`__ of the software source that provides this module stream.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param software_source_id: The software_source_id of this ModuleStream.
        :type: str
        """
        self._software_source_id = software_source_id

    @property
    def arch_type(self):
        """
        Gets the arch_type of this ModuleStream.
        The architecture for which the packages in this module stream were built.

        Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The arch_type of this ModuleStream.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this ModuleStream.
        The architecture for which the packages in this module stream were built.


        :param arch_type: The arch_type of this ModuleStream.
        :type: str
        """
        allowed_values = ["X86_64", "AARCH64", "I686", "NOARCH", "SRC", "I386"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            arch_type = 'UNKNOWN_ENUM_VALUE'
        self._arch_type = arch_type

    @property
    def description(self):
        """
        Gets the description of this ModuleStream.
        A description of the contents of the module stream.


        :return: The description of this ModuleStream.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ModuleStream.
        A description of the contents of the module stream.


        :param description: The description of this ModuleStream.
        :type: str
        """
        self._description = description

    @property
    def profiles(self):
        """
        Gets the profiles of this ModuleStream.
        A list of profiles that are part of the stream.  Each element in
        the list is the name of a profile.  The name is suitable to use as
        an argument to other OS Management Hub APIs that interact directly with
        module stream profiles.  However, it is not URL encoded.


        :return: The profiles of this ModuleStream.
        :rtype: list[str]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """
        Sets the profiles of this ModuleStream.
        A list of profiles that are part of the stream.  Each element in
        the list is the name of a profile.  The name is suitable to use as
        an argument to other OS Management Hub APIs that interact directly with
        module stream profiles.  However, it is not URL encoded.


        :param profiles: The profiles of this ModuleStream.
        :type: list[str]
        """
        self._profiles = profiles

    @property
    def packages(self):
        """
        Gets the packages of this ModuleStream.
        A list of packages that are contained by the stream.  Each element
        in the list is the name of a package.  The name is suitable to use
        as an argument to other OS Management Hub APIs that interact directly
        with packages.


        :return: The packages of this ModuleStream.
        :rtype: list[str]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """
        Sets the packages of this ModuleStream.
        A list of packages that are contained by the stream.  Each element
        in the list is the name of a package.  The name is suitable to use
        as an argument to other OS Management Hub APIs that interact directly
        with packages.


        :param packages: The packages of this ModuleStream.
        :type: list[str]
        """
        self._packages = packages

    @property
    def is_latest(self):
        """
        Gets the is_latest of this ModuleStream.
        Indicates whether this module stream is the latest.


        :return: The is_latest of this ModuleStream.
        :rtype: bool
        """
        return self._is_latest

    @is_latest.setter
    def is_latest(self, is_latest):
        """
        Sets the is_latest of this ModuleStream.
        Indicates whether this module stream is the latest.


        :param is_latest: The is_latest of this ModuleStream.
        :type: bool
        """
        self._is_latest = is_latest

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
