# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTransferPackageDetails(object):
    """
    CreateTransferPackageDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTransferPackageDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param original_package_delivery_tracking_number:
            The value to assign to the original_package_delivery_tracking_number property of this CreateTransferPackageDetails.
        :type original_package_delivery_tracking_number: str

        :param return_package_delivery_tracking_number:
            The value to assign to the return_package_delivery_tracking_number property of this CreateTransferPackageDetails.
        :type return_package_delivery_tracking_number: str

        :param package_delivery_vendor:
            The value to assign to the package_delivery_vendor property of this CreateTransferPackageDetails.
        :type package_delivery_vendor: str

        """
        self.swagger_types = {
            'original_package_delivery_tracking_number': 'str',
            'return_package_delivery_tracking_number': 'str',
            'package_delivery_vendor': 'str'
        }

        self.attribute_map = {
            'original_package_delivery_tracking_number': 'originalPackageDeliveryTrackingNumber',
            'return_package_delivery_tracking_number': 'returnPackageDeliveryTrackingNumber',
            'package_delivery_vendor': 'packageDeliveryVendor'
        }

        self._original_package_delivery_tracking_number = None
        self._return_package_delivery_tracking_number = None
        self._package_delivery_vendor = None

    @property
    def original_package_delivery_tracking_number(self):
        """
        Gets the original_package_delivery_tracking_number of this CreateTransferPackageDetails.

        :return: The original_package_delivery_tracking_number of this CreateTransferPackageDetails.
        :rtype: str
        """
        return self._original_package_delivery_tracking_number

    @original_package_delivery_tracking_number.setter
    def original_package_delivery_tracking_number(self, original_package_delivery_tracking_number):
        """
        Sets the original_package_delivery_tracking_number of this CreateTransferPackageDetails.

        :param original_package_delivery_tracking_number: The original_package_delivery_tracking_number of this CreateTransferPackageDetails.
        :type: str
        """
        self._original_package_delivery_tracking_number = original_package_delivery_tracking_number

    @property
    def return_package_delivery_tracking_number(self):
        """
        Gets the return_package_delivery_tracking_number of this CreateTransferPackageDetails.

        :return: The return_package_delivery_tracking_number of this CreateTransferPackageDetails.
        :rtype: str
        """
        return self._return_package_delivery_tracking_number

    @return_package_delivery_tracking_number.setter
    def return_package_delivery_tracking_number(self, return_package_delivery_tracking_number):
        """
        Sets the return_package_delivery_tracking_number of this CreateTransferPackageDetails.

        :param return_package_delivery_tracking_number: The return_package_delivery_tracking_number of this CreateTransferPackageDetails.
        :type: str
        """
        self._return_package_delivery_tracking_number = return_package_delivery_tracking_number

    @property
    def package_delivery_vendor(self):
        """
        Gets the package_delivery_vendor of this CreateTransferPackageDetails.

        :return: The package_delivery_vendor of this CreateTransferPackageDetails.
        :rtype: str
        """
        return self._package_delivery_vendor

    @package_delivery_vendor.setter
    def package_delivery_vendor(self, package_delivery_vendor):
        """
        Sets the package_delivery_vendor of this CreateTransferPackageDetails.

        :param package_delivery_vendor: The package_delivery_vendor of this CreateTransferPackageDetails.
        :type: str
        """
        self._package_delivery_vendor = package_delivery_vendor

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
