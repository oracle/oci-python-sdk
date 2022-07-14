# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActivityLog(object):
    """
    The log of the action taken by different persona on the access request, e.g. approve/deny/revoke
    """

    #: A constant which can be used with the user_level property of a ActivityLog.
    #: This constant has a value of "LEVEL1"
    USER_LEVEL_LEVEL1 = "LEVEL1"

    #: A constant which can be used with the user_level property of a ActivityLog.
    #: This constant has a value of "LEVEL2"
    USER_LEVEL_LEVEL2 = "LEVEL2"

    #: A constant which can be used with the user_level property of a ActivityLog.
    #: This constant has a value of "LEVEL3"
    USER_LEVEL_LEVEL3 = "LEVEL3"

    #: A constant which can be used with the user_level property of a ActivityLog.
    #: This constant has a value of "ADMIN"
    USER_LEVEL_ADMIN = "ADMIN"

    #: A constant which can be used with the user_level property of a ActivityLog.
    #: This constant has a value of "OPERATOR"
    USER_LEVEL_OPERATOR = "OPERATOR"

    #: A constant which can be used with the action property of a ActivityLog.
    #: This constant has a value of "APPROVE"
    ACTION_APPROVE = "APPROVE"

    #: A constant which can be used with the action property of a ActivityLog.
    #: This constant has a value of "DENY"
    ACTION_DENY = "DENY"

    #: A constant which can be used with the action property of a ActivityLog.
    #: This constant has a value of "REVOKE"
    ACTION_REVOKE = "REVOKE"

    #: A constant which can be used with the action property of a ActivityLog.
    #: This constant has a value of "CANCEL"
    ACTION_CANCEL = "CANCEL"

    def __init__(self, **kwargs):
        """
        Initializes a new ActivityLog object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param user_id:
            The value to assign to the user_id property of this ActivityLog.
        :type user_id: str

        :param user_level:
            The value to assign to the user_level property of this ActivityLog.
            Allowed values for this property are: "LEVEL1", "LEVEL2", "LEVEL3", "ADMIN", "OPERATOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type user_level: str

        :param action:
            The value to assign to the action property of this ActivityLog.
            Allowed values for this property are: "APPROVE", "DENY", "REVOKE", "CANCEL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param message:
            The value to assign to the message property of this ActivityLog.
        :type message: str

        :param time_updated:
            The value to assign to the time_updated property of this ActivityLog.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'user_id': 'str',
            'user_level': 'str',
            'action': 'str',
            'message': 'str',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'user_id': 'userId',
            'user_level': 'userLevel',
            'action': 'action',
            'message': 'message',
            'time_updated': 'timeUpdated'
        }

        self._user_id = None
        self._user_level = None
        self._action = None
        self._message = None
        self._time_updated = None

    @property
    def user_id(self):
        """
        Gets the user_id of this ActivityLog.
        User OCID of the persona


        :return: The user_id of this ActivityLog.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ActivityLog.
        User OCID of the persona


        :param user_id: The user_id of this ActivityLog.
        :type: str
        """
        self._user_id = user_id

    @property
    def user_level(self):
        """
        Gets the user_level of this ActivityLog.
        Level of the persona

        Allowed values for this property are: "LEVEL1", "LEVEL2", "LEVEL3", "ADMIN", "OPERATOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The user_level of this ActivityLog.
        :rtype: str
        """
        return self._user_level

    @user_level.setter
    def user_level(self, user_level):
        """
        Sets the user_level of this ActivityLog.
        Level of the persona


        :param user_level: The user_level of this ActivityLog.
        :type: str
        """
        allowed_values = ["LEVEL1", "LEVEL2", "LEVEL3", "ADMIN", "OPERATOR"]
        if not value_allowed_none_or_none_sentinel(user_level, allowed_values):
            user_level = 'UNKNOWN_ENUM_VALUE'
        self._user_level = user_level

    @property
    def action(self):
        """
        Gets the action of this ActivityLog.
        The action take by persona

        Allowed values for this property are: "APPROVE", "DENY", "REVOKE", "CANCEL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this ActivityLog.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ActivityLog.
        The action take by persona


        :param action: The action of this ActivityLog.
        :type: str
        """
        allowed_values = ["APPROVE", "DENY", "REVOKE", "CANCEL"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def message(self):
        """
        Gets the message of this ActivityLog.
        The action justification or details.


        :return: The message of this ActivityLog.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ActivityLog.
        The action justification or details.


        :param message: The message of this ActivityLog.
        :type: str
        """
        self._message = message

    @property
    def time_updated(self):
        """
        Gets the time_updated of this ActivityLog.
        The time the action was taken. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this ActivityLog.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ActivityLog.
        The time the action was taken. Format is defined by `RFC3339`__.
        Example: `2020-01-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this ActivityLog.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
