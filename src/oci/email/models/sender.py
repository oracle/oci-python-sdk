# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Sender(object):

    def __init__(self, **kwargs):
        """
        Initializes a new Sender object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param email_address:
            The value to assign to the email_address property of this Sender.
        :type email_address: str

        :param id:
            The value to assign to the id property of this Sender.
        :type id: str

        :param is_spf:
            The value to assign to the is_spf property of this Sender.
        :type is_spf: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Sender.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Sender.
        :type time_created: datetime

        """
        self.swagger_types = {
            'email_address': 'str',
            'id': 'str',
            'is_spf': 'bool',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'email_address': 'emailAddress',
            'id': 'id',
            'is_spf': 'isSpf',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }

        self._email_address = None
        self._id = None
        self._is_spf = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def email_address(self):
        """
        Gets the email_address of this Sender.
        Email address of the sender.


        :return: The email_address of this Sender.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this Sender.
        Email address of the sender.


        :param email_address: The email_address of this Sender.
        :type: str
        """
        self._email_address = email_address

    @property
    def id(self):
        """
        Gets the id of this Sender.
        The unique OCID of the sender.


        :return: The id of this Sender.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Sender.
        The unique OCID of the sender.


        :param id: The id of this Sender.
        :type: str
        """
        self._id = id

    @property
    def is_spf(self):
        """
        Gets the is_spf of this Sender.
        Value of the SPF field. For more information about SPF, please see
        `SPF Authentication`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Email/Concepts/emaildeliveryoverview.htm#spf


        :return: The is_spf of this Sender.
        :rtype: bool
        """
        return self._is_spf

    @is_spf.setter
    def is_spf(self, is_spf):
        """
        Sets the is_spf of this Sender.
        Value of the SPF field. For more information about SPF, please see
        `SPF Authentication`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Email/Concepts/emaildeliveryoverview.htm#spf


        :param is_spf: The is_spf of this Sender.
        :type: bool
        """
        self._is_spf = is_spf

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Sender.
        The sender's current lifecycle state.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Sender.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Sender.
        The sender's current lifecycle state.


        :param lifecycle_state: The lifecycle_state of this Sender.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this Sender.
        The date and time the approved sender was added in \"YYYY-MM-ddThh:mmZ\"
        format with a Z offset, as defined by RFC 3339.


        :return: The time_created of this Sender.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Sender.
        The date and time the approved sender was added in \"YYYY-MM-ddThh:mmZ\"
        format with a Z offset, as defined by RFC 3339.


        :param time_created: The time_created of this Sender.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
