# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UIPassword(object):
    """
    A text password that enables a user to sign in to the Console, the user interface for interacting with Oracle
    Cloud Infrastructure.

    For more information about user credentials, see `User Credentials`__.

    __ https://docs.cloud.oracle.com/Content/Identity/usercred/usercredentials.htm
    """

    #: A constant which can be used with the lifecycle_state property of a UIPassword.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a UIPassword.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a UIPassword.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a UIPassword.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a UIPassword.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new UIPassword object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param password:
            The value to assign to the password property of this UIPassword.
        :type password: str

        :param user_id:
            The value to assign to the user_id property of this UIPassword.
        :type user_id: str

        :param time_created:
            The value to assign to the time_created property of this UIPassword.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this UIPassword.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this UIPassword.
        :type inactive_status: int

        """
        self.swagger_types = {
            'password': 'str',
            'user_id': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int'
        }

        self.attribute_map = {
            'password': 'password',
            'user_id': 'userId',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus'
        }

        self._password = None
        self._user_id = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None

    @property
    def password(self):
        """
        Gets the password of this UIPassword.
        The user's password for the Console.


        :return: The password of this UIPassword.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UIPassword.
        The user's password for the Console.


        :param password: The password of this UIPassword.
        :type: str
        """
        self._password = password

    @property
    def user_id(self):
        """
        Gets the user_id of this UIPassword.
        The OCID of the user.


        :return: The user_id of this UIPassword.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UIPassword.
        The OCID of the user.


        :param user_id: The user_id of this UIPassword.
        :type: str
        """
        self._user_id = user_id

    @property
    def time_created(self):
        """
        Gets the time_created of this UIPassword.
        Date and time the password was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this UIPassword.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this UIPassword.
        Date and time the password was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this UIPassword.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this UIPassword.
        The password's current state. After creating a password, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this UIPassword.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this UIPassword.
        The password's current state. After creating a password, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this UIPassword.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this UIPassword.
        The detailed status of INACTIVE lifecycleState.


        :return: The inactive_status of this UIPassword.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this UIPassword.
        The detailed status of INACTIVE lifecycleState.


        :param inactive_status: The inactive_status of this UIPassword.
        :type: int
        """
        self._inactive_status = inactive_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
