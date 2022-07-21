# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrDatabaseSnapshotRangeSummary(object):
    """
    The summary data for a range of AWR snapshots.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AwrDatabaseSnapshotRangeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param awr_source_database_identifier:
            The value to assign to the awr_source_database_identifier property of this AwrDatabaseSnapshotRangeSummary.
        :type awr_source_database_identifier: str

        :param db_name:
            The value to assign to the db_name property of this AwrDatabaseSnapshotRangeSummary.
        :type db_name: str

        :param instance_list:
            The value to assign to the instance_list property of this AwrDatabaseSnapshotRangeSummary.
        :type instance_list: list[int]

        :param time_db_startup:
            The value to assign to the time_db_startup property of this AwrDatabaseSnapshotRangeSummary.
        :type time_db_startup: datetime

        :param time_first_snapshot_begin:
            The value to assign to the time_first_snapshot_begin property of this AwrDatabaseSnapshotRangeSummary.
        :type time_first_snapshot_begin: datetime

        :param time_latest_snapshot_end:
            The value to assign to the time_latest_snapshot_end property of this AwrDatabaseSnapshotRangeSummary.
        :type time_latest_snapshot_end: datetime

        :param first_snapshot_identifier:
            The value to assign to the first_snapshot_identifier property of this AwrDatabaseSnapshotRangeSummary.
        :type first_snapshot_identifier: int

        :param latest_snapshot_identifier:
            The value to assign to the latest_snapshot_identifier property of this AwrDatabaseSnapshotRangeSummary.
        :type latest_snapshot_identifier: int

        :param snapshot_count:
            The value to assign to the snapshot_count property of this AwrDatabaseSnapshotRangeSummary.
        :type snapshot_count: int

        :param snapshot_interval_in_min:
            The value to assign to the snapshot_interval_in_min property of this AwrDatabaseSnapshotRangeSummary.
        :type snapshot_interval_in_min: int

        :param db_version:
            The value to assign to the db_version property of this AwrDatabaseSnapshotRangeSummary.
        :type db_version: str

        :param snapshot_timezone:
            The value to assign to the snapshot_timezone property of this AwrDatabaseSnapshotRangeSummary.
        :type snapshot_timezone: str

        """
        self.swagger_types = {
            'awr_source_database_identifier': 'str',
            'db_name': 'str',
            'instance_list': 'list[int]',
            'time_db_startup': 'datetime',
            'time_first_snapshot_begin': 'datetime',
            'time_latest_snapshot_end': 'datetime',
            'first_snapshot_identifier': 'int',
            'latest_snapshot_identifier': 'int',
            'snapshot_count': 'int',
            'snapshot_interval_in_min': 'int',
            'db_version': 'str',
            'snapshot_timezone': 'str'
        }

        self.attribute_map = {
            'awr_source_database_identifier': 'awrSourceDatabaseIdentifier',
            'db_name': 'dbName',
            'instance_list': 'instanceList',
            'time_db_startup': 'timeDbStartup',
            'time_first_snapshot_begin': 'timeFirstSnapshotBegin',
            'time_latest_snapshot_end': 'timeLatestSnapshotEnd',
            'first_snapshot_identifier': 'firstSnapshotIdentifier',
            'latest_snapshot_identifier': 'latestSnapshotIdentifier',
            'snapshot_count': 'snapshotCount',
            'snapshot_interval_in_min': 'snapshotIntervalInMin',
            'db_version': 'dbVersion',
            'snapshot_timezone': 'snapshotTimezone'
        }

        self._awr_source_database_identifier = None
        self._db_name = None
        self._instance_list = None
        self._time_db_startup = None
        self._time_first_snapshot_begin = None
        self._time_latest_snapshot_end = None
        self._first_snapshot_identifier = None
        self._latest_snapshot_identifier = None
        self._snapshot_count = None
        self._snapshot_interval_in_min = None
        self._db_version = None
        self._snapshot_timezone = None

    @property
    def awr_source_database_identifier(self):
        """
        **[Required]** Gets the awr_source_database_identifier of this AwrDatabaseSnapshotRangeSummary.
        The internal ID of the database. The internal ID of the database is not the `OCID`__.
        It can be retrieved from the following endpoint:
        /awrHubs/{awrHubId}/awrDatabases

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The awr_source_database_identifier of this AwrDatabaseSnapshotRangeSummary.
        :rtype: str
        """
        return self._awr_source_database_identifier

    @awr_source_database_identifier.setter
    def awr_source_database_identifier(self, awr_source_database_identifier):
        """
        Sets the awr_source_database_identifier of this AwrDatabaseSnapshotRangeSummary.
        The internal ID of the database. The internal ID of the database is not the `OCID`__.
        It can be retrieved from the following endpoint:
        /awrHubs/{awrHubId}/awrDatabases

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param awr_source_database_identifier: The awr_source_database_identifier of this AwrDatabaseSnapshotRangeSummary.
        :type: str
        """
        self._awr_source_database_identifier = awr_source_database_identifier

    @property
    def db_name(self):
        """
        **[Required]** Gets the db_name of this AwrDatabaseSnapshotRangeSummary.
        The name of the database.


        :return: The db_name of this AwrDatabaseSnapshotRangeSummary.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this AwrDatabaseSnapshotRangeSummary.
        The name of the database.


        :param db_name: The db_name of this AwrDatabaseSnapshotRangeSummary.
        :type: str
        """
        self._db_name = db_name

    @property
    def instance_list(self):
        """
        Gets the instance_list of this AwrDatabaseSnapshotRangeSummary.
        The database instance numbers.


        :return: The instance_list of this AwrDatabaseSnapshotRangeSummary.
        :rtype: list[int]
        """
        return self._instance_list

    @instance_list.setter
    def instance_list(self, instance_list):
        """
        Sets the instance_list of this AwrDatabaseSnapshotRangeSummary.
        The database instance numbers.


        :param instance_list: The instance_list of this AwrDatabaseSnapshotRangeSummary.
        :type: list[int]
        """
        self._instance_list = instance_list

    @property
    def time_db_startup(self):
        """
        Gets the time_db_startup of this AwrDatabaseSnapshotRangeSummary.
        The timestamp of the database startup.


        :return: The time_db_startup of this AwrDatabaseSnapshotRangeSummary.
        :rtype: datetime
        """
        return self._time_db_startup

    @time_db_startup.setter
    def time_db_startup(self, time_db_startup):
        """
        Sets the time_db_startup of this AwrDatabaseSnapshotRangeSummary.
        The timestamp of the database startup.


        :param time_db_startup: The time_db_startup of this AwrDatabaseSnapshotRangeSummary.
        :type: datetime
        """
        self._time_db_startup = time_db_startup

    @property
    def time_first_snapshot_begin(self):
        """
        Gets the time_first_snapshot_begin of this AwrDatabaseSnapshotRangeSummary.
        The start time of the earliest snapshot.


        :return: The time_first_snapshot_begin of this AwrDatabaseSnapshotRangeSummary.
        :rtype: datetime
        """
        return self._time_first_snapshot_begin

    @time_first_snapshot_begin.setter
    def time_first_snapshot_begin(self, time_first_snapshot_begin):
        """
        Sets the time_first_snapshot_begin of this AwrDatabaseSnapshotRangeSummary.
        The start time of the earliest snapshot.


        :param time_first_snapshot_begin: The time_first_snapshot_begin of this AwrDatabaseSnapshotRangeSummary.
        :type: datetime
        """
        self._time_first_snapshot_begin = time_first_snapshot_begin

    @property
    def time_latest_snapshot_end(self):
        """
        Gets the time_latest_snapshot_end of this AwrDatabaseSnapshotRangeSummary.
        The end time of the latest snapshot.


        :return: The time_latest_snapshot_end of this AwrDatabaseSnapshotRangeSummary.
        :rtype: datetime
        """
        return self._time_latest_snapshot_end

    @time_latest_snapshot_end.setter
    def time_latest_snapshot_end(self, time_latest_snapshot_end):
        """
        Sets the time_latest_snapshot_end of this AwrDatabaseSnapshotRangeSummary.
        The end time of the latest snapshot.


        :param time_latest_snapshot_end: The time_latest_snapshot_end of this AwrDatabaseSnapshotRangeSummary.
        :type: datetime
        """
        self._time_latest_snapshot_end = time_latest_snapshot_end

    @property
    def first_snapshot_identifier(self):
        """
        Gets the first_snapshot_identifier of this AwrDatabaseSnapshotRangeSummary.
        The ID of the earliest snapshot. The snapshot identifier is not the `OCID`__.
        It can be retrieved from the following endpoint:
        /awrHubs/{awrHubId}/awrDatabaseSnapshots

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The first_snapshot_identifier of this AwrDatabaseSnapshotRangeSummary.
        :rtype: int
        """
        return self._first_snapshot_identifier

    @first_snapshot_identifier.setter
    def first_snapshot_identifier(self, first_snapshot_identifier):
        """
        Sets the first_snapshot_identifier of this AwrDatabaseSnapshotRangeSummary.
        The ID of the earliest snapshot. The snapshot identifier is not the `OCID`__.
        It can be retrieved from the following endpoint:
        /awrHubs/{awrHubId}/awrDatabaseSnapshots

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param first_snapshot_identifier: The first_snapshot_identifier of this AwrDatabaseSnapshotRangeSummary.
        :type: int
        """
        self._first_snapshot_identifier = first_snapshot_identifier

    @property
    def latest_snapshot_identifier(self):
        """
        Gets the latest_snapshot_identifier of this AwrDatabaseSnapshotRangeSummary.
        The ID of the latest snapshot. The snapshot identifier is not the `OCID`__.
        It can be retrieved from the following endpoint:
        /awrHubs/{awrHubId}/awrDatabaseSnapshots

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The latest_snapshot_identifier of this AwrDatabaseSnapshotRangeSummary.
        :rtype: int
        """
        return self._latest_snapshot_identifier

    @latest_snapshot_identifier.setter
    def latest_snapshot_identifier(self, latest_snapshot_identifier):
        """
        Sets the latest_snapshot_identifier of this AwrDatabaseSnapshotRangeSummary.
        The ID of the latest snapshot. The snapshot identifier is not the `OCID`__.
        It can be retrieved from the following endpoint:
        /awrHubs/{awrHubId}/awrDatabaseSnapshots

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param latest_snapshot_identifier: The latest_snapshot_identifier of this AwrDatabaseSnapshotRangeSummary.
        :type: int
        """
        self._latest_snapshot_identifier = latest_snapshot_identifier

    @property
    def snapshot_count(self):
        """
        Gets the snapshot_count of this AwrDatabaseSnapshotRangeSummary.
        The total number of snapshots.


        :return: The snapshot_count of this AwrDatabaseSnapshotRangeSummary.
        :rtype: int
        """
        return self._snapshot_count

    @snapshot_count.setter
    def snapshot_count(self, snapshot_count):
        """
        Sets the snapshot_count of this AwrDatabaseSnapshotRangeSummary.
        The total number of snapshots.


        :param snapshot_count: The snapshot_count of this AwrDatabaseSnapshotRangeSummary.
        :type: int
        """
        self._snapshot_count = snapshot_count

    @property
    def snapshot_interval_in_min(self):
        """
        Gets the snapshot_interval_in_min of this AwrDatabaseSnapshotRangeSummary.
        The interval time between snapshots (in minutes).


        :return: The snapshot_interval_in_min of this AwrDatabaseSnapshotRangeSummary.
        :rtype: int
        """
        return self._snapshot_interval_in_min

    @snapshot_interval_in_min.setter
    def snapshot_interval_in_min(self, snapshot_interval_in_min):
        """
        Sets the snapshot_interval_in_min of this AwrDatabaseSnapshotRangeSummary.
        The interval time between snapshots (in minutes).


        :param snapshot_interval_in_min: The snapshot_interval_in_min of this AwrDatabaseSnapshotRangeSummary.
        :type: int
        """
        self._snapshot_interval_in_min = snapshot_interval_in_min

    @property
    def db_version(self):
        """
        Gets the db_version of this AwrDatabaseSnapshotRangeSummary.
        The version of the database.


        :return: The db_version of this AwrDatabaseSnapshotRangeSummary.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this AwrDatabaseSnapshotRangeSummary.
        The version of the database.


        :param db_version: The db_version of this AwrDatabaseSnapshotRangeSummary.
        :type: str
        """
        self._db_version = db_version

    @property
    def snapshot_timezone(self):
        """
        Gets the snapshot_timezone of this AwrDatabaseSnapshotRangeSummary.
        The time zone of the snapshot. sample -  snapshotTimezone=+0 00:00:00


        :return: The snapshot_timezone of this AwrDatabaseSnapshotRangeSummary.
        :rtype: str
        """
        return self._snapshot_timezone

    @snapshot_timezone.setter
    def snapshot_timezone(self, snapshot_timezone):
        """
        Sets the snapshot_timezone of this AwrDatabaseSnapshotRangeSummary.
        The time zone of the snapshot. sample -  snapshotTimezone=+0 00:00:00


        :param snapshot_timezone: The snapshot_timezone of this AwrDatabaseSnapshotRangeSummary.
        :type: str
        """
        self._snapshot_timezone = snapshot_timezone

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
