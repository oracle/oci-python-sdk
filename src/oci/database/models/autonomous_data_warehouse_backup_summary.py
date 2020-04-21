# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDataWarehouseBackupSummary(object):
    """
    **Deprecated.** See :func:`autonomous_data_warehouse_backup_summary` for reference information about Autonomous Data Warehouse backups.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the type property of a AutonomousDataWarehouseBackupSummary.
    #: This constant has a value of "INCREMENTAL"
    TYPE_INCREMENTAL = "INCREMENTAL"

    #: A constant which can be used with the type property of a AutonomousDataWarehouseBackupSummary.
    #: This constant has a value of "FULL"
    TYPE_FULL = "FULL"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseBackupSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseBackupSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseBackupSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseBackupSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDataWarehouseBackupSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDataWarehouseBackupSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutonomousDataWarehouseBackupSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AutonomousDataWarehouseBackupSummary.
        :type compartment_id: str

        :param autonomous_data_warehouse_id:
            The value to assign to the autonomous_data_warehouse_id property of this AutonomousDataWarehouseBackupSummary.
        :type autonomous_data_warehouse_id: str

        :param display_name:
            The value to assign to the display_name property of this AutonomousDataWarehouseBackupSummary.
        :type display_name: str

        :param type:
            The value to assign to the type property of this AutonomousDataWarehouseBackupSummary.
            Allowed values for this property are: "INCREMENTAL", "FULL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param is_automatic:
            The value to assign to the is_automatic property of this AutonomousDataWarehouseBackupSummary.
        :type is_automatic: bool

        :param time_started:
            The value to assign to the time_started property of this AutonomousDataWarehouseBackupSummary.
        :type time_started: datetime

        :param time_ended:
            The value to assign to the time_ended property of this AutonomousDataWarehouseBackupSummary.
        :type time_ended: datetime

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AutonomousDataWarehouseBackupSummary.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousDataWarehouseBackupSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'autonomous_data_warehouse_id': 'str',
            'display_name': 'str',
            'type': 'str',
            'is_automatic': 'bool',
            'time_started': 'datetime',
            'time_ended': 'datetime',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'autonomous_data_warehouse_id': 'autonomousDataWarehouseId',
            'display_name': 'displayName',
            'type': 'type',
            'is_automatic': 'isAutomatic',
            'time_started': 'timeStarted',
            'time_ended': 'timeEnded',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState'
        }

        self._id = None
        self._compartment_id = None
        self._autonomous_data_warehouse_id = None
        self._display_name = None
        self._type = None
        self._is_automatic = None
        self._time_started = None
        self._time_ended = None
        self._lifecycle_details = None
        self._lifecycle_state = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutonomousDataWarehouseBackupSummary.
        The `OCID`__ of the Autonomous Data Warehouse backup.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AutonomousDataWarehouseBackupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutonomousDataWarehouseBackupSummary.
        The `OCID`__ of the Autonomous Data Warehouse backup.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AutonomousDataWarehouseBackupSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AutonomousDataWarehouseBackupSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this AutonomousDataWarehouseBackupSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AutonomousDataWarehouseBackupSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this AutonomousDataWarehouseBackupSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def autonomous_data_warehouse_id(self):
        """
        **[Required]** Gets the autonomous_data_warehouse_id of this AutonomousDataWarehouseBackupSummary.
        The `OCID`__ of the Autonomous Data Warehouse.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The autonomous_data_warehouse_id of this AutonomousDataWarehouseBackupSummary.
        :rtype: str
        """
        return self._autonomous_data_warehouse_id

    @autonomous_data_warehouse_id.setter
    def autonomous_data_warehouse_id(self, autonomous_data_warehouse_id):
        """
        Sets the autonomous_data_warehouse_id of this AutonomousDataWarehouseBackupSummary.
        The `OCID`__ of the Autonomous Data Warehouse.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param autonomous_data_warehouse_id: The autonomous_data_warehouse_id of this AutonomousDataWarehouseBackupSummary.
        :type: str
        """
        self._autonomous_data_warehouse_id = autonomous_data_warehouse_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AutonomousDataWarehouseBackupSummary.
        The user-friendly name for the backup. The name does not have to be unique.


        :return: The display_name of this AutonomousDataWarehouseBackupSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutonomousDataWarehouseBackupSummary.
        The user-friendly name for the backup. The name does not have to be unique.


        :param display_name: The display_name of this AutonomousDataWarehouseBackupSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AutonomousDataWarehouseBackupSummary.
        The type of backup.

        Allowed values for this property are: "INCREMENTAL", "FULL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AutonomousDataWarehouseBackupSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AutonomousDataWarehouseBackupSummary.
        The type of backup.


        :param type: The type of this AutonomousDataWarehouseBackupSummary.
        :type: str
        """
        allowed_values = ["INCREMENTAL", "FULL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def is_automatic(self):
        """
        **[Required]** Gets the is_automatic of this AutonomousDataWarehouseBackupSummary.
        Indicates whether the backup is user-initiated or automatic.


        :return: The is_automatic of this AutonomousDataWarehouseBackupSummary.
        :rtype: bool
        """
        return self._is_automatic

    @is_automatic.setter
    def is_automatic(self, is_automatic):
        """
        Sets the is_automatic of this AutonomousDataWarehouseBackupSummary.
        Indicates whether the backup is user-initiated or automatic.


        :param is_automatic: The is_automatic of this AutonomousDataWarehouseBackupSummary.
        :type: bool
        """
        self._is_automatic = is_automatic

    @property
    def time_started(self):
        """
        Gets the time_started of this AutonomousDataWarehouseBackupSummary.
        The date and time the backup started.


        :return: The time_started of this AutonomousDataWarehouseBackupSummary.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this AutonomousDataWarehouseBackupSummary.
        The date and time the backup started.


        :param time_started: The time_started of this AutonomousDataWarehouseBackupSummary.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_ended(self):
        """
        Gets the time_ended of this AutonomousDataWarehouseBackupSummary.
        The date and time the backup completed.


        :return: The time_ended of this AutonomousDataWarehouseBackupSummary.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this AutonomousDataWarehouseBackupSummary.
        The date and time the backup completed.


        :param time_ended: The time_ended of this AutonomousDataWarehouseBackupSummary.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AutonomousDataWarehouseBackupSummary.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this AutonomousDataWarehouseBackupSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AutonomousDataWarehouseBackupSummary.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this AutonomousDataWarehouseBackupSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutonomousDataWarehouseBackupSummary.
        The current state of the backup.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AutonomousDataWarehouseBackupSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutonomousDataWarehouseBackupSummary.
        The current state of the backup.


        :param lifecycle_state: The lifecycle_state of this AutonomousDataWarehouseBackupSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
