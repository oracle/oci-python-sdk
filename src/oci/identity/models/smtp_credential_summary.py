# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SmtpCredentialSummary(object):
    """
    As the name suggests, an `SmtpCredentialSummary` object contains information about an `SmtpCredential`.
    The SMTP credential is used for SMTP authentication with
    the `Email Delivery Service`__.

    __ https://docs.cloud.oracle.com/Content/Email/Concepts/overview.htm
    """

    #: A constant which can be used with the lifecycle_state property of a SmtpCredentialSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SmtpCredentialSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SmtpCredentialSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SmtpCredentialSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SmtpCredentialSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new SmtpCredentialSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param username:
            The value to assign to the username property of this SmtpCredentialSummary.
        :type username: str

        :param id:
            The value to assign to the id property of this SmtpCredentialSummary.
        :type id: str

        :param user_id:
            The value to assign to the user_id property of this SmtpCredentialSummary.
        :type user_id: str

        :param description:
            The value to assign to the description property of this SmtpCredentialSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this SmtpCredentialSummary.
        :type time_created: datetime

        :param time_expires:
            The value to assign to the time_expires property of this SmtpCredentialSummary.
        :type time_expires: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SmtpCredentialSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this SmtpCredentialSummary.
        :type inactive_status: int

        """
        self.swagger_types = {
            'username': 'str',
            'id': 'str',
            'user_id': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_expires': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int'
        }

        self.attribute_map = {
            'username': 'username',
            'id': 'id',
            'user_id': 'userId',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_expires': 'timeExpires',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus'
        }

        self._username = None
        self._id = None
        self._user_id = None
        self._description = None
        self._time_created = None
        self._time_expires = None
        self._lifecycle_state = None
        self._inactive_status = None

    @property
    def username(self):
        """
        Gets the username of this SmtpCredentialSummary.
        The SMTP user name.


        :return: The username of this SmtpCredentialSummary.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this SmtpCredentialSummary.
        The SMTP user name.


        :param username: The username of this SmtpCredentialSummary.
        :type: str
        """
        self._username = username

    @property
    def id(self):
        """
        Gets the id of this SmtpCredentialSummary.
        The OCID of the SMTP credential.


        :return: The id of this SmtpCredentialSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SmtpCredentialSummary.
        The OCID of the SMTP credential.


        :param id: The id of this SmtpCredentialSummary.
        :type: str
        """
        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this SmtpCredentialSummary.
        The OCID of the user the SMTP credential belongs to.


        :return: The user_id of this SmtpCredentialSummary.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this SmtpCredentialSummary.
        The OCID of the user the SMTP credential belongs to.


        :param user_id: The user_id of this SmtpCredentialSummary.
        :type: str
        """
        self._user_id = user_id

    @property
    def description(self):
        """
        Gets the description of this SmtpCredentialSummary.
        The description you assign to the SMTP credential. Does not have to be unique, and it's changeable.


        :return: The description of this SmtpCredentialSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SmtpCredentialSummary.
        The description you assign to the SMTP credential. Does not have to be unique, and it's changeable.


        :param description: The description of this SmtpCredentialSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this SmtpCredentialSummary.
        Date and time the `SmtpCredential` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this SmtpCredentialSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SmtpCredentialSummary.
        Date and time the `SmtpCredential` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this SmtpCredentialSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_expires(self):
        """
        Gets the time_expires of this SmtpCredentialSummary.
        Date and time when this credential will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_expires of this SmtpCredentialSummary.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this SmtpCredentialSummary.
        Date and time when this credential will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_expires: The time_expires of this SmtpCredentialSummary.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SmtpCredentialSummary.
        The credential's current state. After creating a SMTP credential, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SmtpCredentialSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SmtpCredentialSummary.
        The credential's current state. After creating a SMTP credential, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this SmtpCredentialSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this SmtpCredentialSummary.
        The detailed status of INACTIVE lifecycleState.


        :return: The inactive_status of this SmtpCredentialSummary.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this SmtpCredentialSummary.
        The detailed status of INACTIVE lifecycleState.


        :param inactive_status: The inactive_status of this SmtpCredentialSummary.
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
