# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Update(object):
    """
    Update model.
    """

    #: A constant which can be used with the last_action property of a Update.
    #: This constant has a value of "ROLLING_APPLY"
    LAST_ACTION_ROLLING_APPLY = "ROLLING_APPLY"

    #: A constant which can be used with the last_action property of a Update.
    #: This constant has a value of "NON_ROLLING_APPLY"
    LAST_ACTION_NON_ROLLING_APPLY = "NON_ROLLING_APPLY"

    #: A constant which can be used with the last_action property of a Update.
    #: This constant has a value of "PRECHECK"
    LAST_ACTION_PRECHECK = "PRECHECK"

    #: A constant which can be used with the last_action property of a Update.
    #: This constant has a value of "ROLLBACK"
    LAST_ACTION_ROLLBACK = "ROLLBACK"

    #: A constant which can be used with the available_actions property of a Update.
    #: This constant has a value of "ROLLING_APPLY"
    AVAILABLE_ACTIONS_ROLLING_APPLY = "ROLLING_APPLY"

    #: A constant which can be used with the available_actions property of a Update.
    #: This constant has a value of "NON_ROLLING_APPLY"
    AVAILABLE_ACTIONS_NON_ROLLING_APPLY = "NON_ROLLING_APPLY"

    #: A constant which can be used with the available_actions property of a Update.
    #: This constant has a value of "PRECHECK"
    AVAILABLE_ACTIONS_PRECHECK = "PRECHECK"

    #: A constant which can be used with the available_actions property of a Update.
    #: This constant has a value of "ROLLBACK"
    AVAILABLE_ACTIONS_ROLLBACK = "ROLLBACK"

    #: A constant which can be used with the update_type property of a Update.
    #: This constant has a value of "GI_UPGRADE"
    UPDATE_TYPE_GI_UPGRADE = "GI_UPGRADE"

    #: A constant which can be used with the update_type property of a Update.
    #: This constant has a value of "GI_PATCH"
    UPDATE_TYPE_GI_PATCH = "GI_PATCH"

    #: A constant which can be used with the update_type property of a Update.
    #: This constant has a value of "OS_UPDATE"
    UPDATE_TYPE_OS_UPDATE = "OS_UPDATE"

    #: A constant which can be used with the lifecycle_state property of a Update.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a Update.
    #: This constant has a value of "SUCCESS"
    LIFECYCLE_STATE_SUCCESS = "SUCCESS"

    #: A constant which can be used with the lifecycle_state property of a Update.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a Update.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Update object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Update.
        :type id: str

        :param description:
            The value to assign to the description property of this Update.
        :type description: str

        :param last_action:
            The value to assign to the last_action property of this Update.
            Allowed values for this property are: "ROLLING_APPLY", "NON_ROLLING_APPLY", "PRECHECK", "ROLLBACK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type last_action: str

        :param available_actions:
            The value to assign to the available_actions property of this Update.
            Allowed values for items in this list are: "ROLLING_APPLY", "NON_ROLLING_APPLY", "PRECHECK", "ROLLBACK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type available_actions: list[str]

        :param update_type:
            The value to assign to the update_type property of this Update.
            Allowed values for this property are: "GI_UPGRADE", "GI_PATCH", "OS_UPDATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type update_type: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Update.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Update.
            Allowed values for this property are: "AVAILABLE", "SUCCESS", "IN_PROGRESS", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_released:
            The value to assign to the time_released property of this Update.
        :type time_released: datetime

        :param version:
            The value to assign to the version property of this Update.
        :type version: str

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'last_action': 'str',
            'available_actions': 'list[str]',
            'update_type': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'time_released': 'datetime',
            'version': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'last_action': 'lastAction',
            'available_actions': 'availableActions',
            'update_type': 'updateType',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'time_released': 'timeReleased',
            'version': 'version'
        }

        self._id = None
        self._description = None
        self._last_action = None
        self._available_actions = None
        self._update_type = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._time_released = None
        self._version = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Update.
        The `OCID`__ of the maintenance update.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Update.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Update.
        The `OCID`__ of the maintenance update.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Update.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        **[Required]** Gets the description of this Update.
        Details of the maintenance update package.


        :return: The description of this Update.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Update.
        Details of the maintenance update package.


        :param description: The description of this Update.
        :type: str
        """
        self._description = description

    @property
    def last_action(self):
        """
        Gets the last_action of this Update.
        The update action.

        Allowed values for this property are: "ROLLING_APPLY", "NON_ROLLING_APPLY", "PRECHECK", "ROLLBACK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The last_action of this Update.
        :rtype: str
        """
        return self._last_action

    @last_action.setter
    def last_action(self, last_action):
        """
        Sets the last_action of this Update.
        The update action.


        :param last_action: The last_action of this Update.
        :type: str
        """
        allowed_values = ["ROLLING_APPLY", "NON_ROLLING_APPLY", "PRECHECK", "ROLLBACK"]
        if not value_allowed_none_or_none_sentinel(last_action, allowed_values):
            last_action = 'UNKNOWN_ENUM_VALUE'
        self._last_action = last_action

    @property
    def available_actions(self):
        """
        Gets the available_actions of this Update.
        The possible actions performed by the update operation on the infrastructure components.

        Allowed values for items in this list are: "ROLLING_APPLY", "NON_ROLLING_APPLY", "PRECHECK", "ROLLBACK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The available_actions of this Update.
        :rtype: list[str]
        """
        return self._available_actions

    @available_actions.setter
    def available_actions(self, available_actions):
        """
        Sets the available_actions of this Update.
        The possible actions performed by the update operation on the infrastructure components.


        :param available_actions: The available_actions of this Update.
        :type: list[str]
        """
        allowed_values = ["ROLLING_APPLY", "NON_ROLLING_APPLY", "PRECHECK", "ROLLBACK"]
        if available_actions:
            available_actions[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in available_actions]
        self._available_actions = available_actions

    @property
    def update_type(self):
        """
        **[Required]** Gets the update_type of this Update.
        The type of cloud VM cluster maintenance update.

        Allowed values for this property are: "GI_UPGRADE", "GI_PATCH", "OS_UPDATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The update_type of this Update.
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        """
        Sets the update_type of this Update.
        The type of cloud VM cluster maintenance update.


        :param update_type: The update_type of this Update.
        :type: str
        """
        allowed_values = ["GI_UPGRADE", "GI_PATCH", "OS_UPDATE"]
        if not value_allowed_none_or_none_sentinel(update_type, allowed_values):
            update_type = 'UNKNOWN_ENUM_VALUE'
        self._update_type = update_type

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Update.
        Descriptive text providing additional details about the lifecycle state.


        :return: The lifecycle_details of this Update.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Update.
        Descriptive text providing additional details about the lifecycle state.


        :param lifecycle_details: The lifecycle_details of this Update.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Update.
        The current state of the maintenance update. Dependent on value of `lastAction`.

        Allowed values for this property are: "AVAILABLE", "SUCCESS", "IN_PROGRESS", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Update.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Update.
        The current state of the maintenance update. Dependent on value of `lastAction`.


        :param lifecycle_state: The lifecycle_state of this Update.
        :type: str
        """
        allowed_values = ["AVAILABLE", "SUCCESS", "IN_PROGRESS", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_released(self):
        """
        **[Required]** Gets the time_released of this Update.
        The date and time the maintenance update was released.


        :return: The time_released of this Update.
        :rtype: datetime
        """
        return self._time_released

    @time_released.setter
    def time_released(self, time_released):
        """
        Sets the time_released of this Update.
        The date and time the maintenance update was released.


        :param time_released: The time_released of this Update.
        :type: datetime
        """
        self._time_released = time_released

    @property
    def version(self):
        """
        **[Required]** Gets the version of this Update.
        The version of the maintenance update package.


        :return: The version of this Update.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Update.
        The version of the maintenance update package.


        :param version: The version of this Update.
        :type: str
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
