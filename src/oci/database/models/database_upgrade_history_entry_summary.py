# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseUpgradeHistoryEntrySummary(object):
    """
    The Database service supports the upgrade history of databases.

    To use any of the API operations, you must be authorized in an IAM policy. If you are not authorized, talk to an administrator. If you are an administrator who needs to write policies to give users access, see `Getting Started with Policies`__.

    For information about access control and compartments, see
    `Overview of the Identity Service`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm
    """

    #: A constant which can be used with the action property of a DatabaseUpgradeHistoryEntrySummary.
    #: This constant has a value of "PRECHECK"
    ACTION_PRECHECK = "PRECHECK"

    #: A constant which can be used with the action property of a DatabaseUpgradeHistoryEntrySummary.
    #: This constant has a value of "UPGRADE"
    ACTION_UPGRADE = "UPGRADE"

    #: A constant which can be used with the action property of a DatabaseUpgradeHistoryEntrySummary.
    #: This constant has a value of "ROLLBACK"
    ACTION_ROLLBACK = "ROLLBACK"

    #: A constant which can be used with the source property of a DatabaseUpgradeHistoryEntrySummary.
    #: This constant has a value of "DB_HOME"
    SOURCE_DB_HOME = "DB_HOME"

    #: A constant which can be used with the source property of a DatabaseUpgradeHistoryEntrySummary.
    #: This constant has a value of "DB_VERSION"
    SOURCE_DB_VERSION = "DB_VERSION"

    #: A constant which can be used with the source property of a DatabaseUpgradeHistoryEntrySummary.
    #: This constant has a value of "DB_SOFTWARE_IMAGE"
    SOURCE_DB_SOFTWARE_IMAGE = "DB_SOFTWARE_IMAGE"

    #: A constant which can be used with the lifecycle_state property of a DatabaseUpgradeHistoryEntrySummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a DatabaseUpgradeHistoryEntrySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a DatabaseUpgradeHistoryEntrySummary.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseUpgradeHistoryEntrySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DatabaseUpgradeHistoryEntrySummary.
        :type id: str

        :param action:
            The value to assign to the action property of this DatabaseUpgradeHistoryEntrySummary.
            Allowed values for this property are: "PRECHECK", "UPGRADE", "ROLLBACK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param source:
            The value to assign to the source property of this DatabaseUpgradeHistoryEntrySummary.
            Allowed values for this property are: "DB_HOME", "DB_VERSION", "DB_SOFTWARE_IMAGE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type source: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DatabaseUpgradeHistoryEntrySummary.
            Allowed values for this property are: "SUCCEEDED", "FAILED", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DatabaseUpgradeHistoryEntrySummary.
        :type lifecycle_details: str

        :param target_db_version:
            The value to assign to the target_db_version property of this DatabaseUpgradeHistoryEntrySummary.
        :type target_db_version: str

        :param target_database_software_image_id:
            The value to assign to the target_database_software_image_id property of this DatabaseUpgradeHistoryEntrySummary.
        :type target_database_software_image_id: str

        :param target_db_home_id:
            The value to assign to the target_db_home_id property of this DatabaseUpgradeHistoryEntrySummary.
        :type target_db_home_id: str

        :param source_db_home_id:
            The value to assign to the source_db_home_id property of this DatabaseUpgradeHistoryEntrySummary.
        :type source_db_home_id: str

        :param time_started:
            The value to assign to the time_started property of this DatabaseUpgradeHistoryEntrySummary.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this DatabaseUpgradeHistoryEntrySummary.
        :type time_ended: datetime

        :param options:
            The value to assign to the options property of this DatabaseUpgradeHistoryEntrySummary.
        :type options: str

        """
        self.swagger_types = {
            'id': 'str',
            'action': 'str',
            'source': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'target_db_version': 'str',
            'target_database_software_image_id': 'str',
            'target_db_home_id': 'str',
            'source_db_home_id': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'options': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'action': 'action',
            'source': 'source',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'target_db_version': 'targetDBVersion',
            'target_database_software_image_id': 'targetDatabaseSoftwareImageId',
            'target_db_home_id': 'targetDbHomeId',
            'source_db_home_id': 'sourceDbHomeId',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'options': 'options'
        }

        self._id = None
        self._action = None
        self._source = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._target_db_version = None
        self._target_database_software_image_id = None
        self._target_db_home_id = None
        self._source_db_home_id = None
        self._time_started = None
        self._time_ended = None
        self._options = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DatabaseUpgradeHistoryEntrySummary.
        The `OCID`__ of the database upgrade history.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DatabaseUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DatabaseUpgradeHistoryEntrySummary.
        The `OCID`__ of the database upgrade history.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DatabaseUpgradeHistoryEntrySummary.
        :type: str
        """
        self._id = id

    @property
    def action(self):
        """
        **[Required]** Gets the action of this DatabaseUpgradeHistoryEntrySummary.
        The database upgrade action.

        Allowed values for this property are: "PRECHECK", "UPGRADE", "ROLLBACK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this DatabaseUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this DatabaseUpgradeHistoryEntrySummary.
        The database upgrade action.


        :param action: The action of this DatabaseUpgradeHistoryEntrySummary.
        :type: str
        """
        allowed_values = ["PRECHECK", "UPGRADE", "ROLLBACK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def source(self):
        """
        Gets the source of this DatabaseUpgradeHistoryEntrySummary.
        The source of the Oracle Database software to be used for the upgrade.
         - Use `DB_HOME` to specify an existing Database Home to upgrade the database. The database is moved to the target Database Home and makes use of the Oracle Database software version of the target Database Home.
         - Use `DB_VERSION` to specify a generally-available Oracle Database software version to upgrade the database.
         - Use `DB_SOFTWARE_IMAGE` to specify a `database software image`__ to upgrade the database.

        __ https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/databasesoftwareimage.htm

        Allowed values for this property are: "DB_HOME", "DB_VERSION", "DB_SOFTWARE_IMAGE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The source of this DatabaseUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this DatabaseUpgradeHistoryEntrySummary.
        The source of the Oracle Database software to be used for the upgrade.
         - Use `DB_HOME` to specify an existing Database Home to upgrade the database. The database is moved to the target Database Home and makes use of the Oracle Database software version of the target Database Home.
         - Use `DB_VERSION` to specify a generally-available Oracle Database software version to upgrade the database.
         - Use `DB_SOFTWARE_IMAGE` to specify a `database software image`__ to upgrade the database.

        __ https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/databasesoftwareimage.htm


        :param source: The source of this DatabaseUpgradeHistoryEntrySummary.
        :type: str
        """
        allowed_values = ["DB_HOME", "DB_VERSION", "DB_SOFTWARE_IMAGE"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            source = 'UNKNOWN_ENUM_VALUE'
        self._source = source

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DatabaseUpgradeHistoryEntrySummary.
        Status of database upgrade history SUCCEEDED|IN_PROGRESS|FAILED.

        Allowed values for this property are: "SUCCEEDED", "FAILED", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DatabaseUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DatabaseUpgradeHistoryEntrySummary.
        Status of database upgrade history SUCCEEDED|IN_PROGRESS|FAILED.


        :param lifecycle_state: The lifecycle_state of this DatabaseUpgradeHistoryEntrySummary.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED", "IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DatabaseUpgradeHistoryEntrySummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this DatabaseUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DatabaseUpgradeHistoryEntrySummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this DatabaseUpgradeHistoryEntrySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def target_db_version(self):
        """
        Gets the target_db_version of this DatabaseUpgradeHistoryEntrySummary.
        A valid Oracle Database version. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :return: The target_db_version of this DatabaseUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._target_db_version

    @target_db_version.setter
    def target_db_version(self, target_db_version):
        """
        Sets the target_db_version of this DatabaseUpgradeHistoryEntrySummary.
        A valid Oracle Database version. To get a list of supported versions, use the :func:`list_db_versions` operation.


        :param target_db_version: The target_db_version of this DatabaseUpgradeHistoryEntrySummary.
        :type: str
        """
        self._target_db_version = target_db_version

    @property
    def target_database_software_image_id(self):
        """
        Gets the target_database_software_image_id of this DatabaseUpgradeHistoryEntrySummary.
        the database software image used for upgrading database.


        :return: The target_database_software_image_id of this DatabaseUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._target_database_software_image_id

    @target_database_software_image_id.setter
    def target_database_software_image_id(self, target_database_software_image_id):
        """
        Sets the target_database_software_image_id of this DatabaseUpgradeHistoryEntrySummary.
        the database software image used for upgrading database.


        :param target_database_software_image_id: The target_database_software_image_id of this DatabaseUpgradeHistoryEntrySummary.
        :type: str
        """
        self._target_database_software_image_id = target_database_software_image_id

    @property
    def target_db_home_id(self):
        """
        Gets the target_db_home_id of this DatabaseUpgradeHistoryEntrySummary.
        The `OCID`__ of the Database Home.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The target_db_home_id of this DatabaseUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._target_db_home_id

    @target_db_home_id.setter
    def target_db_home_id(self, target_db_home_id):
        """
        Sets the target_db_home_id of this DatabaseUpgradeHistoryEntrySummary.
        The `OCID`__ of the Database Home.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param target_db_home_id: The target_db_home_id of this DatabaseUpgradeHistoryEntrySummary.
        :type: str
        """
        self._target_db_home_id = target_db_home_id

    @property
    def source_db_home_id(self):
        """
        Gets the source_db_home_id of this DatabaseUpgradeHistoryEntrySummary.
        The `OCID`__ of the Database Home.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_db_home_id of this DatabaseUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._source_db_home_id

    @source_db_home_id.setter
    def source_db_home_id(self, source_db_home_id):
        """
        Sets the source_db_home_id of this DatabaseUpgradeHistoryEntrySummary.
        The `OCID`__ of the Database Home.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_db_home_id: The source_db_home_id of this DatabaseUpgradeHistoryEntrySummary.
        :type: str
        """
        self._source_db_home_id = source_db_home_id

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this DatabaseUpgradeHistoryEntrySummary.
        The date and time when the database upgrade started.


        :return: The time_started of this DatabaseUpgradeHistoryEntrySummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this DatabaseUpgradeHistoryEntrySummary.
        The date and time when the database upgrade started.


        :param time_started: The time_started of this DatabaseUpgradeHistoryEntrySummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this DatabaseUpgradeHistoryEntrySummary.
        The date and time when the database upgrade ended.


        :return: The time_ended of this DatabaseUpgradeHistoryEntrySummary.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this DatabaseUpgradeHistoryEntrySummary.
        The date and time when the database upgrade ended.


        :param time_ended: The time_ended of this DatabaseUpgradeHistoryEntrySummary.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def options(self):
        """
        Gets the options of this DatabaseUpgradeHistoryEntrySummary.
        Additional upgrade options supported by DBUA(Database Upgrade Assistant).
        Example: \"-upgradeTimezone false -keepEvents\"


        :return: The options of this DatabaseUpgradeHistoryEntrySummary.
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this DatabaseUpgradeHistoryEntrySummary.
        Additional upgrade options supported by DBUA(Database Upgrade Assistant).
        Example: \"-upgradeTimezone false -keepEvents\"


        :param options: The options of this DatabaseUpgradeHistoryEntrySummary.
        :type: str
        """
        self._options = options

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
