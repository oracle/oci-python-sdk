# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbCredentialSummary(object):
    """
    As the name suggests, an `DbCredentialSummary` object contains information about an `DbCredential`.
    The DB credential is used for DB authentication with
    the [DB Service].
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DbCredentialSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DbCredentialSummary.
        :type id: str

        :param user_id:
            The value to assign to the user_id property of this DbCredentialSummary.
        :type user_id: str

        :param description:
            The value to assign to the description property of this DbCredentialSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this DbCredentialSummary.
        :type time_created: datetime

        :param time_expires:
            The value to assign to the time_expires property of this DbCredentialSummary.
        :type time_expires: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbCredentialSummary.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'user_id': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'time_expires': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId',
            'description': 'description',
            'time_created': 'timeCreated',
            'time_expires': 'timeExpires',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._user_id = None
        self._description = None
        self._time_created = None
        self._time_expires = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        Gets the id of this DbCredentialSummary.
        The OCID of the DB credential.


        :return: The id of this DbCredentialSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbCredentialSummary.
        The OCID of the DB credential.


        :param id: The id of this DbCredentialSummary.
        :type: str
        """
        self._id = id

    @property
    def user_id(self):
        """
        Gets the user_id of this DbCredentialSummary.
        The OCID of the user the DB credential belongs to.


        :return: The user_id of this DbCredentialSummary.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this DbCredentialSummary.
        The OCID of the user the DB credential belongs to.


        :param user_id: The user_id of this DbCredentialSummary.
        :type: str
        """
        self._user_id = user_id

    @property
    def description(self):
        """
        Gets the description of this DbCredentialSummary.
        The description you assign to the DB credential. Does not have to be unique, and it's changeable.

        (For tenancies that support identity domains) You can have an empty description.


        :return: The description of this DbCredentialSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DbCredentialSummary.
        The description you assign to the DB credential. Does not have to be unique, and it's changeable.

        (For tenancies that support identity domains) You can have an empty description.


        :param description: The description of this DbCredentialSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        Gets the time_created of this DbCredentialSummary.
        Date and time the `DbCredential` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this DbCredentialSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbCredentialSummary.
        Date and time the `DbCredential` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this DbCredentialSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_expires(self):
        """
        Gets the time_expires of this DbCredentialSummary.
        Date and time when this credential will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_expires of this DbCredentialSummary.
        :rtype: datetime
        """
        return self._time_expires

    @time_expires.setter
    def time_expires(self, time_expires):
        """
        Sets the time_expires of this DbCredentialSummary.
        Date and time when this credential will expire, in the format defined by RFC3339.
        Null if it never expires.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_expires: The time_expires of this DbCredentialSummary.
        :type: datetime
        """
        self._time_expires = time_expires

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DbCredentialSummary.
        The credential's current state. After creating a DB credential, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.


        :return: The lifecycle_state of this DbCredentialSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbCredentialSummary.
        The credential's current state. After creating a DB credential, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this DbCredentialSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
