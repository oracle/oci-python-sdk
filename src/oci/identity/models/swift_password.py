# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SwiftPassword(object):
    """
    Swift is the OpenStack object storage service. A `SwiftPassword` is an Oracle-provided password for using a
    Swift client with the Oracle Cloud Infrastructure Object Storage Service. This password is associated with
    the user's Console login. Swift passwords never expire. A user can have up to two Swift passwords at a time.

    **Note:** The password is always an Oracle-generated string; you can't change it to a string of your choice.

    For more information, see `Managing User Credentials`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/managingcredentials.htm
    """

    #: A constant which can be used with the lifecycle_state property of a SwiftPassword.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SwiftPassword.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SwiftPassword.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SwiftPassword.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SwiftPassword.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new SwiftPassword object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param password:
            The value to assign to the password property of this SwiftPassword.
        :type password: str

        :param id:
            The value to assign to the id property of this SwiftPassword.
        :type id: str

        :param user_id:
            The value to assign to the user_id property of this SwiftPassword.
        :type user_id: str

        :param description:
            The value to assign to the description property of this SwiftPassword.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this SwiftPassword.
        :type time_created: datetime

        :param expires_on:
            The value to assign to the expires_on property of this SwiftPassword.
        :type expires_on: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SwiftPassword.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this SwiftPassword.
        :type inactive_status: int

        """
        self.swagger_types = {
            'password': 'str',
            'id': 'str',
            'user_id': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'expires_on': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int'
        }

        self.attribute_map = {
            'password': 'password',
            'id': 'id',
            'user_id': 'userId',
            'description': 'description',
            'time_created': 'timeCreated',
            'expires_on': 'expiresOn',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus'
        }

        self._password = None
        self._id = None
        self._user_id = None
        self._description = None
        self._time_created = None
        self._expires_on = None
        self._lifecycle_state = None
        self._inactive_status = None

    @property
    def password(self):
        """
        Gets the password of this SwiftPassword.
        The Swift password. The value is available only in the response for `CreateSwiftPassword`, and not
        for `ListSwiftPasswords` or `UpdateSwiftPassword`.


        :return: The password of this SwiftPassword.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this SwiftPassword.
        The Swift password. The value is available only in the response for `CreateSwiftPassword`, and not
        for `ListSwiftPasswords` or `UpdateSwiftPassword`.


        :param password: The password of this SwiftPassword.
        :type: str
        """
        self._password = password

    @property
    def id(self):
        """
        Gets the id of this SwiftPassword.
        The OCID of the Swift password.


        :return: The id of this SwiftPassword.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SwiftPassword.
        The OCID of the Swift password.


        :param id: The id of this SwiftPassword.
        :type: str
        """
        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this SwiftPassword.
        The OCID of the user the password belongs to.


        :return: The user_id of this SwiftPassword.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this SwiftPassword.
        The OCID of the user the password belongs to.


        :param user_id: The user_id of this SwiftPassword.
        :type: str
        """
        self._user_id = user_id

    @property
    def description(self):
        """
        Gets the description of this SwiftPassword.
        The description you assign to the Swift password. Does not have to be unique, and it's changeable.


        :return: The description of this SwiftPassword.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SwiftPassword.
        The description you assign to the Swift password. Does not have to be unique, and it's changeable.


        :param description: The description of this SwiftPassword.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this SwiftPassword.
        Date and time the `SwiftPassword` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this SwiftPassword.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SwiftPassword.
        Date and time the `SwiftPassword` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this SwiftPassword.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def expires_on(self):
        """
        Gets the expires_on of this SwiftPassword.
        Date and time when this password will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The expires_on of this SwiftPassword.
        :rtype: datetime
        """
        return self._expires_on

    @expires_on.setter
    def expires_on(self, expires_on):
        """
        Sets the expires_on of this SwiftPassword.
        Date and time when this password will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :param expires_on: The expires_on of this SwiftPassword.
        :type: datetime
        """
        self._expires_on = expires_on

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SwiftPassword.
        The password's current state. After creating a password, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SwiftPassword.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SwiftPassword.
        The password's current state. After creating a password, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this SwiftPassword.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this SwiftPassword.
        The detailed status of INACTIVE lifecycleState.


        :return: The inactive_status of this SwiftPassword.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this SwiftPassword.
        The detailed status of INACTIVE lifecycleState.


        :param inactive_status: The inactive_status of this SwiftPassword.
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
