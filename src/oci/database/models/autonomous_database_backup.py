# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseBackup(object):
    """
    An Autonomous Database backup.
    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator. If you're an administrator who needs to write policies to give users access, see `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseBackup.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseBackup.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseBackup.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseBackup.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseBackup.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the type property of a AutonomousDatabaseBackup.
    #: This constant has a value of "INCREMENTAL"
    TYPE_INCREMENTAL = "INCREMENTAL"

    #: A constant which can be used with the type property of a AutonomousDatabaseBackup.
    #: This constant has a value of "FULL"
    TYPE_FULL = "FULL"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseBackup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param autonomous_database_id:
            The value to assign to the autonomous_database_id property of this AutonomousDatabaseBackup.
        :type autonomous_database_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AutonomousDatabaseBackup.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this AutonomousDatabaseBackup.
        :type display_name: str

        :param id:
            The value to assign to the id property of this AutonomousDatabaseBackup.
        :type id: str

        :param is_automatic:
            The value to assign to the is_automatic property of this AutonomousDatabaseBackup.
        :type is_automatic: bool

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AutonomousDatabaseBackup.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousDatabaseBackup.
            Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_ended:
            The value to assign to the time_ended property of this AutonomousDatabaseBackup.
        :type time_ended: datetime

        :param time_started:
            The value to assign to the time_started property of this AutonomousDatabaseBackup.
        :type time_started: datetime

        :param type:
            The value to assign to the type property of this AutonomousDatabaseBackup.
            Allowed values for this property are: "INCREMENTAL", "FULL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        """
        self.swagger_types = {
            'autonomous_database_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'is_automatic': 'bool',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'time_ended': 'datetime',
            'time_started': 'datetime',
            'type': 'str'
        }

        self.attribute_map = {
            'autonomous_database_id': 'autonomousDatabaseId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'is_automatic': 'isAutomatic',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'time_ended': 'timeEnded',
            'time_started': 'timeStarted',
            'type': 'type'
        }

        self._autonomous_database_id = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._is_automatic = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._time_ended = None
        self._time_started = None
        self._type = None

    @property
    def autonomous_database_id(self):
        """
        **[Required]** Gets the autonomous_database_id of this AutonomousDatabaseBackup.
        The `OCID`__ of the Autonomous Database.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The autonomous_database_id of this AutonomousDatabaseBackup.
        :rtype: str
        """
        return self._autonomous_database_id

    @autonomous_database_id.setter
    def autonomous_database_id(self, autonomous_database_id):
        """
        Sets the autonomous_database_id of this AutonomousDatabaseBackup.
        The `OCID`__ of the Autonomous Database.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param autonomous_database_id: The autonomous_database_id of this AutonomousDatabaseBackup.
        :type: str
        """
        self._autonomous_database_id = autonomous_database_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AutonomousDatabaseBackup.
        The `OCID`__ of the compartment.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this AutonomousDatabaseBackup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AutonomousDatabaseBackup.
        The `OCID`__ of the compartment.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this AutonomousDatabaseBackup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this AutonomousDatabaseBackup.
        The user-friendly name for the backup. The name does not have to be unique.


        :return: The display_name of this AutonomousDatabaseBackup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutonomousDatabaseBackup.
        The user-friendly name for the backup. The name does not have to be unique.


        :param display_name: The display_name of this AutonomousDatabaseBackup.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutonomousDatabaseBackup.
        The `OCID`__ of the Autonomous Database backup.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AutonomousDatabaseBackup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutonomousDatabaseBackup.
        The `OCID`__ of the Autonomous Database backup.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AutonomousDatabaseBackup.
        :type: str
        """
        self._id = id

    @property
    def is_automatic(self):
        """
        **[Required]** Gets the is_automatic of this AutonomousDatabaseBackup.
        Indicates whether the backup is user-initiated or automatic.


        :return: The is_automatic of this AutonomousDatabaseBackup.
        :rtype: bool
        """
        return self._is_automatic

    @is_automatic.setter
    def is_automatic(self, is_automatic):
        """
        Sets the is_automatic of this AutonomousDatabaseBackup.
        Indicates whether the backup is user-initiated or automatic.


        :param is_automatic: The is_automatic of this AutonomousDatabaseBackup.
        :type: bool
        """
        self._is_automatic = is_automatic

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AutonomousDatabaseBackup.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this AutonomousDatabaseBackup.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AutonomousDatabaseBackup.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this AutonomousDatabaseBackup.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutonomousDatabaseBackup.
        The current state of the backup.

        Allowed values for this property are: "CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AutonomousDatabaseBackup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutonomousDatabaseBackup.
        The current state of the backup.


        :param lifecycle_state: The lifecycle_state of this AutonomousDatabaseBackup.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_ended(self):
        """
        Gets the time_ended of this AutonomousDatabaseBackup.
        The date and time the backup completed.


        :return: The time_ended of this AutonomousDatabaseBackup.
        :rtype: datetime
        """
        return self._time_ended

    @time_ended.setter
    def time_ended(self, time_ended):
        """
        Sets the time_ended of this AutonomousDatabaseBackup.
        The date and time the backup completed.


        :param time_ended: The time_ended of this AutonomousDatabaseBackup.
        :type: datetime
        """
        self._time_ended = time_ended

    @property
    def time_started(self):
        """
        Gets the time_started of this AutonomousDatabaseBackup.
        The date and time the backup started.


        :return: The time_started of this AutonomousDatabaseBackup.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this AutonomousDatabaseBackup.
        The date and time the backup started.


        :param time_started: The time_started of this AutonomousDatabaseBackup.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AutonomousDatabaseBackup.
        The type of backup.

        Allowed values for this property are: "INCREMENTAL", "FULL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this AutonomousDatabaseBackup.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AutonomousDatabaseBackup.
        The type of backup.


        :param type: The type of this AutonomousDatabaseBackup.
        :type: str
        """
        allowed_values = ["INCREMENTAL", "FULL"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
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
