# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiKey(object):
    """
    A PEM-format RSA credential for securing requests to the Oracle Cloud Infrastructure REST API. Also known
    as an *API signing key*. Specifically, this is the public key from the key pair. The private key remains with
    the user calling the API. For information about generating a key pair
    in the required PEM format, see `Required Keys and OCIDs`__.

    **Important:** This is **not** the SSH key for accessing compute instances.

    Each user can have a maximum of three API signing keys.

    For more information about user credentials, see `User Credentials`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm
    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/usercredentials.htm
    """

    #: A constant which can be used with the lifecycle_state property of a ApiKey.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ApiKey.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ApiKey.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ApiKey.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ApiKey.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ApiKey object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_id:
            The value to assign to the key_id property of this ApiKey.
        :type key_id: str

        :param key_value:
            The value to assign to the key_value property of this ApiKey.
        :type key_value: str

        :param fingerprint:
            The value to assign to the fingerprint property of this ApiKey.
        :type fingerprint: str

        :param user_id:
            The value to assign to the user_id property of this ApiKey.
        :type user_id: str

        :param time_created:
            The value to assign to the time_created property of this ApiKey.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ApiKey.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param inactive_status:
            The value to assign to the inactive_status property of this ApiKey.
        :type inactive_status: int

        """
        self.swagger_types = {
            'key_id': 'str',
            'key_value': 'str',
            'fingerprint': 'str',
            'user_id': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'inactive_status': 'int'
        }

        self.attribute_map = {
            'key_id': 'keyId',
            'key_value': 'keyValue',
            'fingerprint': 'fingerprint',
            'user_id': 'userId',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'inactive_status': 'inactiveStatus'
        }

        self._key_id = None
        self._key_value = None
        self._fingerprint = None
        self._user_id = None
        self._time_created = None
        self._lifecycle_state = None
        self._inactive_status = None

    @property
    def key_id(self):
        """
        Gets the key_id of this ApiKey.
        An Oracle-assigned identifier for the key, in this format:
        TENANCY_OCID/USER_OCID/KEY_FINGERPRINT.


        :return: The key_id of this ApiKey.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this ApiKey.
        An Oracle-assigned identifier for the key, in this format:
        TENANCY_OCID/USER_OCID/KEY_FINGERPRINT.


        :param key_id: The key_id of this ApiKey.
        :type: str
        """
        self._key_id = key_id

    @property
    def key_value(self):
        """
        Gets the key_value of this ApiKey.
        The key's value.


        :return: The key_value of this ApiKey.
        :rtype: str
        """
        return self._key_value

    @key_value.setter
    def key_value(self, key_value):
        """
        Sets the key_value of this ApiKey.
        The key's value.


        :param key_value: The key_value of this ApiKey.
        :type: str
        """
        self._key_value = key_value

    @property
    def fingerprint(self):
        """
        Gets the fingerprint of this ApiKey.
        The key's fingerprint (e.g., 12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef).


        :return: The fingerprint of this ApiKey.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this ApiKey.
        The key's fingerprint (e.g., 12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef).


        :param fingerprint: The fingerprint of this ApiKey.
        :type: str
        """
        self._fingerprint = fingerprint

    @property
    def user_id(self):
        """
        Gets the user_id of this ApiKey.
        The OCID of the user the key belongs to.


        :return: The user_id of this ApiKey.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ApiKey.
        The OCID of the user the key belongs to.


        :param user_id: The user_id of this ApiKey.
        :type: str
        """
        self._user_id = user_id

    @property
    def time_created(self):
        """
        Gets the time_created of this ApiKey.
        Date and time the `ApiKey` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this ApiKey.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ApiKey.
        Date and time the `ApiKey` object was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this ApiKey.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this ApiKey.
        The API key's current state. After creating an `ApiKey` object, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ApiKey.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ApiKey.
        The API key's current state. After creating an `ApiKey` object, make sure its `lifecycleState` changes from
        CREATING to ACTIVE before using it.


        :param lifecycle_state: The lifecycle_state of this ApiKey.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def inactive_status(self):
        """
        Gets the inactive_status of this ApiKey.
        The detailed status of INACTIVE lifecycleState.


        :return: The inactive_status of this ApiKey.
        :rtype: int
        """
        return self._inactive_status

    @inactive_status.setter
    def inactive_status(self, inactive_status):
        """
        Sets the inactive_status of this ApiKey.
        The detailed status of INACTIVE lifecycleState.


        :param inactive_status: The inactive_status of this ApiKey.
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
