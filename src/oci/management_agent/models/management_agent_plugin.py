# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagementAgentPlugin(object):
    """
    Summary of the ManagementAgentPlugin.
    """

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentPlugin.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentPlugin.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentPlugin.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentPlugin.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentPlugin.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentPlugin.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentPlugin.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ManagementAgentPlugin.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ManagementAgentPlugin object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagementAgentPlugin.
        :type id: str

        :param name:
            The value to assign to the name property of this ManagementAgentPlugin.
        :type name: str

        :param version:
            The value to assign to the version property of this ManagementAgentPlugin.
        :type version: int

        :param supported_platform_types:
            The value to assign to the supported_platform_types property of this ManagementAgentPlugin.
        :type supported_platform_types: list[oci.management_agent.models.PlatformTypes]

        :param display_name:
            The value to assign to the display_name property of this ManagementAgentPlugin.
        :type display_name: str

        :param description:
            The value to assign to the description property of this ManagementAgentPlugin.
        :type description: str

        :param is_console_deployable:
            The value to assign to the is_console_deployable property of this ManagementAgentPlugin.
        :type is_console_deployable: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ManagementAgentPlugin.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'version': 'int',
            'supported_platform_types': 'list[PlatformTypes]',
            'display_name': 'str',
            'description': 'str',
            'is_console_deployable': 'bool',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'version': 'version',
            'supported_platform_types': 'supportedPlatformTypes',
            'display_name': 'displayName',
            'description': 'description',
            'is_console_deployable': 'isConsoleDeployable',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._name = None
        self._version = None
        self._supported_platform_types = None
        self._display_name = None
        self._description = None
        self._is_console_deployable = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagementAgentPlugin.
        Management Agent Plugin Id


        :return: The id of this ManagementAgentPlugin.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagementAgentPlugin.
        Management Agent Plugin Id


        :param id: The id of this ManagementAgentPlugin.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ManagementAgentPlugin.
        Management Agent Plugin Name


        :return: The name of this ManagementAgentPlugin.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagementAgentPlugin.
        Management Agent Plugin Name


        :param name: The name of this ManagementAgentPlugin.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """
        Gets the version of this ManagementAgentPlugin.
        Management Agent Plugin Version


        :return: The version of this ManagementAgentPlugin.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ManagementAgentPlugin.
        Management Agent Plugin Version


        :param version: The version of this ManagementAgentPlugin.
        :type: int
        """
        self._version = version

    @property
    def supported_platform_types(self):
        """
        Gets the supported_platform_types of this ManagementAgentPlugin.
        Supported Platform Types


        :return: The supported_platform_types of this ManagementAgentPlugin.
        :rtype: list[oci.management_agent.models.PlatformTypes]
        """
        return self._supported_platform_types

    @supported_platform_types.setter
    def supported_platform_types(self, supported_platform_types):
        """
        Sets the supported_platform_types of this ManagementAgentPlugin.
        Supported Platform Types


        :param supported_platform_types: The supported_platform_types of this ManagementAgentPlugin.
        :type: list[oci.management_agent.models.PlatformTypes]
        """
        self._supported_platform_types = supported_platform_types

    @property
    def display_name(self):
        """
        Gets the display_name of this ManagementAgentPlugin.
        Management Agent Plugin Display Name


        :return: The display_name of this ManagementAgentPlugin.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ManagementAgentPlugin.
        Management Agent Plugin Display Name


        :param display_name: The display_name of this ManagementAgentPlugin.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ManagementAgentPlugin.
        Management Agent Plugin description


        :return: The description of this ManagementAgentPlugin.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManagementAgentPlugin.
        Management Agent Plugin description


        :param description: The description of this ManagementAgentPlugin.
        :type: str
        """
        self._description = description

    @property
    def is_console_deployable(self):
        """
        Gets the is_console_deployable of this ManagementAgentPlugin.
        A flag to indicate whether a given plugin can be deployed from Agent Console UI or not.


        :return: The is_console_deployable of this ManagementAgentPlugin.
        :rtype: bool
        """
        return self._is_console_deployable

    @is_console_deployable.setter
    def is_console_deployable(self, is_console_deployable):
        """
        Sets the is_console_deployable of this ManagementAgentPlugin.
        A flag to indicate whether a given plugin can be deployed from Agent Console UI or not.


        :param is_console_deployable: The is_console_deployable of this ManagementAgentPlugin.
        :type: bool
        """
        self._is_console_deployable = is_console_deployable

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ManagementAgentPlugin.
        The current state of Management Agent Plugin

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"


        :return: The lifecycle_state of this ManagementAgentPlugin.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ManagementAgentPlugin.
        The current state of Management Agent Plugin


        :param lifecycle_state: The lifecycle_state of this ManagementAgentPlugin.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "TERMINATED", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
