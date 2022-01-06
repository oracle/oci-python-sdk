# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbCredential(object):
    """
    Database credentials are needed for onboarding cloud database to identity.
    The DB credentials are used for DB authentication with the service.
    """

    #: A constant which can be used with the lifecycle_state property of a DbCredential.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DbCredential.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DbCredential.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DbCredential.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new DbCredential object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DbCredential.
        :type id: str

        :param user_id:
            The value to assign to the user_id property of this DbCredential.
        :type user_id: str

        :param time_created:
            The value to assign to the time_created property of this DbCredential.
        :type time_created: datetime

        :param time_expires:
            The value to assign to the time_expires property of this DbCredential.
        :type time_expires: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbCredential.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DbCredential.
        :type lifecycle_details: int

        """
        self.swagger_types = {
            'id': 'str',
            'user_id': 'str',
            'time_created': 'datetime',
            'time_expires': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId',
            'time_created': 'timeCreated',
            'time_expires': 'timeExpires',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._id = None
        self._user_id = None
        self._time_created = None
        self._time_expires = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def id(self):
        """
        Gets the id of this DbCredential.
        The OCID of the DB credential.


        :return: The id of this DbCredential.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbCredential.
        The OCID of the DB credential.


        :param id: The id of this DbCredential.
        :type: str
        """
        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this DbCredential.
        The OCID of the user the DB credential belongs to.


        :return: The user_id of this DbCredential.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this DbCredential.
        The OCID of the user the DB credential belongs to.


        :param user_id: The user_id of this DbCredential.
        :type: str
        """
        self._user_id = user_id

    @property
    def time_created(self):
        """
        Gets the time_created of this DbCredential.
        Date and time the `DbCredential` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this DbCredential.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbCredential.
        Date and time the `DbCredential` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this DbCredential.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_expires(self):
        """
        Gets the time_expires of this DbCredential.
        Date and time when this credential will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_expires of this DbCredential.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this DbCredential.
        Date and time when this credential will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_expires: The time_expires of this DbCredential.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DbCredential.
        The credential's current state. After creating a DB credential, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DbCredential.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbCredential.
        The credential's current state. After creating a DB credential, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this DbCredential.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DbCredential.
        The detailed status of INACTIVE lifecycleState.


        :return: The lifecycle_details of this DbCredential.
        :rtype: int
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DbCredential.
        The detailed status of INACTIVE lifecycleState.


        :param lifecycle_details: The lifecycle_details of this DbCredential.
        :type: int
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
