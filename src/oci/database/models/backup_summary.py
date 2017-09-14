# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class BackupSummary(object):

    def __init__(self):

        self.swagger_types = {
            'compartment_id': 'str',
            'database_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'time_ended': 'datetime',
            'time_started': 'datetime',
            'type': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'database_id': 'databaseId',
            'display_name': 'displayName',
            'id': 'id',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'time_ended': 'timeEnded',
            'time_started': 'timeStarted',
            'type': 'type'
        }

        self._compartment_id = None
        self._database_id = None
        self._display_name = None
        self._id = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._time_ended = None
        self._time_started = None
        self._type = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this BackupSummary.
        The OCID of the compartment.


        :return: The compartment_id of this BackupSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this BackupSummary.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this BackupSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def database_id(self):
        """
        Gets the database_id of this BackupSummary.
        The OCID of the database.


        :return: The database_id of this BackupSummary.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this BackupSummary.
        The OCID of the database.


        :param database_id: The database_id of this BackupSummary.
        :type: str
        """
        self._database_id = database_id

    @property
    def display_name(self):
        """
        Gets the display_name of this BackupSummary.
        The user-friendly name for the Backup. It does not have to be unique.


        :return: The display_name of this BackupSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BackupSummary.
        The user-friendly name for the Backup. It does not have to be unique.


        :param display_name: The display_name of this BackupSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this BackupSummary.
        The OCID of the backup.


        :return: The id of this BackupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BackupSummary.
        The OCID of the backup.


        :param id: The id of this BackupSummary.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this BackupSummary.
        Additional information about the current lifecycleState.


        :return: The lifecycle_details of this BackupSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this BackupSummary.
        Additional information about the current lifecycleState.


        :param lifecycle_details: The lifecycle_details of this BackupSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this BackupSummary.
        The current state of the backup.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this BackupSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BackupSummary.
        The current state of the backup.


        :param lifecycle_state: The lifecycle_state of this BackupSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_ended(self):
        """
        Gets the time_ended of this BackupSummary.
        The date and time the backup was completed.


        :return: The time_ended of this BackupSummary.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this BackupSummary.
        The date and time the backup was completed.


        :param time_ended: The time_ended of this BackupSummary.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def time_started(self):
        """
        Gets the time_started of this BackupSummary.
        The date and time the backup starts.


        :return: The time_started of this BackupSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this BackupSummary.
        The date and time the backup starts.


        :param time_started: The time_started of this BackupSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def type(self):
        """
        Gets the type of this BackupSummary.
        The default backup type is INCREMENTAL

        Allowed values for this property are: "INCREMENTAL", "FULL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this BackupSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this BackupSummary.
        The default backup type is INCREMENTAL


        :param type: The type of this BackupSummary.
        :type: str
        """
        allowed_values = ["INCREMENTAL", "FULL"]
        if type not in allowed_values:
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
