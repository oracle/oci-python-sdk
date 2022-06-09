# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Commitment(object):
    """
    Subscribed Service commitment summary
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Commitment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Commitment.
        :type id: str

        :param subscribed_service_id:
            The value to assign to the subscribed_service_id property of this Commitment.
        :type subscribed_service_id: str

        :param time_start:
            The value to assign to the time_start property of this Commitment.
        :type time_start: datetime

        :param time_end:
            The value to assign to the time_end property of this Commitment.
        :type time_end: datetime

        :param quantity:
            The value to assign to the quantity property of this Commitment.
        :type quantity: str

        :param used_amount:
            The value to assign to the used_amount property of this Commitment.
        :type used_amount: str

        :param available_amount:
            The value to assign to the available_amount property of this Commitment.
        :type available_amount: str

        :param funded_allocation_value:
            The value to assign to the funded_allocation_value property of this Commitment.
        :type funded_allocation_value: str

        """
        self.swagger_types = {
            'id': 'str',
            'subscribed_service_id': 'str',
            'time_start': 'datetime',
            'time_end': 'datetime',
            'quantity': 'str',
            'used_amount': 'str',
            'available_amount': 'str',
            'funded_allocation_value': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'subscribed_service_id': 'subscribedServiceId',
            'time_start': 'timeStart',
            'time_end': 'timeEnd',
            'quantity': 'quantity',
            'used_amount': 'usedAmount',
            'available_amount': 'availableAmount',
            'funded_allocation_value': 'fundedAllocationValue'
        }

        self._id = None
        self._subscribed_service_id = None
        self._time_start = None
        self._time_end = None
        self._quantity = None
        self._used_amount = None
        self._available_amount = None
        self._funded_allocation_value = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Commitment.
        SPM internal Commitment ID


        :return: The id of this Commitment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Commitment.
        SPM internal Commitment ID


        :param id: The id of this Commitment.
        :type: str
        """
        self._id = id

    @property
    def subscribed_service_id(self):
        """
        Gets the subscribed_service_id of this Commitment.
        SPM internal Subscribed Service ID


        :return: The subscribed_service_id of this Commitment.
        :rtype: str
        """
        return self._subscribed_service_id

    @subscribed_service_id.setter
    def subscribed_service_id(self, subscribed_service_id):
        """
        Sets the subscribed_service_id of this Commitment.
        SPM internal Subscribed Service ID


        :param subscribed_service_id: The subscribed_service_id of this Commitment.
        :type: str
        """
        self._subscribed_service_id = subscribed_service_id

    @property
    def time_start(self):
        """
        Gets the time_start of this Commitment.
        Commitment start date


        :return: The time_start of this Commitment.
        :rtype: datetime
        """
        return self._time_start

    @time_start.setter
    def time_start(self, time_start):
        """
        Sets the time_start of this Commitment.
        Commitment start date


        :param time_start: The time_start of this Commitment.
        :type: datetime
        """
        self._time_start = time_start

    @property
    def time_end(self):
        """
        Gets the time_end of this Commitment.
        Commitment end date


        :return: The time_end of this Commitment.
        :rtype: datetime
        """
        return self._time_end

    @time_end.setter
    def time_end(self, time_end):
        """
        Sets the time_end of this Commitment.
        Commitment end date


        :param time_end: The time_end of this Commitment.
        :type: datetime
        """
        self._time_end = time_end

    @property
    def quantity(self):
        """
        Gets the quantity of this Commitment.
        Commitment quantity


        :return: The quantity of this Commitment.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this Commitment.
        Commitment quantity


        :param quantity: The quantity of this Commitment.
        :type: str
        """
        self._quantity = quantity

    @property
    def used_amount(self):
        """
        Gets the used_amount of this Commitment.
        Commitment used amount


        :return: The used_amount of this Commitment.
        :rtype: str
        """
        return self._used_amount

    @used_amount.setter
    def used_amount(self, used_amount):
        """
        Sets the used_amount of this Commitment.
        Commitment used amount


        :param used_amount: The used_amount of this Commitment.
        :type: str
        """
        self._used_amount = used_amount

    @property
    def available_amount(self):
        """
        Gets the available_amount of this Commitment.
        Commitment available amount


        :return: The available_amount of this Commitment.
        :rtype: str
        """
        return self._available_amount

    @available_amount.setter
    def available_amount(self, available_amount):
        """
        Sets the available_amount of this Commitment.
        Commitment available amount


        :param available_amount: The available_amount of this Commitment.
        :type: str
        """
        self._available_amount = available_amount

    @property
    def funded_allocation_value(self):
        """
        Gets the funded_allocation_value of this Commitment.
        Funded Allocation line value
        example: 12000.00


        :return: The funded_allocation_value of this Commitment.
        :rtype: str
        """
        return self._funded_allocation_value

    @funded_allocation_value.setter
    def funded_allocation_value(self, funded_allocation_value):
        """
        Sets the funded_allocation_value of this Commitment.
        Funded Allocation line value
        example: 12000.00


        :param funded_allocation_value: The funded_allocation_value of this Commitment.
        :type: str
        """
        self._funded_allocation_value = funded_allocation_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
