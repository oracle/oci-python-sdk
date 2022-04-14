# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MonthlyRewardSummary(object):
    """
    Object describing the monthly rewards summary for the requested subscription ID.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MonthlyRewardSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param available_rewards:
            The value to assign to the available_rewards property of this MonthlyRewardSummary.
        :type available_rewards: float

        :param redeemed_rewards:
            The value to assign to the redeemed_rewards property of this MonthlyRewardSummary.
        :type redeemed_rewards: float

        :param earned_rewards:
            The value to assign to the earned_rewards property of this MonthlyRewardSummary.
        :type earned_rewards: float

        :param is_manual:
            The value to assign to the is_manual property of this MonthlyRewardSummary.
        :type is_manual: bool

        :param time_rewards_expired:
            The value to assign to the time_rewards_expired property of this MonthlyRewardSummary.
        :type time_rewards_expired: datetime

        :param time_rewards_earned:
            The value to assign to the time_rewards_earned property of this MonthlyRewardSummary.
        :type time_rewards_earned: datetime

        :param time_usage_started:
            The value to assign to the time_usage_started property of this MonthlyRewardSummary.
        :type time_usage_started: datetime

        :param time_usage_ended:
            The value to assign to the time_usage_ended property of this MonthlyRewardSummary.
        :type time_usage_ended: datetime

        :param usage_amount:
            The value to assign to the usage_amount property of this MonthlyRewardSummary.
        :type usage_amount: float

        :param eligible_usage_amount:
            The value to assign to the eligible_usage_amount property of this MonthlyRewardSummary.
        :type eligible_usage_amount: float

        :param ineligible_usage_amount:
            The value to assign to the ineligible_usage_amount property of this MonthlyRewardSummary.
        :type ineligible_usage_amount: float

        :param usage_period_key:
            The value to assign to the usage_period_key property of this MonthlyRewardSummary.
        :type usage_period_key: str

        """
        self.swagger_types = {
            'available_rewards': 'float',
            'redeemed_rewards': 'float',
            'earned_rewards': 'float',
            'is_manual': 'bool',
            'time_rewards_expired': 'datetime',
            'time_rewards_earned': 'datetime',
            'time_usage_started': 'datetime',
            'time_usage_ended': 'datetime',
            'usage_amount': 'float',
            'eligible_usage_amount': 'float',
            'ineligible_usage_amount': 'float',
            'usage_period_key': 'str'
        }

        self.attribute_map = {
            'available_rewards': 'availableRewards',
            'redeemed_rewards': 'redeemedRewards',
            'earned_rewards': 'earnedRewards',
            'is_manual': 'isManual',
            'time_rewards_expired': 'timeRewardsExpired',
            'time_rewards_earned': 'timeRewardsEarned',
            'time_usage_started': 'timeUsageStarted',
            'time_usage_ended': 'timeUsageEnded',
            'usage_amount': 'usageAmount',
            'eligible_usage_amount': 'eligibleUsageAmount',
            'ineligible_usage_amount': 'ineligibleUsageAmount',
            'usage_period_key': 'usagePeriodKey'
        }

        self._available_rewards = None
        self._redeemed_rewards = None
        self._earned_rewards = None
        self._is_manual = None
        self._time_rewards_expired = None
        self._time_rewards_earned = None
        self._time_usage_started = None
        self._time_usage_ended = None
        self._usage_amount = None
        self._eligible_usage_amount = None
        self._ineligible_usage_amount = None
        self._usage_period_key = None

    @property
    def available_rewards(self):
        """
        Gets the available_rewards of this MonthlyRewardSummary.
        The number of rewards available for a specific usage period.


        :return: The available_rewards of this MonthlyRewardSummary.
        :rtype: float
        """
        return self._available_rewards

    @available_rewards.setter
    def available_rewards(self, available_rewards):
        """
        Sets the available_rewards of this MonthlyRewardSummary.
        The number of rewards available for a specific usage period.


        :param available_rewards: The available_rewards of this MonthlyRewardSummary.
        :type: float
        """
        self._available_rewards = available_rewards

    @property
    def redeemed_rewards(self):
        """
        Gets the redeemed_rewards of this MonthlyRewardSummary.
        The number of rewards redeemed for a specific month.


        :return: The redeemed_rewards of this MonthlyRewardSummary.
        :rtype: float
        """
        return self._redeemed_rewards

    @redeemed_rewards.setter
    def redeemed_rewards(self, redeemed_rewards):
        """
        Sets the redeemed_rewards of this MonthlyRewardSummary.
        The number of rewards redeemed for a specific month.


        :param redeemed_rewards: The redeemed_rewards of this MonthlyRewardSummary.
        :type: float
        """
        self._redeemed_rewards = redeemed_rewards

    @property
    def earned_rewards(self):
        """
        Gets the earned_rewards of this MonthlyRewardSummary.
        The number of rewards earned for the specific usage period.


        :return: The earned_rewards of this MonthlyRewardSummary.
        :rtype: float
        """
        return self._earned_rewards

    @earned_rewards.setter
    def earned_rewards(self, earned_rewards):
        """
        Sets the earned_rewards of this MonthlyRewardSummary.
        The number of rewards earned for the specific usage period.


        :param earned_rewards: The earned_rewards of this MonthlyRewardSummary.
        :type: float
        """
        self._earned_rewards = earned_rewards

    @property
    def is_manual(self):
        """
        Gets the is_manual of this MonthlyRewardSummary.
        The boolean parameter to indicate whether or not the available rewards are manually posted.


        :return: The is_manual of this MonthlyRewardSummary.
        :rtype: bool
        """
        return self._is_manual

    @is_manual.setter
    def is_manual(self, is_manual):
        """
        Sets the is_manual of this MonthlyRewardSummary.
        The boolean parameter to indicate whether or not the available rewards are manually posted.


        :param is_manual: The is_manual of this MonthlyRewardSummary.
        :type: bool
        """
        self._is_manual = is_manual

    @property
    def time_rewards_expired(self):
        """
        Gets the time_rewards_expired of this MonthlyRewardSummary.
        The date and time when rewards expire.


        :return: The time_rewards_expired of this MonthlyRewardSummary.
        :rtype: datetime
        """
        return self._time_rewards_expired

    @time_rewards_expired.setter
    def time_rewards_expired(self, time_rewards_expired):
        """
        Sets the time_rewards_expired of this MonthlyRewardSummary.
        The date and time when rewards expire.


        :param time_rewards_expired: The time_rewards_expired of this MonthlyRewardSummary.
        :type: datetime
        """
        self._time_rewards_expired = time_rewards_expired

    @property
    def time_rewards_earned(self):
        """
        Gets the time_rewards_earned of this MonthlyRewardSummary.
        The date and time when rewards accrue.


        :return: The time_rewards_earned of this MonthlyRewardSummary.
        :rtype: datetime
        """
        return self._time_rewards_earned

    @time_rewards_earned.setter
    def time_rewards_earned(self, time_rewards_earned):
        """
        Sets the time_rewards_earned of this MonthlyRewardSummary.
        The date and time when rewards accrue.


        :param time_rewards_earned: The time_rewards_earned of this MonthlyRewardSummary.
        :type: datetime
        """
        self._time_rewards_earned = time_rewards_earned

    @property
    def time_usage_started(self):
        """
        Gets the time_usage_started of this MonthlyRewardSummary.
        The start date and time for the usage period.


        :return: The time_usage_started of this MonthlyRewardSummary.
        :rtype: datetime
        """
        return self._time_usage_started

    @time_usage_started.setter
    def time_usage_started(self, time_usage_started):
        """
        Sets the time_usage_started of this MonthlyRewardSummary.
        The start date and time for the usage period.


        :param time_usage_started: The time_usage_started of this MonthlyRewardSummary.
        :type: datetime
        """
        self._time_usage_started = time_usage_started

    @property
    def time_usage_ended(self):
        """
        Gets the time_usage_ended of this MonthlyRewardSummary.
        The end date and time for the usage period.


        :return: The time_usage_ended of this MonthlyRewardSummary.
        :rtype: datetime
        """
        return self._time_usage_ended

    @time_usage_ended.setter
    def time_usage_ended(self, time_usage_ended):
        """
        Sets the time_usage_ended of this MonthlyRewardSummary.
        The end date and time for the usage period.


        :param time_usage_ended: The time_usage_ended of this MonthlyRewardSummary.
        :type: datetime
        """
        self._time_usage_ended = time_usage_ended

    @property
    def usage_amount(self):
        """
        Gets the usage_amount of this MonthlyRewardSummary.
        The usage amount for the usage period.


        :return: The usage_amount of this MonthlyRewardSummary.
        :rtype: float
        """
        return self._usage_amount

    @usage_amount.setter
    def usage_amount(self, usage_amount):
        """
        Sets the usage_amount of this MonthlyRewardSummary.
        The usage amount for the usage period.


        :param usage_amount: The usage_amount of this MonthlyRewardSummary.
        :type: float
        """
        self._usage_amount = usage_amount

    @property
    def eligible_usage_amount(self):
        """
        Gets the eligible_usage_amount of this MonthlyRewardSummary.
        The eligible usage amount for the usage period.


        :return: The eligible_usage_amount of this MonthlyRewardSummary.
        :rtype: float
        """
        return self._eligible_usage_amount

    @eligible_usage_amount.setter
    def eligible_usage_amount(self, eligible_usage_amount):
        """
        Sets the eligible_usage_amount of this MonthlyRewardSummary.
        The eligible usage amount for the usage period.


        :param eligible_usage_amount: The eligible_usage_amount of this MonthlyRewardSummary.
        :type: float
        """
        self._eligible_usage_amount = eligible_usage_amount

    @property
    def ineligible_usage_amount(self):
        """
        Gets the ineligible_usage_amount of this MonthlyRewardSummary.
        The ineligible usage amount for the usage period.


        :return: The ineligible_usage_amount of this MonthlyRewardSummary.
        :rtype: float
        """
        return self._ineligible_usage_amount

    @ineligible_usage_amount.setter
    def ineligible_usage_amount(self, ineligible_usage_amount):
        """
        Sets the ineligible_usage_amount of this MonthlyRewardSummary.
        The ineligible usage amount for the usage period.


        :param ineligible_usage_amount: The ineligible_usage_amount of this MonthlyRewardSummary.
        :type: float
        """
        self._ineligible_usage_amount = ineligible_usage_amount

    @property
    def usage_period_key(self):
        """
        Gets the usage_period_key of this MonthlyRewardSummary.
        The usage period ID.


        :return: The usage_period_key of this MonthlyRewardSummary.
        :rtype: str
        """
        return self._usage_period_key

    @usage_period_key.setter
    def usage_period_key(self, usage_period_key):
        """
        Sets the usage_period_key of this MonthlyRewardSummary.
        The usage period ID.


        :param usage_period_key: The usage_period_key of this MonthlyRewardSummary.
        :type: str
        """
        self._usage_period_key = usage_period_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
