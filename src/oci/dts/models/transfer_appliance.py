# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TransferAppliance(object):
    """
    TransferAppliance model.
    """

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "REQUESTED"
    LIFECYCLE_STATE_REQUESTED = "REQUESTED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "ORACLE_PREPARING"
    LIFECYCLE_STATE_ORACLE_PREPARING = "ORACLE_PREPARING"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "SHIPPING"
    LIFECYCLE_STATE_SHIPPING = "SHIPPING"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "DELIVERED"
    LIFECYCLE_STATE_DELIVERED = "DELIVERED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "PREPARING"
    LIFECYCLE_STATE_PREPARING = "PREPARING"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "FINALIZED"
    LIFECYCLE_STATE_FINALIZED = "FINALIZED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "RETURN_LABEL_REQUESTED"
    LIFECYCLE_STATE_RETURN_LABEL_REQUESTED = "RETURN_LABEL_REQUESTED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "RETURN_LABEL_GENERATING"
    LIFECYCLE_STATE_RETURN_LABEL_GENERATING = "RETURN_LABEL_GENERATING"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "RETURN_LABEL_AVAILABLE"
    LIFECYCLE_STATE_RETURN_LABEL_AVAILABLE = "RETURN_LABEL_AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "RETURN_DELAYED"
    LIFECYCLE_STATE_RETURN_DELAYED = "RETURN_DELAYED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "RETURN_SHIPPED"
    LIFECYCLE_STATE_RETURN_SHIPPED = "RETURN_SHIPPED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "RETURN_SHIPPED_CANCELLED"
    LIFECYCLE_STATE_RETURN_SHIPPED_CANCELLED = "RETURN_SHIPPED_CANCELLED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "ORACLE_RECEIVED"
    LIFECYCLE_STATE_ORACLE_RECEIVED = "ORACLE_RECEIVED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "ORACLE_RECEIVED_CANCELLED"
    LIFECYCLE_STATE_ORACLE_RECEIVED_CANCELLED = "ORACLE_RECEIVED_CANCELLED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "PROCESSING"
    LIFECYCLE_STATE_PROCESSING = "PROCESSING"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "COMPLETE"
    LIFECYCLE_STATE_COMPLETE = "COMPLETE"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "CUSTOMER_NEVER_RECEIVED"
    LIFECYCLE_STATE_CUSTOMER_NEVER_RECEIVED = "CUSTOMER_NEVER_RECEIVED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "ORACLE_NEVER_RECEIVED"
    LIFECYCLE_STATE_ORACLE_NEVER_RECEIVED = "ORACLE_NEVER_RECEIVED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "CUSTOMER_LOST"
    LIFECYCLE_STATE_CUSTOMER_LOST = "CUSTOMER_LOST"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "CANCELLED"
    LIFECYCLE_STATE_CANCELLED = "CANCELLED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "REJECTED"
    LIFECYCLE_STATE_REJECTED = "REJECTED"

    #: A constant which can be used with the lifecycle_state property of a TransferAppliance.
    #: This constant has a value of "ERROR"
    LIFECYCLE_STATE_ERROR = "ERROR"

    def __init__(self, **kwargs):
        """
        Initializes a new TransferAppliance object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label:
            The value to assign to the label property of this TransferAppliance.
        :type label: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TransferAppliance.
            Allowed values for this property are: "REQUESTED", "ORACLE_PREPARING", "SHIPPING", "DELIVERED", "PREPARING", "FINALIZED", "RETURN_LABEL_REQUESTED", "RETURN_LABEL_GENERATING", "RETURN_LABEL_AVAILABLE", "RETURN_DELAYED", "RETURN_SHIPPED", "RETURN_SHIPPED_CANCELLED", "ORACLE_RECEIVED", "ORACLE_RECEIVED_CANCELLED", "PROCESSING", "COMPLETE", "CUSTOMER_NEVER_RECEIVED", "ORACLE_NEVER_RECEIVED", "CUSTOMER_LOST", "CANCELLED", "DELETED", "REJECTED", "ERROR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param transfer_job_id:
            The value to assign to the transfer_job_id property of this TransferAppliance.
        :type transfer_job_id: str

        :param serial_number:
            The value to assign to the serial_number property of this TransferAppliance.
        :type serial_number: str

        :param creation_time:
            The value to assign to the creation_time property of this TransferAppliance.
        :type creation_time: datetime

        :param customer_received_time:
            The value to assign to the customer_received_time property of this TransferAppliance.
        :type customer_received_time: datetime

        :param customer_returned_time:
            The value to assign to the customer_returned_time property of this TransferAppliance.
        :type customer_returned_time: datetime

        :param next_billing_time:
            The value to assign to the next_billing_time property of this TransferAppliance.
        :type next_billing_time: datetime

        :param delivery_security_tie_id:
            The value to assign to the delivery_security_tie_id property of this TransferAppliance.
        :type delivery_security_tie_id: str

        :param return_security_tie_id:
            The value to assign to the return_security_tie_id property of this TransferAppliance.
        :type return_security_tie_id: str

        :param appliance_delivery_tracking_number:
            The value to assign to the appliance_delivery_tracking_number property of this TransferAppliance.
        :type appliance_delivery_tracking_number: str

        :param appliance_return_delivery_tracking_number:
            The value to assign to the appliance_return_delivery_tracking_number property of this TransferAppliance.
        :type appliance_return_delivery_tracking_number: str

        :param appliance_delivery_vendor:
            The value to assign to the appliance_delivery_vendor property of this TransferAppliance.
        :type appliance_delivery_vendor: str

        :param customer_shipping_address:
            The value to assign to the customer_shipping_address property of this TransferAppliance.
        :type customer_shipping_address: oci.dts.models.ShippingAddress

        :param upload_status_log_uri:
            The value to assign to the upload_status_log_uri property of this TransferAppliance.
        :type upload_status_log_uri: str

        :param return_shipping_label_uri:
            The value to assign to the return_shipping_label_uri property of this TransferAppliance.
        :type return_shipping_label_uri: str

        :param expected_return_date:
            The value to assign to the expected_return_date property of this TransferAppliance.
        :type expected_return_date: datetime

        :param pickup_window_start_time:
            The value to assign to the pickup_window_start_time property of this TransferAppliance.
        :type pickup_window_start_time: datetime

        :param pickup_window_end_time:
            The value to assign to the pickup_window_end_time property of this TransferAppliance.
        :type pickup_window_end_time: datetime

        :param minimum_storage_capacity_in_terabytes:
            The value to assign to the minimum_storage_capacity_in_terabytes property of this TransferAppliance.
        :type minimum_storage_capacity_in_terabytes: int

        """
        self.swagger_types = {
            'label': 'str',
            'lifecycle_state': 'str',
            'transfer_job_id': 'str',
            'serial_number': 'str',
            'creation_time': 'datetime',
            'customer_received_time': 'datetime',
            'customer_returned_time': 'datetime',
            'next_billing_time': 'datetime',
            'delivery_security_tie_id': 'str',
            'return_security_tie_id': 'str',
            'appliance_delivery_tracking_number': 'str',
            'appliance_return_delivery_tracking_number': 'str',
            'appliance_delivery_vendor': 'str',
            'customer_shipping_address': 'ShippingAddress',
            'upload_status_log_uri': 'str',
            'return_shipping_label_uri': 'str',
            'expected_return_date': 'datetime',
            'pickup_window_start_time': 'datetime',
            'pickup_window_end_time': 'datetime',
            'minimum_storage_capacity_in_terabytes': 'int'
        }

        self.attribute_map = {
            'label': 'label',
            'lifecycle_state': 'lifecycleState',
            'transfer_job_id': 'transferJobId',
            'serial_number': 'serialNumber',
            'creation_time': 'creationTime',
            'customer_received_time': 'customerReceivedTime',
            'customer_returned_time': 'customerReturnedTime',
            'next_billing_time': 'nextBillingTime',
            'delivery_security_tie_id': 'deliverySecurityTieId',
            'return_security_tie_id': 'returnSecurityTieId',
            'appliance_delivery_tracking_number': 'applianceDeliveryTrackingNumber',
            'appliance_return_delivery_tracking_number': 'applianceReturnDeliveryTrackingNumber',
            'appliance_delivery_vendor': 'applianceDeliveryVendor',
            'customer_shipping_address': 'customerShippingAddress',
            'upload_status_log_uri': 'uploadStatusLogUri',
            'return_shipping_label_uri': 'returnShippingLabelUri',
            'expected_return_date': 'expectedReturnDate',
            'pickup_window_start_time': 'pickupWindowStartTime',
            'pickup_window_end_time': 'pickupWindowEndTime',
            'minimum_storage_capacity_in_terabytes': 'minimumStorageCapacityInTerabytes'
        }

        self._label = None
        self._lifecycle_state = None
        self._transfer_job_id = None
        self._serial_number = None
        self._creation_time = None
        self._customer_received_time = None
        self._customer_returned_time = None
        self._next_billing_time = None
        self._delivery_security_tie_id = None
        self._return_security_tie_id = None
        self._appliance_delivery_tracking_number = None
        self._appliance_return_delivery_tracking_number = None
        self._appliance_delivery_vendor = None
        self._customer_shipping_address = None
        self._upload_status_log_uri = None
        self._return_shipping_label_uri = None
        self._expected_return_date = None
        self._pickup_window_start_time = None
        self._pickup_window_end_time = None
        self._minimum_storage_capacity_in_terabytes = None

    @property
    def label(self):
        """
        **[Required]** Gets the label of this TransferAppliance.
        Unique alpha-numeric identifier for a transfer appliance auto generated during create.


        :return: The label of this TransferAppliance.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this TransferAppliance.
        Unique alpha-numeric identifier for a transfer appliance auto generated during create.


        :param label: The label of this TransferAppliance.
        :type: str
        """
        self._label = label

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TransferAppliance.
        Allowed values for this property are: "REQUESTED", "ORACLE_PREPARING", "SHIPPING", "DELIVERED", "PREPARING", "FINALIZED", "RETURN_LABEL_REQUESTED", "RETURN_LABEL_GENERATING", "RETURN_LABEL_AVAILABLE", "RETURN_DELAYED", "RETURN_SHIPPED", "RETURN_SHIPPED_CANCELLED", "ORACLE_RECEIVED", "ORACLE_RECEIVED_CANCELLED", "PROCESSING", "COMPLETE", "CUSTOMER_NEVER_RECEIVED", "ORACLE_NEVER_RECEIVED", "CUSTOMER_LOST", "CANCELLED", "DELETED", "REJECTED", "ERROR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TransferAppliance.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TransferAppliance.

        :param lifecycle_state: The lifecycle_state of this TransferAppliance.
        :type: str
        """
        allowed_values = ["REQUESTED", "ORACLE_PREPARING", "SHIPPING", "DELIVERED", "PREPARING", "FINALIZED", "RETURN_LABEL_REQUESTED", "RETURN_LABEL_GENERATING", "RETURN_LABEL_AVAILABLE", "RETURN_DELAYED", "RETURN_SHIPPED", "RETURN_SHIPPED_CANCELLED", "ORACLE_RECEIVED", "ORACLE_RECEIVED_CANCELLED", "PROCESSING", "COMPLETE", "CUSTOMER_NEVER_RECEIVED", "ORACLE_NEVER_RECEIVED", "CUSTOMER_LOST", "CANCELLED", "DELETED", "REJECTED", "ERROR"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def transfer_job_id(self):
        """
        Gets the transfer_job_id of this TransferAppliance.

        :return: The transfer_job_id of this TransferAppliance.
        :rtype: str
        """
        return self._transfer_job_id

    @transfer_job_id.setter
    def transfer_job_id(self, transfer_job_id):
        """
        Sets the transfer_job_id of this TransferAppliance.

        :param transfer_job_id: The transfer_job_id of this TransferAppliance.
        :type: str
        """
        self._transfer_job_id = transfer_job_id

    @property
    def serial_number(self):
        """
        Gets the serial_number of this TransferAppliance.

        :return: The serial_number of this TransferAppliance.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """
        Sets the serial_number of this TransferAppliance.

        :param serial_number: The serial_number of this TransferAppliance.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def creation_time(self):
        """
        Gets the creation_time of this TransferAppliance.

        :return: The creation_time of this TransferAppliance.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this TransferAppliance.

        :param creation_time: The creation_time of this TransferAppliance.
        :type: datetime
        """
        self._creation_time = creation_time

    @property
    def customer_received_time(self):
        """
        Gets the customer_received_time of this TransferAppliance.

        :return: The customer_received_time of this TransferAppliance.
        :rtype: datetime
        """
        return self._customer_received_time

    @customer_received_time.setter
    def customer_received_time(self, customer_received_time):
        """
        Sets the customer_received_time of this TransferAppliance.

        :param customer_received_time: The customer_received_time of this TransferAppliance.
        :type: datetime
        """
        self._customer_received_time = customer_received_time

    @property
    def customer_returned_time(self):
        """
        Gets the customer_returned_time of this TransferAppliance.

        :return: The customer_returned_time of this TransferAppliance.
        :rtype: datetime
        """
        return self._customer_returned_time

    @customer_returned_time.setter
    def customer_returned_time(self, customer_returned_time):
        """
        Sets the customer_returned_time of this TransferAppliance.

        :param customer_returned_time: The customer_returned_time of this TransferAppliance.
        :type: datetime
        """
        self._customer_returned_time = customer_returned_time

    @property
    def next_billing_time(self):
        """
        Gets the next_billing_time of this TransferAppliance.

        :return: The next_billing_time of this TransferAppliance.
        :rtype: datetime
        """
        return self._next_billing_time

    @next_billing_time.setter
    def next_billing_time(self, next_billing_time):
        """
        Sets the next_billing_time of this TransferAppliance.

        :param next_billing_time: The next_billing_time of this TransferAppliance.
        :type: datetime
        """
        self._next_billing_time = next_billing_time

    @property
    def delivery_security_tie_id(self):
        """
        Gets the delivery_security_tie_id of this TransferAppliance.

        :return: The delivery_security_tie_id of this TransferAppliance.
        :rtype: str
        """
        return self._delivery_security_tie_id

    @delivery_security_tie_id.setter
    def delivery_security_tie_id(self, delivery_security_tie_id):
        """
        Sets the delivery_security_tie_id of this TransferAppliance.

        :param delivery_security_tie_id: The delivery_security_tie_id of this TransferAppliance.
        :type: str
        """
        self._delivery_security_tie_id = delivery_security_tie_id

    @property
    def return_security_tie_id(self):
        """
        Gets the return_security_tie_id of this TransferAppliance.

        :return: The return_security_tie_id of this TransferAppliance.
        :rtype: str
        """
        return self._return_security_tie_id

    @return_security_tie_id.setter
    def return_security_tie_id(self, return_security_tie_id):
        """
        Sets the return_security_tie_id of this TransferAppliance.

        :param return_security_tie_id: The return_security_tie_id of this TransferAppliance.
        :type: str
        """
        self._return_security_tie_id = return_security_tie_id

    @property
    def appliance_delivery_tracking_number(self):
        """
        Gets the appliance_delivery_tracking_number of this TransferAppliance.

        :return: The appliance_delivery_tracking_number of this TransferAppliance.
        :rtype: str
        """
        return self._appliance_delivery_tracking_number

    @appliance_delivery_tracking_number.setter
    def appliance_delivery_tracking_number(self, appliance_delivery_tracking_number):
        """
        Sets the appliance_delivery_tracking_number of this TransferAppliance.

        :param appliance_delivery_tracking_number: The appliance_delivery_tracking_number of this TransferAppliance.
        :type: str
        """
        self._appliance_delivery_tracking_number = appliance_delivery_tracking_number

    @property
    def appliance_return_delivery_tracking_number(self):
        """
        Gets the appliance_return_delivery_tracking_number of this TransferAppliance.

        :return: The appliance_return_delivery_tracking_number of this TransferAppliance.
        :rtype: str
        """
        return self._appliance_return_delivery_tracking_number

    @appliance_return_delivery_tracking_number.setter
    def appliance_return_delivery_tracking_number(self, appliance_return_delivery_tracking_number):
        """
        Sets the appliance_return_delivery_tracking_number of this TransferAppliance.

        :param appliance_return_delivery_tracking_number: The appliance_return_delivery_tracking_number of this TransferAppliance.
        :type: str
        """
        self._appliance_return_delivery_tracking_number = appliance_return_delivery_tracking_number

    @property
    def appliance_delivery_vendor(self):
        """
        Gets the appliance_delivery_vendor of this TransferAppliance.

        :return: The appliance_delivery_vendor of this TransferAppliance.
        :rtype: str
        """
        return self._appliance_delivery_vendor

    @appliance_delivery_vendor.setter
    def appliance_delivery_vendor(self, appliance_delivery_vendor):
        """
        Sets the appliance_delivery_vendor of this TransferAppliance.

        :param appliance_delivery_vendor: The appliance_delivery_vendor of this TransferAppliance.
        :type: str
        """
        self._appliance_delivery_vendor = appliance_delivery_vendor

    @property
    def customer_shipping_address(self):
        """
        Gets the customer_shipping_address of this TransferAppliance.

        :return: The customer_shipping_address of this TransferAppliance.
        :rtype: oci.dts.models.ShippingAddress
        """
        return self._customer_shipping_address

    @customer_shipping_address.setter
    def customer_shipping_address(self, customer_shipping_address):
        """
        Sets the customer_shipping_address of this TransferAppliance.

        :param customer_shipping_address: The customer_shipping_address of this TransferAppliance.
        :type: oci.dts.models.ShippingAddress
        """
        self._customer_shipping_address = customer_shipping_address

    @property
    def upload_status_log_uri(self):
        """
        Gets the upload_status_log_uri of this TransferAppliance.

        :return: The upload_status_log_uri of this TransferAppliance.
        :rtype: str
        """
        return self._upload_status_log_uri

    @upload_status_log_uri.setter
    def upload_status_log_uri(self, upload_status_log_uri):
        """
        Sets the upload_status_log_uri of this TransferAppliance.

        :param upload_status_log_uri: The upload_status_log_uri of this TransferAppliance.
        :type: str
        """
        self._upload_status_log_uri = upload_status_log_uri

    @property
    def return_shipping_label_uri(self):
        """
        Gets the return_shipping_label_uri of this TransferAppliance.

        :return: The return_shipping_label_uri of this TransferAppliance.
        :rtype: str
        """
        return self._return_shipping_label_uri

    @return_shipping_label_uri.setter
    def return_shipping_label_uri(self, return_shipping_label_uri):
        """
        Sets the return_shipping_label_uri of this TransferAppliance.

        :param return_shipping_label_uri: The return_shipping_label_uri of this TransferAppliance.
        :type: str
        """
        self._return_shipping_label_uri = return_shipping_label_uri

    @property
    def expected_return_date(self):
        """
        Gets the expected_return_date of this TransferAppliance.
        Expected return date from customer for the device, time portion should be zero.


        :return: The expected_return_date of this TransferAppliance.
        :rtype: datetime
        """
        return self._expected_return_date

    @expected_return_date.setter
    def expected_return_date(self, expected_return_date):
        """
        Sets the expected_return_date of this TransferAppliance.
        Expected return date from customer for the device, time portion should be zero.


        :param expected_return_date: The expected_return_date of this TransferAppliance.
        :type: datetime
        """
        self._expected_return_date = expected_return_date

    @property
    def pickup_window_start_time(self):
        """
        Gets the pickup_window_start_time of this TransferAppliance.
        Start time for the window to pickup the device from customer.


        :return: The pickup_window_start_time of this TransferAppliance.
        :rtype: datetime
        """
        return self._pickup_window_start_time

    @pickup_window_start_time.setter
    def pickup_window_start_time(self, pickup_window_start_time):
        """
        Sets the pickup_window_start_time of this TransferAppliance.
        Start time for the window to pickup the device from customer.


        :param pickup_window_start_time: The pickup_window_start_time of this TransferAppliance.
        :type: datetime
        """
        self._pickup_window_start_time = pickup_window_start_time

    @property
    def pickup_window_end_time(self):
        """
        Gets the pickup_window_end_time of this TransferAppliance.
        End time for the window to pickup the device from customer.


        :return: The pickup_window_end_time of this TransferAppliance.
        :rtype: datetime
        """
        return self._pickup_window_end_time

    @pickup_window_end_time.setter
    def pickup_window_end_time(self, pickup_window_end_time):
        """
        Sets the pickup_window_end_time of this TransferAppliance.
        End time for the window to pickup the device from customer.


        :param pickup_window_end_time: The pickup_window_end_time of this TransferAppliance.
        :type: datetime
        """
        self._pickup_window_end_time = pickup_window_end_time

    @property
    def minimum_storage_capacity_in_terabytes(self):
        """
        Gets the minimum_storage_capacity_in_terabytes of this TransferAppliance.
        Minimum storage capacity of the device, in terabytes. Valid options are 50, 95 and 150.


        :return: The minimum_storage_capacity_in_terabytes of this TransferAppliance.
        :rtype: int
        """
        return self._minimum_storage_capacity_in_terabytes

    @minimum_storage_capacity_in_terabytes.setter
    def minimum_storage_capacity_in_terabytes(self, minimum_storage_capacity_in_terabytes):
        """
        Sets the minimum_storage_capacity_in_terabytes of this TransferAppliance.
        Minimum storage capacity of the device, in terabytes. Valid options are 50, 95 and 150.


        :param minimum_storage_capacity_in_terabytes: The minimum_storage_capacity_in_terabytes of this TransferAppliance.
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
