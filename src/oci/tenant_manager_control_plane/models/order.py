# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Order(object):
    """
    Order details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Order object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param order_number:
            The value to assign to the order_number property of this Order.
        :type order_number: str

        :param data_center_region:
            The value to assign to the data_center_region property of this Order.
        :type data_center_region: str

        :param admin_email:
            The value to assign to the admin_email property of this Order.
        :type admin_email: str

        :param order_state:
            The value to assign to the order_state property of this Order.
        :type order_state: str

        :param subscriptions:
            The value to assign to the subscriptions property of this Order.
        :type subscriptions: list[oci.tenant_manager_control_plane.models.SubscriptionInfo]

        """
        self.swagger_types = {
            'order_number': 'str',
            'data_center_region': 'str',
            'admin_email': 'str',
            'order_state': 'str',
            'subscriptions': 'list[SubscriptionInfo]'
        }

        self.attribute_map = {
            'order_number': 'orderNumber',
            'data_center_region': 'dataCenterRegion',
            'admin_email': 'adminEmail',
            'order_state': 'orderState',
            'subscriptions': 'subscriptions'
        }

        self._order_number = None
        self._data_center_region = None
        self._admin_email = None
        self._order_state = None
        self._subscriptions = None

    @property
    def order_number(self):
        """
        **[Required]** Gets the order_number of this Order.
        Immutable and unique order number holding customer subscription information.


        :return: The order_number of this Order.
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """
        Sets the order_number of this Order.
        Immutable and unique order number holding customer subscription information.


        :param order_number: The order_number of this Order.
        :type: str
        """
        self._order_number = order_number

    @property
    def data_center_region(self):
        """
        Gets the data_center_region of this Order.
        Order's data center region.


        :return: The data_center_region of this Order.
        :rtype: str
        """
        return self._data_center_region

    @data_center_region.setter
    def data_center_region(self, data_center_region):
        """
        Sets the data_center_region of this Order.
        Order's data center region.


        :param data_center_region: The data_center_region of this Order.
        :type: str
        """
        self._data_center_region = data_center_region

    @property
    def admin_email(self):
        """
        **[Required]** Gets the admin_email of this Order.
        Administrator email owning the subscription.


        :return: The admin_email of this Order.
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """
        Sets the admin_email of this Order.
        Administrator email owning the subscription.


        :param admin_email: The admin_email of this Order.
        :type: str
        """
        self._admin_email = admin_email

    @property
    def order_state(self):
        """
        **[Required]** Gets the order_state of this Order.
        State of the order.


        :return: The order_state of this Order.
        :rtype: str
        """
        return self._order_state

    @order_state.setter
    def order_state(self, order_state):
        """
        Sets the order_state of this Order.
        State of the order.


        :param order_state: The order_state of this Order.
        :type: str
        """
        self._order_state = order_state

    @property
    def subscriptions(self):
        """
        **[Required]** Gets the subscriptions of this Order.
        Array of subscriptions associated with the order.


        :return: The subscriptions of this Order.
        :rtype: list[oci.tenant_manager_control_plane.models.SubscriptionInfo]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """
        Sets the subscriptions of this Order.
        Array of subscriptions associated with the order.


        :param subscriptions: The subscriptions of this Order.
        :type: list[oci.tenant_manager_control_plane.models.SubscriptionInfo]
        """
        self._subscriptions = subscriptions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
