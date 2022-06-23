# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Promotion(object):
    """
    Promotion information for a subscription.
    """

    #: A constant which can be used with the status property of a Promotion.
    #: This constant has a value of "INITIALIZED"
    STATUS_INITIALIZED = "INITIALIZED"

    #: A constant which can be used with the status property of a Promotion.
    #: This constant has a value of "ACTIVE"
    STATUS_ACTIVE = "ACTIVE"

    #: A constant which can be used with the status property of a Promotion.
    #: This constant has a value of "EXPIRED"
    STATUS_EXPIRED = "EXPIRED"

    def __init__(self, **kwargs):
        """
        Initializes a new Promotion object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param duration:
            The value to assign to the duration property of this Promotion.
        :type duration: int

        :param duration_unit:
            The value to assign to the duration_unit property of this Promotion.
        :type duration_unit: str

        :param amount:
            The value to assign to the amount property of this Promotion.
        :type amount: float

        :param status:
            The value to assign to the status property of this Promotion.
            Allowed values for this property are: "INITIALIZED", "ACTIVE", "EXPIRED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type status: str

        :param is_intent_to_pay:
            The value to assign to the is_intent_to_pay property of this Promotion.
        :type is_intent_to_pay: bool

        :param currency_unit:
            The value to assign to the currency_unit property of this Promotion.
        :type currency_unit: str

        :param time_started:
            The value to assign to the time_started property of this Promotion.
        :type time_started: datetime

        :param time_expired:
            The value to assign to the time_expired property of this Promotion.
        :type time_expired: datetime

        """
        self.swagger_types = {
            'duration': 'int',
            'duration_unit': 'str',
            'amount': 'float',
            'status': 'str',
            'is_intent_to_pay': 'bool',
            'currency_unit': 'str',
            'time_started': 'datetime',
            'time_expired': 'datetime'
        }

        self.attribute_map = {
            'duration': 'duration',
            'duration_unit': 'durationUnit',
            'amount': 'amount',
            'status': 'status',
            'is_intent_to_pay': 'isIntentToPay',
            'currency_unit': 'currencyUnit',
            'time_started': 'timeStarted',
            'time_expired': 'timeExpired'
        }

        self._duration = None
        self._duration_unit = None
        self._amount = None
        self._status = None
        self._is_intent_to_pay = None
        self._currency_unit = None
        self._time_started = None
        self._time_expired = None

    @property
    def duration(self):
        """
        Gets the duration of this Promotion.
        How long the promotion related to the subscription, if any, is valid in duration units.


        :return: The duration of this Promotion.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this Promotion.
        How long the promotion related to the subscription, if any, is valid in duration units.


        :param duration: The duration of this Promotion.
        :type: int
        """
        self._duration = duration

    @property
    def duration_unit(self):
        """
        Gets the duration_unit of this Promotion.
        Unit for the duration.


        :return: The duration_unit of this Promotion.
        :rtype: str
        """
        return self._duration_unit

    @duration_unit.setter
    def duration_unit(self, duration_unit):
        """
        Sets the duration_unit of this Promotion.
        Unit for the duration.


        :param duration_unit: The duration_unit of this Promotion.
        :type: str
        """
        self._duration_unit = duration_unit

    @property
    def amount(self):
        """
        Gets the amount of this Promotion.
        Total amount of credit for the promotion related to the subscription if there is one.


        :return: The amount of this Promotion.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this Promotion.
        Total amount of credit for the promotion related to the subscription if there is one.


        :param amount: The amount of this Promotion.
        :type: float
        """
        self._amount = amount

    @property
    def status(self):
        """
        Gets the status of this Promotion.
        Current status of the promotion related to the subscription if there is one.

        Allowed values for this property are: "INITIALIZED", "ACTIVE", "EXPIRED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The status of this Promotion.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Promotion.
        Current status of the promotion related to the subscription if there is one.


        :param status: The status of this Promotion.
        :type: str
        """
        allowed_values = ["INITIALIZED", "ACTIVE", "EXPIRED"]
        if not value_allowed_none_or_none_sentinel(status, allowed_values):
            status = 'UNKNOWN_ENUM_VALUE'
        self._status = status

    @property
    def is_intent_to_pay(self):
        """
        Gets the is_intent_to_pay of this Promotion.
        Whether or not customer intends to pay once the promotion is done.


        :return: The is_intent_to_pay of this Promotion.
        :rtype: bool
        """
        return self._is_intent_to_pay

    @is_intent_to_pay.setter
    def is_intent_to_pay(self, is_intent_to_pay):
        """
        Sets the is_intent_to_pay of this Promotion.
        Whether or not customer intends to pay once the promotion is done.


        :param is_intent_to_pay: The is_intent_to_pay of this Promotion.
        :type: bool
        """
        self._is_intent_to_pay = is_intent_to_pay

    @property
    def currency_unit(self):
        """
        Gets the currency_unit of this Promotion.
        Currency unit associated with the promotion.


        :return: The currency_unit of this Promotion.
        :rtype: str
        """
        return self._currency_unit

    @currency_unit.setter
    def currency_unit(self, currency_unit):
        """
        Sets the currency_unit of this Promotion.
        Currency unit associated with the promotion.


        :param currency_unit: The currency_unit of this Promotion.
        :type: str
        """
        self._currency_unit = currency_unit

    @property
    def time_started(self):
        """
        Gets the time_started of this Promotion.
        Date-time for when the promotion starts.


        :return: The time_started of this Promotion.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this Promotion.
        Date-time for when the promotion starts.


        :param time_started: The time_started of this Promotion.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_expired(self):
        """
        Gets the time_expired of this Promotion.
        Date-time for when the promotion ends.


        :return: The time_expired of this Promotion.
        :rtype: datetime
        """
        return self._time_expired

    @time_expired.setter
    def time_expired(self, time_expired):
        """
        Sets the time_expired of this Promotion.
        Date-time for when the promotion ends.


        :param time_expired: The time_expired of this Promotion.
        :type: datetime
        """
        self._time_expired = time_expired

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
