# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CancelExecutionWindowDetails(object):
    """
    Describe the parameters to create a new execution window after this execution window is canceled.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CancelExecutionWindowDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_scheduled_of_new_window:
            The value to assign to the time_scheduled_of_new_window property of this CancelExecutionWindowDetails.
        :type time_scheduled_of_new_window: datetime

        :param window_duration_in_mins_of_new_window:
            The value to assign to the window_duration_in_mins_of_new_window property of this CancelExecutionWindowDetails.
        :type window_duration_in_mins_of_new_window: int

        :param is_enforced_duration_of_new_window:
            The value to assign to the is_enforced_duration_of_new_window property of this CancelExecutionWindowDetails.
        :type is_enforced_duration_of_new_window: bool

        """
        self.swagger_types = {
            'time_scheduled_of_new_window': 'datetime',
            'window_duration_in_mins_of_new_window': 'int',
            'is_enforced_duration_of_new_window': 'bool'
        }

        self.attribute_map = {
            'time_scheduled_of_new_window': 'timeScheduledOfNewWindow',
            'window_duration_in_mins_of_new_window': 'windowDurationInMinsOfNewWindow',
            'is_enforced_duration_of_new_window': 'isEnforcedDurationOfNewWindow'
        }

        self._time_scheduled_of_new_window = None
        self._window_duration_in_mins_of_new_window = None
        self._is_enforced_duration_of_new_window = None

    @property
    def time_scheduled_of_new_window(self):
        """
        **[Required]** Gets the time_scheduled_of_new_window of this CancelExecutionWindowDetails.
        New scheduled date and time of the execution window.


        :return: The time_scheduled_of_new_window of this CancelExecutionWindowDetails.
        :rtype: datetime
        """
        return self._time_scheduled_of_new_window

    @time_scheduled_of_new_window.setter
    def time_scheduled_of_new_window(self, time_scheduled_of_new_window):
        """
        Sets the time_scheduled_of_new_window of this CancelExecutionWindowDetails.
        New scheduled date and time of the execution window.


        :param time_scheduled_of_new_window: The time_scheduled_of_new_window of this CancelExecutionWindowDetails.
        :type: datetime
        """
        self._time_scheduled_of_new_window = time_scheduled_of_new_window

    @property
    def window_duration_in_mins_of_new_window(self):
        """
        **[Required]** Gets the window_duration_in_mins_of_new_window of this CancelExecutionWindowDetails.
        Duration window allows user to set a duration they plan to allocate for Scheduling window. The duration is in minutes.


        :return: The window_duration_in_mins_of_new_window of this CancelExecutionWindowDetails.
        :rtype: int
        """
        return self._window_duration_in_mins_of_new_window

    @window_duration_in_mins_of_new_window.setter
    def window_duration_in_mins_of_new_window(self, window_duration_in_mins_of_new_window):
        """
        Sets the window_duration_in_mins_of_new_window of this CancelExecutionWindowDetails.
        Duration window allows user to set a duration they plan to allocate for Scheduling window. The duration is in minutes.


        :param window_duration_in_mins_of_new_window: The window_duration_in_mins_of_new_window of this CancelExecutionWindowDetails.
        :type: int
        """
        self._window_duration_in_mins_of_new_window = window_duration_in_mins_of_new_window

    @property
    def is_enforced_duration_of_new_window(self):
        """
        Gets the is_enforced_duration_of_new_window of this CancelExecutionWindowDetails.
        Indicates if duration the user plans to allocate for scheduling window is strictly enforced. The default value is `FALSE`.


        :return: The is_enforced_duration_of_new_window of this CancelExecutionWindowDetails.
        :rtype: bool
        """
        return self._is_enforced_duration_of_new_window

    @is_enforced_duration_of_new_window.setter
    def is_enforced_duration_of_new_window(self, is_enforced_duration_of_new_window):
        """
        Sets the is_enforced_duration_of_new_window of this CancelExecutionWindowDetails.
        Indicates if duration the user plans to allocate for scheduling window is strictly enforced. The default value is `FALSE`.


        :param is_enforced_duration_of_new_window: The is_enforced_duration_of_new_window of this CancelExecutionWindowDetails.
        :type: bool
        """
        self._is_enforced_duration_of_new_window = is_enforced_duration_of_new_window

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
