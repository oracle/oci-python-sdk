# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .importable_agent_entity_summary import ImportableAgentEntitySummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostImportableAgentEntitySummary(ImportableAgentEntitySummary):
    """
    An agent host entity that can be imported into Operations Insights.
    """

    #: A constant which can be used with the platform_type property of a HostImportableAgentEntitySummary.
    #: This constant has a value of "LINUX"
    PLATFORM_TYPE_LINUX = "LINUX"

    #: A constant which can be used with the platform_type property of a HostImportableAgentEntitySummary.
    #: This constant has a value of "SOLARIS"
    PLATFORM_TYPE_SOLARIS = "SOLARIS"

    #: A constant which can be used with the platform_type property of a HostImportableAgentEntitySummary.
    #: This constant has a value of "SUNOS"
    PLATFORM_TYPE_SUNOS = "SUNOS"

    def __init__(self, **kwargs):
        """
        Initializes a new HostImportableAgentEntitySummary object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.HostImportableAgentEntitySummary.entity_source` attribute
        of this class is ``MACS_MANAGED_EXTERNAL_HOST`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_source:
            The value to assign to the entity_source property of this HostImportableAgentEntitySummary.
            Allowed values for this property are: "MACS_MANAGED_EXTERNAL_HOST", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type entity_source: str

        :param management_agent_id:
            The value to assign to the management_agent_id property of this HostImportableAgentEntitySummary.
        :type management_agent_id: str

        :param management_agent_display_name:
            The value to assign to the management_agent_display_name property of this HostImportableAgentEntitySummary.
        :type management_agent_display_name: str

        :param host_name:
            The value to assign to the host_name property of this HostImportableAgentEntitySummary.
        :type host_name: str

        :param platform_type:
            The value to assign to the platform_type property of this HostImportableAgentEntitySummary.
            Allowed values for this property are: "LINUX", "SOLARIS", "SUNOS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type platform_type: str

        """
        self.swagger_types = {
            'entity_source': 'str',
            'management_agent_id': 'str',
            'management_agent_display_name': 'str',
            'host_name': 'str',
            'platform_type': 'str'
        }

        self.attribute_map = {
            'entity_source': 'entitySource',
            'management_agent_id': 'managementAgentId',
            'management_agent_display_name': 'managementAgentDisplayName',
            'host_name': 'hostName',
            'platform_type': 'platformType'
        }

        self._entity_source = None
        self._management_agent_id = None
        self._management_agent_display_name = None
        self._host_name = None
        self._platform_type = None
        self._entity_source = 'MACS_MANAGED_EXTERNAL_HOST'

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this HostImportableAgentEntitySummary.
        The host name. The host name is unique amongst the hosts managed by the same management agent.


        :return: The host_name of this HostImportableAgentEntitySummary.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this HostImportableAgentEntitySummary.
        The host name. The host name is unique amongst the hosts managed by the same management agent.


        :param host_name: The host_name of this HostImportableAgentEntitySummary.
        :type: str
        """
        self._host_name = host_name

    @property
    def platform_type(self):
        """
        **[Required]** Gets the platform_type of this HostImportableAgentEntitySummary.
        Platform type.
        Supported platformType(s) for MACS-managed external host insight: [LINUX].
        Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS].

        Allowed values for this property are: "LINUX", "SOLARIS", "SUNOS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The platform_type of this HostImportableAgentEntitySummary.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this HostImportableAgentEntitySummary.
        Platform type.
        Supported platformType(s) for MACS-managed external host insight: [LINUX].
        Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS].


        :param platform_type: The platform_type of this HostImportableAgentEntitySummary.
        :type: str
        """
        allowed_values = ["LINUX", "SOLARIS", "SUNOS"]
        if not value_allowed_none_or_none_sentinel(platform_type, allowed_values):
            platform_type = 'UNKNOWN_ENUM_VALUE'
        self._platform_type = platform_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
