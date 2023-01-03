# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubscriptionSummary(object):
    """
    Subscription summary
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubscriptionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param status:
            The value to assign to the status property of this SubscriptionSummary.
        :type status: str

        :param time_start:
            The value to assign to the time_start property of this SubscriptionSummary.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this SubscriptionSummary.
        :type time_end: datetime

        :param currency:
            The value to assign to the currency property of this SubscriptionSummary.
        :type currency: oci.osub_subscription.models.Currency

        :param service_name:
            The value to assign to the service_name property of this SubscriptionSummary.
        :type service_name: str

        :param subscribed_services:
            The value to assign to the subscribed_services property of this SubscriptionSummary.
        :type subscribed_services: list[oci.osub_subscription.models.SubscribedServiceSummary]

        """
        self.swagger_types = {
            'status': 'str',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'currency': 'Currency',
            'service_name': 'str',
            'subscribed_services': 'list[SubscribedServiceSummary]'
        }

        self.attribute_map = {
            'status': 'status',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'currency': 'currency',
            'service_name': 'serviceName',
            'subscribed_services': 'subscribedServices'
        }

        self._status = None
        self._time_start = None
        self._time_end = None
        self._currency = None
        self._service_name = None
        self._subscribed_services = None

    @property
    def status(self):
        """
        Gets the status of this SubscriptionSummary.
        Status of the plan


        :return: The status of this SubscriptionSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this SubscriptionSummary.
        Status of the plan


        :param status: The status of this SubscriptionSummary.
        :type: str
        """
        self._status = status

    @property
    def time_start(self):
        """
        Gets the time_start of this SubscriptionSummary.
        Represents the date when the first service of the subscription was activated


        :return: The time_start of this SubscriptionSummary.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this SubscriptionSummary.
        Represents the date when the first service of the subscription was activated


        :param time_start: The time_start of this SubscriptionSummary.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this SubscriptionSummary.
        Represents the date when the last service of the subscription ends


        :return: The time_end of this SubscriptionSummary.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this SubscriptionSummary.
        Represents the date when the last service of the subscription ends


        :param time_end: The time_end of this SubscriptionSummary.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def currency(self):
        """
        Gets the currency of this SubscriptionSummary.

        :return: The currency of this SubscriptionSummary.
        :rtype: oci.osub_subscription.models.Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this SubscriptionSummary.

        :param currency: The currency of this SubscriptionSummary.
        :type: oci.osub_subscription.models.Currency
        """
        self._currency = currency

    @property
    def service_name(self):
        """
        Gets the service_name of this SubscriptionSummary.
        Customer friendly service name provided by PRG


        :return: The service_name of this SubscriptionSummary.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this SubscriptionSummary.
        Customer friendly service name provided by PRG


        :param service_name: The service_name of this SubscriptionSummary.
        :type: str
        """
        self._service_name = service_name

    @property
    def subscribed_services(self):
        """
        Gets the subscribed_services of this SubscriptionSummary.
        List of Subscribed Services of the plan


        :return: The subscribed_services of this SubscriptionSummary.
        :rtype: list[oci.osub_subscription.models.SubscribedServiceSummary]
        """
        return self._subscribed_services

    @subscribed_services.setter
    def subscribed_services(self, subscribed_services):
        """
        Sets the subscribed_services of this SubscriptionSummary.
        List of Subscribed Services of the plan


        :param subscribed_services: The subscribed_services of this SubscriptionSummary.
        :type: list[oci.osub_subscription.models.SubscribedServiceSummary]
        """
        self._subscribed_services = subscribed_services

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
