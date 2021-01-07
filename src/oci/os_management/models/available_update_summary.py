# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AvailableUpdateSummary(object):
    """
    An update available for a managed instance
    """

    #: A constant which can be used with the update_type property of a AvailableUpdateSummary.
    #: This constant has a value of "SECURITY"
    UPDATE_TYPE_SECURITY = "SECURITY"

    #: A constant which can be used with the update_type property of a AvailableUpdateSummary.
    #: This constant has a value of "BUG"
    UPDATE_TYPE_BUG = "BUG"

    #: A constant which can be used with the update_type property of a AvailableUpdateSummary.
    #: This constant has a value of "ENHANCEMENT"
    UPDATE_TYPE_ENHANCEMENT = "ENHANCEMENT"

    #: A constant which can be used with the update_type property of a AvailableUpdateSummary.
    #: This constant has a value of "OTHER"
    UPDATE_TYPE_OTHER = "OTHER"

    def __init__(self, **kwargs):
        """
        Initializes a new AvailableUpdateSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this AvailableUpdateSummary.
        :type display_name: str

        :param name:
            The value to assign to the name property of this AvailableUpdateSummary.
        :type name: str

        :param update_type:
            The value to assign to the update_type property of this AvailableUpdateSummary.
            Allowed values for this property are: "SECURITY", "BUG", "ENHANCEMENT", "OTHER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type update_type: str

        :param type:
            The value to assign to the type property of this AvailableUpdateSummary.
        :type type: str

        :param installed_version:
            The value to assign to the installed_version property of this AvailableUpdateSummary.
        :type installed_version: str

        :param available_version:
            The value to assign to the available_version property of this AvailableUpdateSummary.
        :type available_version: str

        :param architecture:
            The value to assign to the architecture property of this AvailableUpdateSummary.
        :type architecture: str

        :param errata:
            The value to assign to the errata property of this AvailableUpdateSummary.
        :type errata: list[oci.os_management.models.Id]

        :param related_cves:
            The value to assign to the related_cves property of this AvailableUpdateSummary.
        :type related_cves: list[str]

        :param software_sources:
            The value to assign to the software_sources property of this AvailableUpdateSummary.
        :type software_sources: list[oci.os_management.models.SoftwareSourceId]

        """
        self.swagger_types = {
            'display_name': 'str',
            'name': 'str',
            'update_type': 'str',
            'type': 'str',
            'installed_version': 'str',
            'available_version': 'str',
            'architecture': 'str',
            'errata': 'list[Id]',
            'related_cves': 'list[str]',
            'software_sources': 'list[SoftwareSourceId]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'name': 'name',
            'update_type': 'updateType',
            'type': 'type',
            'installed_version': 'installedVersion',
            'available_version': 'availableVersion',
            'architecture': 'architecture',
            'errata': 'errata',
            'related_cves': 'relatedCves',
            'software_sources': 'softwareSources'
        }

        self._display_name = None
        self._name = None
        self._update_type = None
        self._type = None
        self._installed_version = None
        self._available_version = None
        self._architecture = None
        self._errata = None
        self._related_cves = None
        self._software_sources = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AvailableUpdateSummary.
        Package name


        :return: The display_name of this AvailableUpdateSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AvailableUpdateSummary.
        Package name


        :param display_name: The display_name of this AvailableUpdateSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AvailableUpdateSummary.
        Unique identifier for the package available for update. NOTE - This is not an OCID


        :return: The name of this AvailableUpdateSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AvailableUpdateSummary.
        Unique identifier for the package available for update. NOTE - This is not an OCID


        :param name: The name of this AvailableUpdateSummary.
        :type: str
        """
        self._name = name

    @property
    def update_type(self):
        """
        Gets the update_type of this AvailableUpdateSummary.
        The purpose of this update.

        Allowed values for this property are: "SECURITY", "BUG", "ENHANCEMENT", "OTHER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The update_type of this AvailableUpdateSummary.
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        """
        Sets the update_type of this AvailableUpdateSummary.
        The purpose of this update.


        :param update_type: The update_type of this AvailableUpdateSummary.
        :type: str
        """
        allowed_values = ["SECURITY", "BUG", "ENHANCEMENT", "OTHER"]
        if not value_allowed_none_or_none_sentinel(update_type, allowed_values):
            update_type = 'UNKNOWN_ENUM_VALUE'
        self._update_type = update_type

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AvailableUpdateSummary.
        Type of the package


        :return: The type of this AvailableUpdateSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AvailableUpdateSummary.
        Type of the package


        :param type: The type of this AvailableUpdateSummary.
        :type: str
        """
        self._type = type

    @property
    def installed_version(self):
        """
        **[Required]** Gets the installed_version of this AvailableUpdateSummary.
        Version of the installed package


        :return: The installed_version of this AvailableUpdateSummary.
        :rtype: str
        """
        return self._installed_version

    @installed_version.setter
    def installed_version(self, installed_version):
        """
        Sets the installed_version of this AvailableUpdateSummary.
        Version of the installed package


        :param installed_version: The installed_version of this AvailableUpdateSummary.
        :type: str
        """
        self._installed_version = installed_version

    @property
    def available_version(self):
        """
        **[Required]** Gets the available_version of this AvailableUpdateSummary.
        Version of the package available for update


        :return: The available_version of this AvailableUpdateSummary.
        :rtype: str
        """
        return self._available_version

    @available_version.setter
    def available_version(self, available_version):
        """
        Sets the available_version of this AvailableUpdateSummary.
        Version of the package available for update


        :param available_version: The available_version of this AvailableUpdateSummary.
        :type: str
        """
        self._available_version = available_version

    @property
    def architecture(self):
        """
        Gets the architecture of this AvailableUpdateSummary.
        The architecture for which this package was built


        :return: The architecture of this AvailableUpdateSummary.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """
        Sets the architecture of this AvailableUpdateSummary.
        The architecture for which this package was built


        :param architecture: The architecture of this AvailableUpdateSummary.
        :type: str
        """
        self._architecture = architecture

    @property
    def errata(self):
        """
        Gets the errata of this AvailableUpdateSummary.
        List of errata containing this update


        :return: The errata of this AvailableUpdateSummary.
        :rtype: list[oci.os_management.models.Id]
        """
        return self._errata

    @errata.setter
    def errata(self, errata):
        """
        Sets the errata of this AvailableUpdateSummary.
        List of errata containing this update


        :param errata: The errata of this AvailableUpdateSummary.
        :type: list[oci.os_management.models.Id]
        """
        self._errata = errata

    @property
    def related_cves(self):
        """
        Gets the related_cves of this AvailableUpdateSummary.
        List of CVEs applicable to this erratum


        :return: The related_cves of this AvailableUpdateSummary.
        :rtype: list[str]
        """
        return self._related_cves

    @related_cves.setter
    def related_cves(self, related_cves):
        """
        Sets the related_cves of this AvailableUpdateSummary.
        List of CVEs applicable to this erratum


        :param related_cves: The related_cves of this AvailableUpdateSummary.
        :type: list[str]
        """
        self._related_cves = related_cves

    @property
    def software_sources(self):
        """
        Gets the software_sources of this AvailableUpdateSummary.
        list of software sources that provide the software package


        :return: The software_sources of this AvailableUpdateSummary.
        :rtype: list[oci.os_management.models.SoftwareSourceId]
        """
        return self._software_sources

    @software_sources.setter
    def software_sources(self, software_sources):
        """
        Sets the software_sources of this AvailableUpdateSummary.
        list of software sources that provide the software package


        :param software_sources: The software_sources of this AvailableUpdateSummary.
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
