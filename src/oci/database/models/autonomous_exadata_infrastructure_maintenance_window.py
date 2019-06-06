# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousExadataInfrastructureMaintenanceWindow(object):
    """
    Autonomous Exadata Infrastructure maintenance window details for quarterly patching.
    """

    #: A constant which can be used with the day_of_week property of a AutonomousExadataInfrastructureMaintenanceWindow.
    #: This constant has a value of "ANY"
    DAY_OF_WEEK_ANY = "ANY"

    #: A constant which can be used with the day_of_week property of a AutonomousExadataInfrastructureMaintenanceWindow.
    #: This constant has a value of "SUNDAY"
    DAY_OF_WEEK_SUNDAY = "SUNDAY"

    #: A constant which can be used with the day_of_week property of a AutonomousExadataInfrastructureMaintenanceWindow.
    #: This constant has a value of "MONDAY"
    DAY_OF_WEEK_MONDAY = "MONDAY"

    #: A constant which can be used with the day_of_week property of a AutonomousExadataInfrastructureMaintenanceWindow.
    #: This constant has a value of "TUESDAY"
    DAY_OF_WEEK_TUESDAY = "TUESDAY"

    #: A constant which can be used with the day_of_week property of a AutonomousExadataInfrastructureMaintenanceWindow.
    #: This constant has a value of "WEDNESDAY"
    DAY_OF_WEEK_WEDNESDAY = "WEDNESDAY"

    #: A constant which can be used with the day_of_week property of a AutonomousExadataInfrastructureMaintenanceWindow.
    #: This constant has a value of "THURSDAY"
    DAY_OF_WEEK_THURSDAY = "THURSDAY"

    #: A constant which can be used with the day_of_week property of a AutonomousExadataInfrastructureMaintenanceWindow.
    #: This constant has a value of "FRIDAY"
    DAY_OF_WEEK_FRIDAY = "FRIDAY"

    #: A constant which can be used with the day_of_week property of a AutonomousExadataInfrastructureMaintenanceWindow.
    #: This constant has a value of "SATURDAY"
    DAY_OF_WEEK_SATURDAY = "SATURDAY"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousExadataInfrastructureMaintenanceWindow object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param day_of_week:
            The value to assign to the day_of_week property of this AutonomousExadataInfrastructureMaintenanceWindow.
            Allowed values for this property are: "ANY", "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"
        :type day_of_week: str

        :param hour_of_day:
            The value to assign to the hour_of_day property of this AutonomousExadataInfrastructureMaintenanceWindow.
        :type hour_of_day: int

        """
        self.swagger_types = {
            'day_of_week': 'str',
            'hour_of_day': 'int'
        }

        self.attribute_map = {
            'day_of_week': 'dayOfWeek',
            'hour_of_day': 'hourOfDay'
        }

        self._day_of_week = None
        self._hour_of_day = None

    @property
    def day_of_week(self):
        """
        **[Required]** Gets the day_of_week of this AutonomousExadataInfrastructureMaintenanceWindow.
        Day of the week that the patch should be applied to the Autonomous Exadata Infrastructure. Patches are applied during the first week of the quarter.

        Allowed values for this property are: "ANY", "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"


        :return: The day_of_week of this AutonomousExadataInfrastructureMaintenanceWindow.
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """
        Sets the day_of_week of this AutonomousExadataInfrastructureMaintenanceWindow.
        Day of the week that the patch should be applied to the Autonomous Exadata Infrastructure. Patches are applied during the first week of the quarter.


        :param day_of_week: The day_of_week of this AutonomousExadataInfrastructureMaintenanceWindow.
        :type: str
        """
        allowed_values = ["ANY", "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
        if not value_allowed_none_or_none_sentinel(day_of_week, allowed_values):
            raise ValueError(
                "Invalid value for `day_of_week`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._day_of_week = day_of_week

    @property
    def hour_of_day(self):
        """
        Gets the hour_of_day of this AutonomousExadataInfrastructureMaintenanceWindow.
        Hour of the day that the patch should be applied.


        :return: The hour_of_day of this AutonomousExadataInfrastructureMaintenanceWindow.
        :rtype: int
        """
        return self._hour_of_day

    @hour_of_day.setter
    def hour_of_day(self, hour_of_day):
        """
        Sets the hour_of_day of this AutonomousExadataInfrastructureMaintenanceWindow.
        Hour of the day that the patch should be applied.


        :param hour_of_day: The hour_of_day of this AutonomousExadataInfrastructureMaintenanceWindow.
        :type: int
        """
        self._hour_of_day = hour_of_day

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
