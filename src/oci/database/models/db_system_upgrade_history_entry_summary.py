# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystemUpgradeHistoryEntrySummary(object):
    """
    The summary for the record of an OS upgrade action on a DB system.
    """

    #: A constant which can be used with the action property of a DbSystemUpgradeHistoryEntrySummary.
    #: This constant has a value of "PRECHECK"
    ACTION_PRECHECK = "PRECHECK"

    #: A constant which can be used with the action property of a DbSystemUpgradeHistoryEntrySummary.
    #: This constant has a value of "ROLLBACK"
    ACTION_ROLLBACK = "ROLLBACK"

    #: A constant which can be used with the action property of a DbSystemUpgradeHistoryEntrySummary.
    #: This constant has a value of "UPDATE_SNAPSHOT_RETENTION_DAYS"
    ACTION_UPDATE_SNAPSHOT_RETENTION_DAYS = "UPDATE_SNAPSHOT_RETENTION_DAYS"

    #: A constant which can be used with the action property of a DbSystemUpgradeHistoryEntrySummary.
    #: This constant has a value of "UPGRADE"
    ACTION_UPGRADE = "UPGRADE"

    #: A constant which can be used with the lifecycle_state property of a DbSystemUpgradeHistoryEntrySummary.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a DbSystemUpgradeHistoryEntrySummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a DbSystemUpgradeHistoryEntrySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DbSystemUpgradeHistoryEntrySummary.
    #: This constant has a value of "NEEDS_ATTENTION"
    LIFECYCLE_STATE_NEEDS_ATTENTION = "NEEDS_ATTENTION"

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystemUpgradeHistoryEntrySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DbSystemUpgradeHistoryEntrySummary.
        :type id: str

        :param action:
            The value to assign to the action property of this DbSystemUpgradeHistoryEntrySummary.
            Allowed values for this property are: "PRECHECK", "ROLLBACK", "UPDATE_SNAPSHOT_RETENTION_DAYS", "UPGRADE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param new_gi_version:
            The value to assign to the new_gi_version property of this DbSystemUpgradeHistoryEntrySummary.
        :type new_gi_version: str

        :param old_gi_version:
            The value to assign to the old_gi_version property of this DbSystemUpgradeHistoryEntrySummary.
        :type old_gi_version: str

        :param snapshot_retention_period_in_days:
            The value to assign to the snapshot_retention_period_in_days property of this DbSystemUpgradeHistoryEntrySummary.
        :type snapshot_retention_period_in_days: int

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbSystemUpgradeHistoryEntrySummary.
            Allowed values for this property are: "IN_PROGRESS", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DbSystemUpgradeHistoryEntrySummary.
        :type lifecycle_details: str

        :param time_started:
            The value to assign to the time_started property of this DbSystemUpgradeHistoryEntrySummary.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this DbSystemUpgradeHistoryEntrySummary.
        :type time_ended: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'action': 'str',
            'new_gi_version': 'str',
            'old_gi_version': 'str',
            'snapshot_retention_period_in_days': 'int',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'action': 'action',
            'new_gi_version': 'newGiVersion',
            'old_gi_version': 'oldGiVersion',
            'snapshot_retention_period_in_days': 'snapshotRetentionPeriodInDays',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded'
        }

        self._id = None
        self._action = None
        self._new_gi_version = None
        self._old_gi_version = None
        self._snapshot_retention_period_in_days = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_started = None
        self._time_ended = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DbSystemUpgradeHistoryEntrySummary.
        The `OCID`__ of the upgrade history entry.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DbSystemUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbSystemUpgradeHistoryEntrySummary.
        The `OCID`__ of the upgrade history entry.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DbSystemUpgradeHistoryEntrySummary.
        :type: str
        """
        self._id = id

    @property
    def action(self):
        """
        **[Required]** Gets the action of this DbSystemUpgradeHistoryEntrySummary.
        The operating system upgrade action.

        Allowed values for this property are: "PRECHECK", "ROLLBACK", "UPDATE_SNAPSHOT_RETENTION_DAYS", "UPGRADE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this DbSystemUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this DbSystemUpgradeHistoryEntrySummary.
        The operating system upgrade action.


        :param action: The action of this DbSystemUpgradeHistoryEntrySummary.
        :type: str
        """
        allowed_values = ["PRECHECK", "ROLLBACK", "UPDATE_SNAPSHOT_RETENTION_DAYS", "UPGRADE"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def new_gi_version(self):
        """
        **[Required]** Gets the new_gi_version of this DbSystemUpgradeHistoryEntrySummary.
        A valid Oracle Grid Infrastructure (GI) software version.


        :return: The new_gi_version of this DbSystemUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._new_gi_version

    @new_gi_version.setter
    def new_gi_version(self, new_gi_version):
        """
        Sets the new_gi_version of this DbSystemUpgradeHistoryEntrySummary.
        A valid Oracle Grid Infrastructure (GI) software version.


        :param new_gi_version: The new_gi_version of this DbSystemUpgradeHistoryEntrySummary.
        :type: str
        """
        self._new_gi_version = new_gi_version

    @property
    def old_gi_version(self):
        """
        **[Required]** Gets the old_gi_version of this DbSystemUpgradeHistoryEntrySummary.
        A valid Oracle Grid Infrastructure (GI) software version.


        :return: The old_gi_version of this DbSystemUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._old_gi_version

    @old_gi_version.setter
    def old_gi_version(self, old_gi_version):
        """
        Sets the old_gi_version of this DbSystemUpgradeHistoryEntrySummary.
        A valid Oracle Grid Infrastructure (GI) software version.


        :param old_gi_version: The old_gi_version of this DbSystemUpgradeHistoryEntrySummary.
        :type: str
        """
        self._old_gi_version = old_gi_version

    @property
    def snapshot_retention_period_in_days(self):
        """
        **[Required]** Gets the snapshot_retention_period_in_days of this DbSystemUpgradeHistoryEntrySummary.
        The retention period, in days, for the snapshot that allows you to perform a rollback of the upgrade operation. After this number of days passes, you cannot roll back the upgrade.


        :return: The snapshot_retention_period_in_days of this DbSystemUpgradeHistoryEntrySummary.
        :rtype: int
        """
        return self._snapshot_retention_period_in_days

    @snapshot_retention_period_in_days.setter
    def snapshot_retention_period_in_days(self, snapshot_retention_period_in_days):
        """
        Sets the snapshot_retention_period_in_days of this DbSystemUpgradeHistoryEntrySummary.
        The retention period, in days, for the snapshot that allows you to perform a rollback of the upgrade operation. After this number of days passes, you cannot roll back the upgrade.


        :param snapshot_retention_period_in_days: The snapshot_retention_period_in_days of this DbSystemUpgradeHistoryEntrySummary.
        :type: int
        """
        self._snapshot_retention_period_in_days = snapshot_retention_period_in_days

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DbSystemUpgradeHistoryEntrySummary.
        The current state of the action.

        Allowed values for this property are: "IN_PROGRESS", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DbSystemUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbSystemUpgradeHistoryEntrySummary.
        The current state of the action.


        :param lifecycle_state: The lifecycle_state of this DbSystemUpgradeHistoryEntrySummary.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DbSystemUpgradeHistoryEntrySummary.
        A descriptive text associated with the lifecycleState.
        Typically contains additional displayable text.


        :return: The lifecycle_details of this DbSystemUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DbSystemUpgradeHistoryEntrySummary.
        A descriptive text associated with the lifecycleState.
        Typically contains additional displayable text.


        :param lifecycle_details: The lifecycle_details of this DbSystemUpgradeHistoryEntrySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this DbSystemUpgradeHistoryEntrySummary.
        The date and time when the upgrade action started.


        :return: The time_started of this DbSystemUpgradeHistoryEntrySummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this DbSystemUpgradeHistoryEntrySummary.
        The date and time when the upgrade action started.


        :param time_started: The time_started of this DbSystemUpgradeHistoryEntrySummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this DbSystemUpgradeHistoryEntrySummary.
        The date and time when the upgrade action completed


        :return: The time_ended of this DbSystemUpgradeHistoryEntrySummary.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this DbSystemUpgradeHistoryEntrySummary.
        The date and time when the upgrade action completed


        :param time_ended: The time_ended of this DbSystemUpgradeHistoryEntrySummary.
        :type: datetime
        """
        self._time_ended = time_ended

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
