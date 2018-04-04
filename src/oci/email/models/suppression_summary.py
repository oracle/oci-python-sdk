# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SuppressionSummary(object):
    """
    The full information representing a suppression.
    """

    #: A constant which can be used with the reason property of a SuppressionSummary.
    #: This constant has a value of "UNKNOWN"
    REASON_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the reason property of a SuppressionSummary.
    #: This constant has a value of "HARDBOUNCE"
    REASON_HARDBOUNCE = "HARDBOUNCE"

    #: A constant which can be used with the reason property of a SuppressionSummary.
    #: This constant has a value of "COMPLAINT"
    REASON_COMPLAINT = "COMPLAINT"

    #: A constant which can be used with the reason property of a SuppressionSummary.
    #: This constant has a value of "MANUAL"
    REASON_MANUAL = "MANUAL"

    #: A constant which can be used with the reason property of a SuppressionSummary.
    #: This constant has a value of "SOFTBOUNCE"
    REASON_SOFTBOUNCE = "SOFTBOUNCE"

    #: A constant which can be used with the reason property of a SuppressionSummary.
    #: This constant has a value of "UNSUBSCRIBE"
    REASON_UNSUBSCRIBE = "UNSUBSCRIBE"

    def __init__(self, **kwargs):
        """
        Initializes a new SuppressionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param email_address:
            The value to assign to the email_address property of this SuppressionSummary.
        :type email_address: str

        :param id:
            The value to assign to the id property of this SuppressionSummary.
        :type id: str

        :param reason:
            The value to assign to the reason property of this SuppressionSummary.
            Allowed values for this property are: "UNKNOWN", "HARDBOUNCE", "COMPLAINT", "MANUAL", "SOFTBOUNCE", "UNSUBSCRIBE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type reason: str

        :param time_created:
            The value to assign to the time_created property of this SuppressionSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'email_address': 'str',
            'id': 'str',
            'reason': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'email_address': 'emailAddress',
            'id': 'id',
            'reason': 'reason',
            'time_created': 'timeCreated'
        }

        self._email_address = None
        self._id = None
        self._reason = None
        self._time_created = None

    @property
    def email_address(self):
        """
        Gets the email_address of this SuppressionSummary.
        The email address of the suppression.


        :return: The email_address of this SuppressionSummary.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this SuppressionSummary.
        The email address of the suppression.


        :param email_address: The email_address of this SuppressionSummary.
        :type: str
        """
        self._email_address = email_address

    @property
    def id(self):
        """
        Gets the id of this SuppressionSummary.
        The unique OCID of the suppression.


        :return: The id of this SuppressionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SuppressionSummary.
        The unique OCID of the suppression.


        :param id: The id of this SuppressionSummary.
        :type: str
        """
        self._id = id

    @property
    def reason(self):
        """
        Gets the reason of this SuppressionSummary.
        The reason that the email address was suppressed.

        Allowed values for this property are: "UNKNOWN", "HARDBOUNCE", "COMPLAINT", "MANUAL", "SOFTBOUNCE", "UNSUBSCRIBE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The reason of this SuppressionSummary.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this SuppressionSummary.
        The reason that the email address was suppressed.


        :param reason: The reason of this SuppressionSummary.
        :type: str
        """
        allowed_values = ["UNKNOWN", "HARDBOUNCE", "COMPLAINT", "MANUAL", "SOFTBOUNCE", "UNSUBSCRIBE"]
        if not value_allowed_none_or_none_sentinel(reason, allowed_values):
            reason = 'UNKNOWN_ENUM_VALUE'
        self._reason = reason

    @property
    def time_created(self):
        """
        Gets the time_created of this SuppressionSummary.
        The date and time a recipient's email address was added to the
        suppression list, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as
        defined by RFC 3339.


        :return: The time_created of this SuppressionSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SuppressionSummary.
        The date and time a recipient's email address was added to the
        suppression list, in \"YYYY-MM-ddThh:mmZ\" format with a Z offset, as
        defined by RFC 3339.


        :param time_created: The time_created of this SuppressionSummary.
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
