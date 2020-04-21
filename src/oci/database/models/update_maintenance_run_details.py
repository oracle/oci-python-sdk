# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMaintenanceRunDetails(object):
    """
    Describes the modification parameters for the Maintenance Run.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMaintenanceRunDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_enabled:
            The value to assign to the is_enabled property of this UpdateMaintenanceRunDetails.
        :type is_enabled: bool

        :param time_scheduled:
            The value to assign to the time_scheduled property of this UpdateMaintenanceRunDetails.
        :type time_scheduled: datetime

        """
        self.swagger_types = {
            'is_enabled': 'bool',
            'time_scheduled': 'datetime'
        }

        self.attribute_map = {
            'is_enabled': 'isEnabled',
            'time_scheduled': 'timeScheduled'
        }

        self._is_enabled = None
        self._time_scheduled = None

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this UpdateMaintenanceRunDetails.
        If set to false, skips the Maintenance Run.


        :return: The is_enabled of this UpdateMaintenanceRunDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this UpdateMaintenanceRunDetails.
        If set to false, skips the Maintenance Run.


        :param is_enabled: The is_enabled of this UpdateMaintenanceRunDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def time_scheduled(self):
        """
        Gets the time_scheduled of this UpdateMaintenanceRunDetails.
        The scheduled date and time of the Maintenance Run to update.


        :return: The time_scheduled of this UpdateMaintenanceRunDetails.
        :rtype: datetime
        """
        return self._time_scheduled

    @time_scheduled.setter
    def time_scheduled(self, time_scheduled):
        """
        Sets the time_scheduled of this UpdateMaintenanceRunDetails.
        The scheduled date and time of the Maintenance Run to update.


        :param time_scheduled: The time_scheduled of this UpdateMaintenanceRunDetails.
        :type: datetime
        """
        self._time_scheduled = time_scheduled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
