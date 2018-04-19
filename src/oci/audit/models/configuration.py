# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Configuration(object):
    """
    Configuration model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Configuration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param retention_period_days:
            The value to assign to the retention_period_days property of this Configuration.
        :type retention_period_days: int

        """
        self.swagger_types = {
            'retention_period_days': 'int'
        }

        self.attribute_map = {
            'retention_period_days': 'retentionPeriodDays'
        }

        self._retention_period_days = None

    @property
    def retention_period_days(self):
        """
        Gets the retention_period_days of this Configuration.
        The retention period days


        :return: The retention_period_days of this Configuration.
        :rtype: int
        """
        return self._retention_period_days

    @retention_period_days.setter
    def retention_period_days(self, retention_period_days):
        """
        Sets the retention_period_days of this Configuration.
        The retention period days


        :param retention_period_days: The retention_period_days of this Configuration.
        :type: int
        """
        self._retention_period_days = retention_period_days

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
