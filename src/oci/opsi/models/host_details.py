# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HostDetails(object):
    """
    Partial information about a host which includes id, name, type.
    """

    #: A constant which can be used with the platform_type property of a HostDetails.
    #: This constant has a value of "LINUX"
    PLATFORM_TYPE_LINUX = "LINUX"

    #: A constant which can be used with the platform_type property of a HostDetails.
    #: This constant has a value of "SOLARIS"
    PLATFORM_TYPE_SOLARIS = "SOLARIS"

    #: A constant which can be used with the platform_type property of a HostDetails.
    #: This constant has a value of "SUNOS"
    PLATFORM_TYPE_SUNOS = "SUNOS"

    #: A constant which can be used with the platform_type property of a HostDetails.
    #: This constant has a value of "ZLINUX"
    PLATFORM_TYPE_ZLINUX = "ZLINUX"

    def __init__(self, **kwargs):
        """
        Initializes a new HostDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this HostDetails.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this HostDetails.
        :type compartment_id: str

        :param host_name:
            The value to assign to the host_name property of this HostDetails.
        :type host_name: str

        :param host_display_name:
            The value to assign to the host_display_name property of this HostDetails.
        :type host_display_name: str

        :param platform_type:
            The value to assign to the platform_type property of this HostDetails.
            Allowed values for this property are: "LINUX", "SOLARIS", "SUNOS", "ZLINUX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type platform_type: str

        :param agent_identifier:
            The value to assign to the agent_identifier property of this HostDetails.
        :type agent_identifier: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'host_name': 'str',
            'host_display_name': 'str',
            'platform_type': 'str',
            'agent_identifier': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'host_name': 'hostName',
            'host_display_name': 'hostDisplayName',
            'platform_type': 'platformType',
            'agent_identifier': 'agentIdentifier'
        }

        self._id = None
        self._compartment_id = None
        self._host_name = None
        self._host_display_name = None
        self._platform_type = None
        self._agent_identifier = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this HostDetails.
        The `OCID`__ of the host.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this HostDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HostDetails.
        The `OCID`__ of the host.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this HostDetails.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this HostDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this HostDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this HostDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this HostDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this HostDetails.
        The host name. The host name is unique amongst the hosts managed by the same management agent.


        :return: The host_name of this HostDetails.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this HostDetails.
        The host name. The host name is unique amongst the hosts managed by the same management agent.


        :param host_name: The host_name of this HostDetails.
        :type: str
        """
        self._host_name = host_name

    @property
    def host_display_name(self):
        """
        Gets the host_display_name of this HostDetails.
        The user-friendly name for the host. The name does not have to be unique.


        :return: The host_display_name of this HostDetails.
        :rtype: str
        """
        return self._host_display_name

    @host_display_name.setter
    def host_display_name(self, host_display_name):
        """
        Sets the host_display_name of this HostDetails.
        The user-friendly name for the host. The name does not have to be unique.


        :param host_display_name: The host_display_name of this HostDetails.
        :type: str
        """
        self._host_display_name = host_display_name

    @property
    def platform_type(self):
        """
        **[Required]** Gets the platform_type of this HostDetails.
        Platform type.
        Supported platformType(s) for MACS-managed external host insight: [LINUX].
        Supported platformType(s) for MACS-managed cloud host insight: [LINUX].
        Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].

        Allowed values for this property are: "LINUX", "SOLARIS", "SUNOS", "ZLINUX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The platform_type of this HostDetails.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this HostDetails.
        Platform type.
        Supported platformType(s) for MACS-managed external host insight: [LINUX].
        Supported platformType(s) for MACS-managed cloud host insight: [LINUX].
        Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX].


        :param platform_type: The platform_type of this HostDetails.
        :type: str
        """
        allowed_values = ["LINUX", "SOLARIS", "SUNOS", "ZLINUX"]
        if not value_allowed_none_or_none_sentinel(platform_type, allowed_values):
            platform_type = 'UNKNOWN_ENUM_VALUE'
        self._platform_type = platform_type

    @property
    def agent_identifier(self):
        """
        **[Required]** Gets the agent_identifier of this HostDetails.
        The identifier of the agent.


        :return: The agent_identifier of this HostDetails.
        :rtype: str
        """
        return self._agent_identifier

    @agent_identifier.setter
    def agent_identifier(self, agent_identifier):
        """
        Sets the agent_identifier of this HostDetails.
        The identifier of the agent.


        :param agent_identifier: The agent_identifier of this HostDetails.
        :type: str
        """
        self._agent_identifier = agent_identifier

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
