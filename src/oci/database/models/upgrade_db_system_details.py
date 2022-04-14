# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpgradeDbSystemDetails(object):
    """
    Details for upgrading the operating system and Oracle Grid Infrastructure (GI) of a DB system.
    """

    #: A constant which can be used with the action property of a UpgradeDbSystemDetails.
    #: This constant has a value of "PRECHECK"
    ACTION_PRECHECK = "PRECHECK"

    #: A constant which can be used with the action property of a UpgradeDbSystemDetails.
    #: This constant has a value of "ROLLBACK"
    ACTION_ROLLBACK = "ROLLBACK"

    #: A constant which can be used with the action property of a UpgradeDbSystemDetails.
    #: This constant has a value of "UPDATE_SNAPSHOT_RETENTION_DAYS"
    ACTION_UPDATE_SNAPSHOT_RETENTION_DAYS = "UPDATE_SNAPSHOT_RETENTION_DAYS"

    #: A constant which can be used with the action property of a UpgradeDbSystemDetails.
    #: This constant has a value of "UPGRADE"
    ACTION_UPGRADE = "UPGRADE"

    def __init__(self, **kwargs):
        """
        Initializes a new UpgradeDbSystemDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this UpgradeDbSystemDetails.
            Allowed values for this property are: "PRECHECK", "ROLLBACK", "UPDATE_SNAPSHOT_RETENTION_DAYS", "UPGRADE"
        :type action: str

        :param snapshot_retention_period_in_days:
            The value to assign to the snapshot_retention_period_in_days property of this UpgradeDbSystemDetails.
        :type snapshot_retention_period_in_days: int

        :param new_gi_version:
            The value to assign to the new_gi_version property of this UpgradeDbSystemDetails.
        :type new_gi_version: str

        :param is_snapshot_retention_days_force_updated:
            The value to assign to the is_snapshot_retention_days_force_updated property of this UpgradeDbSystemDetails.
        :type is_snapshot_retention_days_force_updated: bool

        """
        self.swagger_types = {
            'action': 'str',
            'snapshot_retention_period_in_days': 'int',
            'new_gi_version': 'str',
            'is_snapshot_retention_days_force_updated': 'bool'
        }

        self.attribute_map = {
            'action': 'action',
            'snapshot_retention_period_in_days': 'snapshotRetentionPeriodInDays',
            'new_gi_version': 'newGiVersion',
            'is_snapshot_retention_days_force_updated': 'isSnapshotRetentionDaysForceUpdated'
        }

        self._action = None
        self._snapshot_retention_period_in_days = None
        self._new_gi_version = None
        self._is_snapshot_retention_days_force_updated = None

    @property
    def action(self):
        """
        **[Required]** Gets the action of this UpgradeDbSystemDetails.
        The operating system upgrade action.

        Allowed values for this property are: "PRECHECK", "ROLLBACK", "UPDATE_SNAPSHOT_RETENTION_DAYS", "UPGRADE"


        :return: The action of this UpgradeDbSystemDetails.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this UpgradeDbSystemDetails.
        The operating system upgrade action.


        :param action: The action of this UpgradeDbSystemDetails.
        :type: str
        """
        allowed_values = ["PRECHECK", "ROLLBACK", "UPDATE_SNAPSHOT_RETENTION_DAYS", "UPGRADE"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            raise ValueError(
                "Invalid value for `action`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._action = action

    @property
    def snapshot_retention_period_in_days(self):
        """
        Gets the snapshot_retention_period_in_days of this UpgradeDbSystemDetails.
        The retention period, in days, for the snapshot that allows you to perform a rollback of the upgrade operation. After this number of days passes, you cannot roll back the upgrade.


        :return: The snapshot_retention_period_in_days of this UpgradeDbSystemDetails.
        :rtype: int
        """
        return self._snapshot_retention_period_in_days

    @snapshot_retention_period_in_days.setter
    def snapshot_retention_period_in_days(self, snapshot_retention_period_in_days):
        """
        Sets the snapshot_retention_period_in_days of this UpgradeDbSystemDetails.
        The retention period, in days, for the snapshot that allows you to perform a rollback of the upgrade operation. After this number of days passes, you cannot roll back the upgrade.


        :param snapshot_retention_period_in_days: The snapshot_retention_period_in_days of this UpgradeDbSystemDetails.
        :type: int
        """
        self._snapshot_retention_period_in_days = snapshot_retention_period_in_days

    @property
    def new_gi_version(self):
        """
        Gets the new_gi_version of this UpgradeDbSystemDetails.
        A valid Oracle Grid Infrastructure (GI) software version.


        :return: The new_gi_version of this UpgradeDbSystemDetails.
        :rtype: str
        """
        return self._new_gi_version

    @new_gi_version.setter
    def new_gi_version(self, new_gi_version):
        """
        Sets the new_gi_version of this UpgradeDbSystemDetails.
        A valid Oracle Grid Infrastructure (GI) software version.


        :param new_gi_version: The new_gi_version of this UpgradeDbSystemDetails.
        :type: str
        """
        self._new_gi_version = new_gi_version

    @property
    def is_snapshot_retention_days_force_updated(self):
        """
        Gets the is_snapshot_retention_days_force_updated of this UpgradeDbSystemDetails.
        If true, rollback time is updated even if operating system upgrade history contains errors.


        :return: The is_snapshot_retention_days_force_updated of this UpgradeDbSystemDetails.
        :rtype: bool
        """
        return self._is_snapshot_retention_days_force_updated

    @is_snapshot_retention_days_force_updated.setter
    def is_snapshot_retention_days_force_updated(self, is_snapshot_retention_days_force_updated):
        """
        Sets the is_snapshot_retention_days_force_updated of this UpgradeDbSystemDetails.
        If true, rollback time is updated even if operating system upgrade history contains errors.


        :param is_snapshot_retention_days_force_updated: The is_snapshot_retention_days_force_updated of this UpgradeDbSystemDetails.
        :type: bool
        """
        self._is_snapshot_retention_days_force_updated = is_snapshot_retention_days_force_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
