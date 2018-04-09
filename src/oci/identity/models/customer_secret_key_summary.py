# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomerSecretKeySummary(object):
    """
    As the name suggests, a `CustomerSecretKeySummary` object contains information about a `CustomerSecretKey`.
    A `CustomerSecretKey` is an Oracle-provided key for using the Object Storage Service's Amazon S3 compatible API.
    """

    #: A constant which can be used with the lifecycle_state property of a CustomerSecretKeySummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a CustomerSecretKeySummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CustomerSecretKeySummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a CustomerSecretKeySummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a CustomerSecretKeySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new CustomerSecretKeySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this CustomerSecretKeySummary.
        :type id: str

        :param user_id:
            The value to assign to the user_id property of this CustomerSecretKeySummary.
        :type user_id: str

        :param display_name:
            The value to assign to the display_name property of this CustomerSecretKeySummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this CustomerSecretKeySummary.
        :type time_created: datetime

        :param time_expires:
            The value to assign to the time_expires property of this CustomerSecretKeySummary.
        :type time_expires: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this CustomerSecretKeySummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this CustomerSecretKeySummary.
        :type inactive_status: int

        """
        self.swagger_types = {
            'id': 'str',
            'user_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_expires': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_expires': 'timeExpires',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus'
        }

        self._id = None
        self._user_id = None
        self._display_name = None
        self._time_created = None
        self._time_expires = None
        self._lifecycle_state = None
        self._inactive_status = None

    @property
    def id(self):
        """
        Gets the id of this CustomerSecretKeySummary.
        The OCID of the secret key.


        :return: The id of this CustomerSecretKeySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CustomerSecretKeySummary.
        The OCID of the secret key.


        :param id: The id of this CustomerSecretKeySummary.
        :type: str
        """
        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this CustomerSecretKeySummary.
        The OCID of the user the password belongs to.


        :return: The user_id of this CustomerSecretKeySummary.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this CustomerSecretKeySummary.
        The OCID of the user the password belongs to.


        :param user_id: The user_id of this CustomerSecretKeySummary.
        :type: str
        """
        self._user_id = user_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CustomerSecretKeySummary.
        The displayName you assign to the secret key. Does not have to be unique, and it's changeable.


        :return: The display_name of this CustomerSecretKeySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CustomerSecretKeySummary.
        The displayName you assign to the secret key. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CustomerSecretKeySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this CustomerSecretKeySummary.
        Date and time the `CustomerSecretKey` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this CustomerSecretKeySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this CustomerSecretKeySummary.
        Date and time the `CustomerSecretKey` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this CustomerSecretKeySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_expires(self):
        """
        Gets the time_expires of this CustomerSecretKeySummary.
        Date and time when this password will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_expires of this CustomerSecretKeySummary.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this CustomerSecretKeySummary.
        Date and time when this password will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_expires: The time_expires of this CustomerSecretKeySummary.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this CustomerSecretKeySummary.
        The secret key's current state. After creating a secret key, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this CustomerSecretKeySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this CustomerSecretKeySummary.
        The secret key's current state. After creating a secret key, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this CustomerSecretKeySummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this CustomerSecretKeySummary.
        The detailed status of INACTIVE lifecycleState.


        :return: The inactive_status of this CustomerSecretKeySummary.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this CustomerSecretKeySummary.
        The detailed status of INACTIVE lifecycleState.


        :param inactive_status: The inactive_status of this CustomerSecretKeySummary.
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
