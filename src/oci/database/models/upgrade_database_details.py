# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpgradeDatabaseDetails(object):
    """
    Details for upgrading a database to a specific Oracle Database version.
    """

    #: A constant which can be used with the action property of a UpgradeDatabaseDetails.
    #: This constant has a value of "PRECHECK"
    ACTION_PRECHECK = "PRECHECK"

    #: A constant which can be used with the action property of a UpgradeDatabaseDetails.
    #: This constant has a value of "UPGRADE"
    ACTION_UPGRADE = "UPGRADE"

    #: A constant which can be used with the action property of a UpgradeDatabaseDetails.
    #: This constant has a value of "ROLLBACK"
    ACTION_ROLLBACK = "ROLLBACK"

    def __init__(self, **kwargs):
        """
        Initializes a new UpgradeDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this UpgradeDatabaseDetails.
            Allowed values for this property are: "PRECHECK", "UPGRADE", "ROLLBACK"
        :type action: str

        :param database_upgrade_source_details:
            The value to assign to the database_upgrade_source_details property of this UpgradeDatabaseDetails.
        :type database_upgrade_source_details: oci.database.models.DatabaseUpgradeSourceBase

        """
        self.swagger_types = {
            'action': 'str',
            'database_upgrade_source_details': 'DatabaseUpgradeSourceBase'
        }

        self.attribute_map = {
            'action': 'action',
            'database_upgrade_source_details': 'databaseUpgradeSourceDetails'
        }

        self._action = None
        self._database_upgrade_source_details = None

    @property
    def action(self):
        """
        **[Required]** Gets the action of this UpgradeDatabaseDetails.
        The database upgrade action.

        Allowed values for this property are: "PRECHECK", "UPGRADE", "ROLLBACK"


        :return: The action of this UpgradeDatabaseDetails.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this UpgradeDatabaseDetails.
        The database upgrade action.


        :param action: The action of this UpgradeDatabaseDetails.
        :type: str
        """
        allowed_values = ["PRECHECK", "UPGRADE", "ROLLBACK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            raise ValueError(
                "Invalid value for `action`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._action = action

    @property
    def database_upgrade_source_details(self):
        """
        Gets the database_upgrade_source_details of this UpgradeDatabaseDetails.

        :return: The database_upgrade_source_details of this UpgradeDatabaseDetails.
        :rtype: oci.database.models.DatabaseUpgradeSourceBase
        """
        return self._database_upgrade_source_details

    @database_upgrade_source_details.setter
    def database_upgrade_source_details(self, database_upgrade_source_details):
        """
        Sets the database_upgrade_source_details of this UpgradeDatabaseDetails.

        :param database_upgrade_source_details: The database_upgrade_source_details of this UpgradeDatabaseDetails.
        :type: oci.database.models.DatabaseUpgradeSourceBase
        """
        self._database_upgrade_source_details = database_upgrade_source_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
