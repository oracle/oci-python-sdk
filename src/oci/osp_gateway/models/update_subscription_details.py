# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateSubscriptionDetails(object):
    """
    Request object for updating a subscription
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateSubscriptionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param subscription:
            The value to assign to the subscription property of this UpdateSubscriptionDetails.
        :type subscription: oci.osp_gateway.models.Subscription

        :param email:
            The value to assign to the email property of this UpdateSubscriptionDetails.
        :type email: str

        """
        self.swagger_types = {
            'subscription': 'Subscription',
            'email': 'str'
        }

        self.attribute_map = {
            'subscription': 'subscription',
            'email': 'email'
        }

        self._subscription = None
        self._email = None

    @property
    def subscription(self):
        """
        **[Required]** Gets the subscription of this UpdateSubscriptionDetails.

        :return: The subscription of this UpdateSubscriptionDetails.
        :rtype: oci.osp_gateway.models.Subscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """
        Sets the subscription of this UpdateSubscriptionDetails.

        :param subscription: The subscription of this UpdateSubscriptionDetails.
        :type: oci.osp_gateway.models.Subscription
        """
        self._subscription = subscription

    @property
    def email(self):
        """
        **[Required]** Gets the email of this UpdateSubscriptionDetails.
        User email


        :return: The email of this UpdateSubscriptionDetails.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UpdateSubscriptionDetails.
        User email


        :param email: The email of this UpdateSubscriptionDetails.
        :type: str
        """
        self._email = email

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
