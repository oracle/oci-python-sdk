# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseStandbySummary(object):
    """
    Autonomous Data Guard standby database details.
    """

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "UNAVAILABLE"
    LIFECYCLE_STATE_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "RESTORE_IN_PROGRESS"
    LIFECYCLE_STATE_RESTORE_IN_PROGRESS = "RESTORE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "RESTORE_FAILED"
    LIFECYCLE_STATE_RESTORE_FAILED = "RESTORE_FAILED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "BACKUP_IN_PROGRESS"
    LIFECYCLE_STATE_BACKUP_IN_PROGRESS = "BACKUP_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "SCALE_IN_PROGRESS"
    LIFECYCLE_STATE_SCALE_IN_PROGRESS = "SCALE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "AVAILABLE_NEEDS_ATTENTION"
    LIFECYCLE_STATE_AVAILABLE_NEEDS_ATTENTION = "AVAILABLE_NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_STATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "RESTARTING"
    LIFECYCLE_STATE_RESTARTING = "RESTARTING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "RECREATING"
    LIFECYCLE_STATE_RECREATING = "RECREATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "ROLE_CHANGE_IN_PROGRESS"
    LIFECYCLE_STATE_ROLE_CHANGE_IN_PROGRESS = "ROLE_CHANGE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseStandbySummary.
    #: This constant has a value of "UPGRADING"
    LIFECYCLE_STATE_UPGRADING = "UPGRADING"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseStandbySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param lag_time_in_seconds:
            The value to assign to the lag_time_in_seconds property of this AutonomousDatabaseStandbySummary.
        :type lag_time_in_seconds: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousDatabaseStandbySummary.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS", "RESTARTING", "RECREATING", "ROLE_CHANGE_IN_PROGRESS", "UPGRADING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AutonomousDatabaseStandbySummary.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'lag_time_in_seconds': 'int',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'lag_time_in_seconds': 'lagTimeInSeconds',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._lag_time_in_seconds = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def lag_time_in_seconds(self):
        """
        Gets the lag_time_in_seconds of this AutonomousDatabaseStandbySummary.
        The amount of time, in seconds, that the data of the standby database lags the data of the primary database. Can be used to determine the potential data loss in the event of a failover.


        :return: The lag_time_in_seconds of this AutonomousDatabaseStandbySummary.
        :rtype: int
        """
        return self._lag_time_in_seconds

    @lag_time_in_seconds.setter
    def lag_time_in_seconds(self, lag_time_in_seconds):
        """
        Sets the lag_time_in_seconds of this AutonomousDatabaseStandbySummary.
        The amount of time, in seconds, that the data of the standby database lags the data of the primary database. Can be used to determine the potential data loss in the event of a failover.


        :param lag_time_in_seconds: The lag_time_in_seconds of this AutonomousDatabaseStandbySummary.
        :type: int
        """
        self._lag_time_in_seconds = lag_time_in_seconds

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this AutonomousDatabaseStandbySummary.
        The current state of the Autonomous Database.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS", "RESTARTING", "RECREATING", "ROLE_CHANGE_IN_PROGRESS", "UPGRADING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AutonomousDatabaseStandbySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutonomousDatabaseStandbySummary.
        The current state of the Autonomous Database.


        :param lifecycle_state: The lifecycle_state of this AutonomousDatabaseStandbySummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS", "RESTARTING", "RECREATING", "ROLE_CHANGE_IN_PROGRESS", "UPGRADING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AutonomousDatabaseStandbySummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this AutonomousDatabaseStandbySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AutonomousDatabaseStandbySummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this AutonomousDatabaseStandbySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
