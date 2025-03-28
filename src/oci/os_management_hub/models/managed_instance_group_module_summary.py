# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220901


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedInstanceGroupModuleSummary(object):
    """
    Provides the summary information about a module on a managed instance group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedInstanceGroupModuleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ManagedInstanceGroupModuleSummary.
        :type name: str

        :param enabled_stream:
            The value to assign to the enabled_stream property of this ManagedInstanceGroupModuleSummary.
        :type enabled_stream: str

        :param installed_profiles:
            The value to assign to the installed_profiles property of this ManagedInstanceGroupModuleSummary.
        :type installed_profiles: list[str]

        :param software_source_id:
            The value to assign to the software_source_id property of this ManagedInstanceGroupModuleSummary.
        :type software_source_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'enabled_stream': 'str',
            'installed_profiles': 'list[str]',
            'software_source_id': 'str'
        }
        self.attribute_map = {
            'name': 'name',
            'enabled_stream': 'enabledStream',
            'installed_profiles': 'installedProfiles',
            'software_source_id': 'softwareSourceId'
        }
        self._name = None
        self._enabled_stream = None
        self._installed_profiles = None
        self._software_source_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ManagedInstanceGroupModuleSummary.
        The name of the module.


        :return: The name of this ManagedInstanceGroupModuleSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagedInstanceGroupModuleSummary.
        The name of the module.


        :param name: The name of this ManagedInstanceGroupModuleSummary.
        :type: str
        """
        self._name = name

    @property
    def enabled_stream(self):
        """
        Gets the enabled_stream of this ManagedInstanceGroupModuleSummary.
        The name of the module stream that is enabled for the group.


        :return: The enabled_stream of this ManagedInstanceGroupModuleSummary.
        :rtype: str
        """
        return self._enabled_stream

    @enabled_stream.setter
    def enabled_stream(self, enabled_stream):
        """
        Sets the enabled_stream of this ManagedInstanceGroupModuleSummary.
        The name of the module stream that is enabled for the group.


        :param enabled_stream: The enabled_stream of this ManagedInstanceGroupModuleSummary.
        :type: str
        """
        self._enabled_stream = enabled_stream

    @property
    def installed_profiles(self):
        """
        Gets the installed_profiles of this ManagedInstanceGroupModuleSummary.
        The list of installed profiles under the currently enabled module stream.


        :return: The installed_profiles of this ManagedInstanceGroupModuleSummary.
        :rtype: list[str]
        """
        return self._installed_profiles

    @installed_profiles.setter
    def installed_profiles(self, installed_profiles):
        """
        Sets the installed_profiles of this ManagedInstanceGroupModuleSummary.
        The list of installed profiles under the currently enabled module stream.


        :param installed_profiles: The installed_profiles of this ManagedInstanceGroupModuleSummary.
        :type: list[str]
        """
        self._installed_profiles = installed_profiles

    @property
    def software_source_id(self):
        """
        Gets the software_source_id of this ManagedInstanceGroupModuleSummary.
        The `OCID`__ of the software source that provides this module stream.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The software_source_id of this ManagedInstanceGroupModuleSummary.
        :rtype: str
        """
        return self._software_source_id

    @software_source_id.setter
    def software_source_id(self, software_source_id):
        """
        Sets the software_source_id of this ManagedInstanceGroupModuleSummary.
        The `OCID`__ of the software source that provides this module stream.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param software_source_id: The software_source_id of this ManagedInstanceGroupModuleSummary.
        :type: str
        """
        self._software_source_id = software_source_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
