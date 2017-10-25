# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class Patch(object):

    def __init__(self):

        self.swagger_types = {
            'available_actions': 'list[str]',
            'description': 'str',
            'id': 'str',
            'last_action': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'time_released': 'datetime',
            'version': 'str'
        }

        self.attribute_map = {
            'available_actions': 'availableActions',
            'description': 'description',
            'id': 'id',
            'last_action': 'lastAction',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'time_released': 'timeReleased',
            'version': 'version'
        }

        self._available_actions = None
        self._description = None
        self._id = None
        self._last_action = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._time_released = None
        self._version = None

    @property
    def available_actions(self):
        """
        Gets the available_actions of this Patch.
        Actions that can possibly be performed using this patch.

        Allowed values for items in this list are: "APPLY", "PRECHECK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The available_actions of this Patch.
        :rtype: list[str]
        """
        return self._available_actions

    @available_actions.setter
    def available_actions(self, available_actions):
        """
        Sets the available_actions of this Patch.
        Actions that can possibly be performed using this patch.


        :param available_actions: The available_actions of this Patch.
        :type: list[str]
        """
        allowed_values = ["APPLY", "PRECHECK"]
        available_actions[:] = ['UNKNOWN_ENUM_VALUE' if x not in allowed_values else x for x in available_actions]
        self._available_actions = available_actions

    @property
    def description(self):
        """
        Gets the description of this Patch.
        The text describing this patch package.


        :return: The description of this Patch.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Patch.
        The text describing this patch package.


        :param description: The description of this Patch.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """
        Gets the id of this Patch.
        The OCID of the patch.


        :return: The id of this Patch.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Patch.
        The OCID of the patch.


        :param id: The id of this Patch.
        :type: str
        """
        self._id = id

    @property
    def last_action(self):
        """
        Gets the last_action of this Patch.
        Action that is currently being performed or was completed last.

        Allowed values for this property are: "APPLY", "PRECHECK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The last_action of this Patch.
        :rtype: str
        """
        return self._last_action

    @last_action.setter
    def last_action(self, last_action):
        """
        Sets the last_action of this Patch.
        Action that is currently being performed or was completed last.


        :param last_action: The last_action of this Patch.
        :type: str
        """
        allowed_values = ["APPLY", "PRECHECK"]
        if last_action not in allowed_values:
            last_action = 'UNKNOWN_ENUM_VALUE'
        self._last_action = last_action

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Patch.
        A descriptive text associated with the lifecycleState.
        Typically can contain additional displayable text.


        :return: The lifecycle_details of this Patch.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Patch.
        A descriptive text associated with the lifecycleState.
        Typically can contain additional displayable text.


        :param lifecycle_details: The lifecycle_details of this Patch.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Patch.
        The current state of the patch as a result of lastAction.

        Allowed values for this property are: "AVAILABLE", "SUCCESS", "IN_PROGRESS", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Patch.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Patch.
        The current state of the patch as a result of lastAction.


        :param lifecycle_state: The lifecycle_state of this Patch.
        :type: str
        """
        allowed_values = ["AVAILABLE", "SUCCESS", "IN_PROGRESS", "FAILED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_released(self):
        """
        Gets the time_released of this Patch.
        The date and time that the patch was released.


        :return: The time_released of this Patch.
        :rtype: datetime
        """
        return self._time_released

    @time_released.setter
    def time_released(self, time_released):
        """
        Sets the time_released of this Patch.
        The date and time that the patch was released.


        :param time_released: The time_released of this Patch.
        :type: datetime
        """
        self._time_released = time_released

    @property
    def version(self):
        """
        Gets the version of this Patch.
        The version of this patch package.


        :return: The version of this Patch.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Patch.
        The version of this patch package.


        :param version: The version of this Patch.
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
