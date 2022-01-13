# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseDataguardAssociation(object):
    """
    The properties that define dataguard association between two different Autonomous Databases.
    Note that Autonomous Databases inherit DataGuard association from parent Autonomous Container Database.
    No actions can be taken on AutonomousDatabaseDataguardAssociation, usage is strictly informational.
    """

    #: A constant which can be used with the role property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "PRIMARY"
    ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the role property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "STANDBY"
    ROLE_STANDBY = "STANDBY"

    #: A constant which can be used with the role property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "DISABLED_STANDBY"
    ROLE_DISABLED_STANDBY = "DISABLED_STANDBY"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "ROLE_CHANGE_IN_PROGRESS"
    LIFECYCLE_STATE_ROLE_CHANGE_IN_PROGRESS = "ROLE_CHANGE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "UNAVAILABLE"
    LIFECYCLE_STATE_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the peer_role property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "PRIMARY"
    PEER_ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the peer_role property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "STANDBY"
    PEER_ROLE_STANDBY = "STANDBY"

    #: A constant which can be used with the peer_role property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "DISABLED_STANDBY"
    PEER_ROLE_DISABLED_STANDBY = "DISABLED_STANDBY"

    #: A constant which can be used with the peer_autonomous_database_life_cycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "PROVISIONING"
    PEER_AUTONOMOUS_DATABASE_LIFE_CYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the peer_autonomous_database_life_cycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "AVAILABLE"
    PEER_AUTONOMOUS_DATABASE_LIFE_CYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the peer_autonomous_database_life_cycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "ROLE_CHANGE_IN_PROGRESS"
    PEER_AUTONOMOUS_DATABASE_LIFE_CYCLE_STATE_ROLE_CHANGE_IN_PROGRESS = "ROLE_CHANGE_IN_PROGRESS"

    #: A constant which can be used with the peer_autonomous_database_life_cycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "TERMINATING"
    PEER_AUTONOMOUS_DATABASE_LIFE_CYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the peer_autonomous_database_life_cycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "TERMINATED"
    PEER_AUTONOMOUS_DATABASE_LIFE_CYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the peer_autonomous_database_life_cycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "FAILED"
    PEER_AUTONOMOUS_DATABASE_LIFE_CYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the peer_autonomous_database_life_cycle_state property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "UNAVAILABLE"
    PEER_AUTONOMOUS_DATABASE_LIFE_CYCLE_STATE_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the protection_mode property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "MAXIMUM_AVAILABILITY"
    PROTECTION_MODE_MAXIMUM_AVAILABILITY = "MAXIMUM_AVAILABILITY"

    #: A constant which can be used with the protection_mode property of a AutonomousDatabaseDataguardAssociation.
    #: This constant has a value of "MAXIMUM_PERFORMANCE"
    PROTECTION_MODE_MAXIMUM_PERFORMANCE = "MAXIMUM_PERFORMANCE"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseDataguardAssociation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutonomousDatabaseDataguardAssociation.
        :type id: str

        :param autonomous_database_id:
            The value to assign to the autonomous_database_id property of this AutonomousDatabaseDataguardAssociation.
        :type autonomous_database_id: str

        :param role:
            The value to assign to the role property of this AutonomousDatabaseDataguardAssociation.
            Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousDatabaseDataguardAssociation.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ROLE_CHANGE_IN_PROGRESS", "TERMINATING", "TERMINATED", "FAILED", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AutonomousDatabaseDataguardAssociation.
        :type lifecycle_details: str

        :param peer_role:
            The value to assign to the peer_role property of this AutonomousDatabaseDataguardAssociation.
            Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type peer_role: str

        :param peer_autonomous_database_id:
            The value to assign to the peer_autonomous_database_id property of this AutonomousDatabaseDataguardAssociation.
        :type peer_autonomous_database_id: str

        :param peer_autonomous_database_life_cycle_state:
            The value to assign to the peer_autonomous_database_life_cycle_state property of this AutonomousDatabaseDataguardAssociation.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ROLE_CHANGE_IN_PROGRESS", "TERMINATING", "TERMINATED", "FAILED", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type peer_autonomous_database_life_cycle_state: str

        :param protection_mode:
            The value to assign to the protection_mode property of this AutonomousDatabaseDataguardAssociation.
            Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protection_mode: str

        :param apply_lag:
            The value to assign to the apply_lag property of this AutonomousDatabaseDataguardAssociation.
        :type apply_lag: str

        :param apply_rate:
            The value to assign to the apply_rate property of this AutonomousDatabaseDataguardAssociation.
        :type apply_rate: str

        :param is_automatic_failover_enabled:
            The value to assign to the is_automatic_failover_enabled property of this AutonomousDatabaseDataguardAssociation.
        :type is_automatic_failover_enabled: bool

        :param transport_lag:
            The value to assign to the transport_lag property of this AutonomousDatabaseDataguardAssociation.
        :type transport_lag: str

        :param time_last_synced:
            The value to assign to the time_last_synced property of this AutonomousDatabaseDataguardAssociation.
        :type time_last_synced: datetime

        :param time_created:
            The value to assign to the time_created property of this AutonomousDatabaseDataguardAssociation.
        :type time_created: datetime

        :param time_last_role_changed:
            The value to assign to the time_last_role_changed property of this AutonomousDatabaseDataguardAssociation.
        :type time_last_role_changed: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'autonomous_database_id': 'str',
            'role': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'peer_role': 'str',
            'peer_autonomous_database_id': 'str',
            'peer_autonomous_database_life_cycle_state': 'str',
            'protection_mode': 'str',
            'apply_lag': 'str',
            'apply_rate': 'str',
            'is_automatic_failover_enabled': 'bool',
            'transport_lag': 'str',
            'time_last_synced': 'datetime',
            'time_created': 'datetime',
            'time_last_role_changed': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'autonomous_database_id': 'autonomousDatabaseId',
            'role': 'role',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'peer_role': 'peerRole',
            'peer_autonomous_database_id': 'peerAutonomousDatabaseId',
            'peer_autonomous_database_life_cycle_state': 'peerAutonomousDatabaseLifeCycleState',
            'protection_mode': 'protectionMode',
            'apply_lag': 'applyLag',
            'apply_rate': 'applyRate',
            'is_automatic_failover_enabled': 'isAutomaticFailoverEnabled',
            'transport_lag': 'transportLag',
            'time_last_synced': 'timeLastSynced',
            'time_created': 'timeCreated',
            'time_last_role_changed': 'timeLastRoleChanged'
        }

        self._id = None
        self._autonomous_database_id = None
        self._role = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._peer_role = None
        self._peer_autonomous_database_id = None
        self._peer_autonomous_database_life_cycle_state = None
        self._protection_mode = None
        self._apply_lag = None
        self._apply_rate = None
        self._is_automatic_failover_enabled = None
        self._transport_lag = None
        self._time_last_synced = None
        self._time_created = None
        self._time_last_role_changed = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutonomousDatabaseDataguardAssociation.
        The OCID of the Autonomous Dataguard created for Autonomous Container Database where given Autonomous Database resides in.


        :return: The id of this AutonomousDatabaseDataguardAssociation.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutonomousDatabaseDataguardAssociation.
        The OCID of the Autonomous Dataguard created for Autonomous Container Database where given Autonomous Database resides in.


        :param id: The id of this AutonomousDatabaseDataguardAssociation.
        :type: str
        """
        self._id = id

    @property
    def autonomous_database_id(self):
        """
        **[Required]** Gets the autonomous_database_id of this AutonomousDatabaseDataguardAssociation.
        The `OCID`__ of the Autonomous Database that has a relationship with the peer Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The autonomous_database_id of this AutonomousDatabaseDataguardAssociation.
        :rtype: str
        """
        return self._autonomous_database_id

    @autonomous_database_id.setter
    def autonomous_database_id(self, autonomous_database_id):
        """
        Sets the autonomous_database_id of this AutonomousDatabaseDataguardAssociation.
        The `OCID`__ of the Autonomous Database that has a relationship with the peer Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param autonomous_database_id: The autonomous_database_id of this AutonomousDatabaseDataguardAssociation.
        :type: str
        """
        self._autonomous_database_id = autonomous_database_id

    @property
    def role(self):
        """
        **[Required]** Gets the role of this AutonomousDatabaseDataguardAssociation.
        The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

        Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this AutonomousDatabaseDataguardAssociation.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this AutonomousDatabaseDataguardAssociation.
        The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.


        :param role: The role of this AutonomousDatabaseDataguardAssociation.
        :type: str
        """
        allowed_values = ["PRIMARY", "STANDBY", "DISABLED_STANDBY"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutonomousDatabaseDataguardAssociation.
        The current state of Autonomous Data Guard.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ROLE_CHANGE_IN_PROGRESS", "TERMINATING", "TERMINATED", "FAILED", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AutonomousDatabaseDataguardAssociation.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutonomousDatabaseDataguardAssociation.
        The current state of Autonomous Data Guard.


        :param lifecycle_state: The lifecycle_state of this AutonomousDatabaseDataguardAssociation.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "ROLE_CHANGE_IN_PROGRESS", "TERMINATING", "TERMINATED", "FAILED", "UNAVAILABLE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AutonomousDatabaseDataguardAssociation.
        Additional information about the current lifecycleState, if available.


        :return: The lifecycle_details of this AutonomousDatabaseDataguardAssociation.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AutonomousDatabaseDataguardAssociation.
        Additional information about the current lifecycleState, if available.


        :param lifecycle_details: The lifecycle_details of this AutonomousDatabaseDataguardAssociation.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def peer_role(self):
        """
        **[Required]** Gets the peer_role of this AutonomousDatabaseDataguardAssociation.
        The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

        Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The peer_role of this AutonomousDatabaseDataguardAssociation.
        :rtype: str
        """
        return self._peer_role

    @peer_role.setter
    def peer_role(self, peer_role):
        """
        Sets the peer_role of this AutonomousDatabaseDataguardAssociation.
        The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.


        :param peer_role: The peer_role of this AutonomousDatabaseDataguardAssociation.
        :type: str
        """
        allowed_values = ["PRIMARY", "STANDBY", "DISABLED_STANDBY"]
        if not value_allowed_none_or_none_sentinel(peer_role, allowed_values):
            peer_role = 'UNKNOWN_ENUM_VALUE'
        self._peer_role = peer_role

    @property
    def peer_autonomous_database_id(self):
        """
        Gets the peer_autonomous_database_id of this AutonomousDatabaseDataguardAssociation.
        The `OCID`__ of the peer Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The peer_autonomous_database_id of this AutonomousDatabaseDataguardAssociation.
        :rtype: str
        """
        return self._peer_autonomous_database_id

    @peer_autonomous_database_id.setter
    def peer_autonomous_database_id(self, peer_autonomous_database_id):
        """
        Sets the peer_autonomous_database_id of this AutonomousDatabaseDataguardAssociation.
        The `OCID`__ of the peer Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param peer_autonomous_database_id: The peer_autonomous_database_id of this AutonomousDatabaseDataguardAssociation.
        :type: str
        """
        self._peer_autonomous_database_id = peer_autonomous_database_id

    @property
    def peer_autonomous_database_life_cycle_state(self):
        """
        Gets the peer_autonomous_database_life_cycle_state of this AutonomousDatabaseDataguardAssociation.
        The current state of Autonomous Data Guard.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "ROLE_CHANGE_IN_PROGRESS", "TERMINATING", "TERMINATED", "FAILED", "UNAVAILABLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The peer_autonomous_database_life_cycle_state of this AutonomousDatabaseDataguardAssociation.
        :rtype: str
        """
        return self._peer_autonomous_database_life_cycle_state

    @peer_autonomous_database_life_cycle_state.setter
    def peer_autonomous_database_life_cycle_state(self, peer_autonomous_database_life_cycle_state):
        """
        Sets the peer_autonomous_database_life_cycle_state of this AutonomousDatabaseDataguardAssociation.
        The current state of Autonomous Data Guard.


        :param peer_autonomous_database_life_cycle_state: The peer_autonomous_database_life_cycle_state of this AutonomousDatabaseDataguardAssociation.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "ROLE_CHANGE_IN_PROGRESS", "TERMINATING", "TERMINATED", "FAILED", "UNAVAILABLE"]
        if not value_allowed_none_or_none_sentinel(peer_autonomous_database_life_cycle_state, allowed_values):
            peer_autonomous_database_life_cycle_state = 'UNKNOWN_ENUM_VALUE'
        self._peer_autonomous_database_life_cycle_state = peer_autonomous_database_life_cycle_state

    @property
    def protection_mode(self):
        """
        Gets the protection_mode of this AutonomousDatabaseDataguardAssociation.
        The protection mode of this Data Guard association. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000

        Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protection_mode of this AutonomousDatabaseDataguardAssociation.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """
        Sets the protection_mode of this AutonomousDatabaseDataguardAssociation.
        The protection mode of this Data Guard association. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000


        :param protection_mode: The protection_mode of this AutonomousDatabaseDataguardAssociation.
        :type: str
        """
        allowed_values = ["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE"]
        if not value_allowed_none_or_none_sentinel(protection_mode, allowed_values):
            protection_mode = 'UNKNOWN_ENUM_VALUE'
        self._protection_mode = protection_mode

    @property
    def apply_lag(self):
        """
        Gets the apply_lag of this AutonomousDatabaseDataguardAssociation.
        The lag time between updates to the primary database and application of the redo data on the standby database,
        as computed by the reporting database.

        Example: `9 seconds`


        :return: The apply_lag of this AutonomousDatabaseDataguardAssociation.
        :rtype: str
        """
        return self._apply_lag

    @apply_lag.setter
    def apply_lag(self, apply_lag):
        """
        Sets the apply_lag of this AutonomousDatabaseDataguardAssociation.
        The lag time between updates to the primary database and application of the redo data on the standby database,
        as computed by the reporting database.

        Example: `9 seconds`


        :param apply_lag: The apply_lag of this AutonomousDatabaseDataguardAssociation.
        :type: str
        """
        self._apply_lag = apply_lag

    @property
    def apply_rate(self):
        """
        Gets the apply_rate of this AutonomousDatabaseDataguardAssociation.
        The rate at which redo logs are synced between the associated databases.

        Example: `180 Mb per second`


        :return: The apply_rate of this AutonomousDatabaseDataguardAssociation.
        :rtype: str
        """
        return self._apply_rate

    @apply_rate.setter
    def apply_rate(self, apply_rate):
        """
        Sets the apply_rate of this AutonomousDatabaseDataguardAssociation.
        The rate at which redo logs are synced between the associated databases.

        Example: `180 Mb per second`


        :param apply_rate: The apply_rate of this AutonomousDatabaseDataguardAssociation.
        :type: str
        """
        self._apply_rate = apply_rate

    @property
    def is_automatic_failover_enabled(self):
        """
        Gets the is_automatic_failover_enabled of this AutonomousDatabaseDataguardAssociation.
        Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association


        :return: The is_automatic_failover_enabled of this AutonomousDatabaseDataguardAssociation.
        :rtype: bool
        """
        return self._is_automatic_failover_enabled

    @is_automatic_failover_enabled.setter
    def is_automatic_failover_enabled(self, is_automatic_failover_enabled):
        """
        Sets the is_automatic_failover_enabled of this AutonomousDatabaseDataguardAssociation.
        Indicates whether Automatic Failover is enabled for Autonomous Container Database Dataguard Association


        :param is_automatic_failover_enabled: The is_automatic_failover_enabled of this AutonomousDatabaseDataguardAssociation.
        :type: bool
        """
        self._is_automatic_failover_enabled = is_automatic_failover_enabled

    @property
    def transport_lag(self):
        """
        Gets the transport_lag of this AutonomousDatabaseDataguardAssociation.
        The approximate number of seconds of redo data not yet available on the standby Autonomous Container Database,
        as computed by the reporting database.

        Example: `7 seconds`


        :return: The transport_lag of this AutonomousDatabaseDataguardAssociation.
        :rtype: str
        """
        return self._transport_lag

    @transport_lag.setter
    def transport_lag(self, transport_lag):
        """
        Sets the transport_lag of this AutonomousDatabaseDataguardAssociation.
        The approximate number of seconds of redo data not yet available on the standby Autonomous Container Database,
        as computed by the reporting database.

        Example: `7 seconds`


        :param transport_lag: The transport_lag of this AutonomousDatabaseDataguardAssociation.
        :type: str
        """
        self._transport_lag = transport_lag

    @property
    def time_last_synced(self):
        """
        Gets the time_last_synced of this AutonomousDatabaseDataguardAssociation.
        The date and time of the last update to the apply lag, apply rate, and transport lag values.


        :return: The time_last_synced of this AutonomousDatabaseDataguardAssociation.
        :rtype: datetime
        """
        return self._time_last_synced

    @time_last_synced.setter
    def time_last_synced(self, time_last_synced):
        """
        Sets the time_last_synced of this AutonomousDatabaseDataguardAssociation.
        The date and time of the last update to the apply lag, apply rate, and transport lag values.


        :param time_last_synced: The time_last_synced of this AutonomousDatabaseDataguardAssociation.
        :type: datetime
        """
        self._time_last_synced = time_last_synced

    @property
    def time_created(self):
        """
        Gets the time_created of this AutonomousDatabaseDataguardAssociation.
        The date and time the Data Guard association was created.


        :return: The time_created of this AutonomousDatabaseDataguardAssociation.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AutonomousDatabaseDataguardAssociation.
        The date and time the Data Guard association was created.


        :param time_created: The time_created of this AutonomousDatabaseDataguardAssociation.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_last_role_changed(self):
        """
        Gets the time_last_role_changed of this AutonomousDatabaseDataguardAssociation.
        The date and time when the last role change action happened.


        :return: The time_last_role_changed of this AutonomousDatabaseDataguardAssociation.
        :rtype: datetime
        """
        return self._time_last_role_changed

    @time_last_role_changed.setter
    def time_last_role_changed(self, time_last_role_changed):
        """
        Sets the time_last_role_changed of this AutonomousDatabaseDataguardAssociation.
        The date and time when the last role change action happened.


        :param time_last_role_changed: The time_last_role_changed of this AutonomousDatabaseDataguardAssociation.
        :type: datetime
        """
        self._time_last_role_changed = time_last_role_changed

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
