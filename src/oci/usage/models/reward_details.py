# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RewardDetails(object):
    """
    The overrall reward summary of the monthly summary rewards.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RewardDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenancy_id:
            The value to assign to the tenancy_id property of this RewardDetails.
        :type tenancy_id: str

        :param subscription_id:
            The value to assign to the subscription_id property of this RewardDetails.
        :type subscription_id: str

        :param currency:
            The value to assign to the currency property of this RewardDetails.
        :type currency: str

        :param rewards_rate:
            The value to assign to the rewards_rate property of this RewardDetails.
        :type rewards_rate: float

        :param total_rewards_available:
            The value to assign to the total_rewards_available property of this RewardDetails.
        :type total_rewards_available: float

        """
        self.swagger_types = {
            'tenancy_id': 'str',
            'subscription_id': 'str',
            'currency': 'str',
            'rewards_rate': 'float',
            'total_rewards_available': 'float'
        }

        self.attribute_map = {
            'tenancy_id': 'tenancyId',
            'subscription_id': 'subscriptionId',
            'currency': 'currency',
            'rewards_rate': 'rewardsRate',
            'total_rewards_available': 'totalRewardsAvailable'
        }

        self._tenancy_id = None
        self._subscription_id = None
        self._currency = None
        self._rewards_rate = None
        self._total_rewards_available = None

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this RewardDetails.
        The OCID of the target tenancy.


        :return: The tenancy_id of this RewardDetails.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this RewardDetails.
        The OCID of the target tenancy.


        :param tenancy_id: The tenancy_id of this RewardDetails.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def subscription_id(self):
        """
        Gets the subscription_id of this RewardDetails.
        The entitlement id from MQS and it is same as subcription id.


        :return: The subscription_id of this RewardDetails.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """
        Sets the subscription_id of this RewardDetails.
        The entitlement id from MQS and it is same as subcription id.


        :param subscription_id: The subscription_id of this RewardDetails.
        :type: str
        """
        self._subscription_id = subscription_id

    @property
    def currency(self):
        """
        Gets the currency of this RewardDetails.
        The currency unit for the reward amount.


        :return: The currency of this RewardDetails.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this RewardDetails.
        The currency unit for the reward amount.


        :param currency: The currency of this RewardDetails.
        :type: str
        """
        self._currency = currency

    @property
    def rewards_rate(self):
        """
        Gets the rewards_rate of this RewardDetails.
        The current Rewards percentage in decimal format.


        :return: The rewards_rate of this RewardDetails.
        :rtype: float
        """
        return self._rewards_rate

    @rewards_rate.setter
    def rewards_rate(self, rewards_rate):
        """
        Sets the rewards_rate of this RewardDetails.
        The current Rewards percentage in decimal format.


        :param rewards_rate: The rewards_rate of this RewardDetails.
        :type: float
        """
        self._rewards_rate = rewards_rate

    @property
    def total_rewards_available(self):
        """
        Gets the total_rewards_available of this RewardDetails.
        The total number of available rewards for a given subscription Id.


        :return: The total_rewards_available of this RewardDetails.
        :rtype: float
        """
        return self._total_rewards_available

    @total_rewards_available.setter
    def total_rewards_available(self, total_rewards_available):
        """
        Sets the total_rewards_available of this RewardDetails.
        The total number of available rewards for a given subscription Id.


        :param total_rewards_available: The total_rewards_available of this RewardDetails.
        :type: float
        """
        self._total_rewards_available = total_rewards_available

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
