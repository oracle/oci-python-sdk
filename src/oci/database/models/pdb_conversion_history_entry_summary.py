# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PdbConversionHistoryEntrySummary(object):
    """
    Details of operations performed to convert a non-container database to pluggable database.
    """

    #: A constant which can be used with the action property of a PdbConversionHistoryEntrySummary.
    #: This constant has a value of "PRECHECK"
    ACTION_PRECHECK = "PRECHECK"

    #: A constant which can be used with the action property of a PdbConversionHistoryEntrySummary.
    #: This constant has a value of "CONVERT"
    ACTION_CONVERT = "CONVERT"

    #: A constant which can be used with the action property of a PdbConversionHistoryEntrySummary.
    #: This constant has a value of "SYNC"
    ACTION_SYNC = "SYNC"

    #: A constant which can be used with the action property of a PdbConversionHistoryEntrySummary.
    #: This constant has a value of "SYNC_ROLLBACK"
    ACTION_SYNC_ROLLBACK = "SYNC_ROLLBACK"

    #: A constant which can be used with the target property of a PdbConversionHistoryEntrySummary.
    #: This constant has a value of "NEW_DATABASE"
    TARGET_NEW_DATABASE = "NEW_DATABASE"

    #: A constant which can be used with the lifecycle_state property of a PdbConversionHistoryEntrySummary.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a PdbConversionHistoryEntrySummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a PdbConversionHistoryEntrySummary.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    def __init__(self, **kwargs):
        """
        Initializes a new PdbConversionHistoryEntrySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PdbConversionHistoryEntrySummary.
        :type id: str

        :param action:
            The value to assign to the action property of this PdbConversionHistoryEntrySummary.
            Allowed values for this property are: "PRECHECK", "CONVERT", "SYNC", "SYNC_ROLLBACK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param target:
            The value to assign to the target property of this PdbConversionHistoryEntrySummary.
            Allowed values for this property are: "NEW_DATABASE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type target: str

        :param source_database_id:
            The value to assign to the source_database_id property of this PdbConversionHistoryEntrySummary.
        :type source_database_id: str

        :param target_database_id:
            The value to assign to the target_database_id property of this PdbConversionHistoryEntrySummary.
        :type target_database_id: str

        :param cdb_name:
            The value to assign to the cdb_name property of this PdbConversionHistoryEntrySummary.
        :type cdb_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PdbConversionHistoryEntrySummary.
            Allowed values for this property are: "SUCCEEDED", "FAILED", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this PdbConversionHistoryEntrySummary.
        :type lifecycle_details: str

        :param time_started:
            The value to assign to the time_started property of this PdbConversionHistoryEntrySummary.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this PdbConversionHistoryEntrySummary.
        :type time_ended: datetime

        :param additional_cdb_params:
            The value to assign to the additional_cdb_params property of this PdbConversionHistoryEntrySummary.
        :type additional_cdb_params: str

        """
        self.swagger_types = {
            'id': 'str',
            'action': 'str',
            'target': 'str',
            'source_database_id': 'str',
            'target_database_id': 'str',
            'cdb_name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'additional_cdb_params': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'action': 'action',
            'target': 'target',
            'source_database_id': 'sourceDatabaseId',
            'target_database_id': 'targetDatabaseId',
            'cdb_name': 'cdbName',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'additional_cdb_params': 'additionalCdbParams'
        }

        self._id = None
        self._action = None
        self._target = None
        self._source_database_id = None
        self._target_database_id = None
        self._cdb_name = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_started = None
        self._time_ended = None
        self._additional_cdb_params = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PdbConversionHistoryEntrySummary.
        The `OCID`__ of the database conversion history.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this PdbConversionHistoryEntrySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PdbConversionHistoryEntrySummary.
        The `OCID`__ of the database conversion history.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this PdbConversionHistoryEntrySummary.
        :type: str
        """
        self._id = id

    @property
    def action(self):
        """
        **[Required]** Gets the action of this PdbConversionHistoryEntrySummary.
        The operations used to convert a non-container database to a pluggable database.
        - Use `PRECHECK` to run a pre-check operation on non-container database prior to converting it into a pluggable database.
        - Use `CONVERT` to convert a non-container database into a pluggable database.
        - Use `SYNC` if the non-container database was manually converted into a pluggable database using the dbcli command-line utility. Databases may need to be converted manually if the CONVERT action fails when converting a non-container database using the API.
        - Use `SYNC_ROLLBACK` if the conversion of a non-container database into a pluggable database was manually rolled back using the dbcli command line utility. Conversions may need to be manually rolled back if the CONVERT action fails when converting a non-container database using the API.

        Allowed values for this property are: "PRECHECK", "CONVERT", "SYNC", "SYNC_ROLLBACK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this PdbConversionHistoryEntrySummary.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this PdbConversionHistoryEntrySummary.
        The operations used to convert a non-container database to a pluggable database.
        - Use `PRECHECK` to run a pre-check operation on non-container database prior to converting it into a pluggable database.
        - Use `CONVERT` to convert a non-container database into a pluggable database.
        - Use `SYNC` if the non-container database was manually converted into a pluggable database using the dbcli command-line utility. Databases may need to be converted manually if the CONVERT action fails when converting a non-container database using the API.
        - Use `SYNC_ROLLBACK` if the conversion of a non-container database into a pluggable database was manually rolled back using the dbcli command line utility. Conversions may need to be manually rolled back if the CONVERT action fails when converting a non-container database using the API.


        :param action: The action of this PdbConversionHistoryEntrySummary.
        :type: str
        """
        allowed_values = ["PRECHECK", "CONVERT", "SYNC", "SYNC_ROLLBACK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def target(self):
        """
        Gets the target of this PdbConversionHistoryEntrySummary.
        The target container database of the pluggable database created by the database conversion operation. Currently, the database conversion operation only supports creating the pluggable database in a new container database.
         - Use `NEW_DATABASE` to specify that the pluggable database be created within a new container database in the same database home.

        Allowed values for this property are: "NEW_DATABASE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The target of this PdbConversionHistoryEntrySummary.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this PdbConversionHistoryEntrySummary.
        The target container database of the pluggable database created by the database conversion operation. Currently, the database conversion operation only supports creating the pluggable database in a new container database.
         - Use `NEW_DATABASE` to specify that the pluggable database be created within a new container database in the same database home.


        :param target: The target of this PdbConversionHistoryEntrySummary.
        :type: str
        """
        allowed_values = ["NEW_DATABASE"]
        if not value_allowed_none_or_none_sentinel(target, allowed_values):
            target = 'UNKNOWN_ENUM_VALUE'
        self._target = target

    @property
    def source_database_id(self):
        """
        **[Required]** Gets the source_database_id of this PdbConversionHistoryEntrySummary.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_database_id of this PdbConversionHistoryEntrySummary.
        :rtype: str
        """
        return self._source_database_id

    @source_database_id.setter
    def source_database_id(self, source_database_id):
        """
        Sets the source_database_id of this PdbConversionHistoryEntrySummary.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_database_id: The source_database_id of this PdbConversionHistoryEntrySummary.
        :type: str
        """
        self._source_database_id = source_database_id

    @property
    def target_database_id(self):
        """
        Gets the target_database_id of this PdbConversionHistoryEntrySummary.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The target_database_id of this PdbConversionHistoryEntrySummary.
        :rtype: str
        """
        return self._target_database_id

    @target_database_id.setter
    def target_database_id(self, target_database_id):
        """
        Sets the target_database_id of this PdbConversionHistoryEntrySummary.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param target_database_id: The target_database_id of this PdbConversionHistoryEntrySummary.
        :type: str
        """
        self._target_database_id = target_database_id

    @property
    def cdb_name(self):
        """
        **[Required]** Gets the cdb_name of this PdbConversionHistoryEntrySummary.
        The database name. The name must begin with an alphabetic character and can contain a maximum of 8 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :return: The cdb_name of this PdbConversionHistoryEntrySummary.
        :rtype: str
        """
        return self._cdb_name

    @cdb_name.setter
    def cdb_name(self, cdb_name):
        """
        Sets the cdb_name of this PdbConversionHistoryEntrySummary.
        The database name. The name must begin with an alphabetic character and can contain a maximum of 8 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :param cdb_name: The cdb_name of this PdbConversionHistoryEntrySummary.
        :type: str
        """
        self._cdb_name = cdb_name

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this PdbConversionHistoryEntrySummary.
        Status of an operation performed during the conversion of a non-container database to a pluggable database.

        Allowed values for this property are: "SUCCEEDED", "FAILED", "IN_PROGRESS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PdbConversionHistoryEntrySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PdbConversionHistoryEntrySummary.
        Status of an operation performed during the conversion of a non-container database to a pluggable database.


        :param lifecycle_state: The lifecycle_state of this PdbConversionHistoryEntrySummary.
        :type: str
        """
        allowed_values = ["SUCCEEDED", "FAILED", "IN_PROGRESS"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this PdbConversionHistoryEntrySummary.
        Additional information about the current lifecycle state for the conversion operation.


        :return: The lifecycle_details of this PdbConversionHistoryEntrySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this PdbConversionHistoryEntrySummary.
        Additional information about the current lifecycle state for the conversion operation.


        :param lifecycle_details: The lifecycle_details of this PdbConversionHistoryEntrySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this PdbConversionHistoryEntrySummary.
        The date and time when the database conversion operation started.


        :return: The time_started of this PdbConversionHistoryEntrySummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this PdbConversionHistoryEntrySummary.
        The date and time when the database conversion operation started.


        :param time_started: The time_started of this PdbConversionHistoryEntrySummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this PdbConversionHistoryEntrySummary.
        The date and time when the database conversion operation ended.


        :return: The time_ended of this PdbConversionHistoryEntrySummary.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this PdbConversionHistoryEntrySummary.
        The date and time when the database conversion operation ended.


        :param time_ended: The time_ended of this PdbConversionHistoryEntrySummary.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def additional_cdb_params(self):
        """
        Gets the additional_cdb_params of this PdbConversionHistoryEntrySummary.
        Additional container database parameter.


        :return: The additional_cdb_params of this PdbConversionHistoryEntrySummary.
        :rtype: str
        """
        return self._additional_cdb_params

    @additional_cdb_params.setter
    def additional_cdb_params(self, additional_cdb_params):
        """
        Sets the additional_cdb_params of this PdbConversionHistoryEntrySummary.
        Additional container database parameter.


        :param additional_cdb_params: The additional_cdb_params of this PdbConversionHistoryEntrySummary.
        :type: str
        """
        self._additional_cdb_params = additional_cdb_params

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
