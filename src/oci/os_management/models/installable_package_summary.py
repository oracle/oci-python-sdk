# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstallablePackageSummary(object):
    """
    A software package available for install on a managed instance
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstallablePackageSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this InstallablePackageSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this InstallablePackageSummary.
        :type name: str

        :param type:
            The value to assign to the type property of this InstallablePackageSummary.
        :type type: str

        :param version:
            The value to assign to the version property of this InstallablePackageSummary.
        :type version: str

        :param architecture:
            The value to assign to the architecture property of this InstallablePackageSummary.
        :type architecture: str

        :param software_sources:
            The value to assign to the software_sources property of this InstallablePackageSummary.
        :type software_sources: list[oci.os_management.models.SoftwareSourceId]

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'type': 'str',
            'version': 'str',
            'architecture': 'str',
            'software_sources': 'list[SoftwareSourceId]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'type': 'type',
            'version': 'version',
            'architecture': 'architecture',
            'software_sources': 'softwareSources'
        }

        self._display_name = None
        self._name = None
        self._type = None
        self._version = None
        self._architecture = None
        self._software_sources = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this InstallablePackageSummary.
        Package name


        :return: The display_name of this InstallablePackageSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this InstallablePackageSummary.
        Package name


        :param display_name: The display_name of this InstallablePackageSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this InstallablePackageSummary.
        Unique identifier for the package. NOTE - This is not an OCID


        :return: The name of this InstallablePackageSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this InstallablePackageSummary.
        Unique identifier for the package. NOTE - This is not an OCID


        :param name: The name of this InstallablePackageSummary.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this InstallablePackageSummary.
        Type of the package


        :return: The type of this InstallablePackageSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this InstallablePackageSummary.
        Type of the package


        :param type: The type of this InstallablePackageSummary.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """
        **[Required]** Gets the version of this InstallablePackageSummary.
        Version of the package


        :return: The version of this InstallablePackageSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this InstallablePackageSummary.
        Version of the package


        :param version: The version of this InstallablePackageSummary.
        :type: str
        """
        self._version = version

    @property
    def architecture(self):
        """
        Gets the architecture of this InstallablePackageSummary.
        The architecture for which this package was built


        :return: The architecture of this InstallablePackageSummary.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this InstallablePackageSummary.
        The architecture for which this package was built


        :param architecture: The architecture of this InstallablePackageSummary.
        :type: str
        """
        self._architecture = architecture

    @property
    def software_sources(self):
        """
        Gets the software_sources of this InstallablePackageSummary.
        list of software sources that provide the software package


        :return: The software_sources of this InstallablePackageSummary.
        :rtype: list[oci.os_management.models.SoftwareSourceId]
        """
        return self._software_sources

    @software_sources.setter
    def software_sources(self, software_sources):
        """
        Sets the software_sources of this InstallablePackageSummary.
        list of software sources that provide the software package


        :param software_sources: The software_sources of this InstallablePackageSummary.
        :type: list[oci.os_management.models.SoftwareSourceId]
        """
        self._software_sources = software_sources

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
