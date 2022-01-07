# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MfaTotpDevice(object):
    """
    Users can enable multi-factor authentication (MFA) for their own user accounts. After MFA is enabled, the
    user is prompted for a time-based one-time password (TOTP) to authenticate before they can sign in to the
    Console. To enable multi-factor authentication, the user must register a mobile device with a TOTP authenticator app
    installed. The registration process creates the `MfaTotpDevice` object. The registration process requires
    interaction with the Console and cannot be completed programmatically. For more information, see
    `Managing Multi-Factor Authentication`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Tasks/usingmfa.htm
    """

    #: A constant which can be used with the lifecycle_state property of a MfaTotpDevice.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MfaTotpDevice.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MfaTotpDevice.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MfaTotpDevice.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MfaTotpDevice.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new MfaTotpDevice object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MfaTotpDevice.
        :type id: str

        :param seed:
            The value to assign to the seed property of this MfaTotpDevice.
        :type seed: str

        :param user_id:
            The value to assign to the user_id property of this MfaTotpDevice.
        :type user_id: str

        :param time_created:
            The value to assign to the time_created property of this MfaTotpDevice.
        :type time_created: datetime

        :param time_expires:
            The value to assign to the time_expires property of this MfaTotpDevice.
        :type time_expires: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MfaTotpDevice.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this MfaTotpDevice.
        :type inactive_status: int

        :param is_activated:
            The value to assign to the is_activated property of this MfaTotpDevice.
        :type is_activated: bool

        """
        self.swagger_types = {
            'id': 'str',
            'seed': 'str',
            'user_id': 'str',
            'time_created': 'datetime',
            'time_expires': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int',
            'is_activated': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'seed': 'seed',
            'user_id': 'userId',
            'time_created': 'timeCreated',
            'time_expires': 'timeExpires',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus',
            'is_activated': 'isActivated'
        }

        self._id = None
        self._seed = None
        self._user_id = None
        self._time_created = None
        self._time_expires = None
        self._lifecycle_state = None
        self._inactive_status = None
        self._is_activated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MfaTotpDevice.
        The OCID of the MFA TOTP device.


        :return: The id of this MfaTotpDevice.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MfaTotpDevice.
        The OCID of the MFA TOTP device.


        :param id: The id of this MfaTotpDevice.
        :type: str
        """
        self._id = id

    @property
    def seed(self):
        """
        **[Required]** Gets the seed of this MfaTotpDevice.
        The seed for the MFA TOTP device (Base32 encoded).


        :return: The seed of this MfaTotpDevice.
        :rtype: str
        """
        return self._seed

    @seed.setter
    def seed(self, seed):
        """
        Sets the seed of this MfaTotpDevice.
        The seed for the MFA TOTP device (Base32 encoded).


        :param seed: The seed of this MfaTotpDevice.
        :type: str
        """
        self._seed = seed

    @property
    def user_id(self):
        """
        **[Required]** Gets the user_id of this MfaTotpDevice.
        The OCID of the user the MFA TOTP device belongs to.


        :return: The user_id of this MfaTotpDevice.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this MfaTotpDevice.
        The OCID of the user the MFA TOTP device belongs to.


        :param user_id: The user_id of this MfaTotpDevice.
        :type: str
        """
        self._user_id = user_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MfaTotpDevice.
        Date and time the `MfaTotpDevice` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this MfaTotpDevice.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MfaTotpDevice.
        Date and time the `MfaTotpDevice` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this MfaTotpDevice.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_expires(self):
        """
        Gets the time_expires of this MfaTotpDevice.
        Date and time when this MFA TOTP device will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_expires of this MfaTotpDevice.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this MfaTotpDevice.
        Date and time when this MFA TOTP device will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_expires: The time_expires of this MfaTotpDevice.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MfaTotpDevice.
        The MFA TOTP device's current state. After creating the MFA TOTP device, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MfaTotpDevice.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MfaTotpDevice.
        The MFA TOTP device's current state. After creating the MFA TOTP device, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this MfaTotpDevice.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this MfaTotpDevice.
        The detailed status of INACTIVE lifecycleState.
        Allowed values are:
         - 1 - SUSPENDED
         - 2 - DISABLED
         - 4 - BLOCKED
         - 8 - LOCKED


        :return: The inactive_status of this MfaTotpDevice.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this MfaTotpDevice.
        The detailed status of INACTIVE lifecycleState.
        Allowed values are:
         - 1 - SUSPENDED
         - 2 - DISABLED
         - 4 - BLOCKED
         - 8 - LOCKED


        :param inactive_status: The inactive_status of this MfaTotpDevice.
        :type: int
        """
        self._inactive_status = inactive_status

    @property
    def is_activated(self):
        """
        **[Required]** Gets the is_activated of this MfaTotpDevice.
        Flag to indicate if the MFA TOTP device has been activated.


        :return: The is_activated of this MfaTotpDevice.
        :rtype: bool
        """
        return self._is_activated

    @is_activated.setter
    def is_activated(self, is_activated):
        """
        Sets the is_activated of this MfaTotpDevice.
        Flag to indicate if the MFA TOTP device has been activated.


        :param is_activated: The is_activated of this MfaTotpDevice.
        :type: bool
        """
        self._is_activated = is_activated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
