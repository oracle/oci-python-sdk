# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VmClusterUpdateHistoryEntry(object):
    """
    The record of a maintenance update action performed on a specified VM cluster. Applies to Exadata Cloud@Customer instances only.
    """

    #: A constant which can be used with the update_action property of a VmClusterUpdateHistoryEntry.
    #: This constant has a value of "ROLLING_APPLY"
    UPDATE_ACTION_ROLLING_APPLY = "ROLLING_APPLY"

    #: A constant which can be used with the update_action property of a VmClusterUpdateHistoryEntry.
    #: This constant has a value of "PRECHECK"
    UPDATE_ACTION_PRECHECK = "PRECHECK"

    #: A constant which can be used with the update_action property of a VmClusterUpdateHistoryEntry.
    #: This constant has a value of "ROLLBACK"
    UPDATE_ACTION_ROLLBACK = "ROLLBACK"

    #: A constant which can be used with the update_type property of a VmClusterUpdateHistoryEntry.
    #: This constant has a value of "GI_UPGRADE"
    UPDATE_TYPE_GI_UPGRADE = "GI_UPGRADE"

    #: A constant which can be used with the update_type property of a VmClusterUpdateHistoryEntry.
    #: This constant has a value of "GI_PATCH"
    UPDATE_TYPE_GI_PATCH = "GI_PATCH"

    #: A constant which can be used with the update_type property of a VmClusterUpdateHistoryEntry.
    #: This constant has a value of "OS_UPDATE"
    UPDATE_TYPE_OS_UPDATE = "OS_UPDATE"

    #: A constant which can be used with the lifecycle_state property of a VmClusterUpdateHistoryEntry.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a VmClusterUpdateHistoryEntry.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a VmClusterUpdateHistoryEntry.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new VmClusterUpdateHistoryEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this VmClusterUpdateHistoryEntry.
        :type id: str

        :param update_id:
            The value to assign to the update_id property of this VmClusterUpdateHistoryEntry.
        :type update_id: str

        :param update_action:
            The value to assign to the update_action property of this VmClusterUpdateHistoryEntry.
            Allowed values for this property are: "ROLLING_APPLY", "PRECHECK", "ROLLBACK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type update_action: str

        :param update_type:
            The value to assign to the update_type property of this VmClusterUpdateHistoryEntry.
            Allowed values for this property are: "GI_UPGRADE", "GI_PATCH", "OS_UPDATE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type update_type: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VmClusterUpdateHistoryEntry.
            Allowed values for this property are: "IN_PROGRESS", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this VmClusterUpdateHistoryEntry.
        :type lifecycle_details: str

        :param time_started:
            The value to assign to the time_started property of this VmClusterUpdateHistoryEntry.
        :type time_started: datetime

        :param time_completed:
            The value to assign to the time_completed property of this VmClusterUpdateHistoryEntry.
        :type time_completed: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'update_id': 'str',
            'update_action': 'str',
            'update_type': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_started': 'datetime',
            'time_completed': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'update_id': 'updateId',
            'update_action': 'updateAction',
            'update_type': 'updateType',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_started': 'timeStarted',
            'time_completed': 'timeCompleted'
        }

        self._id = None
        self._update_id = None
        self._update_action = None
        self._update_type = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_started = None
        self._time_completed = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VmClusterUpdateHistoryEntry.
        The `OCID`__ of the maintenance update history entry.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this VmClusterUpdateHistoryEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VmClusterUpdateHistoryEntry.
        The `OCID`__ of the maintenance update history entry.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this VmClusterUpdateHistoryEntry.
        :type: str
        """
        self._id = id

    @property
    def update_id(self):
        """
        **[Required]** Gets the update_id of this VmClusterUpdateHistoryEntry.
        The `OCID`__ of the maintenance update.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The update_id of this VmClusterUpdateHistoryEntry.
        :rtype: str
        """
        return self._update_id

    @update_id.setter
    def update_id(self, update_id):
        """
        Sets the update_id of this VmClusterUpdateHistoryEntry.
        The `OCID`__ of the maintenance update.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param update_id: The update_id of this VmClusterUpdateHistoryEntry.
        :type: str
        """
        self._update_id = update_id

    @property
    def update_action(self):
        """
        Gets the update_action of this VmClusterUpdateHistoryEntry.
        The update action performed using this maintenance update.

        Allowed values for this property are: "ROLLING_APPLY", "PRECHECK", "ROLLBACK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The update_action of this VmClusterUpdateHistoryEntry.
        :rtype: str
        """
        return self._update_action

    @update_action.setter
    def update_action(self, update_action):
        """
        Sets the update_action of this VmClusterUpdateHistoryEntry.
        The update action performed using this maintenance update.


        :param update_action: The update_action of this VmClusterUpdateHistoryEntry.
        :type: str
        """
        allowed_values = ["ROLLING_APPLY", "PRECHECK", "ROLLBACK"]
        if not value_allowed_none_or_none_sentinel(update_action, allowed_values):
            update_action = 'UNKNOWN_ENUM_VALUE'
        self._update_action = update_action

    @property
    def update_type(self):
        """
        **[Required]** Gets the update_type of this VmClusterUpdateHistoryEntry.
        The type of VM cluster maintenance update.

        Allowed values for this property are: "GI_UPGRADE", "GI_PATCH", "OS_UPDATE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The update_type of this VmClusterUpdateHistoryEntry.
        :rtype: str
        """
        return self._update_type

    @update_type.setter
    def update_type(self, update_type):
        """
        Sets the update_type of this VmClusterUpdateHistoryEntry.
        The type of VM cluster maintenance update.


        :param update_type: The update_type of this VmClusterUpdateHistoryEntry.
        :type: str
        """
        allowed_values = ["GI_UPGRADE", "GI_PATCH", "OS_UPDATE"]
        if not value_allowed_none_or_none_sentinel(update_type, allowed_values):
            update_type = 'UNKNOWN_ENUM_VALUE'
        self._update_type = update_type

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this VmClusterUpdateHistoryEntry.
        The current lifecycle state of the maintenance update operation.

        Allowed values for this property are: "IN_PROGRESS", "SUCCEEDED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VmClusterUpdateHistoryEntry.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VmClusterUpdateHistoryEntry.
        The current lifecycle state of the maintenance update operation.


        :param lifecycle_state: The lifecycle_state of this VmClusterUpdateHistoryEntry.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "SUCCEEDED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this VmClusterUpdateHistoryEntry.
        Descriptive text providing additional details about the lifecycle state.


        :return: The lifecycle_details of this VmClusterUpdateHistoryEntry.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this VmClusterUpdateHistoryEntry.
        Descriptive text providing additional details about the lifecycle state.


        :param lifecycle_details: The lifecycle_details of this VmClusterUpdateHistoryEntry.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this VmClusterUpdateHistoryEntry.
        The date and time when the maintenance update action started.


        :return: The time_started of this VmClusterUpdateHistoryEntry.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this VmClusterUpdateHistoryEntry.
        The date and time when the maintenance update action started.


        :param time_started: The time_started of this VmClusterUpdateHistoryEntry.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_completed(self):
        """
        Gets the time_completed of this VmClusterUpdateHistoryEntry.
        The date and time when the maintenance update action completed.


        :return: The time_completed of this VmClusterUpdateHistoryEntry.
        :rtype: datetime
        """
        return self._time_completed

    @time_completed.setter
    def time_completed(self, time_completed):
        """
        Sets the time_completed of this VmClusterUpdateHistoryEntry.
        The date and time when the maintenance update action completed.


        :param time_completed: The time_completed of this VmClusterUpdateHistoryEntry.
        :type: datetime
        """
        self._time_completed = time_completed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
