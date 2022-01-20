# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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

        :param id:
            The value to assign to the id property of this SubscriptionSummary.
        :type id: str

        :param service_name:
            The value to assign to the service_name property of this SubscriptionSummary.
        :type service_name: str

        :param type:
            The value to assign to the type property of this SubscriptionSummary.
        :type type: str

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
        :type currency: oci.osub_organization_subscription.models.Currency

        :param total_value:
            The value to assign to the total_value property of this SubscriptionSummary.
        :type total_value: str

        """
        self.swagger_types = {
            'id': 'str',
            'service_name': 'str',
            'type': 'str',
            'status': 'str',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'currency': 'Currency',
            'total_value': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'service_name': 'serviceName',
            'type': 'type',
            'status': 'status',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'currency': 'currency',
            'total_value': 'totalValue'
        }

        self._id = None
        self._service_name = None
        self._type = None
        self._status = None
        self._time_start = None
        self._time_end = None
        self._currency = None
        self._total_value = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SubscriptionSummary.
        SPM internal Subscription ID


        :return: The id of this SubscriptionSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SubscriptionSummary.
        SPM internal Subscription ID


        :param id: The id of this SubscriptionSummary.
        :type: str
        """
        self._id = id

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
    def type(self):
        """
        Gets the type of this SubscriptionSummary.
        Subscription Type i.e. IAAS,SAAS,PAAS


        :return: The type of this SubscriptionSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SubscriptionSummary.
        Subscription Type i.e. IAAS,SAAS,PAAS


        :param type: The type of this SubscriptionSummary.
        :type: str
        """
        self._type = type

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
        :rtype: oci.osub_organization_subscription.models.Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this SubscriptionSummary.

        :param currency: The currency of this SubscriptionSummary.
        :type: oci.osub_organization_subscription.models.Currency
        """
        self._currency = currency

    @property
    def total_value(self):
        """
        Gets the total_value of this SubscriptionSummary.
        Total aggregate TCLV of all lines for the subscription including expired, active, and signed


        :return: The total_value of this SubscriptionSummary.
        :rtype: str
        """
        return self._total_value

    @total_value.setter
    def total_value(self, total_value):
        """
        Sets the total_value of this SubscriptionSummary.
        Total aggregate TCLV of all lines for the subscription including expired, active, and signed


        :param total_value: The total_value of this SubscriptionSummary.
        :type: str
        """
        self._total_value = total_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
