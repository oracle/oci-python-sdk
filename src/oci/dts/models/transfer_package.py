# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TransferPackage(object):
    """
    TransferPackage model.
    """

    #: A constant which can be used with the lifecycle_state property of a TransferPackage.
    #: This constant has a value of "PREPARING"
    LIFECYCLE_STATE_PREPARING = "PREPARING"

    #: A constant which can be used with the lifecycle_state property of a TransferPackage.
    #: This constant has a value of "SHIPPING"
    LIFECYCLE_STATE_SHIPPING = "SHIPPING"

    #: A constant which can be used with the lifecycle_state property of a TransferPackage.
    #: This constant has a value of "RECEIVED"
    LIFECYCLE_STATE_RECEIVED = "RECEIVED"

    #: A constant which can be used with the lifecycle_state property of a TransferPackage.
    #: This constant has a value of "PROCESSING"
    LIFECYCLE_STATE_PROCESSING = "PROCESSING"

    #: A constant which can be used with the lifecycle_state property of a TransferPackage.
    #: This constant has a value of "PROCESSED"
    LIFECYCLE_STATE_PROCESSED = "PROCESSED"

    #: A constant which can be used with the lifecycle_state property of a TransferPackage.
    #: This constant has a value of "RETURNED"
    LIFECYCLE_STATE_RETURNED = "RETURNED"

    #: A constant which can be used with the lifecycle_state property of a TransferPackage.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a TransferPackage.
    #: This constant has a value of "CANCELLED"
    LIFECYCLE_STATE_CANCELLED = "CANCELLED"

    #: A constant which can be used with the lifecycle_state property of a TransferPackage.
    #: This constant has a value of "CANCELLED_RETURNED"
    LIFECYCLE_STATE_CANCELLED_RETURNED = "CANCELLED_RETURNED"

    def __init__(self, **kwargs):
        """
        Initializes a new TransferPackage object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label:
            The value to assign to the label property of this TransferPackage.
        :type label: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TransferPackage.
            Allowed values for this property are: "PREPARING", "SHIPPING", "RECEIVED", "PROCESSING", "PROCESSED", "RETURNED", "DELETED", "CANCELLED", "CANCELLED_RETURNED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param transfer_job_id:
            The value to assign to the transfer_job_id property of this TransferPackage.
        :type transfer_job_id: str

        :param creation_time:
            The value to assign to the creation_time property of this TransferPackage.
        :type creation_time: datetime

        :param original_package_delivery_tracking_number:
            The value to assign to the original_package_delivery_tracking_number property of this TransferPackage.
        :type original_package_delivery_tracking_number: str

        :param return_package_delivery_tracking_number:
            The value to assign to the return_package_delivery_tracking_number property of this TransferPackage.
        :type return_package_delivery_tracking_number: str

        :param package_delivery_vendor:
            The value to assign to the package_delivery_vendor property of this TransferPackage.
        :type package_delivery_vendor: str

        :param transfer_site_shipping_address:
            The value to assign to the transfer_site_shipping_address property of this TransferPackage.
        :type transfer_site_shipping_address: str

        :param attached_transfer_device_labels:
            The value to assign to the attached_transfer_device_labels property of this TransferPackage.
        :type attached_transfer_device_labels: list[str]

        """
        self.swagger_types = {
            'label': 'str',
            'lifecycle_state': 'str',
            'transfer_job_id': 'str',
            'creation_time': 'datetime',
            'original_package_delivery_tracking_number': 'str',
            'return_package_delivery_tracking_number': 'str',
            'package_delivery_vendor': 'str',
            'transfer_site_shipping_address': 'str',
            'attached_transfer_device_labels': 'list[str]'
        }

        self.attribute_map = {
            'label': 'label',
            'lifecycle_state': 'lifecycleState',
            'transfer_job_id': 'transferJobId',
            'creation_time': 'creationTime',
            'original_package_delivery_tracking_number': 'originalPackageDeliveryTrackingNumber',
            'return_package_delivery_tracking_number': 'returnPackageDeliveryTrackingNumber',
            'package_delivery_vendor': 'packageDeliveryVendor',
            'transfer_site_shipping_address': 'transferSiteShippingAddress',
            'attached_transfer_device_labels': 'attachedTransferDeviceLabels'
        }

        self._label = None
        self._lifecycle_state = None
        self._transfer_job_id = None
        self._creation_time = None
        self._original_package_delivery_tracking_number = None
        self._return_package_delivery_tracking_number = None
        self._package_delivery_vendor = None
        self._transfer_site_shipping_address = None
        self._attached_transfer_device_labels = None

    @property
    def label(self):
        """
        **[Required]** Gets the label of this TransferPackage.

        :return: The label of this TransferPackage.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this TransferPackage.

        :param label: The label of this TransferPackage.
        :type: str
        """
        self._label = label

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TransferPackage.
        Allowed values for this property are: "PREPARING", "SHIPPING", "RECEIVED", "PROCESSING", "PROCESSED", "RETURNED", "DELETED", "CANCELLED", "CANCELLED_RETURNED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TransferPackage.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TransferPackage.

        :param lifecycle_state: The lifecycle_state of this TransferPackage.
        :type: str
        """
        allowed_values = ["PREPARING", "SHIPPING", "RECEIVED", "PROCESSING", "PROCESSED", "RETURNED", "DELETED", "CANCELLED", "CANCELLED_RETURNED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def transfer_job_id(self):
        """
        Gets the transfer_job_id of this TransferPackage.

        :return: The transfer_job_id of this TransferPackage.
        :rtype: str
        """
        return self._transfer_job_id

    @transfer_job_id.setter
    def transfer_job_id(self, transfer_job_id):
        """
        Sets the transfer_job_id of this TransferPackage.

        :param transfer_job_id: The transfer_job_id of this TransferPackage.
        :type: str
        """
        self._transfer_job_id = transfer_job_id

    @property
    def creation_time(self):
        """
        Gets the creation_time of this TransferPackage.

        :return: The creation_time of this TransferPackage.
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this TransferPackage.

        :param creation_time: The creation_time of this TransferPackage.
        :type: datetime
        """
        self._creation_time = creation_time

    @property
    def original_package_delivery_tracking_number(self):
        """
        Gets the original_package_delivery_tracking_number of this TransferPackage.

        :return: The original_package_delivery_tracking_number of this TransferPackage.
        :rtype: str
        """
        return self._original_package_delivery_tracking_number

    @original_package_delivery_tracking_number.setter
    def original_package_delivery_tracking_number(self, original_package_delivery_tracking_number):
        """
        Sets the original_package_delivery_tracking_number of this TransferPackage.

        :param original_package_delivery_tracking_number: The original_package_delivery_tracking_number of this TransferPackage.
        :type: str
        """
        self._original_package_delivery_tracking_number = original_package_delivery_tracking_number

    @property
    def return_package_delivery_tracking_number(self):
        """
        Gets the return_package_delivery_tracking_number of this TransferPackage.

        :return: The return_package_delivery_tracking_number of this TransferPackage.
        :rtype: str
        """
        return self._return_package_delivery_tracking_number

    @return_package_delivery_tracking_number.setter
    def return_package_delivery_tracking_number(self, return_package_delivery_tracking_number):
        """
        Sets the return_package_delivery_tracking_number of this TransferPackage.

        :param return_package_delivery_tracking_number: The return_package_delivery_tracking_number of this TransferPackage.
        :type: str
        """
        self._return_package_delivery_tracking_number = return_package_delivery_tracking_number

    @property
    def package_delivery_vendor(self):
        """
        Gets the package_delivery_vendor of this TransferPackage.

        :return: The package_delivery_vendor of this TransferPackage.
        :rtype: str
        """
        return self._package_delivery_vendor

    @package_delivery_vendor.setter
    def package_delivery_vendor(self, package_delivery_vendor):
        """
        Sets the package_delivery_vendor of this TransferPackage.

        :param package_delivery_vendor: The package_delivery_vendor of this TransferPackage.
        :type: str
        """
        self._package_delivery_vendor = package_delivery_vendor

    @property
    def transfer_site_shipping_address(self):
        """
        Gets the transfer_site_shipping_address of this TransferPackage.

        :return: The transfer_site_shipping_address of this TransferPackage.
        :rtype: str
        """
        return self._transfer_site_shipping_address

    @transfer_site_shipping_address.setter
    def transfer_site_shipping_address(self, transfer_site_shipping_address):
        """
        Sets the transfer_site_shipping_address of this TransferPackage.

        :param transfer_site_shipping_address: The transfer_site_shipping_address of this TransferPackage.
        :type: str
        """
        self._transfer_site_shipping_address = transfer_site_shipping_address

    @property
    def attached_transfer_device_labels(self):
        """
        Gets the attached_transfer_device_labels of this TransferPackage.
        Transfer Devices attached to this Transfer Package


        :return: The attached_transfer_device_labels of this TransferPackage.
        :rtype: list[str]
        """
        return self._attached_transfer_device_labels

    @attached_transfer_device_labels.setter
    def attached_transfer_device_labels(self, attached_transfer_device_labels):
        """
        Sets the attached_transfer_device_labels of this TransferPackage.
        Transfer Devices attached to this Transfer Package


        :param attached_transfer_device_labels: The attached_transfer_device_labels of this TransferPackage.
        :type: list[str]
        """
        self._attached_transfer_device_labels = attached_transfer_device_labels

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
