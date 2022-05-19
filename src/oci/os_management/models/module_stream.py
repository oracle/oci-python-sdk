# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModuleStream(object):
    """
    A module stream provided by a software source
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModuleStream object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param module_name:
            The value to assign to the module_name property of this ModuleStream.
        :type module_name: str

        :param stream_name:
            The value to assign to the stream_name property of this ModuleStream.
        :type stream_name: str

        :param is_default:
            The value to assign to the is_default property of this ModuleStream.
        :type is_default: bool

        :param software_source_id:
            The value to assign to the software_source_id property of this ModuleStream.
        :type software_source_id: str

        :param architecture:
            The value to assign to the architecture property of this ModuleStream.
        :type architecture: str

        :param description:
            The value to assign to the description property of this ModuleStream.
        :type description: str

        :param profiles:
            The value to assign to the profiles property of this ModuleStream.
        :type profiles: list[str]

        :param packages:
            The value to assign to the packages property of this ModuleStream.
        :type packages: list[str]

        """
        self.swagger_types = {
            'module_name': 'str',
            'stream_name': 'str',
            'is_default': 'bool',
            'software_source_id': 'str',
            'architecture': 'str',
            'description': 'str',
            'profiles': 'list[str]',
            'packages': 'list[str]'
        }

        self.attribute_map = {
            'module_name': 'moduleName',
            'stream_name': 'streamName',
            'is_default': 'isDefault',
            'software_source_id': 'softwareSourceId',
            'architecture': 'architecture',
            'description': 'description',
            'profiles': 'profiles',
            'packages': 'packages'
        }

        self._module_name = None
        self._stream_name = None
        self._is_default = None
        self._software_source_id = None
        self._architecture = None
        self._description = None
        self._profiles = None
        self._packages = None

    @property
    def module_name(self):
        """
        **[Required]** Gets the module_name of this ModuleStream.
        The name of the module that contains the stream


        :return: The module_name of this ModuleStream.
        :rtype: str
        """
        return self._module_name

    @module_name.setter
    def module_name(self, module_name):
        """
        Sets the module_name of this ModuleStream.
        The name of the module that contains the stream


        :param module_name: The module_name of this ModuleStream.
        :type: str
        """
        self._module_name = module_name

    @property
    def stream_name(self):
        """
        **[Required]** Gets the stream_name of this ModuleStream.
        The name of the stream


        :return: The stream_name of this ModuleStream.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the stream_name of this ModuleStream.
        The name of the stream


        :param stream_name: The stream_name of this ModuleStream.
        :type: str
        """
        self._stream_name = stream_name

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
        The OCID of the software source that provides this module stream.


        :return: The software_source_id of this ModuleStream.
        :rtype: str
        """
        return self._software_source_id

    @software_source_id.setter
    def software_source_id(self, software_source_id):
        """
        Sets the software_source_id of this ModuleStream.
        The OCID of the software source that provides this module stream.


        :param software_source_id: The software_source_id of this ModuleStream.
        :type: str
        """
        self._software_source_id = software_source_id

    @property
    def architecture(self):
        """
        Gets the architecture of this ModuleStream.
        The architecture for which the packages in this module stream were built


        :return: The architecture of this ModuleStream.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this ModuleStream.
        The architecture for which the packages in this module stream were built


        :param architecture: The architecture of this ModuleStream.
        :type: str
        """
        self._architecture = architecture

    @property
    def description(self):
        """
        Gets the description of this ModuleStream.
        A description of the contents of the module stream


        :return: The description of this ModuleStream.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ModuleStream.
        A description of the contents of the module stream


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
        an argument to other OS Management APIs that interact directly with
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
        an argument to other OS Management APIs that interact directly with
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
        as an argument to other OS Management APIs that interact directly
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
        as an argument to other OS Management APIs that interact directly
        with packages.


        :param packages: The packages of this ModuleStream.
        :type: list[str]
        """
        self._packages = packages

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
