# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTransferApplianceDetails(object):
    """
    UpdateTransferApplianceDetails model.
    """

    #: A constant which can be used with the lifecycle_state property of a UpdateTransferApplianceDetails.
    #: This constant has a value of "PREPARING"
    LIFECYCLE_STATE_PREPARING = "PREPARING"

    #: A constant which can be used with the lifecycle_state property of a UpdateTransferApplianceDetails.
    #: This constant has a value of "FINALIZED"
    LIFECYCLE_STATE_FINALIZED = "FINALIZED"

    #: A constant which can be used with the lifecycle_state property of a UpdateTransferApplianceDetails.
    #: This constant has a value of "RETURN_LABEL_REQUESTED"
    LIFECYCLE_STATE_RETURN_LABEL_REQUESTED = "RETURN_LABEL_REQUESTED"

    #: A constant which can be used with the lifecycle_state property of a UpdateTransferApplianceDetails.
    #: This constant has a value of "RETURN_LABEL_GENERATING"
    LIFECYCLE_STATE_RETURN_LABEL_GENERATING = "RETURN_LABEL_GENERATING"

    #: A constant which can be used with the lifecycle_state property of a UpdateTransferApplianceDetails.
    #: This constant has a value of "RETURN_LABEL_AVAILABLE"
    LIFECYCLE_STATE_RETURN_LABEL_AVAILABLE = "RETURN_LABEL_AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a UpdateTransferApplianceDetails.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a UpdateTransferApplianceDetails.
    #: This constant has a value of "CUSTOMER_NEVER_RECEIVED"
    LIFECYCLE_STATE_CUSTOMER_NEVER_RECEIVED = "CUSTOMER_NEVER_RECEIVED"

    #: A constant which can be used with the lifecycle_state property of a UpdateTransferApplianceDetails.
    #: This constant has a value of "CANCELLED"
    LIFECYCLE_STATE_CANCELLED = "CANCELLED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTransferApplianceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this UpdateTransferApplianceDetails.
            Allowed values for this property are: "PREPARING", "FINALIZED", "RETURN_LABEL_REQUESTED", "RETURN_LABEL_GENERATING", "RETURN_LABEL_AVAILABLE", "DELETED", "CUSTOMER_NEVER_RECEIVED", "CANCELLED"
        :type lifecycle_state: str

        :param customer_shipping_address:
            The value to assign to the customer_shipping_address property of this UpdateTransferApplianceDetails.
        :type customer_shipping_address: oci.dts.models.ShippingAddress

        :param expected_return_date:
            The value to assign to the expected_return_date property of this UpdateTransferApplianceDetails.
        :type expected_return_date: datetime

        :param pickup_window_start_time:
            The value to assign to the pickup_window_start_time property of this UpdateTransferApplianceDetails.
        :type pickup_window_start_time: datetime

        :param pickup_window_end_time:
            The value to assign to the pickup_window_end_time property of this UpdateTransferApplianceDetails.
        :type pickup_window_end_time: datetime

        :param minimum_storage_capacity_in_terabytes:
            The value to assign to the minimum_storage_capacity_in_terabytes property of this UpdateTransferApplianceDetails.
        :type minimum_storage_capacity_in_terabytes: int

        """
        self.swagger_types = {
            'lifecycle_state': 'str',
            'customer_shipping_address': 'ShippingAddress',
            'expected_return_date': 'datetime',
            'pickup_window_start_time': 'datetime',
            'pickup_window_end_time': 'datetime',
            'minimum_storage_capacity_in_terabytes': 'int'
        }

        self.attribute_map = {
            'lifecycle_state': 'lifecycleState',
            'customer_shipping_address': 'customerShippingAddress',
            'expected_return_date': 'expectedReturnDate',
            'pickup_window_start_time': 'pickupWindowStartTime',
            'pickup_window_end_time': 'pickupWindowEndTime',
            'minimum_storage_capacity_in_terabytes': 'minimumStorageCapacityInTerabytes'
        }

        self._lifecycle_state = None
        self._customer_shipping_address = None
        self._expected_return_date = None
        self._pickup_window_start_time = None
        self._pickup_window_end_time = None
        self._minimum_storage_capacity_in_terabytes = None

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this UpdateTransferApplianceDetails.
        Allowed values for this property are: "PREPARING", "FINALIZED", "RETURN_LABEL_REQUESTED", "RETURN_LABEL_GENERATING", "RETURN_LABEL_AVAILABLE", "DELETED", "CUSTOMER_NEVER_RECEIVED", "CANCELLED"


        :return: The lifecycle_state of this UpdateTransferApplianceDetails.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this UpdateTransferApplianceDetails.

        :param lifecycle_state: The lifecycle_state of this UpdateTransferApplianceDetails.
        :type: str
        """
        allowed_values = ["PREPARING", "FINALIZED", "RETURN_LABEL_REQUESTED", "RETURN_LABEL_GENERATING", "RETURN_LABEL_AVAILABLE", "DELETED", "CUSTOMER_NEVER_RECEIVED", "CANCELLED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            raise ValueError(
                "Invalid value for `lifecycle_state`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._lifecycle_state = lifecycle_state

    @property
    def customer_shipping_address(self):
        """
        Gets the customer_shipping_address of this UpdateTransferApplianceDetails.

        :return: The customer_shipping_address of this UpdateTransferApplianceDetails.
        :rtype: oci.dts.models.ShippingAddress
        """
        return self._customer_shipping_address

    @customer_shipping_address.setter
    def customer_shipping_address(self, customer_shipping_address):
        """
        Sets the customer_shipping_address of this UpdateTransferApplianceDetails.

        :param customer_shipping_address: The customer_shipping_address of this UpdateTransferApplianceDetails.
        :type: oci.dts.models.ShippingAddress
        """
        self._customer_shipping_address = customer_shipping_address

    @property
    def expected_return_date(self):
        """
        Gets the expected_return_date of this UpdateTransferApplianceDetails.
        Expected return date from customer for the device, time portion should be zero.


        :return: The expected_return_date of this UpdateTransferApplianceDetails.
        :rtype: datetime
        """
        return self._expected_return_date

    @expected_return_date.setter
    def expected_return_date(self, expected_return_date):
        """
        Sets the expected_return_date of this UpdateTransferApplianceDetails.
        Expected return date from customer for the device, time portion should be zero.


        :param expected_return_date: The expected_return_date of this UpdateTransferApplianceDetails.
        :type: datetime
        """
        self._expected_return_date = expected_return_date

    @property
    def pickup_window_start_time(self):
        """
        Gets the pickup_window_start_time of this UpdateTransferApplianceDetails.
        Start time for the window to pickup the device from customer.


        :return: The pickup_window_start_time of this UpdateTransferApplianceDetails.
        :rtype: datetime
        """
        return self._pickup_window_start_time

    @pickup_window_start_time.setter
    def pickup_window_start_time(self, pickup_window_start_time):
        """
        Sets the pickup_window_start_time of this UpdateTransferApplianceDetails.
        Start time for the window to pickup the device from customer.


        :param pickup_window_start_time: The pickup_window_start_time of this UpdateTransferApplianceDetails.
        :type: datetime
        """
        self._pickup_window_start_time = pickup_window_start_time

    @property
    def pickup_window_end_time(self):
        """
        Gets the pickup_window_end_time of this UpdateTransferApplianceDetails.
        End time for the window to pickup the device from customer.


        :return: The pickup_window_end_time of this UpdateTransferApplianceDetails.
        :rtype: datetime
        """
        return self._pickup_window_end_time

    @pickup_window_end_time.setter
    def pickup_window_end_time(self, pickup_window_end_time):
        """
        Sets the pickup_window_end_time of this UpdateTransferApplianceDetails.
        End time for the window to pickup the device from customer.


        :param pickup_window_end_time: The pickup_window_end_time of this UpdateTransferApplianceDetails.
        :type: datetime
        """
        self._pickup_window_end_time = pickup_window_end_time

    @property
    def minimum_storage_capacity_in_terabytes(self):
        """
        Gets the minimum_storage_capacity_in_terabytes of this UpdateTransferApplianceDetails.
        Minimum storage capacity of the device, in terabytes. Valid options are 50, 95 and 150.


        :return: The minimum_storage_capacity_in_terabytes of this UpdateTransferApplianceDetails.
        :rtype: int
        """
        return self._minimum_storage_capacity_in_terabytes

    @minimum_storage_capacity_in_terabytes.setter
    def minimum_storage_capacity_in_terabytes(self, minimum_storage_capacity_in_terabytes):
        """
        Sets the minimum_storage_capacity_in_terabytes of this UpdateTransferApplianceDetails.
        Minimum storage capacity of the device, in terabytes. Valid options are 50, 95 and 150.


        :param minimum_storage_capacity_in_terabytes: The minimum_storage_capacity_in_terabytes of this UpdateTransferApplianceDetails.
        :type: int
        """
        self._minimum_storage_capacity_in_terabytes = minimum_storage_capacity_in_terabytes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
