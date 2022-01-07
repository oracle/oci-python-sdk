# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MfaTotpDeviceSummary(object):
    """
    As the name suggests, a `MfaTotpDeviceSummary` object contains information about a `MfaTotpDevice`.
    """

    #: A constant which can be used with the lifecycle_state property of a MfaTotpDeviceSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MfaTotpDeviceSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MfaTotpDeviceSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MfaTotpDeviceSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MfaTotpDeviceSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new MfaTotpDeviceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MfaTotpDeviceSummary.
        :type id: str

        :param user_id:
            The value to assign to the user_id property of this MfaTotpDeviceSummary.
        :type user_id: str

        :param time_created:
            The value to assign to the time_created property of this MfaTotpDeviceSummary.
        :type time_created: datetime

        :param time_expires:
            The value to assign to the time_expires property of this MfaTotpDeviceSummary.
        :type time_expires: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MfaTotpDeviceSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this MfaTotpDeviceSummary.
        :type inactive_status: int

        :param is_activated:
            The value to assign to the is_activated property of this MfaTotpDeviceSummary.
        :type is_activated: bool

        """
        self.swagger_types = {
            'id': 'str',
            'user_id': 'str',
            'time_created': 'datetime',
            'time_expires': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int',
            'is_activated': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId',
            'time_created': 'timeCreated',
            'time_expires': 'timeExpires',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus',
            'is_activated': 'isActivated'
        }

        self._id = None
        self._user_id = None
        self._time_created = None
        self._time_expires = None
        self._lifecycle_state = None
        self._inactive_status = None
        self._is_activated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MfaTotpDeviceSummary.
        The OCID of the MFA TOTP Device.


        :return: The id of this MfaTotpDeviceSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MfaTotpDeviceSummary.
        The OCID of the MFA TOTP Device.


        :param id: The id of this MfaTotpDeviceSummary.
        :type: str
        """
        self._id = id

    @property
    def user_id(self):
        """
        **[Required]** Gets the user_id of this MfaTotpDeviceSummary.
        The OCID of the user the MFA TOTP device belongs to.


        :return: The user_id of this MfaTotpDeviceSummary.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this MfaTotpDeviceSummary.
        The OCID of the user the MFA TOTP device belongs to.


        :param user_id: The user_id of this MfaTotpDeviceSummary.
        :type: str
        """
        self._user_id = user_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this MfaTotpDeviceSummary.
        Date and time the `MfaTotpDevice` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this MfaTotpDeviceSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MfaTotpDeviceSummary.
        Date and time the `MfaTotpDevice` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this MfaTotpDeviceSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_expires(self):
        """
        Gets the time_expires of this MfaTotpDeviceSummary.
        Date and time when this MFA TOTP device will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_expires of this MfaTotpDeviceSummary.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this MfaTotpDeviceSummary.
        Date and time when this MFA TOTP device will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_expires: The time_expires of this MfaTotpDeviceSummary.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MfaTotpDeviceSummary.
        The MFA TOTP device's current state.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MfaTotpDeviceSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MfaTotpDeviceSummary.
        The MFA TOTP device's current state.


        :param lifecycle_state: The lifecycle_state of this MfaTotpDeviceSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this MfaTotpDeviceSummary.
        The detailed status of INACTIVE lifecycleState.
        Allowed values are:
         - 1 - SUSPENDED
         - 2 - DISABLED
         - 4 - BLOCKED
         - 8 - LOCKED


        :return: The inactive_status of this MfaTotpDeviceSummary.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this MfaTotpDeviceSummary.
        The detailed status of INACTIVE lifecycleState.
        Allowed values are:
         - 1 - SUSPENDED
         - 2 - DISABLED
         - 4 - BLOCKED
         - 8 - LOCKED


        :param inactive_status: The inactive_status of this MfaTotpDeviceSummary.
        :type: int
        """
        self._inactive_status = inactive_status

    @property
    def is_activated(self):
        """
        **[Required]** Gets the is_activated of this MfaTotpDeviceSummary.
        Flag to indicate if the MFA TOTP device has been activated


        :return: The is_activated of this MfaTotpDeviceSummary.
        :rtype: bool
        """
        return self._is_activated

    @is_activated.setter
    def is_activated(self, is_activated):
        """
        Sets the is_activated of this MfaTotpDeviceSummary.
        Flag to indicate if the MFA TOTP device has been activated


        :param is_activated: The is_activated of this MfaTotpDeviceSummary.
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
