# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
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
            Allowed values for this property are: "PREPARING", "FINALIZED", "DELETED", "CUSTOMER_NEVER_RECEIVED", "CANCELLED"
        :type lifecycle_state: str

        :param customer_shipping_address:
            The value to assign to the customer_shipping_address property of this UpdateTransferApplianceDetails.
        :type customer_shipping_address: ShippingAddress

        """
        self.swagger_types = {
            'lifecycle_state': 'str',
            'customer_shipping_address': 'ShippingAddress'
        }

        self.attribute_map = {
            'lifecycle_state': 'lifecycleState',
            'customer_shipping_address': 'customerShippingAddress'
        }

        self._lifecycle_state = None
        self._customer_shipping_address = None

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this UpdateTransferApplianceDetails.
        Allowed values for this property are: "PREPARING", "FINALIZED", "DELETED", "CUSTOMER_NEVER_RECEIVED", "CANCELLED"


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
        allowed_values = ["PREPARING", "FINALIZED", "DELETED", "CUSTOMER_NEVER_RECEIVED", "CANCELLED"]
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
        :rtype: ShippingAddress
        """
        return self._customer_shipping_address

    @customer_shipping_address.setter
    def customer_shipping_address(self, customer_shipping_address):
        """
        Sets the customer_shipping_address of this UpdateTransferApplianceDetails.

        :param customer_shipping_address: The customer_shipping_address of this UpdateTransferApplianceDetails.
        :type: ShippingAddress
        """
        self._customer_shipping_address = customer_shipping_address

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
