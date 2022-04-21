# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HorizontalScalingScheduleDetails(object):
    """
    Details of a horizontal scaling schedule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HorizontalScalingScheduleDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.bds.models.DayBasedHorizontalScalingScheduleDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param schedule_type:
            The value to assign to the schedule_type property of this HorizontalScalingScheduleDetails.
        :type schedule_type: str

        """
        self.swagger_types = {
            'schedule_type': 'str'
        }

        self.attribute_map = {
            'schedule_type': 'scheduleType'
        }

        self._schedule_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['scheduleType']

        if type == 'DAY_BASED':
            return 'DayBasedHorizontalScalingScheduleDetails'
        else:
            return 'HorizontalScalingScheduleDetails'

    @property
    def schedule_type(self):
        """
        Gets the schedule_type of this HorizontalScalingScheduleDetails.
        The type of schedule.


        :return: The schedule_type of this HorizontalScalingScheduleDetails.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this HorizontalScalingScheduleDetails.
        The type of schedule.


        :param schedule_type: The schedule_type of this HorizontalScalingScheduleDetails.
        :type: str
        """
        self._schedule_type = schedule_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
