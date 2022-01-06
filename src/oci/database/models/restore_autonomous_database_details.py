# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RestoreAutonomousDatabaseDetails(object):
    """
    Details to restore an Oracle Autonomous Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RestoreAutonomousDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param timestamp:
            The value to assign to the timestamp property of this RestoreAutonomousDatabaseDetails.
        :type timestamp: datetime

        :param database_scn:
            The value to assign to the database_scn property of this RestoreAutonomousDatabaseDetails.
        :type database_scn: str

        :param latest:
            The value to assign to the latest property of this RestoreAutonomousDatabaseDetails.
        :type latest: bool

        """
        self.swagger_types = {
            'timestamp': 'datetime',
            'database_scn': 'str',
            'latest': 'bool'
        }

        self.attribute_map = {
            'timestamp': 'timestamp',
            'database_scn': 'databaseSCN',
            'latest': 'latest'
        }

        self._timestamp = None
        self._database_scn = None
        self._latest = None

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this RestoreAutonomousDatabaseDetails.
        The time to restore the database to.


        :return: The timestamp of this RestoreAutonomousDatabaseDetails.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this RestoreAutonomousDatabaseDetails.
        The time to restore the database to.


        :param timestamp: The timestamp of this RestoreAutonomousDatabaseDetails.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def database_scn(self):
        """
        Gets the database_scn of this RestoreAutonomousDatabaseDetails.
        Restores using the backup with the System Change Number (SCN) specified.


        :return: The database_scn of this RestoreAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._database_scn

    @database_scn.setter
    def database_scn(self, database_scn):
        """
        Sets the database_scn of this RestoreAutonomousDatabaseDetails.
        Restores using the backup with the System Change Number (SCN) specified.


        :param database_scn: The database_scn of this RestoreAutonomousDatabaseDetails.
        :type: str
        """
        self._database_scn = database_scn

    @property
    def latest(self):
        """
        Gets the latest of this RestoreAutonomousDatabaseDetails.
        Restores to the last known good state with the least possible data loss.


        :return: The latest of this RestoreAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._latest

    @latest.setter
    def latest(self, latest):
        """
        Sets the latest of this RestoreAutonomousDatabaseDetails.
        Restores to the last known good state with the least possible data loss.


        :param latest: The latest of this RestoreAutonomousDatabaseDetails.
        :type: bool
        """
        self._latest = latest

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
