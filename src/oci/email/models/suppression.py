# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Suppression(object):
    """
    The full information representing an email suppression.
    """

    #: A constant which can be used with the reason property of a Suppression.
    #: This constant has a value of "UNKNOWN"
    REASON_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the reason property of a Suppression.
    #: This constant has a value of "HARDBOUNCE"
    REASON_HARDBOUNCE = "HARDBOUNCE"

    #: A constant which can be used with the reason property of a Suppression.
    #: This constant has a value of "COMPLAINT"
    REASON_COMPLAINT = "COMPLAINT"

    #: A constant which can be used with the reason property of a Suppression.
    #: This constant has a value of "MANUAL"
    REASON_MANUAL = "MANUAL"

    #: A constant which can be used with the reason property of a Suppression.
    #: This constant has a value of "SOFTBOUNCE"
    REASON_SOFTBOUNCE = "SOFTBOUNCE"

    #: A constant which can be used with the reason property of a Suppression.
    #: This constant has a value of "UNSUBSCRIBE"
    REASON_UNSUBSCRIBE = "UNSUBSCRIBE"

    def __init__(self, **kwargs):
        """
        Initializes a new Suppression object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Suppression.
        :type compartment_id: str

        :param email_address:
            The value to assign to the email_address property of this Suppression.
        :type email_address: str

        :param id:
            The value to assign to the id property of this Suppression.
        :type id: str

        :param reason:
            The value to assign to the reason property of this Suppression.
            Allowed values for this property are: "UNKNOWN", "HARDBOUNCE", "COMPLAINT", "MANUAL", "SOFTBOUNCE", "UNSUBSCRIBE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type reason: str

        :param time_created:
            The value to assign to the time_created property of this Suppression.
        :type time_created: datetime

        :param time_last_suppressed:
            The value to assign to the time_last_suppressed property of this Suppression.
        :type time_last_suppressed: datetime

        :param message_id:
            The value to assign to the message_id property of this Suppression.
        :type message_id: str

        :param error_detail:
            The value to assign to the error_detail property of this Suppression.
        :type error_detail: str

        :param error_source:
            The value to assign to the error_source property of this Suppression.
        :type error_source: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'email_address': 'str',
            'id': 'str',
            'reason': 'str',
            'time_created': 'datetime',
            'time_last_suppressed': 'datetime',
            'message_id': 'str',
            'error_detail': 'str',
            'error_source': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'email_address': 'emailAddress',
            'id': 'id',
            'reason': 'reason',
            'time_created': 'timeCreated',
            'time_last_suppressed': 'timeLastSuppressed',
            'message_id': 'messageId',
            'error_detail': 'errorDetail',
            'error_source': 'errorSource'
        }

        self._compartment_id = None
        self._email_address = None
        self._id = None
        self._reason = None
        self._time_created = None
        self._time_last_suppressed = None
        self._message_id = None
        self._error_detail = None
        self._error_source = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Suppression.
        The OCID of the compartment to contain the suppression. Since
        suppressions are at the customer level, this must be the tenancy
        OCID.


        :return: The compartment_id of this Suppression.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Suppression.
        The OCID of the compartment to contain the suppression. Since
        suppressions are at the customer level, this must be the tenancy
        OCID.


        :param compartment_id: The compartment_id of this Suppression.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def email_address(self):
        """
        **[Required]** Gets the email_address of this Suppression.
        Email address of the suppression.


        :return: The email_address of this Suppression.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this Suppression.
        Email address of the suppression.


        :param email_address: The email_address of this Suppression.
        :type: str
        """
        self._email_address = email_address

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Suppression.
        The unique ID of the suppression.


        :return: The id of this Suppression.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Suppression.
        The unique ID of the suppression.


        :param id: The id of this Suppression.
        :type: str
        """
        self._id = id

    @property
    def reason(self):
        """
        Gets the reason of this Suppression.
        The reason that the email address was suppressed. For more information on the types of bounces, see `Suppression List`__.

        __ https://docs.cloud.oracle.com/Content/Email/Concepts/overview.htm#components

        Allowed values for this property are: "UNKNOWN", "HARDBOUNCE", "COMPLAINT", "MANUAL", "SOFTBOUNCE", "UNSUBSCRIBE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The reason of this Suppression.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this Suppression.
        The reason that the email address was suppressed. For more information on the types of bounces, see `Suppression List`__.

        __ https://docs.cloud.oracle.com/Content/Email/Concepts/overview.htm#components


        :param reason: The reason of this Suppression.
        :type: str
        """
        allowed_values = ["UNKNOWN", "HARDBOUNCE", "COMPLAINT", "MANUAL", "SOFTBOUNCE", "UNSUBSCRIBE"]
        if not value_allowed_none_or_none_sentinel(reason, allowed_values):
            reason = 'UNKNOWN_ENUM_VALUE'
        self._reason = reason

    @property
    def time_created(self):
        """
        Gets the time_created of this Suppression.
        The date and time the suppression was added in \"YYYY-MM-ddThh:mmZ\"
        format with a Z offset, as defined by RFC 3339.


        :return: The time_created of this Suppression.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Suppression.
        The date and time the suppression was added in \"YYYY-MM-ddThh:mmZ\"
        format with a Z offset, as defined by RFC 3339.


        :param time_created: The time_created of this Suppression.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_last_suppressed(self):
        """
        Gets the time_last_suppressed of this Suppression.
        The last date and time the suppression prevented submission
        in \"YYYY-MM-ddThh:mmZ\"
        format with a Z offset, as defined by RFC 3339.


        :return: The time_last_suppressed of this Suppression.
        :rtype: datetime
        """
        return self._time_last_suppressed

    @time_last_suppressed.setter
    def time_last_suppressed(self, time_last_suppressed):
        """
        Sets the time_last_suppressed of this Suppression.
        The last date and time the suppression prevented submission
        in \"YYYY-MM-ddThh:mmZ\"
        format with a Z offset, as defined by RFC 3339.


        :param time_last_suppressed: The time_last_suppressed of this Suppression.
        :type: datetime
        """
        self._time_last_suppressed = time_last_suppressed

    @property
    def message_id(self):
        """
        Gets the message_id of this Suppression.
        The value of the Message-ID header from the email that triggered a suppression.
        This value is as defined in RFC 5322 section 3.6.4, excluding angle-brackets.
        Not provided for all types of suppressions.


        :return: The message_id of this Suppression.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """
        Sets the message_id of this Suppression.
        The value of the Message-ID header from the email that triggered a suppression.
        This value is as defined in RFC 5322 section 3.6.4, excluding angle-brackets.
        Not provided for all types of suppressions.


        :param message_id: The message_id of this Suppression.
        :type: str
        """
        self._message_id = message_id

    @property
    def error_detail(self):
        """
        Gets the error_detail of this Suppression.
        The specific error message returned by a system that resulted in the suppression.
        This message is usually an SMTP error code with additional descriptive text.
        Not provided for all types of suppressions.


        :return: The error_detail of this Suppression.
        :rtype: str
        """
        return self._error_detail

    @error_detail.setter
    def error_detail(self, error_detail):
        """
        Sets the error_detail of this Suppression.
        The specific error message returned by a system that resulted in the suppression.
        This message is usually an SMTP error code with additional descriptive text.
        Not provided for all types of suppressions.


        :param error_detail: The error_detail of this Suppression.
        :type: str
        """
        self._error_detail = error_detail

    @property
    def error_source(self):
        """
        Gets the error_source of this Suppression.
        DNS name of the source of the error that caused the suppression.
        Will be set to either the remote-mta or reporting-mta field from a delivery status notification (RFC 3464) when available.
        Not provided for all types of suppressions, and not always known.

        Note: Most SMTP errors that cause suppressions come from software run by email receiving systems rather than from OCI email delivery itself.


        :return: The error_source of this Suppression.
        :rtype: str
        """
        return self._error_source

    @error_source.setter
    def error_source(self, error_source):
        """
        Sets the error_source of this Suppression.
        DNS name of the source of the error that caused the suppression.
        Will be set to either the remote-mta or reporting-mta field from a delivery status notification (RFC 3464) when available.
        Not provided for all types of suppressions, and not always known.

        Note: Most SMTP errors that cause suppressions come from software run by email receiving systems rather than from OCI email delivery itself.


        :param error_source: The error_source of this Suppression.
        :type: str
        """
        self._error_source = error_source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
