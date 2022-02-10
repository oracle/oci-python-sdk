# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModifyGlobalSettingsDetails(object):
    """
    The details required to modify the global settings in Data Safe.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModifyGlobalSettingsDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_paid_usage:
            The value to assign to the is_paid_usage property of this ModifyGlobalSettingsDetails.
        :type is_paid_usage: bool

        :param online_retention_period:
            The value to assign to the online_retention_period property of this ModifyGlobalSettingsDetails.
        :type online_retention_period: int

        :param offline_retention_period:
            The value to assign to the offline_retention_period property of this ModifyGlobalSettingsDetails.
        :type offline_retention_period: int

        """
        self.swagger_types = {
            'is_paid_usage': 'bool',
            'online_retention_period': 'int',
            'offline_retention_period': 'int'
        }

        self.attribute_map = {
            'is_paid_usage': 'isPaidUsage',
            'online_retention_period': 'onlineRetentionPeriod',
            'offline_retention_period': 'offlineRetentionPeriod'
        }

        self._is_paid_usage = None
        self._online_retention_period = None
        self._offline_retention_period = None

    @property
    def is_paid_usage(self):
        """
        Gets the is_paid_usage of this ModifyGlobalSettingsDetails.
        The paid usage option chosen by the customer admin.


        :return: The is_paid_usage of this ModifyGlobalSettingsDetails.
        :rtype: bool
        """
        return self._is_paid_usage

    @is_paid_usage.setter
    def is_paid_usage(self, is_paid_usage):
        """
        Sets the is_paid_usage of this ModifyGlobalSettingsDetails.
        The paid usage option chosen by the customer admin.


        :param is_paid_usage: The is_paid_usage of this ModifyGlobalSettingsDetails.
        :type: bool
        """
        self._is_paid_usage = is_paid_usage

    @property
    def online_retention_period(self):
        """
        Gets the online_retention_period of this ModifyGlobalSettingsDetails.
        The online retention period in months.


        :return: The online_retention_period of this ModifyGlobalSettingsDetails.
        :rtype: int
        """
        return self._online_retention_period

    @online_retention_period.setter
    def online_retention_period(self, online_retention_period):
        """
        Sets the online_retention_period of this ModifyGlobalSettingsDetails.
        The online retention period in months.


        :param online_retention_period: The online_retention_period of this ModifyGlobalSettingsDetails.
        :type: int
        """
        self._online_retention_period = online_retention_period

    @property
    def offline_retention_period(self):
        """
        Gets the offline_retention_period of this ModifyGlobalSettingsDetails.
        The offline retention period in months.


        :return: The offline_retention_period of this ModifyGlobalSettingsDetails.
        :rtype: int
        """
        return self._offline_retention_period

    @offline_retention_period.setter
    def offline_retention_period(self, offline_retention_period):
        """
        Sets the offline_retention_period of this ModifyGlobalSettingsDetails.
        The offline retention period in months.


        :param offline_retention_period: The offline_retention_period of this ModifyGlobalSettingsDetails.
        :type: int
        """
        self._offline_retention_period = offline_retention_period

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
