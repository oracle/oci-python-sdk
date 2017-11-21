# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbHomeSummary(object):

    def __init__(self, **kwargs):
        """
        Initializes a new DbHomeSummary object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this DbHomeSummary.
        :type compartment_id: str

        :param db_system_id:
            The value to assign to the db_system_id property of this DbHomeSummary.
        :type db_system_id: str

        :param db_version:
            The value to assign to the db_version property of this DbHomeSummary.
        :type db_version: str

        :param display_name:
            The value to assign to the display_name property of this DbHomeSummary.
        :type display_name: str

        :param id:
            The value to assign to the id property of this DbHomeSummary.
        :type id: str

        :param last_patch_history_entry_id:
            The value to assign to the last_patch_history_entry_id property of this DbHomeSummary.
        :type last_patch_history_entry_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DbHomeSummary.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this DbHomeSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'db_system_id': 'str',
            'db_version': 'str',
            'display_name': 'str',
            'id': 'str',
            'last_patch_history_entry_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'db_system_id': 'dbSystemId',
            'db_version': 'dbVersion',
            'display_name': 'displayName',
            'id': 'id',
            'last_patch_history_entry_id': 'lastPatchHistoryEntryId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._db_system_id = None
        self._db_version = None
        self._display_name = None
        self._id = None
        self._last_patch_history_entry_id = None
        self._lifecycle_state = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this DbHomeSummary.
        The OCID of the compartment.


        :return: The compartment_id of this DbHomeSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DbHomeSummary.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this DbHomeSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_system_id(self):
        """
        Gets the db_system_id of this DbHomeSummary.
        The OCID of the DB System.


        :return: The db_system_id of this DbHomeSummary.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this DbHomeSummary.
        The OCID of the DB System.


        :param db_system_id: The db_system_id of this DbHomeSummary.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def db_version(self):
        """
        Gets the db_version of this DbHomeSummary.
        The Oracle database version.


        :return: The db_version of this DbHomeSummary.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this DbHomeSummary.
        The Oracle database version.


        :param db_version: The db_version of this DbHomeSummary.
        :type: str
        """
        self._db_version = db_version

    @property
    def display_name(self):
        """
        Gets the display_name of this DbHomeSummary.
        The user-provided name for the database home. It does not need to be unique.


        :return: The display_name of this DbHomeSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DbHomeSummary.
        The user-provided name for the database home. It does not need to be unique.


        :param display_name: The display_name of this DbHomeSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this DbHomeSummary.
        The OCID of the database home.


        :return: The id of this DbHomeSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DbHomeSummary.
        The OCID of the database home.


        :param id: The id of this DbHomeSummary.
        :type: str
        """
        self._id = id

    @property
    def last_patch_history_entry_id(self):
        """
        Gets the last_patch_history_entry_id of this DbHomeSummary.
        The OCID of the last patch history. This is updated as soon as a patch operation is started.


        :return: The last_patch_history_entry_id of this DbHomeSummary.
        :rtype: str
        """
        return self._last_patch_history_entry_id

    @last_patch_history_entry_id.setter
    def last_patch_history_entry_id(self, last_patch_history_entry_id):
        """
        Sets the last_patch_history_entry_id of this DbHomeSummary.
        The OCID of the last patch history. This is updated as soon as a patch operation is started.


        :param last_patch_history_entry_id: The last_patch_history_entry_id of this DbHomeSummary.
        :type: str
        """
        self._last_patch_history_entry_id = last_patch_history_entry_id

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DbHomeSummary.
        The current state of the database home.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DbHomeSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DbHomeSummary.
        The current state of the database home.


        :param lifecycle_state: The lifecycle_state of this DbHomeSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this DbHomeSummary.
        The date and time the database home was created.


        :return: The time_created of this DbHomeSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DbHomeSummary.
        The date and time the database home was created.


        :param time_created: The time_created of this DbHomeSummary.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
