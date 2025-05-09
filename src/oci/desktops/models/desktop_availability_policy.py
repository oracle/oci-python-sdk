# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220618


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DesktopAvailabilityPolicy(object):
    """
    Provides the start and stop schedule information for desktop availability of the desktop pool.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DesktopAvailabilityPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param start_schedule:
            The value to assign to the start_schedule property of this DesktopAvailabilityPolicy.
        :type start_schedule: oci.desktops.models.DesktopSchedule

        :param stop_schedule:
            The value to assign to the stop_schedule property of this DesktopAvailabilityPolicy.
        :type stop_schedule: oci.desktops.models.DesktopSchedule

        """
        self.swagger_types = {
            'start_schedule': 'DesktopSchedule',
            'stop_schedule': 'DesktopSchedule'
        }
        self.attribute_map = {
            'start_schedule': 'startSchedule',
            'stop_schedule': 'stopSchedule'
        }
        self._start_schedule = None
        self._stop_schedule = None

    @property
    def start_schedule(self):
        """
        **[Required]** Gets the start_schedule of this DesktopAvailabilityPolicy.

        :return: The start_schedule of this DesktopAvailabilityPolicy.
        :rtype: oci.desktops.models.DesktopSchedule
        """
        return self._start_schedule

    @start_schedule.setter
    def start_schedule(self, start_schedule):
        """
        Sets the start_schedule of this DesktopAvailabilityPolicy.

        :param start_schedule: The start_schedule of this DesktopAvailabilityPolicy.
        :type: oci.desktops.models.DesktopSchedule
        """
        self._start_schedule = start_schedule

    @property
    def stop_schedule(self):
        """
        **[Required]** Gets the stop_schedule of this DesktopAvailabilityPolicy.

        :return: The stop_schedule of this DesktopAvailabilityPolicy.
        :rtype: oci.desktops.models.DesktopSchedule
        """
        return self._stop_schedule

    @stop_schedule.setter
    def stop_schedule(self, stop_schedule):
        """
        Sets the stop_schedule of this DesktopAvailabilityPolicy.

        :param stop_schedule: The stop_schedule of this DesktopAvailabilityPolicy.
        :type: oci.desktops.models.DesktopSchedule
        """
        self._stop_schedule = stop_schedule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
